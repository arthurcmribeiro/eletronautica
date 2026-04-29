---
title: "Fundamentos da Elétrica Náutica"
note_type: "moc"
domain: "00_Mapas"
source_file: "FUNDAMENTOS DA ELETRICA NÁUTICA 1e419734f7fb80f9abe4d621dcf45570.md"
status: "moc-curated-plus"
fase_6_reescrita: 135
reviewed_on: "2026-04-29"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
review_level: "moc-curated-plus"
aliases:
  - "FUNDAMENTOS DA ELETRICA NÁUTICA"
  - "Mapa central da elétrica náutica"
  - "Hub de estudo principal"
seo_title: "Fundamentos da elétrica náutica: trilha mestre de estudo, projeto, diagnóstico e segurança"
seo_description: "Hub central da vault de elétrica náutica brasileira. Trilhas de estudo, projeto, diagnóstico e operação + arquitetura por domínios + norma mestre estrutural + padrão DEC-11."
seo_keywords:
  - "fundamentos elétrica náutica"
  - "trilha estudo elétrica marine"
  - "moc elétrica náutica brasil"
  - "DEC-11 premium-l3"
  - "Brasil-primeiro elétrica"
geo_queries:
  - "Por onde começar a estudar elétrica náutica?"
  - "Qual a trilha de estudo recomendada?"
  - "Como projetar instalação elétrica em barco?"
  - "Como diagnosticar falha elétrica em embarcação?"
  - "Quais são as notas críticas para comissionar barco?"
normas_citadas: []
related_notes:
  - "Atlas Técnico"
  - "MOC — Mapas"
  - "MOC — Trilha do Iniciante"
  - "MOC — Trilha do Projetista"
  - "MOC — Trilha do Diagnosticador"
  - "MOC — Trilha de Operação"
  - "Normas e Regulamentações — Abyc Iso e Brasil"
  - "Lei de Ohm e Cálculos Básicos"
  - "Princípios Náuticos"
---

# Fundamentos da Elétrica Náutica

> [!abstract] Sobre este hub
> Esta página é o **mapa central de estudo** da vault. Diferente do [[Atlas Técnico]] (visão administrativa), aqui está a **trilha de aprendizado em 5 camadas** — pensada para você dominar elétrica náutica do conceito ao retrofit. Use como cardápio: percorra na ordem se está começando, ou pule para a camada relevante se já tem base.

> [!tip] Decisão rápida — qual camada hoje?
> - **Nunca toquei em elétrica de barco:** Camada 1 (Conceitos)
> - **Sei elétrica residencial, mas barco é diferente:** Camada 2 (Adaptação ao marine)
> - **Vou projetar / dimensionar:** Camada 3 (Projeto)
> - **Vou diagnosticar / consertar:** Camada 4 (Diagnóstico)
> - **Vou comissionar / operar:** Camada 5 (Operação)
> - **Vou ensinar:** todas + visuais em `_visuals/generated/`

## Camada 1 — Conceitos fundamentais (vocabulário base)

Antes de qualquer coisa, dominar vocabulário e relações de base.

| # | Nota | Tier | Por que ler |
|---|------|------|-------------|
| 1 | [[Princípios Náuticos]] | 🔧 A | Vocabulário marine + classificação + ambiente agressivo + corrosão galvânica |
| 2 | [[Tipos de Embarcação]] | 🔧 A | Recreio × comercial × SOLAS × mega-iate — define regime regulatório |
| 3 | [[Lei de Ohm e Cálculos Básicos]] | 🔧 A | V=I×R + Kirchhoff + queda de tensão + AC vs DC + RMS |
| 4 | [[DC vs AC — Corrente Contínua e Alternada]] | ⚡ S | Diferenças críticas em barco (frequência, RMS, harmônicas, segurança) |
| 5 | [[Fase e Neutro]] | ⚡ S | AC marine — sistemas derivados, split-phase, neutro flutuante |
| 6 | [[Neutro, Negativo, Terra, PE, Bonding e DR — Diferenças Críticas]] | ⚡ S | Erro #1 do eletricista residencial em barco: confundir esses 6 conceitos |
| 7 | [[Simbologia Elétrica Náutica]] | 🔧 A | IEC 60617 × ANSI 315 × ABNT NBR 5444 — leitura de diagrama |

## Camada 2 — Adaptação ao ambiente marine

Após a Camada 1, você sabe **eletricidade**. Agora aprenda **eletricidade no barco**.

| Nota | Tier | Por que ler |
|------|------|-------------|
| [[Cabeamento Náutico]] | 🔧 A | Tinned copper, UL 1426 BC5W2, IEC 60092-353 — não é cabo automotivo |
| [[Bonding — Sistema de Interligação de Massas]] | ⚡ S | ABYC E-11.16 — interligação previne corrosão galvânica |
| [[Aterramento]] | ⚡ S | Em barco "terra" não é estaca enterrada — é casco/bonding/shore-PE |
| [[Correntes Parasitas — Stray Currents]] | ⚡ S | Fuga DC + casco metálico = corrosão acelerada → morte do casco |
| [[Eletrólise]] | 🔧 A | Diferenciar eletrólise × galvânica × stray currents |
| [[Anôdo]] | ⚡ S | Zinco/Al/Mg sacrificial protege hélice/eixos/leme |
| [[Inspeção de Cabos Terminais e Conexões]] | ⚡ S | Crimpagem calibrada × solda — ABYC E-11.13 |

## Camada 3 — Projeto e dimensionamento

Você sabe os fundamentos. Agora dimensione um sistema completo.

### Arquitetura

- [[Projeto Elétrico de Embarcação — Passo a Passo]] (⚡ S) — workflow completo
- [[Diagrama Unifilar — Documentação do Sistema Elétrico]] (⚡ S) — documentação obrigatória
- [[Leitura de Diagramas e Esquemas Elétricos]] (🔧 A) — interpretar diagramas existentes

### Cálculo

- [[Dimensionamento de Cabos DC — Cálculo Prático]] (⚡ S) — bitola por queda (ABYC E-11.4)
- [[Dimensionamento de Banco de Baterias — Cálculo de Autonomia]] (⚡ S) — Ah × tempo × DOD × inversor
- [[Lei de Ohm e Cálculos Básicos]] (🔧 A) — base matemática

### Decisão de equipamento

- [[Tipos de Bateria]] (⚡ S) — chumbo × AGM × Gel × LFP × NiMH
- [[Bancos de Bateria]] (⚡ S) — partida × serviço, paralelo × série
- [[Carregador de Bateria (AC To DC)]] (⚡ S) — multi-stage, AC-DC topology
- [[Inversora (DC To AC)]] (⚡ S) — pure sine wave, fator de potência, dimensionamento VA
- [[CAIS (Pier) (AC)]] (⚡ S) — interface marina (NEC Article 555 + IEC 60364-7-709)
- [[Isolador Galvânico - Transformador de Isolamento]] (⚡ S) — isolação correta
- [[Quadro Elétrico e Painel de Distribuição AC-DC]] (🔧 A) — distribuição central

### Norma e conformidade

- [[Normas e Regulamentações — Abyc Iso e Brasil]] (⚡ S) — **norma mestre estrutural** (340+ docs)
- [[Referência Rápida — Valores de Campo]] (🔧 A) — cheat sheet operacional

## Camada 4 — Diagnóstico e troubleshooting

Sistema instalado, algo dá problema. Trilha de detetive elétrico.

| # | Nota | Tier | Quando usar |
|---|------|------|-------------|
| 1 | [[Troubleshooting — Diagnóstico de Falhas Elétricas]] | ⚡ S | Método estruturado — sempre comece aqui |
| 2 | [[Multímetro e Instrumentos de Medição]] | ⚡ S | Ferramenta primária + categoria CAT II/III/IV |
| 3 | [[Voltímetro - Amperímetro (DC e AC)]] | ⚡ S | Medições críticas + True RMS |
| 4 | [[Ferramentas do Eletricista Náutico]] | 🔧 A | Toolkit completo (Fluke + Hioki + Knipex + EPI) |
| 5 | [[Inspeção de Cabos Terminais e Conexões]] | ⚡ S | Diagnóstico empírico — termômetro IR + visual |
| 6 | [[Manutenção Preventiva Elétrica — Checklist]] | ⚡ S | Antes de virar problema |

**Trilha específica de diagnóstico:** [[MOC — Trilha do Diagnosticador]].

## Camada 5 — Operação e manutenção

Barco em uso — rotina segura.

- [[Manutenção Preventiva Elétrica — Checklist]] (⚡ S) — checklist trimestral/semestral/anual
- [[Bancos de Bateria]] + [[Monitor de Bateria - BMV - Shunt]] — gerenciamento de banco
- [[Carregador de Bateria (AC To DC)]] + [[Inversora (DC To AC)]] — fluxo AC↔DC
- [[Detector de CO — Monóxido de Carbono]] (⚡ S) — risco a vida
- [[Detector de Gás GLP - GN]] (⚡ S) — risco explosão
- [[Alarme de Alagamento - Sensor de Porão]] (⚡ S) — risco afundamento
- [[Extintor Automático — Combate a Incêndio na Casa de Máquinas]] (⚡ S) — risco fogo
- [[Iluminação de Emergência a Bordo]] (⚡ S) — IEC 60598-2-22 + IMO MSC.81(70)

**Trilha específica de operação:** [[MOC — Trilha de Operação]].

## Cross-references — entrar em outros domínios

| Para | Vá para |
|------|---------|
| Geração de energia | [[MOC — Energia e Conversao]] |
| Distribuição AC/DC + proteção | [[MOC — Distribuicao Protecao e Aterramento]] |
| Navegação eletrônica | [[MOC — Navegacao Instrumentacao e Comunicacao]] |
| Iluminação | [[MOC — Iluminacao e Sinalizacao]] |
| Automação de bordo | [[MOC — Automacao Conectividade e Monitoramento]] |
| Hidráulica / climatização / sanitário | [[MOC — Hidraulica Climatizacao e Utilidades]] |
| Segurança e corrosão | [[MOC — Seguranca e Corrosao]] |
| Acervo de PDFs | [[MOC — Revisao Manual]] |

## Hubs transversais

- [[Atlas Técnico]] — visão administrativa
- [[MOC — Diagnóstico e Manutenção]] — troubleshooting + manutenção
- [[MOC — Segurança Integrada]] — risco elétrico + alarme + porão + corrosão
- [[MOC — Trilha de Operação]] — rotina de uso, pré-saída, pernoite e retorno
- [[Guia da Vault Curada]] — manual editorial de uso

## Quick-reference — top 6 dúvidas

1. **Pode usar cabo automotivo no barco?** NÃO. Vide [[Cabeamento Náutico]].
2. **Bonding × Aterramento × PE — qual é qual?** [[Neutro, Negativo, Terra, PE, Bonding e DR — Diferenças Críticas]].
3. **Como dimensionar fusível?** 125% da nominal. [[Fusíveis DC — Proteção Contra Sobrecorrente]] + [[Lei de Ohm e Cálculos Básicos]].
4. **Que norma seguir no Brasil?** ABNT NBR 14728 + DPC NORMAM (211 amador / 201 comercial). [[Normas e Regulamentações — Abyc Iso e Brasil]].
5. **Quando transformador de isolamento?** Em marina com topologia variável (típico BR). [[Isolador Galvânico - Transformador de Isolamento]].
6. **Como começar troubleshooting?** [[Troubleshooting — Diagnóstico de Falhas Elétricas]].

## Glossário rápido (termos básicos)

- **AC × DC:** corrente alternada × contínua. Barco usa ambos.
- **CCA / MCA / RC:** Cold/Marine Cranking Amps / Reserve Capacity (SAE J537).
- **DOD:** Depth of Discharge (FLA 50%, LFP 80%).
- **ELCI / GFCI / DR:** diferenciais (30 mA marine / 5 mA pessoa / equiv. BR).
- **Bonding:** ABYC E-11.16 — interligação de massas.
- **PE:** Protective Earth (verde-amarelo) — diferente de bonding.
- **Tinned copper:** cobre estanhado — padrão marine.
- **Pure sine wave:** onda senoidal verdadeira (inversor premium).
- **NMEA 0183 / 2000:** padrões de instrumentação.
- **IP code:** Ingress Protection (IEC 60529).

## Quando NÃO entrar aqui

- **Valor específico de campo** → [[Referência Rápida — Valores de Campo]]
- **Citar norma agora** → [[Normas e Regulamentações — Abyc Iso e Brasil]]
- **Resolver problema agora** → [[Troubleshooting — Diagnóstico de Falhas Elétricas]]
- **Manual OEM de equipamento** → [[MOC — Revisao Manual]]

## Perguntas que esta página responde

- Por onde começar a estudar elétrica náutica?
- Qual a trilha de estudo recomendada?
- Como projetar instalação elétrica em barco?
- Como diagnosticar falha elétrica em embarcação?
- Quais são as notas críticas para comissionar barco?
- Em que ordem ler os domínios, hubs e trilhas principais?
- Como mapear conceitos de elétrica residencial para marine?
