from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent

if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.append(str(SCRIPTS_ROOT))

from vault_tools import ROOT  # noqa: E402
from pdf_text_tools import extract_pdf_text  # noqa: E402


TRIAGE_ROOT = (
    ROOT
    / "90_Revisao_Manual"
    / "_Acervo_Local"
    / "Acervo do humano"
    / "10_Tecnico_Nautico"
    / "90_Triagem_Tecnica_por_Codigo"
)

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}


@dataclass(frozen=True)
class Rule:
    destination: str
    keywords: tuple[str, ...]


RULES: tuple[Rule, ...] = (
    Rule(
        "01_Geradores_e_Motores_Base",
        (
            "rehlko",
            "kohler",
            "efkod",
            "ekod",
            "efkozd",
            "ekozd",
            "efozdj",
            "eozdj",
            "genset",
            "generator set",
            "generator",
            "onan",
            "cummins onan",
            "kubota",
            "d905",
            "d1105",
            "v1505",
            "v1305",
            "v1903",
            "v2203",
            "v2403",
            "v2803",
        ),
    ),
    Rule(
        "02_Navegacao_Comunicacao_e_Instrumentos",
        (
            "garmin",
            "ghc",
            "gpsmap",
            "gps 17x",
            "raymarine",
            "furuno",
            "simrad",
            "standard horizon",
            "intellian",
            "rs40",
            "hs40",
            "vhf",
            "nmea",
            "vdo",
            "clipper",
            "seatalk",
            "chartplotter",
            "autopilot",
            "smartpilot",
            "protouch",
        ),
    ),
    Rule(
        "03_Propulsao_Motores_e_Turbo",
        (
            "volvo penta",
            "volvo",
            "penta",
            "yanmar",
            "scania",
            "mpi",
            "marine engines",
            "turbocompressor",
            "turbocharger",
            "intercooler",
            "edc",
            "btdc",
            "th360b",
            "l70",
            "d72",
            "d74",
            "engine",
        ),
    ),
    Rule(
        "04_DC_Componentes_e_Controle",
        (
            "phoenix",
            "irfz",
            "smart volt amp",
            "volt amp",
            "pcwmvar",
            "pwm",
            "ata7340",
            "ab12210",
            "datasheet",
            "mosfet",
        ),
    ),
    Rule(
        "05_Bombas_Utilidades_e_Acessorios",
        (
            "jabsco",
            "pump",
            "chiaperini",
            "compressor",
            "searchlight",
            "halogen lamp",
            "docka",
            "ct165",
            "ct225",
            "pieces detachees",
            "quick",
            "siphon break",
        ),
    ),
    Rule(
        "06_Artigos_Normas_e_Referencia_Tecnica",
        (
            "artigo",
            "texto do artigo",
            "rbme",
            "thesis",
            "msc",
            "normas",
            "almanaque",
            "non-metallic",
            "materials brochure",
            "technical brochure",
            "rpmgf",
            "materials",
        ),
    ),
)

OUT_OF_SCOPE_PATTERNS = (
    "classificacao",
    "parecer-tecnico",
    "lisado-bacteriano",
    "tarifs",
    "tariffe",
    "edj",
    "cariacica",
    "reaciona",
    "booglee",
    "gennaro",
    "erogazioni",
    "condicoes_acesso",
)

IMAGE_NAME_PATTERNS = (
    "doc-",
    "img-",
    "screenshot",
    "corrected_image",
    "edited_image",
    "wa000",
    "wa0045",
)


def normalize(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    without_accents = "".join(
        character for character in normalized if not unicodedata.combining(character)
    )
    return without_accents.casefold()


def io_path(path: Path) -> str:
    resolved = str(path.resolve())
    if os.name != "nt" or resolved.startswith("\\\\?\\"):
        return resolved
    return f"\\\\?\\{resolved}"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_text(value: str) -> str:
    normalized = unicodedata.normalize("NFC", value)
    return normalized.encode("cp1252", errors="replace").decode("cp1252")


def content_blob(path: Path, cache: dict[Path, str]) -> str:
    cached = cache.get(path)
    if cached is not None:
        return cached

    blob = normalize(path.name)
    if path.suffix.lower() == ".pdf":
        extraction = extract_pdf_text(path, max_pages=2, timeout=15)
        if extraction.text:
            blob = f"{blob} {normalize(extraction.text)}"

    cache[path] = blob
    return blob


def classify(path: Path, cache: dict[Path, str]) -> str:
    normalized_name = normalize(path.name)
    suffix = path.suffix.lower()

    if suffix in IMAGE_EXTENSIONS or any(pattern in normalized_name for pattern in IMAGE_NAME_PATTERNS):
        return "07_Imagens_e_Recortes_Tecnicos"

    if any(pattern in normalized_name for pattern in OUT_OF_SCOPE_PATTERNS):
        return "99_Fora_do_Escopo_ou_Pessoal"

    blob = content_blob(path, cache)
    if any(pattern in blob for pattern in OUT_OF_SCOPE_PATTERNS):
        return "99_Fora_do_Escopo_ou_Pessoal"

    best_destination = "ZZ_Residual_Manual"
    best_score = 0

    for rule in RULES:
        score = sum(1 for keyword in rule.keywords if keyword in blob)
        if score > best_score:
            best_destination = rule.destination
            best_score = score

    return best_destination


def canonical_sort_key(path: Path) -> tuple[int, int, str]:
    normalized_name = normalize(path.name)
    duplicate_penalty = 1 if re.search(r"\(\d+\)", normalized_name) else 0
    return (duplicate_penalty, len(normalized_name), normalized_name)


def move_file(source: Path, target: Path, apply_changes: bool) -> str:
    if source == target:
        return "unchanged"

    if target.exists():
        if sha256(source) == sha256(target):
            if apply_changes:
                source.unlink()
                return "deduped"
            return "planned_duplicate"
        raise FileExistsError(f"Destino existente com conteudo diferente: {target}")

    if not apply_changes:
        return "planned"

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(io_path(source), io_path(target))
    return "moved"


def build_hash_groups(files: list[Path]) -> defaultdict[str, list[Path]]:
    groups: defaultdict[str, list[Path]] = defaultdict(list)
    total = len(files)
    for index, path in enumerate(files, start=1):
        print(safe_text(f"HASH {index:03d}/{total:03d}: {path.name}"))
        groups[sha256(path)].append(path)
    return groups


def organize(apply_changes: bool, *, limit: int | None = None) -> tuple[dict[str, int], Counter[str]]:
    cache: dict[Path, str] = {}
    files = sorted(path for path in TRIAGE_ROOT.iterdir() if path.is_file())
    if limit is not None:
        files = files[:limit]

    counters: Counter[str] = Counter()
    destination_counts: Counter[str] = Counter()

    if not files:
        return dict(counters), destination_counts

    by_hash = build_hash_groups(files)
    groups = list(by_hash.values())
    total_groups = len(groups)

    for group_index, group in enumerate(groups, start=1):
        canonical = sorted(group, key=canonical_sort_key)[0]
        print(safe_text(f"CLASSIFY {group_index:03d}/{total_groups:03d}: {canonical.name}"))
        destination = classify(canonical, cache)
        canonical_target = TRIAGE_ROOT / destination / canonical.name
        result = move_file(canonical, canonical_target, apply_changes)
        counters[result] += 1
        destination_counts[destination] += 1
        print(
            safe_text(
                f"{result.upper()}: {canonical.name} -> {canonical_target.relative_to(TRIAGE_ROOT).as_posix()}"
            )
        )

        duplicate_root = TRIAGE_ROOT / "98_Duplicatas" / destination
        for duplicate in sorted((path for path in group if path != canonical), key=canonical_sort_key):
            duplicate_target = duplicate_root / duplicate.name
            result = move_file(duplicate, duplicate_target, apply_changes)
            counters[result] += 1
            destination_counts[f"98_Duplicatas/{destination}"] += 1
            print(
                safe_text(
                    f"{result.upper()}: {duplicate.name} -> {duplicate_target.relative_to(TRIAGE_ROOT).as_posix()}"
                )
            )

    return dict(counters), destination_counts


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Organiza em massa a triagem tecnica por codigo em subpastas tematicas."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Move os arquivos de fato. Sem esta flag, apenas mostra o plano.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Processa apenas os primeiros N arquivos da raiz da triagem.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    counters, destination_counts = organize(apply_changes=args.apply, limit=args.limit)
    mode = "APLICADO" if args.apply else "DRY-RUN"

    print("")
    print(safe_text("Resumo por destino:"))
    for destination, count in sorted(destination_counts.items()):
        print(safe_text(f"- {destination}: {count}"))

    print("")
    print(f"Modo: {mode}")
    print(f"Arquivos movidos: {counters.get('moved', 0)}")
    print(f"Arquivos planejados: {counters.get('planned', 0)}")
    print(f"Duplicatas consolidadas: {counters.get('deduped', 0)}")
    print(f"Duplicatas planejadas: {counters.get('planned_duplicate', 0)}")
    print(f"Sem alteracao: {counters.get('unchanged', 0)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
