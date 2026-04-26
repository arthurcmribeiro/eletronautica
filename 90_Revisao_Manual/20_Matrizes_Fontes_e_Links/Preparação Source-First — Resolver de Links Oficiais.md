---
title: "Preparação Source-First — Resolver de Links Oficiais"
note_type: "inventory"
domain: "90_Revisao_Manual"
status: "active-curation"
reviewed_on: "2026-04-26"
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
> Gerado em `2026-04-26T07:56:35.629939+00:00`.

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
| Victron Energy | brand | `25` | `6` | `12` | `0` | `1` |
| Garmin | brand | `20` | `0` | `10` | `0` | `1` |
| Cummins | brand | `18` | `0` | `15` | `0` | `1` |
| Onan | subbrand | `17` | `2` | `24` | `26` | `3` |
| Quick | brand | `16` | `5` | `10` | `0` | `1` |
| Starlink | brand | `15` | `0` | `6` | `0` | `1` |
| Mastervolt | brand | `15` | `2` | `7` | `0` | `1` |
| ACR | brand | `15` | `2` | `5` | `0` | `1` |
| Simrad | brand | `14` | `0` | `7` | `0` | `1` |
| Raymarine | brand | `14` | `0` | `5` | `0` | `1` |
| Dometic | brand | `13` | `3` | `12` | `0` | `1` |
| Rehlko | brand | `13` | `0` | `13` | `0` | `1` |
| B&G | brand | `13` | `7` | `12` | `0` | `1` |
| Kohler Marine | subbrand | `12` | `2` | `14` | `0` | `1` |
| Blue Sea Systems | brand | `12` | `0` | `5` | `0` | `1` |
| Rule | subbrand | `11` | `2` | `12` | `0` | `1` |
| Xylem | brand | `10` | `0` | `13` | `0` | `1` |
| Charles Industries | brand | `10` | `1` | `4` | `0` | `1` |
| H-Tec | brand | `10` | `0` | `1` | `0` | `1` |
| Furuno | brand | `10` | `0` | `5` | `0` | `1` |
| Lumitec | brand | `10` | `2` | `6` | `0` | `1` |
| Marine Air | subbrand | `10` | `0` | `12` | `0` | `1` |
| VETUS | brand | `9` | `2` | `9` | `0` | `1` |
| Jabsco | subbrand | `9` | `3` | `13` | `0` | `1` |
| Mabru | brand | `9` | `2` | `5` | `0` | `1` |

## Observações operacionais

### Victron Energy

- child entities: -
- produtos/famílias: `BMV`, `SmartShunt`, `MultiPlus`, `Cerbo GX`, `Quattro`, `SmartSolar`
- seeds oficiais: [seed](https://www.victronenergy.com/support-and-downloads/manuals), [seed](https://www.victronenergy.com/media/pg/VRM_Portal_manual/en/index-en.html), [seed](https://www.victronenergy.com/batteries/lithium-battery-12-8v/), [seed](https://www.victronenergy.com/chargers/blue-smart-ip22-charger)
- candidatos curados: -

### Garmin

- child entities: -
- produtos/famílias: -
- seeds oficiais: [seed](https://support.garmin.com/marine/), [seed](https://support.garmin.com/en-US/?identifier=3326298033&tab=manuals), [seed](https://support.garmin.com/en-US/?identifier=561671&tab=manuals), [seed](https://support.garmin.com/en-US/?identifier=877856&tab=manuals)
- candidatos curados: -

### Cummins

- child entities: `Onan`
- produtos/famílias: -
- seeds oficiais: [seed](https://www.cummins.com/generators/marine/resources), [seed](https://www.cummins.com/support/manuals?locset=US), [seed](https://www.cummins.com/en-na/generators/marine-generators/onan-marine-generators), [seed](https://www.cummins.fr/onanmanuel/)
- candidatos curados: -

### Onan

- child entities: -
- produtos/famílias: `MDK`, `QD`
- seeds oficiais: [seed](https://www.cummins.fr/onanmanuel/), [seed](https://www.cummins.com/generators/marine/resources), [seed](https://www.cummins.com/en-na/generators/marine-generators/onan-marine-generators), [seed](https://www.cummins.com/generators/products/onan-marine-qd-45-kw-generator)
- candidatos curados: `operator-hub`, `product-line`, `product-page`, `product-page`, `product-page`, `product-page`

### Quick

- child entities: -
- produtos/famílias: `QNN`, `QCC`, `LDIM`, `HDIM`, `ZDIM`
- seeds oficiais: [seed](https://www.quickitaly.com/en/manuals/), [seed](https://www.quickitaly.com/en/products/quick-marine-lighting/control-systems-and-accessories/dimmers/hdim-300-plus/), [seed](https://www.quickitaly.com/en/products/quick-marine-lighting/control-systems-and-accessories/dimmers/zdim-100/), [seed](https://www.quickitaly.com/en/products/quick-marine-lighting/control-systems-and-accessories/qcc-system/)
- candidatos curados: -

### Starlink

- child entities: -
- produtos/famílias: -
- seeds oficiais: [seed](https://www.starlink.com/), [seed](https://starlink.com/us/residential/installation), [seed](https://www.starlink.com/us/roam), [seed](https://www.starlink.com/business/maritime)
- candidatos curados: -

### Mastervolt

- child entities: -
- produtos/famílias: `Mass Combi`, `ChargeMaster`
- seeds oficiais: [seed](https://www.mastervolt.com/downloads/), [seed](https://www.mastervolt.com/country/us/product/5910/), [seed](https://www.mastervolt.com/downloads/6905), [seed](https://www.mastervolt.com/products/ac-master-12v/ac-master-12-700-120-v/)
- candidatos curados: -

### ACR

- child entities: -
- produtos/famílias: `ResQLink`, `GlobalFix`
- seeds oficiais: [seed](https://www.acrartex.com/support/), [seed](https://www.acrartex.com/wp-content/uploads/downloads/774/Product_Manual_GlobalFix_Pro_ACR.pdf), [seed](https://www.acrartex.com/wp-content/uploads/downloads/947/USA_Product_Manual_ResQLink__ACR.pdf), [seed](https://www.acrartex.com/products/globalfix-pro-epirb)
- candidatos curados: -

### Simrad

- child entities: -
- produtos/famílias: -
- seeds oficiais: [seed](https://www.simrad-yachting.com/help--support/service-and-support/), [seed](https://www.simrad-yachting.com/en-eu/nss-evo3s/), [seed](https://www.simrad-yachting.com/en-gb/simrad/type/compasses/hs70-gps-compass/), [seed](https://www.simrad-yachting.com/en-nz/simrad/type/autopilots/autopilot-controllers/ap44-rotary-pilot-head/)
- candidatos curados: -

### Raymarine

- child entities: -
- produtos/famílias: -
- seeds oficiais: [seed](https://www.raymarine.com/en-us/support/document-library), [seed](https://www.raymarine.com/en-us/download/axiom-axiom-manuals), [seed](https://www.raymarine.com/en-us/download/evolution-autopilot-manuals), [seed](https://www.raymarine.com/en-us/download/quantum-radar-manuals)
- candidatos curados: -

### Dometic

- child entities: `Marine Air`, `Cruisair`, `Condaria`, `Optimus`, `SeaStar`, `Xtreme`, `BayStar`
- produtos/famílias: `ECD`, `MasterFlush`, `VacuFlush`
- seeds oficiais: [seed](https://www.dometic.com/en-us/lp/marinelp-dometic-marine), [seed](https://www.dometic.com/globalassets/1-outdoor/out-category-pages/climate--comfort/air-conditioners/dometic-marine-ac-guide-2023.pdf), [seed](https://www.dometic.com/globalassets/1-outdoor/out-buying-guides/boat-toilets/dometic-marine-sanitation-guide-202363.pdf?ref=ACB369A871), [seed](https://www.dometic.com/en-us/product/dometic-optimus-link-9620017870)
- candidatos curados: -

### Rehlko

- child entities: `Kohler Marine`
- produtos/famílias: -
- seeds oficiais: [seed](https://www.marine.rehlko.com/), [seed](https://www.marine.rehlko.com/brochures-literature), [seed](https://resources.rehlko.com/marine/PDF/PocketGuide.pdf), [seed](https://www.marine.rehlko.com/product/5efkod)
- candidatos curados: -

## Premissas travadas nesta camada

- o resolvedor futuro pode visitar páginas HTML e registrar PDFs ou páginas candidatas, mas não deve baixar documentos automaticamente;
- `catálogo`, `brochure`, `guide`, `document library` e `support page` continuam entrando como pistas de acervo, não só `manual` puro;
- submarcas históricas continuam vivas na fila para evitar erro de busca em portal rebatizado;
- quando o site oficial bloquear o crawler, a fila pode expor `curated_candidates` e `seed_urls` oficiais já revisados editorialmente.
