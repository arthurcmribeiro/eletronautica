---
title: "Atuador Linear"
note_type: "component"
domain: "60_Automacao_Conectividade_e_Monitoramento"
source_file: "ATUADOR LINEAR 5a319734f7fb8392ad8b81db5fd17f98.md"
status: "premium-l3"
fase_6_reescrita: 91
reviewed_on: "2026-04-26"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://webstore.iec.ch/publication/2697"
  - "https://www.lewmar.com/"
  - "https://www.linakmarine.com/"
  - "https://www.thomsonlinear.com/"
review_level: "engineering-curated"
aliases:
  - "ATUADOR LINEAR"
  - "Linear actuator"
  - "Atuador eletromecânico linear"
  - "Push-pull actuator"
  - "Electric ram"
  - "Servo linear"
  - "Spindle drive marine"
seo_title: "Atuador linear náutico: ABYC E-11/P-22, IEC 60204-1, IP66/67, dimensionamento força/curso/duty, fabricantes Lewmar/Linak/Thomson"
seo_description: "Guia técnico premium do atuador linear (linear actuator) em embarcações: princípio (motor DC + redutor + parafuso de esferas/trapezoidal), aplicações (capota retrátil, escotilha, plataforma popa, flap, davit, trim tab), dimensionamento força × curso × duty cycle × stall current, ABYC E-11/P-22/H-29, IEC 60204-1, IP66/67, fabricantes (Lewmar, Linak, Thomson, SKF, Bosch Rexroth, LinMot), proteção elétrica fusível ANL/MIDI, fim de curso (limit switch / Hall sensor / encoder)."
seo_keywords:
  - "atuador linear barco"
  - "linear actuator marine"
  - "Lewmar atuador"
  - "Linak Marine"
  - "Thomson actuator"
  - "atuador eletromecânico DC"
  - "stall current atuador"
  - "duty cycle linear actuator"
  - "limit switch IP67"
  - "atuador hidráulico vs elétrico"
  - "ABYC E-11"
  - "IEC 60204-1"
geo_queries:
  - "Como dimensionar atuador linear para escotilha náutica?"
  - "Atuador linear elétrico ou hidráulico — qual escolher?"
  - "Por que o atuador linear trava em mar agitado?"
  - "Stall current de atuador linear: como calcular?"
  - "Lewmar vs Linak vs Thomson: qual escolher para barco?"
  - "Atuador linear sem fim de curso é seguro?"
  - "Como integrar atuador ao MFD via NMEA 2000?"
  - "Atuador linear IP66 vale para deck molhado?"
  - "Como dimensionar fusível para atuador linear 12V/30A?"
  - "Atuador linear para flap eletricamente acionado vs hidráulico?"
normas_citadas:
  - "ABYC E-11 (AC and DC Electrical Systems on Boats)"
  - "ABYC P-22 (Steering Systems)"
  - "ABYC H-29 (Hatches, Companionway Doors and Gangway)"
  - "ABYC TE-30 (Electronic Equipment Installation Standards)"
  - "ABYC TE-04 (Lightning Protection)"
  - "IEC 60204-1 (Safety of machinery — Electrical equipment of machines)"
  - "IEC 60034-1 (Rotating electrical machines — Rating and performance)"
  - "IEC 60068 (Environmental testing)"
  - "IEC 60529 (IP code)"
  - "IEC 61000-6-1/-3 (EMC)"
  - "ISO 12100 (Safety of machinery — General principles)"
  - "ISO 13849-1 (Safety-related parts of control systems)"
  - "ISO 9013 (Marine environments — referência cruzada)"
  - "ISO 4413 (Hydraulic fluid power — referência cruzada para alternativa hidráulica)"
  - "ISO 8528 (Reciprocating internal combustion engine driven alternating current generating sets)"
  - "EN ISO 12100 (CE Machinery)"
  - "EN ISO 13849-1 / EN 62061 (Safety functions)"
  - "CE Machinery Directive 2006/42/EC"
  - "EU Directive 2014/30/EU (EMC)"
  - "EU Directive 2014/35/EU (LVD)"
  - "EU 2013/53/EU (Recreational Craft Directive — RCD)"
  - "NEMA Standards (Motor enclosure)"
  - "ABNT NBR 5410 (Instalações elétricas BT)"
  - "ABNT NBR 14728 (Embarcações de recreio)"
  - "ABNT NBR ISO 12100 (Segurança de máquinas)"
  - "ABNT NBR IEC 60529 (IP)"
  - "DPC NORMAM-211/DPC (esporte e recreio)"
  - "DPC NORMAM-201/DPC (comerciais)"
  - "Manual técnico Lewmar Linear Actuator HC / Mamba (legacy)"
  - "Manual técnico Linak Marine LA12/LA20/LA28/LA31/LA36/LA37"
  - "Manual técnico Thomson Marine Electrak HD / 1 / 10 / 50"
  - "Manual técnico SKF CAHB"
  - "Manual técnico Bosch Rexroth EMA"
  - "Manual técnico LinMot Marine"
  - "Manual técnico Octopus Hydraulic Actuator (alternativa hidráulica)"
  - "Manual técnico Bug Buster (USA marine actuator)"
related_notes:
  - "Plataforma de Popa Elétrica - Hidráulica"
  - "Flap"
  - "Motor de Trim - Tilt"
  - "Catraca"
  - "Davit - Munk - Guindaste de Bote - Tender Lift"
  - "Piloto Automático"
  - "Automação de Bordo — Sistemas Domoticos"
  - "Sistema de Alarme Geral - Painel de Alarmes"
  - "Relés e Relés de Estado Sólido"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Disjuntores (DC) e (AC)"
  - "Bonding — Sistema de Interligação de Massas"
  - "Cabeamento Náutico"
  - "Dimensionamento de Cabos DC — Cálculo Prático"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
---

# Atuador Linear

> [!abstract] Resumo técnico
> O **atuador linear (linear actuator)** é o conjunto eletromecânico que converte **rotação do motor DC** em **movimento linear (push-pull)** via **redutor + parafuso de esferas (ball screw) ou parafuso trapezoidal (lead screw)**. Em embarcações, é o atuador padrão para **escotilhas elétricas, capotas retráteis (T-top), plataforma de popa elétrica (vide [[Plataforma de Popa Elétrica - Hidráulica]]), flap eletro-mecânico (vide [[Flap]]), trim-tilt (vide [[Motor de Trim - Tilt]]), davit/guindaste de bote (vide [[Davit - Munk - Guindaste de Bote - Tender Lift]])**, assento helm ajustável e portas elétricas. **Não confundir com atuador hidráulico** — o linear elétrico tem força menor (50-1000+ kgf) mas é mais simples, sem reservatório de óleo. Padrões: **ABYC E-11** (wiring) + **ABYC P-22** (steering systems) + **ABYC H-29** (hatches) + **IEC 60204-1** (safety of machinery) + **IEC 60034-1** (motor) + **IEC 60529** (IP66/67 marine) + **ISO 12100/13849-1** (safety of machinery) + **CE Machinery Directive 2006/42/EC**. Dimensionamento crítico: **força (kgf), curso (mm), velocidade (mm/s), duty cycle (%), corrente nominal e de bloqueio (stall current — 5-10× nominal)**, fim de curso (limit switch / Hall sensor / encoder absoluto). Fabricantes premium: **Lewmar HC, Linak Marine LA12/LA20/LA28/LA31/LA36, Thomson Electrak HD / 1 / 10 / 50, SKF CAHB, Bosch Rexroth EMA, LinMot, Bug Buster (USA marine)**.

> [!tldr] TL;DR — 10 regras inegociáveis
> 1. **Dimensionar atuador para 1,5-2× a força nominal de pico** prevista na aplicação. Em escotilha pesada com vento contra, 100 kgf nominal facilmente vira 200 kgf de pico — atuador subdimensionado trava (stall) e queima.
> 2. **Stall current (corrente de bloqueio) é 5-10× a corrente nominal.** Atuador 12V/10A nominal pode pico em 80-120A no stall. Fusível ANL/MIDI dimensionado a 125% do pico (não nominal); cabo dimensionado idem.
> 3. **Duty cycle do fabricante é absoluto.** Maioria especifica 25% ou 50% (5 min ON / 15 min OFF, etc.). Operação contínua queima motor em horas.
> 4. **Fim de curso (limit switch) obrigatório.** Sem limit switch, atuador empurra até travar mecanicamente → stall current → fusível abre OU motor queima. Limit switch interno em todos os modelos profissionais.
> 5. **IP66/IP67 mínimo em deck/exposto.** IP54 não basta em ambiente marine real (chuva, spray salino). Modelos premium IP67 ou IP69K em uso prolongado.
> 6. **Reversão suave via H-bridge dedicada** (driver eletrônico) ou contatores reversores (relés DPDT) — comutação direta queima escovas e chicoteia mecânica.
> 7. **Anti-pinch protection** em escotilha/capota motorizada — sensor de torque OU encoder + algoritmo detecta obstrução (criança, dedo, animal) → para movimento → reverso. ISO 13849-1.
> 8. **Bonding** da carcaça (ABYC E-11.16) + **surge protection** (ABYC TE-04) — atuador em mastro / deck exposto a relâmpago.
> 9. **Cabo flexível** apropriado para movimento contínuo (chain-flex / drag chain). Cabo rígido em atuador móvel rompe internamente em 1-2 anos de uso.
> 10. **Lubrificação periódica** do parafuso de esferas (graxa marine sintética NLGI 2 ou específica do fabricante). Sem lubrificação: atrito sobe → corrente sobe → eficiência cai → falha precoce.

> [!danger] Cenários de risco
> - **Atuador trava em escotilha com mar agitado** → stall current → fusível abre OU motor queima → escotilha fica entreaberta com onda batendo → alagamento progressivo. **Prevenção:** atuador 1,5-2× margem; backup manual mecânico; alarme de stall.
> - **Esmagamento por escotilha/capota motorizada:** anti-pinch ausente / mal calibrado + criança/animal + escotilha grande → lesão grave / morte. **Prevenção:** ISO 13849-1 PL "c" mínimo; sensor de torque; treinamento; chave de emergência acessível.
> - **Cabo flexível rompendo internamente após 6-12 meses:** cabo rígido em uso móvel → quebra de fio interno → curto intermitente → motor pulsa → desgaste mecânico + risco de fogo. **Prevenção:** cabo chain-flex marine (Lapp Olflex, Igus Chainflex); roteamento sem dobra acima da rotação mínima.
> - **Choque elétrico em atuador AC** mal aterrado em ambiente molhado: 220V em capota T-top + cockpit alagado → choque ao tocar carcaça. **Prevenção:** SEMPRE 12V/24V DC quando possível; ELCI 30 mA em AC; bonding; ABYC E-11.
> - **Falha catastrófica de davit/guindaste de bote** com bote pendurado: atuador sobrecarregado + sem sensor de torque → cabo de aço rompe → bote cai 4-8 m → impacto + lesão. **Prevenção:** dimensionamento + fator de segurança 5:1; inspeção semestral; cabo aço EN 14492-2 vide [[Davit - Munk - Guindaste de Bote - Tender Lift]].
> - **Surto atmosférico via cabo do atuador** queima driver + chartplotter + fusíveis: instalação em mastro sem surge protection. **Prevenção:** ABYC TE-04 surge protector; bonding mastro-quilha.
> - **Operação contínua além do duty cycle** (operador insistindo em "fechar" capota travada): motor 130-160°C → enrolamento queima. **Prevenção:** treinar operador; alarme de overheating no driver eletrônico.
> - **Fim de curso (limit switch) falha:** atuador empurra contra batente mecânico → stall sustained → fogo elétrico em casos extremos. **Prevenção:** limit switch redundante (mecânico + Hall); diagnóstico semestral; fusível protege.
> - **Fluido (graxa) ressecando no parafuso após 5+ anos** sem manutenção: atrito sobe → consumo elétrico sobe → falha precoce do motor. **Prevenção:** lubrificação anual; trocar graxa a cada 5 anos.
> - **Mistura de fluidos errados em modelo hidráulico-assistido** (alguns atuadores são electro-hydraulic): ATF + óleo motor → vedação degrada → vazamento. **Prevenção:** consultar manual; fluido específico (vide [[Óleos Hidráulicos Marine — Guia Completo]]).

## O que é (definição rigorosa)

O **atuador linear** combina:

```
[Motor DC 12/24V] ── [Redutor planetário] ── [Parafuso de esferas/trapezoidal] ── [Haste / spindle] ── [Carga]
        │                                                                                │
        └── [Driver eletrônico ou controle direto via relé/contator] ─── [Limit switch / encoder]
```

### Componentes

1. **Motor DC** (12/24V padrão; alguns 110/220V AC industriais).
2. **Redutor planetário** (relação típica 50:1 a 200:1) — multiplica torque, divide velocidade.
3. **Parafuso de esferas (ball screw)** ou **parafuso trapezoidal (lead screw / Acme)**:
   - Ball screw: alta eficiência (90%+), reversível, premium.
   - Acme: eficiência média (40-60%), self-locking quando desligado, econômico.
4. **Haste com camisa** + **bucha lateral** para suportar carga lateral.
5. **Limit switch** (microinterruptor mecânico) ou **Hall sensor** ou **encoder absoluto** (premium) — fim de curso.
6. **Driver eletrônico** (em modelos profissionais) com proteção térmica + reversão suave + anti-pinch.

### Aplicações típicas em embarcação

| Aplicação | Curso típico | Força típica | Modelo típico |
|-----------|--------------|--------------|----------------|
| **Escotilha motorizada** | 200-500 mm | 50-200 kgf | Linak LA20 / LA28 |
| **Capota T-top retrátil** | 400-1000 mm | 100-300 kgf | Linak LA31 / Lewmar HC |
| **Plataforma popa elétrica** | 500-1200 mm | 300-1000+ kgf | Thomson Electrak HD; Lewmar |
| **Flap eletromecânico (Lenco-style)** | 50-150 mm | 30-100 kgf | Lenco proprietário |
| **Trim-tilt** | 200-400 mm | 50-150 kgf | OEM (Mercury/Yamaha) |
| **Davit (sistema completo)** | 1000-3000 mm | 200-1000 kgf | OEM Davit + atuador |
| **Mesa elétrica salão** | 100-500 mm | 50-200 kgf | Linak LA12 / LA20 |
| **Helm seat ajustável** | 100-300 mm | 30-100 kgf | Linak LA12 |
| **Porta motorizada** | 200-500 mm | 50-200 kgf | Linak / Thomson |

## Comparação técnica entre tecnologias

### Parafuso de esferas vs trapezoidal

| Parâmetro | Ball Screw | Acme (Trapezoidal) |
|-----------|------------|---------------------|
| **Eficiência** | 90-95% | 40-60% |
| **Reversível** | Sim | Não (self-locking) |
| **Custo** | Alto | Baixo |
| **Vida útil** | 50.000-500.000 ciclos | 10.000-100.000 ciclos |
| **Aplicação** | Premium (regular use) | Econômica (uso ocasional) |
| **Self-lock no off** | Não (precisa freio) | Sim |

### Atuador elétrico vs hidráulico

| Parâmetro | Linear elétrico | Hidráulico |
|-----------|-----------------|------------|
| **Força máxima** | 50-1000 kgf típica | 500-10.000+ kgf |
| **Velocidade** | 5-50 mm/s | 50-200 mm/s |
| **Manutenção** | Mínima (lubrificação) | Fluido + filtro + vedação |
| **Custo total** | Médio | Alto |
| **Ruído** | Médio (motor + redutor) | Baixo |
| **Resposta** | Rápida | Muito rápida |
| **Aplicação** | Cargas leves-médias | Cargas pesadas (plataforma >1 ton) |

## Onde se encaixa

```
[Bateria] ── [Disjuntor / Fusível] ── [Relé / Contator / Driver eletrônico]
                                                  │
                                          ┌───────┴───────┐
                                          │               │
                                  [Botão / chave]  [NMEA 2000 control]
                                                  │
                                                  └── [Atuador linear]
                                                          │
                                                  [Limit switch / encoder]
```

## Fabricantes e modelos dominantes

### Marine-specific premium

- **Lewmar HC Linear Actuator** — referência para escotilhas/capotas.
- **Linak Marine LA12 / LA20 / LA28 / LA31 / LA36 / LA37** — premium DK.
- **Thomson Electrak HD / Electrak 1 / 10 / 50** — USA premium.

### Generalistas industriais com linha marine

- **SKF CAHB** — sueco premium.
- **Bosch Rexroth EMA** — alemão.
- **LinMot** — direct-drive sem redutor (high-end).
- **Igus Drylin** — econômico.

### Específicos para aplicações marine

- **Lenco Marine Trim Tabs** — flap eletromecânico.
- **Bennett Trim Tabs** — flap hidráulico ou elétrico.
- **Octopus Hydraulic Actuator** — para piloto automático (vide [[Piloto Automático]]).
- **Bug Buster (USA marine)** — atuadores marine custom.

> [!example] Comparação Brasil 2024-2026 (importado)
> | Equipamento | Força × Curso | Preço (R$) |
> |-------------|----------------|------------|
> | Linak LA12 (mesa/seat) | 100 kgf × 200 mm | 1.500-3.000 |
> | Linak LA20 (escotilha leve) | 200 kgf × 300 mm | 3.000-5.500 |
> | Linak LA28 (capota T-top) | 350 kgf × 500 mm | 5.500-9.500 |
> | Lewmar HC Linear | 250 kgf × 400 mm | 4.500-8.000 |
> | Thomson Electrak HD | 1000 kgf × 1000 mm | 18.000-35.000 |
> | Lenco Trim Tabs Pair Standard | — | 4.500-7.500 |
> | Octopus Linear (piloto) | 200 kgf × 250 mm | 8.000-14.000 |

## Princípio de operação detalhado

### Cálculo de força e velocidade

```
F = T × η × 2π / p
```

Onde:
- F = força linear (N).
- T = torque do motor (N·m).
- η = eficiência (0,4-0,95 conforme parafuso).
- p = passo do parafuso (m/rev).

Para velocidade:

```
v = n × p / 60
```

Onde n = RPM do motor.

### Stall current (corrente de bloqueio)

Quando atuador trava (carga > capacidade):

```
I_stall = V / R_armadura ≈ 5-10 × I_nominal
```

Em motor DC com R_armadura ≈ 0,5 Ω e V = 12V → I_stall ≈ 24A se nominal 4-5A.

### Duty cycle

```
Duty = (t_ON / t_total) × 100%
```

Modelos típicos: 10%, 25%, 50%. Operação acima do duty → temperatura excede classe do motor (Classe B 130°C, F 155°C, H 180°C) → vida útil cai exponencialmente.

## Instalação correta (ABYC E-11 + IEC 60204-1 + ISO 12100)

### Mecânica

1. **Pontos de ancoragem rígidos** — chassis ou estrutura reforçada.
2. **Alinhamento** com a direção de movimento (sem cargas laterais excessivas).
3. **Fim de curso** (mecânico + elétrico redundante).
4. **Cabos chain-flex** em uso móvel.
5. **Lubrificação inicial** + cronograma anual.

### Elétrica

1. **Circuito dedicado** com fusível ANL/MIDI/ATC para corrente de pico (stall).
2. **Cabo dimensionado** para corrente nominal + pico curto (queda <3%).
3. **Reversão via contator DPDT** ou driver eletrônico H-bridge.
4. **Bonding** da carcaça (ABYC E-11.16).
5. **Surge protection** se em deck/mastro (ABYC TE-04).

### Segurança (ISO 13849-1)

1. **Anti-pinch / sensor de torque** em escotilha/capota.
2. **Chave de emergência** acessível.
3. **PL ≥ "c"** em aplicação que envolve risco a pessoa.

## Falhas comuns

| Falha | Causa | Solução |
|-------|-------|---------|
| Atuador trava | Sobrecarga / batente | Dimensionar 1,5-2× margem |
| Motor queima | Duty cycle excedido | Treinar operador; alarme |
| Cabo rompe | Cabo rígido em movimento | Chain-flex marine |
| Fim de curso falha | Limit switch defeituoso | Substituir; redundância |
| Stall current alto | Atrito por falta de lubrificação | Lubrificar / trocar graxa |
| Reversão chicoteia | Comutação direta sem ramp | Driver eletrônico |
| Choque ao tocar | AC sem aterramento | Bonding; ELCI |
| Falha em chuva | IP inadequado | IP66/67+ |
| Esmagamento | Anti-pinch ausente | Sensor torque + PL "c" |

## Boas práticas

- **Dimensionar 1,5-2× margem** em força.
- **Lubrificação anual** + troca a cada 5 anos.
- **Inspeção semestral** mecânica + elétrica.
- **Cabo chain-flex** em movimento.
- **Fim de curso redundante**.
- **Driver eletrônico** com soft start/stop.
- **Bonding** da carcaça.
- **Documentar** modelo + força + curso + duty.
- **Backup manual mecânico** em escotilha/capota crítica.
- **Treinamento** da tripulação.

## Erros comuns

- "Mais força = melhor." → Falso. Sobre-dimensionado tem força excessiva que destroi mecânica adjacente.
- "Cabo rígido funciona em movimento." → Falso. Quebra em 6-12 meses.
- "Fim de curso é opcional." → Falso. Sem ele, atuador empurra batente → fogo.
- "Anti-pinch é luxo." → ISO 13849-1 PL "c" obrigatório em risco a pessoa.
- "AC é igual a DC em barco." → Em ambiente molhado, AC sem ELCI = perigo.

## Glossário

- **Atuador linear:** mecanismo de movimento linear.
- **Push-pull:** força em ambos sentidos.
- **Ball screw:** parafuso de esferas (alta eficiência).
- **Acme / lead screw:** parafuso trapezoidal.
- **Self-locking:** trava sem energia (parafuso trapezoidal).
- **Stall current:** corrente de bloqueio (5-10× nominal).
- **Duty cycle:** % tempo ON.
- **Limit switch:** fim de curso mecânico.
- **Hall sensor:** sensor de fim de curso por efeito Hall.
- **Encoder absoluto:** posição precisa contínua.
- **H-bridge:** driver de motor reversível.
- **Soft start / stop:** rampa de aceleração.
- **Anti-pinch:** detecção de obstrução.
- **Chain-flex:** cabo flexível para movimento.
- **Drag chain:** corrente porta-cabos.
- **Class B/F/H:** classes de isolamento térmico (130/155/180°C).
- **PL (Performance Level):** nível de segurança ISO 13849-1.
- **IP code:** Ingress Protection.
- **EMC:** electromagnetic compatibility.
- **NMEA 2000:** protocolo de instrumento.
- **CE Machinery:** diretiva europeia 2006/42/EC.
- **Bonding:** interligação de massas (ABYC E-11.16).
- **Vide [[Plataforma de Popa Elétrica - Hidráulica]]**, [[Flap]], [[Davit - Munk - Guindaste de Bote - Tender Lift]] — aplicações específicas.

## Integração com outras notas

- [[Plataforma de Popa Elétrica - Hidráulica]] — aplicação típica.
- [[Flap]] — alternativa eletromecânica vs hidráulica.
- [[Motor de Trim - Tilt]] — atuador específico OEM.
- [[Davit - Munk - Guindaste de Bote - Tender Lift]] — sistema com atuador.
- [[Catraca]] — alternativa para algumas aplicações.
- [[Piloto Automático]] — atuador linear é uma das tecnologias.
- [[Automação de Bordo — Sistemas Domoticos]] — integração de cenas.
- [[Sistema de Alarme Geral - Painel de Alarmes]] — alarme de stall.
- [[Relés e Relés de Estado Sólido]] — comutação.
- [[Fusíveis DC — Proteção Contra Sobrecorrente]] / [[Disjuntores (DC) e (AC)]] — proteção.
- [[Bonding — Sistema de Interligação de Massas]] — aterramento.
- [[Cabeamento Náutico]] / [[Dimensionamento de Cabos DC — Cálculo Prático]] — bitola.
- [[Quadro Elétrico e Painel de Distribuição AC-DC]] — disjuntor.
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]] — diagnóstico.

## Perguntas que esta nota responde

- Como dimensionar atuador linear para escotilha náutica?
- Atuador linear elétrico ou hidráulico — qual escolher?
- Por que o atuador linear trava em mar agitado?
- Stall current de atuador linear: como calcular?
- Lewmar vs Linak vs Thomson: qual escolher para barco?
- Atuador linear sem fim de curso é seguro?
- Como integrar atuador ao MFD via NMEA 2000?
- Atuador linear IP66 vale para deck molhado?
- Como dimensionar fusível para atuador linear 12V/30A?
- Atuador linear para flap eletricamente acionado vs hidráulico?
