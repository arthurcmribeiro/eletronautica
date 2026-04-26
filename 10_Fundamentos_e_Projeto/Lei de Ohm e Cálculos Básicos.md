---
title: "Lei de Ohm e Cálculos Básicos"
note_type: "technical-note"
domain: "10_Fundamentos_e_Projeto"
source_file: "LEI DE OHM E CÁLCULOS BÁSICOS 33a19734f7fb81fbad36ddc9b762e6c4.md"
status: "premium-l3"
fase_6_reescrita: 95
reviewed_on: "2026-04-26"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://webstore.iec.ch/publication/2697"
  - "https://www.nist.gov/pml/weights-and-measures"
review_level: "engineering-curated"
aliases:
  - "LEI DE OHM E CÁLCULOS BÁSICOS"
  - "Ohm's Law"
  - "Lei de Ohm marine"
  - "Cálculos elétricos básicos"
  - "Circuit fundamentals"
  - "Princípios DC e AC"
seo_title: "Lei de Ohm e cálculos básicos: V=I×R, P=V×I, fórmulas DC × AC, ABYC E-11.4, IEC 60364, dimensionamento marine"
seo_description: "Guia técnico premium da Lei de Ohm aplicada à elétrica náutica: V=I×R fundamental, P=V×I=I²R=V²/R, série × paralelo, queda de tensão (ABYC E-11.4.4.1.b ≤3%), DC × AC (RMS, fator de potência, impedância, reativos), exemplos práticos (luz de navegação, motor, banco de bateria, inversor), ferramentas (multímetro, alicate amperímetro, osciloscópio)."
seo_keywords:
  - "lei de ohm marine"
  - "V=IR cálculo"
  - "potência elétrica P=VI"
  - "queda de tensão ABYC"
  - "dimensionamento cabo DC"
  - "AC RMS pico fator potência"
  - "impedância reativos"
  - "circuit série paralelo"
  - "Kirchhoff KVL KCL"
  - "DC vs AC"
geo_queries:
  - "Como calcular corrente em circuito DC marine?"
  - "Por que queda de tensão importa em barco DC?"
  - "Como dimensionar fusível usando Lei de Ohm?"
  - "Diferença entre potência ativa, reativa e aparente em AC?"
  - "RMS vs pico em corrente alternada?"
  - "Circuitos série × paralelo: quando usar cada?"
  - "Kirchhoff KVL e KCL: aplicação prática em barco?"
  - "Lei de Ohm funciona em motor (carga não-resistiva)?"
  - "Como medir resistência de cabo náutico?"
  - "Cálculo de potência dissipada em cabo subdimensionado?"
normas_citadas:
  - "ABYC E-11 (AC and DC Electrical Systems on Boats)"
  - "ABYC E-11.4 (Wire Sizing — Voltage Drop)"
  - "ABYC E-11.4.4.1.b (Queda de tensão ≤3% sob carga)"
  - "ABYC E-11.5 (Overcurrent Protection)"
  - "ABYC E-11.5.4 (Fusível ≤7 polegadas da bateria)"
  - "IEC 60364-1 (Low-voltage electrical installations — Fundamental principles)"
  - "IEC 60364-5-52 (Wiring systems)"
  - "IEC 60364-7-709 (Marinas)"
  - "IEC 61557 (Electrical safety in low-voltage distribution systems)"
  - "ISO 10133 (Extra-low voltage DC installations) — atenção: sucessora ISO 28848"
  - "ISO 13297 (AC installations)"
  - "ISO 28848 (DC installations)"
  - "IEEE 100 (Standard Dictionary of Electrical and Electronics Terms)"
  - "NFPA 70 (NEC — National Electrical Code USA)"
  - "NFPA 70 Article 555 (Marinas)"
  - "UL 1426 (Boat Cable BC5W2)"
  - "SAE J1127 / SAE J1128 (Battery Cable)"
  - "IEC 60092-353 (Marine cable)"
  - "IEC 60228 (Conductors of insulated cables)"
  - "EU Directive 2014/35/EU (LVD)"
  - "EU 2013/53/EU (RCD)"
  - "ABNT NBR 5410 (Instalações elétricas BT)"
  - "ABNT NBR 14728 (Embarcações de recreio)"
  - "ABNT NBR ISO 13297"
  - "ABNT NBR ISO 28848"
  - "DPC NORMAM-211/DPC"
  - "DPC NORMAM-201/DPC"
related_notes:
  - "DC vs AC — Corrente Contínua e Alternada"
  - "Diagrama Unifilar — Documentação do Sistema Elétrico"
  - "Dimensionamento de Banco de Baterias — Cálculo de Autonomia"
  - "Dimensionamento de Cabos DC — Cálculo Prático"
  - "Fase e Neutro"
  - "Ferramentas do Eletricista Náutico"
  - "Inspeção de Cabos Terminais e Conexões"
  - "Leitura de Diagramas e Esquemas Elétricos"
  - "Multímetro e Instrumentos de Medição"
  - "Voltímetro - Amperímetro (DC e AC)"
  - "Referência Rápida — Valores de Campo"
  - "Simbologia Elétrica Náutica"
  - "Cabeamento Náutico"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Disjuntores (DC) e (AC)"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
---

# Lei de Ohm e Cálculos Básicos

> [!abstract] Resumo técnico
> A **Lei de Ohm (V = I × R)** + **fórmula de potência (P = V × I = I² × R = V²/R)** + **leis de Kirchhoff (KVL malhas + KCL nós)** formam o **núcleo matemático fundamental** de toda análise de circuito elétrico — DC ou AC. Em embarcação, dominar Lei de Ohm é pré-requisito para: **dimensionar cabo (queda de tensão ≤3% — ABYC E-11.4.4.1.b)**, **calcular fusível (125% da corrente nominal)**, **estimar consumo de banco de bateria (Ah × tempo)**, **diagnosticar falha (resistência de contato anormal, queda excessiva)**, **especificar inversor (W vs VA), gerador, motor**. **Lei de Ohm em sentido estrito aplica-se a condutores ôhmicos** (resistência constante com tensão); cargas reais (motor, fluorescente, semicondutor) **não são puramente ôhmicas** — requerem extensões via impedância (Z = R + jX em AC). Em corrente alternada AC, conceitos adicionais: **valores RMS vs pico** (V_pico = V_RMS × √2), **fator de potência (PF = cos φ)**, **potência ativa (W) × reativa (VAr) × aparente (VA)**, **harmônicas e THD**. Padrões aplicáveis: **ABYC E-11** (wiring), **IEC 60364** (low-voltage installations), **ISO 28848 + 13297** (marine DC + AC), **ABNT NBR 14728 + 5410**, **NFPA 70 + UL 1426 + SAE J1127/J1128** (USA cables), **IEC 60092-353 + 60228** (cabos marítimos).

> [!tldr] TL;DR — 9 regras inegociáveis
> 1. **Lei de Ohm: V = I × R** — três variáveis, uma relação. Conhecer 2 → calcular a 3ª. Em DC puro (resistivo), exato; em AC ou cargas reais, é aproximação útil mas não exclusiva.
> 2. **Potência: P = V × I (DC)** — em AC com PF: **P (ativa, W) = V × I × cos φ**. **S (aparente, VA) = V × I**. Inversor de 3 kW (S) com PF 0,7 entrega só 2,1 kW reais. Sempre dimensionar pelo aparente (VA), não pelo ativo (W).
> 3. **Queda de tensão ≤3% sob carga** (ABYC E-11.4.4.1.b — o critério marine universal). Cálculo: **ΔV = 2 × L × I × ρ / S** onde ρ_cobre = 1,72×10⁻⁸ Ω·m. Cabo subdimensionado → motor opera fora do nominal → torque cai → corrente sobe → ciclo destrutivo.
> 4. **Fusível dimensionado a 125% da corrente nominal** da carga (ABYC E-11.5). Não 200%, não 100%. Super: queima motor antes do fusível. Sub: dispara em uso normal.
> 5. **Lei de Ohm NÃO se aplica a cargas não-ôhmicas** (motor sob partida, lâmpada incandescente fria, LED com driver, transformador). Para essas: usar dados do datasheet (corrente nominal, partida, FLA, LRA).
> 6. **Série: I igual em todos, V soma.** **Paralelo: V igual em todos, I soma.** Em barco, baterias em série dobram tensão (12+12=24V, mesmo Ah); em paralelo dobram capacidade (12V, Ah1+Ah2). Mistura de Ah ou idades em paralelo: corrente desbalanceada + degradação acelerada.
> 7. **Kirchhoff KCL (corrente):** soma de correntes no nó = 0. **KVL (tensão):** soma de tensões na malha = 0. Aplicação prática: medir queda em cada trecho do cabo para identificar onde está a perda.
> 8. **AC: pensar em RMS sempre.** Multímetro mostra RMS; instrumentos AC analógicos quasi-RMS são imprecisos com formas de onda não-senoidais (inversor, gerador). Onda senoidal: V_pico = V_RMS × √2 ≈ 1,414 × V_RMS.
> 9. **Calor por efeito Joule: P = I² × R.** Cabo com R = 0,01 Ω carregando 50 A dissipa 25 W → cabo aquece. Em circuito longo (10 m), pode chegar a 100 W → fogo elétrico. Daí queda de tensão ser também critério de **segurança térmica**, não só performance.

> [!danger] Cenários de risco
> - **Cabo subdimensionado em circuito de motor:** ΔV >5% → torque cai 10-15% → corrente sobe 10-20% → P_dissipada (I²R) sobe ~25% → cabo aquece a 80-100°C → derretimento de isolação → curto contra casco / fogo. **Caso típico:** macerador sanitário em cabo AWG 14 a 5 m (deveria ser AWG 8) → falha catastrófica em meses.
> - **Fusível dimensionado pelo "máximo do cabo"** em vez da carga: cabo aguenta 50A, carga é 20A → instalou fusível 50A → motor trava em 80A (stall) → fusível NÃO abre → motor queima em segundos. **Prevenção:** fusível dimensionado pela CARGA (125% nominal), não pelo cabo (que pode ser sobre-dimensionado).
> - **Confusão W × VA em inversor:** inversor 2000W especificado em pico (peak) — usuário interpreta como contínuo → liga ar-condicionado 1500W contínuo + bomba 800W → inversor em sobrecarga permanente → falha em meses. **Prevenção:** ler datasheet (continuous vs peak vs surge); calcular VA com fator de potência; aplicar margem 30%.
> - **Bancos de bateria em paralelo com idades diferentes:** célula 8 anos + célula nova → corrente desbalanceada (KCL — célula nova fornece mais) → degradação acelerada da nova → ciclo destrutivo. **Prevenção:** bancos em paralelo com idades + capacidades + química idênticas; substituir todos juntos.
> - **AC quasi-senoidal de inversor low-end** medido com multímetro AC quasi-RMS: leitura aparente correta mas onda real distorcida → motores não rotam suavemente, eletrônica sensível falha. **Prevenção:** True RMS multimeter (Fluke 17B+, 87V); inversor pure sine wave em AC sensível.
> - **Corrente de partida (LRA) ignorada em motor:** motor 3A nominal partida 18A → instalou cabo / fusível para 3A → fusível abre em cada partida ou cabo aquece → falha. **Prevenção:** dimensionar para LRA momentâneo + nominal contínuo; fusível tipo Slow-Blow ou ANL.
> - **Curto-circuito por análise errada:** instalou disjuntor magnético térmico para circuit residencial em barco DC → tempo de abertura inadequado em DC (DC não tem zero crossing) → arco contínuo + fogo. **Prevenção:** disjuntor especificado para DC com rated voltage adequado (vide [[Disjuntores (DC) e (AC)]]); fusível ANL/MIDI/ATC para alta corrente.
> - **Conexão paralela de baterias com cabos de bitolas diferentes:** cabo curto de uma bateria + cabo longo da outra → resistência desbalanceada → corrente concentra na bateria com cabo curto → desgaste assimétrico. **Prevenção:** "method 4 paralelo" (cabos de mesmo comprimento de cada bateria à carga).
> - **Soma errada de potência em circuito misto AC + DC:** usuário soma 2000W AC + 200W DC = "2200W" sem considerar que AC consome do inversor (com perda 10-15%) → dimensionamento de bateria/banco erra 10-30%. **Prevenção:** converter AC → DC equivalente: P_DC = P_AC / η_inversor.
> - **Dimensionamento por nominal sem considerar duty cycle:** macerador 15A nominal duty 25% → instalou cabo / fusível para "15A contínuo" mas usou em uso intenso (pump-out 60s contínuo) → motor 130°C + fogo. **Prevenção:** ler datasheet duty cycle; respeitar tempo ON/OFF.

## A fórmula fundamental — Lei de Ohm

```
                                  ╭───╮
                              ╭───╯ V ╰───╮
                              │   ╱   ╲   │
                              │  ╱     ╲  │
                              │ ╱       ╲ │
                              │╱         ╲│
                              │           │
                              │   I × R   │
                              │           │
                              ╰───────────╯
```

```
V = I × R    →  Tensão (V) = Corrente (A) × Resistência (Ω)
I = V / R    →  Corrente (A) = Tensão (V) / Resistência (Ω)
R = V / I    →  Resistência (Ω) = Tensão (V) / Corrente (A)
```

### Triângulo de Ohm

```
            V
          /   \
         /     \
        / I × R \
       /_________\
        I       R
```

Cobrindo a variável que quer calcular, leem-se as outras duas (com operação implicada).

## Potência elétrica

### DC

```
P = V × I       →  Potência (W) = Tensão × Corrente
P = I² × R      →  Potência = Corrente² × Resistência (efeito Joule)
P = V² / R      →  Potência = Tensão² / Resistência
```

### AC (com fator de potência)

```
S (aparente, VA) = V × I              →  Potência aparente (instalação dimensiona por aqui)
P (ativa, W)     = V × I × cos φ      →  Potência consumida pela carga (efetivamente trabalho)
Q (reativa, VAr) = V × I × sin φ      →  Potência reativa (campo magnético / capacitivo)

|S|² = P² + Q²                        →  Triângulo de potências
PF = cos φ = P / S                    →  Fator de potência (0 a 1)
```

> [!info] Fatores de potência típicos em barco
> | Carga | PF típico |
> |-------|-----------|
> | Resistiva (chuveiro, ferro) | 1,0 |
> | Lâmpada incandescente | 1,0 |
> | LED bem projetado | 0,9-0,98 |
> | LED ruim / driver simples | 0,5-0,7 |
> | Motor de indução em carga | 0,7-0,9 |
> | Motor em partida (sem carga) | 0,3-0,5 |
> | Ar-condicionado | 0,7-0,9 |
> | Inversor / SMPS | 0,9-0,99 |

## Lei de Ohm aplicada à queda de tensão

```
ΔV = 2 × L × I × ρ / S
```

Onde:
- **L** = comprimento do cabo (m) — o "2×" considera ida + volta.
- **I** = corrente (A).
- **ρ** = resistividade do cobre = 1,72 × 10⁻⁸ Ω·m a 20°C; aumenta ~0,4%/°C.
- **S** = seção do condutor (m²).

### Tabela ABYC E-11.4 — Queda de tensão 3% (referência)

| Bitola AWG | Bitola mm² | Comprimento máximo (12V/10A, ΔV ≤ 3%) |
|------------|-------------|------------------------------------------|
| AWG 16 | 1,3 mm² | 1,5 m |
| AWG 14 | 2,1 mm² | 2,5 m |
| AWG 12 | 3,3 mm² | 4,0 m |
| AWG 10 | 5,3 mm² | 6,0 m |
| AWG 8 | 8,4 mm² | 9,5 m |
| AWG 6 | 13,3 mm² | 15 m |
| AWG 4 | 21,2 mm² | 24 m |

> [!warning] Exemplo prático
> Macerador 12V × 22A nominal a 6 m (ida+volta = 12 m round-trip):
> - AWG 14 (2,1 mm²): ΔV = 2 × 6 × 22 × 1,72e-8 / 2,1e-6 = **2,16 V (18% — INACEITÁVEL)** → motor 9,8V em vez de 12V → torque cai 30% → motor queima em meses.
> - AWG 6 (13,3 mm²): ΔV = 2 × 6 × 22 × 1,72e-8 / 13,3e-6 = **0,34 V (2,8% — OK)**.

## Circuitos série × paralelo

### Série

```
[Bateria] → [R₁] → [R₂] → [R₃] → [Bateria]

R_total = R₁ + R₂ + R₃
I_total = igual em todos os componentes
V_total = V₁ + V₂ + V₃
```

### Paralelo

```
                    ┌──[R₁]──┐
[Bateria] ──────────┼──[R₂]──┼──── [Bateria]
                    └──[R₃]──┘

1/R_total = 1/R₁ + 1/R₂ + 1/R₃
V_total = V em todos
I_total = I₁ + I₂ + I₃
```

### Exemplos práticos em barco

| Aplicação | Configuração | Comportamento |
|-----------|--------------|----------------|
| Bateria 12V (6 células 2V) | Série | Mantém Ah, tensão cresce |
| 2 bancos 12V/100Ah em paralelo | Paralelo | 12V × 200Ah, mas mistura quebra equilíbrio |
| Iluminação cabine LED | Paralelo | Cada lâmpada vê 12V; falha de uma não afeta outras |
| Strings de painel solar 24V | 2× em série + N em paralelo | 48V × N×Ah |
| Detector de fumaça com fim-de-linha resistor | Série + paralelo (loop) | Detecção de quebra de cabo via resistência |

## Leis de Kirchhoff

### KVL (Lei das Tensões — Kirchhoff Voltage Law)

```
Soma das tensões em qualquer malha fechada = 0
∑ V = 0
```

Aplicação: **medir queda de tensão em cada trecho do cabo** para identificar perda anormal.

### KCL (Lei das Correntes — Kirchhoff Current Law)

```
Soma das correntes que entram em um nó = soma das que saem
∑ I_in = ∑ I_out
```

Aplicação: **balanço de corrente em barramento DC** (vide [[Barramento DC - Bus Bar - Distribuição DC]]).

## DC × AC — diferenças críticas

| Conceito | DC | AC |
|----------|----|----|
| Frequência | 0 Hz | 50 Hz (BR) ou 60 Hz (USA) |
| Tensão | Constante | Senoidal (V_pico = V_RMS × √2) |
| Corrente | Constante | Senoidal |
| Potência | P = V × I | P = V × I × cos φ |
| Resistência | R | Z = R + jX (impedância) |
| Capacitor | Carrega + abre | Reactância capacitiva: X_C = 1/(ωC) |
| Indutor | Curto sustentado | Reactância indutiva: X_L = ωL |
| Multímetro | Direto | RMS (true vs quasi-RMS) |

### Valores RMS, médio, pico em AC

```
V_pico = V_RMS × √2 ≈ V_RMS × 1,414
V_pico-pico = 2 × V_pico
V_médio = (2/π) × V_pico ≈ 0,637 × V_pico  (onda senoidal)

V_RMS = √(1/T × ∫ v(t)² dt)  (definição matemática)
```

Para 220V RMS (BR): V_pico ≈ 311 V, V_pico-pico ≈ 622 V.

## Calor por efeito Joule

```
P_dissipada = I² × R
```

**Exemplo prático:**

- Cabo AWG 14 (R ≈ 0,02 Ω/m) carregando 30A em 5 m:
  - P_dissipada = 30² × (0,02 × 5 × 2) = 900 × 0,2 = **180 W**.
  - 180 W em cabo de 10 m total = 18 W/m → cabo aquece > 80°C → derretimento da isolação.
- **Solução:** cabo AWG 8 (R ≈ 0,007 Ω/m) → P = 30² × 0,07 = **63 W** = 6,3 W/m → cabo confortável.

## Extensões — análise de cargas reais

### Motor DC sob partida (LRA)

```
I_partida (Locked Rotor Amps) ≈ V / R_armadura ≈ 5-10 × I_nominal

Em motor 12V, R_armadura ≈ 0,5 Ω → I_LRA ≈ 24A para nominal 4A.
```

Implicações: fusível tipo "Slow-Blow" (ANL); cabo dimensionado para nominal; barra de bateria + chave gerais para LRA.

### Carga LED com driver

LED em si NÃO segue Lei de Ohm linearmente (Vf cresce ~0,005 V/°C). Driver eletrônico mantém **corrente constante (CC)** ou **tensão constante (CV)**.

### Inversor SMPS

Eficiência típica 85-95%. Para calcular consumo DC:
```
P_DC = P_AC / η_inversor
I_DC = P_DC / V_DC
```

## Ferramentas de medição (vide [[Multímetro e Instrumentos de Medição]] + [[Voltímetro - Amperímetro (DC e AC)]])

| Ferramenta | Uso típico |
|------------|------------|
| Multímetro digital (DMM) True RMS | V/I/R/continuidade — base do diagnóstico |
| Alicate amperímetro (clamp) AC+DC | I sem desconectar circuito — essencial em motor / banco |
| Osciloscópio | Forma de onda AC, harmônicas, ripple inversor |
| Megôhmetro (megger) | Isolação de cabo (>100 MΩ vs casco) |
| Termômetro IR | Temperatura cabo / conector — confirma I²R efetivo |

## Falhas comuns

| Falha | Causa | Solução |
|-------|-------|---------|
| Cabo aquece | Subdimensionado para corrente | Recalcular ΔV; aumentar bitola |
| Fusível abre em uso normal | Subdimensionado vs LRA | Tipo Slow-Blow; recalcular |
| Motor torque baixo | Queda de tensão excessiva | AWG correto; conectores limpos |
| Inversor desliga em sobrecarga | Carga real > rated VA | Calcular VA com PF; margem 30% |
| Banco paralelo desbalanceado | Idades / Ah / cabos diferentes | Method 4 paralelo; substituir todos |
| AC quasi-RMS lê errado | Inversor onda quasi-senoidal | True RMS multimeter |

## Boas práticas

- **Calcular ANTES de comprar** (cabo, fusível, banco, inversor).
- **Margem 25-30%** em todos os dimensionamentos.
- **Documentar cálculos** no diário de bordo elétrico.
- **Verificar empiricamente** após instalação (multímetro + termômetro IR).
- **Conhecer datasheet** das cargas (nominal, partida, FLA, LRA, duty).
- **Lei de Ohm como ponto de partida**, não como única ferramenta.

## Erros comuns

- "V = I × R sempre funciona." → Em cargas não-ôhmicas, é aproximação.
- "Margem 10% é suficiente." → ABYC + IEC: ≥25%.
- "Inversor 2000W aguenta 2000W contínuo." → Ler datasheet (peak vs continuous).
- "AC e DC são iguais com cuidado." → Frequência, RMS, PF, harmônicas mudam tudo.
- "Fusível pelo cabo." → Dimensionar pela CARGA (125% nominal).

## Glossário

- **V (Volt):** tensão / diferença de potencial.
- **I (Ampere):** corrente.
- **R (Ohm):** resistência.
- **P (Watt):** potência ativa.
- **S (VA):** potência aparente.
- **Q (VAr):** potência reativa.
- **PF (Power Factor):** cos φ = P/S.
- **Z (Impedance):** impedância (R + jX em AC).
- **X_L:** reactância indutiva = ωL.
- **X_C:** reactância capacitiva = 1/(ωC).
- **ω (omega):** 2π × f (rad/s).
- **f:** frequência (Hz).
- **RMS:** Root Mean Square — valor eficaz.
- **True RMS:** medição correta para qualquer forma de onda.
- **Quasi-RMS:** medição calibrada apenas para senoidal.
- **THD:** Total Harmonic Distortion.
- **Harmônica:** componente de frequência múltipla da fundamental.
- **FLA:** Full Load Amps.
- **LRA:** Locked Rotor Amps (5-10× FLA).
- **KVL:** Kirchhoff Voltage Law.
- **KCL:** Kirchhoff Current Law.
- **Ohmic load:** carga linear (R constante).
- **Non-ohmic load:** carga não-linear.
- **Resistividade ρ:** Ω·m (cobre 1,72×10⁻⁸ a 20°C).
- **Condutividade σ:** 1/ρ.
- **Joule heat:** P = I²R.
- **AWG:** American Wire Gauge.
- **mm²:** seção do condutor.
- **Slow-Blow:** fusível que tolera transiente.
- **Fast-Blow:** fusível rápido.
- **CC (Constant Current):** driver de corrente constante.
- **CV (Constant Voltage):** driver de tensão constante.
- **SMPS:** Switching Mode Power Supply.
- **Inversor pure sine wave:** onda senoidal verdadeira.
- **Inversor modified sine wave:** onda quasi-senoidal (em desuso).
- **ABYC E-11.4:** wire sizing voltage drop.
- **IEC 60364:** low-voltage installations.
- **ISO 28848:** marine DC.
- **NFPA 70:** NEC USA.
- **UL 1426:** boat cable BC5W2.

## Integração com outras notas

- [[DC vs AC — Corrente Contínua e Alternada]] — diferenças fundamentais.
- [[Diagrama Unifilar — Documentação do Sistema Elétrico]] — diagrama técnico.
- [[Dimensionamento de Banco de Baterias — Cálculo de Autonomia]] — Ah × tempo.
- [[Dimensionamento de Cabos DC — Cálculo Prático]] — aplicação direta.
- [[Fase e Neutro]] — AC fundamentos.
- [[Multímetro e Instrumentos de Medição]] / [[Voltímetro - Amperímetro (DC e AC)]] — medição.
- [[Inspeção de Cabos Terminais e Conexões]] — empírico.
- [[Leitura de Diagramas e Esquemas Elétricos]] — interpretar diagrama.
- [[Referência Rápida — Valores de Campo]] — cheat sheet.
- [[Simbologia Elétrica Náutica]] — símbolos.
- [[Cabeamento Náutico]] — bitola e tipo.
- [[Fusíveis DC — Proteção Contra Sobrecorrente]] / [[Disjuntores (DC) e (AC)]] — proteção.
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]] — diagnóstico.

## Perguntas que esta nota responde

- Como calcular corrente em circuito DC marine?
- Por que queda de tensão importa em barco DC?
- Como dimensionar fusível usando Lei de Ohm?
- Diferença entre potência ativa, reativa e aparente em AC?
- RMS vs pico em corrente alternada?
- Circuitos série × paralelo: quando usar cada?
- Kirchhoff KVL e KCL: aplicação prática em barco?
- Lei de Ohm funciona em motor (carga não-resistiva)?
- Como medir resistência de cabo náutico?
- Cálculo de potência dissipada em cabo subdimensionado?
- Por que cabo subdimensionado é problema térmico além de performance?
- Como dimensionar inversor para cargas mistas?
