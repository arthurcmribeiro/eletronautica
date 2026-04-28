---
title: "Referência Rápida — Valores de Campo"
note_type: "reference"
domain: "10_Fundamentos_e_Projeto"
status: "premium-l3"
fase_6_reescrita: 100
reviewed_on: "2026-04-26"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
normas_citadas:
  - "ABYC E-11 (AC and DC Electrical Systems on Boats)"
  - "ABYC E-11.4 (Wire sizing)"
  - "ABYC E-11.4.4.1.b (Queda de tensão ≤3%)"
  - "ABYC E-11.5 (Overcurrent protection)"
  - "ABYC E-11.5.4 (Fusível ≤7 polegadas da bateria)"
  - "ABYC E-11.11.1.5 (GFCI 5 mA)"
  - "ABYC E-11.11.1.6 (ELCI 30 mA)"
  - "ABYC E-11.16 (Bonding)"
  - "ABYC H-22 (Bilge pumps)"
  - "ABYC TE-04 (Lightning protection)"
  - "IEC 60364-7-709 (Marinas)"
  - "IEC 60092-507 (Pleasure craft)"
  - "ISO 13297 (AC installations)"
  - "ISO 28848 (DC installations)"
  - "ISO 21487 (Fuel tanks)"
  - "ISO 8849 (Bilge pumps)"
  - "ABNT NBR 14728 (Embarcações de recreio)"
  - "ABNT NBR 5410 (Instalações BT)"
  - "DPC NORMAM-211/DPC"
  - "DPC NORMAM-201/DPC"
  - "DPC NORMAM-08/DPC"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://webstore.iec.ch/publication/2697"
review_level: "engineering-curated"
aliases:
  - "Valores de Campo"
  - "Tabela rápida de referência"
  - "Cheat sheet elétrica náutica"
  - "Marine electrical quick reference"
  - "Field values reference"
seo_title: "Referência rápida — valores de campo elétrica náutica: ABYC E-11, IEC, ABNT, tabelas DC + AC + cabo + fusível + bonding"
seo_description: "Cheat sheet técnico premium da elétrica náutica: tensões DC (12/24/48V), tensões AC (110/220/380V), queda de tensão ABYC E-11.4 ≤3%, dimensionamento de cabo (AWG × mm² × ampacidade × queda), fusível ABYC E-11.5 (125% nominal), bonding E-11.16, ELCI 30mA, GFCI 5mA, ânodo > 50% trocar, isolação >100MΩ, valores típicos por aplicação."
seo_keywords:
  - "cheat sheet elétrica náutica"
  - "tabela rápida marine"
  - "ABYC E-11 valores"
  - "queda tensão 3%"
  - "AWG vs mm²"
  - "fusível 125%"
  - "ELCI 30mA"
  - "isolação 100MΩ"
  - "ânodo 50%"
  - "Beaufort knots"
geo_queries:
  - "Tabela completa de valores típicos elétrica náutica?"
  - "Queda de tensão máxima ABYC?"
  - "AWG para 30A em 12V a 5 metros?"
  - "Fusível para macerador 12V/22A?"
  - "ELCI vs GFCI: qual valor de disparo?"
  - "Tensão flutuação banco chumbo-ácido?"
  - "Resistência de bonding aceitável?"
  - "Ânodo: % consumido para trocar?"
  - "Beaufort wind force scale?"
  - "Isolação cabo náutico mínima?"
related_notes:
  - "Lei de Ohm e Cálculos Básicos"
  - "Princípios Náuticos"
  - "Tipos de Embarcação"
  - "Simbologia Elétrica Náutica"
  - "Leitura de Diagramas e Esquemas Elétricos"
  - "DC vs AC — Corrente Contínua e Alternada"
  - "Fase e Neutro"
  - "Diagrama Unifilar — Documentação do Sistema Elétrico"
  - "Dimensionamento de Cabos DC — Cálculo Prático"
  - "Dimensionamento de Banco de Baterias — Cálculo de Autonomia"
  - "Cabeamento Náutico"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Disjuntores (DC) e (AC)"
  - "Bonding — Sistema de Interligação de Massas"
  - "Bancos de Bateria"
  - "Multímetro e Instrumentos de Medição"
  - "Voltímetro - Amperímetro (DC e AC)"
  - "Manutenção Preventiva Elétrica — Checklist"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
  - "Inspeção de Cabos Terminais e Conexões"
---

# Referência Rápida — Valores de Campo

> [!abstract] Resumo técnico
> Esta nota é o **cheat sheet técnico** consolidando valores de referência usados frequentemente em projeto, instalação, manutenção e troubleshooting de elétrica náutica — **DC e AC, marine-grade, padrões USA + Internacional + Europa + Brasil**. Não substitui leitura das normas; é guia de campo para acelerar dimensionamento e diagnóstico. **Sempre verificar contra norma específica para situação não-trivial**. Os valores aqui consolidados vêm de **ABYC E-11 + IEC 60364 + IEC 60092-507 + ISO 13297 + ISO 28848 + ABNT NBR 14728 + ABNT NBR 5410 + DPC NORMAM-201/211**.

> [!tldr] TL;DR — 9 regras inegociáveis
> 1. **Queda de tensão ≤3% sob carga** (ABYC E-11.4.4.1.b) — critério marine universal.
> 2. **Fusível dimensionado a 125% da corrente nominal** (ABYC E-11.5).
> 3. **Fusível ≤7 polegadas** (≤180 mm) da bateria (ABYC E-11.5.4).
> 4. **Bonding (E-11.16)** com cabo verde-amarelo AWG 8 mínimo até barramento.
> 5. **ELCI (Equipment Leakage Circuit Interrupter) 30 mA / 100 ms** em circuito AC marine (ABYC E-11.11.1.6).
> 6. **GFCI (Ground Fault Circuit Interrupter) 5 mA** em áreas molhadas (ABYC E-11.11.1.5).
> 7. **Ânodo a substituir antes de >50%** consumido (vide [[Ânodo]]).
> 8. **Isolação de cabo > 100 MΩ** (vs casco/water — Megger test).
> 9. **Resistência de bonding ≤ 0,01 Ω** entre massa metálica e barramento (ABYC E-11.16).

> [!danger] Cenários de risco em uso de "regra de bolso"
> - **Confiar em "regra de bolso" sem confirmar norma específica** em situação crítica → erro de projeto. **Prevenção:** este cheat sheet é GUIA, não substitui norma.
> - **Padrões diferentes em USA × UE × BR** podem causar dimensionamento errado quando misturado: AWG (USA) vs mm² (UE) vs IEC vs ABYC.
> - **Marca / modelo específico tem datasheet próprio** que sobrepõe regra de bolso.
> - **Mudança de norma (ABYC anual, ISO revisões)** — tabela aqui pode estar defasada.

## TENSÕES DC (marine)

| Sistema | Tensão nominal | Plena carga | Flutuação chumbo-ácido | Bulk LiFePO4 | Vazio |
|---------|----------------|--------------|--------------------------|---------------|-------|
| **6V** | 6,0 V | 6,8-7,2 | 6,8-7,1 | — | <5,8 |
| **12V** | 12,0 V | 14,4-14,7 | 13,5-13,8 | 13,8-14,4 (LFP) | <11,8 |
| **24V** | 24,0 V | 28,8-29,4 | 27,0-27,6 | 27,6-28,8 (LFP) | <23,6 |
| **48V** | 48,0 V | 57,6-58,8 | 54,0-55,2 | 55,2-57,6 (LFP) | <47,2 |

## TENSÕES AC (shore-power + gerador)

| Sistema | Single/Trifásico | Frequência | Aplicação |
|---------|-------------------|-------------|-----------|
| **110V (USA)** | Single 110-120V | 60 Hz | USA marina |
| **220V (UE/BR)** | Single 220-230V | 50 Hz UE / 60 Hz BR | EU/BR marina |
| **220V/127V (Brasil split)** | 2 fases + neutro | 60 Hz | BR com fase-neutro 127V + fase-fase 220V |
| **220V trifásico (BR)** | 3 fases sem neutro | 60 Hz | Comercial / mega-iate |
| **380V trifásico (BR/UE)** | 3 fases + neutro | 50/60 Hz | Mega-iate / comercial |
| **480V trifásico (USA)** | 3 fases | 60 Hz | Comercial USA |

## QUEDA DE TENSÃO (ABYC E-11.4.4.1.b)

```
ΔV = 2 × L × I × ρ / S
```

- L = comprimento (m); I = corrente (A); ρ_cobre = 1,72×10⁻⁸ Ω·m; S = seção (m²).
- **Critério ABYC marine: ΔV ≤ 3% sob carga** (5% para circuito não-crítico de iluminação).

### Tabela rápida AWG × comprimento máximo (12V, ΔV 3%)

| Bitola | Seção | I=10A | I=20A | I=30A | I=50A | I=100A |
|--------|-------|-------|-------|-------|-------|--------|
| AWG 16 | 1,3 mm² | 1,5 m | 0,8 m | — | — | — |
| AWG 14 | 2,1 mm² | 2,5 m | 1,2 m | 0,8 m | — | — |
| AWG 12 | 3,3 mm² | 4,0 m | 2,0 m | 1,3 m | 0,8 m | — |
| AWG 10 | 5,3 mm² | 6,0 m | 3,0 m | 2,0 m | 1,2 m | — |
| AWG 8 | 8,4 mm² | 9,5 m | 4,8 m | 3,2 m | 1,9 m | 0,9 m |
| AWG 6 | 13,3 mm² | 15 m | 7,5 m | 5,0 m | 3,0 m | 1,5 m |
| AWG 4 | 21,2 mm² | 24 m | 12 m | 8,0 m | 4,8 m | 2,4 m |
| AWG 2 | 33,6 mm² | 38 m | 19 m | 13 m | 7,5 m | 3,8 m |
| AWG 1/0 | 53,5 mm² | 60 m | 30 m | 20 m | 12 m | 6,0 m |
| AWG 2/0 | 67,4 mm² | 75 m | 38 m | 25 m | 15 m | 7,5 m |

> **Em 24V, multiplicar comprimento por 2; em 48V, por 4** (mesma queda absoluta = % menor).

## DIMENSIONAMENTO DE FUSÍVEL (ABYC E-11.5)

- **Corrente nominal × 125%** = fusível padrão.
- **Slow-Blow** para motor (suporta partida 5-10× nominal).
- **Fast-Blow** para eletrônica.
- **ANL/MIDI/ATC** marine para alta corrente DC.
- **<7 polegadas (180 mm) da bateria** ABYC E-11.5.4.

### Fusíveis típicos por corrente

| Carga | Tipo | Fusível |
|-------|------|---------|
| Iluminação LED 1A | Fast-Blow | 1-2 A |
| Bomba água pressurizada 6A | Fast-Blow | 7,5-10 A |
| Bomba banheiro 15A | Slow-Blow | 20 A ANL |
| Macerador 22A | Slow-Blow | 30 A ANL |
| Anchor windlass 100A | Slow-Blow | 125-150 A ANL |
| Inversor 1500W em 12V | Slow-Blow | 200 A MEGA |
| Bus principal 200A | Slow-Blow | 250 A ANL ou MRBF |

## DISJUNTORES E PROTEÇÃO

| Tipo | Função | Disparo | Notas |
|------|--------|---------|-------|
| **MCB Tipo B** | Curva B (3-5× In) | Residencial | Pouco usado em marine |
| **MCB Tipo C** | Curva C (5-10× In) | Iluminação geral | AC general |
| **MCB Tipo D** | Curva D (10-20× In) | Motor | Partida motor AC |
| **GFCI 5 mA / 25 ms** | Proteção pessoa | Áreas molhadas | ABYC E-11.11.1.5 |
| **ELCI 30 mA / 100 ms** | Equipment leakage | Geral marine | ABYC E-11.11.1.6 |
| **DR 30 mA / 200 ms** | Diferencial residencial | BR (NBR 5410) | Aplicável marine |
| **MRBF / Class T** | High-current DC | Banco bateria | Próximo ao polo |

## CABOS NÁUTICOS

| Padrão | Construção | Aplicação |
|--------|------------|-----------|
| **UL 1426 BC5W2** | Tinned copper, isolação CSPE | USA marine |
| **IEC 60092-353** | Tinned copper, EPDM/PVC | Internacional marine |
| **SAE J1127** | Tinned copper, marine engine | Battery / motor cable |
| **SAE J1128** | SXL/GXL automotivo (NÃO marine) | Cuidado: não-tinned |
| **IEC 60228 Classes 1-6** | Stranded copper | 1=solid, 6=fino-fino |

## ISOLAÇÃO

- **Megger test mínimo:** > 100 MΩ entre condutor e casco / massa (instalação nova: > 1 GΩ).
- **<1 MΩ:** isolação degradada — investigar.
- **<100 kΩ:** falha — substituir.

## BONDING (ABYC E-11.16)

| Condutor | Cor | Bitola mínima |
|----------|-----|----------------|
| Bonding wire | Verde-amarelo (BR) ou verde (USA) | AWG 8 (8,4 mm²) |
| Resistência bonding entre massa e barramento | — | ≤ 0,01 Ω |
| Resistência bonding entre 2 massas | — | ≤ 1 Ω |

## ÂNODOS (vide [[Ânodo]])

| Material | Aplicação | Vida útil típica | Substituir |
|----------|-----------|------------------|-------------|
| Zinco (Zn) | Mar (água salgada) | 1-3 anos | > 50% consumido |
| Alumínio (Al) | Mar + salobra | 1-3 anos | > 50% consumido |
| Magnésio (Mg) | Água doce / lago | 6-18 meses | > 50% consumido |

## REFERENCE Ag/AgCl ELECTRODE (medição de potencial)

| Material | Potencial (mV vs Ag/AgCl) | Status |
|----------|----------------------------|--------|
| Magnésio | -1.500 a -1.700 | Anódico |
| Zinco | -1.000 a -1.050 | Anódico (referência) |
| Alumínio | -1.000 a -1.150 | Anódico |
| Aço galvanizado | -1.000 a -1.100 | Anódico |
| Aço carbono | -550 a -750 | Catódico (sem proteção) |
| Aço carbono protegido | -800 a -900 | Catódico protegido |
| Bronze | -200 a -350 | Catódico |
| Aço inox 316L passivado | -50 a -150 | Catódico |
| Cobre | +50 a -50 | Catódico |

> **Critério ABYC: aço carbono protegido entre -850 e -1.100 mV vs Ag/AgCl.**

## BANCO DE BATERIA (vide [[Bancos de Bateria]] + [[Tipos de Bateria]])

| Química | DOD máximo recomendado | Ciclos típicos | Eficiência |
|---------|--------------------------|------------------|-------------|
| Chumbo-ácido (FLA) | 50% | 300-500 | 75-80% |
| AGM | 50% (até 80% emergência) | 500-1000 | 85-90% |
| Gel | 50% | 500-700 | 80-85% |
| LiFePO4 | 80% (até 100%) | 3000-5000+ | 95-99% |
| NiCd | 80% | 1500-2000 | 65-70% |
| NiMH | 80% | 500-1000 | 70-75% |

## DIMENSIONAMENTO DE BANCO (vide [[Dimensionamento de Banco de Baterias — Cálculo de Autonomia]])

```
Ah_necessário = Σ (W × h × η_inversor) / V × 1/(1 - DOD)
```

- η_inversor: 0,85-0,95 (LFP), 0,80-0,90 (chumbo).
- DOD: 0,5 (chumbo), 0,8 (LFP).

### Margem prática:
- **+25% para imprevistos.**
- **Ah real ≈ 80% do nominal** após anos.

## INVERSOR

| Tipo | Eficiência | Aplicação |
|------|------------|-----------|
| Pure sine wave | 88-95% | Eletrônica sensível, motor |
| Modified sine | 85-90% | Cargas resistivas (em desuso) |
| Auto-transfer (ATS) | — | Shore vs gerador vs inversor |

### Dimensionamento:
- **VA contínuo** = soma de cargas com PF.
- **VA pico** = motor de partida (LRA × V) + carga base.
- **Margem 30%.**

## CARREGADOR DE BATERIA (multi-stage)

| Estágio | Tensão (banco 12V chumbo) | Função |
|---------|----------------------------|---------|
| Bulk | 14,4-14,7 V | Carga rápida até 80% |
| Absorption | 14,4-14,7 V (corrente cai) | Top off 80-100% |
| Float | 13,5-13,8 V | Manutenção indefinida |
| Equalization | 15,5-16,0 V | Mensal (FLA only) |

### Para LiFePO4:
- Bulk: 13,8-14,4 V
- Float: 13,4-13,6 V (não pode ficar em float alto contínuo)
- Sem equalization.

## CONSUMO TÍPICO DE CARGAS DC (12V)

| Carga | Corrente típica |
|-------|-----------------|
| LED leitura | 0,1-0,5 A |
| LED salão | 0,2-1,0 A |
| Bomba pressurizada (intermitente) | 5-15 A |
| Geladeira 12V (média) | 2-4 A (compressor) |
| Bomba de porão automática | 2-5 A |
| Macerador | 15-25 A |
| Anchor windlass | 80-150 A |
| Bow thruster | 200-400 A |
| Inversor 1500W em uso médio | 100-150 A DC |
| Autopilot em mar moderado | 5-12 A |
| Chartplotter MFD | 1-5 A |
| Ar-condicionado 12V (raro) | 30-60 A |
| Geladeira AC 110V via inversor (50 W) | ~5 A DC |
| Iluminação cabine LED total | 2-8 A |

## BEAUFORT WIND SCALE

| Bft | Vento (knots) | Vento (km/h) | Mar | Descrição |
|-----|----------------|---------------|------|-----------|
| 0 | <1 | <1 | Liso | Calmaria |
| 1 | 1-3 | 1-5 | Pequenas ondulações | Aragem |
| 2 | 4-6 | 6-11 | Pequenas ondas | Brisa leve |
| 3 | 7-10 | 12-19 | Cristas começam | Brisa fraca |
| 4 | 11-16 | 20-28 | Ondas pequenas frequentes | Brisa moderada |
| 5 | 17-21 | 29-38 | Ondas moderadas (1-1,5 m) | Brisa forte |
| 6 | 22-27 | 39-49 | Ondas grandes (2-3 m), espuma | Vento fresco |
| 7 | 28-33 | 50-61 | Mar grosso (3-4 m), espuma sopra | Vento forte |
| 8 | 34-40 | 62-74 | Mar muito grosso (4-5,5 m) | Ventania |
| 9 | 41-47 | 75-88 | Mar grosso (5,5-7 m) | Ventania forte |
| 10 | 48-55 | 89-102 | Mar muito alto (7-9 m) | Tempestade |
| 11 | 56-63 | 103-117 | Mar enorme (9-11+ m) | Tempestade violenta |
| 12 | 64+ | 118+ | Mar branco — visibilidade nula | Furacão |

> **RCD categorias:** A/B até 8 Bft; C até 6 Bft; D até 4 Bft.

## DISTÂNCIAS (NORMAM / MARPOL)

| Item | Distância mínima |
|------|------------------|
| Descarte de águas negras (BR — NORMAM-08) | >1 nm da costa |
| Descarte macerado/desinfetado (MARPOL Anexo IV Reg.11.1.1) | >3 nm |
| Descarte não-tratado (MARPOL Reg.11.1.2) | >12 nm a ≥4 kn |
| NDZ (No Discharge Zone EUA) | Proibido qualquer descarte |
| Polar Code (Antártico) | Proibido qualquer descarte |
| HELCOM (Báltico) | Proibido qualquer descarte |
| ARIE / APA (BR) | Proibido qualquer descarte sanitário |

## RPM E POTÊNCIA TÍPICOS DE MOTOR DIESEL MARINE

| Aplicação | RPM operacional | Watts típicos |
|-----------|------------------|----------------|
| Velocidade cruzeiro | 70-80% RPM nominal | — |
| Manobra | 1.000-1.500 | — |
| Idle | 700-900 | — |

## ROTAS DE CHECKLIST DE INSPEÇÃO (vide [[Manutenção Preventiva Elétrica — Checklist]])

### Inspeção semestral:
- Tensão banco repouso (≥12,4 V chumbo / ≥13,1 V LFP).
- Tensão banco em flutuação (13,5-13,8 V chumbo).
- Corrente parasita em standby (<200 mA típico).
- Resistência de bonding (massa-barramento <0,01 Ω).
- Estado de ânodos (>50% consumido = trocar).
- Inspeção visual cabos / conectores.
- Teste GFCI / ELCI (botão TEST).
- Teste fusível principal.
- Teste alarme de água / CO / GLP.

### Inspeção anual:
- Megger test isolação (>100 MΩ).
- Termovisor em painéis carregados.
- Calibração sensores.
- Update firmware equipamentos.

## Ferramentas mínimas a bordo (vide [[Ferramentas do Eletricista Náutico]])

- Multímetro True RMS DMM.
- Alicate amperímetro AC + DC.
- Megohmímetro (megger).
- Termômetro IR.
- Termômetro de contato.
- Crimpador calibrado para AWG marine.
- Decapador automático.
- Fita 3M VHB + heat-shrink + dielectric grease.
- Fusíveis sobressalentes.
- LED testers diversos.

## Glossário compacto

- **AWG:** American Wire Gauge.
- **mm²:** seção em mm quadrado.
- **ABYC E-11:** norma marine USA wiring.
- **ELCI / GFCI:** Equipment Leakage / Ground Fault.
- **Bonding:** ABYC E-11.16.
- **PE:** Protective Earth.
- **ABYC TE-04:** lightning protection.
- **Megger:** medidor de isolação.
- **DMM:** Digital MultiMeter.
- **True RMS:** medição correta de qualquer onda.
- **PF:** Power Factor.
- **THD:** Total Harmonic Distortion.
- **LFP:** LiFePO4.
- **DOD:** Depth of Discharge.
- **Bft:** Beaufort.
- **kn:** knot (nó).
- **NDZ:** No Discharge Zone.
- **MARPOL Anexo IV:** poluição por esgoto.
- **NORMAM-08:** tráfego e permanência BR.
- **Vide [[Lei de Ohm e Cálculos Básicos]] + [[Princípios Náuticos]]** + outras notas referenciadas.

## Integração com outras notas

Esta nota referencia praticamente todas as notas técnicas do vault. Principais:

- [[Lei de Ohm e Cálculos Básicos]] — fundamentos.
- [[Dimensionamento de Cabos DC — Cálculo Prático]].
- [[Dimensionamento de Banco de Baterias — Cálculo de Autonomia]].
- [[Cabeamento Náutico]].
- [[Fusíveis DC — Proteção Contra Sobrecorrente]] / [[Disjuntores (DC) e (AC)]].
- [[Bonding — Sistema de Interligação de Massas]] / [[Aterramento]].
- [[Bancos de Bateria]] / [[Tipos de Bateria]].
- [[Inversora (DC To AC)]] / [[Carregador de Bateria (AC To DC)]].
- [[Multímetro e Instrumentos de Medição]] / [[Voltímetro - Amperímetro (DC e AC)]].
- [[Manutenção Preventiva Elétrica — Checklist]].
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]].
- [[Ferramentas do Eletricista Náutico]].

## Perguntas que esta nota responde

- Tabela completa de valores típicos elétrica náutica?
- Queda de tensão máxima ABYC?
- AWG para 30A em 12V a 5 metros?
- Fusível para macerador 12V/22A?
- ELCI vs GFCI: qual valor de disparo?
- Tensão flutuação banco chumbo-ácido?
- Resistência de bonding aceitável?
- Ânodo: % consumido para trocar?
- Beaufort wind force scale?
- Isolação cabo náutico mínima?
- Distância mínima para descarte sanitário?
- Consumo típico de cargas DC em 12V?
