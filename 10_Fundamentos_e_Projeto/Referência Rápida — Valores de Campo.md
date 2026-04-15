---
title: "Referência Rápida — Valores de Campo"
note_type: "reference"
domain: "10_Fundamentos_e_Projeto"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "Valores de Campo"
  - "Tabela rápida de referência"
seo_title: "Referência rápida de valores de campo na elétrica náutica"
seo_description: "Tabela compacta com valores típicos de campo para tensão, queda de tensão, correntes, cabos e verificações rápidas em elétrica náutica, com cautela explícita sobre uso prático versus uso normativo."
geo_queries:
  - "Quais valores de campo ajudam no diagnóstico elétrico náutico?"
  - "Quais tensões e referências rápidas devo usar em elétrica náutica?"
related_notes:
  - "Dimensionamento de Cabos DC — Cálculo Prático"
  - "Dimensionamento de Banco de Baterias — Cálculo de Autonomia"
  - "Normas e Regulamentações — Abyc Iso e Brasil"
  - "MOC — Diagnóstico e Manutenção"
---

# Referência Rápida — Valores de Campo

> [!abstract] Resumo técnico
> Esta nota reúne valores típicos para triagem, medição e conversa de campo. Não substitui cálculo formal, folha de dados do fabricante nem leitura da norma aplicável; serve para orientação rápida e auditável.

## Como usar esta nota

- Use como referência de triagem e não como norma automática.
- Sempre reconfirme com:
  - química da bateria;
  - fabricante do equipamento;
  - topologia do sistema;
  - contexto de carga, repouso e temperatura.

## Tensões de referência — sistema DC 12 V

| Condição | Valor típico |
| --- | --- |
| Chumbo-ácido em repouso, banco cheio | `12,6–12,8 V` |
| Chumbo-ácido em repouso, ~50% SoC | `~12,2 V` |
| Chumbo-ácido em repouso, banco muito baixo | `11,8–12,0 V` |
| Em carga normal com alternador/carregador | `13,8–14,4 V` |
| Float típico | `13,2–13,6 V` |
| LiFePO4 em carga plena | `13,6–14,4 V` |

## Tensões de referência — sistema AC no Brasil

| Parâmetro | Valor de referência |
| --- | --- |
| Frequência nominal | `60 Hz` |
| Rede monofásica mais comum | `127 V` ou `220 V` |
| Faixa prática para 220 V com tolerância aproximada de ±10% | `198–242 V` |
| Faixa prática para 127 V com tolerância aproximada de ±10% | `115–140 V` |

## Queda de tensão — referência rápida

| Circuito | Queda máxima de referência |
| --- | --- |
| Iluminação, instrumentação e circuitos críticos | `3%` |
| Circuitos de conforto e cargas menos críticas | `10%` |
| Partida do motor | verificar projeto e fabricante; usar como meta conservadora `4%` para o circuito completo |

## Correntes típicas — sistema 12 V

| Equipamento | Faixa típica |
| --- | --- |
| Geladeira DC | `3–8 A` |
| Bomba de água pressurizada | `4–8 A` |
| Bomba de porão | `3–10 A` |
| VHF transmitindo | `5–6 A` |
| Chartplotter / MFD | `1–4 A` |
| Inversor de 1.000 W em carga alta | `~90 A` |
| Thruster | `80–250 A` |
| Guincho de âncora | `50–200 A` |
| Arranque do motor | `200–600 A` |

## Cabos DC — referência de conversa rápida

| Corrente máxima | Comprimento total ida + volta | Faixa inicial de seção |
| --- | --- | --- |
| até `20 A` | até `3 m` | `4 mm²` |
| até `20 A` | `3–5 m` | `6 mm²` |
| até `40 A` | até `3 m` | `6 mm²` |
| até `40 A` | `3–6 m` | `10 mm²` |
| até `100 A` | até `2 m` | `25 mm²` |
| até `100 A` | `2–4 m` | `35 mm²` |
| acima de `100 A` | sempre calcular | usar [[Dimensionamento de Cabos DC — Cálculo Prático]] |

## Proteção — posicionamento prático

| Item | Referência rápida |
| --- | --- |
| Fusível próximo à bateria | o mais perto possível do positivo |
| Proteção do circuito | dimensionar para o cabo, não só para a carga |
| Trechos de alta corrente | minimizar comprimento, conexões e pontos de aquecimento |

## Cautelas importantes

- Tensão em repouso só faz sentido após repouso suficiente.
- Durante carga ou descarga, tensão não equivale a SoC real.
- Em LiFePO4, voltímetro simples não substitui monitor com shunt.
- Qualquer tabela rápida deve ser revalidada quando:
  - a química muda;
  - o equipamento é importado;
  - o sistema é 24 V / 48 V;
  - a frequência ou a topologia AC saem do caso usual.

## Integração com outras notas

- [[Dimensionamento de Cabos DC — Cálculo Prático]]
- [[Dimensionamento de Banco de Baterias — Cálculo de Autonomia]]
- [[Tipos de Bateria]]
- [[Voltímetro - Amperímetro (DC e AC)]]
- [[MOC — Diagnóstico e Manutenção]]
