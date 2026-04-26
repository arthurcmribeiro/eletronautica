---
title: "Aplicação Piloto — Onan (Resolver Source-First)"
note_type: "inventory"
domain: "90_Revisao_Manual"
status: "active-curation"
reviewed_on: "2026-04-20"
review_jurisdiction: "Brasil"
aliases:
  - "Piloto Onan do Resolvedor"
  - "Onan Source-First"
related_notes:
  - "Portal do Acervo — Biblioteca de Referência"
  - "Preparação Source-First — Resolver de Links Oficiais"
  - "Links Confirmados — Geradores Pequenos (Onan e Rehlko)"
  - "Links Confirmados — Geradores Médios (Onan MDKDP a MDKDU)"
  - "Matriz de Modelos e Versões — Geradores"
  - "Tabela-Mestre do Acervo — Biblioteca de Referência"
---

# Aplicação Piloto — Onan (Resolver Source-First)

> [!abstract] Resumo tecnico
> Esta nota registra a primeira aplicação real do resolvedor `source-first` em um grupo pequeno do acervo. O alvo foi `Onan`, mantendo a premissa editorial `official -> secondary -> mirror` e sem baixar nenhum PDF.

## Escopo do piloto

- marca-alvo: `Onan / Cummins Onan`
- recorte documental: `operator`, `product page`, `service`, `parts`, `installation` e `archive`
- familias cobertas nesta passada:
  - `MDKBH`
  - `MDKBJ / MDKBW`
  - `MDKDK / MDKDL / MDKDM / MDKDN`
  - `MDKDP / MDKDR / MDKDS / MDKDT / MDKDU / MDKDV`
  - `QD 40-110 / MDDC`

## Artefatos desta aplicação

- fila atualizada: `90_Revisao_Manual/_Dados_Acervo/manual-resolution-queue.json`
- resultado do piloto: `90_Revisao_Manual/_Dados_Acervo/manual-resolution-results-onan.json`
- scripts usados:
  - `scripts/acervo/build_manual_resolution_queue.py`
  - `scripts/acervo/resolve_manual_links.py`

## Resultado objetivo

- candidatos totais úteis: `26`
- camada `official`: `13`
- camada `secondary`: `9`
- camada `mirror`: `4`
- `unknown`: `0`

## Leitura crítica do piloto

- o resolvedor deixou de ficar refém de `ManualsLib`;
- a ordenação agora privilegia `operador oficial` e `produto oficial` antes de qualquer espelho;
- a `Onan` ficou com `candidatos curados` por família, então o resultado continua útil mesmo quando o site oficial responde `timeout` ao crawler;
- o crawler ainda não navega bem o HTML da `Cummins`, mas isso agora não derruba a biblioteca, porque os links oficiais revisados editorialmente entram direto na fila;
- não houve download de arquivo nesta etapa.

## Mapa prático por família

| Família | Operação oficial | Produto oficial | Serviço | Parts | Installation |
| --- | --- | --- | --- | --- | --- |
| `MDKBH` | [0981-0180](https://www.cummins.fr/wp-content/uploads/2020/10/0981-0180-Issue-5-English.pdf) | [QD 4-5](https://www.cummins.com/generators/products/onan-marine-qd-45-kw-generator) | [Service](https://www.seapowermarine.com/seapowerwp/wp-content/uploads/2018/05/MDKBH-Service-Manual.pdf) | [Parts](https://www.marine-j.com/pdf/MDKBH-Parts-Manual.pdf) | [Installation](https://onan.xmsi.net/981-0647%20Onan%20MDKBH%20Spec%20A-E%20Installation%20Manual%20%2810-2013%29.pdf) |
| `MDKBJ / MDKBW` | [A029Z105](https://www.cummins.fr/wp-content/uploads/2020/10/A029Z105-Issue-5-English.pdf) | [QD 6-8](https://www.cummins.com/generators/products/onan-marine-qd-6758-kw-generator) | [Service](https://www.seapowermarine.com/seapowerwp/wp-content/uploads/2018/05/MDKBJ-BW-Service-Manual.pdf) | [Parts](https://www.seapowermarine.com/wpfd_file/mdkbj-bw-parts-manual/) | `pendente curado` |
| `MDKDK / MDKDL / MDKDM / MDKDN` | [A052J727](https://www.cummins.fr/wp-content/uploads/2020/10/A052J727-Issue-1-English.pdf) | [QD 7-9 Space Saver](https://www.cummins.com/en-na/generators/products/onan-marine-qd-79-kw-space-saver-generator) / [QD 9-13.5](https://www.cummins.com/generators/products/onan-marine-qd-9511115135-kw-generator) | [Service](https://www.seapowermarine.com/seapowerwp/wp-content/uploads/2018/05/MDKDK-DL-DM-DN-Service-Manual.pdf) | [MDKDK Parts](https://www.seapowermarine.com/wpfd_file/mdkdk-parts-manual/) / [MDKDL-DM-DN Parts](https://www.seapowermarine.com/wpfd_file/mdkdl-dm-dn-parts-manual/) | `pendente curado` |
| `MDKDP / MDKDR / MDKDV` | [A050G574 PT-BR](https://www.cummins.fr/wp-content/uploads/2020/10/A050G574-Issue-1-Portuguese-Brazil.pdf) | [QD 13.5-21.5](https://selfscreening.cummins.com/en-in/generators/onan-marine-qd-1351717519215-kw-generator) | [Service](https://www.seapowermarine.com/seapowerwp/wp-content/uploads/2018/05/MDKDP-DR-DS-DT-DU-DV-Service-Manual.pdf) | [Parts](https://www.seapowermarine.com/seapowerwp/wp-content/uploads/2018/05/MDKDP-DR-DV-Parts-Manual.pdf) | [Installation](https://bazakonkurencyjnosci.funduszeeuropejskie.gov.pl/api/files/760932) |
| `MDKDS / MDKDT / MDKDU` | [A050G574 PT-BR](https://www.cummins.fr/wp-content/uploads/2020/10/A050G574-Issue-1-Portuguese-Brazil.pdf) | [QD 22.5-29](https://selfscreening.cummins.com/generators/onan-marine-qd-2252729-kw-generator) | [Service](https://www.seapowermarine.com/seapowerwp/wp-content/uploads/2018/05/MDKDP-DR-DS-DT-DU-DV-Service-Manual.pdf) | [Parts](https://www.seapowermarine.com/seapowerwp/wp-content/uploads/2018/05/MDKDS-DT-DU-Parts-Manual.pdf) | [Installation](https://bazakonkurencyjnosci.funduszeeuropejskie.gov.pl/api/files/760932) |
| `MDDC / QD 40-110` | `pendente curado` | [QD 40-110](https://www.cummins.com/en-na/generators/products/onan-marine-qd-40-110-kw-generator) | `pendente curado` | `pendente curado` | `pendente curado` |

## O que mudou na ferramenta

- a taxonomia da `Onan` agora separa:
  - `source_layers.official`
  - `source_layers.secondary`
  - `source_layers.mirror`
- o resolvedor agora:
  - aceita `curated_candidates`;
  - registra `source_tier`;
  - ordena o resultado por camada de fonte;
  - normaliza URLs de espelho para reduzir duplicação;
  - reconhece `PDF direto` como candidato sem baixar o arquivo.

## Conclusão prática

- o piloto `Onan` já serve como modelo para aplicar a mesma lógica em `Rehlko / Kohler`, `Dometic`, `Xylem` e outras marcas-matriz;
- para esta marca, a melhor estratégia futura é continuar com:
  - `official` para `operator` e `product page`;
  - `secondary` para `service` e parte de `parts`;
  - `mirror` só para lacunas como `installation` e legado.
