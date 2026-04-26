from __future__ import annotations

import os
import re
import shutil
import subprocess
import zlib
from dataclasses import dataclass
from pathlib import Path


PDFTOTEXT_CANDIDATES = (
    r"C:\Program Files\Git\mingw64\bin\pdftotext.exe",
    r"C:\Program Files\poppler\bin\pdftotext.exe",
)


@dataclass(frozen=True, slots=True)
class PdfTextResult:
    text: str
    method: str
    useful_text: bool


def path_arg(path: Path) -> str:
    resolved = str(path.resolve())
    if os.name == "nt" and not resolved.startswith("\\\\?\\"):
        return "\\\\?\\" + resolved
    return resolved


def clean_pdf_string(value: str) -> str:
    compact = value.replace("\x00", " ").replace("\x0c", " ")
    return " ".join(compact.split())


def clean_text_block(value: str) -> str:
    normalized = value.replace("\x00", " ").replace("\x0c", "\n")
    lines = [" ".join(line.split()) for line in normalized.splitlines()]
    return "\n".join(line for line in lines if line)


def find_pdftotext() -> Path | None:
    environment_path = os.environ.get("PDFTOTEXT_PATH")
    if environment_path:
        candidate = Path(environment_path)
        if candidate.exists():
            return candidate

    executable = shutil.which("pdftotext")
    if executable:
        return Path(executable)

    for candidate in PDFTOTEXT_CANDIDATES:
        path = Path(candidate)
        if path.exists():
            return path

    return None


def looks_like_useful_text(value: str) -> bool:
    compact = " ".join(clean_text_block(value).split())
    if len(compact) < 80:
        return False

    words = re.findall(r"[A-Za-z][A-Za-z0-9/+._:-]{2,}", compact)
    return len(words) >= 12


def extract_text_with_pdftotext(
    path: Path,
    *,
    max_pages: int = 3,
    timeout: int = 30,
) -> str:
    tool = find_pdftotext()
    if tool is None:
        return ""

    try:
        result = subprocess.run(
            [
                str(tool),
                "-enc",
                "UTF-8",
                "-nopgbrk",
                "-f",
                "1",
                "-l",
                str(max_pages),
                path_arg(path),
                "-",
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            timeout=timeout,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return ""

    if result.returncode != 0:
        return ""

    return clean_text_block(result.stdout)


def extract_stream_strings(
    path: Path,
    *,
    max_streams: int = 100,
    max_items: int = 300,
) -> list[str]:
    try:
        with open(path_arg(path), "rb") as handle:
            data = handle.read()
    except OSError:
        return []

    snippets: list[str] = []
    seen: set[str] = set()

    def push(value: str) -> None:
        cleaned = clean_pdf_string(value)
        if len(cleaned) < 4:
            return
        key = cleaned.casefold()
        if key in seen:
            return
        seen.add(key)
        snippets.append(cleaned)

    for pattern in (
        rb"/Title\s*\((.*?)\)",
        rb"/Subject\s*\((.*?)\)",
        rb"/Author\s*\((.*?)\)",
    ):
        for raw in re.findall(pattern, data):
            push(raw.decode("latin1", "ignore"))

    streams = re.findall(rb"stream\r?\n(.*?)\r?\nendstream", data, re.S)
    for stream in streams[:max_streams]:
        try:
            decoded = zlib.decompress(stream)
        except Exception:
            continue

        for raw in re.findall(rb"\(([^()]*)\)", decoded):
            push(raw.decode("latin1", "ignore"))

        for raw in re.findall(rb"[A-Za-z0-9][A-Za-z0-9 /+._:-]{6,120}", decoded):
            push(raw.decode("latin1", "ignore"))

        if len(snippets) >= max_items:
            break

    return snippets[:max_items]


def extract_pdf_text(
    path: Path,
    *,
    max_pages: int = 3,
    timeout: int = 30,
) -> PdfTextResult:
    direct_text = extract_text_with_pdftotext(path, max_pages=max_pages, timeout=timeout)
    if looks_like_useful_text(direct_text):
        return PdfTextResult(direct_text, "pdftotext", True)

    fallback_lines = extract_stream_strings(path)
    fallback_text = clean_text_block("\n".join(fallback_lines))
    if looks_like_useful_text(fallback_text):
        return PdfTextResult(fallback_text, "pdf-stream-strings", True)

    if fallback_text:
        return PdfTextResult(fallback_text, "pdf-stream-strings-low-confidence", False)

    return PdfTextResult("", "no-text-detected", False)
