---
title: "MOC — Baterias e Armazenamento"
note_type: "moc"
domain: "20_Baterias_e_Armazenamento"
status: "moc-curated-plus"
fase_6_reescrita: 108
reviewed_on: "2026-04-29"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
review_level: "moc-curated-plus"
seo_title: "MOC Baterias: chumbo × AGM × Gel × LiFePO4, BMS, banco partida × serviço, BMV, carregador multi-stage"
seo_description: "Hub do domínio 20: 6 notas premium-l3 sobre tipos de bateria (FLA/AGM/Gel/LFP/NiMH), bancos (partida × serviço, série × paralelo), BMS, lítio LiFePO4, monitor BMV/shunt e carregador AC-DC multi-stage. ABYC E-10/E-11/E-13, SAE J537, BCI Group."
seo_keywords:
  - "bateria náutica"
  - "banco de bateria marine"
  - "BMS LiFePO4"
  - "monitor de bateria BMV"
  - "carregador multi-stage"
  - "ABYC E-10 E-13"
geo_queries:
  - "Qual bateria escolher para meu barco?"
  - "Lítio LiFePO4 vale a pena no marine?"
  - "Como dimensionar banco de bateria?"
  - "BMS é obrigatório em LiFePO4?"
  - "Como instalar BMV/shunt corretamente?"
normas_citadas: []
related_notes:
  - "Atlas Técnico"
  - "Fundamentos da Elétrica Náutica"
  - "Dimensionamento de Banco de Baterias — Cálculo de Autonomia"
---

# MOC — Baterias e Armazenamento

> [!abstract] Sobre este domínio
> Domínio **20_Baterias_e_Armazenamento** cobre **armazenamento de energia DC**: tipos de bateria (chumbo-ácido / AGM / Gel / LiFePO4 / NiMH), arquitetura de bancos (partida × serviço, série × paralelo), gerenciamento (BMS) e monitoramento (BMV/shunt) + recarga (carregador multi-stage AC-DC). **Vir aqui** para escolher química, dimensionar banco, projetar BMS, configurar monitor ou retrofitar para lítio. **6 notas, todas Tier S premium-l3.**

> [!tip] Trilhas de leitura
> - **Iniciante:** [[Tipos de Bateria]] → [[Bancos de Bateria]] → [[Monitor de Bateria - BMV - Shunt]]
> - **Projetando banco novo:** [[Dimensionamento de Banco de Baterias — Cálculo de Autonomia]] → [[Tipos de Bateria]] → [[Bancos de Bateria]] → [[Carregador de Bateria (AC To DC)]]
> - **Migrando para lítio:** [[Lítio LiFePO4 — Instalação e Cuidados Específicos]] → [[BMS — Battery Management System]] → [[Carregador de Bateria (AC To DC)]]
> - **Diagnosticando consumo/autonomia:** [[Monitor de Bateria - BMV - Shunt]] → [[Bancos de Bateria]]

## Notas por categoria

### Escolha da química (1)

- [[Tipos de Bateria]] — ⚡ S — FLA × AGM × Gel × LFP × NiMH × NiCd, DOD, ciclos, eficiência, custo TCO

### Arquitetura do banco (2)

- [[Bancos de Bateria]] — ⚡ S — partida × serviço, série × paralelo, isolation (ACR/VSR/diodo/FET/DC-DC)
- [[Lítio LiFePO4 — Instalação e Cuidados Específicos]] — ⚡ S — thermal runaway, BMS, comissionamento, ABYC E-13

### Gerenciamento (1)

- [[BMS — Battery Management System]] — ⚡ S — proteção células, balanceamento, comm CAN, integração inversor

### Monitoramento (1)

- [[Monitor de Bateria - BMV - Shunt]] — ⚡ S — Victron BMV-712 / SmartShunt, SoC, histórico, integração VRM

### Recarga (1)

- [[Carregador de Bateria (AC To DC)]] — ⚡ S — multi-stage (Bulk-Absorption-Float-Equalization), perfil chumbo × LFP

## Cross-domain links

| Para | Vá para |
|------|---------|
| Cálculo de autonomia (Ah × tempo) | [[Dimensionamento de Banco de Baterias — Cálculo de Autonomia]] (em [[MOC — Fundamentos e Projeto]]) |
| Geração (alternador, solar, eólica) | [[MOC — Energia e Conversao]] |
| Inversora (DC→AC) | [[Inversora (DC To AC)]] |
| Distribuição DC + barramento + chave geral | [[MOC — Distribuicao Protecao e Aterramento]] |
| Monitoramento remoto (telemetria) | [[Monitoramento Remoto — VRM - Telemetria]] (em [[MOC — Automacao Conectividade e Monitoramento]]) |
| Bateria de partida (motor) | [[Arranque]] (em [[MOC — Energia e Conversao]]) |
| Banco do tender / jet ski | [[Carregador Elétrico para Tender e Jet Ski]] (em [[MOC — Energia e Conversao]]) |

## Quick-reference — top 5 dúvidas

1. **AGM × LFP — qual escolher?** → [[Tipos de Bateria]] (LFP: 3-5× ciclos, 2× custo, 30% mais leve, 80% DOD vs 50%).
2. **Partida × serviço no mesmo banco?** → NÃO. [[Bancos de Bateria]] (banco dedicado preserva CCA + isola cargas standby).
3. **BMS é obrigatório em LFP?** → SIM. [[BMS — Battery Management System]] (proteção thermal runaway + balanceamento).
4. **Como medir SoC corretamente?** → [[Monitor de Bateria - BMV - Shunt]] (BMV/shunt em série com negativo, calibração inicial 100% após carga completa).
5. **Tensão de flutuação correta?** → Chumbo 13.5-13.8V; LFP NÃO pode ficar em float alto contínuo (carregador específico). [[Carregador de Bateria (AC To DC)]].

## Glossário rápido (termos do domínio)

- **FLA (Flooded Lead-Acid):** chumbo-ácido inundado tradicional.
- **AGM (Absorbed Glass Mat):** chumbo absorvido em fibra de vidro.
- **Gel:** chumbo gelatinoso.
- **LFP / LiFePO4:** lithium iron phosphate (química lítio mais segura).
- **NiMH:** Nickel Metal Hydride.
- **DOD:** Depth of Discharge — % descarga máxima recomendada.
- **SoC:** State of Charge — % de carga atual.
- **CCA / MCA / RC:** Cold/Marine Cranking Amps + Reserve Capacity (SAE J537).
- **Ah:** Amp-hour — capacidade.
- **C-rate:** taxa de carga/descarga (1C = capacidade nominal em 1h).
- **BMS:** Battery Management System.
- **BMV:** Battery Monitor Victron.
- **Shunt:** resistor de baixíssima resistência para medir corrente.
- **ACR / VSR:** Automatic Charging Relay / Voltage Sensitive Relay.
- **Bulk / Absorption / Float / Equalization:** estágios do carregador multi-stage.
- **ABYC E-10:** Storage Batteries.
- **ABYC E-11:** AC and DC Electrical Systems on Boats.
- **ABYC E-13:** Lithium Ion Batteries.
- **BCI Group:** Battery Council International (24/27/31/4D/8D — tamanhos padrão).
- **UN 38.3:** transporte de lítio (IATA/IMDG).

## Quando NÃO entrar aqui

- **Como instalar carregador shore-power** → [[CAIS (Pier) (AC)]] (em [[MOC — Energia e Conversao]])
- **Inversor DC→AC** → [[Inversora (DC To AC)]]
- **Painel solar / eólico (geração DC)** → [[MOC — Energia e Conversao]]
- **Cabo de bateria + crimpagem** → [[Cabeamento Náutico]] (em [[MOC — Distribuicao Protecao e Aterramento]])
- **Disjuntor / fusível do banco** → [[MOC — Distribuicao Protecao e Aterramento]]
- **Manual OEM da bateria** → [[MOC — Revisao Manual]]

## Perguntas que esta página responde

- Qual bateria escolher para meu barco?
- Lítio LiFePO4 vale a pena no marine?
- Como dimensionar banco de bateria?
- BMS é obrigatório em LiFePO4?
- Como instalar BMV/shunt corretamente?
- Posso misturar baterias velhas com novas?
- Como configurar carregador multi-stage para LFP?
