from __future__ import annotations

import re
import sys

from vault_tools import ROOT, build_key_index, load_notes, wikilink_targets


SENSITIVE_PATTERNS = {
    "NORMAM-02": "Referência antiga para esporte e recreio; revisar para NORMAM-211 quando aplicável.",
    "ABYC TE-13": "Usar a referência ABYC E-13 para a família de lítio nesta base.",
    "NBR 13885": "Código ABNT precisa de validação oficial antes de ser citado nesta base.",
    "ABNT NBR 16033": "Código ABNT precisa de validação oficial antes de ser citado nesta base.",
}
SENSITIVE_PATTERN_EXCEPTIONS = {
    "NORMAM-02": {
        "10_Fundamentos_e_Projeto/Normas e Regulamentações — Abyc Iso e Brasil.md",
        "_Editorial/convencao_citacao_normativa.md",
        "_Editorial/frontmatter_migration_20260417.md",
        "_Editorial/frontmatter_migration_20260418.md",
        "_Editorial/plano_execucao_auditoria.md",
    },
    "ABYC TE-13": {
        "_Editorial/convencao_citacao_normativa.md",
    },
    "NBR 13885": {
        "_Editorial/bugs_conhecidos.md",
        "_Editorial/convencao_citacao_normativa.md",
        "_Editorial/frontmatter_migration_20260417.md",
        "_Editorial/frontmatter_migration_20260418.md",
    },
    "ABNT NBR 16033": {
        "_Editorial/convencao_citacao_normativa.md",
        "_Editorial/frontmatter_migration_20260417.md",
        "_Editorial/frontmatter_migration_20260418.md",
    },
}

WARN_NOTE_TYPES = {"reference", "technical-note", "procedure", "system"}
MAX_PRINT = 80
LOW_CONFIDENCE_EXTRACTION_METHODS = {
    "pdf-stream-strings-low-confidence",
    "no-text-detected",
}
STAGING_TMP_SOURCE_RE = re.compile(
    r"(^|/)_*(?:tmp\d*)-renomear-\d+(?:-\d+)?\.[^/]+$",
    re.I,
)
SUSPICIOUS_COMPANION_TOKENS = {
    "board",
    "camera",
    "command",
    "courses",
    "cursos",
    "diagrama",
    "diagramas",
    "electrical",
    "eletrica",
    "energy",
    "equipa",
    "espelho",
    "esquematico",
    "estudo",
    "estudos",
    "from",
    "fundamentos",
    "fusion",
    "genset",
    "hidraulico",
    "instalacao",
    "internos",
    "introduction",
    "international",
    "issue",
    "january",
    "legacy",
    "ligacao",
    "list",
    "materiais",
    "mechanicsburg",
    "motores",
    "nautica",
    "olathe",
    "performance",
    "printed",
    "products",
    "propulsao",
    "raphael",
    "quality",
    "residual",
    "sets",
    "street",
    "support",
    "technical",
    "this",
    "transducers",
    "turbo",
    "trusted",
}
DECIMAL_ARTIFACT_RE = re.compile(r"\d+\.\d{3,}")
ACERVO_LOCAL_ROOT = ROOT / "90_Revisao_Manual" / "_Acervo_Local"
ACERVO_NOTAS_ROOT = ROOT / "90_Revisao_Manual" / "_Acervo_Notas"


def print_items(title: str, items: list[str]) -> None:
    if not items:
        return

    print(f"\n{title}:")
    for item in items[:MAX_PRINT]:
        print(f"- {item}")

    remaining = len(items) - MAX_PRINT
    if remaining > 0:
        print(f"- ... e mais {remaining} itens")


def companion_signal_items(note_text: str, prefix: str) -> list[str]:
    for line in note_text.splitlines():
        if not line.startswith(prefix):
            continue
        payload = line.split("`", 1)[1].rsplit("`", 1)[0].strip()
        if payload == "n/a":
            return []
        return [item.strip() for item in payload.split(",") if item.strip()]
    return []


def suspicious_companion_items(items: list[str]) -> list[str]:
    suspicious: list[str] = []
    for item in items:
        lowered = item.casefold()
        if lowered in SUSPICIOUS_COMPANION_TOKENS:
            suspicious.append(item)
            continue
        if lowered.endswith("-") or "legacy" in lowered or "espelho" in lowered:
            suspicious.append(item)
            continue
        if DECIMAL_ARTIFACT_RE.search(item):
            suspicious.append(item)
    return suspicious


def suspicious_curation_model_line(note_text: str) -> str | None:
    lines = note_text.splitlines()
    for index, line in enumerate(lines):
        if line.strip() != "### Modelos cobertos confirmados":
            continue
        if index + 1 >= len(lines):
            return None
        candidate = lines[index + 1].strip()
        if candidate.startswith("- `") and DECIMAL_ARTIFACT_RE.search(candidate):
            return candidate
        return None
    return None


def validate_main_acervo_pdf_structure(errors: list[str]) -> None:
    if not ACERVO_LOCAL_ROOT.exists():
        return

    for pdf_path in sorted(ACERVO_LOCAL_ROOT.rglob("*.pdf")):
        relative_pdf = pdf_path.relative_to(ACERVO_LOCAL_ROOT)
        if relative_pdf.parts and relative_pdf.parts[0] == "Acervo do humano":
            continue

        if len(relative_pdf.parts) < 4:
            errors.append(
                f"90_Revisao_Manual/_Acervo_Local/{relative_pdf.as_posix()}: "
                "PDF no acervo principal fora do padrao Sistema/Marca/Familia"
            )
            continue

        expected_note = ACERVO_NOTAS_ROOT / relative_pdf.with_suffix(".md")
        if not expected_note.exists():
            errors.append(
                f"90_Revisao_Manual/_Acervo_Local/{relative_pdf.as_posix()}: "
                f"sem nota companheira esperada em {expected_note.relative_to(ROOT).as_posix()}"
            )


def main() -> int:
    notes = load_notes(ROOT)
    key_index = build_key_index(notes)
    errors: list[str] = []
    warnings: list[str] = []

    validate_main_acervo_pdf_structure(errors)

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
            exceptions = SENSITIVE_PATTERN_EXCEPTIONS.get(pattern, set())
            if pattern in note["text"] and relative_path not in exceptions:
                warnings.append(
                    f"{relative_path}: referência sensível '{pattern}' ({reason})"
                )

        if note["note_type"] == "acervo-companion":
            extraction_method = frontmatter.get("extraction_method", "")
            text_extractable = frontmatter.get("text_extractable", "")
            source_file = frontmatter.get("source_file", "")
            is_main_acervo_companion = (
                relative_path.startswith("90_Revisao_Manual/_Acervo_Notas/")
                and "/Acervo do humano/" not in relative_path
            )
            if (
                is_main_acervo_companion
                and frontmatter.get("acervo_origin") != "acervo-principal"
            ):
                errors.append(
                    f"{relative_path}: acervo principal sem acervo_origin='acervo-principal'"
                )

            if (
                extraction_method in LOW_CONFIDENCE_EXTRACTION_METHODS
                and text_extractable != "nao"
            ):
                warnings.append(
                    f"{relative_path}: extração de baixa confiança marcada como texto extraível"
                )

            if (
                frontmatter.get("acervo_origin") == "humano-staging"
                and source_file
                and STAGING_TMP_SOURCE_RE.search(source_file)
            ):
                warnings.append(
                    f"{relative_path}: source_file ainda aponta para nome temporario ({source_file})"
                )

            model_items = companion_signal_items(
                note["text"], "- codigos/modelos detectados: "
            )
            suspicious_items = suspicious_companion_items(model_items)
            if suspicious_items:
                joined = ", ".join(suspicious_items[:4])
                warnings.append(
                    f"{relative_path}: codigos/modelos detectados com ruído ({joined})"
                )

            curation_line = suspicious_curation_model_line(note["text"])
            if curation_line:
                warnings.append(
                    f"{relative_path}: bloco de curadoria com modelos improváveis ({curation_line})"
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
