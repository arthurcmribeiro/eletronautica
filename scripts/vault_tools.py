from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
FRONTMATTER_RE = re.compile(r"(?s)^---\r?\n(.*?)\r?\n---\r?\n?(.*)$")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")
EXCLUDED_PARTS = {".git", ".obsidian", ".claude", "_visuals"}
EXCLUDED_RELATIVE_PREFIXES = {
    "90_Revisao_Manual/_Acervo_Local/Acervo do humano/",
}


def is_excluded_path(path: Path, root: Path = ROOT) -> bool:
    relative_path = path.relative_to(root).as_posix()
    return (
        any(part in EXCLUDED_PARTS for part in path.parts)
        or any(relative_path.startswith(prefix) for prefix in EXCLUDED_RELATIVE_PREFIXES)
    )


def note_files(root: Path = ROOT) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if not is_excluded_path(path, root)
        and path.parent != root
    )


def extract_frontmatter(text: str) -> tuple[str, str]:
    text = text.lstrip("\ufeff")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return "", text
    return match.group(1), match.group(2)


def _clean_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1]
    return value


def parse_frontmatter(frontmatter: str) -> dict[str, Any]:
    if not frontmatter:
        return {}

    data: dict[str, Any] = {}
    current_list_key: str | None = None

    for raw_line in frontmatter.splitlines():
        if not raw_line.strip():
            continue

        if raw_line.startswith("  - ") and current_list_key:
            data.setdefault(current_list_key, []).append(_clean_scalar(raw_line[4:]))
            continue

        if raw_line.startswith("- ") and current_list_key:
            data.setdefault(current_list_key, []).append(_clean_scalar(raw_line[2:]))
            continue

        current_list_key = None
        if ":" not in raw_line:
            continue

        key, value = raw_line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if not value:
            data[key] = []
            current_list_key = key
            continue

        data[key] = _clean_scalar(value)

    return data


def load_note(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    frontmatter_raw, body = extract_frontmatter(text)
    frontmatter = parse_frontmatter(frontmatter_raw)
    relative_path = path.relative_to(ROOT).as_posix()

    aliases = frontmatter.get("aliases", [])
    if isinstance(aliases, str):
        aliases = [aliases]

    source_urls = frontmatter.get("source_urls", [])
    if isinstance(source_urls, str):
        source_urls = [source_urls]

    return {
        "path": path,
        "relative_path": relative_path,
        "stem": path.stem,
        "text": text,
        "body": body,
        "frontmatter_raw": frontmatter_raw,
        "frontmatter": frontmatter,
        "title": frontmatter.get("title", path.stem),
        "note_type": frontmatter.get("note_type", ""),
        "domain": frontmatter.get("domain", ""),
        "status": frontmatter.get("status", ""),
        "aliases": aliases,
        "reviewed_on": frontmatter.get("reviewed_on", ""),
        "review_jurisdiction": frontmatter.get("review_jurisdiction", ""),
        "source_urls": source_urls,
    }


def load_notes(root: Path = ROOT) -> list[dict[str, Any]]:
    return [load_note(path) for path in note_files(root)]


def note_keys(note: dict[str, Any]) -> set[str]:
    keys = {
        note["stem"],
        note["title"],
        note["relative_path"][:-3],
    }
    for alias in note["aliases"]:
        if alias:
            keys.add(alias)
    return {key.strip() for key in keys if key and key.strip()}


def wikilink_targets(note: dict[str, Any]) -> list[str]:
    return [match.group(1).strip() for match in WIKILINK_RE.finditer(note["text"])]


def build_key_index(notes: list[dict[str, Any]]) -> dict[str, str]:
    index: dict[str, str] = {}
    for note in notes:
        for key in note_keys(note):
            index[key] = note["relative_path"]
    return index


def manifest_payload(notes: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "notes": [
            {
                "path": note["relative_path"],
                "title": note["title"],
                "note_type": note["note_type"],
                "domain": note["domain"],
                "status": note["status"],
                "aliases": note["aliases"],
                "reviewed_on": note["reviewed_on"],
                "review_jurisdiction": note["review_jurisdiction"],
                "source_urls": note["source_urls"],
            }
            for note in notes
        ]
    }


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
