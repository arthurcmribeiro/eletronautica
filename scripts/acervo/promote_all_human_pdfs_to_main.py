from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent

if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.append(str(SCRIPTS_ROOT))

from vault_tools import ROOT  # noqa: E402


ACERVO_ROOT = ROOT / "90_Revisao_Manual" / "_Acervo_Local"
STAGING_ROOT = ACERVO_ROOT / "Acervo do humano" / "10_Tecnico_Nautico"
MANIFEST_PATH = ROOT / "manifest" / "acervo-humano-promoted-all-pdfs.json"
REPORT_PATH = ROOT / "_Editorial" / "Promocao Integral do Acervo Humano Tecnico.md"

PDF_EXTENSION = ".pdf"
SOURCE_PREFIX_FOR_MAIN_INDEX = "Acervo do humano/"
MAX_ABSOLUTE_PATH_LENGTH = 238

CATEGORY_SYSTEM_MAP = {
    "00_Documentacao_de_Campo_e_Clientes": "Campo-Clientes",
    "01_Geradores": "Geradores",
    "02_Climatizacao": "Climatizacao",
    "03_Baterias_e_DC": "Energia-DC",
    "04_Shore_Power_e_AC": "Shore-Power-AC",
    "05_Navegacao_e_Eletronicos": "Navegacao",
    "06_Bombas_Hidraulica_e_Utilidades": "Bombas-Utilidades",
    "07_Iluminacao_Sinalizacao_e_Acessorios": "Iluminacao-Acessorios",
    "08_Corrosao_Bonding_e_Seguranca": "Corrosao-Seguranca",
    "09_Propulsao_Motores_Estabilizacao_e_Atuacao": "Propulsao-Motores",
    "10_Materiais_Internos_e_Cursos": "Materiais-Internos",
    "11_HTML_Tecnico_Exportado": "HTML-Tecnico-Exportado",
}

SYSTEM_FALLBACK_BRAND = {
    "Bombas-Utilidades": "Referencia-Bombas-Utilidades",
    "Campo-Clientes": "Referencia-Campo",
    "Climatizacao": "Referencia-Climatizacao",
    "Corrosao-Seguranca": "Referencia-Corrosao-Seguranca",
    "Energia-DC": "Referencia-Energia-DC",
    "Geradores": "Referencia-Geradores",
    "HTML-Tecnico-Exportado": "Referencia-HTML",
    "Iluminacao-Acessorios": "Referencia-Iluminacao",
    "Materiais-Internos": "Referencia-Materiais-Internos",
    "Navegacao": "Referencia-Navegacao",
    "Propulsao-Motores": "Referencia-Propulsao",
    "Shore-Power-AC": "Referencia-Shore-Power",
}

BRAND_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("Cummins-Onan", ("cummins", "onan", "mdk", "hdk", "mcck", "energy command")),
    ("Rehlko-Kohler", ("rehlko", "kohler", "efkod", "ekod", "ekozd", "efkozd")),
    ("Fischer-Panda", ("fischer panda", "fischer", "panda")),
    ("Northern-Lights", ("northern lights", "northen lights", "northern")),
    ("Dometic", ("dometic", "cruisair", "marine air")),
    ("H-Tec", ("h-tec", "htec", "hfc acqua", "hfc-acqua")),
    ("Mabru", ("mabru",)),
    ("Victron", ("victron", "multiplus", "phoenix", "lynx smart")),
    ("Sterling-Power", ("sterling", "sterling power", "pro charge")),
    ("Usina", ("usina",)),
    ("BEP-Marine", ("bep", "bep marine")),
    ("Blue-Sea-Systems", ("blue sea", "bluesea")),
    ("Mastervolt", ("mastervolt",)),
    ("Raymarine", ("raymarine", "seatalk", "smartpilot", "quantum")),
    ("Garmin", ("garmin", "gpsmap", "ghc")),
    ("Furuno", ("furuno", "fi5002", "fi-5002")),
    ("Intellian", ("intellian",)),
    ("Standard-Horizon", ("standard horizon", "gx2000", "gx2150")),
    ("Simrad", ("simrad",)),
    ("VDO", ("vdo",)),
    ("Jabsco", ("jabsco",)),
    ("Whale", ("whale",)),
    ("Johnson-Pump", ("johnson pump",)),
    ("Quick", ("quick",)),
    ("Vetus", ("vetus",)),
    ("Marinco", ("marinco",)),
    ("Lumishore", ("lumishore",)),
    ("Volvo-Penta", ("volvo penta", "volvo")),
    ("Yanmar", ("yanmar",)),
    ("Scania", ("scania",)),
    ("Ultraflex", ("ultraflex",)),
    ("Curtis", ("curtis",)),
    ("Seakeeper", ("seakeeper",)),
    ("Zipwake", ("zipwake",)),
    ("Bennett", ("bennett",)),
)

FAMILY_STOPWORDS = {
    "ac",
    "air",
    "and",
    "catalog",
    "catalogo",
    "conditioner",
    "conditioners",
    "control",
    "controls",
    "data",
    "diagram",
    "doc",
    "document",
    "english",
    "file",
    "guide",
    "install",
    "installation",
    "instructions",
    "manual",
    "marine",
    "model",
    "models",
    "operation",
    "operator",
    "parts",
    "pdf",
    "price",
    "reference",
    "service",
    "spec",
    "specification",
    "specifications",
    "system",
    "systems",
    "technical",
    "the",
    "troubleshooting",
}


@dataclass(slots=True)
class PromotionRecord:
    source_path: Path
    source_relative: str
    target_path: Path
    target_relative: str
    status: str
    system: str
    brand: str
    family: str
    document_kind: str
    sha256: str
    size_bytes: int


def path_arg(path: Path) -> str:
    resolved = str(path.resolve())
    if os.name == "nt" and not resolved.startswith("\\\\?\\"):
        return "\\\\?\\" + resolved
    return resolved


def strip_long_prefix(value: str) -> str:
    if value.startswith("\\\\?\\UNC\\"):
        return "\\\\" + value[8:]
    if value.startswith("\\\\?\\"):
        return value[4:]
    return value


def iter_files_long(root: Path) -> list[Path]:
    files: list[Path] = []
    for dirpath, _dirnames, filenames in os.walk(path_arg(root)):
        for filename in filenames:
            files.append(Path(strip_long_prefix(os.path.join(dirpath, filename))))
    return sorted(files, key=lambda item: item.as_posix().casefold())


def safe_ascii(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    return normalized.encode("ascii", "ignore").decode("ascii")


def compact_text(value: str) -> str:
    return " ".join(safe_ascii(value).replace("_", " ").replace("-", " ").split()).lower()


def folder_slug(value: str, *, default: str, max_length: int = 80) -> str:
    ascii_value = safe_ascii(value)
    ascii_value = re.sub(r"[^A-Za-z0-9]+", "-", ascii_value).strip("-")
    ascii_value = re.sub(r"-{2,}", "-", ascii_value)
    if not ascii_value:
        ascii_value = default
    return ascii_value[:max_length].strip("-") or default


def file_slug(value: str, *, default: str, max_length: int = 120) -> str:
    return folder_slug(value.lower(), default=default, max_length=max_length).lower()


def target_file_slug(value: str, parent: Path, *, default: str = "documento") -> str:
    parent_length = len(str(parent.resolve()))
    max_length = MAX_ABSOLUTE_PATH_LENGTH - parent_length - len("\\") - len(PDF_EXTENSION)
    max_length = max(32, min(96, max_length))
    return file_slug(value, default=default, max_length=max_length)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path_arg(path), "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def collect_staging_files() -> tuple[list[Path], list[Path]]:
    files = iter_files_long(STAGING_ROOT)
    pdfs = [path for path in files if path.suffix.lower() == PDF_EXTENSION]
    non_pdfs = [path for path in files if path.suffix.lower() != PDF_EXTENSION]
    return pdfs, non_pdfs


def collect_existing_main_hashes() -> dict[str, Path]:
    hashes: dict[str, Path] = {}
    for path in iter_files_long(ACERVO_ROOT):
        if path.suffix.lower() != PDF_EXTENSION:
            continue
        relative = path.relative_to(ACERVO_ROOT).as_posix()
        if relative.startswith(SOURCE_PREFIX_FOR_MAIN_INDEX):
            continue
        file_hash = sha256(path)
        hashes.setdefault(file_hash, path)
    return hashes


def source_category(source: Path) -> str:
    relative = source.relative_to(STAGING_ROOT)
    return relative.parts[0] if relative.parts else "00_Sem_Categoria"


def target_system(source: Path) -> str:
    return CATEGORY_SYSTEM_MAP.get(source_category(source), "Complementar-Brasil")


def detect_brand(source: Path, system: str) -> str:
    relative = source.relative_to(STAGING_ROOT).as_posix()
    haystack = compact_text(relative)
    for brand, signals in BRAND_RULES:
        if any(signal in haystack for signal in signals):
            return brand
    return SYSTEM_FALLBACK_BRAND.get(system, "Referencia-Tecnica")


def detect_document_kind(stem: str) -> str:
    lowered = compact_text(stem)
    if "service manual" in lowered:
        return "service-manual"
    if "parts manual" in lowered or "spare parts" in lowered or "catalogo pecas" in lowered:
        return "parts-manual"
    if (
        "installation manual" in lowered
        or "install manual" in lowered
        or "install en" in lowered
        or "supplemental instructions" in lowered
    ):
        return "installation-manual"
    if (
        "operator manual" in lowered
        or "operation manual" in lowered
        or "owners manual" in lowered
        or "user manual" in lowered
    ):
        return "operation-manual"
    if "troubleshooting" in lowered:
        return "troubleshooting-guide"
    if "price list" in lowered or "catalog" in lowered or "catalogo" in lowered:
        return "catalog-brochure"
    if "wiring" in lowered or "diagram" in lowered or "cutout" in lowered or "cabling" in lowered:
        return "documento-tecnico"
    if "spec" in lowered or "data sheet" in lowered or "datasheet" in lowered:
        return "technical-reference"
    if "manual" in lowered:
        return "technical-reference"
    return "technical-reference"


def model_candidates(text: str) -> list[str]:
    ascii_text = safe_ascii(text).upper()
    tokens = re.findall(r"\b[A-Z0-9][A-Z0-9./-]{2,}\b", ascii_text)
    results: list[str] = []
    seen: set[str] = set()
    for raw in tokens:
        cleaned = raw.strip("-_./")
        key = cleaned.casefold()
        if key in seen:
            continue
        seen.add(key)

        lowered = cleaned.lower()
        letter_count = sum(char.isalpha() for char in cleaned)
        digit_count = sum(char.isdigit() for char in cleaned)
        if lowered in FAMILY_STOPWORDS:
            continue
        if len(cleaned) < 3 or len(cleaned) > 28:
            continue
        if letter_count < 2:
            continue
        if digit_count == 0 and "-" not in cleaned and "/" not in cleaned:
            continue
        results.append(cleaned)
        if len(results) >= 4:
            break
    return results


def fallback_family_from_stem(stem: str) -> str:
    words = [
        word
        for word in re.split(r"[^A-Za-z0-9]+", safe_ascii(stem))
        if len(word) >= 3 and word.lower() not in FAMILY_STOPWORDS
    ]
    if not words:
        return "Geral"
    return "-".join(words[:5])


def detect_family(source: Path, brand: str) -> str:
    relative = source.relative_to(STAGING_ROOT)
    text_parts = [source.stem]
    text_parts.extend(part for part in relative.parts[:-1] if not part[:2].isdigit())
    text = " ".join(text_parts)
    candidates = model_candidates(text)
    if candidates:
        return folder_slug("-".join(candidates[:2]), default="Geral", max_length=70)

    parent = relative.parent.name if relative.parent != Path(".") else ""
    if parent and parent != source_category(source) and not parent[:2].isdigit():
        return folder_slug(parent, default="Geral", max_length=70)

    if brand.startswith("Referencia-"):
        return folder_slug(fallback_family_from_stem(source.stem), default="Geral", max_length=70)
    return "Geral"


def build_target_path(source: Path, file_hash: str) -> tuple[Path, str, str, str, str]:
    system = target_system(source)
    brand = detect_brand(source, system)
    family = detect_family(source, brand)
    document_kind = detect_document_kind(source.stem)

    brand_folder = folder_slug(brand, default="Referencia-Tecnica", max_length=28)
    family_folder = folder_slug(family, default="Geral", max_length=24)
    target_parent = ACERVO_ROOT / system / brand_folder / family_folder
    target_name = f"{target_file_slug(source.stem, target_parent)}.pdf"
    target_path = target_parent / target_name
    return target_path, system, brand_folder, family_folder, document_kind


def choose_unique_target(target: Path, source_hash: str) -> Path:
    if not target.exists():
        return target
    if sha256(target) == source_hash:
        return target

    stem = target.stem
    suffix = target.suffix
    for index in range(2, 100):
        candidate = target.with_name(f"{stem}-{index}{suffix}")
        if not candidate.exists():
            return candidate
        if sha256(candidate) == source_hash:
            return candidate
    raise FileExistsError(f"Nao foi possivel criar destino unico para {target}")


def copy_pdf(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path_arg(source), path_arg(target))


def build_records(apply_changes: bool) -> tuple[list[PromotionRecord], list[Path]]:
    pdfs, non_pdfs = collect_staging_files()
    existing_hashes = collect_existing_main_hashes()
    records: list[PromotionRecord] = []

    for source in pdfs:
        source_hash = sha256(source)
        existing = existing_hashes.get(source_hash)

        target_path, system, brand, family, document_kind = build_target_path(source, source_hash)
        status = "planned"
        final_target = target_path

        if existing:
            status = "already-present"
            final_target = existing
        else:
            final_target = choose_unique_target(target_path, source_hash)
            if apply_changes:
                copy_pdf(source, final_target)
                existing_hashes[source_hash] = final_target
                status = "copied"

        size_bytes = os.path.getsize(path_arg(source))
        records.append(
            PromotionRecord(
                source_path=source,
                source_relative=source.relative_to(STAGING_ROOT).as_posix(),
                target_path=final_target,
                target_relative=final_target.relative_to(ACERVO_ROOT).as_posix(),
                status=status,
                system=system,
                brand=brand,
                family=family,
                document_kind=document_kind,
                sha256=source_hash,
                size_bytes=size_bytes,
            )
        )

    return records, non_pdfs


def render_report(records: list[PromotionRecord], non_pdfs: list[Path], *, applied: bool) -> str:
    generated_at = datetime.now(timezone.utc).isoformat()
    reviewed_on = datetime.now().date().isoformat()
    status_counts = Counter(record.status for record in records)
    system_counts = Counter(record.system for record in records)
    category_counts = Counter(record.source_relative.split("/", 1)[0] for record in records)
    non_pdf_counts = Counter(path.suffix.lower() or "(sem-extensao)" for path in non_pdfs)

    lines = [
        "---",
        'title: "Promocao Integral do Acervo Humano Tecnico"',
        'note_type: "audit"',
        'domain: "90_Revisao_Manual"',
        'status: "active-curation"',
        f'reviewed_on: "{reviewed_on}"',
        'review_jurisdiction: "Brasil"',
        "aliases:",
        '  - "Promocao Integral PDF do Acervo Humano"',
        '  - "Promocao em Massa do Acervo Humano Tecnico"',
        "related_notes:",
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Local - Indice Gerado"',
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado"',
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Indice Gerado"',
        "---",
        "",
        "# Promocao Integral do Acervo Humano Tecnico",
        "",
        "> [!abstract] Resumo tecnico",
        "> Esta auditoria registra a promocao em massa dos PDFs tecnicos do staging humano para o acervo principal PDF-first.",
        "> Os originais foram preservados no staging para rastreabilidade; arquivos HTML e imagens ficam em fila separada de conversao/normalizacao.",
        "",
        "## Escopo",
        "",
        f"- modo: `{'aplicado' if applied else 'dry-run'}`",
        f"- gerado em UTC: `{generated_at}`",
        f"- PDFs tecnicos avaliados: `{len(records)}`",
        f"- PDFs copiados agora: `{status_counts.get('copied', 0)}`",
        f"- PDFs ja presentes por hash no acervo principal: `{status_counts.get('already-present', 0)}`",
        f"- PDFs planejados em dry-run: `{status_counts.get('planned', 0)}`",
        f"- arquivos nao-PDF mantidos no staging: `{len(non_pdfs)}`",
        "",
        "## Distribuicao por sistema de destino",
        "",
    ]

    for system, count in sorted(system_counts.items()):
        lines.append(f"- `{system}`: `{count}` PDFs")

    lines.extend(["", "## Distribuicao por bucket de origem", ""])
    for category, count in sorted(category_counts.items()):
        lines.append(f"- `{category}`: `{count}` PDFs")

    lines.extend(["", "## Arquivos nao-PDF pendentes", ""])
    if non_pdf_counts:
        for extension, count in sorted(non_pdf_counts.items()):
            lines.append(f"- `{extension}`: `{count}` arquivos")
    else:
        lines.append("- nenhum arquivo nao-PDF pendente")

    lines.extend(
        [
            "",
            "## Regra operacional",
            "",
            "- PDFs sao promovidos para `Sistema/Marca/Familia/arquivo.pdf`, que e o padrao exigido pelo acervo principal e pela camada de notas companheiras.",
            "- O nome do arquivo preserva o titulo original limpo para leitura humana; SHA-256 e origem ficam no manifesto e nas notas, nao no nome do PDF.",
            "- O script evita duplicacao por hash: se o PDF ja existe no acervo principal, ele registra `already-present` em vez de copiar outra vez.",
            "- HTML, JPG, JPEG e PNG nao foram misturados ao acervo principal porque ainda precisam de conversao para PDF, captura limpa ou nota tecnica curada.",
            "",
            "## Promocoes registradas",
            "",
        ]
    )

    for record in sorted(records, key=lambda item: item.source_relative.casefold()):
        lines.append(
            "- "
            f"`{record.status}` | `{record.source_relative}` -> "
            f"`{record.target_relative}` | `{record.sha256[:12]}`"
        )

    lines.extend(
        [
            "",
            "## Proxima fila sugerida",
            "",
            "- converter HTML tecnico exportado para PDF arquivado e/ou nota Markdown curada quando o conteudo for fonte primaria util",
            "- transformar imagens avulsas em anexos documentados ou descartar duplicatas visuais sem valor tecnico",
            "- rodar novamente a pipeline de OCR para os PDFs promovidos com baixa extracao textual",
            "",
        ]
    )
    return "\n".join(lines)


def write_outputs(records: list[PromotionRecord], non_pdfs: list[Path], *, applied: bool) -> None:
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    payload: dict[str, Any] = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "applied": applied,
        "staging_root": STAGING_ROOT.relative_to(ROOT).as_posix(),
        "acervo_root": ACERVO_ROOT.relative_to(ROOT).as_posix(),
        "pdf_count": len(records),
        "non_pdf_count": len(non_pdfs),
        "status_counts": dict(Counter(record.status for record in records)),
        "system_counts": dict(Counter(record.system for record in records)),
        "non_pdf_extension_counts": dict(
            Counter(path.suffix.lower() or "(sem-extensao)" for path in non_pdfs)
        ),
        "records": [
            {
                "source": record.source_relative,
                "target": record.target_relative,
                "status": record.status,
                "system": record.system,
                "brand": record.brand,
                "family": record.family,
                "document_kind": record.document_kind,
                "sha256": record.sha256,
                "size_bytes": record.size_bytes,
            }
            for record in records
        ],
        "non_pdf_pending": [
            path.relative_to(STAGING_ROOT).as_posix()
            for path in sorted(non_pdfs, key=lambda item: item.as_posix().casefold())
        ],
    }
    MANIFEST_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    REPORT_PATH.write_text(render_report(records, non_pdfs, applied=applied), encoding="utf-8", newline="\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Promove todos os PDFs tecnicos do staging humano para o acervo principal."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Copia os PDFs para o acervo principal. Sem esta flag, executa dry-run.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    records, non_pdfs = build_records(apply_changes=args.apply)
    write_outputs(records, non_pdfs, applied=args.apply)

    counts = Counter(record.status for record in records)
    mode = "APLICADO" if args.apply else "DRY-RUN"
    print(f"Modo: {mode}")
    print(f"PDFs avaliados: {len(records)}")
    print(f"PDFs copiados: {counts.get('copied', 0)}")
    print(f"PDFs ja presentes: {counts.get('already-present', 0)}")
    print(f"PDFs planejados: {counts.get('planned', 0)}")
    print(f"Nao-PDF pendentes: {len(non_pdfs)}")
    print(f"Manifesto: {MANIFEST_PATH.relative_to(ROOT).as_posix()}")
    print(f"Relatorio: {REPORT_PATH.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
