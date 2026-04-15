from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SPEC_DIR = ROOT / "_visuals" / "specs"
EXCLUDED_PARTS = {".git", ".obsidian", ".claude", "_visuals"}


def normalize_key(value: str) -> str:
    normalized = (
        unicodedata.normalize("NFKD", value)
        .encode("ascii", "ignore")
        .decode("ascii")
        .lower()
    )
    normalized = normalized.replace("\\", "/")
    normalized = re.sub(r"[^a-z0-9/(). -]+", "", normalized)
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized.strip()


def note_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*.md")
        if not any(part in EXCLUDED_PARTS for part in path.parts)
        and path.parts[0] != "_Editorial"
    ]


def build_note_index() -> dict[str, Path]:
    index: dict[str, Path] = {}
    for path in note_files():
        relative = path.relative_to(ROOT).as_posix()
        index[normalize_key(relative)] = path
        index.setdefault(normalize_key(path.name), path)
    return index


def load_specs() -> list[dict]:
    return [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted(SPEC_DIR.glob("*.json"))
    ]


def relative_visual_path(note: Path, slug: str, suffix: str) -> str:
    target = ROOT / "_visuals" / "generated" / f"{slug}.{suffix}"
    return Path("../" * (len(note.relative_to(ROOT).parts) - 1)).joinpath(
        target.relative_to(ROOT)
    ).as_posix()


def visual_block(note: Path, spec: dict) -> str:
    slug = spec["slug"]
    svg = relative_visual_path(note, slug, "svg")
    md = relative_visual_path(note, slug, "md")
    title = spec["title"]
    goal = spec["didactic_goal"]
    caution = spec["caution"]
    return (
        "## Visual didático\n\n"
        f"![{title}]({svg})\n\n"
        f"{goal}\n\n"
        f"**Cautela:** {caution}\n\n"
        f"Material de apoio: [{title}]({md})\n\n"
    )


def insert_block(markdown: str, block: str) -> str:
    anchors = [
        "\n## Integração com outras notas\n",
        "\n## Integracao com outras notas\n",
        "\n## FAQ\n",
        "\n## Perguntas que esta nota responde\n",
    ]
    for anchor in anchors:
        index = markdown.find(anchor)
        if index != -1:
            return markdown[: index + 1] + block + markdown[index + 1 :]
    return markdown.rstrip() + "\n\n" + block


def main() -> None:
    index = build_note_index()
    changed = 0
    skipped = 0
    unresolved: list[str] = []
    for spec in load_specs():
        slug = spec["slug"]
        target: Path | None = None
        for candidate in spec.get("target_notes", []):
            target = index.get(normalize_key(candidate))
            if target:
                break
        if not target:
            unresolved.append(slug)
            continue

        text = target.read_text(encoding="utf-8-sig")
        if f"{slug}.svg" in text:
            skipped += 1
            continue
        updated = insert_block(text, visual_block(target, spec))
        target.write_text(updated, encoding="utf-8")
        changed += 1
        print(f"Integrado: {slug} -> {target.relative_to(ROOT)}")

    print(f"Alteradas: {changed}")
    print(f"Ja integradas: {skipped}")
    if unresolved:
        print("Sem alvo resolvido:")
        for slug in unresolved:
            print(f"- {slug}")


if __name__ == "__main__":
    main()
