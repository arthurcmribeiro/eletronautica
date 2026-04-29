from __future__ import annotations

import hashlib
import json
import re
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

from vault_tools import ROOT  # noqa: E402
from pdf_text_tools import extract_pdf_text  # noqa: E402


ACERVO_LOCAL_ROOT = ROOT / "90_Revisao_Manual" / "_Acervo_Local"
ACERVO_NOTAS_ROOT = ROOT / "90_Revisao_Manual" / "_Acervo_Notas"
INDEX_NOTE_PATH = (
    ROOT
    / "90_Revisao_Manual"
    / "10_Indices_e_Paineis"
    / "Acervo Notas - Indice Gerado.md"
)
PDF_TOOLCHAIN_AUDIT_PATH = ROOT / "manifest" / "acervo-pdf-toolchain-audit.json"
OCR_RESULTS_PATH = ROOT / "90_Revisao_Manual" / "_Dados_Acervo" / "ocr-results.json"
MAX_ANALYSIS_PAGES = 12
EXTRACTION_TIMEOUT_SECONDS = 45

CURATION_BLOCK_RE = re.compile(
    r"<!-- CURADORIA-HUMANA:START -->.*?<!-- CURADORIA-HUMANA:END -->",
    re.S,
)
FRONTMATTER_RE = re.compile(r"(?s)^---\n(.*?)\n---\n?(.*)$")
FRONTMATTER_FIELD_RE = re.compile(r'^([A-Za-z0-9_]+): "(.*)"$', re.M)

SYSTEM_ORDER = [
    "Campo-Clientes",
    "Climatizacao",
    "Complementar-Brasil",
    "Energia-DC",
    "Geradores",
    "Shore-Power-AC",
    "Navegacao",
    "Bombas-Utilidades",
    "Iluminacao-Acessorios",
    "Corrosao-Seguranca",
    "Propulsao-Motores",
    "Materiais-Internos",
    "HTML-Tecnico-Exportado",
]
DOCUMENT_KIND_ORDER = [
    "catalog-brochure",
    "documento-tecnico",
    "installation-manual",
    "operation-manual",
    "parts-manual",
    "service-manual",
    "technical-reference",
    "troubleshooting-guide",
]

SYSTEM_CONTEXT_LINKS = {
    "Campo-Clientes": "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Indice Gerado",
    "Climatizacao": "70_Hidraulica_Climatizacao_e_Utilidades",
    "Energia-DC": "30_Sistemas_DC_Baterias_e_Carga",
    "Geradores": "90_Revisao_Manual/90_Arquivo_Historico/Acervo Local - Geradores Iniciais (Cummins Onan)",
    "Shore-Power-AC": "40_Sistemas_AC_Shore_Power_e_Inversores",
    "Navegacao": "50_Navegacao_Instrumentacao_e_Comunicacao",
    "Bombas-Utilidades": "70_Hidraulica_Climatizacao_e_Utilidades",
    "Iluminacao-Acessorios": "60_Iluminacao_Sinalizacao_e_Acessorios",
    "Corrosao-Seguranca": "80_Corrosao_Bonding_e_Seguranca",
    "Propulsao-Motores": "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Indice Gerado",
    "Materiais-Internos": "90_Revisao_Manual/00_Entrada_e_Controle/Portal do Acervo - Biblioteca de Referencia",
}

SYSTEM_APPLICATIONS = {
    "Campo-Clientes": [
        "usar esta nota para rastrear evidencia de campo, fotos convertidas, documentos recebidos e contexto de cliente sem misturar com manual de fabricante",
    ],
    "Climatizacao": [
        "usar esta nota para achar sem abrir o PDF os blocos de instalacao, fluxo de agua, distribuicao de ar e controles",
    ],
    "Complementar-Brasil": [
        "revisar se este documento merece curadoria humana ou se deve ficar apenas como trilha de apoio ao PDF",
    ],
    "Energia-DC": [
        "usar esta nota para localizar topologias de bateria, carregamento, distribuicao DC, protecoes e pontos de auditoria de campo",
    ],
    "Geradores": [
        "usar esta nota para localizar rapidamente procedimentos, identificacao de modelo e pontos de manutencao do grupo gerador",
        "prioridade alta para campo: documentar ligacoes, bitolas, protecoes, ventilacao, posicionamento e checklist de montagem",
    ],
    "Shore-Power-AC": [
        "usar esta nota para rastrear entrada de cais, aterramento, protecoes AC, isolamento, conexoes e compatibilidade com instalacoes brasileiras",
    ],
    "Navegacao": [
        "usar esta nota para rastrear interfaces, protocolos, instalacao fisica e ajustes iniciais de eletronicos",
    ],
    "Bombas-Utilidades": [
        "usar esta nota para achar rapidamente bombas, valvulas, pressostatos, sanitarios, utilidades e requisitos de instalacao/manutencao",
    ],
    "Iluminacao-Acessorios": [
        "usar esta nota para localizar requisitos eletricos de iluminacao, sinalizacao, controles e acessorios de bordo",
    ],
    "Corrosao-Seguranca": [
        "usar esta nota para apoiar analise de bonding, corrosao galvanica, seguranca eletrica e mitigacoes aplicaveis em campo",
    ],
    "Propulsao-Motores": [
        "usar esta nota para separar material eletrico/eletronico de motores, atuadores, controles, estabilizacao e propulsao do acervo de geradores",
    ],
    "Materiais-Internos": [
        "usar esta nota como apoio para curso, aula, procedimento interno ou referencia de oficina antes de publicar como conteudo final",
    ],
    "HTML-Tecnico-Exportado": [
        "usar esta nota apenas quando o conteudo HTML tiver sido normalizado para fonte arquivavel; conferir origem antes de tratar como referencia primaria",
    ],
}

SYSTEM_QUESTIONS = {
    "Campo-Clientes": [
        "este documento e evidencia de campo, material de cliente ou referencia tecnica reutilizavel?",
        "ha dados pessoais, comerciais ou sensiveis que exigem restricao antes de reaproveitar em aula ou SEO?",
    ],
    "Climatizacao": [
        "quais modelos e revisoes este PDF cobre de verdade, e quais ficaram de fora?",
        "quais paginas merecem virar nota humana curada ou material de aula?",
    ],
    "Complementar-Brasil": [
        "quais modelos e revisoes este PDF cobre de verdade, e quais ficaram de fora?",
        "quais paginas merecem virar nota humana curada ou material de aula?",
    ],
    "Energia-DC": [
        "quais tensoes, correntes, protecoes, bitolas e limites termicos precisam ser destacados para uso de oficina?",
        "ha diferenca relevante entre recomendacao de fabricante, ABYC/ISO e pratica comum no Brasil?",
    ],
    "Geradores": [
        "quais modelos e revisoes este PDF cobre de verdade, e quais ficaram de fora?",
        "quais paginas merecem virar nota humana curada ou material de aula?",
        "quais requisitos de montagem, bitola, protecao e ambiente precisam ser destacados no resumo humano?",
    ],
    "Shore-Power-AC": [
        "quais requisitos de aterramento, polaridade, protecao diferencial, isolamento e entrada de cais aparecem neste documento?",
        "o material precisa de nota Brasil-primeiro para evitar aplicacao direta de padrao estrangeiro sem adaptacao?",
    ],
    "Navegacao": [
        "quais modelos e revisoes este PDF cobre de verdade, e quais ficaram de fora?",
        "quais paginas merecem virar nota humana curada ou material de aula?",
        "quais protocolos, interfaces e compatibilidades valem link interno dedicado?",
    ],
    "Bombas-Utilidades": [
        "quais parametros de instalacao, manutencao, corrente, fusivel e acesso fisico merecem resumo de oficina?",
        "o documento tem tabela de falhas ou pecas que deveria virar nota de consulta rapida?",
    ],
    "Iluminacao-Acessorios": [
        "quais requisitos de corrente, protecao, IP, cabos e compatibilidade precisam ir para checklist de instalacao?",
        "o material e manual de produto, catalogo comercial ou referencia tecnica reutilizavel?",
    ],
    "Corrosao-Seguranca": [
        "quais medicoes, limites, riscos e mitigacoes sao aplicaveis a embarcacoes no Brasil?",
        "ha risco de transformar analogia didatica em afirmacao fisica incorreta?",
    ],
    "Propulsao-Motores": [
        "o documento cobre eletrica/eletronica de propulsao ou e predominantemente mecanico?",
        "quais interfaces com baterias, alternadores, comandos, sensores e alarmes merecem link interno?",
    ],
    "Materiais-Internos": [
        "este material pode virar aula, procedimento de oficina ou apenas referencia interna?",
        "ha trechos que exigem reescrita autoral antes de uso publico?",
    ],
    "HTML-Tecnico-Exportado": [
        "a origem do HTML e confiavel e rastreavel?",
        "vale converter para PDF arquivado, transformar em nota tecnica ou descartar como captura fraca?",
    ],
}

COMMON_ACTIONS = [
    "revisar a classificacao desta nota e completar contexto tecnico se necessario",
    "vincular esta nota aos PDFs principais da mesma familia quando houver",
]
GENERATOR_ACTIONS = [
    "destacar ligacoes, torque, bitolas, protecoes e condicoes de montagem",
    "conferir se existe manual operacional complementar na mesma familia",
]

BRAND_SIGNAL_MAP = {
    "BEP Marine": ("bep", "bep marine"),
    "Blue Sea Systems": ("blue sea", "bluesea"),
    "Cummins / Onan": ("cummins", "onan"),
    "Dometic": ("dometic", "cruisair", "marine air"),
    "Fischer Panda": ("fischer panda", "panda"),
    "Furuno": ("furuno",),
    "Garmin": ("garmin",),
    "H-Tec": ("h-tec", "hfc-acqua"),
    "Intellian": ("intellian",),
    "Jabsco": ("jabsco",),
    "Johnson Pump": ("johnson pump",),
    "Lumishore": ("lumishore",),
    "Mabru": ("mabru",),
    "Marinco": ("marinco",),
    "Mastervolt": ("mastervolt",),
    "Northern Lights": ("northern lights",),
    "Quick": ("quick",),
    "Raymarine": ("raymarine", "seatalk", "smartpilot", "quantum"),
    "Rehlko / Kohler": ("rehlko", "kohler"),
    "Scania": ("scania",),
    "Seakeeper": ("seakeeper",),
    "Sterling Power": ("sterling", "sterling power"),
    "Standard Horizon": ("standard horizon",),
    "Ultraflex": ("ultraflex",),
    "Usina": ("usina",),
    "Vetus": ("vetus",),
    "Victron": ("victron", "multiplus", "phoenix"),
    "Volvo Penta": ("volvo penta",),
    "Whale": ("whale",),
    "Yanmar": ("yanmar",),
    "Zipwake": ("zipwake",),
}

TERM_KEYWORDS = (
    "12v",
    "air",
    "alternator",
    "battery",
    "bonding",
    "control",
    "controls",
    "cooling",
    "corrosion",
    "diagnostic",
    "engine",
    "generator",
    "hvac",
    "installation",
    "manual",
    "network",
    "nmea",
    "parts",
    "pump",
    "radar",
    "service",
    "spec",
    "troubleshooting",
    "voltage",
    "wiring",
)
DOCUMENT_KIND_LABELS = {
    "catalog-brochure": "Catalogo / brochure",
    "documento-tecnico": "Documento tecnico",
    "installation-manual": "Manual de instalacao",
    "operation-manual": "Manual de operacao",
    "parts-manual": "Manual de pecas",
    "service-manual": "Manual de servico",
    "technical-reference": "Referencia tecnica",
    "troubleshooting-guide": "Guia de diagnostico",
}
NOISE_LINE_PATTERNS = (
    re.compile(r"redistribution|publication of this document", re.I),
    re.compile(r"proposition\s+65|printed in u\.?s\.?a\.?", re.I),
    re.compile(r"copyright|all rights reserved", re.I),
    re.compile(r"this document contains mixed page sizes", re.I),
    re.compile(r"please adjust your printer settings", re.I),
    re.compile(r"^\s*(page|pagina)\s+\d+\s*$", re.I),
)
DOCUMENT_CODE_RE = re.compile(
    r"\b(?:"
    r"\d{3,4}-\d{4}[A-Z]?"
    r"|TP[-\s]?\d{4}[A-Z]?"
    r"|A\d{3,}[A-Z0-9]*"
    r"|[A-Z]{2,10}\d{4,}[A-Z0-9.-]*"
    r"|[A-Z]{2,6}-\d{4,6}[A-Z0-9.-]*"
    r")\b",
    re.I,
)
DATE_SIGNAL_RE = re.compile(
    r"\b(?:"
    r"\d{1,2}[/-]\d{1,2}[/-]\d{2,4}"
    r"|\d{4}[/-]\d{1,2}[/-]\d{1,2}"
    r"|(?:jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec|"
    r"janeiro|fevereiro|marco|março|abril|maio|junho|julho|agosto|"
    r"setembro|outubro|novembro|dezembro)[a-z]*\.?\s+\d{4}"
    r")\b",
    re.I,
)
TECHNICAL_UNIT_RE = re.compile(
    r"\b\d+(?:[.,]\d+)?\s*(?:"
    r"vdc|vac|v\s*dc|v\s*ac|volt(?:s)?|a|amp(?:s|ere|eres)?|hz|khz|kw|w|"
    r"awg|mm2|mm²|mcm|rpm|nm|n\s*m|psi|bar|gpm|lpm|l/min|"
    r"cubic\s*feet|cfm|btu|°c|deg\s*c|c\b|°f|deg\s*f"
    r")\b",
    re.I,
)
TECHNICAL_KEYWORD_RE = re.compile(
    r"\b(?:"
    r"battery|bateria|alternator|alternador|charger|carregador|breaker|disjuntor|"
    r"fuse|fusivel|fusível|wire|cable|cabo|conductor|condutor|ground|terra|"
    r"bonding|torque|current|corrente|voltage|tensao|tensão|frequency|frequencia|"
    r"pump|bomba|pressure|pressao|pressão|flow|fluxo|cooling|refrigeracao|"
    r"installation|instalacao|instalação|wiring|ligacao|ligação|alarm|alarme|"
    r"fault|falha|diagnostic|diagnostico|diagnóstico|maintenance|manutencao|manutenção"
    r")\b",
    re.I,
)
SECTION_KEYWORD_RE = re.compile(
    r"\b(?:"
    r"installation|instalacao|instalação|operation|operacao|operação|service|servico|serviço|"
    r"maintenance|manutencao|manutenção|troubleshooting|diagnostic|diagnostico|diagnóstico|"
    r"specification|specifications|especificacao|especificações|wiring|ligacao|ligação|"
    r"parts|pecas|peças|safety|seguranca|segurança|cooling|refrigeracao|"
    r"battery|bateria|generator|gerador|control|controle|network|nmea"
    r")\b",
    re.I,
)
TOPIC_KEYWORDS = (
    ("alimentacao eletrica", ("battery", "bateria", "voltage", "tensao", "tensão", "charger", "carregador")),
    ("protecao e seccionamento", ("fuse", "fusivel", "fusível", "breaker", "disjuntor", "switch", "seccion")),
    ("cabos e ligacoes", ("wire", "wiring", "cable", "cabo", "conductor", "ligacao", "ligação")),
    ("aterramento/bonding", ("ground", "terra", "bonding", "galvanic", "galvanica", "galvânica")),
    ("instalacao fisica", ("installation", "instalacao", "instalação", "mounting", "montagem")),
    ("operacao", ("operation", "operacao", "operação", "start", "stop", "partida")),
    ("manutencao", ("maintenance", "manutencao", "manutenção", "service", "servico", "serviço")),
    ("diagnostico de falhas", ("troubleshooting", "diagnostic", "diagnostico", "diagnóstico", "fault", "falha")),
    ("resfriamento/agua", ("cooling", "water", "agua", "água", "pump", "bomba", "flow", "fluxo")),
    ("redes e comunicacao", ("nmea", "can bus", "network", "seatalk", "interbus", "ethernet")),
)

MODEL_STOPWORDS = {
    "AC",
    "AND",
    "AIR",
    "BOAT",
    "BOARD",
    "BOATS",
    "BULLETIN",
    "CAMERA",
    "CATALOGO",
    "CATALOG",
    "CHARTPLOTTER",
    "CONDITIONER",
    "CONDITIONERS",
    "CONDITIONING",
    "CONNECTIONS",
    "CONTAINED",
    "CONTROL",
    "CONTROLS",
    "CORROSAO",
    "COURSES",
    "CURSOS",
    "COVER",
    "DATA",
    "DESIGN",
    "DIAGRAMA",
    "DIAGRAMAS",
    "DIRECT",
    "DOC",
    "DOCTORS",
    "DOCUMENT",
    "DOCUMENTATION",
    "EFFECTIVE",
    "ELECTRICAL",
    "ELETRICA",
    "ELETROLISE",
    "ENERGY",
    "EQUIPA",
    "ENGLISH",
    "ESPELHO",
    "ESQUEMATICO",
    "ESTUDO",
    "ESTUDOS",
    "EXPANSION",
    "FOR",
    "FROM",
    "FUNDAMENTOS",
    "FUSION",
    "GENERATOR",
    "GENERATORS",
    "GENSET",
    "GUIDE",
    "HANDLERS",
    "HIDRAULICO",
    "INSTALACAO",
    "INTERNOS",
    "INTRODUCTION",
    "INTERNATIONAL",
    "INSTALLATION",
    "INSTRUCTIONS",
    "ISSUE",
    "JANUARY",
    "LEGACY",
    "LIGACAO",
    "MANUAL",
    "MANUALS",
    "MARINE",
    "MARINAS",
    "MATERIAIS",
    "MECHANICSBURG",
    "MODEL",
    "MODELS",
    "MOTORES",
    "NAUTICA",
    "NETWORK",
    "OLATHE",
    "OPERATION",
    "OPERATOR",
    "ORIGINAL",
    "PARTS",
    "PERFORMANCE",
    "PDF",
    "PORTUGUES",
    "PRICE",
    "PRINTED",
    "PRODUCTS",
    "PROPULSAO",
    "PRACTICAL",
    "QUALITY",
    "RADAR",
    "RAPHAEL",
    "REFERENCE",
    "REMOTE",
    "RESIDUAL",
    "REV",
    "SERVICE",
    "SELF",
    "SERIES",
    "SETS",
    "SPEC",
    "SPECIFICATIONS",
    "STREET",
    "SUPPORT",
    "SYSTEM",
    "SYSTEMS",
    "TECHNICAL",
    "THE",
    "TEMPLATE",
    "TRANSDUCERS",
    "TROUBLESHOOTING",
    "TURBO",
    "TRUSTED",
    "VOLT",
    "WATER",
}

MODEL_BRAND_TOKENS = {
    re.sub(r"[^A-Z0-9]", "", signal.upper())
    for signals in BRAND_SIGNAL_MAP.values()
    for signal in signals
}
MODEL_BRAND_TOKENS |= {
    part
    for signals in BRAND_SIGNAL_MAP.values()
    for signal in signals
    for part in re.split(r"[^A-Za-z0-9]+", signal.upper())
    if len(part) >= 3
}


@dataclass(slots=True)
class ExistingNoteState:
    curation_block: str | None = None
    curation_priority: str | None = None
    curation_stage: str | None = None


@dataclass(slots=True)
class NoteRecord:
    pdf_path: Path
    note_path: Path
    relative_pdf: str
    relative_note: str
    system: str
    brand: str
    family: str
    title: str
    document_kind: str
    curation_priority: str
    curation_stage: str
    source_sha256: str
    extraction_method: str
    text_extractable: str
    size_label: str
    pdf_pages: str
    pdf_version: str
    pdf_encrypted: str
    qpdf_status: str
    ocr_priority: str
    ocr_reason: str
    ocr_status: str
    ocr_text_path: str
    ocr_note_path: str
    ocr_text_chars: str
    analysis_source: str
    metadata_title: str
    detected_brands: list[str]
    detected_models: list[str]
    detected_terms: list[str]
    document_codes: list[str]
    revision_signals: list[str]
    technical_specs: list[str]
    technical_sections: list[str]
    curation_topics: list[str]
    snippets: list[str]
    curation_block: str


def sha256(path: Path) -> str:
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


def normalize_whitespace(value: str) -> str:
    return " ".join(value.replace("\xa0", " ").split())


def strip_accents(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    return normalized.encode("ascii", "ignore").decode("ascii")


def display_label(value: str) -> str:
    cleaned = value.replace("__", " ").replace("_", " ").replace("-", " ")
    return normalize_whitespace(cleaned)


def title_from_stem(stem: str) -> str:
    return stem.replace("__", " - ").replace("_", " ").strip()


def is_noise_line(line: str) -> bool:
    compact = normalize_whitespace(line)
    if not compact:
        return True
    if len(compact) < 4:
        return True
    if any(pattern.search(compact) for pattern in NOISE_LINE_PATTERNS):
        return True
    alpha_count = sum(char.isalpha() for char in compact)
    return alpha_count < 3


def clean_signal_line(line: str, *, max_length: int = 180) -> str:
    compact = normalize_whitespace(line).replace("`", "'")
    if len(compact) <= max_length:
        return compact
    return compact[: max_length - 3].rstrip() + "..."


def push_unique(items: list[str], seen: set[str], value: str, *, limit: int) -> None:
    cleaned = clean_signal_line(value)
    if not cleaned or is_noise_line(cleaned):
        return
    key = cleaned.casefold()
    if key in seen:
        return
    seen.add(key)
    items.append(cleaned)
    del items[limit:]


def technical_line_score(line: str) -> int:
    compact = normalize_whitespace(line)
    if is_noise_line(compact):
        return -100

    score = 0
    if TECHNICAL_UNIT_RE.search(compact):
        score += 8
    if TECHNICAL_KEYWORD_RE.search(compact):
        score += 6
    if DOCUMENT_CODE_RE.search(compact):
        score += 3
    if re.search(r"\b(?:12|24|48|110|115|120|220|230|240|50|60)\b", compact):
        score += 2
    if 20 <= len(compact) <= 160:
        score += 2
    if len(compact) > 220:
        score -= 4
    return score


def extract_document_codes(*, stem: str, metadata_title: str, text: str) -> list[str]:
    candidates = "\n".join(
        part
        for part in (
            stem,
            stem.replace("-", " "),
            metadata_title if metadata_title != "n/a" else "",
            text,
        )
        if part
    )
    results: list[str] = []
    seen: set[str] = set()
    for match in DOCUMENT_CODE_RE.finditer(candidates):
        token = normalize_model_token(match.group(0)).upper()
        if len(token) < 4 or token in MODEL_STOPWORDS:
            continue
        if token.isdigit():
            continue
        key = token.casefold()
        if key in seen:
            continue
        seen.add(key)
        results.append(token)
        if len(results) >= 10:
            break
    return results


def extract_revision_signals(text: str) -> list[str]:
    results: list[str] = []
    seen: set[str] = set()
    for line in text.splitlines():
        compact = normalize_whitespace(line)
        if is_noise_line(compact):
            continue
        if not DATE_SIGNAL_RE.search(compact):
            continue
        if not re.search(r"rev|revision|revised|issue|printed|date|data|edicao|edição", compact, re.I):
            continue
        push_unique(results, seen, compact, limit=8)
        if len(results) >= 8:
            break
    return results


def extract_technical_specs(text: str) -> list[str]:
    scored: list[tuple[int, int, str]] = []
    seen: set[str] = set()
    for index, raw_line in enumerate(text.splitlines()):
        line = clean_signal_line(raw_line)
        if len(line) < 10:
            continue
        score = technical_line_score(line)
        if score < 8:
            continue
        key = line.casefold()
        if key in seen:
            continue
        seen.add(key)
        scored.append((score, -index, line))

    scored.sort(reverse=True)
    return [line for _score, _index, line in scored[:14]]


def extract_technical_sections(text: str) -> list[str]:
    results: list[str] = []
    seen: set[str] = set()
    for raw_line in text.splitlines():
        line = clean_signal_line(raw_line, max_length=110)
        if len(line) < 5 or len(line) > 110:
            continue
        if is_noise_line(line):
            continue
        if not SECTION_KEYWORD_RE.search(line):
            continue
        if TECHNICAL_UNIT_RE.search(line) and len(line.split()) > 8:
            continue
        if line.endswith(".") and len(line.split()) > 6:
            continue
        push_unique(results, seen, line, limit=14)
        if len(results) >= 14:
            break
    return results


def detect_curation_topics(text: str, system: str, document_kind: str) -> list[str]:
    blob = f"{system} {document_kind} {text}".casefold()
    topics: list[str] = []
    for label, keywords in TOPIC_KEYWORDS:
        if any(keyword.casefold() in blob for keyword in keywords):
            topics.append(label)
        if len(topics) >= 8:
            break
    return topics


def build_human_title(
    *,
    stem: str,
    brand: str,
    family: str,
    document_kind: str,
    document_codes: list[str],
    detected_models: list[str],
    metadata_title: str,
) -> str:
    kind_label = DOCUMENT_KIND_LABELS.get(document_kind, "Documento tecnico")
    brand_label = display_label(brand)
    family_label = display_label(family)
    model_label = ", ".join(detected_models[:4]) if detected_models else family_label
    code = ""
    if document_kind != "catalog-brochure":
        code = next(
            (
                candidate
                for candidate in document_codes
                if candidate.casefold() not in {model.casefold() for model in detected_models}
            ),
            "",
        )

    if brand.casefold().startswith("referencia-"):
        base = f"{family_label} - {kind_label}"
    elif model_label and model_label.casefold() != family_label.casefold():
        base = f"{brand_label} {model_label} - {kind_label}"
    else:
        base = f"{brand_label} {family_label} - {kind_label}"

    if code and code.casefold() not in base.casefold():
        base = f"{base} - {code}"
    elif metadata_title and metadata_title != "n/a" and metadata_title.casefold() not in base.casefold():
        short_metadata = clean_signal_line(metadata_title, max_length=48)
        if short_metadata and not is_noise_line(short_metadata):
            base = f"{base} - {short_metadata}"

    fallback = title_from_stem(stem)
    return normalize_whitespace(base) or fallback


def absolute_link(path: Path) -> str:
    return path.resolve().as_posix()


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
    )


def detect_document_kind(stem: str) -> str:
    lowered = stem.lower()
    if "service-manual" in lowered:
        return "service-manual"
    if "parts-manual" in lowered:
        return "parts-manual"
    if "installation-manual" in lowered or "supplemental-instructions" in lowered:
        return "installation-manual"
    if "operator-manual" in lowered or "operation-manual" in lowered:
        return "operation-manual"
    if "technical-specifications" in lowered:
        return "operation-manual"
    if "troubleshooting-guide" in lowered:
        return "troubleshooting-guide"
    if (
        "price-list" in lowered
        or "catalogo-brochure" in lowered
        or "referencia-comercial" in lowered
    ):
        return "catalog-brochure"
    if "display-cutout-template" in lowered or "cabling-and-connections" in lowered:
        return "documento-tecnico"
    return "technical-reference"


def detect_curation_priority(stem: str, existing: ExistingNoteState) -> str:
    if existing.curation_priority:
        return existing.curation_priority

    lowered = stem.lower()
    if lowered.startswith("referencia-comercial__") or "catalogo-pecas" in lowered:
        return "baixa"
    return "alta"


def detect_curation_stage(existing: ExistingNoteState) -> str:
    if existing.curation_stage:
        return existing.curation_stage
    return "triagem-automatica"


def detect_brand_signals(text: str) -> list[str]:
    lowered = text.lower()
    results: list[str] = []
    for label, signals in BRAND_SIGNAL_MAP.items():
        if any(signal in lowered for signal in signals):
            results.append(label)
    return results


def compact_model_key(value: str) -> str:
    return re.sub(r"[^A-Z0-9]", "", value.upper())


def normalize_model_token(token: str) -> str:
    cleaned = token.strip("()[]{}.,;:!?\"'")
    cleaned = cleaned.strip("-/._")
    cleaned = re.sub(r"-{2,}", "-", cleaned)
    cleaned = re.sub(r"/{2,}", "/", cleaned)
    cleaned = re.sub(r"\.{2,}", ".", cleaned)
    return cleaned


def format_model_token(token: str) -> str:
    if token.islower():
        return token.upper()
    return token


def valid_model_token(token: str, *, allow_alpha_slug: bool = False) -> bool:
    cleaned = normalize_model_token(token)
    if len(cleaned) < 3 or len(cleaned) > 30:
        return False
    if not re.fullmatch(r"[A-Za-z0-9./-]+", cleaned):
        return False

    upper = cleaned.upper()
    compact = compact_model_key(cleaned)
    if upper in MODEL_STOPWORDS:
        return False
    if not compact or compact in MODEL_BRAND_TOKENS:
        return False
    if upper.replace("-", "").replace("/", "").replace(".", "").isdigit():
        return False
    if re.fullmatch(r"\d+(?:[.,]\d+)+", upper):
        return False
    if re.search(r"\d+\.\d{3,}", upper):
        return False

    letter_count = sum(char.isalpha() for char in cleaned)
    digit_count = sum(char.isdigit() for char in cleaned)
    if letter_count < 2:
        return False

    parts = [part for part in re.split(r"[-/.]", upper) if part]
    if any(part in MODEL_STOPWORDS for part in parts):
        return False

    if re.fullmatch(r"[A-Za-z]+", cleaned):
        if allow_alpha_slug:
            return 4 <= len(cleaned) <= 12
        return cleaned.isupper() and 4 <= len(cleaned) <= 10

    if digit_count:
        return True

    if "-" in cleaned or "/" in cleaned or "." in cleaned:
        if not allow_alpha_slug:
            return False
        return 2 <= len(parts) <= 3 and all(2 <= len(part) <= 12 for part in parts)

    return False


def iter_slug_model_candidates(segment: str) -> list[str]:
    cleaned_segment = normalize_model_token(segment.replace("_", "-"))
    if not cleaned_segment:
        return []

    raw_candidates = [cleaned_segment]
    parts = [part for part in cleaned_segment.split("-") if part]
    raw_candidates.extend(parts)

    for left, right in zip(parts, parts[1:]):
        numeric_left = left.replace(".", "", 1).isdigit()
        if numeric_left and any(char.isalpha() for char in right):
            raw_candidates.append(f"{left}-{right}")

    results: list[str] = []
    seen: set[str] = set()
    for token in raw_candidates:
        cleaned = normalize_model_token(token)
        if not valid_model_token(cleaned, allow_alpha_slug=True):
            continue
        formatted = format_model_token(cleaned)
        key = formatted.casefold()
        if key in seen:
            continue
        seen.add(key)
        results.append(formatted)
    return results


def prune_segment_candidates(segment: str, candidates: list[str]) -> list[str]:
    segment_key = segment.casefold()
    trimmed = [candidate for candidate in candidates if candidate.casefold() != segment_key]
    specific_trimmed = [
        candidate
        for candidate in trimmed
        if any(char.isdigit() for char in candidate)
        or re.fullmatch(r"[A-Z]{2,6}", candidate.upper())
    ]
    if specific_trimmed:
        return trimmed
    return candidates


def is_strong_text_model(token: str) -> bool:
    if token[:1].isdigit():
        return False

    upper = token.upper()
    digit_count = sum(char.isdigit() for char in upper)
    if digit_count == 0:
        return False
    if re.fullmatch(r"\d+(?:ST|ND|RD|TH)", upper):
        return False
    if any(char.islower() for char in token) and "-" not in token and "/" not in token:
        return False
    if "." in token and "-" not in token and "/" not in token and digit_count < 2:
        return False
    if digit_count == 1 and "-" not in upper and "/" not in upper and "." not in upper:
        return token.isupper() and len(upper) >= 4
    return True


def detect_model_signals(*, stem: str, family: str, text: str) -> list[str]:
    results: list[str] = []
    seen: set[str] = set()

    def push(token: str) -> None:
        key = token.casefold()
        if key in seen:
            return
        seen.add(key)
        results.append(token)

    stem_parts = stem.split("__")
    slug_sources: list[tuple[str, bool]] = [(family, True)]
    if len(stem_parts) > 1:
        slug_sources.append((stem_parts[1], True))
    if len(stem_parts) > 3:
        slug_sources.append((stem_parts[3], False))

    for segment, trim_full_segment in slug_sources:
        candidates = iter_slug_model_candidates(segment)
        if trim_full_segment:
            candidates = prune_segment_candidates(segment, candidates)
        for token in candidates:
            push(token)
            if len(results) >= 8:
                return results

    if not text:
        return results

    counts: Counter[str] = Counter()
    display_tokens: dict[str, str] = {}
    for raw_token in re.findall(r"\b[A-Za-z0-9][A-Za-z0-9./-]{2,}\b", text):
        cleaned = normalize_model_token(raw_token)
        if not valid_model_token(cleaned):
            continue
        key = cleaned.casefold()
        counts[key] += 1
        display_tokens.setdefault(key, format_model_token(cleaned))

    for key, count in counts.most_common():
        token = display_tokens[key]
        if count < 2:
            continue
        if not is_strong_text_model(token):
            continue
        push(token)
        if len(results) >= 8:
            break

    return results


def build_curation_model_candidates(family: str) -> list[str]:
    candidates = iter_slug_model_candidates(family)
    return prune_segment_candidates(family, candidates)


def detect_term_signals(text: str) -> list[str]:
    lowered = text.lower()
    results: list[str] = []
    for keyword in TERM_KEYWORDS:
        if keyword in lowered:
            results.append(keyword)
        if len(results) >= 8:
            break
    return results


def build_snippets(text: str) -> list[str]:
    candidates: list[tuple[int, int, str]] = []
    seen: set[str] = set()
    for index, raw_line in enumerate(text.splitlines()):
        line = clean_signal_line(raw_line, max_length=200)
        if len(line) < 12 or is_noise_line(line):
            continue
        key = line.casefold()
        if key in seen:
            continue
        seen.add(key)
        score = technical_line_score(line)
        if score < 2 and not SECTION_KEYWORD_RE.search(line):
            continue
        candidates.append((score, -index, line))

    candidates.sort(reverse=True)
    snippets = [line for _score, _index, line in candidates[:12]]
    if snippets:
        return snippets

    for raw_line in text.splitlines():
        line = clean_signal_line(raw_line, max_length=200)
        if len(line) < 12 or is_noise_line(line):
            continue
        snippets.append(line)
        if len(snippets) >= 10:
            break
    return snippets


def join_or_na(values: list[str]) -> str:
    if not values:
        return "n/a"
    return ", ".join(values)


def load_pdf_toolchain_audit() -> dict[str, dict[str, object]]:
    if not PDF_TOOLCHAIN_AUDIT_PATH.exists():
        return {}

    try:
        payload = json.loads(PDF_TOOLCHAIN_AUDIT_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}

    records: dict[str, dict[str, object]] = {}
    for item in payload.get("pdfs", []):
        if not isinstance(item, dict):
            continue
        relative_path = item.get("relative_path")
        if isinstance(relative_path, str) and relative_path:
            records[relative_path] = item
    return records


def load_ocr_results() -> dict[str, dict[str, object]]:
    if not OCR_RESULTS_PATH.exists():
        return {}

    try:
        payload = json.loads(OCR_RESULTS_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}

    records: dict[str, dict[str, object]] = {}
    for item in payload.get("results", []):
        if not isinstance(item, dict):
            continue
        relative_path = item.get("source_pdf")
        if isinstance(relative_path, str) and relative_path:
            records[relative_path] = item
    return records


def read_ocr_text(ocr_record: dict[str, object] | None) -> str:
    if not ocr_record:
        return ""
    if str(ocr_record.get("status")) not in {"completed", "partial"}:
        return ""
    output_text = ocr_record.get("output_text")
    if not isinstance(output_text, str) or not output_text:
        return ""
    path = ROOT / output_text
    if not path.exists():
        return ""
    try:
        raw_text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""
    ignored_prefixes = (
        "OCR text generated at:",
        "source_pdf:",
        "source_sha256:",
        "language:",
        "dpi:",
        "psm:",
        "status:",
        "--- PAGE ",
    )
    lines = [
        line
        for line in raw_text.splitlines()
        if not any(line.startswith(prefix) for prefix in ignored_prefixes)
    ]
    return "\n".join(lines)


def relative_ocr_path(ocr_record: dict[str, object] | None, key: str) -> str:
    if not ocr_record:
        return "n/a"
    value = ocr_record.get(key)
    if not isinstance(value, str) or not value:
        return "n/a"
    return value


def ocr_status_from_record(ocr_record: dict[str, object] | None) -> str:
    if not ocr_record:
        return "nao-gerado"
    return scalar_from_audit(ocr_record.get("status"), "nao-gerado")


def ocr_priority_from_sources(
    audit_record: dict[str, object] | None,
    ocr_record: dict[str, object] | None,
) -> str:
    audit_priority = scalar_from_audit(
        audit_record.get("ocr_priority") if audit_record else None,
        "sem-auditoria",
    )
    if (
        audit_priority in {"alta", "media", "reparar-primeiro", "bloqueado"}
        and ocr_status_from_record(ocr_record) in {"completed", "partial"}
    ):
        return "concluido"
    return audit_priority


def scalar_from_audit(value: object, default: str = "n/a") -> str:
    if value is None or value == "":
        return default
    if isinstance(value, bool):
        return "sim" if value else "nao"
    return str(value)


def metadata_title_from_audit(audit_record: dict[str, object] | None) -> str:
    if not audit_record:
        return "n/a"
    metadata = audit_record.get("metadata")
    if not isinstance(metadata, dict):
        return "n/a"
    return scalar_from_audit(metadata.get("title"))


def build_links(record: NoteRecord) -> list[str]:
    links = [
        "Tabela-Mestre do Acervo - Biblioteca de Referencia",
        "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Local - Indice Gerado",
        "90_Revisao_Manual/00_Entrada_e_Controle/Portal do Acervo - Biblioteca de Referencia",
    ]
    extra = SYSTEM_CONTEXT_LINKS.get(record.system)
    if extra:
        links.append(extra)
    return links


def build_application_lines(record: NoteRecord) -> list[str]:
    return SYSTEM_APPLICATIONS.get(
        record.system,
        ["usar esta nota como ponte de triagem entre o PDF bruto e a curadoria humana"],
    )


def build_question_lines(record: NoteRecord) -> list[str]:
    return SYSTEM_QUESTIONS.get(
        record.system,
        [
            "quais modelos e revisoes este PDF cobre de verdade, e quais ficaram de fora?",
            "quais paginas merecem virar nota humana curada ou material de aula?",
        ],
    )


def build_action_lines(record: NoteRecord) -> list[str]:
    if record.system == "Geradores":
        return GENERATOR_ACTIONS
    return COMMON_ACTIONS


def is_placeholder_curation_block(block: str) -> bool:
    return (
        "### Resumo humano" in block
        and "### Aplicacao de oficina" in block
        and "### Pontos de atencao" in block
        and "- notas relacionadas: pendente" in block
        and "- curadoria humana: pendente" in block
        and block.count("- pendente") >= 3
    )


def should_preserve_curation_block(existing: ExistingNoteState) -> bool:
    if not existing.curation_block:
        return False
    if existing.curation_stage and existing.curation_stage != "triagem-automatica":
        return True
    return not is_placeholder_curation_block(existing.curation_block)


def build_default_curation_block(record: NoteRecord) -> str:
    model_lines = build_curation_model_candidates(record.family) or [record.family]
    model_bullets = "\n".join(f"- `{item}`" for item in model_lines)
    return "\n".join(
        [
            "<!-- CURADORIA-HUMANA:START -->",
            "## Curadoria humana",
            "",
            "### Resumo humano",
            "- pendente",
            "",
            "### Aplicacao de oficina",
            "- pendente",
            "",
            "### Modelos cobertos confirmados",
            model_bullets,
            "",
            "### Pontos de atencao",
            "- pendente",
            "",
            "### Integracoes e links internos",
            f"- sistema-base: `{record.system}`",
            f"- marca/familia: `{record.brand} / {record.family}`",
            "- notas relacionadas: pendente",
            "",
            "### Status de curadoria",
            f"- tipo documental confirmado: `{record.document_kind}`",
            "- curadoria humana: pendente",
            "- pronto para ensino/SEO: nao",
            "<!-- CURADORIA-HUMANA:END -->",
        ]
    )


def collect_pdf_records() -> list[NoteRecord]:
    records: list[NoteRecord] = []
    skipped_outside_structure: list[Path] = []
    toolchain_audit = load_pdf_toolchain_audit()
    ocr_results = load_ocr_results()

    for pdf_path in sorted(ACERVO_LOCAL_ROOT.rglob("*.pdf")):
        if "Acervo do humano" in pdf_path.parts:
            continue

        relative_pdf_path = pdf_path.relative_to(ACERVO_LOCAL_ROOT)
        if len(relative_pdf_path.parts) < 4:
            skipped_outside_structure.append(relative_pdf_path)
            continue

        audit_key = f"90_Revisao_Manual/_Acervo_Local/{relative_pdf_path.as_posix()}"
        audit_record = toolchain_audit.get(audit_key)
        ocr_record = ocr_results.get(audit_key)
        relative_note_path = relative_pdf_path.with_suffix(".md")
        note_path = ACERVO_NOTAS_ROOT / relative_note_path

        parts = relative_pdf_path.parts
        system = parts[0] if len(parts) > 0 else "Sem-Sistema"
        brand = parts[1] if len(parts) > 1 else "Sem-Marca"
        family = parts[2] if len(parts) > 2 else "Sem-Familia"
        stem = pdf_path.stem

        existing = parse_existing_note(note_path)
        extraction = extract_pdf_text(
            pdf_path,
            max_pages=MAX_ANALYSIS_PAGES,
            timeout=EXTRACTION_TIMEOUT_SECONDS,
        )
        ocr_text = read_ocr_text(ocr_record)
        analysis_text = extraction.text if extraction.useful_text else ocr_text
        analysis_source = extraction.method if extraction.useful_text else (
            "ocr-sidecar" if ocr_text else "metadata-only"
        )
        text_extractable = "sim" if extraction.useful_text else "nao"
        seed_text = f"{brand}\n{family}\n{stem}\n{analysis_text}"
        metadata_title = metadata_title_from_audit(audit_record)

        detected_models = detect_model_signals(stem=stem, family=family, text=analysis_text)
        detected_terms = detect_term_signals(seed_text)
        detected_brands = detect_brand_signals(seed_text)
        document_kind = detect_document_kind(stem)
        document_codes = extract_document_codes(
            stem=stem,
            metadata_title=metadata_title,
            text=analysis_text,
        )
        revision_signals = extract_revision_signals(analysis_text)
        technical_specs = extract_technical_specs(analysis_text)
        technical_sections = extract_technical_sections(analysis_text)
        curation_topics = detect_curation_topics(
            seed_text,
            system=system,
            document_kind=document_kind,
        )
        title = build_human_title(
            stem=stem,
            brand=brand,
            family=family,
            document_kind=document_kind,
            document_codes=document_codes,
            detected_models=detected_models,
            metadata_title=metadata_title,
        )

        record = NoteRecord(
            pdf_path=pdf_path,
            note_path=note_path,
            relative_pdf=relative_pdf_path.as_posix(),
            relative_note=relative_note_path.as_posix(),
            system=system,
            brand=brand,
            family=family,
            title=title,
            document_kind=document_kind,
            curation_priority=detect_curation_priority(stem, existing),
            curation_stage=detect_curation_stage(existing),
            source_sha256=sha256(pdf_path),
            extraction_method=extraction.method,
            text_extractable=text_extractable,
            size_label=human_size(pdf_path.stat().st_size),
            pdf_pages=scalar_from_audit(
                audit_record.get("pages") if audit_record else None,
                "sem-auditoria",
            ),
            pdf_version=scalar_from_audit(
                audit_record.get("pdf_version") if audit_record else None,
                "sem-auditoria",
            ),
            pdf_encrypted=scalar_from_audit(
                audit_record.get("encrypted") if audit_record else None,
                "sem-auditoria",
            ),
            qpdf_status=scalar_from_audit(
                audit_record.get("qpdf_status") if audit_record else None,
                "sem-auditoria",
            ),
            ocr_priority=ocr_priority_from_sources(audit_record, ocr_record),
            ocr_reason=scalar_from_audit(
                audit_record.get("ocr_reason") if audit_record else None,
                "sem auditoria operacional executada",
            ),
            ocr_status=ocr_status_from_record(ocr_record),
            ocr_text_path=relative_ocr_path(ocr_record, "output_text"),
            ocr_note_path=relative_ocr_path(ocr_record, "output_note"),
            ocr_text_chars=scalar_from_audit(
                ocr_record.get("chars") if ocr_record else None,
                "0",
            ),
            analysis_source=analysis_source,
            metadata_title=metadata_title,
            detected_brands=detected_brands,
            detected_models=detected_models,
            detected_terms=detected_terms,
            document_codes=document_codes,
            revision_signals=revision_signals,
            technical_specs=technical_specs,
            technical_sections=technical_sections,
            curation_topics=curation_topics,
            snippets=build_snippets(analysis_text),
            curation_block="",
        )

        record.curation_block = (
            existing.curation_block
            if should_preserve_curation_block(existing)
            else build_default_curation_block(record)
        )
        records.append(record)

    if skipped_outside_structure:
        print("PDFs ignorados fora do padrao Sistema/Marca/Familia:")
        for path in skipped_outside_structure:
            print(f"- {path.as_posix()}")

    return records


def render_note(record: NoteRecord, reviewed_on: str) -> str:
    links = build_links(record)
    applications = build_application_lines(record)
    questions = build_question_lines(record)
    actions = build_action_lines(record)

    snippet_lines = record.snippets or [
        "nenhum trecho textual confiavel foi extraido automaticamente"
    ]

    body: list[str] = [
        "---",
        f'title: "{record.title}"',
        'note_type: "acervo-companion"',
        'domain: "90_Revisao_Manual"',
        'status: "auto-extracted"',
        'acervo_origin: "acervo-principal"',
        f'document_kind: "{record.document_kind}"',
        f'curation_priority: "{record.curation_priority}"',
        f'curation_stage: "{record.curation_stage}"',
        f'reviewed_on: "{reviewed_on}"',
        'review_jurisdiction: "Brasil"',
        f'source_pdf: "{record.relative_pdf}"',
        f'source_sha256: "{record.source_sha256}"',
        f'acervo_system: "{record.system}"',
        f'acervo_brand: "{record.brand}"',
        f'acervo_family: "{record.family}"',
        f'extraction_method: "{record.extraction_method}"',
        f'text_extractable: "{record.text_extractable}"',
        f'pdf_pages: "{record.pdf_pages}"',
        f'pdf_version: "{record.pdf_version}"',
        f'pdf_encrypted: "{record.pdf_encrypted}"',
        f'qpdf_status: "{record.qpdf_status}"',
        f'ocr_priority: "{record.ocr_priority}"',
        f'ocr_status: "{record.ocr_status}"',
        f'ocr_text_path: "{record.ocr_text_path}"',
        f'ocr_note_path: "{record.ocr_note_path}"',
        f'ocr_text_chars: "{record.ocr_text_chars}"',
        f'analysis_source: "{record.analysis_source}"',
        f'detected_document_codes: "{join_or_na(record.document_codes)}"',
        f'curation_topics: "{join_or_na(record.curation_topics)}"',
        "aliases:",
        f'  - "{record.pdf_path.name}"',
        "related_notes:",
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Local - Indice Gerado"',
        '  - "Tabela-Mestre do Acervo - Biblioteca de Referencia"',
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado"',
        "---",
        "",
        f"# {record.title}",
        "",
        "> [!abstract] Resumo tecnico",
        "> Nota companheira gerada automaticamente a partir do PDF do acervo local.",
        "> Ela serve como camada de rastreio rapido, busca textual e preparo de curadoria editorial.",
        "",
    ]
    if record.text_extractable == "nao" and record.ocr_status in {"completed", "partial"}:
        body.extend(
            [
                "> [!success] OCR auxiliar disponivel",
                f"> O PDF original nao tem texto extraivel confiavel, mas ha OCR `{record.ocr_status}` em `{record.ocr_note_path}`.",
                "",
            ]
        )
    elif record.text_extractable == "nao":
        body.extend(
            [
            "> [!warning] Extracao textual com baixa confianca",
            "> Esta nota ficou limitada a metadados, familia tecnica e trilha editorial. Use o PDF original como fonte primaria.",
            "",
            ]
        )
    if record.ocr_priority in {"alta", "media", "reparar-primeiro", "bloqueado"}:
        body.extend(
            [
                "> [!tip] Prioridade operacional de OCR",
                f"> Prioridade: `{record.ocr_priority}`. Motivo: {record.ocr_reason}",
                "",
            ]
        )

    body.extend(
        [
            "## Fonte",
            "",
            f"- PDF: [{record.pdf_path.name}](</{absolute_link(record.pdf_path)}>)",
            f"- caminho relativo: `{record.relative_pdf}`",
            f"- nota companheira: `90_Revisao_Manual/_Acervo_Notas/{record.relative_note}`",
            f"- tamanho do arquivo: `{record.size_label}`",
            f"- paginas detectadas: `{record.pdf_pages}`",
            f"- versao PDF: `{record.pdf_version}`",
            f"- PDF criptografado: `{record.pdf_encrypted}`",
            f"- titulo em metadados: `{record.metadata_title}`",
            f"- texto extraivel detectado: `{record.text_extractable}`",
            f"- tipo documental detectado: `{record.document_kind}`",
            f"- metodo de extracao: `{record.extraction_method}`",
            f"- status qpdf: `{record.qpdf_status}`",
            f"- prioridade OCR: `{record.ocr_priority}`",
            f"- status OCR auxiliar: `{record.ocr_status}`",
            f"- nota OCR auxiliar: `{record.ocr_note_path}`",
            f"- texto OCR auxiliar: `{record.ocr_text_path}`",
            f"- caracteres OCR auxiliares: `{record.ocr_text_chars}`",
            f"- fonte de analise automatica: `{record.analysis_source}`",
            "",
            "## Sinais principais",
            "",
            f"- sistema: `{record.system}`",
            f"- marca: `{record.brand}`",
            f"- familia: `{record.family}`",
            f"- marcas detectadas: `{join_or_na(record.detected_brands)}`",
            f"- codigos/modelos detectados: `{join_or_na(record.detected_models)}`",
            f"- codigos tecnicos/documentais detectados: `{join_or_na(record.document_codes)}`",
            f"- datas/revisoes detectadas: `{join_or_na(record.revision_signals)}`",
            f"- termos uteis detectados: `{join_or_na(record.detected_terms)}`",
            f"- topicos de curadoria: `{join_or_na(record.curation_topics)}`",
            "",
            "## Extracao tecnica automatica",
            "",
            "### Secoes e assuntos provaveis",
            "",
        ]
    )
    if record.technical_sections:
        body.extend(f"- `{line}`" for line in record.technical_sections)
    else:
        body.append("- `n/a`")
    body.extend(
        [
            "",
            "### Especificacoes e linhas de valor tecnico",
            "",
        ]
    )
    if record.technical_specs:
        body.extend(f"- `{line}`" for line in record.technical_specs)
    else:
        body.append("- `nenhuma especificacao curta foi extraida automaticamente`")
    body.extend(
        [
            "",
            "### Leitura operacional sugerida",
            "",
        ]
    )
    body.extend(f"- {topic}" for topic in (record.curation_topics or ["confirmar escopo diretamente no PDF"]))
    body.extend(
        [
            "",
            "## Aplicacao e integracoes sugeridas",
            "",
        ]
    )

    body.extend(f"- {line}" for line in applications)
    body.extend(
        [
            "",
            "## Links internos sugeridos",
            "",
        ]
    )
    body.extend(f"- `{link}`" for link in links)
    body.extend(
        [
            "",
            record.curation_block,
            "",
            "## Trechos indexaveis",
            "",
        ]
    )
    body.extend(f"- `{line}`" for line in snippet_lines)
    body.extend(
        [
            "",
            "## Perguntas de curadoria",
            "",
        ]
    )
    body.extend(f"- {line}" for line in questions)
    body.extend(
        [
            "",
            "## Acoes sugeridas",
            "",
        ]
    )
    body.extend(f"- {line}" for line in actions)
    body.extend(
        [
            "",
            "## Observacoes",
            "",
            "- esta nota e automatica; revisar manualmente antes de usar como resumo definitivo",
            "- quando este PDF for relevante para ensino, oficina ou SEO, vale evoluir para nota humana curada",
            "",
        ]
    )
    return "\n".join(body)


def render_index(records: list[NoteRecord], reviewed_on: str) -> str:
    by_system = Counter(record.system for record in records)
    by_kind = Counter(record.document_kind for record in records)
    by_priority = Counter(record.curation_priority for record in records)
    by_qpdf = Counter(record.qpdf_status for record in records)
    by_ocr = Counter(record.ocr_priority for record in records)
    by_ocr_status = Counter(record.ocr_status for record in records)

    family_links: dict[str, list[tuple[str, Path]]] = defaultdict(list)
    for record in records:
        label = f"{record.brand} / {record.family}"
        family_links[record.system].append((label, record.note_path))

    lines: list[str] = [
        "---",
        'title: "Acervo Notas - Indice Gerado"',
        'note_type: "index"',
        'domain: "90_Revisao_Manual"',
        'status: "auto-generated"',
        f'reviewed_on: "{reviewed_on}"',
        'review_jurisdiction: "Brasil"',
        "related_notes:",
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Local - Indice Gerado"',
        '  - "Tabela-Mestre do Acervo - Biblioteca de Referencia"',
        '  - "90_Revisao_Manual/_Acervo_Notas/README"',
        "---",
        "",
        "# Acervo Notas - Indice Gerado",
        "",
        "> [!abstract] Resumo tecnico",
        "> Painel automatico da camada companheira em Markdown dos PDFs do acervo principal.",
        "",
        "## Panorama geral",
        "",
        f"- notas companheiras: `{len(records)}`",
        f"- sistemas cobertos: `{len(by_system)}`",
        f"- atualizacao: `{reviewed_on}`",
        "",
        "## Distribuicao por sistema",
        "",
    ]

    for system in SYSTEM_ORDER:
        if system in by_system:
            lines.append(f"- `{system}`: `{by_system[system]}`")

    lines.extend(["", "## Distribuicao por tipo documental", ""])
    for kind in DOCUMENT_KIND_ORDER:
        if kind in by_kind:
            lines.append(f"- `{kind}`: `{by_kind[kind]}`")

    lines.extend(["", "## Distribuicao por prioridade de curadoria", ""])
    for priority in ("alta", "baixa"):
        if priority in by_priority:
            lines.append(f"- `{priority}`: `{by_priority[priority]}`")

    lines.extend(["", "## Saude operacional dos PDFs", ""])
    for status, count in sorted(by_qpdf.items()):
        lines.append(f"- qpdf `{status}`: `{count}`")

    lines.extend(["", "## Fila operacional de OCR", ""])
    for priority, count in sorted(by_ocr.items()):
        lines.append(f"- OCR `{priority}`: `{count}`")

    lines.extend(["", "## OCR auxiliar gerado", ""])
    for status, count in sorted(by_ocr_status.items()):
        lines.append(f"- OCR auxiliar `{status}`: `{count}`")

    for system in SYSTEM_ORDER:
        if system not in family_links:
            continue

        unique_links: list[tuple[str, Path]] = []
        seen_labels: set[str] = set()
        for label, note_path in sorted(family_links[system], key=lambda item: item[0].casefold()):
            if label.casefold() in seen_labels:
                continue
            seen_labels.add(label.casefold())
            unique_links.append((label, note_path))

        lines.extend(["", f"## {system}", ""])
        for label, note_path in unique_links:
            lines.append(f"- [{label}](</{absolute_link(note_path)}>)")

    lines.append("")
    return "\n".join(lines)


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def main() -> int:
    reviewed_on = date.today().isoformat()
    records = collect_pdf_records()

    for record in records:
        note_content = render_note(record, reviewed_on)
        write_file(record.note_path, note_content)

    index_content = render_index(records, reviewed_on)
    write_file(INDEX_NOTE_PATH, index_content)

    print(f"Notas companheiras geradas: {len(records)}")
    print(f"Painel atualizado: {INDEX_NOTE_PATH.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
