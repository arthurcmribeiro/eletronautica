from __future__ import annotations

import argparse
import json
import os
import re
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent

if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.append(str(SCRIPTS_ROOT))
if str(SCRIPT_DIR) not in sys.path:
    sys.path.append(str(SCRIPT_DIR))

from vault_tools import ROOT, write_json  # noqa: E402
from pdf_text_tools import clean_text_block, looks_like_useful_text  # noqa: E402
from audit_pdf_toolchain import (  # noqa: E402
    TEMP_ROOT,
    add_user_environment_defaults,
    find_tool,
    remove_tree_best_effort,
    run_command,
    tool_version,
)


AUDIT_PATH = ROOT / "manifest" / "acervo-pdf-toolchain-audit.json"
DATA_ROOT = ROOT / "90_Revisao_Manual" / "_Dados_Acervo"
OCR_TEXT_ROOT = DATA_ROOT / "ocr_texts"
OCR_NOTE_ROOT = DATA_ROOT / "ocr_notes"
OCR_RESULTS_PATH = DATA_ROOT / "ocr-results.json"
OCR_REPORT_PATH = ROOT / "_Editorial" / "OCR Controlado - Acervo Principal.md"


def yaml_quote(value: Any) -> str:
    text = str(value).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{text}"'


def absolute_link(path: Path) -> str:
    return path.resolve().as_posix()


def relative_to_root(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def title_from_pdf_name(name: str) -> str:
    return Path(name).stem.replace("__", " - ").replace("_", " ").strip()


def markdown_safe_ocr(text: str) -> str:
    # Raw OCR can contain bracket noise. Avoid accidental Obsidian wikilinks.
    return text.replace("[[", "[ [").replace("]]", "] ]")


def output_paths(record: dict[str, Any]) -> tuple[Path, Path]:
    base = Path(str(record["acervo_relative_path"])).with_suffix("")
    text_path = OCR_TEXT_ROOT / base.parent / f"{base.name}.ocr.txt"
    note_path = OCR_NOTE_ROOT / base.parent / f"{base.name}.ocr.md"
    return text_path, note_path


def load_audit(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(
            f"Manifesto de auditoria nao encontrado: {relative_to_root(path)}"
        )
    return json.loads(path.read_text(encoding="utf-8"))


def selected_records(
    audit: dict[str, Any],
    *,
    priorities: set[str],
    include_qpdf_warning: bool,
    only_contains: str,
) -> list[dict[str, Any]]:
    accepted_qpdf = {"ok"}
    if include_qpdf_warning:
        accepted_qpdf.add("warning")

    records: list[dict[str, Any]] = []
    for record in audit.get("pdfs", []):
        if record.get("collection") != "acervo-principal":
            continue
        if str(record.get("ocr_priority")) not in priorities:
            continue
        if str(record.get("qpdf_status")) not in accepted_qpdf:
            continue
        if record.get("encrypted"):
            continue
        if only_contains and only_contains.casefold() not in str(
            record.get("relative_path", "")
        ).casefold():
            continue
        records.append(record)

    records.sort(key=lambda item: str(item.get("relative_path", "")).casefold())
    return records


def render_page_image(
    *,
    pdf_path: Path,
    page: int,
    temp_dir: Path,
    pdftoppm_tool: Path,
    dpi: int,
    timeout: int,
) -> tuple[Path | None, str]:
    output_prefix = temp_dir / f"page-{page:04d}"
    render_return, _stdout, stderr, render_timeout = run_command(
        [
            str(pdftoppm_tool),
            "-f",
            str(page),
            "-l",
            str(page),
            "-singlefile",
            "-r",
            str(dpi),
            "-png",
            str(pdf_path),
            str(output_prefix),
        ],
        timeout=timeout,
    )
    image_path = output_prefix.with_suffix(".png")
    if render_timeout:
        return None, "pdftoppm timeout"
    if render_return == 0 and image_path.exists():
        return image_path, ""
    return None, clean_text_block(stderr).splitlines()[0] if stderr.strip() else "render-error"


def run_tesseract(
    *,
    image_path: Path,
    tesseract_tool: Path,
    language: str,
    psm: int,
    timeout: int,
) -> tuple[str, str, bool]:
    env = os.environ.copy()
    if os.environ.get("TESSDATA_PREFIX"):
        env["TESSDATA_PREFIX"] = os.environ["TESSDATA_PREFIX"]

    return_code, stdout, stderr, ocr_timeout = run_command(
        [
            str(tesseract_tool),
            str(image_path),
            "stdout",
            "-l",
            language,
            "--psm",
            str(psm),
        ],
        timeout=timeout,
        env=env,
    )
    if ocr_timeout:
        return "", "tesseract timeout", False
    if return_code != 0:
        message = clean_text_block(stderr).splitlines()
        return "", message[0] if message else "tesseract-error", False
    text = clean_text_block(stdout)
    return text, "", True


def page_count_from_record(record: dict[str, Any], max_pages: int) -> int:
    pages = record.get("pages")
    if isinstance(pages, int):
        count = pages
    elif isinstance(pages, str) and pages.isdigit():
        count = int(pages)
    else:
        count = 1

    if max_pages > 0:
        return min(count, max_pages)
    return count


def write_ocr_outputs(
    *,
    record: dict[str, Any],
    text_path: Path,
    note_path: Path,
    page_texts: list[dict[str, Any]],
    status: str,
    language: str,
    dpi: int,
    psm: int,
    generated_at: str,
) -> tuple[int, int]:
    pdf_path = ROOT / str(record["relative_path"])
    reviewed_on = datetime.now().date().isoformat()
    source_pdf = str(record["relative_path"])
    source_sha = str(record.get("sha256", ""))

    text_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.parent.mkdir(parents=True, exist_ok=True)

    txt_lines: list[str] = [
        f"OCR text generated at: {generated_at}",
        f"source_pdf: {source_pdf}",
        f"source_sha256: {source_sha}",
        f"language: {language}",
        f"dpi: {dpi}",
        f"psm: {psm}",
        f"status: {status}",
        "",
    ]
    md_lines: list[str] = [
        "---",
        f"title: {yaml_quote('OCR - ' + title_from_pdf_name(str(record['file_name'])))}",
        'note_type: "acervo-ocr-text"',
        'domain: "90_Revisao_Manual"',
        'status: "auto-generated"',
        f"reviewed_on: {yaml_quote(reviewed_on)}",
        'review_jurisdiction: "Brasil"',
        f"source_pdf: {yaml_quote(source_pdf)}",
        f"source_sha256: {yaml_quote(source_sha)}",
        f"ocr_status: {yaml_quote(status)}",
        f"ocr_language: {yaml_quote(language)}",
        f"ocr_dpi: {yaml_quote(dpi)}",
        f"ocr_psm: {yaml_quote(psm)}",
        "aliases:",
        f"  - {yaml_quote(str(record['file_name']) + ' OCR')}",
        "related_notes:",
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado"',
        "---",
        "",
        f"# OCR - {title_from_pdf_name(str(record['file_name']))}",
        "",
        "> [!warning] Texto derivado por OCR",
        "> Use este arquivo para busca e triagem. O PDF original continua sendo a fonte primaria.",
        "",
        "## Fonte",
        "",
        f"- PDF: [{record['file_name']}](</{absolute_link(pdf_path)}>)",
        f"- caminho relativo: `{source_pdf}`",
        f"- SHA-256: `{source_sha}`",
        f"- TXT OCR: [{text_path.name}](</{absolute_link(text_path)}>)",
        f"- status OCR: `{status}`",
        f"- idioma: `{language}`",
        f"- renderizacao: `{dpi}` dpi",
        "",
        "## Texto OCR",
        "",
    ]

    chars = 0
    useful_pages = 0
    for page in page_texts:
        page_number = int(page["page"])
        page_status = str(page["status"])
        page_text = str(page.get("text", ""))
        page_message = str(page.get("message", ""))
        if page_text:
            chars += len(page_text)
        if looks_like_useful_text(page_text):
            useful_pages += 1

        txt_lines.extend(
            [
                f"--- PAGE {page_number} [{page_status}] ---",
                page_text if page_text else f"[sem texto OCR: {page_message}]",
                "",
            ]
        )
        md_lines.extend([f"### Pagina {page_number}", ""])
        if page_text:
            md_lines.extend(markdown_safe_ocr(page_text).splitlines())
        else:
            md_lines.append(f"`sem texto OCR: {page_message}`")
        md_lines.append("")

    text_path.write_text("\n".join(txt_lines), encoding="utf-8", newline="\n")
    note_path.write_text("\n".join(md_lines), encoding="utf-8", newline="\n")
    return chars, useful_pages


def ocr_pdf(
    *,
    record: dict[str, Any],
    tools: dict[str, Path | None],
    language: str,
    dpi: int,
    psm: int,
    max_pages: int,
    render_timeout: int,
    page_timeout: int,
    force: bool,
) -> dict[str, Any]:
    text_path, note_path = output_paths(record)
    if text_path.exists() and note_path.exists() and not force:
        return {
            "source_pdf": record["relative_path"],
            "source_sha256": record.get("sha256", ""),
            "status": "skipped-existing",
            "output_text": relative_to_root(text_path),
            "output_note": relative_to_root(note_path),
        }

    pdftoppm_tool = tools["pdftoppm"]
    tesseract_tool = tools["tesseract"]
    if pdftoppm_tool is None or tesseract_tool is None:
        return {
            "source_pdf": record["relative_path"],
            "source_sha256": record.get("sha256", ""),
            "status": "missing-tool",
            "message": "pdftoppm ou tesseract ausente",
        }

    pdf_path = ROOT / str(record["relative_path"])
    total_pages = page_count_from_record(record, max_pages)
    generated_at = datetime.now(timezone.utc).isoformat()
    temp_dir = TEMP_ROOT / f"ocr-full-{uuid.uuid4().hex}"
    temp_dir.mkdir(parents=True, exist_ok=False)

    page_texts: list[dict[str, Any]] = []
    try:
        for page in range(1, total_pages + 1):
            print(f"  pagina {page}/{total_pages}")
            image_path, render_message = render_page_image(
                pdf_path=pdf_path,
                page=page,
                temp_dir=temp_dir,
                pdftoppm_tool=pdftoppm_tool,
                dpi=dpi,
                timeout=render_timeout,
            )
            if image_path is None:
                page_texts.append(
                    {"page": page, "status": "render-error", "message": render_message}
                )
                continue

            page_text, ocr_message, ok = run_tesseract(
                image_path=image_path,
                tesseract_tool=tesseract_tool,
                language=language,
                psm=psm,
                timeout=page_timeout,
            )
            page_texts.append(
                {
                    "page": page,
                    "status": "ok" if ok else "ocr-error",
                    "message": "" if ok else ocr_message,
                    "chars": len(page_text),
                    "useful_text": looks_like_useful_text(page_text),
                    "text": page_text,
                }
            )
            try:
                image_path.unlink()
            except OSError:
                pass
    finally:
        try:
            remove_tree_best_effort(temp_dir)
        except OSError:
            pass

    failed_pages = [
        page
        for page in page_texts
        if str(page.get("status")) != "ok" or not looks_like_useful_text(str(page.get("text", "")))
    ]
    status = "completed"
    if failed_pages and len(failed_pages) < len(page_texts):
        status = "partial"
    elif failed_pages and len(failed_pages) == len(page_texts):
        status = "failed"

    chars, useful_pages = write_ocr_outputs(
        record=record,
        text_path=text_path,
        note_path=note_path,
        page_texts=page_texts,
        status=status,
        language=language,
        dpi=dpi,
        psm=psm,
        generated_at=generated_at,
    )

    return {
        "source_pdf": record["relative_path"],
        "acervo_relative_path": record["acervo_relative_path"],
        "source_sha256": record.get("sha256", ""),
        "file_name": record.get("file_name", ""),
        "status": status,
        "pages_total": total_pages,
        "pages_completed": sum(1 for page in page_texts if page.get("status") == "ok"),
        "pages_useful": useful_pages,
        "pages_failed": len(failed_pages),
        "chars": chars,
        "language": language,
        "dpi": dpi,
        "psm": psm,
        "generated_at": generated_at,
        "output_text": relative_to_root(text_path),
        "output_note": relative_to_root(note_path),
        "failed_pages": [
            {
                "page": page.get("page"),
                "status": page.get("status"),
                "message": page.get("message", ""),
            }
            for page in failed_pages
        ],
    }


def merge_existing_results(
    existing_payload: dict[str, Any] | None,
    new_results: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    by_source: dict[str, dict[str, Any]] = {}
    if existing_payload:
        for result in existing_payload.get("results", []):
            source = str(result.get("source_pdf", ""))
            if source:
                by_source[source] = result
    for result in new_results:
        source = str(result.get("source_pdf", ""))
        if source:
            by_source[source] = result
    return sorted(by_source.values(), key=lambda item: str(item.get("source_pdf", "")))


def load_existing_results() -> dict[str, Any] | None:
    if not OCR_RESULTS_PATH.exists():
        return None
    return json.loads(OCR_RESULTS_PATH.read_text(encoding="utf-8"))


def render_report(results: list[dict[str, Any]], tools_payload: dict[str, Any]) -> str:
    reviewed_on = datetime.now().date().isoformat()
    generated_at = datetime.now(timezone.utc).isoformat()
    status_counts: dict[str, int] = {}
    for result in results:
        status = str(result.get("status", ""))
        status_counts[status] = status_counts.get(status, 0) + 1

    lines = [
        "---",
        'title: "OCR Controlado - Acervo Principal"',
        'note_type: "audit"',
        'domain: "90_Revisao_Manual"',
        'status: "auto-generated"',
        f"reviewed_on: {yaml_quote(reviewed_on)}",
        'review_jurisdiction: "Brasil"',
        "related_notes:",
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado"',
        '  - "Auditoria Operacional PDF - Toolchain"',
        "---",
        "",
        "# OCR Controlado - Acervo Principal",
        "",
        "> [!abstract] Resumo tecnico",
        "> OCR pesado executado somente nos PDFs prioritarios do acervo principal, sem regravar os PDFs originais.",
        "",
        "## Execucao",
        "",
        f"- gerado em: `{generated_at}`",
        f"- resultados no manifesto: `{relative_to_root(OCR_RESULTS_PATH)}`",
        f"- pasta TXT: `{relative_to_root(OCR_TEXT_ROOT)}`",
        f"- pasta MD: `{relative_to_root(OCR_NOTE_ROOT)}`",
        "",
        "## Ferramentas",
        "",
    ]
    for name, payload in tools_payload.items():
        lines.append(f"- `{name}`: `{payload['version']}` - `{payload['path']}`")

    lines.extend(["", "## Status", ""])
    for status, count in sorted(status_counts.items()):
        lines.append(f"- `{status}`: `{count}`")

    lines.extend(["", "## PDFs processados", ""])
    if not results:
        lines.append("- nenhum PDF processado")
    for result in results:
        pdf_path = ROOT / str(result.get("source_pdf", ""))
        note_path = ROOT / str(result.get("output_note", ""))
        text_path = ROOT / str(result.get("output_text", ""))
        lines.append(
            f"- `{result.get('status')}` - [{result.get('file_name', pdf_path.name)}](</{absolute_link(pdf_path)}>) - "
            f"`{result.get('pages_useful', 0)}/{result.get('pages_total', '?')}` paginas uteis - "
            f"`{result.get('chars', 0)}` chars - "
            f"[MD](</{absolute_link(note_path)}>) - [TXT](</{absolute_link(text_path)}>)"
        )

    lines.extend(
        [
            "",
            "## Proximos passos",
            "",
            "- Rodar `python scripts/acervo/build_pdf_companion_notes.py` para as notas companheiras herdarem os links OCR.",
            "- Rodar `python scripts/acervo/audit_pdf_toolchain.py --scope all` quando houver janela longa para atualizar a fila global de OCR.",
            "- Manter OCR pesado limitado a `alta` e `media`; nao gastar processamento em duplicata ou fora de escopo.",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Gera OCR auxiliar para PDFs prioritarios do acervo principal."
    )
    parser.add_argument(
        "--priority",
        action="append",
        default=None,
        help="Prioridade de OCR a processar. Pode repetir. Padrao: alta.",
    )
    parser.add_argument(
        "--only-contains",
        default="",
        help="Processa apenas PDFs cujo caminho contenha este texto.",
    )
    parser.add_argument("--language", default="por+eng", help="Idiomas do Tesseract.")
    parser.add_argument("--dpi", type=int, default=150, help="DPI de renderizacao.")
    parser.add_argument("--psm", type=int, default=3, help="Modo PSM do Tesseract.")
    parser.add_argument(
        "--max-pages",
        type=int,
        default=0,
        help="Limite de paginas por PDF. 0 processa todas.",
    )
    parser.add_argument("--render-timeout", type=int, default=60)
    parser.add_argument("--page-timeout", type=int, default=120)
    parser.add_argument("--force", action="store_true", help="Regera OCR existente.")
    parser.add_argument(
        "--strict-qpdf",
        action="store_true",
        help="Processa apenas qpdf ok, ignorando warning.",
    )
    parser.add_argument("--audit-path", type=Path, default=AUDIT_PATH)
    parser.add_argument("--report-path", type=Path, default=OCR_REPORT_PATH)
    return parser.parse_args()


def main() -> int:
    add_user_environment_defaults()
    args = parse_args()
    audit = load_audit(args.audit_path)
    priorities = set(args.priority or ["alta"])
    records = selected_records(
        audit,
        priorities=priorities,
        include_qpdf_warning=not args.strict_qpdf,
        only_contains=args.only_contains,
    )

    tools = {
        "pdftoppm": find_tool("pdftoppm"),
        "tesseract": find_tool("tesseract"),
    }
    tools_payload = {
        name: {
            "path": str(path) if path else "",
            "version": tool_version(name, path),
        }
        for name, path in tools.items()
    }

    print(f"PDFs selecionados para OCR: {len(records)}")
    new_results: list[dict[str, Any]] = []
    for index, record in enumerate(records, start=1):
        print(f"[{index}/{len(records)}] {record['relative_path']}")
        result = ocr_pdf(
            record=record,
            tools=tools,
            language=args.language,
            dpi=args.dpi,
            psm=args.psm,
            max_pages=args.max_pages,
            render_timeout=args.render_timeout,
            page_timeout=args.page_timeout,
            force=args.force,
        )
        new_results.append(result)

    existing_payload = load_existing_results()
    merged_results = merge_existing_results(existing_payload, new_results)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_audit": relative_to_root(args.audit_path),
        "tools": tools_payload,
        "results": merged_results,
    }
    write_json(OCR_RESULTS_PATH, payload)

    args.report_path.parent.mkdir(parents=True, exist_ok=True)
    args.report_path.write_text(
        render_report(merged_results, tools_payload),
        encoding="utf-8",
        newline="\n",
    )

    completed = sum(1 for result in new_results if result.get("status") == "completed")
    partial = sum(1 for result in new_results if result.get("status") == "partial")
    failed = sum(1 for result in new_results if result.get("status") == "failed")
    skipped = sum(1 for result in new_results if result.get("status") == "skipped-existing")
    print("")
    print(f"OCR completed={completed} partial={partial} failed={failed} skipped={skipped}")
    print(f"Manifesto OCR: {relative_to_root(OCR_RESULTS_PATH)}")
    print(f"Relatorio OCR: {relative_to_root(args.report_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
