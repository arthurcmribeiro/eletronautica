from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent

if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.append(str(SCRIPTS_ROOT))

from vault_tools import ROOT, extract_frontmatter, parse_frontmatter, write_json  # noqa: E402


ACERVO_NOTAS_ROOT = ROOT / "90_Revisao_Manual" / "_Acervo_Notas"
AUDIT_PATH = ROOT / "manifest" / "acervo-pdf-toolchain-audit.json"
OCR_RESULTS_PATH = ROOT / "90_Revisao_Manual" / "_Dados_Acervo" / "ocr-results.json"
NON_PDF_MANIFEST_PATH = ROOT / "manifest" / "acervo-humano-non-pdf-support.json"
PIPELINE_MANIFEST_PATH = ROOT / "manifest" / "pdf-pipeline-last-run.json"
OUTPUT_JSON_PATH = ROOT / "manifest" / "acervo-curation-dashboard.json"
OUTPUT_NOTE_PATH = (
    ROOT
    / "90_Revisao_Manual"
    / "10_Indices_e_Paineis"
    / "Painel de Curadoria do Acervo.md"
)

CURATION_BLOCK_RE = re.compile(
    r"<!-- CURADORIA-HUMANA:START -->.*?<!-- CURADORIA-HUMANA:END -->",
    re.S,
)

TECHNICAL_SIGNALS = (
    "abyc",
    "alternador",
    "alternator",
    "battery",
    "bateria",
    "bilge",
    "bomba",
    "bonding",
    "bus",
    "charger",
    "climat",
    "control",
    "diagnostic",
    "dometic",
    "engine",
    "furuno",
    "garmin",
    "generator",
    "gerador",
    "ground",
    "installation",
    "inverter",
    "kohler",
    "marine",
    "motor",
    "onan",
    "operation",
    "parts",
    "pump",
    "raymarine",
    "service",
    "shore",
    "thruster",
    "victron",
    "wiring",
)
PERSONAL_SIGNALS = (
    "alice",
    "arthur",
    "banco",
    "boleto",
    "certidao",
    "certificado",
    "consular",
    "contratto",
    "covid",
    "cpf",
    "diploma",
    "fatura",
    "historico",
    "imposto",
    "matricula",
    "passaporte",
    "policia",
    "poupatempo",
    "recibo",
    "viagem",
)
SYSTEM_WEIGHT = {
    "Geradores": 35,
    "Shore-Power-AC": 32,
    "Energia-DC": 30,
    "Climatizacao": 28,
    "Bombas-Utilidades": 24,
    "Corrosao-Seguranca": 24,
    "Propulsao-Motores": 22,
    "Navegacao": 20,
    "Iluminacao-Acessorios": 18,
    "Campo-Clientes": 12,
    "Materiais-Internos": 10,
}
DOCUMENT_KIND_WEIGHT = {
    "service-manual": 35,
    "installation-manual": 32,
    "troubleshooting-guide": 30,
    "operation-manual": 24,
    "technical-reference": 18,
    "parts-manual": 16,
    "catalog-brochure": 8,
    "documento-tecnico": 14,
}
PRIORITY_WEIGHT = {"alta": 35, "media": 20, "baixa": 8, "nao": 0}


@dataclass(slots=True)
class Candidate:
    score: int
    reasons: list[str]
    pdf: dict[str, Any]
    note_path: Path
    frontmatter: dict[str, Any]


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8-sig"))


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def strip_accents(value: str) -> str:
    table = str.maketrans(
        "áàãâäéèêëíìîïóòõôöúùûüçÁÀÃÂÄÉÈÊËÍÌÎÏÓÒÕÔÖÚÙÛÜÇ",
        "aaaaaeeeeiiiiooooouuuucAAAAAEEEEIIIIOOOOOUUUUC",
    )
    return value.translate(table)


def normalized_blob(*parts: object) -> str:
    return strip_accents(" ".join(str(part or "") for part in parts)).lower()


def note_path_for_pdf(pdf: dict[str, Any]) -> Path | None:
    acervo_relative = str(pdf.get("acervo_relative_path") or "")
    if not acervo_relative or not acervo_relative.lower().endswith(".pdf"):
        return None
    return ACERVO_NOTAS_ROOT / Path(acervo_relative).with_suffix(".md")


def read_note(path: Path) -> tuple[str, dict[str, Any], str]:
    text = path.read_text(encoding="utf-8-sig")
    frontmatter_raw, body = extract_frontmatter(text)
    return text, parse_frontmatter(frontmatter_raw), body


def score_pdf(pdf: dict[str, Any], frontmatter: dict[str, Any]) -> tuple[int, list[str]]:
    reasons: list[str] = []
    system = str(frontmatter.get("acervo_system") or pdf.get("acervo_relative_path", "").split("/", 1)[0])
    kind = str(frontmatter.get("document_kind") or "")
    priority = str(frontmatter.get("curation_priority") or "baixa")
    ocr_priority = str(pdf.get("ocr_priority") or "nao")
    qpdf_status = str(pdf.get("qpdf_status") or "")
    text_extractable = str(pdf.get("text_extractable") or "")
    pages = int(pdf.get("pages") or 0)

    score = 0
    score += SYSTEM_WEIGHT.get(system, 8)
    if system in SYSTEM_WEIGHT:
        reasons.append(f"sistema {system}")
    score += DOCUMENT_KIND_WEIGHT.get(kind, 10)
    if kind:
        reasons.append(f"tipo {kind}")
    score += PRIORITY_WEIGHT.get(priority, 0)
    if priority == "alta":
        reasons.append("prioridade editorial alta")
    if ocr_priority in {"alta", "media"}:
        score += 22 if ocr_priority == "alta" else 12
        reasons.append(f"OCR {ocr_priority}")
    if text_extractable == "nao":
        score += 25
        reasons.append("sem texto pesquisavel direto")
    if qpdf_status == "warning":
        score += 6
        reasons.append("qpdf com warning")
    if pages >= 100:
        score += 6
        reasons.append(f"documento longo ({pages} paginas)")
    if bool(pdf.get("encrypted")):
        score += 5
        reasons.append("PDF criptografado")

    return score, reasons[:6]


def is_placeholder_block(block: str) -> bool:
    lower = normalized_blob(block)
    return "pendente" in lower and "curadoria assistida por automacao" not in lower


def replace_frontmatter_field(text: str, key: str, value: str) -> str:
    pattern = re.compile(rf"^{re.escape(key)}: .*$", re.M)
    line = f'{key}: "{value}"'
    if pattern.search(text):
        return pattern.sub(line, text, count=1)
    return text.replace("\nreviewed_on:", f"\n{line}\nreviewed_on:", 1)


def application_line(system: str, kind: str) -> str:
    if system == "Geradores":
        return "priorizar ligacoes, protecoes, ventilacao, alarmes, partida/parada e rotina de manutencao do grupo gerador."
    if system == "Shore-Power-AC":
        return "priorizar entrada de cais, polaridade, DR, aterramento, isolamento, chaveamento e compatibilidade com pratica brasileira."
    if system == "Energia-DC":
        return "priorizar bateria, alternador, carregador, bitola, queda de tensao, fusivel e seccionamento."
    if system == "Climatizacao":
        return "priorizar agua de mar, bomba, fluxo, dreno, alimentacao, controle e acesso de manutencao."
    if system == "Bombas-Utilidades":
        return "priorizar corrente, fusivel, pressostato, valvulas, altura manometrica, acesso e falhas recorrentes."
    if system == "Navegacao":
        return "priorizar alimentacao, rede, protocolos, fusivel, aterramento funcional e compatibilidade entre equipamentos."
    if system == "Corrosao-Seguranca":
        return "priorizar medicao, bonding, anodos, corrente galvanica, mitigacao e limites de aplicacao da fonte."
    if system == "Propulsao-Motores":
        return "priorizar interfaces eletricas, comandos, sensores, alarmes, alternadores e separacao entre conteudo mecanico e eletrico."
    if kind == "catalog-brochure":
        return "usar como indice de modelos e especificacoes comerciais, nao como manual tecnico final."
    return "priorizar identificacao de modelos, requisitos de instalacao, protecoes, manutencao e pontos de falha uteis para oficina."


def build_assisted_block(candidate: Candidate) -> str:
    pdf = candidate.pdf
    fm = candidate.frontmatter
    system = str(fm.get("acervo_system") or "A revisar")
    brand = str(fm.get("acervo_brand") or "A revisar")
    family = str(fm.get("acervo_family") or "A revisar")
    kind = str(fm.get("document_kind") or "documento-tecnico")
    priority = str(fm.get("curation_priority") or "media")
    pages = str(pdf.get("pages") or fm.get("pdf_pages") or "n/a")
    qpdf = str(pdf.get("qpdf_status") or fm.get("qpdf_status") or "n/a")
    text_status = str(pdf.get("text_extractable") or fm.get("text_extractable") or "n/a")
    text_method = str(pdf.get("text_method") or fm.get("extraction_method") or "n/a")
    ocr_priority = str(pdf.get("ocr_priority") or fm.get("ocr_priority") or "nao")
    encrypted = "sim" if bool(pdf.get("encrypted")) else "nao"
    reasons = "; ".join(candidate.reasons) if candidate.reasons else "prioridade operacional"

    caution_lines = [
        f"texto pesquisavel: `{text_status}` por `{text_method}`",
        f"status qpdf: `{qpdf}`",
        f"prioridade OCR: `{ocr_priority}`",
        f"PDF criptografado: `{encrypted}`",
    ]
    if qpdf == "warning":
        caution_lines.append("validar paginas e integridade antes de extrair tabela critica.")
    if text_status == "nao":
        caution_lines.append("usar OCR auxiliar e revisar visualmente trechos tecnicos.")
    if kind in {"installation-manual", "service-manual", "troubleshooting-guide"}:
        caution_lines.append("boa candidata para virar checklist de oficina ou aula tecnica.")

    caution_bullets = "\n".join(f"- {line}" for line in caution_lines)
    next_steps = [
        "confirmar modelos/revisoes diretamente no PDF",
        "marcar paginas-chave para instalacao, diagnostico, protecao e manutencao",
        "separar recomendacao de fabricante de exigencia normativa",
        "adicionar links internos para notas de sistema da vault",
    ]
    next_step_bullets = "\n".join(f"- {line}" for line in next_steps)

    return "\n".join(
        [
            "<!-- CURADORIA-HUMANA:START -->",
            "## Curadoria assistida por automacao",
            "",
            "> [!warning] Status",
            "> Este bloco foi preenchido automaticamente para acelerar busca e priorizacao. Nao substitui revisao tecnica humana antes de aula, atendimento, orcamento ou publicacao.",
            "",
            "### Resumo operacional",
            f"- documento `{kind}` em `{system}` para `{brand} / {family}`.",
            f"- prioridade atual: `{priority}`; score operacional: `{candidate.score}`.",
            f"- razoes de prioridade: {reasons}.",
            f"- paginas detectadas: `{pages}`.",
            "",
            "### Aplicacao de oficina",
            f"- {application_line(system, kind)}",
            "",
            "### Modelos cobertos provaveis",
            f"- `{family}`",
            "- confirmar modelos, revisoes e excecoes no PDF antes de uso publico.",
            "",
            "### Pontos de atencao",
            caution_bullets,
            "",
            "### Integracoes e links internos",
            f"- sistema-base: `{system}`",
            f"- marca/familia: `{brand} / {family}`",
            "- conectar com nota tecnica do sistema quando este PDF virar material de ensino.",
            "",
            "### Proximo passo humano",
            next_step_bullets,
            "",
            "### Status de curadoria",
            f"- tipo documental confirmado automaticamente: `{kind}`",
            "- curadoria humana: pendente",
            "- pronto para ensino/SEO: nao",
            "<!-- CURADORIA-HUMANA:END -->",
        ]
    )


def enrich_notes(candidates: list[Candidate], limit: int) -> list[dict[str, Any]]:
    enriched: list[dict[str, Any]] = []
    for candidate in candidates[:limit]:
        text, frontmatter, _body = read_note(candidate.note_path)
        stage = str(frontmatter.get("curation_stage") or "")
        if stage and stage != "triagem-automatica":
            continue
        match = CURATION_BLOCK_RE.search(text)
        if not match or not is_placeholder_block(match.group(0)):
            continue

        updated = replace_frontmatter_field(text, "curation_stage", "curadoria-assistida-automatica")
        updated = replace_frontmatter_field(updated, "curation_priority", str(frontmatter.get("curation_priority") or "alta"))
        updated = CURATION_BLOCK_RE.sub(build_assisted_block(candidate), updated, count=1)
        candidate.note_path.write_text(updated, encoding="utf-8", newline="\n")
        enriched.append(
            {
                "note": rel(candidate.note_path),
                "source_pdf": candidate.pdf.get("relative_path"),
                "score": candidate.score,
                "reasons": candidate.reasons,
            }
        )
    return enriched


def classify_human_separation(pdfs: list[dict[str, Any]]) -> dict[str, Any]:
    by_collection = Counter(str(pdf.get("collection") or "desconhecido") for pdf in pdfs)
    technical_total = by_collection.get("acervo-principal", 0) + by_collection.get("humano-staging-tecnico", 0)
    non_technical_total = by_collection.get("humano-fora-do-escopo", 0)
    archived_total = by_collection.get("humano-arquivado-duplicata", 0)

    suspected_technical: list[dict[str, str]] = []
    suspected_personal: list[dict[str, str]] = []
    for pdf in pdfs:
        collection = str(pdf.get("collection") or "")
        blob = normalized_blob(pdf.get("file_name"))
        signal_hits = [signal for signal in TECHNICAL_SIGNALS if signal in blob]
        personal_hits = [signal for signal in PERSONAL_SIGNALS if signal in blob]
        if collection == "humano-fora-do-escopo" and signal_hits:
            suspected_technical.append(
                {
                    "path": str(pdf.get("relative_path")),
                    "signals": ", ".join(signal_hits[:5]),
                }
            )
        if collection == "humano-staging-tecnico" and personal_hits:
            suspected_personal.append(
                {
                    "path": str(pdf.get("relative_path")),
                    "signals": ", ".join(personal_hits[:5]),
                }
            )

    return {
        "collection_counts": dict(sorted(by_collection.items())),
        "technical_total": technical_total,
        "non_technical_or_personal_total": non_technical_total,
        "archived_duplicate_total": archived_total,
        "suspected_technical_in_out_of_scope": suspected_technical[:40],
        "suspected_personal_in_technical_staging": suspected_personal[:40],
    }


def build_candidates(pdfs: list[dict[str, Any]]) -> list[Candidate]:
    candidates: list[Candidate] = []
    for pdf in pdfs:
        if pdf.get("collection") != "acervo-principal":
            continue
        note_path = note_path_for_pdf(pdf)
        if not note_path or not note_path.exists():
            continue
        _text, frontmatter, _body = read_note(note_path)
        score, reasons = score_pdf(pdf, frontmatter)
        candidates.append(Candidate(score, reasons, pdf, note_path, frontmatter))
    return sorted(candidates, key=lambda item: (-item.score, rel(item.note_path)))


def count_companion_notes() -> dict[str, int]:
    notes = [
        path
        for path in ACERVO_NOTAS_ROOT.rglob("*.md")
        if path.name.lower() != "readme.md"
    ]
    by_stage = Counter()
    by_priority = Counter()
    for path in notes:
        try:
            _text, frontmatter, _body = read_note(path)
        except UnicodeDecodeError:
            continue
        by_stage[str(frontmatter.get("curation_stage") or "sem-stage")] += 1
        by_priority[str(frontmatter.get("curation_priority") or "sem-prioridade")] += 1
    return {
        "total": len(notes),
        "by_stage": dict(sorted(by_stage.items())),
        "by_priority": dict(sorted(by_priority.items())),
    }


def render_table(rows: list[list[str]]) -> list[str]:
    if not rows:
        return ["_Sem itens._"]
    widths = [max(len(row[index]) for row in rows) for index in range(len(rows[0]))]
    output = []
    header = rows[0]
    output.append("| " + " | ".join(value.ljust(widths[index]) for index, value in enumerate(header)) + " |")
    output.append("| " + " | ".join("-" * widths[index] for index in range(len(header))) + " |")
    for row in rows[1:]:
        output.append("| " + " | ".join(value.ljust(widths[index]) for index, value in enumerate(row)) + " |")
    return output


def render_note(payload: dict[str, Any]) -> str:
    audit = payload["audit"]
    summary = audit["summary"]
    separation = payload["human_separation"]
    companion = payload["companion_notes"]
    ocr = payload["ocr"]
    pipeline = payload["pipeline"]
    candidates = payload["top_curation_targets"]
    enriched = payload["enriched_notes"]
    reviewed_on = date.today().isoformat()

    collection_rows = [["Bucket", "PDFs"]]
    for key, value in separation["collection_counts"].items():
        collection_rows.append([key, str(value)])

    ocr_rows = [["Status", "Arquivos"]]
    for key, value in ocr["status_counts"].items():
        ocr_rows.append([key, str(value)])

    target_rows = [["Score", "Nota", "PDF", "Motivo"]]
    for item in candidates[:30]:
        note = item["note"]
        pdf = item["source_pdf"]
        target_rows.append(
            [
                str(item["score"]),
                f"[[{note[:-3]}|nota]]",
                Path(pdf).name,
                "; ".join(item["reasons"][:3]),
            ]
        )

    suspect_rows = [["Caminho", "Sinais"]]
    for item in separation["suspected_technical_in_out_of_scope"][:20]:
        suspect_rows.append([item["path"], item["signals"]])

    lines = [
        "---",
        'title: "Painel de Curadoria do Acervo"',
        'note_type: "dashboard"',
        'domain: "90_Revisao_Manual"',
        'status: "auto-generated"',
        f'reviewed_on: "{reviewed_on}"',
        'review_jurisdiction: "Brasil"',
        "related_notes:",
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Local - Indice Gerado"',
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado"',
        '  - "Auditoria Operacional PDF - Toolchain"',
        '  - "OCR Controlado - Acervo Principal"',
        "---",
        "",
        "# Painel de Curadoria do Acervo",
        "",
        "> [!abstract] Resumo tecnico",
        "> Painel gerado automaticamente para separar acervo principal, staging tecnico, fora de escopo, OCR pendente e fila de curadoria das notas companheiras.",
        "",
        "## Saude operacional",
        "",
        f"- pipeline: `{pipeline.get('status', 'desconhecido')}`",
        f"- ultima execucao: `{pipeline.get('finished_at', 'n/a')}`",
        f"- PDFs auditados: `{summary.get('total_pdfs', 0)}`",
        f"- tamanho auditado: `{summary.get('total_size_label', 'n/a')}`",
        f"- paginas conhecidas: `{summary.get('known_pages', 0)}`",
        f"- qpdf ok/warning: `{summary.get('qpdf_status', {}).get('ok', 0)}` / `{summary.get('qpdf_status', {}).get('warning', 0)}`",
        f"- texto pesquisavel sim/nao: `{summary.get('text_status', {}).get('sim', 0)}` / `{summary.get('text_status', {}).get('nao', 0)}`",
        f"- notas companheiras: `{companion['total']}`",
        f"- notas com curadoria assistida: `{companion['by_stage'].get('curadoria-assistida-automatica', 0)}`",
        f"- notas enriquecidas nesta rodada: `{len(enriched)}`",
        "",
        "## Separacao humano vs tecnico",
        "",
        f"- tecnico operacional: `{separation['technical_total']}` PDFs (`acervo-principal` + `humano-staging-tecnico`).",
        f"- fora de escopo/pessoal: `{separation['non_technical_or_personal_total']}` PDFs.",
        f"- duplicatas arquivadas: `{separation['archived_duplicate_total']}` PDFs.",
        "",
        *render_table(collection_rows),
        "",
        "## OCR",
        "",
        f"- OCR executado nesta base: `{ocr['total_results']}` registros.",
        f"- OCR pendente por auditoria: `{ocr['pending_from_audit']}` PDFs (`alta`, `media` ou `baixa`).",
        "",
        *render_table(ocr_rows),
        "",
        "## Fila de curadoria tecnica",
        "",
        "Prioridade calculada por sistema, tipo documental, OCR, texto pesquisavel, paginas, `qpdf` e prioridade editorial.",
        "",
        *render_table(target_rows),
        "",
        "## Possiveis tecnicos no fora de escopo",
        "",
        "Fila conservadora: nao move arquivo automaticamente, apenas aponta nomes com sinais tecnicos para revisao humana.",
        "",
        *render_table(suspect_rows),
        "",
        "## Rotina para PDF novo",
        "",
        "```powershell",
        "python scripts/acervo/run_pdf_pipeline.py",
        "```",
        "",
        "A pipeline atualiza auditoria, OCR prioritario, notas companheiras, este painel, validacao e manifesto.",
        "",
    ]
    return "\n".join(lines)


def build_payload(enrich_limit: int, no_enrich: bool) -> dict[str, Any]:
    audit = load_json(AUDIT_PATH, {"summary": {}, "pdfs": []})
    ocr_results = load_json(OCR_RESULTS_PATH, {"results": []})
    non_pdf = load_json(NON_PDF_MANIFEST_PATH, {})
    pipeline = load_json(PIPELINE_MANIFEST_PATH, {})
    pdfs = audit.get("pdfs", [])
    if not isinstance(pdfs, list):
        pdfs = []

    separation = classify_human_separation(pdfs)
    candidates = build_candidates(pdfs)
    enriched = [] if no_enrich else enrich_notes(candidates, enrich_limit)

    ocr_status_counts = Counter(str(item.get("status") or "desconhecido") for item in ocr_results.get("results", []))
    pending_from_audit = sum(
        1
        for pdf in pdfs
        if str(pdf.get("ocr_priority") or "nao") in {"alta", "media", "baixa"}
    )

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "audit": {
            "path": rel(AUDIT_PATH),
            "summary": audit.get("summary", {}),
        },
        "pipeline": {
            "path": rel(PIPELINE_MANIFEST_PATH),
            "status": pipeline.get("status"),
            "finished_at": pipeline.get("finished_at"),
            "duration_seconds": pipeline.get("duration_seconds"),
        },
        "human_separation": separation,
        "non_pdf_support": {
            "path": rel(NON_PDF_MANIFEST_PATH),
            "non_pdf_count": non_pdf.get("non_pdf_count", 0),
            "extension_counts": non_pdf.get("extension_counts", {}),
            "extractable_counts": non_pdf.get("extractable_counts", {}),
        },
        "ocr": {
            "path": rel(OCR_RESULTS_PATH),
            "total_results": len(ocr_results.get("results", [])),
            "status_counts": dict(sorted(ocr_status_counts.items())),
            "pending_from_audit": pending_from_audit,
        },
        "companion_notes": count_companion_notes(),
        "top_curation_targets": [
            {
                "score": candidate.score,
                "note": rel(candidate.note_path),
                "source_pdf": str(candidate.pdf.get("relative_path")),
                "collection": str(candidate.pdf.get("collection")),
                "system": str(candidate.frontmatter.get("acervo_system") or ""),
                "brand": str(candidate.frontmatter.get("acervo_brand") or ""),
                "family": str(candidate.frontmatter.get("acervo_family") or ""),
                "document_kind": str(candidate.frontmatter.get("document_kind") or ""),
                "curation_stage": str(candidate.frontmatter.get("curation_stage") or ""),
                "curation_priority": str(candidate.frontmatter.get("curation_priority") or ""),
                "reasons": candidate.reasons,
            }
            for candidate in candidates[:100]
        ],
        "enriched_notes": enriched,
    }
    return payload


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Gera painel de curadoria, separacao humano/tecnico e enriquecimento automatico de notas prioritarias."
    )
    parser.add_argument("--enrich-limit", type=int, default=24)
    parser.add_argument("--no-enrich", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    payload = build_payload(args.enrich_limit, args.no_enrich)
    write_json(OUTPUT_JSON_PATH, payload)
    OUTPUT_NOTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_NOTE_PATH.write_text(render_note(payload), encoding="utf-8", newline="\n")

    print(f"Painel gerado: {rel(OUTPUT_NOTE_PATH)}")
    print(f"Manifesto gerado: {rel(OUTPUT_JSON_PATH)}")
    print(f"Notas enriquecidas: {len(payload['enriched_notes'])}")
    print(f"Alvos priorizados: {len(payload['top_curation_targets'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
