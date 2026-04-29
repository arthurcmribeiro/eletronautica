---
title: "Preparação Source-First — Resolver de Links Oficiais"
note_type: "inventory"
domain: "90_Revisao_Manual"
status: "active-curation"
reviewed_on: "2026-04-28"
review_jurisdiction: "Brasil"
aliases:
  - "Fila de Resolução de Links Oficiais"
  - "Preparação do Resolver de Manuais"
related_notes:
  - "Banco de Marcas e Normas Citadas — Corpus Integral"
  - "Matriz de Fontes — Fabricantes e Repositórios"
  - "Backlog Operacional — Coleta de Manuais"
  - "Tabela-Mestre do Acervo — Biblioteca de Referência"
---

# Preparação Source-First — Resolver de Links Oficiais

> [!abstract] Resumo tecnico
> Esta nota expõe a fila preparada para o resolvedor Python de links oficiais. Ela não baixa nenhum arquivo: apenas define quais marcas, submarcas e famílias devem ser visitadas no futuro para localizar `pagina de manual`, `hub de downloads`, `document library`, `catálogo técnico` e `PDF direto`.

> [!info] Geração
> Comando: `python scripts/acervo/build_manual_resolution_queue.py`.
> Gerado em `2026-04-29T01:39:33.049748+00:00`.

## Resumo

- itens na fila: `52`
- política desta camada: `acessar, classificar e ligar`; `não baixar`
- hierarquia-base: `official -> secondary -> mirror`

## Como essa fila deve ser usada

1. atualizar o banco com `python scripts/acervo/build_brand_norm_bank.py`;
2. regenerar a fila com `python scripts/acervo/build_manual_resolution_queue.py`;
3. quando a etapa de coleta estiver autorizada, rodar `python scripts/acervo/resolve_manual_links.py`;
4. revisar resultados antes de qualquer download.

## Primeiros itens prontos para resolução futura

| Item | Tipo | Notas | Produtos/famílias | Seeds | Curados | Camadas |
| --- | --- | --- | --- | --- | --- | --- |
| Onan | subbrand | `127` | `2` | `24` | `26` | `3` |
| Cummins | brand | `127` | `0` | `15` | `0` | `1` |
| Quick | brand | `83` | `5` | `10` | `0` | `1` |
| Dometic | brand | `43` | `3` | `12` | `0` | `1` |
| Kohler Marine | subbrand | `41` | `2` | `14` | `0` | `1` |
| Rehlko | brand | `41` | `0` | `13` | `0` | `1` |
| Victron Energy | brand | `40` | `6` | `12` | `0` | `1` |
| Garmin | brand | `40` | `0` | `10` | `0` | `1` |
| Raymarine | brand | `31` | `0` | `5` | `0` | `1` |
| Cruisair | subbrand | `23` | `0` | `12` | `0` | `1` |
| Furuno | brand | `21` | `0` | `5` | `0` | `1` |
| Mastervolt | brand | `20` | `2` | `7` | `0` | `1` |
| H-Tec | brand | `19` | `0` | `1` | `0` | `1` |
| Blue Sea Systems | brand | `17` | `0` | `5` | `0` | `1` |
| Simrad | brand | `16` | `0` | `7` | `0` | `1` |
| ACR | brand | `16` | `2` | `5` | `0` | `1` |
| Starlink | brand | `15` | `0` | `6` | `0` | `1` |
| Xantrex | brand | `14` | `2` | `7` | `0` | `1` |
| Marinco | brand | `14` | `0` | `4` | `0` | `1` |
| B&G | brand | `13` | `7` | `12` | `0` | `1` |
| Mabru | brand | `12` | `2` | `5` | `0` | `1` |
| Rule | subbrand | `12` | `2` | `12` | `0` | `1` |
| Jabsco | subbrand | `11` | `3` | `13` | `0` | `1` |
| Xylem | brand | `11` | `0` | `13` | `0` | `1` |
| Standard Horizon | brand | `11` | `0` | `4` | `0` | `1` |

## Observações operacionais

### Onan

- child entities: -
- produtos/famílias: `MDK`, `QD`
- seeds oficiais: [seed](https://www.cummins.fr/onanmanuel/), [seed](https://www.cummins.com/generators/marine/resources), [seed](https://www.cummins.com/en-na/generators/marine-generators/onan-marine-generators), [seed](https://www.cummins.com/generators/products/onan-marine-qd-45-kw-generator)
- candidatos curados: `operator-hub`, `product-line`, `product-page`, `product-page`, `product-page`, `product-page`

### Cummins

- child entities: `Onan`
- produtos/famílias: -
- seeds oficiais: [seed](https://www.cummins.com/generators/marine/resources), [seed](https://www.cummins.com/support/manuals?locset=US), [seed](https://www.cummins.com/en-na/generators/marine-generators/onan-marine-generators), [seed](https://www.cummins.fr/onanmanuel/)
- candidatos curados: -

### Quick

- child entities: -
- produtos/famílias: `QNN`, `QCC`, `LDIM`, `HDIM`, `ZDIM`
- seeds oficiais: [seed](https://www.quickitaly.com/en/manuals/), [seed](https://www.quickitaly.com/en/products/quick-marine-lighting/control-systems-and-accessories/dimmers/hdim-300-plus/), [seed](https://www.quickitaly.com/en/products/quick-marine-lighting/control-systems-and-accessories/dimmers/zdim-100/), [seed](https://www.quickitaly.com/en/products/quick-marine-lighting/control-systems-and-accessories/qcc-system/)
- candidatos curados: -

### Dometic

- child entities: `Cruisair`, `Marine Air`, `Condaria`, `Optimus`, `SeaStar`, `Xtreme`, `BayStar`
- produtos/famílias: `ECD`, `MasterFlush`, `VacuFlush`
- seeds oficiais: [seed](https://www.dometic.com/en-us/lp/marinelp-dometic-marine), [seed](https://www.dometic.com/globalassets/1-outdoor/out-category-pages/climate--comfort/air-conditioners/dometic-marine-ac-guide-2023.pdf), [seed](https://www.dometic.com/globalassets/1-outdoor/out-buying-guides/boat-toilets/dometic-marine-sanitation-guide-202363.pdf?ref=ACB369A871), [seed](https://www.dometic.com/en-us/product/dometic-optimus-link-9620017870)
- candidatos curados: -

### Kohler Marine

- child entities: -
- produtos/famílias: `EFKOD`, `EKOZD`
- seeds oficiais: [seed](https://www.marine.rehlko.com/), [seed](https://www.manualslib.com/brand/kohler.html), [seed](https://www.manualslib.com/manual/1071277/Kohler-6ekod.html), [seed](https://www.manualslib.com/manual/1196255/Kohler-6ekod.html)
- candidatos curados: -

### Rehlko

- child entities: `Kohler Marine`
- produtos/famílias: -
- seeds oficiais: [seed](https://www.marine.rehlko.com/), [seed](https://www.marine.rehlko.com/brochures-literature), [seed](https://resources.rehlko.com/marine/PDF/PocketGuide.pdf), [seed](https://www.marine.rehlko.com/product/5efkod)
- candidatos curados: -

### Victron Energy

- child entities: -
- produtos/famílias: `BMV`, `SmartShunt`, `MultiPlus`, `Quattro`, `Cerbo GX`, `SmartSolar`
- seeds oficiais: [seed](https://www.victronenergy.com/support-and-downloads/manuals), [seed](https://www.victronenergy.com/media/pg/VRM_Portal_manual/en/index-en.html), [seed](https://www.victronenergy.com/batteries/lithium-battery-12-8v/), [seed](https://www.victronenergy.com/chargers/blue-smart-ip22-charger)
- candidatos curados: -

### Garmin

- child entities: -
- produtos/famílias: -
- seeds oficiais: [seed](https://support.garmin.com/marine/), [seed](https://support.garmin.com/en-US/?identifier=3326298033&tab=manuals), [seed](https://support.garmin.com/en-US/?identifier=561671&tab=manuals), [seed](https://support.garmin.com/en-US/?identifier=877856&tab=manuals)
- candidatos curados: -

### Raymarine

- child entities: -
- produtos/famílias: -
- seeds oficiais: [seed](https://www.raymarine.com/en-us/support/document-library), [seed](https://www.raymarine.com/en-us/download/evolution-autopilot-manuals), [seed](https://www.raymarine.com/en-us/download/quantum-radar-manuals), [seed](https://www.raymarine.com/en-us/download/axiom-axiom-manuals)
- candidatos curados: -

### Cruisair

- child entities: -
- produtos/famílias: -
- seeds oficiais: [seed](https://www.dometic.com/en-us/lp/marinelp-dometic-marine), [seed](https://www.dometic.com/globalassets/1-outdoor/out-category-pages/climate--comfort/air-conditioners/dometic-marine-ac-guide-2023.pdf), [seed](https://www.dometic.com/en-us/lp/rebranded-cruisair), [seed](https://www.dometic.com/globalassets/1-outdoor/out-buying-guides/boat-toilets/dometic-marine-sanitation-guide-202363.pdf?ref=ACB369A871)
- candidatos curados: -

### Furuno

- child entities: -
- produtos/famílias: -
- seeds oficiais: [seed](https://furunousa.com/en/knowledge_base/general/manuals_for_furuno_products), [seed](https://furunousa.com/en/support/gp1971f), [seed](https://www.furunousa.com/en/support/drs4dnxt), [seed](https://www.furunousa.com/en/support/sc50)
- candidatos curados: -

### Mastervolt

- child entities: -
- produtos/famílias: `Mass Combi`, `ChargeMaster`
- seeds oficiais: [seed](https://www.mastervolt.com/downloads/), [seed](https://www.mastervolt.com/country/us/product/5910/), [seed](https://www.mastervolt.com/downloads/6905), [seed](https://www.mastervolt.com/products/ac-master-12v/ac-master-12-700-120-v/)
- candidatos curados: -

## Premissas travadas nesta camada

- o resolvedor futuro pode visitar páginas HTML e registrar PDFs ou páginas candidatas, mas não deve baixar documentos automaticamente;
- `catálogo`, `brochure`, `guide`, `document library` e `support page` continuam entrando como pistas de acervo, não só `manual` puro;
- submarcas históricas continuam vivas na fila para evitar erro de busca em portal rebatizado;
- quando o site oficial bloquear o crawler, a fila pode expor `curated_candidates` e `seed_urls` oficiais já revisados editorialmente.
