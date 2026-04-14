---
title: "Lei de Ohm e Cálculos Básicos"
note_type: "technical-note"
domain: "10_Fundamentos_e_Projeto"
source_file: "LEI DE OHM E CÁLCULOS BÁSICOS 33a19734f7fb81fbad36ddc9b762e6c4.md"
status: "technical-review-l1"
aliases:
  - "LEI DE OHM E CÁLCULOS BÁSICOS"
seo_title: "Lei de Ohm e Cálculos Básicos"
seo_description: "LEI DE OHM — O fundamento matemático de toda a elétrica. Três variáveis, uma relação — entender isso é entender por que os circuitos se comportam como se comportam."
seo_keywords:
  - "Lei"
  - "Ohm"
  - "Cálculos"
  - "Básicos"
  - "10 Fundamentos e Projeto"
geo_queries:
  - "O que é Lei de Ohm e Cálculos Básicos em instalações elétricas náuticas?"
related_notes:
  - "DC vs AC — Corrente Contínua e Alternada"
  - "Diagrama Unifilar — Documentação do Sistema Elétrico"
  - "Dimensionamento de Banco de Baterias — Cálculo de Autonomia"
  - "Dimensionamento de Cabos DC — Cálculo Prático"
  - "Fase e Neutro"
  - "Ferramentas do Eletricista Náutico"
  - "Inspeção de Cabos Terminais e Conexões"
  - "Leitura de Diagramas e Esquemas Elétricos"
---

# Lei de Ohm e Cálculos Básicos

> [!abstract] Resumo técnico
> LEI DE OHM — O fundamento matemático de toda a elétrica. Três variáveis, uma relação — entender isso é entender por que os circuitos se comportam como se comportam.

## O que é

A Lei de Ohm descreve a relação entre tensão (V), corrente (I) e resistência (R) em um circuito elétrico. Formulada por Georg Simon Ohm em 1827, é o ponto de partida para entender o comportamento de qualquer circuito DC — desde uma luz de navegação até um banco de baterias completo.

## A fórmula

```jsx
V = I × R
I = V / R
R = V / I
P = V × I = I² × R = V² / R
```

| Símbolo | Grandeza | Unidade |
| --- | --- | --- |
| V | Tensão (Voltage) | Volts (V) |
| I | Corrente (Current / Intensity) | Amperes (A) |
| R | Resistência (Resistance) | Ohms (Ω) |
| P | Potência (Power) | Watts (W) |

## Triângulo de Ohm — memorização rápida

```jsx
  [ V ]
─────────
[ I ][ R ]
```

Para encontrar qualquer variável: cobrir ela com o dedo e o que restar é a fórmula.

- Cobrir V: I × R
- Cobrir I: V / R
- Cobrir R: V / I

## Aplicações práticas a bordo

**Calcular corrente de um equipamento:**

```jsx
Motor de bomba de porão: 120W em 12V
I = P / V = 120 / 12 = 10A
→ A corrente calculada é a base para selecionar proteção e cabo, que depois ainda devem ser verificados por inrush, comprimento, ampacidade e ambiente
```

**Calcular queda de tensão em um cabo:**

```jsx
Cabo AWG 16 (1,5mm²), 5m de comprimento (10m ida+volta)
R_cabo = (0,0175 × 10) / 1,5 = 0,117 Ω
Corrente: 8A
Queda = I × R = 8 × 0,117 = 0,93V (7,8% de 12V — excessivo!)
→ Usar cabo maior
```

**Calcular resistência de um aquecedor DC:**

```jsx
Aquecedor de 12V, 150W
R = V² / P = 144 / 150 = 0,96 Ω
I = V / R = 12 / 0,96 = 12,5A
→ Esse valor de corrente é ponto de partida para a seleção do circuito; fusível e bitola exigem validação adicional
```

**Calcular consumo de energia de uma carga:**

```jsx
GPS: 15W × 8h = 120 Wh/dia
Radar: 50W × 4h = 200 Wh/dia
Total: 320 Wh/dia
```

## Circuitos em série vs em paralelo

**Em série:**

- Mesma corrente passa por todos os componentes
- Tensões somam: V_total = V1 + V2 + V3
- Resistências somam: R_total = R1 + R2 + R3
- Falha em um componente interrompe todo o circuito

**Em paralelo:**

- Mesma tensão em todos os componentes
- Correntes somam: I_total = I1 + I2 + I3
- Resistência total < menor resistência: 1/R_total = 1/R1 + 1/R2 + 1/R3
- Falha em um componente não afeta os demais

**Aplicação em baterias:**

- Baterias em série: tensão soma, capacidade (Ah) mantém → 2 × 12V = 24V, mesma capacidade
- Baterias em paralelo: tensão mantém, capacidade soma → 2 × 12V 100Ah = 12V 200Ah

## Relação com queda de tensão

Queda de tensão é a aplicação direta da Lei de Ohm:

```jsx
ΔV = I × R_cabo
```

Todo cabo tem resistência. Quanto maior a corrente ou maior o comprimento, maior a queda de tensão. O equipamento no final do cabo recebe a tensão da bateria menos a queda no cabo.

**Exemplo real:**

- Bateria carregada: 12,6V
- Cabo: 0,3Ω (cabo fino, longo)
- Corrente: 8A
- Queda no cabo: 8 × 0,3 = 2,4V
- Tensão no equipamento: 12,6 - 2,4 = **10,2V** (criticamente baixo)

## Relação com consumo e baterias

**Energia em Wh:**

```jsx
E (Wh) = P (W) × t (h)
E (Wh) = V × I × t
```

**Capacidade de bateria:**

```jsx
Capacidade (Ah) = Corrente (A) × Tempo (h)
Energia (Wh) = Capacidade (Ah) × Tensão (V)
```

**Tempo de autonomia:**

```jsx
t = Capacidade (Ah) / Corrente total (A)
Exemplo: banco de 200Ah, consumo de 25A → t = 200/25 = 8h (sem considerar DOD)
```

## Potência e calor — a relação esquecida

A Lei de Joule (derivada de Ohm) diz que toda resistência dissipa calor:

```jsx
P_calor = I² × R
```

**Por que isso importa:**

- Um terminal oxidado com R = 0,1Ω e 10A de corrente gera: 10² × 0,1 = **10W de calor**
- 10W em uma área pequena (terminal) = aquecimento intenso = falha progressiva
- Este é um dos mecanismos clássicos de aquecimento e incêndio por conexão defeituosa

**Detectar:** câmera termográfica mostra pontos quentes antes da falha.

## Limitações da Lei de Ohm

A Lei de Ohm é válida para:

- Resistências puras (resistores, cabos, aquecedores)
- Condições DC estacionárias

Não é diretamente aplicável a:

- Capacitores (armazenam carga, não consomem como resistência)
- Indutores (bobinas — resistência varia com frequência em AC)
- Motores elétricos (têm backEMF — comportam-se diferente de uma resistência)
- Baterias (fonte de tensão, não resistência pura)

## Como ensinar este tópico

**Sequência recomendada:**

1. Analogia hidráulica: tensão = pressão da água, corrente = fluxo, resistência = diâmetro da tubulação
2. Triângulo de Ohm — memorização imediata com exercício de cobrir o dedo
3. Cálculo ao vivo: dado um equipamento real, calcular corrente e usar esse resultado como base para selecionar fusível e cabo
4. Demonstrar queda de tensão: ligar LED no final de cabo fino e longo — brilha menos
5. Exercício: dado um circuito, calcular corrente, queda de tensão, verificar se o cabo é adequado

**Conceito-chave para fixar:**

"V = I × R. Três variáveis. Saber duas → calcular a terceira. Isso resolve 80% dos problemas práticos de campo."

## Erros comuns

**Esquecer que a resistência do cabo importa:**

"O cabo é condutor, não tem resistência significativa." Todo cabo tem resistência. Em correntes altas ou comprimentos longos, a queda é real e impactante.

**Calcular corrente mas esquecer a potência:**

Saber que o circuito tem 10A não é o mesmo que saber que tem 120W. Ambos são necessários para dimensionar cabos e banco.

**Confundir Wh com Ah:**

Ah mede carga (corrente × tempo). Wh mede energia (potência × tempo). A conversão depende da tensão do sistema: 100Ah × 12V = 1200Wh.

## Relação com outros sistemas

- **Dimensionamento de cabos:** fórmula de queda de tensão é Lei de Ohm aplicada
- **Fusíveis:** fusível correto = calculado pela corrente do circuito (I = P/V)
- **Banco de baterias:** autonomia calculada com I e capacidade em Ah
- **Troubleshooting:** medir V, I e R para identificar qualquer falha no circuito

## FAQ

**Qual a diferença entre Watts e Volt-amperes (VA)?**

Em DC, são iguais: W = V × A. Em AC, diferem pelo fator de potência (FP): W = VA × FP. Para cargas resistivas (aquecedores, incandescentes) FP=1. Para eletrônicos e motores, FP < 1. Em DC e náutica básica, trabalhar com Watts é suficiente.

**Por que baterias têm capacidade em Ah e não em Wh?**

Convenção histórica. Ah é independente da tensão — uma bateria de 100Ah sempre tem 100Ah. Wh depende da tensão, que varia durante o ciclo de carga/descarga. Atualmente, muitos fabricantes fornecem ambos.

**A resistência muda com a temperatura?**

Sim. A resistência do cobre aumenta com a temperatura: +0,4% por grau Celsius. A 60°C vs 20°C, a resistência do cobre é ~16% maior — aumenta a queda de tensão. Por isso os fatores de correção existem no dimensionamento.

## Integração com outras notas

- [[DC vs AC — Corrente Contínua e Alternada]]
- [[Diagrama Unifilar — Documentação do Sistema Elétrico]]
- [[Dimensionamento de Banco de Baterias — Cálculo de Autonomia]]
- [[Dimensionamento de Cabos DC — Cálculo Prático]]
- [[Fase e Neutro]]
- [[Ferramentas do Eletricista Náutico]]
- [[Inspeção de Cabos Terminais e Conexões]]
- [[Leitura de Diagramas e Esquemas Elétricos]]

## Perguntas que esta nota responde

- O que é Lei de Ohm e Cálculos Básicos em instalações elétricas náuticas?
