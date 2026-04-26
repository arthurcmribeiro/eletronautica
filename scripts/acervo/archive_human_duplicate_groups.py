from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent

if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.append(str(SCRIPTS_ROOT))

from vault_tools import ROOT  # noqa: E402


STAGING_ROOT = (
    ROOT
    / "90_Revisao_Manual"
    / "_Acervo_Local"
    / "Acervo do humano"
    / "10_Tecnico_Nautico"
)
ARCHIVE_ROOT = (
    ROOT
    / "90_Revisao_Manual"
    / "_Acervo_Local"
    / "Acervo do humano"
    / "_Arquivados_Duplicatas_Resolvidas"
    / "10_Tecnico_Nautico"
)
DUPLICATE_JSON_PATH = ROOT / "manifest" / "acervo-humano-duplicates.json"
ARCHIVE_JSON_PATH = ROOT / "manifest" / "acervo-humano-duplicates-archived.json"
ARCHIVE_NOTE_PATH = (
    ROOT
    / "90_Revisao_Manual"
    / "10_Indices_e_Paineis"
    / "Acervo Humano Tecnico - Arquivo de Duplicatas Resolvidas.md"
)


@dataclass(frozen=True, slots=True)
class ArchiveAction:
    sha256: str
    priority: str
    canonical_relative: str
    source_relative: str
    archive_relative: str
    bucket: str
    status: str


def load_manifest() -> dict[str, object]:
    return json.loads(DUPLICATE_JSON_PATH.read_text(encoding="utf-8"))


def windows_extended_path(path: Path) -> str:
    raw = str(path.resolve())
    if os.name != "nt":
        return raw
    if raw.startswith("\\\\?\\"):
        return raw
    if raw.startswith("\\\\"):
        return "\\\\?\\UNC\\" + raw[2:]
    return "\\\\?\\" + raw


def render_archive_note(actions: list[ArchiveAction], reviewed_on: str) -> str:
    grouped: dict[str, list[ArchiveAction]] = {}
    for action in actions:
        grouped.setdefault(action.sha256, []).append(action)

    status_counter = Counter(action.status for action in actions)
    priority_counter = Counter(action.priority for action in actions)

    lines: list[str] = [
        "---",
        'title: "Acervo Humano Tecnico - Arquivo de Duplicatas Resolvidas"',
        'note_type: "index"',
        'domain: "90_Revisao_Manual"',
        'status: "auto-generated"',
        f'reviewed_on: "{reviewed_on}"',
        'review_jurisdiction: "Brasil"',
        "---",
        "",
        "# Acervo Humano Tecnico - Arquivo de Duplicatas Resolvidas",
        "",
        "> [!abstract] Resumo tecnico",
        "> Registro operacional das duplicatas arquivadas fora do staging ativo para reduzir ruido sem perder rastreabilidade.",
        "",
        "## Panorama geral",
        "",
        f"- acoes registradas: `{len(actions)}`",
        f"- movidas nesta rodada: `{status_counter.get('moved', 0)}`",
        f"- ja arquivadas anteriormente: `{status_counter.get('already-archived', 0)}`",
        f"- ausentes no staging no momento da rodada: `{status_counter.get('missing-source', 0)}`",
        f"- prioridade alta resolvida nesta rodada: `{priority_counter.get('alta', 0)}`",
        f"- prioridade media resolvida nesta rodada: `{priority_counter.get('media', 0)}`",
        f"- prioridade baixa resolvida nesta rodada: `{priority_counter.get('baixa', 0)}`",
        f"- atualizacao: `{reviewed_on}`",
        "",
    ]

    for index, (sha256, group_actions) in enumerate(sorted(grouped.items()), start=1):
        sample = group_actions[0]
        lines.extend(
            [
                f"## Grupo arquivado {index:02d}",
                "",
                f"- hash: `{sha256}`",
                f"- prioridade original: `{sample.priority}`",
                f"- bucket canonico mantido: `{sample.bucket}`",
                f"- arquivo canonico mantido no staging: `{sample.canonical_relative}`",
                f"- excedentes tratados nesta rodada: `{len(group_actions)}`",
                "",
                "### Itens tratados",
                "",
            ]
        )
        for action in group_actions:
            lines.append(
                f"- `{action.status}`: `{action.source_relative}` -> `{action.archive_relative}`"
            )
        lines.append("")

    return "\n".join(lines)


def write_json(payload: dict[str, object]) -> None:
    ARCHIVE_JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARCHIVE_JSON_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )


def write_note(content: str) -> None:
    ARCHIVE_NOTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARCHIVE_NOTE_PATH.write_text(content, encoding="utf-8", newline="\n")


def archive_groups(*, priorities: set[str], dry_run: bool) -> list[ArchiveAction]:
    payload = load_manifest()
    groups = payload.get("groups", [])
    actions: list[ArchiveAction] = []

    for group in groups:
        priority = str(group.get("priority", ""))
        if priority not in priorities:
            continue

        sha256 = str(group["sha256"])
        canonical_relative = str(group["canonical_relative"])
        bucket = str(group["bucket"])
        members = [str(member) for member in group.get("members", [])]

        for member in members:
            if member == canonical_relative:
                continue

            source_path = STAGING_ROOT / Path(member)
            archive_path = ARCHIVE_ROOT / Path(member)

            if source_path.exists():
                status = "planned" if dry_run else "moved"
                if not dry_run:
                    archive_path.parent.mkdir(parents=True, exist_ok=True)
                    if archive_path.exists():
                        raise FileExistsError(
                            f"Destino ja existe para duplicata arquivada: {archive_path}"
                        )
                    os.replace(
                        windows_extended_path(source_path),
                        windows_extended_path(archive_path),
                    )
            elif archive_path.exists():
                status = "already-archived"
            else:
                status = "missing-source"

            actions.append(
                ArchiveAction(
                    sha256=sha256,
                    priority=priority,
                    canonical_relative=canonical_relative,
                    source_relative=member,
                    archive_relative=archive_path.relative_to(ROOT).as_posix(),
                    bucket=bucket,
                    status=status,
                )
            )

    return actions


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Arquiva excedentes de grupos de duplicatas do staging tecnico humano."
    )
    parser.add_argument(
        "--priority",
        action="append",
        choices=("alta", "media", "baixa"),
        help="Prioridade dos grupos que deve ser tratada. Pode ser repetido.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Apenas mostra o que seria arquivado, sem mover arquivos.",
    )
    args = parser.parse_args()

    priorities = set(args.priority or ["alta"])
    actions = archive_groups(priorities=priorities, dry_run=args.dry_run)
    reviewed_on = date.today().isoformat()

    print(f"Prioridades tratadas: {', '.join(sorted(priorities))}")
    print(f"Acoes previstas/registradas: {len(actions)}")
    for status, count in sorted(Counter(action.status for action in actions).items()):
        print(f"- {status}: {count}")

    if args.dry_run:
        for action in actions[:40]:
            print(f"* {action.source_relative} -> {action.archive_relative} [{action.status}]")
        return 0

    note_content = render_archive_note(actions, reviewed_on)
    write_note(note_content)
    write_json(
        {
            "reviewed_on": reviewed_on,
            "priorities": sorted(priorities),
            "action_count": len(actions),
            "status_counts": Counter(action.status for action in actions),
            "actions": [
                {
                    "sha256": action.sha256,
                    "priority": action.priority,
                    "bucket": action.bucket,
                    "canonical_relative": action.canonical_relative,
                    "source_relative": action.source_relative,
                    "archive_relative": action.archive_relative,
                    "status": action.status,
                }
                for action in actions
            ],
        }
    )
    print(f"Nota de arquivo: {ARCHIVE_NOTE_PATH.relative_to(ROOT).as_posix()}")
    print(f"Manifesto JSON: {ARCHIVE_JSON_PATH.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
