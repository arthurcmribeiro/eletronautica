from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent

if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.append(str(SCRIPTS_ROOT))

from vault_tools import ROOT, write_json  # noqa: E402


TAXONOMY_PATH = SCRIPT_DIR / "acervo_taxonomy.json"
BANK_PATH = ROOT / "90_Revisao_Manual" / "_Dados_Acervo" / "brand-norm-bank.json"
QUEUE_PATH = ROOT / "90_Revisao_Manual" / "_Dados_Acervo" / "manual-resolution-queue.json"
NOTE_PATH = (
    ROOT
    / "90_Revisao_Manual"
    / "20_Matrizes_Fontes_e_Links"
    / "Preparação Source-First — Resolver de Links Oficiais.md"
)
SOURCE_TIERS = ("official", "secondary", "mirror")
MANUAL_KEYWORDS = [
    "manual",
    "manuals",
    "support",
    "download",
    "document",
    "documents",
    "guide",
    "brochure",
    "catalog",
    "catalogue",
    "resources",
    "library",
    "installation",
    "operation",
    "service",
    "parts",
    "datasheet",
]
REJECT_KEYWORDS = [
    "login",
    "cart",
    "checkout",
    "dealer",
    "privacy",
    "cookie",
    "facebook",
    "instagram",
    "linkedin",
    "youtube",
]


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def entity_by_name(items: list[dict[str, object]]) -> dict[str, dict[str, object]]:
    return {str(item["canonical"]): item for item in items}


def unique_strings(values: list[object]) -> list[str]:
    cleaned: list[str] = []
    seen: set[str] = set()

    for value in values:
        text = str(value).strip().rstrip("\"'")
        if not text or text in seen:
            continue
        seen.add(text)
        cleaned.append(text)

    return cleaned


def empty_layer() -> dict[str, list[str]]:
    return {
        "domains": [],
        "seed_urls": [],
        "resource_urls": [],
    }


def build_source_layers(
    entity: dict[str, object],
    bank_entry: dict[str, object] | None,
) -> tuple[dict[str, dict[str, list[str]]], list[str], list[str]]:
    raw_layers = entity.get("source_layers", {})
    layers = {tier: empty_layer() for tier in SOURCE_TIERS}

    if isinstance(raw_layers, dict) and raw_layers:
        for tier in SOURCE_TIERS:
            tier_payload = raw_layers.get(tier, {})
            if not isinstance(tier_payload, dict):
                continue
            layers[tier]["domains"] = unique_strings(list(tier_payload.get("domains", [])))
            layers[tier]["seed_urls"] = unique_strings(list(tier_payload.get("seed_urls", [])))
    else:
        layers["official"]["domains"] = unique_strings(list(entity.get("domains", [])))
        layers["official"]["seed_urls"] = unique_strings(list(entity.get("seed_urls", [])))

    allowed_domains = unique_strings(
        [
            domain
            for tier in SOURCE_TIERS
            for domain in layers[tier]["domains"]
        ]
    )

    if bank_entry:
        for resource in bank_entry.get("resources", []):
            url = str(resource.get("url", "")).strip().rstrip("\"'")
            domain = str(resource.get("domain", "")).lower().strip()
            if not url or not domain:
                continue

            matched_tier = ""
            for tier in SOURCE_TIERS:
                if any(layer_domain and layer_domain in domain for layer_domain in layers[tier]["domains"]):
                    matched_tier = tier
                    break

            if matched_tier:
                layers[matched_tier]["resource_urls"].append(url)

    for tier in SOURCE_TIERS:
        layers[tier]["domains"] = unique_strings(layers[tier]["domains"])
        layers[tier]["resource_urls"] = unique_strings(layers[tier]["resource_urls"])
        layers[tier]["seed_urls"] = unique_strings(layers[tier]["seed_urls"] + layers[tier]["resource_urls"])

    seed_urls = unique_strings(
        [
            url
            for tier in SOURCE_TIERS
            for url in layers[tier]["seed_urls"]
        ]
    )

    return layers, allowed_domains, seed_urls


def build_queue() -> dict[str, object]:
    taxonomy = load_json(TAXONOMY_PATH)
    bank = load_json(BANK_PATH)
    bank_brands = entity_by_name(bank["brands"])
    taxonomy_brands = entity_by_name(taxonomy["brands"])

    queue_items: list[dict[str, object]] = []

    for canonical, entity in taxonomy_brands.items():
        bank_entry = bank_brands.get(canonical)
        note_count = int(bank_entry["note_count"]) if bank_entry else 0
        mention_count = int(bank_entry["mention_count"]) if bank_entry else 0

        if note_count <= 0:
            continue

        child_entities = [
            item
            for item in bank["brands"]
            if item["parent"] == canonical and int(item["note_count"]) > 0
        ]
        related_products = [
            item
            for item in bank["products"]
            if item["brand"] == canonical and int(item["note_count"]) > 0
        ]

        aliases = unique_strings(list(entity.get("aliases", [])))
        child_aliases = unique_strings(
            [
                alias
                for child in child_entities
                for alias in child.get("aliases", [])
            ]
        )
        product_aliases = unique_strings(
            [
                alias
                for product in related_products
                for alias in product.get("aliases", [])
            ]
        )

        source_layers, allowed_domains, seed_urls = build_source_layers(entity, bank_entry)
        curated_candidates = list(entity.get("curated_candidates", []))

        queue_items.append(
            {
                "id": f"RES-{canonical.upper().replace(' ', '-').replace('&', 'AND').replace('/', '-')}",
                "canonical": canonical,
                "type": entity.get("type", "brand"),
                "parent": entity.get("parent", ""),
                "note_count": note_count,
                "mention_count": mention_count,
                "aliases": aliases,
                "child_entities": [child["canonical"] for child in child_entities],
                "child_aliases": child_aliases,
                "product_families": [product["canonical"] for product in related_products],
                "product_aliases": product_aliases,
                "allowed_domains": allowed_domains,
                "seed_urls": seed_urls[:24],
                "source_layers": source_layers,
                "curated_candidates": curated_candidates,
                "resolver_profile": {
                    "manual_keywords": MANUAL_KEYWORDS,
                    "reject_keywords": REJECT_KEYWORDS,
                    "max_depth": 2,
                    "max_seed_pages": 18,
                    "max_links_per_item": 150,
                    "allow_pdf_candidates": True,
                    "download_files": False,
                    "prefer_source_order": list(SOURCE_TIERS),
                },
                "status": "planned",
            }
        )

    queue_items.sort(key=lambda item: (-int(item["note_count"]), -int(item["mention_count"]), str(item["canonical"])))

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_bank": BANK_PATH.relative_to(ROOT).as_posix(),
        "source_taxonomy": TAXONOMY_PATH.relative_to(ROOT).as_posix(),
        "item_count": len(queue_items),
        "items": queue_items,
    }


def build_note(queue_payload: dict[str, object]) -> str:
    reviewed_on = datetime.now().date().isoformat()
    items = queue_payload["items"]
    lines = [
        "---",
        'title: "Preparação Source-First — Resolver de Links Oficiais"',
        'note_type: "inventory"',
        'domain: "90_Revisao_Manual"',
        'status: "active-curation"',
        f'reviewed_on: "{reviewed_on}"',
        'review_jurisdiction: "Brasil"',
        "aliases:",
        '  - "Fila de Resolução de Links Oficiais"',
        '  - "Preparação do Resolver de Manuais"',
        "related_notes:",
        '  - "Banco de Marcas e Normas Citadas — Corpus Integral"',
        '  - "Matriz de Fontes — Fabricantes e Repositórios"',
        '  - "Backlog Operacional — Coleta de Manuais"',
        '  - "Tabela-Mestre do Acervo — Biblioteca de Referência"',
        "---",
        "",
        "# Preparação Source-First — Resolver de Links Oficiais",
        "",
        "> [!abstract] Resumo tecnico",
        "> Esta nota expõe a fila preparada para o resolvedor Python de links oficiais. Ela não baixa nenhum arquivo: apenas define quais marcas, submarcas e famílias devem ser visitadas no futuro para localizar `pagina de manual`, `hub de downloads`, `document library`, `catálogo técnico` e `PDF direto`.",
        "",
        "> [!info] Geração",
        "> Comando: `python scripts/acervo/build_manual_resolution_queue.py`.",
        f"> Gerado em `{queue_payload['generated_at']}`.",
        "",
        "## Resumo",
        "",
        f"- itens na fila: `{queue_payload['item_count']}`",
        "- política desta camada: `acessar, classificar e ligar`; `não baixar`",
        "- hierarquia-base: `official -> secondary -> mirror`",
        "",
        "## Como essa fila deve ser usada",
        "",
        "1. atualizar o banco com `python scripts/acervo/build_brand_norm_bank.py`;",
        "2. regenerar a fila com `python scripts/acervo/build_manual_resolution_queue.py`;",
        "3. quando a etapa de coleta estiver autorizada, rodar `python scripts/acervo/resolve_manual_links.py`;",
        "4. revisar resultados antes de qualquer download.",
        "",
        "## Primeiros itens prontos para resolução futura",
        "",
        "| Item | Tipo | Notas | Produtos/famílias | Seeds | Curados | Camadas |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]

    for item in items[:25]:
        active_layers = sum(1 for tier in SOURCE_TIERS if item["source_layers"][tier]["domains"] or item["source_layers"][tier]["seed_urls"])
        lines.append(
            f"| {item['canonical']} | {item['type']} | `{item['note_count']}` | `{len(item['product_families'])}` | `{len(item['seed_urls'])}` | `{len(item['curated_candidates'])}` | `{active_layers}` |"
        )

    lines.extend(["", "## Observações operacionais", ""])
    for item in items[:12]:
        child_entities = ", ".join(f"`{name}`" for name in item["child_entities"][:8]) or "-"
        products = ", ".join(f"`{name}`" for name in item["product_families"][:8]) or "-"
        curated = ", ".join(f"`{candidate['document_type']}`" for candidate in item["curated_candidates"][:6]) or "-"
        official_seeds = ", ".join(f"[seed]({url})" for url in item["source_layers"]["official"]["seed_urls"][:4]) or "-"
        lines.append(f"### {item['canonical']}")
        lines.append("")
        lines.append(f"- child entities: {child_entities}")
        lines.append(f"- produtos/famílias: {products}")
        lines.append(f"- seeds oficiais: {official_seeds}")
        lines.append(f"- candidatos curados: {curated}")
        lines.append("")

    lines.extend(
        [
            "## Premissas travadas nesta camada",
            "",
            "- o resolvedor futuro pode visitar páginas HTML e registrar PDFs ou páginas candidatas, mas não deve baixar documentos automaticamente;",
            "- `catálogo`, `brochure`, `guide`, `document library` e `support page` continuam entrando como pistas de acervo, não só `manual` puro;",
            "- submarcas históricas continuam vivas na fila para evitar erro de busca em portal rebatizado;",
            "- quando o site oficial bloquear o crawler, a fila pode expor `curated_candidates` e `seed_urls` oficiais já revisados editorialmente.",
        ]
    )

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    payload = build_queue()
    write_json(QUEUE_PATH, payload)
    NOTE_PATH.write_text(build_note(payload), encoding="utf-8")
    print(f"Fila gerada em: {QUEUE_PATH}")
    print(f"Nota gerada em: {NOTE_PATH}")


if __name__ == "__main__":
    main()
