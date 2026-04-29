from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent

if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.append(str(SCRIPTS_ROOT))

from vault_tools import ROOT, is_excluded_path, write_json  # noqa: E402


TAXONOMY_PATH = SCRIPT_DIR / "acervo_taxonomy.json"
DATA_DIR = ROOT / "90_Revisao_Manual" / "_Dados_Acervo"
BANK_JSON_PATH = DATA_DIR / "brand-norm-bank.json"
BANK_NOTE_PATH = (
    ROOT
    / "90_Revisao_Manual"
    / "20_Matrizes_Fontes_e_Links"
    / "Banco de Marcas e Normas Citadas — Corpus Integral.md"
)
GENERATED_NOTE_NAMES = {
    "Acervo Local — Índice Gerado.md",
    "Banco de Marcas e Normas Citadas — Corpus Integral.md",
    "Preparação Source-First — Resolver de Links Oficiais.md",
}
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^\s)]+)\)")
BARE_URL_RE = re.compile(r"https?://[^\s)>]+")
SPACE_RE = re.compile(r"\s+")
COMMON_RESOURCE_KEYWORDS = (
    "manual",
    "download",
    "support",
    "resource",
    "resources",
    "document",
    "documents",
    "library",
    "catalog",
    "catalogue",
    "guide",
    "brochure",
    "portfolio",
    "literature",
    "spec",
    "product",
)
NORM_REGEXES = (
    ("ABYC", re.compile(r"\bABYC\s+[A-Z]{1,3}-\d{1,3}[A-Z]?\b", re.IGNORECASE)),
    ("ISO", re.compile(r"\bISO\s+\d{4,5}(?:-\d+)?(?::\d{4})?\b", re.IGNORECASE)),
    ("IEC", re.compile(r"\bIEC\s+\d{3,5}(?:-\d+)*(?::\d{4})?\b", re.IGNORECASE)),
    ("ABNT NBR", re.compile(r"\b(?:ABNT\s+)?NBR\s+\d{4,5}(?:-\d+)?\b", re.IGNORECASE)),
    ("NR", re.compile(r"\bNR[-\s]?\d{1,2}\b", re.IGNORECASE)),
    ("NORMAM", re.compile(r"\bNORMAM[-\s]?\d{1,3}\b", re.IGNORECASE)),
    ("SOLAS", re.compile(r"\bSOLAS\b", re.IGNORECASE)),
    ("COLREG", re.compile(r"\bCOLREGS?\b", re.IGNORECASE)),
)
UNMAPPED_STOPWORDS = {
    "Manual",
    "Manuals",
    "Downloads",
    "Support",
    "Resources",
    "Library",
    "Guide",
    "Brochure",
    "Product",
    "Products",
    "Documents",
    "Portal",
    "Marine",
}


def load_taxonomy() -> dict[str, list[dict[str, object]]]:
    return json.loads(TAXONOMY_PATH.read_text(encoding="utf-8"))


def corpus_files() -> list[Path]:
    paths: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if is_excluded_path(path):
            continue
        if path.name in GENERATED_NOTE_NAMES:
            continue
        paths.append(path)
    return sorted(paths)


def normalize_space(value: str) -> str:
    return SPACE_RE.sub(" ", value).strip()


def normalize_norm(value: str) -> str:
    text = normalize_space(value).upper()
    text = text.replace("ABNT NBR", "NBR")
    text = text.replace("NR ", "NR-")
    text = text.replace("NORMAM ", "NORMAM-")
    return text


def alias_pattern(alias: str) -> re.Pattern[str]:
    return re.compile(rf"(?<![A-Za-z0-9]){re.escape(alias)}(?![A-Za-z0-9])", re.IGNORECASE)


def extract_urls(text: str) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()

    for match in MD_LINK_RE.finditer(text):
        label = normalize_space(match.group(1))
        url = match.group(2).rstrip(").,;\"'")
        key = (label, url)
        if key in seen:
            continue
        seen.add(key)
        results.append(
            {
                "label": label,
                "url": url,
                "domain": urlparse(url).netloc.lower(),
            }
        )

    for match in BARE_URL_RE.finditer(text):
        url = match.group(0).rstrip(").,;\"'")
        key = ("", url)
        if key in seen:
            continue
        seen.add(key)
        results.append(
            {
                "label": "",
                "url": url,
                "domain": urlparse(url).netloc.lower(),
            }
        )

    return results


def note_payload(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    relative_path = path.relative_to(ROOT).as_posix()
    return {
        "path": path,
        "relative_path": relative_path,
        "text": text,
        "urls": extract_urls(text),
    }


def url_matches_entity(url_info: dict[str, str], entity: dict[str, object], aliases: list[str]) -> bool:
    label = url_info["label"].lower()
    url = url_info["url"].lower()
    domain = url_info["domain"].lower()
    domains = [str(item).lower() for item in entity.get("domains", [])]
    domain_match = any(seed_domain and seed_domain in domain for seed_domain in domains)

    if domain_match:
        return True

    if domains:
        return False

    if any(alias.lower() in label or alias.lower() in url for alias in aliases):
        return True

    if any(keyword in label or keyword in url for keyword in COMMON_RESOURCE_KEYWORDS):
        return any(alias.lower() in label or alias.lower() in url for alias in aliases)

    return False


def resource_score(url_info: dict[str, str], entity: dict[str, object], aliases: list[str]) -> int:
    score = 0
    label = url_info["label"].lower()
    url = url_info["url"].lower()
    domain = url_info["domain"].lower()
    domains = [str(item).lower() for item in entity.get("domains", [])]

    if any(seed_domain and seed_domain in domain for seed_domain in domains):
        score += 4
    if any(alias.lower() in label or alias.lower() in url for alias in aliases):
        score += 3
    if any(keyword in label or keyword in url for keyword in COMMON_RESOURCE_KEYWORDS):
        score += 2
    if url.endswith(".pdf"):
        score += 2
    return score


def looks_like_unmapped_candidate(label: str) -> bool:
    if not label or label in UNMAPPED_STOPWORDS:
        return False
    if len(label) > 48:
        return False
    if not any(char.isdigit() or char.isupper() for char in label):
        return False
    if label.lower() == label:
        return False
    if all(char in "-_/ " or char.isdigit() for char in label):
        return False
    return True


def build_bank() -> dict[str, object]:
    taxonomy = load_taxonomy()
    notes = [note_payload(path) for path in corpus_files()]

    brand_entries: dict[str, dict[str, object]] = {}
    product_entries: dict[str, dict[str, object]] = {}
    brand_patterns: dict[str, list[re.Pattern[str]]] = {}
    product_patterns: dict[str, list[re.Pattern[str]]] = {}
    product_to_brand: dict[str, str] = {}
    body_patterns: dict[str, list[re.Pattern[str]]] = {}

    for entity in taxonomy["brands"]:
        canonical = str(entity["canonical"])
        aliases = sorted({canonical, *[str(alias) for alias in entity.get("aliases", [])]}, key=len, reverse=True)
        brand_entries[canonical] = {
            "canonical": canonical,
            "type": entity.get("type", "brand"),
            "parent": entity.get("parent", ""),
            "aliases": aliases,
            "domains": entity.get("domains", []),
            "seed_urls": entity.get("seed_urls", []),
            "note_mentions": Counter(),
            "mention_count": 0,
            "resources": {},
        }
        brand_patterns[canonical] = [alias_pattern(alias) for alias in aliases if alias]

    for entity in taxonomy["products"]:
        canonical = str(entity["canonical"])
        aliases = sorted({canonical, *[str(alias) for alias in entity.get("aliases", [])]}, key=len, reverse=True)
        brand = str(entity["brand"])
        product_entries[canonical] = {
            "canonical": canonical,
            "brand": brand,
            "aliases": aliases,
            "note_mentions": Counter(),
            "mention_count": 0,
        }
        product_patterns[canonical] = [alias_pattern(alias) for alias in aliases if alias]
        product_to_brand[canonical] = brand

    for entity in taxonomy["norm_bodies"]:
        canonical = str(entity["canonical"])
        aliases = sorted({canonical, *[str(alias) for alias in entity.get("aliases", [])]}, key=len, reverse=True)
        body_patterns[canonical] = [alias_pattern(alias) for alias in aliases if alias]

    norm_refs: dict[str, dict[str, object]] = {}
    norm_body_counts: dict[str, Counter[str]] = {name: Counter() for name in body_patterns}
    unmapped_candidates: Counter[str] = Counter()
    unmapped_notes: dict[str, set[str]] = defaultdict(set)

    for note in notes:
        note_path = str(note["relative_path"])
        text = str(note["text"])
        urls = list(note["urls"])

        brands_in_note: set[str] = set()

        for canonical, patterns in brand_patterns.items():
            count = sum(len(pattern.findall(text)) for pattern in patterns)
            if count <= 0:
                continue
            brand_entries[canonical]["mention_count"] = int(brand_entries[canonical]["mention_count"]) + count
            brand_entries[canonical]["note_mentions"][note_path] += count
            brands_in_note.add(canonical)

        for canonical, patterns in product_patterns.items():
            count = sum(len(pattern.findall(text)) for pattern in patterns)
            if count <= 0:
                continue
            product_entries[canonical]["mention_count"] = int(product_entries[canonical]["mention_count"]) + count
            product_entries[canonical]["note_mentions"][note_path] += count
            brands_in_note.add(product_to_brand[canonical])

        for body_name, patterns in body_patterns.items():
            count = sum(len(pattern.findall(text)) for pattern in patterns)
            if count > 0:
                norm_body_counts[body_name][note_path] += count

        for family, pattern in NORM_REGEXES:
            for match in pattern.findall(text):
                normalized = normalize_norm(match)
                entry = norm_refs.setdefault(
                    normalized,
                    {
                        "canonical": normalized,
                        "family": family,
                        "note_mentions": Counter(),
                        "mention_count": 0,
                    },
                )
                entry["mention_count"] = int(entry["mention_count"]) + 1
                entry["note_mentions"][note_path] += 1

        for brand_name in brands_in_note:
            aliases = list(brand_entries[brand_name]["aliases"])
            for url_info in urls:
                if not url_matches_entity(url_info, brand_entries[brand_name], aliases):
                    continue
                resource_key = url_info["url"]
                resource_entry = brand_entries[brand_name]["resources"].setdefault(
                    resource_key,
                    {
                        "url": url_info["url"],
                        "label": url_info["label"],
                        "domain": url_info["domain"],
                        "score": 0,
                        "notes": set(),
                    },
                )
                resource_entry["score"] = max(
                    int(resource_entry["score"]),
                    resource_score(url_info, brand_entries[brand_name], aliases),
                )
                resource_entry["notes"].add(note_path)

        mapped_labels: set[str] = set()
        for url_info in urls:
            label = url_info["label"]
            if not label:
                continue
            lower_label = label.lower()
            if any(alias.lower() in lower_label for entry in brand_entries.values() for alias in entry["aliases"]):
                mapped_labels.add(label)
                continue
            if any(alias.lower() in lower_label for entry in product_entries.values() for alias in entry["aliases"]):
                mapped_labels.add(label)
                continue
            if looks_like_unmapped_candidate(label):
                unmapped_candidates[label] += 1
                unmapped_notes[label].add(note_path)

    brands_output: list[dict[str, object]] = []
    for canonical, entry in brand_entries.items():
        note_mentions: Counter[str] = entry["note_mentions"]
        resources = []
        for resource_entry in entry["resources"].values():
            resources.append(
                {
                    "url": resource_entry["url"],
                    "label": resource_entry["label"],
                    "domain": resource_entry["domain"],
                    "score": resource_entry["score"],
                    "note_count": len(resource_entry["notes"]),
                    "notes": sorted(resource_entry["notes"]),
                }
            )
        resources.sort(key=lambda item: (-int(item["score"]), -int(item["note_count"]), str(item["url"])))
        brands_output.append(
            {
                "canonical": canonical,
                "type": entry["type"],
                "parent": entry["parent"],
                "aliases": entry["aliases"],
                "domains": entry["domains"],
                "seed_urls": entry["seed_urls"],
                "mention_count": entry["mention_count"],
                "note_count": len(note_mentions),
                "notes": [
                    {"path": path, "count": count}
                    for path, count in note_mentions.most_common()
                ],
                "resources": resources[:12],
            }
        )

    brands_output.sort(key=lambda item: (-int(item["note_count"]), -int(item["mention_count"]), str(item["canonical"])))

    products_output: list[dict[str, object]] = []
    for canonical, entry in product_entries.items():
        note_mentions = entry["note_mentions"]
        products_output.append(
            {
                "canonical": canonical,
                "brand": entry["brand"],
                "aliases": entry["aliases"],
                "mention_count": entry["mention_count"],
                "note_count": len(note_mentions),
                "notes": [
                    {"path": path, "count": count}
                    for path, count in note_mentions.most_common()
                ],
            }
        )
    products_output.sort(key=lambda item: (-int(item["note_count"]), -int(item["mention_count"]), str(item["canonical"])))

    norms_output: list[dict[str, object]] = []
    for normalized, entry in norm_refs.items():
        note_mentions = entry["note_mentions"]
        norms_output.append(
            {
                "canonical": normalized,
                "family": entry["family"],
                "mention_count": entry["mention_count"],
                "note_count": len(note_mentions),
                "notes": [
                    {"path": path, "count": count}
                    for path, count in note_mentions.most_common()
                ],
            }
        )
    norms_output.sort(key=lambda item: (-int(item["note_count"]), -int(item["mention_count"]), str(item["canonical"])))

    norm_bodies_output: list[dict[str, object]] = []
    for body_name, counter in norm_body_counts.items():
        mention_count = sum(counter.values())
        norm_bodies_output.append(
            {
                "canonical": body_name,
                "mention_count": mention_count,
                "note_count": len(counter),
                "notes": [{"path": path, "count": count} for path, count in counter.most_common()],
            }
        )
    norm_bodies_output.sort(key=lambda item: (-int(item["note_count"]), -int(item["mention_count"]), str(item["canonical"])))

    unmapped_output = [
        {
            "label": label,
            "count": count,
            "notes": sorted(unmapped_notes[label]),
        }
        for label, count in unmapped_candidates.most_common(40)
    ]

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "taxonomy_path": TAXONOMY_PATH.relative_to(ROOT).as_posix(),
        "notes_scanned": len(notes),
        "brands": brands_output,
        "products": products_output,
        "norms": norms_output,
        "norm_bodies": norm_bodies_output,
        "unmapped_candidates": unmapped_output,
    }


def brand_products(bank: dict[str, object], brand_name: str) -> list[dict[str, object]]:
    products = [item for item in bank["products"] if item["brand"] == brand_name and int(item["note_count"]) > 0]
    return sorted(products, key=lambda item: (-int(item["note_count"]), -int(item["mention_count"]), str(item["canonical"])))


def child_brands(bank: dict[str, object], parent_name: str) -> list[dict[str, object]]:
    children = [item for item in bank["brands"] if item["parent"] == parent_name and int(item["note_count"]) > 0]
    return sorted(children, key=lambda item: (-int(item["note_count"]), -int(item["mention_count"]), str(item["canonical"])))


def build_note(bank: dict[str, object]) -> str:
    reviewed_on = datetime.now().date().isoformat()
    top_brands = [item for item in bank["brands"] if int(item["note_count"]) > 0][:15]
    top_products = [item for item in bank["products"] if int(item["note_count"]) > 0][:20]
    top_norms = [item for item in bank["norms"] if int(item["note_count"]) > 0][:20]
    norm_families = [item for item in bank["norm_bodies"] if int(item["note_count"]) > 0]

    lines = [
        "---",
        'title: "Banco de Marcas e Normas Citadas — Corpus Integral"',
        'note_type: "inventory"',
        'domain: "90_Revisao_Manual"',
        'status: "active-curation"',
        f'reviewed_on: "{reviewed_on}"',
        'review_jurisdiction: "Brasil"',
        "aliases:",
        '  - "Banco do Corpus Integral"',
        '  - "Banco de Marcas e Normativas"',
        "related_notes:",
        '  - "MOC — Revisao Manual"',
        '  - "Matriz de Marcas Matriz — Ecossistemas e Subgrupos"',
        '  - "Matriz de Fontes — Fabricantes e Repositórios"',
        '  - "Tabela-Mestre do Acervo — Biblioteca de Referência"',
        '  - "Normas e Regulamentações — Abyc Iso e Brasil"',
        "---",
        "",
        "# Banco de Marcas e Normas Citadas — Corpus Integral",
        "",
        "> [!abstract] Resumo tecnico",
        "> Esta nota e gerada por Python a partir da varredura integral dos arquivos Markdown da vault. Ela consolida `marcas`, `submarcas`, `produtos/familias`, `corpos normativos` e `normas citadas` para orientar a biblioteca em modo `corpus-first + source-first`.",
        "",
        "> [!info] Geracao",
        "> Comando: `python scripts/acervo/build_brand_norm_bank.py`.",
        f"> Gerado em `{bank['generated_at']}`.",
        "",
        "## Resumo",
        "",
        f"- notas analisadas: `{bank['notes_scanned']}`",
        f"- marcas na taxonomia: `{len(bank['brands'])}`",
        f"- produtos/familias na taxonomia: `{len(bank['products'])}`",
        f"- normas especificas encontradas no corpus: `{len([item for item in bank['norms'] if int(item['note_count']) > 0])}`",
        f"- corpos normativos com presenca no corpus: `{len(norm_families)}`",
        "",
        "## Marcas mais citadas",
        "",
        "| Marca | Tipo | Notas | Citacoes | Parent |",
        "| --- | --- | --- | --- | --- |",
    ]

    for item in top_brands:
        parent = str(item["parent"]) or "-"
        lines.append(
            f"| {item['canonical']} | {item['type']} | `{item['note_count']}` | `{item['mention_count']}` | {parent} |"
        )

    lines.extend(["", "## Ecossistemas e desdobramentos", ""])
    for item in top_brands:
        if item["type"] != "brand":
            continue
        children = child_brands(bank, str(item["canonical"]))
        products = brand_products(bank, str(item["canonical"]))
        if not children and not products and not item["resources"]:
            continue
        lines.append(f"### {item['canonical']}")
        lines.append("")
        lines.append(
            f"- presenca no corpus: `{item['note_count']}` notas / `{item['mention_count']}` citacoes"
        )
        if children:
            child_labels = ", ".join(f"`{child['canonical']}`" for child in children[:8])
            lines.append(f"- submarcas/aliases fortes: {child_labels}")
        if products:
            product_labels = ", ".join(f"`{product['canonical']}`" for product in products[:8])
            lines.append(f"- produtos/familias detectados: {product_labels}")
        if item["resources"]:
            top_resources = item["resources"][:5]
            resource_labels = []
            for resource in top_resources:
                label = resource["label"] or resource["domain"]
                resource_labels.append(f"[{label}]({resource['url']})")
            lines.append(f"- hubs e literatura ja ligados ao corpus: {', '.join(resource_labels)}")
        lines.append("")

    lines.extend(
        [
            "## Produtos e familias com presenca real",
            "",
            "| Produto/familia | Marca | Notas | Citacoes |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in top_products:
        lines.append(
            f"| {item['canonical']} | {item['brand']} | `{item['note_count']}` | `{item['mention_count']}` |"
        )

    lines.extend(
        [
            "",
            "## Normas especificas citadas",
            "",
            "| Norma | Familia | Notas | Citacoes |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in top_norms:
        lines.append(
            f"| `{item['canonical']}` | {item['family']} | `{item['note_count']}` | `{item['mention_count']}` |"
        )

    lines.extend(
        [
            "",
            "## Corpos normativos mais presentes",
            "",
            "| Corpo normativo | Notas | Citacoes |",
            "| --- | --- | --- |",
        ]
    )
    for item in norm_families:
        lines.append(
            f"| {item['canonical']} | `{item['note_count']}` | `{item['mention_count']}` |"
        )

    lines.extend(
        [
            "",
            "## Sinais para ampliar a taxonomia",
            "",
            "Estes termos apareceram em links ou labels do corpus e merecem revisao manual para possivel incorporacao como `submarca`, `produto` ou `familia`.",
            "",
        ]
    )
    for candidate in bank["unmapped_candidates"][:20]:
        lines.append(
            f"- `{candidate['label']}` — `{candidate['count']}` ocorrencias"
        )

    lines.extend(
        [
            "",
            "## Leitura operacional",
            "",
            "- este banco agora vira camada estrutural para varrer o corpus sem depender de leitura manual nota a nota;",
            "- `marca` e `submarca` deixam de ser so memoria editorial e passam a ter banco proprio;",
            "- `normas citadas` passam a ser auditaveis, o que ajuda a verificar referencias como `ABYC E-11`, `ABYC A-31`, `ISO 13297`, `ISO 10133`, `NORMAM-211`, `NBR 5410` e correlatas;",
            "- o proximo passo natural e usar esse banco para montar a fila `nome -> portal oficial -> pagina de manual`, sem baixar nada ainda.",
        ]
    )

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    bank = build_bank()
    write_json(BANK_JSON_PATH, bank)
    BANK_NOTE_PATH.write_text(build_note(bank), encoding="utf-8")
    print(f"Banco JSON gerado em: {BANK_JSON_PATH}")
    print(f"Banco Markdown gerado em: {BANK_NOTE_PATH}")


if __name__ == "__main__":
    main()
