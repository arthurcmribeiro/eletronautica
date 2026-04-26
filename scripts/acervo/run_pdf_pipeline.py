from __future__ import annotations

import argparse
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent

if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.append(str(SCRIPTS_ROOT))

from vault_tools import ROOT, write_json  # noqa: E402


REPORT_PATH = ROOT / "_Editorial" / "Pipeline PDF - Ultima Execucao.md"
MANIFEST_PATH = ROOT / "manifest" / "pdf-pipeline-last-run.json"


@dataclass(slots=True)
class PipelineStep:
    name: str
    command: list[str]
    enabled: bool = True


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def command_line(command: list[str]) -> str:
    return subprocess.list2cmdline(command)


def run_step(step: PipelineStep, *, dry_run: bool) -> dict[str, object]:
    started = datetime.now(timezone.utc)
    start_time = time.perf_counter()
    result = {
        "name": step.name,
        "command": command_line(step.command),
        "started_at": started.isoformat(),
        "duration_seconds": 0.0,
        "returncode": 0,
        "status": "skipped" if not step.enabled else "pending",
    }

    if not step.enabled:
        print(f"[skip] {step.name}")
        return result

    print("")
    print(f"==> {step.name}")
    print(command_line(step.command))

    if dry_run:
        result["status"] = "dry-run"
        result["duration_seconds"] = round(time.perf_counter() - start_time, 3)
        return result

    completed = subprocess.run(step.command, cwd=ROOT)
    result["returncode"] = completed.returncode
    result["duration_seconds"] = round(time.perf_counter() - start_time, 3)
    result["status"] = "ok" if completed.returncode == 0 else "failed"
    return result


def build_steps(args: argparse.Namespace) -> list[PipelineStep]:
    python = sys.executable

    audit_command = [
        python,
        "scripts/acervo/audit_pdf_toolchain.py",
        "--scope",
        args.audit_scope,
        "--ocr-sample-limit",
        str(args.ocr_sample_limit),
    ]
    if args.fast_audit:
        audit_command.extend(["--skip-qpdf", "--max-text-pages", "1"])
    if args.max_audit_files:
        audit_command.extend(["--max-files", str(args.max_audit_files)])

    ocr_command = [
        python,
        "scripts/acervo/ocr_priority_pdfs.py",
        "--priority",
        args.ocr_priority,
    ]
    if args.force_ocr:
        ocr_command.append("--force")
    if args.max_ocr_pages:
        ocr_command.extend(["--max-pages", str(args.max_ocr_pages)])
    if args.ocr_only_contains:
        ocr_command.extend(["--only-contains", args.ocr_only_contains])

    return [
        PipelineStep(
            "Empacotar/atualizar staging humano tecnico",
            [python, "scripts/acervo/package_human_technical_archive.py"],
            enabled=not args.skip_package,
        ),
        PipelineStep(
            "Reconstruir indice local do acervo principal",
            [python, "scripts/acervo/build_local_index.py"],
            enabled=not args.skip_local_index,
        ),
        PipelineStep(
            "Auditar PDFs com toolchain externo",
            audit_command,
            enabled=not args.skip_audit,
        ),
        PipelineStep(
            "Gerar OCR auxiliar prioritario",
            ocr_command,
            enabled=not args.skip_ocr,
        ),
        PipelineStep(
            "Regenerar notas companheiras dos PDFs",
            [python, "scripts/acervo/build_pdf_companion_notes.py"],
            enabled=not args.skip_companion_notes,
        ),
        PipelineStep(
            "Construir painel de curadoria do acervo",
            [python, "scripts/acervo/build_curation_dashboard.py"],
            enabled=not args.skip_curation_dashboard,
        ),
        PipelineStep(
            "Validar scripts Python",
            [python, "scripts/check_python_scripts.py"],
            enabled=not args.skip_check_scripts,
        ),
        PipelineStep(
            "Validar vault Markdown",
            [python, "scripts/validate_vault.py"],
            enabled=not args.skip_validate,
        ),
        PipelineStep(
            "Reconstruir manifesto geral",
            [python, "scripts/build_manifest.py"],
            enabled=not args.skip_manifest,
        ),
    ]


def render_report(payload: dict[str, object]) -> str:
    reviewed_on = datetime.now().date().isoformat()
    steps = payload["steps"]
    assert isinstance(steps, list)
    status_counts: dict[str, int] = {}
    for item in steps:
        if not isinstance(item, dict):
            continue
        status = str(item.get("status", "unknown"))
        status_counts[status] = status_counts.get(status, 0) + 1

    lines = [
        "---",
        'title: "Pipeline PDF - Ultima Execucao"',
        'note_type: "audit"',
        'domain: "90_Revisao_Manual"',
        'status: "auto-generated"',
        f'reviewed_on: "{reviewed_on}"',
        'review_jurisdiction: "Brasil"',
        "related_notes:",
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Local - Indice Gerado"',
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado"',
        '  - "Auditoria Operacional PDF - Toolchain"',
        '  - "OCR Controlado - Acervo Principal"',
        "---",
        "",
        "# Pipeline PDF - Ultima Execucao",
        "",
        "> [!abstract] Resumo tecnico",
        "> Orquestrador operacional para atualizar indice local, auditoria PDF, OCR auxiliar, notas companheiras, validacao e manifestos.",
        "",
        "## Resultado",
        "",
        f"- status geral: `{payload['status']}`",
        f"- iniciado em: `{payload['started_at']}`",
        f"- finalizado em: `{payload['finished_at']}`",
        f"- duracao total: `{payload['duration_seconds']}` s",
        f"- dry-run: `{payload['dry_run']}`",
        f"- manifesto: `{relative(MANIFEST_PATH)}`",
        "",
        "## Contagem por status",
        "",
    ]
    for status, count in sorted(status_counts.items()):
        lines.append(f"- `{status}`: `{count}`")

    lines.extend(["", "## Passos", ""])
    for item in steps:
        if not isinstance(item, dict):
            continue
        lines.extend(
            [
                f"### {item.get('name')}",
                "",
                f"- status: `{item.get('status')}`",
                f"- retorno: `{item.get('returncode')}`",
                f"- duracao: `{item.get('duration_seconds')}` s",
                f"- comando: `{item.get('command')}`",
                "",
            ]
        )

    lines.extend(
        [
            "## Uso recomendado",
            "",
            "- Para rotina completa: `python scripts/acervo/run_pdf_pipeline.py`.",
            "- Para teste rapido: `python scripts/acervo/run_pdf_pipeline.py --dry-run`.",
            "- Para nao gastar OCR pesado: `python scripts/acervo/run_pdf_pipeline.py --skip-ocr`.",
            "- Para janela curta: `python scripts/acervo/run_pdf_pipeline.py --fast-audit --skip-ocr`.",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Orquestra a rotina operacional dos PDFs do acervo."
    )
    parser.add_argument(
        "--audit-scope",
        choices=("all", "main", "staging"),
        default="all",
        help="Escopo repassado ao auditor PDF.",
    )
    parser.add_argument(
        "--ocr-priority",
        default="alta",
        help="Prioridade repassada ao OCR auxiliar.",
    )
    parser.add_argument("--ocr-sample-limit", type=int, default=2)
    parser.add_argument("--max-audit-files", type=int, default=0)
    parser.add_argument("--max-ocr-pages", type=int, default=0)
    parser.add_argument("--ocr-only-contains", default="")
    parser.add_argument("--fast-audit", action="store_true")
    parser.add_argument("--force-ocr", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--keep-going", action="store_true")
    parser.add_argument("--skip-package", action="store_true")
    parser.add_argument("--skip-local-index", action="store_true")
    parser.add_argument("--skip-audit", action="store_true")
    parser.add_argument("--skip-ocr", action="store_true")
    parser.add_argument("--skip-companion-notes", action="store_true")
    parser.add_argument("--skip-curation-dashboard", action="store_true")
    parser.add_argument("--skip-check-scripts", action="store_true")
    parser.add_argument("--skip-validate", action="store_true")
    parser.add_argument("--skip-manifest", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    started_at = datetime.now(timezone.utc)
    start_time = time.perf_counter()
    steps = build_steps(args)
    results: list[dict[str, object]] = []
    status = "ok"

    for step in steps:
        result = run_step(step, dry_run=args.dry_run)
        results.append(result)
        if result["status"] == "failed":
            status = "failed"
            if not args.keep_going:
                break

    finished_at = datetime.now(timezone.utc)
    payload: dict[str, object] = {
        "generated_at": finished_at.isoformat(),
        "started_at": started_at.isoformat(),
        "finished_at": finished_at.isoformat(),
        "duration_seconds": round(time.perf_counter() - start_time, 3),
        "status": status,
        "dry_run": args.dry_run,
        "audit_scope": args.audit_scope,
        "ocr_priority": args.ocr_priority,
        "steps": results,
    }
    write_json(MANIFEST_PATH, payload)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(render_report(payload), encoding="utf-8", newline="\n")

    print("")
    print(f"Status geral: {status}")
    print(f"Manifesto: {relative(MANIFEST_PATH)}")
    print(f"Relatorio: {relative(REPORT_PATH)}")
    return 0 if status == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
