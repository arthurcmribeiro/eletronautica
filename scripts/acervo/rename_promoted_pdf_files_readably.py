from __future__ import annotations

import argparse
import json
import os
import re
import unicodedata
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import sys


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent

if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.append(str(SCRIPTS_ROOT))

from vault_tools import ROOT  # noqa: E402


ACERVO_ROOT = ROOT / "90_Revisao_Manual" / "_Acervo_Local"
NOTAS_ROOT = ROOT / "90_Revisao_Manual" / "_Acervo_Notas"
OCR_TEXT_ROOT = ROOT / "90_Revisao_Manual" / "_Dados_Acervo" / "ocr_texts"
OCR_NOTE_ROOT = ROOT / "90_Revisao_Manual" / "_Dados_Acervo" / "ocr_notes"
PROMOTION_MANIFEST = ROOT / "manifest" / "acervo-humano-promoted-all-pdfs.json"
MIGRATION_MANIFEST = ROOT / "manifest" / "acervo-readable-pdf-renames.json"
PROMOTION_REPORT = ROOT / "_Editorial" / "Promocao Integral do Acervo Humano Tecnico.md"
OCR_RESULTS = ROOT / "90_Revisao_Manual" / "_Dados_Acervo" / "ocr-results.json"
OCR_REPORT = ROOT / "_Editorial" / "OCR Controlado - Acervo Principal.md"

MACHINE_NAME_RE = re.compile(r"__.*__.*__h-[0-9a-f]{12}(?:-\d+)?\.pdf$", re.I)
MAX_ABSOLUTE_PATH_LENGTH = 238
TARGET_STEM_OVERRIDES = {
    "06_Bombas_Hidraulica_e_Utilidades/document-91095466-installation-guide-mini-pressurizador-com-pressostato-eletronico-externo-agua-quente-350w-220v-syllent.pdf": "91095466-mini-pressurizador-pressostato-eletronico",
}


@dataclass(slots=True)
class RenamePlan:
    source: str
    old_target: str
    new_target: str
    sha256: str


def path_arg(path: Path) -> str:
    resolved = str(path.resolve())
    if os.name == "nt" and not resolved.startswith("\\\\?\\"):
        return "\\\\?\\" + resolved
    return resolved


def safe_ascii(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    return normalized.encode("ascii", "ignore").decode("ascii")


def file_slug(value: str, *, default: str = "documento", max_length: int = 96) -> str:
    ascii_value = safe_ascii(value)
    ascii_value = re.sub(r"[^A-Za-z0-9]+", "-", ascii_value).strip("-")
    ascii_value = re.sub(r"-{2,}", "-", ascii_value)
    ascii_value = ascii_value.lower()
    if not ascii_value:
        ascii_value = default
    return ascii_value[:max_length].strip("-") or default


def path_exists(path: Path) -> bool:
    return os.path.exists(path_arg(path))


def read_text(path: Path) -> str:
    with open(path_arg(path), "r", encoding="utf-8", errors="ignore") as handle:
        return handle.read()


def write_text(path: Path, value: str) -> None:
    with open(path_arg(path), "w", encoding="utf-8", newline="\n") as handle:
        handle.write(value)


def target_slug_for_parent(value: str, parent: Path, *, default: str = "documento") -> str:
    pdf_budget = MAX_ABSOLUTE_PATH_LENGTH - len(str(parent.resolve())) - len("\\") - len(".pdf")
    note_parent = NOTAS_ROOT / parent.relative_to(ACERVO_ROOT)
    note_budget = MAX_ABSOLUTE_PATH_LENGTH - len(str(note_parent.resolve())) - len("\\") - len(".md")
    max_length = max(32, min(96, pdf_budget, note_budget))
    return file_slug(value, default=default, max_length=max_length)


def load_manifest() -> dict[str, Any]:
    if not path_exists(PROMOTION_MANIFEST):
        raise FileNotFoundError(
            f"Manifesto de promocao nao encontrado: {PROMOTION_MANIFEST}"
        )
    return json.loads(read_text(PROMOTION_MANIFEST))


def unique_target(parent: Path, stem: str, old_path: Path) -> Path:
    for index in range(1, 100):
        suffix = "" if index == 1 else f"-{index}"
        candidate = parent / f"{stem}{suffix}.pdf"
        if candidate == old_path or not path_exists(candidate):
            return candidate
    raise FileExistsError(f"Nao foi possivel criar nome unico em {parent}")


def build_plan(payload: dict[str, Any]) -> list[RenamePlan]:
    plans: list[RenamePlan] = []
    for record in payload.get("records", []):
        if not isinstance(record, dict):
            continue
        target = str(record.get("target", ""))
        source = str(record.get("source", ""))
        status = str(record.get("status", ""))
        old_path = ACERVO_ROOT / target
        should_rename = MACHINE_NAME_RE.search(Path(target).name) is not None
        should_rename = should_rename or len(str(old_path.resolve())) > MAX_ABSOLUTE_PATH_LENGTH
        if status != "copied" or not should_rename:
            continue

        if not path_exists(old_path):
            continue

        source_stem = Path(source).stem
        new_stem = TARGET_STEM_OVERRIDES.get(source) or target_slug_for_parent(
            source_stem,
            old_path.parent,
        )
        new_path = unique_target(old_path.parent, new_stem, old_path)
        new_target = new_path.relative_to(ACERVO_ROOT).as_posix()

        if new_target == target:
            continue

        plans.append(
            RenamePlan(
                source=source,
                old_target=target,
                new_target=new_target,
                sha256=str(record.get("sha256", "")),
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


def companion_rel(target: str) -> str:
    return Path(target).with_suffix(".md").as_posix()


def root_rel_from_acervo(target: str) -> str:
    return "90_Revisao_Manual/_Acervo_Local/" + target


def root_rel_from_note(target: str) -> str:
    return "90_Revisao_Manual/_Acervo_Notas/" + companion_rel(target)


def replacement_pairs(plan: RenamePlan) -> list[tuple[str, str]]:
    old_pdf_root = root_rel_from_acervo(plan.old_target)
    new_pdf_root = root_rel_from_acervo(plan.new_target)
    old_note_root = root_rel_from_note(plan.old_target)
    new_note_root = root_rel_from_note(plan.new_target)
    old_ocr_text = ocr_text_rel(plan.old_target)
    new_ocr_text = ocr_text_rel(plan.new_target)
    old_ocr_note = ocr_note_rel(plan.old_target)
    new_ocr_note = ocr_note_rel(plan.new_target)

    old_pdf_abs = (ACERVO_ROOT / plan.old_target).resolve().as_posix()
    new_pdf_abs = (ACERVO_ROOT / plan.new_target).resolve().as_posix()
    old_note_abs = (NOTAS_ROOT / companion_rel(plan.old_target)).resolve().as_posix()
    new_note_abs = (NOTAS_ROOT / companion_rel(plan.new_target)).resolve().as_posix()
    old_ocr_text_abs = (ROOT / old_ocr_text).resolve().as_posix()
    new_ocr_text_abs = (ROOT / new_ocr_text).resolve().as_posix()
    old_ocr_note_abs = (ROOT / old_ocr_note).resolve().as_posix()
    new_ocr_note_abs = (ROOT / new_ocr_note).resolve().as_posix()

    old_pdf_name = Path(plan.old_target).name
    new_pdf_name = Path(plan.new_target).name
    old_note_name = Path(plan.old_target).with_suffix(".md").name
    new_note_name = Path(plan.new_target).with_suffix(".md").name

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
        (old_pdf_name, new_pdf_name),
        (old_note_name, new_note_name),
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


def update_promotion_manifest(
    payload: dict[str, Any],
    plan_by_old: dict[str, RenamePlan],
) -> None:
    for record in payload.get("records", []):
        if not isinstance(record, dict):
            continue
        target = str(record.get("target", ""))
        plan = plan_by_old.get(target)
        if plan:
            record["target"] = plan.new_target


def update_ocr_results(
    plan_by_old_root: dict[str, RenamePlan],
    *,
    apply_changes: bool,
) -> int:
    if not path_exists(OCR_RESULTS):
        return 0
    payload = json.loads(read_text(OCR_RESULTS))
    changed = False

    for record in payload.get("results", []):
        if not isinstance(record, dict):
            continue
        source_pdf = str(record.get("source_pdf", ""))
        plan = plan_by_old_root.get(source_pdf)
        if not plan:
            continue
        record["source_pdf"] = root_rel_from_acervo(plan.new_target)
        record["acervo_relative_path"] = plan.new_target
        record["file_name"] = Path(plan.new_target).name
        record["output_text"] = ocr_text_rel(plan.new_target)
        record["output_note"] = ocr_note_rel(plan.new_target)
        changed = True

    if changed and apply_changes:
        write_text(OCR_RESULTS, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    return 1 if changed else 0


def move_related_files(plan: RenamePlan, *, apply_changes: bool) -> dict[str, bool]:
    old_note = NOTAS_ROOT / companion_rel(plan.old_target)
    new_note = NOTAS_ROOT / companion_rel(plan.new_target)
    old_ocr_text = ROOT / ocr_text_rel(plan.old_target)
    new_ocr_text = ROOT / ocr_text_rel(plan.new_target)
    old_ocr_note = ROOT / ocr_note_rel(plan.old_target)
    new_ocr_note = ROOT / ocr_note_rel(plan.new_target)

    return {
        "pdf": move_if_exists(
            ACERVO_ROOT / plan.old_target,
            ACERVO_ROOT / plan.new_target,
            apply_changes=apply_changes,
        ),
        "note": move_if_exists(old_note, new_note, apply_changes=apply_changes),
        "ocr_text": move_if_exists(old_ocr_text, new_ocr_text, apply_changes=apply_changes),
        "ocr_note": move_if_exists(old_ocr_note, new_ocr_note, apply_changes=apply_changes),
    }


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
                "source": plan.source,
                "old_target": plan.old_target,
                "new_target": plan.new_target,
                "sha256": plan.sha256,
            }
            for plan in plans
        ],
    }
    if apply_changes:
        write_text(MIGRATION_MANIFEST, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def rename_all(*, apply_changes: bool) -> int:
    payload = load_manifest()
    plans = build_plan(payload)
    plan_by_old = {plan.old_target: plan for plan in plans}
    plan_by_old_root = {root_rel_from_acervo(plan.old_target): plan for plan in plans}

    all_pairs: list[tuple[str, str]] = []
    moved_counts = {"pdf": 0, "note": 0, "ocr_text": 0, "ocr_note": 0}

    for plan in plans:
        moved = move_related_files(plan, apply_changes=apply_changes)
        for key, did_move in moved.items():
            moved_counts[key] += int(did_move)
        all_pairs.extend(replacement_pairs(plan))

    text_updates = 0
    text_targets = [
        PROMOTION_REPORT,
        OCR_REPORT,
    ]

    for plan in plans:
        text_targets.extend(
            [
                NOTAS_ROOT / companion_rel(plan.new_target),
                ROOT / ocr_text_rel(plan.new_target),
                ROOT / ocr_note_rel(plan.new_target),
            ]
        )

    unique_text_targets = sorted(set(text_targets), key=lambda item: item.as_posix())
    for path in unique_text_targets:
        text_updates += replace_in_file(path, all_pairs, apply_changes=apply_changes)

    update_promotion_manifest(payload, plan_by_old)
    ocr_updates = update_ocr_results(plan_by_old_root, apply_changes=apply_changes)

    if apply_changes:
        write_text(PROMOTION_MANIFEST, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")

    write_migration_manifest(plans, moved_counts, apply_changes=apply_changes)

    mode = "APLICADO" if apply_changes else "DRY-RUN"
    verb_plural = "movidos" if apply_changes else "planejados"
    verb_feminine_plural = "movidas" if apply_changes else "planejadas"
    print(f"Modo: {mode}")
    print(f"PDFs a renomear: {len(plans)}")
    print(f"PDFs {verb_plural}: {moved_counts['pdf']}")
    print(f"Notas {verb_feminine_plural}: {moved_counts['note']}")
    print(f"Textos OCR {verb_plural}: {moved_counts['ocr_text']}")
    print(f"Notas OCR {verb_feminine_plural}: {moved_counts['ocr_note']}")
    print(f"Arquivos textuais {'atualizados' if apply_changes else 'com atualizacao prevista'}: {text_updates + ocr_updates}")
    if plans:
        print("")
        print("Amostra:")
        for plan in plans[:10]:
            print(f"- {plan.old_target} -> {plan.new_target}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Renomeia PDFs promovidos do acervo para nomes legiveis por humanos."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Aplica a migracao. Sem esta flag, executa dry-run.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return rename_all(apply_changes=args.apply)


if __name__ == "__main__":
    raise SystemExit(main())
