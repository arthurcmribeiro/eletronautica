---
title: "Matriz Dometic — Subgrupos, Linhas e Documentos"
note_type: "inventory"
domain: "90_Revisao_Manual"
status: "active-curation"
reviewed_on: "2026-04-19"
review_jurisdiction: "Brasil"
aliases:
  - "Matriz Dometic"
  - "Dometic Marine — Subgrupos e Documentos"
related_notes:
  - "MOC — Revisao Manual"
  - "Matriz de Fontes — Fabricantes e Repositórios"
  - "Matriz de Marcas Matriz — Ecossistemas e Subgrupos"
  - "Backlog Operacional — Coleta de Manuais"
  - "Acervo de Manuais — Marcas e Modelos Prioritários"
---

# Matriz Dometic — Subgrupos, Linhas e Documentos

> [!abstract] Resumo técnico
> Nesta matriz, `Dometic` é tratada como marca-matriz. `Cruisair`, `Condaria` e `Marine Air` entram como linhas históricas reabsorvidas, não como blocos principais de organização. O objetivo é deixar a coleta mais racional por `subgrupo atual > linha/família > documento`.

## Regra de organização adotada

- `Dometic` é a marca principal de busca;
- `Cruisair`, `Condaria` e `Marine Air` devem ser lidas como aliases históricos dentro do ecossistema de climatização;
- quando houver documentação atual sob Dometic e documentação legada sob nome histórico, as duas devem ser cruzadas;
- para Dometic, vale separar obrigatoriamente:
  - climatização;
  - displays e controles;
  - bombas;
  - steering / marine control;
  - sanitário e holding tanks;
  - conforto e galley.

## Aliases históricos que precisam ser normalizados

| Nome encontrado no mercado | Leitura correta na coleta | Base oficial |
| --- | --- | --- |
| Cruisair | linha histórica dentro de `Dometic Marine` | [Cruisair is now Dometic](https://www.dometic.com/en-us/lp/rebranded-cruisair) |
| Condaria | linha histórica dentro de `Dometic Marine`, com forte viés de chilled water | [Condaria is now Dometic](https://www.dometic.com/en-us/lp/condaria-rebranding-page) |
| Marine Air | linha histórica dentro de `Dometic Marine`, ligada a self-contained e chilled water | [Marine Air is now Dometic](https://www.dometic.com/en-us/outdoor/lp/rebranded-marine-air) |

## Subgrupos atuais do ecossistema Dometic

| Subgrupo principal | Linhas / famílias visíveis | O que coletar | Fonte oficial |
| --- | --- | --- | --- |
| Climatização marinha | `GT`, `GTX`, `GVTX`, `ECD`, `DCU`, `DLU`, `DTG`, `TX`, `VARCX`, `DEGX`, fan coils, air handlers | installation, operation, service, troubleshooting, specs e guides | [Marine Air Conditioners](https://www.dometic.com/en-us/outdoor/boat/marine-air-conditioners) |
| Displays, controles e painéis de climatização | `ECD digital control`, touchscreen de chiller, PGD1 legado quando aparecer em campo | instalação, operação, setup, painel, alarmes e interface | [Dometic ECD](https://www.dometic.com/en-us/outdoor/boat/marine-air-conditioners/dometic-ecd-75055) / [Touch-screen control](https://www.dometic.com/en-us/article/dometic-introduces-new-touch-screen-control) |
| Bombas de climatização | `MagDrive P030`, `P045`, `P062`, `P075`, `P100`, `P137`, `P150`, `P200` | instalação, operação, folha técnica, manutenção | [Dometic MagDrive Pump](https://www.dometic.com/en-us/outdoor/boat/marine-air-conditioners/marine-climate-water-pumps/dometic-magdrive-pump-328692) |
| Marine Control e steering | `SeaStar`, `BayStar`, `Optimus`, `Xtreme`, `Interact Drive`, electronic controls, mechanical controls, jack plates, trim tabs | instalação, operação, setup, calibração, service, brochures | [Marine Control](https://www.dometic.com/en-us/outdoor/boat/marine-control) / [Marine Steering Systems](https://www.dometic.com/en-us/outdoor/boat/marine-steering-systems) |
| Displays de steering / marine control | `Optimus Link`, `Optimus EPS Color Display ED1700`, `ED1800` | instalação, configuração, operação e troubleshooting | [Displays](https://www.dometic.com/en-us/outdoor/boat/marine-control/displays) |
| Sanitário e holding | `MasterFlush`, toilettes, holding tanks & pumps, tratamentos e peças | instalação, operação, parts guide, troubleshooting, reposição | [Dometic Marine Partner Resources](https://www.dometic.com/en-us/lp/marinelp-dometic-marine) |
| Conforto e galley | `boat refrigerators`, `cooktops`, `stoves`, `sinks`, `blinds` | installation, operation e product literature | [Dometic Marine Partner Resources](https://www.dometic.com/en-us/lp/marinelp-dometic-marine) |

## Climatização — quebra operacional

| Faixa | Subitem | Exemplo de linha / detalhe | Observação operacional |
| --- | --- | --- | --- |
| Self-contained water cooled | unidades compactas | `ECD`, `GT`, `GTX`, `GVTX`, `DCU`, `DLU` | melhor ponto de entrada para barcos médios e refit |
| Split-gas water cooled | condensadora + evaporadora remota | `DEGX`, remote condensers / evaporators | importante em instalações mais distribuídas |
| Chilled water systems | chillers e rede de distribuição | `VARCX`, `Condaria` legado, air handlers, fan coils | aqui `Condaria` aparece como alias histórico, não como categoria independente |
| Bombas | circulação de água de climatização | `MagDrive P030-P200` | subgrupo próprio; não deve ficar escondido dentro de “AC” |
| Displays / painéis | interface do usuário e setup | `ECD digital control`, chiller touch screen, PGD1 legado | útil demais para diagnóstico de campo |
| Acessórios e parts | filtros, caixas elétricas, peças | parts guides e literatura técnica | importante para manutenção e retrofit |

## Steering e Marine Control — quebra operacional

| Faixa | Subitem | Exemplo visível no portal | Observação operacional |
| --- | --- | --- | --- |
| Steering eletrônica | `Optimus EPS` | cilindros e ecossistema EPS | forte incidência em integração e calibração |
| Steering hidráulica / mecânica | `SeaStar`, `BayStar`, `Xtreme` | cilindros, helms, cabos e kits | catálogo muito amplo; precisa de recorte por família |
| Displays | `Optimus Link`, `ED1700`, `ED1800` | telas e interface de steering | subgrupo próprio de display/painel |
| Electronic controls | atuadores e controles eletrônicos | `i7700`, `SeaStar i7800 Dual` e correlatos no portal | agrupar por interface e comando |
| Jack plates e trim tabs | acessórios de performance e comando | `Xtreme Jack Plate` e correlatos | úteis em lanchas rápidas e setups de outboard |

## Documentos e catálogos oficiais úteis

| Documento / portal | Tipo | Valor prático | URL |
| --- | --- | --- | --- |
| Dometic Marine Partner Resources | portal-mãe | manuals, marketing & sales tools, climate parts guide, sanitation replacement parts guide e system builder | [Partner Resources](https://www.dometic.com/en-us/lp/marinelp-dometic-marine) |
| Dometic Marine AC Guide 2023 | guia / catálogo técnico | resume tipos de sistema, arquitetura e seleção de AC marinho | [Marine AC Guide PDF](https://www.dometic.com/globalassets/1-outdoor/out-category-pages/climate--comfort/air-conditioners/dometic-marine-ac-guide-2023.pdf) |
| Dometic Marine Sanitation Guide | guia / catálogo técnico | útil para toilets, holding tanks e dimensionamento de sanitário | [Marine Sanitation Guide PDF](https://www.dometic.com/globalassets/1-outdoor/out-buying-guides/boat-toilets/dometic-marine-sanitation-guide-202363.pdf?ref=ACB369A871) |
| Marine Air Conditioners | catálogo navegável por categoria | mostra famílias, subtipos e links de produto | [Marine Air Conditioners](https://www.dometic.com/en-us/category/boat/marine-air-conditioners) |
| Marine Control | catálogo navegável por categoria | mostra steering, controls, displays, trim tabs e jack plates | [Marine Control](https://www.dometic.com/en-us/outdoor/boat/marine-control) |
| Displays | catálogo navegável de displays | isola `Optimus Link`, `ED1700`, `ED1800` | [Displays](https://www.dometic.com/en-us/outdoor/boat/marine-control/displays) |
| Spare Parts Information | suporte de reposição | importante para organizar acervo por `SKU/PNC` | [Spare Parts Information](https://www.dometic.com/en-us/support/spare-parts-information) |

## Consultas prontas para busca

- `Dometic ECD installation manual`
- `Dometic GVTX service manual`
- `Dometic VARCX installation guide`
- `Dometic MagDrive P100 manual`
- `Dometic Optimus Link manual`
- `Dometic ED1700 setup`
- `Cruisair legacy control manual Dometic`
- `Condaria chilled water manual Dometic`

## Próxima passada recomendada

1. Abrir uma matriz específica de `Dometic climate controls, displays e pumps`.
2. Desdobrar o steering em `SeaStar`, `BayStar`, `Optimus` e `Xtreme`.
3. Separar depois uma camada só de `catálogos e buying guides` da Dometic, útil para consulta rápida e orçamento.
