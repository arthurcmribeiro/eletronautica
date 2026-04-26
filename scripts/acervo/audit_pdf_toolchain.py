from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import uuid
from collections import Counter, defaultdict
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
from pdf_text_tools import (  # noqa: E402
    clean_text_block,
    extract_pdf_text,
    looks_like_useful_text,
)


ACERVO_ROOT = ROOT / "90_Revisao_Manual" / "_Acervo_Local"
ACERVO_NOTAS_ROOT = ROOT / "90_Revisao_Manual" / "_Acervo_Notas"
MANIFEST_PATH = ROOT / "manifest" / "acervo-pdf-toolchain-audit.json"
REPORT_PATH = ROOT / "_Editorial" / "Auditoria Operacional PDF - Toolchain.md"
TEMP_ROOT = ROOT / ".tmp_pdf_tools"
OCR_RESULTS_PATH = ROOT / "90_Revisao_Manual" / "_Dados_Acervo" / "ocr-results.json"

TOOL_NAMES = (
    "pdftotext",
    "pdfinfo",
    "pdftoppm",
    "qpdf",
    "exiftool",
    "tesseract",
    "mutool",
    "magick",
    "gswin64c",
    "7z",
)

TOOL_CANDIDATES: dict[str, tuple[str, ...]] = {
    "pdftotext": (
        r"C:\Program Files\Git\mingw64\bin\pdftotext.exe",
        r"C:\Program Files\poppler\bin\pdftotext.exe",
    ),
    "pdfinfo": (
        r"C:\Program Files\Git\mingw64\bin\pdfinfo.exe",
        r"C:\Program Files\poppler\bin\pdfinfo.exe",
    ),
    "pdftoppm": (
        r"C:\Program Files\Git\mingw64\bin\pdftoppm.exe",
        r"C:\Program Files\poppler\bin\pdftoppm.exe",
    ),
    "qpdf": (r"C:\Program Files\qpdf 12.3.2\bin\qpdf.exe",),
    "exiftool": (r"C:\Users\User\AppData\Local\Programs\ExifTool\ExifTool.exe",),
    "tesseract": (r"C:\Program Files\Tesseract-OCR\tesseract.exe",),
    "mutool": (),
    "magick": (),
    "gswin64c": (r"C:\Program Files\gs\gs10.07.0\bin\gswin64c.exe",),
    "7z": (r"C:\Program Files\7-Zip\7z.exe",),
}

WINGET_PACKAGES = (
    Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft" / "WinGet" / "Packages"
)


def path_key(path: Path) -> str:
    return path.resolve().as_posix().casefold()


def add_user_environment_defaults() -> None:
    user_tessdata = (
        Path(os.environ.get("LOCALAPPDATA", "")) / "Tesseract-OCR" / "tessdata"
    )
    if user_tessdata.exists() and not os.environ.get("TESSDATA_PREFIX"):
        os.environ["TESSDATA_PREFIX"] = str(user_tessdata)


def remove_tree_best_effort(path: Path) -> None:
    def make_writable_and_retry(function: Any, blocked_path: str, _exc: Any) -> None:
        try:
            os.chmod(blocked_path, stat.S_IWRITE)
            function(blocked_path)
        except OSError:
            pass

    shutil.rmtree(path, ignore_errors=False, onerror=make_writable_and_retry)


def find_tool(name: str) -> Path | None:
    env_key = f"{name.upper()}_PATH"
    if os.environ.get(env_key):
        candidate = Path(os.environ[env_key])
        if candidate.exists():
            return candidate

    executable = shutil.which(name)
    if executable:
        return Path(executable)

    for candidate_text in TOOL_CANDIDATES.get(name, ()):
        candidate = Path(candidate_text)
        if candidate.exists():
            return candidate

    if WINGET_PACKAGES.exists():
        try:
            matches = sorted(WINGET_PACKAGES.rglob(f"{name}.exe"))
        except OSError:
            matches = []
        if matches:
            return matches[-1]

    return None


def run_command(
    args: list[str],
    *,
    timeout: int = 30,
    env: dict[str, str] | None = None,
) -> tuple[int | None, str, str, bool]:
    try:
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            timeout=timeout,
            check=False,
            env=env,
        )
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout if isinstance(exc.stdout, str) else ""
        stderr = exc.stderr if isinstance(exc.stderr, str) else ""
        return None, stdout, stderr, True
    except OSError as exc:
        return None, "", str(exc), False

    return result.returncode, result.stdout, result.stderr, False


def first_line(value: str) -> str:
    for line in value.splitlines():
        if line.strip():
            return " ".join(line.split())
    return ""


def tool_version(name: str, tool: Path | None) -> str:
    if tool is None:
        return "missing"

    args_by_tool = {
        "pdftotext": [str(tool), "-v"],
        "pdfinfo": [str(tool), "-v"],
        "pdftoppm": [str(tool), "-v"],
        "qpdf": [str(tool), "--version"],
        "exiftool": [str(tool), "-ver"],
        "tesseract": [str(tool), "--version"],
        "mutool": [str(tool), "-v"],
        "magick": [str(tool), "-version"],
        "gswin64c": [str(tool), "-version"],
        "7z": [str(tool)],
    }
    returncode, stdout, stderr, _timed_out = run_command(
        args_by_tool[name],
        timeout=15,
    )
    output = "\n".join(part for part in (stdout, stderr) if part)
    if returncode is None and not output:
        return "unavailable"
    if name == "7z":
        lines = [line.strip() for line in output.splitlines() if line.strip()]
        for line in lines:
            if line.startswith("7-Zip"):
                return line
    return first_line(output) or "available"


def tesseract_languages(tool: Path | None) -> list[str]:
    if tool is None:
        return []
    returncode, stdout, stderr, _timed_out = run_command(
        [str(tool), "--list-langs"],
        timeout=15,
    )
    if returncode not in (0, None):
        return []
    output = "\n".join(part for part in (stdout, stderr) if part)
    results: list[str] = []
    for line in output.splitlines():
        cleaned = line.strip()
        if not cleaned or cleaned.startswith("List of available"):
            continue
        results.append(cleaned)
    return sorted(set(results))


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def human_size(size_bytes: int) -> str:
    value = float(size_bytes)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if value < 1024 or unit == "TB":
            if unit == "B":
                return f"{int(value)} B"
            return f"{value:.1f} {unit}"
        value /= 1024
    return f"{size_bytes} B"


def parse_pdfinfo(output: str) -> dict[str, str | int | bool]:
    fields: dict[str, str | int | bool] = {}
    for raw_line in output.splitlines():
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        normalized_key = re.sub(r"[^a-z0-9]+", "_", key.strip().lower()).strip("_")
        fields[normalized_key] = " ".join(value.split())

    if "pages" in fields:
        try:
            fields["pages"] = int(str(fields["pages"]))
        except ValueError:
            pass
    if "encrypted" in fields:
        encrypted_text = str(fields["encrypted"]).lower()
        fields["encrypted"] = encrypted_text not in {"no", "false", "0"}

    return fields


def collect_pdfinfo(path: Path, tool: Path | None) -> dict[str, Any]:
    if tool is None:
        return {"status": "missing-tool"}

    returncode, stdout, stderr, timed_out = run_command(
        [str(tool), str(path)],
        timeout=20,
    )
    if timed_out:
        return {"status": "timeout"}
    if returncode != 0:
        return {
            "status": "error",
            "message": first_line(stderr or stdout),
        }

    fields = parse_pdfinfo(stdout)
    fields["status"] = "ok"
    return fields


def collect_qpdf_check(path: Path, tool: Path | None, *, skip: bool) -> dict[str, Any]:
    if skip:
        return {"status": "skipped", "messages": []}
    if tool is None:
        return {"status": "missing-tool", "messages": []}

    returncode, stdout, stderr, timed_out = run_command(
        [str(tool), "--check", str(path)],
        timeout=30,
    )
    combined = "\n".join(part for part in (stdout, stderr) if part)
    messages = [
        " ".join(line.split())
        for line in combined.splitlines()
        if line.strip()
    ][:12]

    if timed_out:
        return {"status": "timeout", "messages": messages}
    if returncode == 0:
        return {"status": "ok", "messages": messages}
    if returncode == 3 or "warning" in combined.lower():
        return {"status": "warning", "messages": messages}
    return {"status": "error", "messages": messages}


def chunks(items: list[Path], size: int) -> list[list[Path]]:
    return [items[index : index + size] for index in range(0, len(items), size)]


def collect_exif_metadata(paths: list[Path], tool: Path | None) -> dict[str, dict[str, Any]]:
    if tool is None or not paths:
        return {}

    metadata: dict[str, dict[str, Any]] = {}
    fields = [
        "-Title",
        "-Author",
        "-Creator",
        "-Producer",
        "-CreateDate",
        "-ModifyDate",
        "-PDFVersion",
        "-PageCount",
        "-Encrypted",
        "-FileType",
        "-MIMEType",
    ]

    for group in chunks(paths, 25):
        args = [str(tool), "-json", *fields, *(str(path) for path in group)]
        returncode, stdout, stderr, timed_out = run_command(args, timeout=90)
        if timed_out or returncode not in (0, None) or not stdout.strip():
            continue
        try:
            payload = json.loads(stdout)
        except json.JSONDecodeError:
            continue
        if not isinstance(payload, list):
            continue
        for item in payload:
            if not isinstance(item, dict):
                continue
            source = item.get("SourceFile")
            if not source:
                continue
            source_path = Path(str(source))
            metadata[path_key(source_path)] = {
                key: value
                for key, value in item.items()
                if key != "SourceFile" and value not in ("", None)
            }
    return metadata


def collection_for(path: Path) -> str:
    relative_parts = path.relative_to(ACERVO_ROOT).parts
    if not relative_parts or relative_parts[0] != "Acervo do humano":
        return "acervo-principal"

    if "_Arquivados_Duplicatas_Resolvidas" in relative_parts:
        return "humano-arquivado-duplicata"
    if len(relative_parts) > 1 and relative_parts[1] == "10_Tecnico_Nautico":
        return "humano-staging-tecnico"
    if len(relative_parts) > 1 and relative_parts[1] == "00_Fora_do_Escopo_ou_Pessoal":
        return "humano-fora-do-escopo"
    return "humano-staging"


def iter_pdf_paths(scope: str) -> list[Path]:
    paths = sorted(path for path in ACERVO_ROOT.rglob("*.pdf") if path.is_file())
    if scope == "all":
        return paths
    if scope == "main":
        return [path for path in paths if collection_for(path) == "acervo-principal"]
    if scope == "staging":
        return [path for path in paths if collection_for(path) != "acervo-principal"]
    raise ValueError(f"Escopo invalido: {scope}")


def companion_note_info(path: Path) -> dict[str, Any]:
    if collection_for(path) != "acervo-principal":
        return {"expected": "", "exists": False}

    relative_to_acervo = path.relative_to(ACERVO_ROOT)
    note_path = ACERVO_NOTAS_ROOT / relative_to_acervo.with_suffix(".md")
    return {
        "expected": note_path.relative_to(ROOT).as_posix(),
        "exists": note_path.exists(),
    }


def load_ocr_results() -> dict[str, dict[str, Any]]:
    if not OCR_RESULTS_PATH.exists():
        return {}
    try:
        payload = json.loads(OCR_RESULTS_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}

    results: dict[str, dict[str, Any]] = {}
    for item in payload.get("results", []):
        if not isinstance(item, dict):
            continue
        source_pdf = item.get("source_pdf")
        if isinstance(source_pdf, str) and source_pdf:
            results[source_pdf] = item
    return results


def ocr_sidecar_is_available(ocr_record: dict[str, Any] | None) -> bool:
    if not ocr_record:
        return False
    if str(ocr_record.get("status")) not in {"completed", "partial"}:
        return False
    output_note = ocr_record.get("output_note")
    output_text = ocr_record.get("output_text")
    if not isinstance(output_note, str) or not isinstance(output_text, str):
        return False
    return (ROOT / output_note).exists() and (ROOT / output_text).exists()


def classify_ocr(
    *,
    collection: str,
    encrypted: bool,
    qpdf_status: str,
    text_extractable: bool,
    page_count: int | None,
    ocr_sidecar_available: bool,
) -> tuple[str, str]:
    if text_extractable:
        return "nao", "texto pesquisavel ja detectado"
    if ocr_sidecar_available:
        return "concluido", "OCR auxiliar ja gerado em _Dados_Acervo"
    if encrypted:
        return "bloqueado", "PDF com restricao interna; resolver permissao antes de OCR"
    if qpdf_status in {"error", "timeout"}:
        return "reparar-primeiro", "qpdf nao validou o PDF; reparar antes de OCR"

    if collection == "acervo-principal":
        return "alta", "PDF curado sem texto confiavel; OCR melhora busca e notas"
    if collection == "humano-staging-tecnico":
        return "media", "staging tecnico sem texto confiavel; OCR ajuda triagem"
    if collection == "humano-arquivado-duplicata":
        return "baixa", "duplicata arquivada; OCR so se virar fonte canonica"
    if page_count and page_count <= 2:
        return "baixa", "arquivo curto sem texto; revisar se e recorte/scan util"
    return "baixa", "PDF sem texto confiavel; OCR sob demanda"


def ocr_first_page(
    path: Path,
    *,
    tesseract_tool: Path | None,
    pdftoppm_tool: Path | None,
    mutool_tool: Path | None,
    magick_tool: Path | None,
) -> dict[str, Any]:
    if tesseract_tool is None:
        return {"status": "missing-tesseract"}

    TEMP_ROOT.mkdir(parents=True, exist_ok=True)
    temp_dir = TEMP_ROOT / f"acervo-ocr-{uuid.uuid4().hex}"
    temp_dir.mkdir(parents=True, exist_ok=False)
    try:
        image_path: Path | None = None
        render_message = ""

        if pdftoppm_tool is not None:
            output_prefix = temp_dir / "page"
            render_return, _render_stdout, render_stderr, render_timeout = run_command(
                [
                    str(pdftoppm_tool),
                    "-f",
                    "1",
                    "-singlefile",
                    "-r",
                    "150",
                    "-png",
                    str(path),
                    str(output_prefix),
                ],
                timeout=60,
            )
            candidate = temp_dir / "page.png"
            if render_timeout:
                render_message = "pdftoppm timeout"
            elif render_return == 0 and candidate.exists():
                image_path = candidate
            else:
                render_message = first_line(render_stderr)

        if image_path is None and mutool_tool is not None:
            image_pattern = temp_dir / "page-%d.png"
            render_return, _render_stdout, render_stderr, render_timeout = run_command(
                [
                    str(mutool_tool),
                    "draw",
                    "-q",
                    "-r",
                    "150",
                    "-o",
                    str(image_pattern),
                    str(path),
                    "1",
                ],
                timeout=60,
            )
            rendered_pages = sorted(temp_dir.glob("page-*.png"))
            if render_timeout:
                render_message = "mutool timeout"
            elif render_return == 0 and rendered_pages:
                image_path = rendered_pages[0]
            else:
                render_message = first_line(render_stderr) or render_message

        if image_path is None:
            return {
                "status": "render-error",
                "message": render_message or "nenhum renderizador gerou imagem",
            }

        image_size = ""
        if magick_tool is not None:
            size_return, size_stdout, _size_stderr, _size_timeout = run_command(
                [
                    str(magick_tool),
                    "identify",
                    "-format",
                    "%wx%h",
                    str(image_path),
                ],
                timeout=20,
            )
            if size_return == 0:
                image_size = size_stdout.strip()

        env = os.environ.copy()
        if os.environ.get("TESSDATA_PREFIX"):
            env["TESSDATA_PREFIX"] = os.environ["TESSDATA_PREFIX"]

        ocr_return, ocr_stdout, ocr_stderr, ocr_timeout = run_command(
            [
                str(tesseract_tool),
                str(image_path),
                "stdout",
                "-l",
                "por+eng",
                "--psm",
                "6",
            ],
            timeout=90,
            env=env,
        )
        if ocr_timeout:
            return {"status": "ocr-timeout", "image_size": image_size}
        if ocr_return != 0:
            return {
                "status": "ocr-error",
                "image_size": image_size,
                "message": first_line(ocr_stderr),
            }

        text = clean_text_block(ocr_stdout)
        return {
            "status": "ok",
            "image_size": image_size,
            "chars": len(text),
            "useful_text": looks_like_useful_text(text),
            "snippet": " ".join(text.split())[:240],
        }
    finally:
        # Windows can keep a short-lived handle after OCR/rendering; do not fail the audit
        # just because the temporary folder could not be deleted immediately.
        try:
            remove_tree_best_effort(temp_dir)
        except OSError:
            pass


def build_record(
    path: Path,
    *,
    tools: dict[str, Path | None],
    exif_metadata: dict[str, dict[str, Any]],
    ocr_results: dict[str, dict[str, Any]],
    skip_qpdf: bool,
    skip_text: bool,
    max_text_pages: int,
) -> dict[str, Any]:
    relative_root = path.relative_to(ROOT).as_posix()
    relative_acervo = path.relative_to(ACERVO_ROOT).as_posix()
    collection = collection_for(path)
    size_bytes = path.stat().st_size
    source_sha256 = file_sha256(path)
    pdfinfo = collect_pdfinfo(path, tools["pdfinfo"])
    exif = exif_metadata.get(path_key(path), {})
    qpdf = collect_qpdf_check(path, tools["qpdf"], skip=skip_qpdf)
    ocr_record = ocr_results.get(relative_root)
    sidecar_available = ocr_sidecar_is_available(ocr_record)

    page_count = pdfinfo.get("pages")
    if not isinstance(page_count, int):
        exif_page_count = exif.get("PageCount")
        if isinstance(exif_page_count, int):
            page_count = exif_page_count
        elif isinstance(exif_page_count, str) and exif_page_count.isdigit():
            page_count = int(exif_page_count)
        else:
            page_count = None

    encrypted = pdfinfo.get("encrypted")
    if not isinstance(encrypted, bool):
        encrypted_text = str(exif.get("Encrypted", "")).lower()
        encrypted = encrypted_text in {"yes", "true", "1"}

    if skip_text:
        extraction_method = "skipped"
        text_extractable = False
        text_chars = 0
    else:
        extraction = extract_pdf_text(path, max_pages=max_text_pages, timeout=30)
        extraction_method = extraction.method
        text_extractable = extraction.useful_text
        text_chars = len(extraction.text)

    ocr_priority, ocr_reason = classify_ocr(
        collection=collection,
        encrypted=encrypted,
        qpdf_status=str(qpdf["status"]),
        text_extractable=text_extractable,
        page_count=page_count,
        ocr_sidecar_available=sidecar_available,
    )
    companion_note = companion_note_info(path)

    return {
        "relative_path": relative_root,
        "acervo_relative_path": relative_acervo,
        "collection": collection,
        "file_name": path.name,
        "size_bytes": size_bytes,
        "size_label": human_size(size_bytes),
        "sha256": source_sha256,
        "pages": page_count,
        "pdf_version": pdfinfo.get("pdf_version") or exif.get("PDFVersion") or "",
        "encrypted": encrypted,
        "pdfinfo_status": pdfinfo.get("status", ""),
        "qpdf_status": qpdf["status"],
        "qpdf_messages": qpdf["messages"],
        "text_method": extraction_method,
        "text_extractable": text_extractable,
        "text_chars_sample": text_chars,
        "ocr_priority": ocr_priority,
        "ocr_reason": ocr_reason,
        "ocr_sidecar": ocr_record or {},
        "metadata": {
            "title": exif.get("Title") or pdfinfo.get("title") or "",
            "author": exif.get("Author") or pdfinfo.get("author") or "",
            "creator": exif.get("Creator") or pdfinfo.get("creator") or "",
            "producer": exif.get("Producer") or pdfinfo.get("producer") or "",
            "create_date": exif.get("CreateDate") or pdfinfo.get("creation_date") or "",
            "modify_date": exif.get("ModifyDate") or pdfinfo.get("mod_date") or "",
        },
        "companion_note": companion_note,
    }


def summarize(records: list[dict[str, Any]]) -> dict[str, Any]:
    duplicate_groups: list[dict[str, Any]] = []
    by_hash: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_hash[str(record["sha256"])].append(record)

    for sha_value, group in by_hash.items():
        if len(group) <= 1:
            continue
        duplicate_groups.append(
            {
                "sha256": sha_value,
                "count": len(group),
                "files": [item["relative_path"] for item in group],
            }
        )

    missing_companion = [
        record["relative_path"]
        for record in records
        if record["collection"] == "acervo-principal"
        and not record["companion_note"]["exists"]
    ]

    known_pages = [
        int(record["pages"])
        for record in records
        if isinstance(record.get("pages"), int)
    ]

    return {
        "total_pdfs": len(records),
        "total_size_bytes": sum(int(record["size_bytes"]) for record in records),
        "total_size_label": human_size(sum(int(record["size_bytes"]) for record in records)),
        "known_pages": sum(known_pages),
        "collections": dict(Counter(str(record["collection"]) for record in records)),
        "qpdf_status": dict(Counter(str(record["qpdf_status"]) for record in records)),
        "text_status": dict(
            Counter("sim" if record["text_extractable"] else "nao" for record in records)
        ),
        "text_methods": dict(Counter(str(record["text_method"]) for record in records)),
        "ocr_priorities": dict(Counter(str(record["ocr_priority"]) for record in records)),
        "encrypted": sum(1 for record in records if record["encrypted"]),
        "duplicate_groups": len(duplicate_groups),
        "duplicate_files": sum(len(group["files"]) for group in duplicate_groups),
        "missing_main_companion_notes": missing_companion,
        "duplicate_groups_detail": duplicate_groups,
    }


def render_tool_lines(tools: dict[str, dict[str, str]]) -> list[str]:
    lines: list[str] = []
    for name in TOOL_NAMES:
        info = tools[name]
        path = info["path"] or "missing"
        version = info["version"]
        lines.append(f"- `{name}`: `{version}` - `{path}`")
    return lines


def render_counter_lines(values: dict[str, Any]) -> list[str]:
    if not values:
        return ["- nenhum"]
    return [f"- `{key}`: `{value}`" for key, value in sorted(values.items())]


def render_record_link(record: dict[str, Any]) -> str:
    absolute = (ROOT / str(record["relative_path"])).resolve().as_posix()
    return f"[{record['file_name']}](</{absolute}>)"


def qpdf_issue_message(record: dict[str, Any]) -> str:
    messages = [str(message) for message in record.get("qpdf_messages", [])]
    priority_lines = [
        message
        for message in messages
        if "warning" in message.lower() or "error" in message.lower()
    ]
    selected = priority_lines[:2] or messages[:2]
    return "; ".join(selected) or "sem mensagem"


def render_report(
    *,
    records: list[dict[str, Any]],
    summary: dict[str, Any],
    tools: dict[str, dict[str, str]],
    scope: str,
    ocr_sample_limit: int,
) -> str:
    generated_at = datetime.now(timezone.utc).isoformat()
    reviewed_on = datetime.now().date().isoformat()
    ocr_queue = [
        record
        for record in records
        if record["ocr_priority"] in {"alta", "media", "reparar-primeiro", "bloqueado"}
    ]
    ocr_queue.sort(
        key=lambda item: (
            {"alta": 0, "media": 1, "reparar-primeiro": 2, "bloqueado": 3}.get(
                str(item["ocr_priority"]),
                9,
            ),
            str(item["relative_path"]).casefold(),
        )
    )

    qpdf_issues = [
        record
        for record in records
        if record["qpdf_status"] not in {"ok", "skipped", "missing-tool"}
    ]
    qpdf_issues.sort(
        key=lambda item: (
            0 if item["collection"] == "acervo-principal" else 1,
            str(item["relative_path"]).casefold(),
        )
    )
    large_files = sorted(records, key=lambda item: int(item["size_bytes"]), reverse=True)[:20]
    duplicate_groups = summary["duplicate_groups_detail"][:20]
    main_records = [
        record for record in records if record["collection"] == "acervo-principal"
    ]
    main_qpdf = dict(Counter(str(record["qpdf_status"]) for record in main_records))
    main_text = dict(
        Counter("sim" if record["text_extractable"] else "nao" for record in main_records)
    )
    main_ocr = dict(Counter(str(record["ocr_priority"]) for record in main_records))

    lines: list[str] = [
        "---",
        'title: "Auditoria Operacional PDF - Toolchain"',
        'note_type: "audit"',
        'domain: "90_Revisao_Manual"',
        'status: "auto-generated"',
        f'reviewed_on: "{reviewed_on}"',
        'review_jurisdiction: "Brasil"',
        "related_notes:",
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Local - Indice Gerado"',
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado"',
        "---",
        "",
        "# Auditoria Operacional PDF - Toolchain",
        "",
        "> [!abstract] Resumo tecnico",
        "> Relatorio gerado com Poppler, qpdf, ExifTool, Tesseract, MuPDF, ImageMagick, Ghostscript e 7-Zip instalados no ambiente.",
        "> Objetivo: transformar os PDFs em acervo auditavel, pesquisavel e pronto para filas de OCR/curadoria.",
        "",
        "> [!info] Geracao",
        "> Comando: `python scripts/acervo/audit_pdf_toolchain.py --scope all`.",
        f"> Escopo desta execucao: `{scope}`.",
        f"> Gerado em `{generated_at}`.",
        "",
        "## Resultado executivo",
        "",
        f"- PDFs auditados: `{summary['total_pdfs']}`",
        f"- tamanho total auditado: `{summary['total_size_label']}`",
        f"- paginas conhecidas somadas: `{summary['known_pages']}`",
        f"- PDFs criptografados: `{summary['encrypted']}`",
        f"- grupos de duplicatas fisicas por SHA-256: `{summary['duplicate_groups']}`",
        f"- arquivos envolvidos em duplicatas: `{summary['duplicate_files']}`",
        f"- notas companheiras faltantes no acervo principal: `{len(summary['missing_main_companion_notes'])}`",
        f"- OCR amostral executado em: `{ocr_sample_limit}` candidato(s)",
        "",
        "## Ferramentas detectadas",
        "",
    ]
    lines.extend(render_tool_lines(tools))

    lines.extend(["", "## Recorte do acervo principal", ""])
    lines.append(f"- PDFs curados: `{len(main_records)}`")
    lines.append(
        f"- paginas conhecidas: `{sum(int(record['pages']) for record in main_records if isinstance(record.get('pages'), int))}`"
    )
    lines.append(
        f"- qpdf: `{', '.join(f'{key}:{value}' for key, value in sorted(main_qpdf.items()))}`"
    )
    lines.append(
        f"- texto pesquisavel: `{', '.join(f'{key}:{value}' for key, value in sorted(main_text.items()))}`"
    )
    lines.append(
        f"- OCR: `{', '.join(f'{key}:{value}' for key, value in sorted(main_ocr.items()))}`"
    )

    lines.extend(["", "## Distribuicao por colecao", ""])
    lines.extend(render_counter_lines(summary["collections"]))
    lines.extend(["", "## Status estrutural qpdf", ""])
    lines.extend(render_counter_lines(summary["qpdf_status"]))
    lines.extend(["", "## Texto pesquisavel", ""])
    lines.extend(render_counter_lines(summary["text_status"]))
    lines.extend(["", "## Metodos de texto", ""])
    lines.extend(render_counter_lines(summary["text_methods"]))
    lines.extend(["", "## Prioridade de OCR", ""])
    lines.extend(render_counter_lines(summary["ocr_priorities"]))

    lines.extend(["", "## Fila operacional de OCR", ""])
    if not ocr_queue:
        lines.append("- nenhum candidato prioritario")
    for record in ocr_queue[:40]:
        pages = record["pages"] if record["pages"] is not None else "?"
        sample = record.get("ocr_sample")
        sample_label = ""
        if isinstance(sample, dict):
            sample_label = f" - OCR amostral: `{sample.get('status')}`"
            if sample.get("chars") is not None:
                sample_label += f", `{sample.get('chars')}` chars"
        lines.append(
            f"- `{record['ocr_priority']}` - {render_record_link(record)} - "
            f"`{record['collection']}` - `{pages}` pag. - {record['ocr_reason']}{sample_label}"
        )

    lines.extend(["", "## Problemas estruturais ou de leitura", ""])
    if not qpdf_issues:
        lines.append("- nenhum problema estrutural detectado por qpdf")
    for record in qpdf_issues[:40]:
        message = qpdf_issue_message(record)
        lines.append(
            f"- `{record['qpdf_status']}` - {render_record_link(record)} - `{message}`"
        )

    lines.extend(["", "## Maiores PDFs", ""])
    for record in large_files:
        pages = record["pages"] if record["pages"] is not None else "?"
        lines.append(
            f"- {render_record_link(record)} - `{record['size_label']}` - `{pages}` pag. - `{record['collection']}`"
        )

    lines.extend(["", "## Duplicatas fisicas", ""])
    if not duplicate_groups:
        lines.append("- nenhum grupo de duplicatas fisicas detectado")
    for group in duplicate_groups:
        lines.append(f"- `sha256 {group['sha256'][:12]}` - `{group['count']}` arquivos")
        for file_path in group["files"][:6]:
            lines.append(f"- `{file_path}`")

    missing_notes = summary["missing_main_companion_notes"]
    lines.extend(["", "## Pendencias de nota companheira", ""])
    if not missing_notes:
        lines.append("- nenhuma pendencia no acervo principal")
    for file_path in missing_notes:
        lines.append(f"- `{file_path}`")

    lines.extend(
        [
            "",
            "## Rotina recomendada",
            "",
            "- Rodar esta auditoria sempre que PDF novo entrar no acervo ou staging.",
            "- Rodar `build_pdf_companion_notes.py` depois da auditoria para as notas principais herdarem paginas, qpdf e prioridade de OCR.",
            "- Usar OCR pesado apenas nos itens `alta` e `media`, evitando gastar tempo em duplicata, fora de escopo ou material pessoal.",
            "- Nao compactar ou regravar PDFs originais sem copia reversivel; usar qpdf/Ghostscript primeiro em modo diagnostico.",
            "",
        ]
    )
    return "\n".join(lines)


def build_tools_payload() -> tuple[dict[str, Path | None], dict[str, dict[str, str]]]:
    tool_paths = {name: find_tool(name) for name in TOOL_NAMES}
    tool_payload = {
        name: {
            "path": str(tool_paths[name]) if tool_paths[name] else "",
            "version": tool_version(name, tool_paths[name]),
        }
        for name in TOOL_NAMES
    }
    languages = tesseract_languages(tool_paths["tesseract"])
    tool_payload["tesseract"]["languages"] = ", ".join(languages)
    return tool_paths, tool_payload


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audita PDFs do acervo usando ferramentas externas de PDF/OCR."
    )
    parser.add_argument(
        "--scope",
        choices=("all", "main", "staging"),
        default="all",
        help="Escopo de PDFs a auditar.",
    )
    parser.add_argument(
        "--max-files",
        type=int,
        default=0,
        help="Limita quantidade de PDFs para teste. 0 audita todos do escopo.",
    )
    parser.add_argument(
        "--max-text-pages",
        type=int,
        default=2,
        help="Paginas iniciais usadas para estimar texto pesquisavel.",
    )
    parser.add_argument(
        "--ocr-sample-limit",
        type=int,
        default=8,
        help="Quantidade de candidatos prioritarios em que o OCR da primeira pagina sera testado.",
    )
    parser.add_argument(
        "--skip-qpdf",
        action="store_true",
        help="Pula qpdf --check para rodada mais rapida.",
    )
    parser.add_argument(
        "--skip-text",
        action="store_true",
        help="Pula extracao textual para rodada mais rapida.",
    )
    parser.add_argument(
        "--json-path",
        type=Path,
        default=MANIFEST_PATH,
        help="Destino do manifesto JSON.",
    )
    parser.add_argument(
        "--report-path",
        type=Path,
        default=REPORT_PATH,
        help="Destino do relatorio Markdown.",
    )
    return parser.parse_args()


def main() -> int:
    add_user_environment_defaults()
    args = parse_args()

    pdf_paths = iter_pdf_paths(args.scope)
    if args.max_files and args.max_files > 0:
        pdf_paths = pdf_paths[: args.max_files]

    tool_paths, tool_payload = build_tools_payload()
    exif_metadata = collect_exif_metadata(pdf_paths, tool_paths["exiftool"])
    ocr_results = load_ocr_results()

    records: list[dict[str, Any]] = []
    total = len(pdf_paths)
    for index, path in enumerate(pdf_paths, start=1):
        print(f"[{index}/{total}] {path.relative_to(ROOT).as_posix()}")
        record = build_record(
            path,
            tools=tool_paths,
            exif_metadata=exif_metadata,
            ocr_results=ocr_results,
            skip_qpdf=args.skip_qpdf,
            skip_text=args.skip_text,
            max_text_pages=args.max_text_pages,
        )
        records.append(record)

    ocr_candidates = [
        record
        for record in records
        if record["ocr_priority"] in {"alta", "media"}
        and record["qpdf_status"] == "ok"
        and not record["encrypted"]
    ]
    ocr_candidates.sort(
        key=lambda item: (
            {"alta": 0, "media": 1}.get(str(item["ocr_priority"]), 9),
            str(item["relative_path"]).casefold(),
        )
    )

    for record in ocr_candidates[: max(args.ocr_sample_limit, 0)]:
        pdf_path = ROOT / str(record["relative_path"])
        print(f"OCR amostral: {record['relative_path']}")
        record["ocr_sample"] = ocr_first_page(
            pdf_path,
            tesseract_tool=tool_paths["tesseract"],
            pdftoppm_tool=tool_paths["pdftoppm"],
            mutool_tool=tool_paths["mutool"],
            magick_tool=tool_paths["magick"],
        )

    summary = summarize(records)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "scope": args.scope,
        "tools": tool_payload,
        "summary": summary,
        "pdfs": records,
    }
    write_json(args.json_path, payload)

    report = render_report(
        records=records,
        summary=summary,
        tools=tool_payload,
        scope=args.scope,
        ocr_sample_limit=min(len(ocr_candidates), max(args.ocr_sample_limit, 0)),
    )
    args.report_path.parent.mkdir(parents=True, exist_ok=True)
    args.report_path.write_text(report, encoding="utf-8", newline="\n")

    print("")
    print(f"PDFs auditados: {summary['total_pdfs']}")
    print(f"Manifesto: {args.json_path.relative_to(ROOT).as_posix()}")
    print(f"Relatorio: {args.report_path.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
