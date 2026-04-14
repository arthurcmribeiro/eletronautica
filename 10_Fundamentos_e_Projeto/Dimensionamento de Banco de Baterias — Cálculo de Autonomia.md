---
title: "Dimensionamento de Banco de Baterias — Cálculo de Autonomia"
note_type: "procedure"
domain: "10_Fundamentos_e_Projeto"
source_file: "DIMENSIONAMENTO DE BANCO DE BATERIAS — CÁLCULO DE  33a19734f7fb8174ba99e27e7b0fef11.md"
status: "technical-review-l1"
aliases:
  - "DIMENSIONAMENTO DE BANCO DE BATERIAS — CÁLCULO DE"
  - "DIMENSIONAMENTO DE BANCO DE BATERIAS — CÁLCULO DE AUTONOMIA"
seo_title: "Dimensionamento de Banco de Baterias — Cálculo de Autonomia"
seo_description: "DIMENSIONAMENTO DE BANCO DE BATERIAS — Como calcular a capacidade necessária para um banco de baterias náutico. O cálculo mais importante do projeto elétrico — feito."
seo_keywords:
  - "Dimensionamento"
  - "Banco"
  - "Baterias"
  - "Cálculo"
  - "Autonomia"
  - "10 Fundamentos e Projeto"
geo_queries:
  - "O que é Dimensionamento de Banco de Baterias — Cálculo de Autonomia em instalações elétricas náuticas?"
related_notes:
  - "Dimensionamento de Cabos DC — Cálculo Prático"
  - "DC vs AC — Corrente Contínua e Alternada"
  - "Diagrama Unifilar — Documentação do Sistema Elétrico"
  - "Fase e Neutro"
  - "Ferramentas do Eletricista Náutico"
  - "Inspeção de Cabos Terminais e Conexões"
  - "Lei de Ohm e Cálculos Básicos"
  - "Leitura de Diagramas e Esquemas Elétricos"
---

# Dimensionamento de Banco de Baterias — Cálculo de Autonomia

> [!abstract] Resumo técnico
> DIMENSIONAMENTO DE BANCO DE BATERIAS — Como calcular a capacidade necessária para um banco de baterias náutico. O cálculo mais importante do projeto elétrico — feito errado, o sistema inteiro é sub ou superdimensionado.

## O que é

Dimensionamento de banco é o processo de calcular a capacidade de armazenamento de energia necessária (em Ah ou Wh) para atender ao consumo real da embarcação durante o período de autonomia desejado, respeitando os limites de profundidade de descarga (DOD) de cada tecnologia de bateria.

É o ponto de partida de qualquer projeto elétrico — antes de definir cabos, inversores ou sistema de geração.

## A sequência correta de cálculo

```jsx
1. Levantamento de cargas (consumo de cada equipamento)
        ↓
2. Perfil de uso (quanto tempo cada equipamento fica ligado por dia)
        ↓
3. Consumo diário total (Wh/dia ou Ah/dia)
        ↓
4. Autonomia desejada (quantos dias sem recarga)
        ↓
5. DOD máximo permitido (pela tecnologia da bateria)
        ↓
6. Capacidade necessária do banco
        ↓
7. Reserva de projeto (ajustada ao perfil de uso, envelhecimento e incertezas)
        ↓
8. Banco final definido
```

## Levantamento de cargas

**Template de levantamento:**

| Equipamento | Potência (W) | Tensão | Corrente (A) | Horas/dia | Wh/dia |
| --- | --- | --- | --- | --- | --- |
| Chartplotter / MFD | 20W | 12V | 1,7A | 8h | 160 |
| VHF fixo | 6W (RX) / 25W (TX) | 12V | 0,5A/2,1A | 7h RX + 0,5h TX | 54,5 |
| GPS antena | 2W | 12V | 0,2A | 8h | 16 |
| Radar | 40W | 12V | 3,3A | 4h | 160 |
| AIS | 3W | 12V | 0,25A | 8h | 24 |
| Piloto automático (cruzeiro) | 30W médio | 12V | 2,5A | 8h | 240 |
| Iluminação LED total | 30W | 12V | 2,5A | 5h | 150 |
| Bomba de porão | 60W | 12V | 5A | 0,25h | 15 |
| Geladeira DC | — | 12V | — | contínua | 60Wh/24h |
| Bomba de água doce | 50W | 12V | 4,2A | 0,5h | 25 |
| Carregador USB | 15W | 12V | 1,25A | 6h | 90 |
| **TOTAL** |  |  |  |  | **~1.000 Wh/dia** |

## Cálculo de capacidade

**Fórmula:**

```jsx
Consumo diário: X Wh/dia
Autonomia desejada: N dias
Consumo total: X × N = C_total (Wh)

DOD de projeto por tecnologia (valores de referência, não universais):
→ Chumbo-ácido (VRLA/AGM): frequentemente se adota ~50% para preservar vida útil
→ GEL: também costuma operar em faixa conservadora semelhante, conforme fabricante
→ LiFePO4: muitos projetos trabalham entre ~70% e 90%, conforme fabricante, BMS e vida útil desejada

Capacidade necessária: C_banco = C_total / DOD

Converter para Ah: Ah = C_banco (Wh) / V_sistema
```

**Exemplo — veleiro de cruzeiro (sistema 12V):**

```jsx
Consumo diário: 1.000 Wh
Autonomia: 2 dias sem recarga
Consumo total: 2.000 Wh

Com AGM (DOD 50%):
C_banco = 2.000 / 0,5 = 4.000 Wh
Ah = 4.000 / 12 = 333 Ah
Com margem 25%: 333 × 1,25 = 416 Ah → 2 × 200Ah AGM em paralelo

Com LiFePO4 (DOD 80%):
C_banco = 2.000 / 0,8 = 2.500 Wh
Ah = 2.500 / 12 = 208 Ah
Com margem 25%: 208 × 1,25 = 260 Ah → 1 × 300Ah LiFePO4 (suficiente)
```

## Efeito Peukert — a realidade das baterias de chumbo

A capacidade nominal de uma bateria de chumbo-ácido é medida a C/20 (descarga em 20 horas). Em descargas mais rápidas, a capacidade real é menor:

| Taxa de descarga | Tempo | Capacidade real (bateria 100Ah nominal) |
| --- | --- | --- |
| C/20 (5A) | 20h | 100Ah (100%) |
| C/10 (10A) | 10h | ~85Ah (85%) |
| C/5 (20A) | 5h | ~70Ah (70%) |
| C/2 (50A) | ~1h | ~50Ah (50%) |

**Conclusão:** quanto mais rápido você descarrega, menos capacidade tem. Para consumos altos (inversor, ar-condicionado), a capacidade real é significativamente menor que a nominal.

**LiFePO4 apresenta efeito Peukert muito menos pronunciado no uso náutico típico**, mas isso não elimina limites de C-rate, aquecimento, atuação do BMS e eventuais perdas em descargas severas.

## Sistemas em paralelo e em série

**Baterias em paralelo (mais capacidade, mesma tensão):**

```jsx
2 × 12V 100Ah em paralelo = 12V 200Ah
Cuidado: baterias em paralelo devem ter a MESMA tensão antes de conectar
Baterias de idades diferentes em paralelo: problemas de balanceamento
```

**Baterias em série (mais tensão, mesma capacidade):**

```jsx
2 × 12V 100Ah em série = 24V 100Ah
Cuidado: desbalanceamento de tensão entre baterias — verificar periodicamente
```

**Combinação série/paralelo:**

```jsx
4 × 12V 100Ah: 2 séries de 2 (24V) em paralelo = 24V 200Ah
Mais complexo — manter baterias idênticas (mesma marca, modelo, lote, idade)
```

## Banco de partida vs banco de serviço

**Banco de partida:**

- Função: fornecer alta corrente por curto período para partida do motor
- Tecnologia: chumbo-ácido (excelente em alta corrente instantânea)
- Capacidade: baseada no CCA (Cold Cranking Amperes) — não na capacidade em Ah
- DOD: raramente descarrega — a partida usa < 5% da capacidade
- Nunca usar como banco de serviço

**Banco de serviço:**

- Função: alimentar todos os equipamentos quando o motor está desligado
- Tecnologia: AGM, GEL ou LiFePO4
- Capacidade: calculada pelo método acima
- DOD: ciclo profundo regular

**Isolamento entre bancos:**

Os dois bancos devem ser isolados — o banco de serviço não pode descarregar o banco de partida. Isolamento por: chave manual (Bi-Banco), VSR/ACR (automático), ou diodo de isolamento (com perda de tensão).

## Decisão: AGM vs GEL vs LiFePO4

| Critério | AGM | GEL | LiFePO4 |
| --- | --- | --- | --- |
| Custo inicial | R$500–800/100Ah | R$600–900/100Ah | R$2.000–4.000/100Ah |
| Ciclos de vida | 300–500 ciclos | 500–800 ciclos | 2.000–5.000 ciclos |
| DOD máximo | 50% | 50% | 80% |
| Peso (100Ah 12V) | ~28kg | ~28kg | ~12–14kg |
| Custo por ciclo | Alto | Médio | Baixo (no longo prazo) |
| Complexidade | Baixa | Baixa | Alta (BMS obrigatório) |
| Melhor aplicação | Uso esporádico | Uso regular moderado | Uso intensivo / veleiro |

**Custo por Wh útil ao longo da vida (exemplo ilustrativo):**

```jsx
AGM 100Ah (50% DOD = 50Ah úteis × 12V = 600Wh × 400 ciclos = 240.000 Wh totais):
R$600 / 240.000 Wh = R$0,0025/Wh

LiFePO4 100Ah (80% DOD = 80Ah úteis × 12V = 960Wh × 3.000 ciclos = 2.880.000 Wh totais):
R$3.000 / 2.880.000 Wh = R$0,001/Wh

→ O resultado sugere vantagem econômica de longo prazo, mas o fator real depende de ciclo, temperatura, regime de carga, custo de integração e vida útil efetivamente atingida
```

## Problemas por dimensionamento incorreto

| Erro | Consequência |
| --- | --- |
| Banco subdimensionado | Descargas profundas frequentes → vida útil reduzida |
| Banco superdimensionado | Custo desnecessário, peso excessivo, sistema de geração insuficiente para recarregar |
| Perfil de uso irreal | "Nunca fico sem energia" mas usa gerador todo dia |
| Não considerar envelhecimento | Banco de 3 anos tem 70–80% da capacidade nominal — recalcular |
| Usar capacidade nominal em vez da real | Monitor indicará SoC incorreto, autonomia superestimada |

## Boas práticas profissionais

- Levantar o consumo real (com amperímetro de alicate durante uma saída típica) — não estimar
- Adotar reserva de projeto compatível com a previsibilidade do uso; em muitos cenários práticos, 15–30% é uma boa faixa inicial
- Considerar temperatura ambiente — capacidade de chumbo-ácido cai 1% por grau abaixo de 25°C
- Instalar monitor de bateria para validar o dimensionamento após instalação
- Revisar o dimensionamento a cada 2–3 anos (envelhecimento e novos consumidores)

## Relação com outros sistemas

- **Monitor de bateria:** valida o dimensionamento — SoC real após uso típico
- **Sistema de geração:** banco maior exige mais geração (solar, alternador, gerador)
- **BMS (lítio):** parte integrante do banco LiFePO4
- **Inversor:** consumo do inversor é a maior carga DC — determina o banco
- **Projeto elétrico:** dimensionamento de banco é o primeiro cálculo após levantamento de cargas

## Como ensinar este tópico

**Sequência recomendada:**

1. Levantamento de cargas ao vivo em uma embarcação real
2. Cálculo do consumo diário — mostrar que os números são menores (ou maiores) do que o imaginado
3. Autonomia desejada × DOD = capacidade necessária (fórmula direta)
4. Comparar: AGM vs LiFePO4 — custo total de posse, não apenas preço inicial
5. Exercício: dado uma embarcação com lista de equipamentos, calcular o banco

**Conceito-chave para fixar:**

"O banco correto não é o maior que cabe. É o menor que atende à autonomia desejada com DOD correto e margem de segurança."

## FAQ

**Posso misturar baterias de marcas diferentes no mesmo banco?**

Tecnicamente possível, mas não recomendado. Diferenças de capacidade real, curva de carga e resistência interna causam desbalanceamento progressivo. O banco passa a ser limitado pela bateria mais fraca.

**Qual autonomia devo projetar para uma lancha de uso diário?**

Para uso diário com retorno à marina: 1 dia de autonomia é suficiente (o carregador repõe à noite). Para veleiro ou cruzeiro: mínimo 2–3 dias sem recarga.

**Como atualizar o dimensionamento quando adiciono um novo equipamento?**

Recalcular o consumo diário adicionando o novo equipamento. Se a nova capacidade necessária superar o banco instalado em > 10%, considera-se ampliar o banco ou reduzir outra carga.

**Bateria de 200Ah pode ser ligada em paralelo com bateria de 100Ah?**

Como regra de projeto, não é boa prática formar um banco de serviço permanente com capacidades, idades ou estados de saúde muito diferentes. Em teoria, é possível interligar baterias eletricamente compatíveis; na prática, diferenças de resistência interna, curva de carga e envelhecimento fazem o conjunto trabalhar mal e dificultam balanceamento e diagnóstico. A solução profissional é padronizar o banco.

## Integração com outras notas

- [[Dimensionamento de Cabos DC — Cálculo Prático]]
- [[DC vs AC — Corrente Contínua e Alternada]]
- [[Diagrama Unifilar — Documentação do Sistema Elétrico]]
- [[Fase e Neutro]]
- [[Ferramentas do Eletricista Náutico]]
- [[Inspeção de Cabos Terminais e Conexões]]
- [[Lei de Ohm e Cálculos Básicos]]
- [[Leitura de Diagramas e Esquemas Elétricos]]

## Perguntas que esta nota responde

- O que é Dimensionamento de Banco de Baterias — Cálculo de Autonomia em instalações elétricas náuticas?
