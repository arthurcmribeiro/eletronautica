from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent

if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.append(str(SCRIPTS_ROOT))
if str(SCRIPT_DIR) not in sys.path:
    sys.path.append(str(SCRIPT_DIR))

from vault_tools import ROOT  # noqa: E402
from acervo.build_pdf_companion_notes import (  # noqa: E402
    build_snippets,
    detect_brand_signals,
    detect_document_kind,
    detect_model_signals,
    detect_term_signals,
    join_or_na,
)
from acervo.pdf_text_tools import (  # noqa: E402
    clean_text_block,
    extract_pdf_text,
    looks_like_useful_text,
)
from acervo.promote_human_archive_to_main import PROMOTIONS  # noqa: E402


STAGING_ROOT = (
    ROOT
    / "90_Revisao_Manual"
    / "_Acervo_Local"
    / "Acervo do humano"
    / "10_Tecnico_Nautico"
)
NOTES_ROOT = (
    ROOT
    / "90_Revisao_Manual"
    / "_Acervo_Notas"
    / "Acervo do humano"
    / "10_Tecnico_Nautico"
)
INDEX_NOTE_PATH = (
    ROOT
    / "90_Revisao_Manual"
    / "10_Indices_e_Paineis"
    / "Acervo Humano Tecnico - Indice Gerado.md"
)
NON_PDF_INDEX_NOTE_PATH = (
    ROOT
    / "90_Revisao_Manual"
    / "10_Indices_e_Paineis"
    / "Acervo Humano Tecnico - Nao PDF - Indice Gerado.md"
)
DUPLICATE_NOTE_PATH = (
    ROOT
    / "90_Revisao_Manual"
    / "10_Indices_e_Paineis"
    / "Acervo Humano Tecnico - Manifesto de Duplicatas.md"
)
QUEUE_NOTE_PATH = (
    ROOT
    / "90_Revisao_Manual"
    / "10_Indices_e_Paineis"
    / "Acervo Humano Tecnico - Fila de Resolucao de Duplicatas.md"
)
DUPLICATE_JSON_PATH = ROOT / "manifest" / "acervo-humano-duplicates.json"
NON_PDF_JSON_PATH = ROOT / "manifest" / "acervo-humano-non-pdf-support.json"
NON_PDF_REPORT_PATH = ROOT / "_Editorial" / "Normalizacao Nao PDF - Acervo Humano Tecnico.md"
NON_PDF_TEXT_ROOT = ROOT / "90_Revisao_Manual" / "_Dados_Acervo" / "non_pdf_texts"

TEXT_EXTENSIONS = {".pdf", ".html", ".htm"}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}
NON_PDF_INDEXED_EXTENSIONS = {".html", ".htm", ".jpg", ".jpeg", ".png"}
INDEXED_TEXT_LIMIT = 12000
TESSERACT_CANDIDATES = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
)
LOW_SIGNAL_MODEL_BUCKETS = {
    "00_Documentacao_de_Campo_e_Clientes",
    "10_Materiais_Internos_e_Cursos",
    "11_HTML_Tecnico_Exportado",
}
STAGING_MODEL_STOPWORDS = {
    "ANALISE",
    "AUDIO",
    "CAMERA",
    "CLIENTES",
    "COMMAND",
    "CURSOS",
    "DIAGRAMA",
    "DIAGRAMAS",
    "ELECTRICAL",
    "ELETRICA",
    "ENERGY",
    "EQUIPA",
    "ESBOCO",
    "ESQUEMATICO",
    "ESTUDO",
    "ESTUDOS",
    "FIELD",
    "FUNDAMENTOS",
    "FUSION",
    "GENSET",
    "GERADORES",
    "GUIDE",
    "HIDRAULICO",
    "INSTALACAO",
    "INTERNOS",
    "LIGACAO",
    "MATERIAIS",
    "MOTORES",
    "NAUTICA",
    "PRODUCTS",
    "PROPULSAO",
    "RAPHAEL",
    "RADAR",
    "REFERENCE",
    "RESIDUAL",
    "SERVICE",
    "SISTEMA",
    "TECHNICAL",
    "TRANSDUCERS",
    "TURBO",
}
GENERIC_CONTEXT_HINTS = {
    "98 Duplicatas",
    "99 Fora do Escopo ou Pessoal",
    "ZZ Residual Manual",
}

CATEGORY_LABELS = {
    "00_Documentacao_de_Campo_e_Clientes": "Documentacao de Campo e Clientes",
    "01_Geradores": "Geradores",
    "02_Climatizacao": "Climatizacao",
    "03_Baterias_e_DC": "Baterias e DC",
    "04_Shore_Power_e_AC": "Shore Power e AC",
    "05_Navegacao_e_Eletronicos": "Navegacao e Eletronicos",
    "06_Bombas_Hidraulica_e_Utilidades": "Bombas, Hidraulica e Utilidades",
    "07_Iluminacao_Sinalizacao_e_Acessorios": "Iluminacao, Sinalizacao e Acessorios",
    "08_Corrosao_Bonding_e_Seguranca": "Corrosao, Bonding e Seguranca",
    "09_Propulsao_Motores_Estabilizacao_e_Atuacao": "Propulsao, Motores, Estabilizacao e Atuacao",
    "10_Materiais_Internos_e_Cursos": "Materiais Internos e Cursos",
    "11_HTML_Tecnico_Exportado": "HTML Tecnico Exportado",
    "90_Triagem_Tecnica_por_Codigo": "Triagem Tecnica por Codigo",
}

CATEGORY_SYSTEMS = {
    "00_Documentacao_de_Campo_e_Clientes": "Campo-Clientes",
    "01_Geradores": "Geradores",
    "02_Climatizacao": "Climatizacao",
    "03_Baterias_e_DC": "Baterias-DC",
    "04_Shore_Power_e_AC": "Shore-Power-AC",
    "05_Navegacao_e_Eletronicos": "Navegacao",
    "06_Bombas_Hidraulica_e_Utilidades": "Bombas-Utilidades",
    "07_Iluminacao_Sinalizacao_e_Acessorios": "Iluminacao-Acessorios",
    "08_Corrosao_Bonding_e_Seguranca": "Corrosao-Seguranca",
    "09_Propulsao_Motores_Estabilizacao_e_Atuacao": "Propulsao-Motores",
    "10_Materiais_Internos_e_Cursos": "Materiais-Internos",
    "11_HTML_Tecnico_Exportado": "HTML-Tecnico",
    "90_Triagem_Tecnica_por_Codigo": "Triagem-Tecnica",
}

DUPLICATE_PRIORITY_BUCKET_ORDER = {
    "01_Geradores": 0,
    "04_Shore_Power_e_AC": 1,
    "03_Baterias_e_DC": 2,
    "05_Navegacao_e_Eletronicos": 3,
    "02_Climatizacao": 4,
    "06_Bombas_Hidraulica_e_Utilidades": 5,
    "08_Corrosao_Bonding_e_Seguranca": 6,
    "09_Propulsao_Motores_Estabilizacao_e_Atuacao": 7,
    "90_Triagem_Tecnica_por_Codigo": 8,
    "00_Documentacao_de_Campo_e_Clientes": 9,
    "10_Materiais_Internos_e_Cursos": 10,
    "11_HTML_Tecnico_Exportado": 11,
}
RESOLUTION_PRIORITY_ORDER = {"alta": 0, "media": 1, "baixa": 2}

DOC_REPLACEMENTS = (
    (r"\btech\s*specs?\b", "technical specifications"),
    (r"\btechnical\s+specs?\b", "technical specifications"),
    (r"\boperator[' ]?s?\s+manual\b", "operator manual"),
    (r"\boperator\s+man\b", "operator manual"),
    (r"\boperation\b", "operation manual"),
    (r"\bowners?\s+manual\b", "owners manual"),
    (r"\bservice\s+manual\b", "service manual"),
    (r"\bparts\s+manual\b", "parts manual"),
    (r"\binstall(?:ation)?\b", "installation"),
    (r"\binst\b", "installation"),
    (r"\bsupplemental\s+instructions\b", "supplemental instructions"),
    (r"\btroubleshooting\b", "troubleshooting guide"),
    (r"\bqsg\b", "quick start guide"),
    (r"\bom\b", "operator manual"),
    (r"\bopm\b", "operator manual"),
)

LOW_INFORMATION_RE = re.compile(
    r"^(?:"
    r"[a-f0-9]{12,}"
    r"|[0-9]{3,}"
    r"|manual[-_ ]+[0-9a-f]{8,}"
    r"|arquivo[-_ ]+[0-9a-f]{8,}"
    r"|[0-9a-f]{8}-[0-9a-f-]{20,}"
    r")$",
    re.I,
)

HTML_TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
HTML_H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.I | re.S)
HTML_TAG_RE = re.compile(r"<[^>]+>")
HTML_SCRIPT_STYLE_RE = re.compile(r"<(script|style)[^>]*>.*?</\1>", re.I | re.S)
TEMP_RENAME_RE = re.compile(r"^_*(?:tmp\d*)-renomear-\d{4}(?:-\d+)?$", re.I)
HASH_SUFFIX_RE = re.compile(r"-[0-9a-f]{8}$", re.I)
DUP_SUFFIX_RE = re.compile(r"-dup-\d+$", re.I)
GENERIC_DOC_STEM_RE = re.compile(
    r"^(?:guide|manual|owner-s-manual|operator-s-manual|reference|service-manual|technical-manual|technical-reference)$",
    re.I,
)
DOCUMENT_MARKER_RE = re.compile(
    r"(catalog|guide|installation|manual|operation|operator|parts|service|technical|troubleshooting|__)",
    re.I,
)
GENERIC_FILENAME_HINTS = {
    "doc",
    "download",
    "printed",
    "quick",
}
CURATION_BLOCK_RE = re.compile(
    r"<!-- CURADORIA-HUMANA:START -->.*?<!-- CURADORIA-HUMANA:END -->",
    re.S,
)
FRONTMATTER_RE = re.compile(r"(?s)^---\n(.*?)\n---\n?(.*)$")
FRONTMATTER_FIELD_RE = re.compile(r'^([A-Za-z0-9_]+): "(.*)"$', re.M)


def io_path(path: Path) -> str:
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
    for dirpath, _dirnames, filenames in os.walk(io_path(root)):
        for filename in filenames:
            files.append(Path(strip_long_prefix(os.path.join(dirpath, filename))))
    return sorted(files, key=lambda item: item.as_posix().casefold())


def path_exists(path: Path) -> bool:
    return os.path.exists(io_path(path))


def file_size(path: Path) -> int:
    return os.path.getsize(io_path(path))


@dataclass(slots=True)
class ArchiveFileRecord:
    source_path: Path
    original_relative: str
    renamed_relative: str
    note_relative: str
    note_path: Path
    title: str
    category_key: str
    category_label: str
    system: str
    extension: str
    original_name: str
    renamed_name: str
    document_kind: str
    curation_priority: str
    curation_stage: str
    note_status: str
    brand_label: str
    source_sha256: str
    extraction_method: str
    text_extractable: str
    size_label: str
    extracted_text_chars: int
    indexed_text_path: str
    indexed_text: str
    detected_brands: list[str]
    detected_models: list[str]
    detected_terms: list[str]
    snippets: list[str]
    family_hint: str
    curation_block: str = ""
    duplicate_status: str = "unique"
    duplicate_group_sha256: str = ""
    duplicate_group_size: int = 1
    duplicate_canonical_relative: str = ""
    duplicate_canonical_note_relative: str = ""


@dataclass(frozen=True, slots=True)
class ExtractionBundle:
    text: str
    method: str
    useful: bool


@dataclass(slots=True)
class ExistingNoteState:
    curation_block: str | None = None
    curation_priority: str | None = None
    curation_stage: str | None = None
    status: str | None = None
    title: str | None = None
    document_kind: str | None = None
    acervo_brand: str | None = None
    acervo_family: str | None = None


@dataclass(frozen=True, slots=True)
class DuplicateGroup:
    sha256: str
    canonical: ArchiveFileRecord
    members: tuple[ArchiveFileRecord, ...]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with open(io_path(path), "rb") as handle:
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


def absolute_link(path: Path) -> str:
    return strip_long_prefix(os.path.abspath(str(path))).replace("\\", "/")


def normalize_ascii(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    without_accents = "".join(
        character for character in normalized if not unicodedata.combining(character)
    )
    return without_accents


def clean_source_stem(stem: str) -> str:
    cleaned = stem.strip()
    cleaned = re.sub(r"(?:\.(pdf|html?|jpe?g|png))+$", "", cleaned, flags=re.I)
    cleaned = re.sub(r"\s+\((\d+)\)$", "", cleaned)
    cleaned = re.sub(r"\s+\[[0-9]+\]$", "", cleaned)
    cleaned = re.sub(r"_compressed$", "", cleaned, flags=re.I)
    cleaned = re.sub(r"_copy$", "", cleaned, flags=re.I)
    cleaned = cleaned.replace("__", " ")
    cleaned = cleaned.replace("_", " ")
    cleaned = re.sub(r"\b(pdf|html?|jpe?g|png)\b$", "", cleaned, flags=re.I)
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.strip()


def strip_numeric_prefix(value: str) -> str:
    return re.sub(r"^\d+\s*", "", value).strip()


def normalize_doc_markers(text: str) -> str:
    value = normalize_ascii(text).lower()
    value = value.replace("&", " and ")
    value = value.replace("/", " ")
    value = value.replace("+", " ")
    for pattern, replacement in DOC_REPLACEMENTS:
        value = re.sub(pattern, replacement, value, flags=re.I)
    value = re.sub(r"[\(\)\[\]\{\},;:]", " ", value)
    value = re.sub(r"\bpdf\b", " ", value)
    value = re.sub(r"\b(operation|operator|owners|service|parts|installation)\s+manual\s+manual\b", r"\1 manual", value)
    value = re.sub(r"\bguide\s+guide\b", "guide", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def slugify_filename(text: str) -> str:
    normalized = normalize_doc_markers(text)
    normalized = normalized.replace("'", "")
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized)
    normalized = re.sub(r"-{2,}", "-", normalized)
    slug = normalized.strip("-")
    slug = re.sub(r"(?:-manual){2,}$", "-manual", slug)
    slug = re.sub(r"(?:-guide){2,}$", "-guide", slug)

    parts = [part for part in slug.split("-") if part]
    half = len(parts) // 2
    if len(parts) >= 4 and len(parts) % 2 == 0 and parts[:half] == parts[half:]:
        slug = "-".join(parts[:half])

    return slug


def title_from_slug(stem: str) -> str:
    if "__" in stem:
        return stem.replace("__", " - ").replace("_", " ").strip()
    return stem.replace("-", " ").strip()


def sanitize_promoted_basename(relative_path: str) -> str | None:
    normalized = relative_path.replace("\\", "/")
    for promotion in PROMOTIONS:
        if promotion.source_rel != normalized:
            continue
        basenames = {Path(target).name for target in promotion.targets}
        if len(basenames) == 1:
            return basenames.pop()
    return None


def is_low_information_stem(stem: str) -> bool:
    if TEMP_RENAME_RE.fullmatch(stem.strip()):
        return True
    candidate = normalize_ascii(stem).lower().strip()
    if re.search(r"(?:^|[-_ ])[a-f0-9]{12,}$", candidate):
        return True
    return bool(LOW_INFORMATION_RE.fullmatch(candidate))


def has_contextual_hash_suffix(stem: str) -> bool:
    return bool(HASH_SUFFIX_RE.search(normalize_ascii(stem).lower().strip()))


def best_context_hint(path: Path) -> str:
    relative = path.relative_to(STAGING_ROOT)
    for part in reversed(relative.parts[:-1]):
        cleaned = strip_numeric_prefix(clean_source_stem(part))
        if not cleaned:
            continue
        if cleaned in GENERIC_CONTEXT_HINTS:
            continue
        if "duplicat" in cleaned.casefold():
            continue
        return cleaned
    return "arquivo tecnico"


def build_fallback_title_hint(path: Path) -> str:
    context = best_context_hint(path)
    digest = sha256(path)[:8]
    suffix = path.suffix.lower().lstrip(".") or "arquivo"
    return f"{context} {suffix} {digest}"


def build_traceable_stem_hint(stem: str) -> str:
    if TEMP_RENAME_RE.fullmatch(stem.strip()):
        return ""
    cleaned = clean_source_stem(stem)
    cleaned = re.sub(r"(?i)[\s_-]*[a-f0-9]{12,}$", "", cleaned)
    cleaned = re.sub(r"(?i)[\s_-]*\d{3,}$", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" -_")
    return cleaned or clean_source_stem(stem)


def first_meaningful_line(text: str) -> str:
    for raw_line in text.splitlines():
        line = " ".join(raw_line.split())
        if len(line) < 12:
            continue
        lowered = line.casefold()
        if lowered.startswith("page "):
            continue
        if re.fullmatch(r"[-_/0-9 ]+", line):
            continue
        return line[:160].strip()
    return ""


def extract_html_text(path: Path) -> tuple[str, str, bool]:
    try:
        with open(io_path(path), "r", encoding="utf-8", errors="replace") as handle:
            raw = handle.read()
    except OSError:
        return "", "html-read-failed", False

    raw = HTML_SCRIPT_STYLE_RE.sub(" ", raw)
    title_parts: list[str] = []

    title_match = HTML_TITLE_RE.search(raw)
    if title_match:
        title_parts.append(html.unescape(HTML_TAG_RE.sub(" ", title_match.group(1))))

    h1_match = HTML_H1_RE.search(raw)
    if h1_match:
        title_parts.append(html.unescape(HTML_TAG_RE.sub(" ", h1_match.group(1))))

    body_text = html.unescape(HTML_TAG_RE.sub(" ", raw))
    content = clean_text_block("\n".join(part for part in title_parts if part) + "\n" + body_text)
    useful = looks_like_useful_text(content)
    return content, "html-title-body", useful


def find_tesseract() -> Path | None:
    executable = shutil.which("tesseract")
    if executable:
        return Path(executable)

    for candidate in TESSERACT_CANDIDATES:
        path = Path(candidate)
        if path_exists(path):
            return path

    return None


def extract_image_text(path: Path) -> tuple[str, str, bool]:
    tool = find_tesseract()
    if tool is None:
        return "", "image-ocr-unavailable", False

    for language in ("por+eng", "eng"):
        try:
            result = subprocess.run(
                [
                    str(tool),
                    io_path(path),
                    "stdout",
                    "-l",
                    language,
                    "--psm",
                    "6",
                ],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=90,
                check=False,
            )
        except (OSError, subprocess.SubprocessError):
            continue

        text = clean_text_block(result.stdout)
        if result.returncode == 0 and text:
            return text, f"tesseract-ocr-{language}", looks_like_useful_text(text)

    return "", "tesseract-ocr-failed", False


def extract_file_text(path: Path) -> tuple[str, str, bool]:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        result = extract_pdf_text(path)
        return result.text, result.method, result.useful_text
    if suffix in {".html", ".htm"}:
        return extract_html_text(path)
    if suffix in IMAGE_EXTENSIONS:
        return extract_image_text(path)
    return "", "binary-no-text", False


def build_indexed_text(path: Path, extracted_text: str, useful: bool) -> str:
    extension = path.suffix.lower()
    if extension not in NON_PDF_INDEXED_EXTENSIONS:
        return ""

    cleaned = clean_text_block(extracted_text)
    if not cleaned:
        return ""

    min_chars = 10 if extension in {".html", ".htm"} else 20
    if not useful and len(cleaned) < min_chars:
        return ""

    if len(cleaned) <= INDEXED_TEXT_LIMIT:
        return cleaned

    return (
        cleaned[:INDEXED_TEXT_LIMIT].rstrip()
        + "\n\n[TRUNCADO: texto completo preservado no sidecar gerado.]"
    )


def text_sidecar_relative(note_relative_path: Path, extension: str) -> str:
    if extension not in NON_PDF_INDEXED_EXTENSIONS:
        return ""
    return (
        Path("90_Revisao_Manual")
        / "_Dados_Acervo"
        / "non_pdf_texts"
        / note_relative_path.with_suffix(".txt")
    ).as_posix()


def build_search_title_hint(path: Path, extracted_text: str) -> str:
    if not is_low_information_stem(path.stem):
        return clean_source_stem(path.stem)
    line = first_meaningful_line(extracted_text)
    if line:
        traceable = build_traceable_stem_hint(path.stem)
        if traceable:
            if slugify_filename(traceable) == slugify_filename(line):
                return line
            return f"{traceable} {line}"
        return line
    return build_fallback_title_hint(path)


def determine_target_name(path: Path, extracted_text: str) -> str:
    normalized_suffix = path.suffix.lower()
    if is_preferred_current_name(path):
        stem = trim_stem_for_path(stem=path.stem, suffix=normalized_suffix, parent=path.parent)
        return f"{stem}{normalized_suffix}"

    relative_path = path.relative_to(STAGING_ROOT).as_posix()
    promoted = sanitize_promoted_basename(relative_path)
    if promoted:
        return promoted

    title_hint = build_search_title_hint(path, extracted_text)
    slug = slugify_filename(title_hint)
    if not slug:
        slug = slugify_filename(path.stem) or "arquivo-tecnico"
    slug = trim_slug_for_path(slug=slug, suffix=normalized_suffix, parent=path.parent)
    return f"{slug}{normalized_suffix}"


def trim_slug_for_path(*, slug: str, suffix: str, parent: Path) -> str:
    return trim_stem_for_path(stem=slug, suffix=suffix, parent=parent)


def trim_stem_for_path(*, stem: str, suffix: str, parent: Path) -> str:
    max_total = 220
    budget = max_total - len(str(parent.resolve())) - len(suffix) - 1
    max_stem = max(48, min(120, budget))
    if len(stem) <= max_stem:
        return stem

    digest = hashlib.sha1(stem.encode("utf-8")).hexdigest()[:8]
    trimmed = stem[: max_stem - 9].rstrip("-_.")
    return f"{trimmed}-{digest}"


def is_preferred_current_name(path: Path) -> bool:
    if TEMP_RENAME_RE.fullmatch(path.stem):
        return False
    if is_low_information_stem(path.stem):
        return False
    if path.suffix != path.suffix.lower():
        return False
    if normalize_ascii(path.name) != path.name:
        return False
    if re.search(r"\s", path.name):
        return False
    if GENERIC_DOC_STEM_RE.fullmatch(path.stem):
        return False
    return bool(re.fullmatch(r"[a-z0-9][a-z0-9._-]*", path.stem))


def extension_priority(path: Path) -> tuple[int, str]:
    ext = path.suffix.lower()
    if ext == ".pdf":
        return (0, path.name.casefold())
    if ext in {".html", ".htm"}:
        return (1, path.name.casefold())
    if ext in IMAGE_EXTENSIONS:
        return (2, path.name.casefold())
    return (3, path.name.casefold())


def choose_family_hint(stem: str, models: list[str]) -> str:
    if models:
        return models[0]
    if is_low_information_stem(stem) or has_contextual_hash_suffix(stem):
        return "A revisar"

    cleaned = stem
    for marker in (
        "service-manual",
        "parts-manual",
        "operator-manual",
        "operation-manual",
        "installation-manual",
        "technical-specifications",
        "technical-reference",
        "quick-start-guide",
        "troubleshooting-guide",
    ):
        cleaned = cleaned.replace(marker, "")
    cleaned = cleaned.replace("__", " ")
    cleaned = re.sub(r"[-_]{2,}", " ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" -_")
    return cleaned or "A revisar"


def sanitize_staging_detected_models(
    models: list[str],
    *,
    category_key: str,
    stem: str,
) -> list[str]:
    if not models:
        return []

    low_signal_bucket = category_key in LOW_SIGNAL_MODEL_BUCKETS
    stem_compact_tokens = {
        re.sub(r"[^A-Z0-9]", "", part.upper())
        for part in re.split(r"[^A-Za-z0-9]+", normalize_ascii(stem))
        if part
    }
    results: list[str] = []
    seen: set[str] = set()

    for token in models:
        cleaned = token.strip()
        if not cleaned:
            continue

        upper = cleaned.upper()
        compact = re.sub(r"[^A-Z0-9]", "", upper)
        if not compact:
            continue
        if upper in STAGING_MODEL_STOPWORDS:
            continue
        if cleaned.isalpha():
            if len(upper) > 8:
                continue
            if low_signal_bucket and len(upper) > 6:
                continue
            if compact not in stem_compact_tokens and len(upper) > 6:
                continue
        if compact in {"NA", "NAO"}:
            continue

        key = cleaned.casefold()
        if key in seen:
            continue
        seen.add(key)
        results.append(cleaned)

    return results


def detect_curation_priority(category_key: str) -> str:
    if category_key in {
        "01_Geradores",
        "02_Climatizacao",
        "03_Baterias_e_DC",
        "04_Shore_Power_e_AC",
        "05_Navegacao_e_Eletronicos",
        "06_Bombas_Hidraulica_e_Utilidades",
        "08_Corrosao_Bonding_e_Seguranca",
        "09_Propulsao_Motores_Estabilizacao_e_Atuacao",
        "90_Triagem_Tecnica_por_Codigo",
    }:
        return "alta"
    if category_key in {"00_Documentacao_de_Campo_e_Clientes", "10_Materiais_Internos_e_Cursos"}:
        return "media"
    return "baixa"


def build_curation_block(record: ArchiveFileRecord) -> str:
    model_items = record.detected_models or [record.family_hint]
    model_bullets = "\n".join(f"- `{item}`" for item in model_items)
    return "\n".join(
        [
            "<!-- CURADORIA-HUMANA:START -->",
            "## Curadoria humana",
            "",
            "### Resumo humano",
            "- pendente",
            "",
            "### Aplicacao tecnica / oficina",
            "- pendente",
            "",
            "### Modelos ou codigos prioritarios",
            model_bullets,
            "",
            "### Pontos de atencao",
            "- confirmar cobertura real do arquivo antes de promover ao acervo principal",
            "- revisar se o nome padronizado descreve bem o documento ou se precisa ajuste humano",
            "",
            "### Integracoes e trilha editorial",
            f"- bucket de origem: `{record.category_label}`",
            f"- sistema-base: `{record.system}`",
            "- promocao ao acervo principal: pendente",
            "",
            "### Status de curadoria",
            f"- tipo documental detectado: `{record.document_kind}`",
            f"- prioridade editorial: `{record.curation_priority}`",
            "- curadoria humana: pendente",
            "- pronto para ensino/SEO: nao",
            "<!-- CURADORIA-HUMANA:END -->",
        ]
    )


def parse_existing_note(path: Path) -> ExistingNoteState:
    if not path.exists():
        return ExistingNoteState()

    text = path.read_text(encoding="utf-8", errors="ignore")
    match = FRONTMATTER_RE.match(text)
    frontmatter = match.group(1) if match else ""
    fields = {key: value for key, value in FRONTMATTER_FIELD_RE.findall(frontmatter)}
    block_match = CURATION_BLOCK_RE.search(text)
    return ExistingNoteState(
        curation_block=block_match.group(0) if block_match else None,
        curation_priority=fields.get("curation_priority"),
        curation_stage=fields.get("curation_stage"),
        status=fields.get("status"),
        title=fields.get("title"),
        document_kind=fields.get("document_kind"),
        acervo_brand=fields.get("acervo_brand"),
        acervo_family=fields.get("acervo_family"),
    )


def infer_note_status(*, curation_stage: str, existing_status: str | None) -> str:
    if curation_stage != "triagem-automatica":
        return existing_status or "staging-human-curated"
    return "staging-auto-extracted"


def should_preserve_manual_metadata(existing_state: ExistingNoteState) -> bool:
    return (
        existing_state.status == "staging-human-curated"
        or (
            existing_state.curation_stage is not None
            and existing_state.curation_stage != "triagem-automatica"
        )
    )


def build_duplicate_governance_block(record: ArchiveFileRecord) -> list[str]:
    manifesto_link = f"[{DUPLICATE_NOTE_PATH.name}](</{absolute_link(DUPLICATE_NOTE_PATH)}>)"
    queue_link = f"[{QUEUE_NOTE_PATH.name}](</{absolute_link(QUEUE_NOTE_PATH)}>)"

    lines = [
        "## Governanca de duplicatas",
        "",
        f"- status no lote: `{record.duplicate_status}`",
    ]

    if record.duplicate_status == "unique":
        lines.extend(
            [
                "- este arquivo ficou fisicamente unico no staging desta rodada",
                f"- manifesto geral: {manifesto_link}",
                f"- fila de resolucao: {queue_link}",
                "",
            ]
        )
        return lines

    canonical_source_path = STAGING_ROOT / Path(record.duplicate_canonical_relative)
    canonical_note_path = NOTES_ROOT / Path(record.duplicate_canonical_note_relative)
    lines.extend(
        [
            f"- hash do grupo: `{record.duplicate_group_sha256}`",
            f"- total de arquivos no grupo: `{record.duplicate_group_size}`",
            f"- arquivo canonico sugerido: [{record.duplicate_canonical_relative}](</{absolute_link(canonical_source_path)}>)",
            f"- nota companheira canonica: [{record.duplicate_canonical_note_relative}](</{absolute_link(canonical_note_path)}>)",
        ]
    )

    if record.duplicate_status == "canonical-suggested":
        lines.append("- este item foi escolhido automaticamente como melhor candidato a canonico dentro do grupo")
    else:
        lines.append("- este item e excedente fisico do grupo e deve ser comparado com o canonico antes de qualquer promocao")

    lines.extend(
        [
            f"- manifesto geral: {manifesto_link}",
            f"- fila de resolucao: {queue_link}",
            "",
        ]
    )
    return lines


def render_note(record: ArchiveFileRecord, reviewed_on: str) -> str:
    snippet_lines = record.snippets or [
        "nenhum trecho textual confiavel foi extraido automaticamente"
    ]
    curation_block = record.curation_block or build_curation_block(record)
    duplicate_block = build_duplicate_governance_block(record)

    body: list[str] = [
        "---",
        f'title: "{record.title}"',
        'note_type: "acervo-companion"',
        'domain: "90_Revisao_Manual"',
        f'status: "{record.note_status}"',
        'acervo_origin: "humano-staging"',
        f'document_kind: "{record.document_kind}"',
        f'curation_priority: "{record.curation_priority}"',
        f'curation_stage: "{record.curation_stage}"',
        f'reviewed_on: "{reviewed_on}"',
        'review_jurisdiction: "Brasil"',
        f'source_file: "{record.renamed_relative}"',
        f'source_sha256: "{record.source_sha256}"',
        f'acervo_bucket: "{record.category_label}"',
        f'acervo_system: "{record.system}"',
        f'acervo_brand: "{record.brand_label}"',
        f'acervo_family: "{record.family_hint}"',
        f'extraction_method: "{record.extraction_method}"',
        f'text_extractable: "{record.text_extractable}"',
        f"extracted_text_chars: {record.extracted_text_chars}",
        f'indexed_text_path: "{record.indexed_text_path}"',
        f'duplicate_status: "{record.duplicate_status}"',
        f'duplicate_group_sha256: "{record.duplicate_group_sha256}"',
        f"duplicate_group_size: {record.duplicate_group_size}",
        f'duplicate_canonical_source: "{record.duplicate_canonical_relative}"',
        f'duplicate_canonical_note: "{record.duplicate_canonical_note_relative}"',
        "aliases:",
        f'  - "{record.original_name}"',
        f'  - "{record.renamed_name}"',
        "related_notes:",
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Indice Gerado"',
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Manifesto de Duplicatas"',
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Fila de Resolucao de Duplicatas"',
        "---",
        "",
        f"# {record.title}",
        "",
        "> [!abstract] Resumo tecnico",
        "> Nota companheira automatica do staging tecnico humano.",
        "> Ela preserva trilha editorial, busca textual e prepara a futura promocao ao acervo principal.",
        "",
    ]

    if record.text_extractable == "nao":
        body.extend(
            [
                "> [!warning] Extracao textual limitada",
                "> Este item ficou com leitura fraca ou sem texto util. O arquivo original segue como fonte primaria.",
                "",
            ]
        )

    body.extend(
        [
            "## Fonte",
            "",
            f"- arquivo: [{record.renamed_name}](</{absolute_link(record.source_path)}>)",
            f"- nome original: `{record.original_name}`",
            f"- caminho original: `{record.original_relative}`",
            f"- caminho atual: `{record.renamed_relative}`",
            f"- nota companheira: `90_Revisao_Manual/_Acervo_Notas/Acervo do humano/10_Tecnico_Nautico/{record.note_relative}`",
            f"- extensao: `{record.extension}`",
            f"- tamanho do arquivo: `{record.size_label}`",
            f"- texto extraivel detectado: `{record.text_extractable}`",
            f"- metodo de extracao: `{record.extraction_method}`",
            f"- caracteres extraidos: `{record.extracted_text_chars}`",
            f"- texto integral auxiliar: `{record.indexed_text_path or 'n/a'}`",
            "",
            "## Sinais principais",
            "",
            f"- bucket tecnico: `{record.category_label}`",
            f"- sistema-base: `{record.system}`",
            f"- tipo documental detectado: `{record.document_kind}`",
            f"- marcas detectadas: `{join_or_na(record.detected_brands)}`",
            f"- codigos/modelos detectados: `{join_or_na(record.detected_models)}`",
            f"- termos uteis detectados: `{join_or_na(record.detected_terms)}`",
            "",
            "## Uso sugerido",
            "",
            "- usar esta nota para localizar o arquivo sem depender do nome bruto original",
            "- confirmar se o item deve ficar no staging, ser promovido ao acervo principal ou ir para trilha complementar",
            "- revisar manualmente os modelos/codigos antes de transformar o conteudo em resumo definitivo",
            "",
        ]
    )
    body.extend(duplicate_block)
    body.extend(
        [
            curation_block,
            "",
            "## Trechos indexaveis",
            "",
        ]
    )

    sanitized_snippets = [line.replace("`", "'") for line in snippet_lines]
    body.extend(f"- `{line}`" for line in sanitized_snippets)

    if record.indexed_text:
        safe_text = record.indexed_text.replace("```", "'''")
        body.extend(
            [
                "",
                "## Texto extraido para busca",
                "",
                "> [!info] Camada de indexacao",
                "> Este bloco existe para busca local e triagem. Nao usar como resumo tecnico definitivo sem revisar a fonte original.",
                "",
                "```text",
                safe_text,
                "```",
            ]
        )

    body.extend(
        [
            "",
            "## Observacoes",
            "",
            "- esta nota foi gerada automaticamente a partir do arquivo fisico e ainda pede auditoria humana",
            "- o nome padronizado privilegia rastreabilidade e busca; ajustes finos de semantica podem ser feitos caso a caso",
            "",
        ]
    )
    return "\n".join(body)


def render_index(
    records: list[ArchiveFileRecord],
    reviewed_on: str,
    duplicate_groups: list[DuplicateGroup],
) -> str:
    by_category = Counter(record.category_label for record in records)
    by_extension = Counter(record.extension for record in records)
    by_priority = Counter(record.curation_priority for record in records)
    duplicate_status_counter = Counter(record.duplicate_status for record in records)
    grouped: dict[str, list[ArchiveFileRecord]] = defaultdict(list)
    for record in records:
        grouped[record.category_key].append(record)

    lines: list[str] = [
        "---",
        'title: "Acervo Humano Tecnico - Indice Gerado"',
        'note_type: "index"',
        'domain: "90_Revisao_Manual"',
        'status: "auto-generated"',
        f'reviewed_on: "{reviewed_on}"',
        'review_jurisdiction: "Brasil"',
        "---",
        "",
        "# Acervo Humano Tecnico - Indice Gerado",
        "",
        "> [!abstract] Resumo tecnico",
        "> Painel automatico da camada companheira do staging tecnico humano.",
        "",
        "## Panorama geral",
        "",
        f"- itens processados: `{len(records)}`",
        f"- buckets tecnicos: `{len(by_category)}`",
        f"- atualizacao: `{reviewed_on}`",
        f"- manifesto de duplicatas: [{DUPLICATE_NOTE_PATH.name}](</{absolute_link(DUPLICATE_NOTE_PATH)}>)",
        f"- fila de resolucao: [{QUEUE_NOTE_PATH.name}](</{absolute_link(QUEUE_NOTE_PATH)}>)",
        "",
        "## Distribuicao por bucket",
        "",
    ]

    for category_key in CATEGORY_LABELS:
        label = CATEGORY_LABELS[category_key]
        if label in by_category:
            lines.append(f"- `{label}`: `{by_category[label]}`")

    lines.extend(["", "## Distribuicao por extensao", ""])
    for extension, count in sorted(by_extension.items()):
        lines.append(f"- `{extension}`: `{count}`")

    lines.extend(["", "## Distribuicao por prioridade editorial", ""])
    for priority in ("alta", "media", "baixa"):
        if priority in by_priority:
            lines.append(f"- `{priority}`: `{by_priority[priority]}`")

    lines.extend(["", "## Governanca de duplicatas", ""])
    lines.append(f"- grupos de duplicatas: `{len(duplicate_groups)}`")
    lines.append(
        f"- arquivos canonicos sugeridos: `{duplicate_status_counter.get('canonical-suggested', 0)}`"
    )
    lines.append(f"- arquivos excedentes: `{duplicate_status_counter.get('duplicate', 0)}`")
    lines.append(f"- arquivos unicos: `{duplicate_status_counter.get('unique', 0)}`")

    for category_key in CATEGORY_LABELS:
        if category_key not in grouped:
            continue
        lines.extend(["", f"## {CATEGORY_LABELS[category_key]}", ""])
        for record in sorted(grouped[category_key], key=lambda item: item.renamed_name.casefold()):
            lines.append(f"- [{record.renamed_name}](</{absolute_link(record.note_path)}>)")

    lines.append("")
    return "\n".join(lines)


def non_pdf_records(records: list[ArchiveFileRecord]) -> list[ArchiveFileRecord]:
    return [record for record in records if record.extension in NON_PDF_INDEXED_EXTENSIONS]


def render_non_pdf_index(records: list[ArchiveFileRecord], reviewed_on: str) -> str:
    items = non_pdf_records(records)
    by_extension = Counter(record.extension for record in items)
    by_category = Counter(record.category_label for record in items)
    by_method = Counter(record.extraction_method for record in items)
    searchable = sum(1 for record in items if record.indexed_text)

    lines: list[str] = [
        "---",
        'title: "Acervo Humano Tecnico - Nao PDF - Indice Gerado"',
        'note_type: "index"',
        'domain: "90_Revisao_Manual"',
        'status: "auto-generated"',
        f'reviewed_on: "{reviewed_on}"',
        'review_jurisdiction: "Brasil"',
        "related_notes:",
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Indice Gerado"',
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Local - Indice Gerado"',
        "---",
        "",
        "# Acervo Humano Tecnico - Nao PDF - Indice Gerado",
        "",
        "> [!abstract] Resumo tecnico",
        "> Painel dedicado aos arquivos tecnicos do staging humano que ainda nao sao PDFs.",
        "> Eles nao entram no acervo principal PDF-first, mas ficam pesquisaveis por notas, sidecars e trilha editorial.",
        "",
        "## Panorama geral",
        "",
        f"- arquivos nao-PDF: `{len(items)}`",
        f"- arquivos com texto indexavel em Markdown: `{searchable}`",
        f"- atualizacao: `{reviewed_on}`",
        f"- relatorio operacional: [{NON_PDF_REPORT_PATH.name}](</{absolute_link(NON_PDF_REPORT_PATH)}>)",
        "",
        "## Distribuicao por extensao",
        "",
    ]

    for extension, count in sorted(by_extension.items()):
        lines.append(f"- `{extension}`: `{count}`")

    lines.extend(["", "## Distribuicao por bucket", ""])
    for category_key in CATEGORY_LABELS:
        label = CATEGORY_LABELS[category_key]
        if label in by_category:
            lines.append(f"- `{label}`: `{by_category[label]}`")

    lines.extend(["", "## Metodos de extracao", ""])
    for method, count in sorted(by_method.items()):
        lines.append(f"- `{method}`: `{count}`")

    grouped: dict[str, list[ArchiveFileRecord]] = defaultdict(list)
    for record in items:
        grouped[record.category_key].append(record)

    for category_key in CATEGORY_LABELS:
        if category_key not in grouped:
            continue
        lines.extend(["", f"## {CATEGORY_LABELS[category_key]}", ""])
        for record in sorted(grouped[category_key], key=lambda item: item.renamed_name.casefold()):
            search_flag = "texto" if record.indexed_text else "sem-texto"
            lines.append(
                f"- [{record.renamed_name}](</{absolute_link(record.note_path)}>) - "
                f"`{record.extension}` - `{record.extraction_method}` - `{search_flag}`"
            )

    lines.append("")
    return "\n".join(lines)


def render_non_pdf_report(records: list[ArchiveFileRecord], reviewed_on: str) -> str:
    items = non_pdf_records(records)
    by_extension = Counter(record.extension for record in items)
    by_extractable = Counter(record.text_extractable for record in items)
    indexed_count = sum(1 for record in items if record.indexed_text)
    ocr_count = sum(1 for record in items if record.extraction_method.startswith("tesseract"))

    lines = [
        "---",
        'title: "Normalizacao Nao PDF - Acervo Humano Tecnico"',
        'note_type: "audit"',
        'domain: "90_Revisao_Manual"',
        'status: "active-curation"',
        f'reviewed_on: "{reviewed_on}"',
        'review_jurisdiction: "Brasil"',
        "related_notes:",
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Nao PDF - Indice Gerado"',
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Indice Gerado"',
        "---",
        "",
        "# Normalizacao Nao PDF - Acervo Humano Tecnico",
        "",
        "> [!abstract] Resumo tecnico",
        "> Esta auditoria registra a normalizacao dos arquivos tecnicos do staging humano que ainda nao sao PDFs.",
        "> O objetivo e busca e triagem: preservar os originais, extrair texto e deixar uma fila clara para conversao ou curadoria.",
        "",
        "## Resultado",
        "",
        f"- arquivos nao-PDF processados: `{len(items)}`",
        f"- arquivos com texto extraivel: `{by_extractable.get('sim', 0)}`",
        f"- arquivos sem texto util: `{by_extractable.get('nao', 0)}`",
        f"- notas com bloco integral de busca: `{indexed_count}`",
        f"- imagens com OCR via Tesseract: `{ocr_count}`",
        "",
        "## Distribuicao por extensao",
        "",
    ]

    for extension, count in sorted(by_extension.items()):
        lines.append(f"- `{extension}`: `{count}`")

    lines.extend(
        [
            "",
            "## Decisao operacional",
            "",
            "- HTML tecnico passa a ter texto extraido dentro da propria nota companheira e sidecar `.txt` em `_Dados_Acervo/non_pdf_texts`.",
            "- Imagens tentam OCR via Tesseract quando a ferramenta esta disponivel; quando o OCR nao gera texto util, ficam como evidencias visuais a revisar.",
            "- Estes arquivos continuam fora do acervo principal PDF-first ate haver conversao limpa para PDF, nota tecnica autoral ou descarte fundamentado.",
            "",
            "## Proxima fila sugerida",
            "",
            "- converter HTML de maior valor em notas tecnicas autorais ou PDFs arquivaveis",
            "- revisar imagens de campo para remover conteudo pessoal/sensivel antes de qualquer reaproveitamento",
            "- priorizar HTML de `03_Baterias_e_DC`, `04_Shore_Power_e_AC` e `06_Bombas_Hidraulica_e_Utilidades` para material didatico",
            "",
        ]
    )
    return "\n".join(lines)


def duplicate_quality_rank(record: ArchiveFileRecord) -> tuple[object, ...]:
    relative = record.source_path.relative_to(STAGING_ROOT)
    parts = set(relative.parts)
    stem_tokens = {
        token
        for token in re.split(r"[^A-Za-z0-9]+", record.source_path.stem.casefold())
        if token
    }
    return (
        1 if "98_Duplicatas" in parts else 0,
        1 if TEMP_RENAME_RE.fullmatch(record.source_path.stem) else 0,
        1 if DUP_SUFFIX_RE.search(record.source_path.stem) else 0,
        1 if is_low_information_stem(record.source_path.stem) else 0,
        1 if HASH_SUFFIX_RE.search(record.source_path.stem) else 0,
        0 if "__" in record.source_path.stem else 1,
        0 if DOCUMENT_MARKER_RE.search(record.source_path.stem) else 1,
        1 if stem_tokens & GENERIC_FILENAME_HINTS else 0,
        1 if GENERIC_DOC_STEM_RE.fullmatch(record.source_path.stem) else 0,
        1 if record.extension != ".pdf" else 0,
        len(relative.parts),
        -len(stem_tokens),
        record.renamed_relative.casefold(),
    )


def build_duplicate_groups(records: list[ArchiveFileRecord]) -> list[DuplicateGroup]:
    grouped: defaultdict[str, list[ArchiveFileRecord]] = defaultdict(list)
    for record in records:
        grouped[record.source_sha256].append(record)

    groups: list[DuplicateGroup] = []
    for digest, members in grouped.items():
        if len(members) <= 1:
            continue
        ordered_members = tuple(
            sorted(members, key=lambda item: item.renamed_relative.casefold())
        )
        canonical = min(ordered_members, key=duplicate_quality_rank)
        groups.append(
            DuplicateGroup(
                sha256=digest,
                canonical=canonical,
                members=ordered_members,
            )
        )

    return sorted(groups, key=lambda item: duplicate_quality_rank(item.canonical))


def annotate_duplicate_metadata(
    records: list[ArchiveFileRecord],
    groups: list[DuplicateGroup],
) -> None:
    for record in records:
        record.duplicate_status = "unique"
        record.duplicate_group_sha256 = ""
        record.duplicate_group_size = 1
        record.duplicate_canonical_relative = ""
        record.duplicate_canonical_note_relative = ""

    for group in groups:
        for member in group.members:
            member.duplicate_status = "duplicate"
            member.duplicate_group_sha256 = group.sha256
            member.duplicate_group_size = len(group.members)
            member.duplicate_canonical_relative = group.canonical.renamed_relative
            member.duplicate_canonical_note_relative = group.canonical.note_relative
        group.canonical.duplicate_status = "canonical-suggested"


def duplicate_resolution_priority(group: DuplicateGroup) -> str:
    category_keys = {member.category_key for member in group.members}
    if len(group.members) >= 4 or "01_Geradores" in category_keys or len(category_keys) > 1:
        return "alta"
    if len(group.members) >= 3:
        return "media"
    if group.canonical.category_key in {
        "02_Climatizacao",
        "03_Baterias_e_DC",
        "04_Shore_Power_e_AC",
        "05_Navegacao_e_Eletronicos",
    }:
        return "media"
    return "baixa"


def duplicate_resolution_sort_key(group: DuplicateGroup) -> tuple[object, ...]:
    category_keys = {member.category_key for member in group.members}
    return (
        RESOLUTION_PRIORITY_ORDER[duplicate_resolution_priority(group)],
        0 if len(category_keys) > 1 else 1,
        DUPLICATE_PRIORITY_BUCKET_ORDER.get(group.canonical.category_key, 99),
        -len(group.members),
        duplicate_quality_rank(group.canonical),
    )


def duplicate_resolution_action(group: DuplicateGroup) -> str:
    category_keys = {member.category_key for member in group.members}
    extensions = {member.extension for member in group.members}
    if len(category_keys) > 1:
        return (
            "definir primeiro o bucket canonico do conjunto e manter apenas uma fonte promovivel"
        )
    if any("98_Duplicatas" in member.renamed_relative for member in group.members):
        return "consolidar fora de `98_Duplicatas` e arquivar os excedentes apos conferencia"
    if len(extensions) > 1:
        return (
            "comparar se extensoes diferentes agregam busca real; se nao agregarem, manter so o canonico"
        )
    if len(group.members) >= 3:
        return "manter o canonico sugerido e eliminar ou arquivar os excedentes apos validacao rapida"
    return "comparar metadados e manter apenas o arquivo canonico sugerido"


def render_duplicate_index(groups: list[DuplicateGroup], reviewed_on: str) -> str:
    by_bucket = Counter(group.canonical.category_label for group in groups)
    impacted_files = sum(len(group.members) for group in groups)

    lines: list[str] = [
        "---",
        'title: "Acervo Humano Tecnico - Manifesto de Duplicatas"',
        'note_type: "index"',
        'domain: "90_Revisao_Manual"',
        'status: "auto-generated"',
        f'reviewed_on: "{reviewed_on}"',
        'review_jurisdiction: "Brasil"',
        "---",
        "",
        "# Acervo Humano Tecnico - Manifesto de Duplicatas",
        "",
        "> [!abstract] Resumo tecnico",
        "> Painel automatico dos grupos de arquivos fisicamente duplicados no staging tecnico humano.",
        "",
        "## Panorama geral",
        "",
        f"- grupos de duplicatas: `{len(groups)}`",
        f"- arquivos envolvidos: `{impacted_files}`",
        f"- excedente sobre o canonico: `{max(0, impacted_files - len(groups))}`",
        f"- atualizacao: `{reviewed_on}`",
        f"- fila de resolucao: [{QUEUE_NOTE_PATH.name}](</{absolute_link(QUEUE_NOTE_PATH)}>)",
        "",
        "## Distribuicao por bucket canonico",
        "",
    ]

    for bucket, count in by_bucket.most_common():
        lines.append(f"- `{bucket}`: `{count}`")

    for index, group in enumerate(groups, start=1):
        lines.extend(
            [
                "",
                f"## Grupo {index:02d}",
                "",
                f"- prioridade de resolucao: `{duplicate_resolution_priority(group)}`",
                f"- hash: `{group.sha256}`",
                f"- bucket canonico sugerido: `{group.canonical.category_label}`",
                f"- arquivo canonico sugerido: [{group.canonical.renamed_relative}](</{absolute_link(group.canonical.source_path)}>)",
                f"- nota companheira canonica: [{group.canonical.note_relative}](</{absolute_link(group.canonical.note_path)}>)",
                f"- total de arquivos no grupo: `{len(group.members)}`",
                f"- acao recomendada: {duplicate_resolution_action(group)}",
                "",
                "### Membros do grupo",
                "",
            ]
        )
        for member in group.members:
            marker = "canonico sugerido" if member == group.canonical else "duplicata"
            lines.append(f"- `{marker}`: `{member.renamed_relative}`")

    lines.append("")
    return "\n".join(lines)


def render_duplicate_json(groups: list[DuplicateGroup], reviewed_on: str) -> dict[str, object]:
    return {
        "reviewed_on": reviewed_on,
        "group_count": len(groups),
        "file_count": sum(len(group.members) for group in groups),
        "groups": [
            {
                "sha256": group.sha256,
                "canonical_relative": group.canonical.renamed_relative,
                "canonical_note_relative": group.canonical.note_relative,
                "bucket": group.canonical.category_label,
                "priority": duplicate_resolution_priority(group),
                "recommended_action": duplicate_resolution_action(group),
                "bucket_count": len({member.category_key for member in group.members}),
                "members": [member.renamed_relative for member in group.members],
            }
            for group in groups
        ],
    }


def render_duplicate_resolution_queue(
    groups: list[DuplicateGroup],
    reviewed_on: str,
) -> str:
    ordered_groups = sorted(groups, key=duplicate_resolution_sort_key)
    by_priority = Counter(duplicate_resolution_priority(group) for group in groups)

    lines: list[str] = [
        "---",
        'title: "Acervo Humano Tecnico - Fila de Resolucao de Duplicatas"',
        'note_type: "index"',
        'domain: "90_Revisao_Manual"',
        'status: "auto-generated"',
        f'reviewed_on: "{reviewed_on}"',
        'review_jurisdiction: "Brasil"',
        "---",
        "",
        "# Acervo Humano Tecnico - Fila de Resolucao de Duplicatas",
        "",
        "> [!abstract] Resumo tecnico",
        "> Fila priorizada para limpeza fisica e consolidacao editorial das duplicatas do staging tecnico humano.",
        "",
        "## Panorama geral",
        "",
        f"- grupos na fila: `{len(groups)}`",
        f"- prioridade alta: `{by_priority.get('alta', 0)}`",
        f"- prioridade media: `{by_priority.get('media', 0)}`",
        f"- prioridade baixa: `{by_priority.get('baixa', 0)}`",
        f"- manifesto de apoio: [{DUPLICATE_NOTE_PATH.name}](</{absolute_link(DUPLICATE_NOTE_PATH)}>)",
        f"- atualizacao: `{reviewed_on}`",
        "",
    ]

    for index, group in enumerate(ordered_groups, start=1):
        category_labels = sorted({member.category_label for member in group.members})
        buckets_label = ", ".join(f"`{label}`" for label in category_labels)
        lines.extend(
            [
                f"## Prioridade {duplicate_resolution_priority(group)} - Grupo {index:02d}",
                "",
                f"- hash: `{group.sha256}`",
                f"- bucket canonico sugerido: `{group.canonical.category_label}`",
                f"- buckets envolvidos: {buckets_label}",
                f"- total de arquivos no grupo: `{len(group.members)}`",
                f"- arquivo canonico sugerido: [{group.canonical.renamed_relative}](</{absolute_link(group.canonical.source_path)}>)",
                f"- nota companheira canonica: [{group.canonical.note_relative}](</{absolute_link(group.canonical.note_path)}>)",
                f"- acao recomendada: {duplicate_resolution_action(group)}",
                "",
                "### Excedentes a decidir",
                "",
            ]
        )
        for member in group.members:
            if member == group.canonical:
                continue
            lines.append(
                f"- [{member.renamed_relative}](</{absolute_link(member.source_path)}>) - bucket `{member.category_label}` - extensao `{member.extension}`"
            )
        if len(group.members) == 1:
            lines.append("- nenhum excedente")
        lines.append("")

    return "\n".join(lines)


def unique_targets(
    files: list[Path],
    extracted_cache: dict[Path, ExtractionBundle],
) -> dict[Path, Path]:
    targets: dict[Path, Path] = {}
    per_directory: defaultdict[Path, Counter[str]] = defaultdict(Counter)

    for path in files:
        desired_name = determine_target_name(path, extracted_cache[path].text)
        counter = per_directory[path.parent]
        candidate_name = desired_name
        stem = Path(desired_name).stem
        suffix = Path(desired_name).suffix.lower()
        while candidate_name.casefold() in counter:
            counter[desired_name.casefold()] += 1
            candidate_name = f"{stem}-dup-{counter[desired_name.casefold()]}{suffix}"
        counter[candidate_name.casefold()] += 1
        targets[path] = path.with_name(candidate_name)

    return targets


def apply_renames(targets: dict[Path, Path]) -> int:
    rename_count = 0
    staged_moves: list[tuple[Path, Path, Path]] = []

    for index, (source, target) in enumerate(sorted(targets.items(), key=lambda item: str(item[0]))):
        if source == target:
            continue
        temp = source.with_name(f"__tmp2-renomear-{index:04d}{source.suffix.lower()}")
        serial = 2
        while path_exists(temp):
            temp = source.with_name(
                f"__tmp2-renomear-{index:04d}-{serial}{source.suffix.lower()}"
            )
            serial += 1
        staged_moves.append((source, temp, target))

    for source, temp, _target in staged_moves:
        os.replace(io_path(source), io_path(temp))

    for _source, temp, target in staged_moves:
        os.replace(io_path(temp), io_path(target))
        rename_count += 1

    return rename_count


def cleanup_stale_notes(valid_notes: set[Path]) -> int:
    removed = 0
    if not NOTES_ROOT.exists():
        return removed

    for note_path in sorted(NOTES_ROOT.rglob("*.md")):
        if note_path in valid_notes:
            continue
        note_path.unlink()
        removed += 1

    for directory in sorted(NOTES_ROOT.rglob("*"), reverse=True):
        if directory.is_dir() and not any(directory.iterdir()):
            try:
                directory.rmdir()
            except OSError:
                continue

    return removed


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(io_path(path), "w", encoding="utf-8", newline="\n") as handle:
        handle.write(content)


def write_json_file(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(io_path(path), "w", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def write_text_sidecars(records: list[ArchiveFileRecord]) -> int:
    written = 0
    valid_sidecars: set[Path] = set()

    for record in records:
        if not record.indexed_text_path or not record.indexed_text:
            continue

        relative = Path(record.indexed_text_path).relative_to(
            Path("90_Revisao_Manual") / "_Dados_Acervo" / "non_pdf_texts"
        )
        target = NON_PDF_TEXT_ROOT / relative
        write_file(target, record.indexed_text)
        valid_sidecars.add(target)
        written += 1

    if NON_PDF_TEXT_ROOT.exists():
        for text_path in sorted(NON_PDF_TEXT_ROOT.rglob("*.txt")):
            if text_path in valid_sidecars:
                continue
            text_path.unlink()

    return written


def render_non_pdf_json(records: list[ArchiveFileRecord], reviewed_on: str) -> dict[str, object]:
    items = non_pdf_records(records)
    return {
        "reviewed_on": reviewed_on,
        "non_pdf_count": len(items),
        "extension_counts": dict(Counter(record.extension for record in items)),
        "extractable_counts": dict(Counter(record.text_extractable for record in items)),
        "records": [
            {
                "source_file": record.renamed_relative,
                "note": record.note_relative,
                "extension": record.extension,
                "category": record.category_label,
                "system": record.system,
                "document_kind": record.document_kind,
                "curation_priority": record.curation_priority,
                "extraction_method": record.extraction_method,
                "text_extractable": record.text_extractable,
                "extracted_text_chars": record.extracted_text_chars,
                "indexed_text_path": record.indexed_text_path,
                "sha256": record.source_sha256,
            }
            for record in items
        ],
    }


def build_note_relative_lookup(files: list[Path]) -> dict[Path, Path]:
    base_counts = Counter(
        path.relative_to(STAGING_ROOT).with_suffix(".md").as_posix().casefold()
        for path in files
    )
    lookup: dict[Path, Path] = {}
    for path in files:
        relative = path.relative_to(STAGING_ROOT)
        base_note = relative.with_suffix(".md")
        if base_counts[base_note.as_posix().casefold()] > 1:
            extension_label = path.suffix.lower().lstrip(".") or "file"
            base_note = relative.with_name(f"{relative.stem}__{extension_label}.md")
        lookup[path] = base_note
    return lookup


def detect_family_context(relative: Path, category_key: str, category_label: str) -> str:
    if is_low_information_stem(relative.stem) or has_contextual_hash_suffix(relative.stem):
        return "A revisar"
    if len(relative.parts) <= 1:
        return clean_source_stem(relative.stem)

    parent_name = relative.parent.name
    if parent_name == category_key or CATEGORY_LABELS.get(parent_name) == category_label:
        return clean_source_stem(relative.stem)

    if parent_name == category_label:
        return clean_source_stem(relative.stem)

    return parent_name


def build_records(
    files: list[Path],
    *,
    original_lookup: dict[Path, tuple[str, str]],
    extracted_lookup: dict[Path, ExtractionBundle],
) -> list[ArchiveFileRecord]:
    records: list[ArchiveFileRecord] = []
    reviewed_on = date.today().isoformat()
    note_lookup = build_note_relative_lookup(files)

    for path in sorted(files, key=lambda item: item.relative_to(STAGING_ROOT).as_posix().casefold()):
        relative = path.relative_to(STAGING_ROOT)
        category_key = relative.parts[0] if relative.parts else "Sem-Categoria"
        category_label = CATEGORY_LABELS.get(category_key, category_key)
        system = CATEGORY_SYSTEMS.get(category_key, category_key)
        family_context = detect_family_context(relative, category_key, category_label)
        note_relative_path = note_lookup[path]
        note_relative = note_relative_path.as_posix()
        note_path = NOTES_ROOT / note_relative_path

        original_relative, original_name = original_lookup[path]
        existing_state = parse_existing_note(note_path)
        extracted_bundle = extracted_lookup[path]
        extracted_text = extracted_bundle.text
        extraction_method = extracted_bundle.method
        useful_text = extracted_bundle.useful
        indexed_text = build_indexed_text(path, extracted_text, useful_text)
        sidecar_relative = text_sidecar_relative(note_relative_path, path.suffix.lower())
        analysis_text = extracted_text if useful_text else ""
        normalized_stem = path.stem
        detected_models = detect_model_signals(
            stem=normalized_stem,
            family=family_context,
            text=analysis_text,
        )
        detected_models = sanitize_staging_detected_models(
            detected_models,
            category_key=category_key,
            stem=normalized_stem,
        )
        seed_text = "\n".join(
            filter(
                None,
                [
                    category_label,
                    normalized_stem,
                    analysis_text,
                    first_meaningful_line(extracted_text),
                ],
            )
        )
        detected_brands = detect_brand_signals(seed_text)
        detected_terms = detect_term_signals(seed_text)
        family_hint = choose_family_hint(normalized_stem, detected_models)
        curation_priority = (
            existing_state.curation_priority or detect_curation_priority(category_key)
        )
        curation_stage = existing_state.curation_stage or "triagem-automatica"
        note_status = infer_note_status(
            curation_stage=curation_stage,
            existing_status=existing_state.status,
        )
        preserve_manual_metadata = should_preserve_manual_metadata(existing_state)
        title = existing_state.title or title_from_slug(path.stem)
        document_kind = detect_document_kind(path.stem)
        acervo_brand = join_or_na(detected_brands) if detected_brands else "A revisar"
        acervo_family = family_hint
        if preserve_manual_metadata:
            title = existing_state.title or title
            document_kind = existing_state.document_kind or document_kind
            acervo_brand = existing_state.acervo_brand or acervo_brand
            acervo_family = existing_state.acervo_family or acervo_family

        record = ArchiveFileRecord(
            source_path=path,
            original_relative=original_relative,
            renamed_relative=relative.as_posix(),
            note_relative=note_relative,
            note_path=note_path,
            title=title,
            category_key=category_key,
            category_label=category_label,
            system=system,
            extension=path.suffix.lower(),
            original_name=original_name,
            renamed_name=path.name,
            document_kind=document_kind,
            curation_priority=curation_priority,
            curation_stage=curation_stage,
            note_status=note_status,
            brand_label=acervo_brand,
            source_sha256=sha256(path),
            extraction_method=extraction_method,
            text_extractable="sim" if useful_text else "nao",
            size_label=human_size(file_size(path)),
            extracted_text_chars=len(extracted_text),
            indexed_text_path=sidecar_relative if indexed_text else "",
            indexed_text=indexed_text,
            detected_brands=detected_brands,
            detected_models=detected_models,
            detected_terms=detected_terms,
            snippets=build_snippets(analysis_text),
            family_hint=acervo_family,
            curation_block=existing_state.curation_block or "",
        )
        records.append(record)

    duplicate_groups = build_duplicate_groups(records)
    annotate_duplicate_metadata(records, duplicate_groups)

    index_content = render_index(records, reviewed_on, duplicate_groups)
    write_file(INDEX_NOTE_PATH, index_content)
    write_file(NON_PDF_INDEX_NOTE_PATH, render_non_pdf_index(records, reviewed_on))
    write_file(NON_PDF_REPORT_PATH, render_non_pdf_report(records, reviewed_on))
    write_json_file(NON_PDF_JSON_PATH, render_non_pdf_json(records, reviewed_on))
    write_text_sidecars(records)

    valid_notes: set[Path] = set()
    for record in records:
        content = render_note(record, reviewed_on)
        write_file(record.note_path, content)
        valid_notes.add(record.note_path)

    cleanup_stale_notes(valid_notes)
    write_file(DUPLICATE_NOTE_PATH, render_duplicate_index(duplicate_groups, reviewed_on))
    write_file(
        QUEUE_NOTE_PATH,
        render_duplicate_resolution_queue(duplicate_groups, reviewed_on),
    )
    write_json_file(DUPLICATE_JSON_PATH, render_duplicate_json(duplicate_groups, reviewed_on))
    return records


def collect_files() -> list[Path]:
    return [
        path
        for path in iter_files_long(STAGING_ROOT)
        if path.suffix.lower() not in {".md"}
    ]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Padroniza nomes do staging tecnico humano e gera notas companheiras."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Apenas mostra o resumo do lote sem renomear arquivos nem gerar notas.",
    )
    args = parser.parse_args()

    files = collect_files()
    extracted_cache = {
        path: ExtractionBundle(*extract_file_text(path))
        for path in files
    }
    targets = unique_targets(files, extracted_cache)

    rename_count = sum(1 for source, target in targets.items() if source != target)
    print(f"Itens encontrados: {len(files)}")
    print(f"Renomeacoes planejadas: {rename_count}")

    if args.dry_run:
        for source, target in sorted(targets.items(), key=lambda item: item[0].relative_to(STAGING_ROOT).as_posix().casefold())[:40]:
            if source == target:
                continue
            print(
                f"- {source.relative_to(STAGING_ROOT).as_posix()} -> {target.relative_to(STAGING_ROOT).as_posix()}"
            )
        return 0

    original_lookup = {
        target: (source.relative_to(STAGING_ROOT).as_posix(), source.name)
        for source, target in targets.items()
    }
    extracted_lookup = {target: extracted_cache[source] for source, target in targets.items()}

    applied = apply_renames(targets)
    processed_files = sorted(original_lookup)
    records = build_records(
        processed_files,
        original_lookup=original_lookup,
        extracted_lookup=extracted_lookup,
    )

    print(f"Renomeacoes aplicadas: {applied}")
    print(f"Notas geradas: {len(records)}")
    print(f"Painel atualizado: {INDEX_NOTE_PATH.relative_to(ROOT).as_posix()}")
    print(f"Painel nao-PDF: {NON_PDF_INDEX_NOTE_PATH.relative_to(ROOT).as_posix()}")
    print(f"Manifesto de duplicatas: {DUPLICATE_NOTE_PATH.relative_to(ROOT).as_posix()}")
    print(f"Fila de resolucao: {QUEUE_NOTE_PATH.relative_to(ROOT).as_posix()}")
    print(f"Manifesto JSON: {DUPLICATE_JSON_PATH.relative_to(ROOT).as_posix()}")
    print(f"Manifesto nao-PDF: {NON_PDF_JSON_PATH.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
