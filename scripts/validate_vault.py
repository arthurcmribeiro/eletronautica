from __future__ import annotations

import sys

from vault_tools import ROOT, build_key_index, load_notes, wikilink_targets


SENSITIVE_PATTERNS = {
    "NORMAM-02": "Referência antiga para esporte e recreio; revisar para NORMAM-211 quando aplicável.",
    "ABYC TE-13": "Usar a referência ABYC E-13 para a família de lítio nesta base.",
    "NBR 13885": "Código ABNT precisa de validação oficial antes de ser citado nesta base.",
    "ABNT NBR 16033": "Código ABNT precisa de validação oficial antes de ser citado nesta base.",
}

WARN_NOTE_TYPES = {"reference", "technical-note", "procedure", "system"}
MAX_PRINT = 80


def print_items(title: str, items: list[str]) -> None:
    if not items:
        return

    print(f"\n{title}:")
    for item in items[:MAX_PRINT]:
        print(f"- {item}")

    remaining = len(items) - MAX_PRINT
    if remaining > 0:
        print(f"- ... e mais {remaining} itens")


def main() -> int:
    notes = load_notes(ROOT)
    key_index = build_key_index(notes)
    errors: list[str] = []
    warnings: list[str] = []

    for note in notes:
        relative_path = note["relative_path"]
        frontmatter = note["frontmatter"]

        if "title" not in frontmatter:
            errors.append(f"{relative_path}: frontmatter sem 'title'")
        if "note_type" not in frontmatter:
            errors.append(f"{relative_path}: frontmatter sem 'note_type'")

        if note["note_type"] in WARN_NOTE_TYPES:
            if not note["reviewed_on"]:
                warnings.append(f"{relative_path}: sem 'reviewed_on'")
            if not note["review_jurisdiction"]:
                warnings.append(f"{relative_path}: sem 'review_jurisdiction'")
            if not note["source_urls"]:
                warnings.append(f"{relative_path}: sem 'source_urls'")

        for target in wikilink_targets(note):
            if target not in key_index:
                errors.append(
                    f"{relative_path}: wikilink sem destino resolvido -> [[{target}]]"
                )

        for pattern, reason in SENSITIVE_PATTERNS.items():
            if pattern in note["text"]:
                warnings.append(
                    f"{relative_path}: referência sensível '{pattern}' ({reason})"
                )

    print(f"Notas analisadas: {len(notes)}")
    print(f"Erros: {len(errors)}")
    print(f"Avisos: {len(warnings)}")

    print_items("Avisos", warnings)

    if errors:
        print_items("Erros", errors)
        return 1

    print("\nValidação concluída sem erros bloqueantes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
