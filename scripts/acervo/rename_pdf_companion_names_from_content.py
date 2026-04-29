from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent

if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.append(str(SCRIPTS_ROOT))

from build_pdf_companion_notes import (  # noqa: E402
    ACERVO_LOCAL_ROOT,
    ACERVO_NOTAS_ROOT,
    ROOT,
    NoteRecord,
    collect_pdf_records,
    strip_accents,
)


OCR_RESULTS_PATH = ROOT / "90_Revisao_Manual" / "_Dados_Acervo" / "ocr-results.json"
OCR_TEXT_ROOT = ROOT / "90_Revisao_Manual" / "_Dados_Acervo" / "ocr_texts"
OCR_NOTE_ROOT = ROOT / "90_Revisao_Manual" / "_Dados_Acervo" / "ocr_notes"
MIGRATION_MANIFEST = ROOT / "manifest" / "acervo-content-based-renames.json"
PROMOTION_MANIFEST = ROOT / "manifest" / "acervo-humano-promoted-all-pdfs.json"
READABLE_RENAMES_MANIFEST = ROOT / "manifest" / "acervo-readable-pdf-renames.json"
PROMOTION_REPORT = ROOT / "_Editorial" / "Promocao Integral do Acervo Humano Tecnico.md"
OCR_REPORT = ROOT / "_Editorial" / "OCR Controlado - Acervo Principal.md"

MAX_ABSOLUTE_PATH_LENGTH = 238
REFRESH_NAME_RE = re.compile(r"__|legacy-espelho|h-[0-9a-f]{8,}", re.I)
STRONG_DOCUMENT_CODE_RE = re.compile(
    r"^(?:\d{3,4}-\d{3,4}[A-Z]?|TP-?\d{4}[A-Z]?|A\d{3,}[A-Z0-9]*)$",
    re.I,
)


@dataclass(frozen=True, slots=True)
class RenamePlan:
    old_target: str
    new_target: str
    title: str
    source_sha256: str


def path_arg(path: Path) -> str:
    resolved = str(path.resolve())
    if os.name == "nt" and not resolved.startswith("\\\\?\\"):
        return "\\\\?\\" + resolved
    return resolved


def path_exists(path: Path) -> bool:
    return os.path.exists(path_arg(path))


def read_text(path: Path) -> str:
    with open(path_arg(path), "r", encoding="utf-8", errors="ignore") as handle:
        return handle.read()


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path_arg(path), "w", encoding="utf-8", newline="\n") as handle:
        handle.write(value)


def file_slug(value: str, *, default: str = "documento", max_length: int = 110) -> str:
    ascii_value = strip_accents(value)
    ascii_value = re.sub(r"[^A-Za-z0-9]+", "-", ascii_value).strip("-")
    ascii_value = re.sub(r"-{2,}", "-", ascii_value).lower()
    ascii_value = re.sub(r"^(referencia-tecnica|referencia-geral|referencia-comercial)-", "", ascii_value)
    ascii_value = re.sub(r"-(n-a|sem-auditoria)$", "", ascii_value)
    if not ascii_value:
        ascii_value = default
    return ascii_value[:max_length].strip("-") or default


def note_target_for_pdf_target(target: str) -> str:
    return Path(target).with_suffix(".md").as_posix()


def root_pdf_rel(target: str) -> str:
    return "90_Revisao_Manual/_Acervo_Local/" + target


def root_note_rel(target: str) -> str:
    return "90_Revisao_Manual/_Acervo_Notas/" + note_target_for_pdf_target(target)


def ocr_text_rel(target: str) -> str:
    return (
        "90_Revisao_Manual/_Dados_Acervo/ocr_texts/"
        + Path(target).with_suffix(".ocr.txt").as_posix()
    )


def ocr_note_rel(target: str) -> str:
    return (
        "90_Revisao_Manual/_Dados_Acervo/ocr_notes/"
        + Path(target).with_suffix(".ocr.md").as_posix()
    )


def should_refresh_name(path: Path) -> bool:
    return REFRESH_NAME_RE.search(path.name) is not None


def cleaned_existing_stem(stem: str) -> str:
    cleaned = stem.replace("__", "-")
    cleaned = re.sub(r"-?legacy-espelho\b", "", cleaned, flags=re.I)
    cleaned = re.sub(r"-?h-[0-9a-f]{8,}(?:-\d+)?$", "", cleaned, flags=re.I)
    cleaned = cleaned.replace("catalogo-brochure", "catalogo")
    cleaned = re.sub(r"-{2,}", "-", cleaned).strip("-")
    return cleaned


def strong_document_code(record: NoteRecord) -> str:
    for code in record.document_codes:
        normalized = code.upper().replace(" ", "-")
        if STRONG_DOCUMENT_CODE_RE.fullmatch(normalized):
            return normalized
    return ""


def target_stem_for_record(record: NoteRecord) -> str:
    parent = record.pdf_path.parent
    note_parent = ACERVO_NOTAS_ROOT / record.pdf_path.parent.relative_to(ACERVO_LOCAL_ROOT)
    pdf_budget = MAX_ABSOLUTE_PATH_LENGTH - len(str(parent.resolve())) - len("\\") - len(".pdf")
    note_budget = MAX_ABSOLUTE_PATH_LENGTH - len(str(note_parent.resolve())) - len("\\") - len(".md")
    max_length = max(36, min(110, pdf_budget, note_budget))

    base = cleaned_existing_stem(record.pdf_path.stem)
    code = strong_document_code(record)
    if code and "legacy-espelho" in record.pdf_path.stem.casefold():
        code_slug = file_slug(code, max_length=24)
        if code_slug not in file_slug(base, max_length=max_length):
            base = f"{base}-{code_slug}"

    return file_slug(base, max_length=max_length)


def unique_target(parent: Path, stem: str, old_pdf: Path) -> Path:
    for index in range(1, 100):
        suffix = "" if index == 1 else f"-{index}"
        candidate = parent / f"{stem}{suffix}.pdf"
        candidate_note = ACERVO_NOTAS_ROOT / candidate.relative_to(ACERVO_LOCAL_ROOT).with_suffix(".md")
        if candidate == old_pdf:
            return candidate
        if not path_exists(candidate) and not path_exists(candidate_note):
            return candidate
    raise FileExistsError(f"Nao foi possivel criar nome unico em {parent}")


def build_plan(records: list[NoteRecord]) -> list[RenamePlan]:
    plans: list[RenamePlan] = []
    for record in records:
        if not should_refresh_name(record.pdf_path):
            continue

        stem = target_stem_for_record(record)
        new_pdf = unique_target(record.pdf_path.parent, stem, record.pdf_path)
        if new_pdf.name == record.pdf_path.name:
            continue

        plans.append(
            RenamePlan(
                old_target=record.relative_pdf,
                new_target=new_pdf.relative_to(ACERVO_LOCAL_ROOT).as_posix(),
                title=record.title,
                source_sha256=record.source_sha256,
            )
        )
    return plans


def move_if_exists(old_path: Path, new_path: Path, *, apply_changes: bool) -> bool:
    if not path_exists(old_path):
        return False
    if path_exists(new_path):
        raise FileExistsError(f"Destino ja existe: {new_path}")
    if apply_changes:
        new_path.parent.mkdir(parents=True, exist_ok=True)
        os.replace(path_arg(old_path), path_arg(new_path))
    return True


def replacement_pairs(plan: RenamePlan) -> list[tuple[str, str]]:
    old_pdf_root = root_pdf_rel(plan.old_target)
    new_pdf_root = root_pdf_rel(plan.new_target)
    old_note_root = root_note_rel(plan.old_target)
    new_note_root = root_note_rel(plan.new_target)
    old_ocr_text = ocr_text_rel(plan.old_target)
    new_ocr_text = ocr_text_rel(plan.new_target)
    old_ocr_note = ocr_note_rel(plan.old_target)
    new_ocr_note = ocr_note_rel(plan.new_target)

    old_pdf_abs = (ACERVO_LOCAL_ROOT / plan.old_target).resolve().as_posix()
    new_pdf_abs = (ACERVO_LOCAL_ROOT / plan.new_target).resolve().as_posix()
    old_note_abs = (ACERVO_NOTAS_ROOT / note_target_for_pdf_target(plan.old_target)).resolve().as_posix()
    new_note_abs = (ACERVO_NOTAS_ROOT / note_target_for_pdf_target(plan.new_target)).resolve().as_posix()
    old_ocr_text_abs = (ROOT / old_ocr_text).resolve().as_posix()
    new_ocr_text_abs = (ROOT / new_ocr_text).resolve().as_posix()
    old_ocr_note_abs = (ROOT / old_ocr_note).resolve().as_posix()
    new_ocr_note_abs = (ROOT / new_ocr_note).resolve().as_posix()

    pairs = [
        (plan.old_target, plan.new_target),
        (old_pdf_root, new_pdf_root),
        (old_note_root, new_note_root),
        (old_ocr_text, new_ocr_text),
        (old_ocr_note, new_ocr_note),
        (old_pdf_abs, new_pdf_abs),
        (old_pdf_abs.replace("/", "\\"), new_pdf_abs.replace("/", "\\")),
        (old_note_abs, new_note_abs),
        (old_note_abs.replace("/", "\\"), new_note_abs.replace("/", "\\")),
        (old_ocr_text_abs, new_ocr_text_abs),
        (old_ocr_text_abs.replace("/", "\\"), new_ocr_text_abs.replace("/", "\\")),
        (old_ocr_note_abs, new_ocr_note_abs),
        (old_ocr_note_abs.replace("/", "\\"), new_ocr_note_abs.replace("/", "\\")),
        (Path(plan.old_target).name, Path(plan.new_target).name),
        (Path(plan.old_target).with_suffix(".md").name, Path(plan.new_target).with_suffix(".md").name),
        (Path(old_ocr_text).name, Path(new_ocr_text).name),
        (Path(old_ocr_note).name, Path(new_ocr_note).name),
    ]
    return [(old, new) for old, new in pairs if old != new]


def replace_in_file(path: Path, pairs: list[tuple[str, str]], *, apply_changes: bool) -> int:
    if not path_exists(path):
        return 0
    text = read_text(path)
    updated = text
    for old, new in pairs:
        updated = updated.replace(old, new)
    if updated == text:
        return 0
    if apply_changes:
        write_text(path, updated)
    return 1


def move_related_files(plan: RenamePlan, *, apply_changes: bool) -> dict[str, bool]:
    old_note = ACERVO_NOTAS_ROOT / note_target_for_pdf_target(plan.old_target)
    new_note = ACERVO_NOTAS_ROOT / note_target_for_pdf_target(plan.new_target)
    old_ocr_text = ROOT / ocr_text_rel(plan.old_target)
    new_ocr_text = ROOT / ocr_text_rel(plan.new_target)
    old_ocr_note = ROOT / ocr_note_rel(plan.old_target)
    new_ocr_note = ROOT / ocr_note_rel(plan.new_target)

    return {
        "pdf": move_if_exists(ACERVO_LOCAL_ROOT / plan.old_target, ACERVO_LOCAL_ROOT / plan.new_target, apply_changes=apply_changes),
        "note": move_if_exists(old_note, new_note, apply_changes=apply_changes),
        "ocr_text": move_if_exists(old_ocr_text, new_ocr_text, apply_changes=apply_changes),
        "ocr_note": move_if_exists(old_ocr_note, new_ocr_note, apply_changes=apply_changes),
    }


def update_ocr_results(plan_by_old_root: dict[str, RenamePlan], *, apply_changes: bool) -> int:
    if not path_exists(OCR_RESULTS_PATH):
        return 0
    payload = json.loads(read_text(OCR_RESULTS_PATH))
    changed = False
    for record in payload.get("results", []):
        if not isinstance(record, dict):
            continue
        source_pdf = str(record.get("source_pdf", ""))
        plan = plan_by_old_root.get(source_pdf)
        if not plan:
            continue
        record["source_pdf"] = root_pdf_rel(plan.new_target)
        record["acervo_relative_path"] = plan.new_target
        record["file_name"] = Path(plan.new_target).name
        record["output_text"] = ocr_text_rel(plan.new_target)
        record["output_note"] = ocr_note_rel(plan.new_target)
        changed = True

    if changed and apply_changes:
        write_text(OCR_RESULTS_PATH, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    return 1 if changed else 0


def update_json_by_target(path: Path, plan_by_old: dict[str, RenamePlan], *, apply_changes: bool) -> int:
    if not path_exists(path):
        return 0
    try:
        payload = json.loads(read_text(path))
    except json.JSONDecodeError:
        return 0

    changed = False
    for key in ("records", "files", "pdfs"):
        items = payload.get(key)
        if not isinstance(items, list):
            continue
        for item in items:
            if not isinstance(item, dict):
                continue
            for field in ("target", "acervo_relative_path"):
                value = str(item.get(field, ""))
                plan = plan_by_old.get(value)
                if plan:
                    item[field] = plan.new_target
                    changed = True
            relative_path = str(item.get("relative_path", ""))
            plan = plan_by_old.get(relative_path.removeprefix("90_Revisao_Manual/_Acervo_Local/"))
            if plan:
                item["relative_path"] = root_pdf_rel(plan.new_target)
                item["file_name"] = Path(plan.new_target).name
                changed = True

    if changed and apply_changes:
        write_text(path, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    return 1 if changed else 0


def write_migration_manifest(
    plans: list[RenamePlan],
    moved_counts: dict[str, int],
    *,
    apply_changes: bool,
) -> None:
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "applied": apply_changes,
        "rename_count": len(plans),
        "moved_counts": moved_counts,
        "records": [
            {
                "old_target": plan.old_target,
                "new_target": plan.new_target,
                "title": plan.title,
                "source_sha256": plan.source_sha256,
            }
            for plan in plans
        ],
    }
    if apply_changes:
        write_text(MIGRATION_MANIFEST, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def rename_all(*, apply_changes: bool) -> int:
    records = collect_pdf_records()
    plans = build_plan(records)
    plan_by_old = {plan.old_target: plan for plan in plans}
    plan_by_old_root = {root_pdf_rel(plan.old_target): plan for plan in plans}

    all_pairs: list[tuple[str, str]] = []
    moved_counts = {"pdf": 0, "note": 0, "ocr_text": 0, "ocr_note": 0}

    for plan in plans:
        moved = move_related_files(plan, apply_changes=apply_changes)
        for key, did_move in moved.items():
            moved_counts[key] += int(did_move)
        all_pairs.extend(replacement_pairs(plan))

    text_targets = [PROMOTION_REPORT, OCR_REPORT]
    for plan in plans:
        text_targets.extend(
            [
                ACERVO_NOTAS_ROOT / note_target_for_pdf_target(plan.new_target),
                ROOT / ocr_text_rel(plan.new_target),
                ROOT / ocr_note_rel(plan.new_target),
            ]
        )

    text_updates = 0
    for path in sorted(set(text_targets), key=lambda item: item.as_posix()):
        text_updates += replace_in_file(path, all_pairs, apply_changes=apply_changes)

    json_updates = 0
    for path in (PROMOTION_MANIFEST, READABLE_RENAMES_MANIFEST):
        json_updates += update_json_by_target(path, plan_by_old, apply_changes=apply_changes)
    json_updates += update_ocr_results(plan_by_old_root, apply_changes=apply_changes)

    write_migration_manifest(plans, moved_counts, apply_changes=apply_changes)

    mode = "APLICADO" if apply_changes else "DRY-RUN"
    print(f"Modo: {mode}")
    print(f"PDFs a renomear: {len(plans)}")
    print(f"PDFs movidos: {moved_counts['pdf']}")
    print(f"Notas movidas: {moved_counts['note']}")
    print(f"Textos OCR movidos: {moved_counts['ocr_text']}")
    print(f"Notas OCR movidas: {moved_counts['ocr_note']}")
    print(f"Arquivos textuais atualizados: {text_updates}")
    print(f"JSONs atualizados: {json_updates}")

    if plans:
        print("")
        print("Amostra:")
        for plan in plans[:12]:
            print(f"- {plan.old_target} -> {plan.new_target}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Renomeia PDFs e notas companheiras com base no conteudo extraido."
    )
    parser.add_argument("--apply", action="store_true", help="Aplica a migracao. Sem esta flag, executa dry-run.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return rename_all(apply_changes=args.apply)


if __name__ == "__main__":
    raise SystemExit(main())
