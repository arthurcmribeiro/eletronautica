from __future__ import annotations

import hashlib
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent

if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.append(str(SCRIPTS_ROOT))

from vault_tools import ROOT, write_json  # noqa: E402


ACERVO_ROOT = ROOT / "90_Revisao_Manual" / "_Acervo_Local"
INDEX_JSON_PATH = ACERVO_ROOT / "acervo-local-index.json"
INDEX_NOTE_PATH = (
    ROOT
    / "90_Revisao_Manual"
    / "10_Indices_e_Paineis"
    / "Acervo Local — Índice Gerado.md"
)
DOC_EXTENSIONS = {".pdf"}
EXCLUDED_PREFIXES = {
    "Acervo do humano/",
}


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def human_size(size_bytes: int) -> str:
    size = float(size_bytes)
    units = ["B", "KB", "MB", "GB"]
    for unit in units:
        if size < 1024 or unit == units[-1]:
            if unit == "B":
                return f"{int(size)} {unit}"
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size_bytes} B"


def document_files() -> list[Path]:
    return sorted(
        path
        for path in ACERVO_ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in DOC_EXTENSIONS
        and not any(
            path.relative_to(ACERVO_ROOT).as_posix().startswith(prefix)
            for prefix in EXCLUDED_PREFIXES
        )
    )


def build_entries(paths: list[Path]) -> list[dict[str, str | int]]:
    entries: list[dict[str, str | int]] = []
    for path in paths:
        relative_to_acervo = path.relative_to(ACERVO_ROOT)
        parts = relative_to_acervo.parts
        system = parts[0] if len(parts) > 0 else ""
        brand = parts[1] if len(parts) > 1 else ""
        family = parts[2] if len(parts) > 2 else ""
        entries.append(
            {
                "file_name": path.name,
                "relative_path": path.relative_to(ROOT).as_posix(),
                "absolute_path": path.resolve().as_posix(),
                "system": system,
                "brand": brand,
                "family": family,
                "size_bytes": path.stat().st_size,
                "sha256": file_sha256(path),
            }
        )
    return entries


def build_markdown(entries: list[dict[str, str | int]]) -> str:
    generated_at = datetime.now(timezone.utc).isoformat()
    reviewed_on = datetime.now().date().isoformat()
    grouped: dict[str, dict[str, dict[str, list[dict[str, str | int]]]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(list))
    )

    for entry in entries:
        grouped[str(entry["system"])][str(entry["brand"])][str(entry["family"])].append(
            entry
        )

    brand_count = sum(len(grouped[system]) for system in grouped)
    family_count = sum(
        len(grouped[system][brand]) for system in grouped for brand in grouped[system]
    )

    lines = [
        "---",
        'title: "Acervo Local — Índice Gerado"',
        'note_type: "index"',
        'domain: "90_Revisao_Manual"',
        'status: "active-curation"',
        f'reviewed_on: "{reviewed_on}"',
        'review_jurisdiction: "Brasil"',
        "aliases:",
        '  - "Índice Gerado do Acervo Local"',
        '  - "Inventário Gerado do Acervo Local"',
        "related_notes:",
        '  - "Portal do Acervo — Biblioteca de Referência"',
        '  - "Acervo Local — README"',
        '  - "Acervo Local — Índice Inicial"',
        '  - "Tabela-Mestre do Acervo — Biblioteca de Referência"',
        "---",
        "",
        "# Acervo Local — Índice Gerado",
        "",
        "> [!abstract] Resumo técnico",
        "> Esta nota é gerada por script a partir do conteúdo real da pasta `_Acervo_Local`. Ela serve como inventário operacional do que já está salvo no disco.",
        "",
        "> [!info] Geração",
        "> Comando: `python scripts/acervo/build_local_index.py`.",
        f"> Gerado em `{generated_at}`.",
        "",
        "## Resumo",
        "",
        f"- arquivos documentais: `{len(entries)}`",
        f"- sistemas com conteúdo: `{len(grouped)}`",
        f"- marcas com conteúdo: `{brand_count}`",
        f"- famílias com conteúdo: `{family_count}`",
    ]

    if not entries:
        lines.extend(["", "## Estado atual", "", "- nenhum PDF foi encontrado no acervo local."])
        return "\n".join(lines) + "\n"

    for system in sorted(grouped):
        lines.extend(["", f"## {system}", ""])
        for brand in sorted(grouped[system]):
            for family in sorted(grouped[system][brand]):
                family_entries = sorted(
                    grouped[system][brand][family], key=lambda entry: str(entry["file_name"])
                )
                family_label = family or "(sem família)"
                lines.append(f"### {brand} — {family_label}")
                lines.append("")
                for entry in family_entries:
                    file_name = str(entry["file_name"])
                    absolute_path = str(entry["absolute_path"])
                    size_label = human_size(int(entry["size_bytes"]))
                    sha_short = str(entry["sha256"])[:12]
                    lines.append(
                        f"- [{file_name}](</{absolute_path}>) — `{size_label}` — `sha256 {sha_short}`"
                    )
                lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    paths = document_files()
    entries = build_entries(paths)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "file_count": len(entries),
        "files": entries,
    }
    write_json(INDEX_JSON_PATH, payload)
    INDEX_NOTE_PATH.write_text(build_markdown(entries), encoding="utf-8")
    print(f"Indice JSON gerado em: {INDEX_JSON_PATH}")
    print(f"Indice Markdown gerado em: {INDEX_NOTE_PATH}")


if __name__ == "__main__":
    main()
