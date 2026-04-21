---
title: "Linha Pesada (AC)"
note_type: "system"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "LINHA PESADA (AC) 6bd19734f7fb836e818f01ed1f949d26.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "41"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
  - "internacional"
normas_citadas:
  - "ABYC E-11 (2023) — AC & DC Electrical Systems on Boats"
  - "ABYC E-8 — AC Generators"
  - "ABYC A-6 — Ground Fault Protection"
  - "ABYC A-22 — Marinas and Boatyards"
  - "ABYC H-2 — Ventilation (motor loads)"
  - "ABYC TE-4 — Lightning Protection"
  - "ISO 13297:2020 — Small craft — Electrical systems — AC and DC"
  - "ISO 8846:2020 — Small craft — Electrical devices — Protection against ignition"
  - "IEC 60364-7-709 — Low-voltage electrical installations — Marinas and similar"
  - "IEC 60364-4-43 — Protection against overcurrent"
  - "IEC 60364-5-52 — Selection and erection of wiring systems"
  - "IEC 60092-101 — Electrical installations in ships — Definitions"
  - "IEC 60092-201 — System design"
  - "IEC 60092-202 — System design — Protection"
  - "IEC 60092-301 — Equipment — Generators, converters, transformers"
  - "IEC 60092-352 — Cables for shipboard installations"
  - "NEC Art. 210 — Branch circuits"
  - "NEC Art. 215 — Feeders"
  - "NEC Art. 220 — Branch-circuit, feeder and service calculations"
  - "NEC Art. 240 — Overcurrent protection"
  - "NEC Art. 310 — Conductors for general wiring"
  - "NEC Art. 430 — Motors, motor circuits and controllers"
  - "NEC Art. 440 — Air-conditioning and refrigerating equipment"
  - "NEC Art. 555 — Marinas, Boatyards, Boat Basins"
  - "NFPA 70 (NEC) — National Electrical Code"
  - "NFPA 302 — Pleasure and Commercial Motor Craft"
  - "UL 489 — Molded-Case Circuit Breakers"
  - "UL 1077 — Supplementary Protectors"
  - "NBR 5410:2004 + emendas — Instalações elétricas de baixa tensão"
  - "NBR IEC 60364-4-41 — Proteção contra choques elétricos"
  - "NBR IEC 60364-4-43 — Proteção contra sobrecorrentes"
  - "NBR IEC 60364-5-52 — Seleção e instalação de linhas elétricas"
  - "NBR 10898 — Sistema de iluminação de emergência (referência cruzada)"
  - "DNV-RU-SHIP Pt 4 Ch 8 — Electrical installations"
  - "Lloyd's Register Rules Pt 6 — Electrical"
  - "CE-RCD Directive 2013/53/EU — Recreational Craft Directive"
  - "NORMAM-211/DPC — Esporte e recreio"
  - "NORMAM-201/204/DPC — Comercial / SMM"
review_level: "engineering-curated"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "LINHA PESADA (AC)"
  - "Circuitos AC dedicados"
seo_title: "Linha pesada AC em embarcações: cargas dedicadas, seletividade e gestão de potência"
seo_description: "Critérios profissionais para projetar linha pesada AC em embarcações: cargas dedicadas, correntes de partida, seletividade, shore power, gerador, inversor e proteção."
seo_keywords:
  - "linha pesada AC embarcação"
  - "cargas dedicadas barco"
  - "ar condicionado shore power"
  - "gestão de potência embarcação"
geo_queries:
  - "Como projetar linha pesada AC para ar-condicionado e boiler em embarcação?"
  - "Quando uma carga deve ter circuito AC dedicado no barco?"
related_notes:
  - "Ar-Condicionado Marine — Sistema Completo"
  - "CAIS (Pier) (AC)"
  - "Chaves Seletoras (AC)"
  - "Contatores (AC)"
  - "Gerador (AC)"
  - "Inversora (DC To AC)"
  - "Linha Leve (AC)"
  - "Proteção Dr"
---

# Linha Pesada (AC)

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **Linha pesada ≠ apenas alta corrente.** O critério é combinado: carga sustentada, inrush severo, criticidade operacional, ou impacto na gestão de potência global do barco.
> 2. **Circuito dedicado por carga pesada.** Compartilhar ar-condicionado, boiler e carregador no mesmo ramal é erro de projeto, não economia — destrói seletividade e dificulta diagnóstico.
> 3. **Dimensione por MCA + MOCP da plaqueta**, não por "watts". Compressores usam **MCA** (Minimum Circuit Ampacity) para cabo e **MOCP** (Maximum Overcurrent Protection) para disjuntor — ambos já contemplam partida e ciclo real.
> 4. **Inrush de compressor AC ≈ 6–8× FLA** em partida direta. Soft starter reduz para **2–3× FLA** e frequentemente viabiliza operação em shore 30 A ou em gerador menor.
> 5. **Queda de tensão > 3% exige reanálise.** Partidas sob subtensão aumentam aquecimento do enrolamento, reduzem torque, atrasam a partida e elevam falha prematura de compressor.
> 6. **Seletividade não se resolve com disjuntor maior.** Coordenar proteção ↔ cabo ↔ contator ↔ carga ↔ fonte. Aumentar o disjuntor só desloca o ponto de falha para o ponto mais fraco seguinte.
> 7. **Power Management System (PMS) é obrigatório** em embarcação com múltiplas cargas pesadas: prioridade manual, load shedding automático, shore current limiter e intertravamento de partida entre cargas grandes.
> 8. **Família normativa primária:** ABYC E-11 + NEC Art. 430/440/555 (EUA); NBR 5410 + IEC 60364-7-709 (Brasil); ISO 13297 + IEC 60092-series (internacional/comercial); CE-RCD para Europa.
> 9. **Transferência entre fontes exige ATS coordenado** sem múltiplos bonds N-PE simultâneos. O bond neutro-terra só pode existir na fonte ativa (shore **OU** gerador **OU** inversor) — nunca nas três ao mesmo tempo, sob pena de corrente de neutro pela água (ESD).

> [!danger] Quando chamar um especialista
> 1. **Disjuntor do pedestal do cais abrindo toda vez que o ar-condicionado parte** — sinal de shore subdimensionado, falta de soft starter ou carga simultânea descontrolada. Nunca "peça disjuntor maior" ao operador da marina como solução.
> 2. **Conector shore power aquecendo, derretendo ou com marcas de arco** em operação contínua — corrente acima da capacidade real, oxidação do contato, torque perdido ou cabo subdimensionado. Risco de incêndio no cordame e no pé-de-galinha.
> 3. **Gerador que não sustenta a partida do compressor** mesmo dentro da placa do fabricante — provável inrush subestimado, regulação ruim, gerador sem capacidade transitória adequada ou falta de soft starter.
> 4. **Múltiplas cargas pesadas em operação simultânea sem PMS nem registro documentado** — qualquer coincidência inesperada derruba a fonte; risco de perder refrigeração, bombas, direção hidráulica ou iluminação crítica em navegação.
> 5. **DR/ELCI disparando repetidamente no AC** sob carga de ar-condicionado, boiler ou carregador — pode ser arquitetura incompatível (múltiplos bonds), fuga real por isolação degradada, aquecedor comprometido ou resistência do boiler com falha à massa. Não "trocar por DR maior".
> 6. **Charter, passageiros ou comercial sem plano de gestão de potência documentado** — exposição regulatória (NORMAM-201/204/DPC, USCG Subchapter K/T) e responsabilidade civil ampliadas no caso de incidente com terceiros a bordo.
> 7. **Retrofit de ar-condicionado norte-americano (split-phase 120/240 V) em embarcação brasileira (monofásico 127/220 V ou 220/380 V)** sem análise de neutro, proteção, bond e transformador — erro recorrente e grave em barcos importados.
> 8. **Cabo ou borne aquecendo com carga dentro da nominal** — subdimensionamento, conexão degradada, de-rating por agrupamento ou temperatura ambiente ignorado. Risco de incêndio latente, mesmo sem qualquer disjuntor disparar.
> 9. **Perícia pós-incêndio, pós-dano em linha pesada ou contestação de seguro** — laudo técnico exige rastrear projeto, componentes instalados, conformidade normativa aplicável, histórico de manutenção e adequação da gestão de potência. Tarefa de engenheiro, não de técnico de bordo.

> [!abstract] Resumo técnico
> Linha pesada AC é a camada da distribuição dedicada a cargas de alta potência, alta corrente de partida ou alta criticidade operacional. Em embarcações, ela define boa parte do dimensionamento do shore power, do gerador, do inversor e do próprio quadro AC.

## O que é

Não existe um único valor de corrente que transforme um circuito em "linha pesada". O critério profissional é mais amplo:

- carga com alta potência sustentada;
- carga com alto inrush;
- carga que exige circuito dedicado;
- carga que afeta diretamente a gestão global de potência;
- carga cuja falha não pode derrubar circuitos de uso geral.

Embarcações de recreio costumam enquadrar aqui:

- [[Ar-Condicionado Marine — Sistema Completo]];
- [[Boiler]];
- dessalinizador;
- cooktop, forno ou resistências relevantes;
- carregadores/inversores de maior porte;
- bombas ou máquinas com partida severa.

## Por que isso é central no projeto

É na linha pesada que aparecem, com mais frequência:

- sobrecarga do shore power;
- partida difícil de compressores;
- queda de tensão sob carga;
- aquecimento de conectores e cabos;
- coordenação ruim entre disjuntor, contator e fonte;
- conflito entre conforto e capacidade real da embarcação.

Projeto ruim de linha pesada normalmente cobra a conta cedo: disjuntor caindo, gerador sofrendo, compressor falhando e conectores aquecendo.

## Relação com as fontes de energia

A linha pesada precisa ser pensada a partir da fonte disponível:

- [[CAIS (Pier) (AC)]];
- [[Gerador (AC)]];
- [[Inversora (DC To AC)]], quando a arquitetura permitir;
- sistemas híbridos com gerenciamento de potência.

A pergunta correta não é "qual o disjuntor do equipamento", mas:

- qual fonte vai alimentá-lo;
- que outras cargas podem operar junto;
- qual corrente de partida aparece;
- como a transferência entre fontes será feita;
- o que deve ter prioridade quando a potência for insuficiente.

## Cargas típicas e exigências

### Compressores e ar-condicionado

São os casos mais clássicos de carga pesada. Exigem atenção a:

- corrente nominal;
- corrente de partida;
- quedas de tensão;
- contatores e proteção adequados;
- interação com shore power e gerador.

### Resistências e aquecimento

Boilers e aquecedores são mais previsíveis eletricamente, mas puxam corrente elevada por tempo prolongado. Isso afeta:

- dimensionamento do circuito;
- aquecimento em conectores;
- simultaneidade com outras cargas.

### Carregadores e inversores/carregadores

Não devem ser tratados como "eletrônica leve". Em correntes altas de carga, tornam-se grandes consumidores AC e interferem fortemente na gestão de energia do barco.

## Critérios corretos de projeto

### 1. Circuito dedicado

Toda carga relevante deve ter ramal próprio quando:

- a corrente é alta;
- a partida é severa;
- a criticidade operacional justifica segregação;
- a seletividade se perde se o circuito for compartilhado.

Compartilhar ar-condicionado, boiler e carregador no mesmo circuito raramente é decisão profissional.

### 2. Seletividade e coordenação

O circuito precisa coordenar:

- dispositivo de proteção;
- condutor;
- meio de manobra;
- características da carga;
- capacidade da fonte.

Disjuntor "maior para não cair" não corrige projeto ruim. Só desloca o problema para cabo, conector, contator ou equipamento.

### 3. Corrente de partida

Motores e compressores exigem análise de partida. Em alguns casos, vale considerar:

- soft starter;
- delay e lógica de prioridade;
- dimensionamento mais robusto do gerador;
- limitação ou programação do inversor/carregador;
- intertravamento entre cargas que não devem partir juntas.

### 4. Queda de tensão

Em linha pesada, a queda de tensão passa de detalhe a variável crítica. Partidas sob subtensão aumentam aquecimento, reduzem torque e elevam falhas.

### 5. Gestão de potência

Embarcações com múltiplas cargas pesadas pedem estratégia:

- prioridade manual;
- shedding automático;
- limitação de corrente do shore;
- controle pelo inversor/carregador;
- intertravamentos de partida.

## Falhas típicas em campo

As mais frequentes são:

- disjuntor do cais atuando quando uma carga pesada entra;
- gerador incapaz de sustentar a partida do compressor;
- conector de shore power aquecendo;
- cabo ou borne aquecendo em operação contínua;
- DR disparando por arquitetura incompatível ou fuga real;
- mistura de linha leve e linha pesada no mesmo circuito;
- circuito dedicado mal dimensionado por ignorar inrush e simultaneidade.

## Diagnóstico profissional

O diagnóstico deve medir:

- tensão na origem, no quadro e na carga;
- corrente em regime e no momento de partida, quando possível;
- temperatura de conectores, cabos e terminais;
- resposta da proteção;
- comportamento da fonte sob carga.

Perguntas importantes:

1. A fonte suporta a carga sozinha?
2. O circuito derivado foi pensado para essa carga ou só "adaptado"?
3. O problema é proteção, cabo, contato, carga ou falta de gestão de potência?

## Boas práticas

- usar circuito dedicado para cada carga pesada relevante;
- alinhar proteção, cabo e regime real da carga;
- prever lógica de prioridade quando a soma de cargas puder exceder a fonte;
- tratar conectores e cabos de entrada como itens críticos de manutenção;
- documentar quais cargas podem operar simultaneamente em cada fonte;
- separar claramente linha leve e linha pesada no quadro e no diagrama.

## Erros comuns

Os erros mais danosos são:

- projetar pela corrente nominal e ignorar a partida;
- usar um único circuito para várias cargas severas;
- resolver queda de tensão com disjuntor maior;
- tratar carregador de grande porte como carga "secundária";
- esquecer que a linha pesada redefine a arquitetura inteira do AC do barco.

## Normas aplicáveis

Linha pesada AC é o ponto onde **regras gerais de instalação elétrica**, **normas náuticas específicas** e **critérios de equipamento** convergem. Abaixo, as famílias normativas que o projetista precisa ler (ou ter lido) antes de fechar o dimensionamento.

### Recreio / Small craft (foco principal em embarcações de lazer)

- **ABYC E-11 (2023) — AC & DC Electrical Systems on Boats**: documento de referência nos EUA e adotado informalmente no Brasil por muitos projetistas; define arquitetura AC, bonding, DR/ELCI, proteção, cabos, conectores e sinalização.
- **ABYC A-6 — Ground Fault Protection**: critérios de DR/ELCI por circuito e por embarcação.
- **ABYC E-8 — AC Generators**: integração do gerador à distribuição AC, bonding e coordenação com shore.
- **ABYC H-2 — Ventilation / motor loads**: ventilação de compartimentos com motores AC significativos.
- **ABYC TE-4 — Lightning Protection**: interação da linha pesada com sistema de proteção contra descarga atmosférica.
- **ISO 13297:2020 — Small craft — Electrical systems — AC and DC**: norma internacional para embarcações de recreio até 24 m (referência básica para CE-RCD).
- **ISO 8846:2020 — Electrical devices — Protection against ignition**: equipamentos AC em compartimentos com atmosfera potencialmente inflamável (gasolina).
- **CE-RCD Directive 2013/53/EU — Recreational Craft Directive**: exigência europeia, apoia-se em ISO 13297 e ISO 8846.

### Marinas, cais e interface shore power

- **IEC 60364-7-709 — Low-voltage electrical installations — Marinas and similar**: projeto do pedestal, do cabo de cais, proteção e seleção de dispositivos na interface cais ↔ barco.
- **NEC Art. 555 — Marinas, Boatyards, Boat Basins**: equivalente norte-americano; pedestais de 30 A, 50 A, 100 A, RCD/ELCI, sinalização e distância.

### Baixa tensão / Instalações elétricas prediais aplicáveis ao barco

- **IEC 60364-4-43 — Protection against overcurrent** e **NBR IEC 60364-4-43**: seletividade e coordenação de proteção de sobrecorrente.
- **IEC 60364-5-52 — Selection and erection of wiring systems** e **NBR IEC 60364-5-52**: ampacidade, agrupamento, métodos de instalação e de-rating de cabos.
- **NBR IEC 60364-4-41 — Proteção contra choques elétricos**: bond, DR, esquemas de aterramento (TN, TT, IT) aplicáveis ao barco.
- **NBR 5410:2004 + emendas — Instalações elétricas de baixa tensão**: documento brasileiro de referência para a parte geral do projeto AC; é a norma que a perícia brasileira cobra em laudo.

### Circuitos derivados, motores e ar-condicionado (família americana)

- **NEC Art. 210 — Branch circuits** e **Art. 215 — Feeders**: estrutura de circuitos e alimentadores.
- **NEC Art. 220 — Branch-circuit, feeder and service calculations**: fator de demanda, coincidência e dimensionamento de alimentadores.
- **NEC Art. 240 — Overcurrent protection**: proteção contra sobrecorrente.
- **NEC Art. 310 — Conductors for general wiring**: tabelas de ampacidade, de-rating e seleção de condutores.
- **NEC Art. 430 — Motors, motor circuits and controllers**: dimensionamento de cabo e proteção para motores AC (base do MCA/MOCP).
- **NEC Art. 440 — Air-conditioning and refrigerating equipment**: a família mais importante para ar-condicionado marítimo — define como interpretar MCA, MOCP, RLA e LRA.
- **UL 489 — Molded-Case Circuit Breakers** e **UL 1077 — Supplementary Protectors**: tipo de disjuntor admitido como proteção de ramal (489) vs. proteção suplementar (1077) — confundir os dois é erro comum.
- **NFPA 70 — National Electrical Code** (que contém todos os NEC Arts. acima) e **NFPA 302 — Pleasure and Commercial Motor Craft**: NFPA 302 é a norma de instalação aplicável a embarcações nos EUA e traz exigências específicas de linha pesada.

### Embarcações comerciais / classificadas

- **IEC 60092-101 — Electrical installations in ships — Definitions**.
- **IEC 60092-201 — System design**.
- **IEC 60092-202 — System design — Protection**.
- **IEC 60092-301 — Equipment — Generators, converters, transformers**.
- **IEC 60092-352 — Cables for shipboard installations**.
- **DNV-RU-SHIP Pt 4 Ch 8 — Electrical installations** (sociedade classificadora DNV).
- **Lloyd's Register Rules Pt 6 — Electrical**.
- **NORMAM-201 / 204 / DPC** para comercial e **NORMAM-211 / DPC** para esporte e recreio (Brasil, Marinha do Brasil, Diretoria de Portos e Costas).

### Iluminação de emergência e referência cruzada

- **NBR 10898 — Sistema de iluminação de emergência**: usada como referência cruzada quando a linha pesada pode impactar iluminação de emergência em embarcação de passageiros.

### Comparação rápida por jurisdição

| Tema | EUA (ABYC + NFPA/NEC + UL) | Brasil (NBR + NORMAM) | Internacional / Comercial (IEC + Classificadoras) | Europa (CE-RCD + ISO) |
|---|---|---|---|---|
| Referência primária | ABYC E-11 + NFPA 302 + NEC 555 | NBR 5410 + NORMAM-211/201 | IEC 60092-series + DNV / Lloyd's | CE-RCD 2013/53/EU + ISO 13297 |
| Ar-condicionado | NEC 440 (MCA/MOCP/RLA/LRA) | NBR 5410 + plaqueta do fabricante | IEC 60092-301 | ISO 13297 + plaqueta |
| Shore power (marina) | NEC 555 | IEC 60364-7-709 (adotada) | IEC 60364-7-709 | IEC 60364-7-709 |
| DR / ELCI | ABYC A-6 | NBR IEC 60364-4-41 | IEC 60364-4-41 | ISO 13297 + IEC 60364-4-41 |
| Proteção sobrecorrente | NEC 240 + UL 489 | NBR IEC 60364-4-43 | IEC 60364-4-43 + IEC 60092-202 | IEC 60364-4-43 |
| Cabos e ampacidade | NEC 310 + ABYC E-11 (marine cable) | NBR IEC 60364-5-52 | IEC 60092-352 | IEC 60092-352 + ISO 13297 |
| Proteção contra ignição (gasolina) | ABYC E-11 (ignition protection) | NBR 5410 (apenas geral) | IEC 60092 + ISO 8846 | ISO 8846 |

## Glossário rápido

- **AC (Alternating Current)**: corrente alternada; no contexto do barco, geralmente 120/240 V (EUA), 127/220 V ou 220/380 V (Brasil), 50 Hz ou 60 Hz conforme origem.
- **Linha pesada**: camada da distribuição AC dedicada a cargas de alta potência, alto inrush ou alta criticidade operacional.
- **Linha leve**: camada da distribuição AC para cargas de baixa potência e uso geral (tomadas, iluminação, eletrônica).
- **Carga dedicada**: carga que ocupa circuito próprio, do quadro até o equipamento, sem compartilhamento com outras cargas.
- **FLA (Full Load Amps)**: corrente nominal plena do motor/compressor operando em regime.
- **RLA (Rated Load Amps)**: corrente nominal dada pelo fabricante para o compressor AC em condições de catálogo.
- **LRA (Locked Rotor Amps)**: corrente com rotor bloqueado — valor de referência do pico de partida; tipicamente 5–8× FLA.
- **SFA (Service Factor Amps)**: corrente no fator de serviço (sobrecarga admitida continuamente, geralmente 1,15 × FLA).
- **Inrush current / corrente de partida**: pico transitório de corrente na energização (motores, compressores, transformadores, retificadores).
- **MCA (Minimum Circuit Ampacity)**: ampacidade mínima do cabo do ramal, já contemplando ciclo e partida; valor da plaqueta do equipamento. **Dimensiona o cabo.**
- **MOCP (Maximum Overcurrent Protection)**: máximo ajuste/valor do dispositivo de proteção do ramal; valor da plaqueta. **Dimensiona o disjuntor.**
- **Partida direta (DOL — Direct On Line)**: compressor/motor parte ligado diretamente à rede; pico de partida pleno.
- **Soft starter**: dispositivo eletrônico que reduz o pico de partida (tipicamente de 6–8× FLA para 2–3× FLA) através de rampa de tensão.
- **VFD (Variable Frequency Drive)**: conversor de frequência, permite partida suave e controle de velocidade; usado em compressores inverter.
- **Compressor inverter**: compressor com VFD integrado; inrush muito menor e modulação contínua da capacidade.
- **Contator**: chave de manobra eletromecânica para carga AC; dimensionado por AC-3 (partida de motor) ou AC-1 (resistiva).
- **Categoria de emprego (AC-1, AC-3, AC-7a, etc.)**: classificação IEC 60947 da severidade da manobra do contator.
- **Relé de sobrecarga térmico**: proteção da bobina do motor contra sobrecarga prolongada (não protege contra curto).
- **Disjuntor motor / MPCB (Motor Protection Circuit Breaker)**: combina curto-circuito + sobrecarga térmica em um único dispositivo.
- **UL 489 vs UL 1077**: disjuntor de ramal (489) é obrigatório na origem do circuito; disjuntor suplementar (1077) só pode ser usado após proteção principal adequada.
- **Seletividade**: coordenação entre proteções em série de forma que apenas a mais próxima da falta opere.
- **Coordenação**: harmonização entre proteção, cabo, contator, carga e fonte — conceito mais amplo que seletividade.
- **Queda de tensão / voltage drop**: diferença entre tensão na origem e tensão na carga; típico limite admitido ≤ 3% em circuito de linha pesada.
- **Ampacidade**: capacidade de condução de corrente do cabo em regime, já considerando temperatura, agrupamento e método de instalação.
- **AWG (American Wire Gauge)**: padrão norte-americano de bitola de cabo; usado na maioria dos barcos americanos.
- **mm² / seção nominal**: padrão métrico de seção do condutor; referência brasileira e europeia.
- **De-rating / fator de redução**: redução da ampacidade por temperatura ambiente alta, agrupamento de cabos, exposição solar ou instalação em ambiente adverso.
- **Marine cable / cabo marítimo**: cabo tinned (estanhado), com isolação adequada ao ambiente salino; especificado em ABYC E-11, IEC 60092-352 ou UL 1426.
- **Torque de aperto**: valor especificado pelo fabricante para parafuso do conector ou borne; conexão mal torqueada é fonte primária de aquecimento.
- **Tinned copper / cobre estanhado**: cobre revestido de estanho para resistência à corrosão em ambiente marinho.
- **IP rating (Ingress Protection)**: grau de proteção da carcaça contra pó e água (IEC 60529); tipicamente IP44 em compartimentos secos e IP55/IP66 em áreas expostas.
- **GFPE (Ground Fault Protection of Equipment)**: proteção contra fuga à terra em nível de equipamento ou alimentador (30 mA – 30 A); no NEC, é distinta do GFCI pessoal (5 mA).
- **ELCI (Equipment Leakage Circuit Interrupter)**: variante marine do GFPE/DR, com limiar típico de 30 mA na alimentação principal da embarcação (ABYC E-11 / NEC 555).
- **DR (Dispositivo a Corrente Diferencial Residual)**: termo brasileiro para RCD; genérico para DR pessoal (30 mA) e DR de equipamento.
- **AFCI (Arc-Fault Circuit Interrupter)**: proteção contra falha de arco; exigido pelo NEC em certas ocupações terrestres, pouco usado em embarcação de recreio.
- **Bond / bonding**: conexão equipotencial entre partes metálicas; no AC, refere-se à ligação neutro-terra (N-PE) feita na fonte ativa.
- **ATS (Automatic Transfer Switch)**: chave automática de transferência entre fontes; em barcos, precisa ser "break-before-make" e preferencialmente 4-pole para manejar o neutro.
- **Shore power**: alimentação AC do cais, via cabo e conector padrão (30 A, 50 A ou 100 A nos EUA; IEC 60309 no padrão internacional).
- **Shore current limiter**: limitador ativo que garante que a corrente total drenada do cais não exceda o ajuste do pedestal.
- **Load shedding**: desligamento automático de cargas não prioritárias quando a fonte chega perto do limite.
- **PMS (Power Management System)**: sistema integrado de gestão de potência; coordena fontes, ATS, shedding, prioridades e inversor/carregador.
- **Demand factor / fator de demanda**: relação entre a máxima demanda simultânea e a soma das cargas conectadas.
- **Coincidence factor / fator de coincidência**: probabilidade de cargas pesadas operarem ao mesmo tempo.
- **Fator de potência (cos φ)**: relação entre potência ativa e aparente; compressores e motores operam tipicamente em 0,7–0,9.
- **kVA vs kW**: aparente vs ativa; dimensionamento de gerador e transformador é em **kVA**, não em kW.
- **BTU/h (British Thermal Unit per hour)**: unidade de capacidade de refrigeração; base de catálogo do ar-condicionado marine.
- **TR (Ton of Refrigeration)**: 1 TR = 12 000 BTU/h.
- **COP (Coefficient of Performance)**: relação entre capacidade de refrigeração e potência elétrica consumida em um ponto de operação.
- **EER (Energy Efficiency Ratio)**: COP expresso em BTU/h por W elétrico.
- **Intertravamento**: lógica que impede partidas simultâneas de cargas pesadas incompatíveis com a fonte.
- **Back-feed**: corrente de retorno indesejada (por exemplo, gerador energizando o shore com o disjuntor aberto); ATS adequado previne.
- **Ilha / operação isolada**: barco operando exclusivamente no gerador ou inversor, desconectado do shore.
- **Split-phase 120/240 V**: arquitetura AC residencial norte-americana; retrofit em barco brasileiro exige análise cuidadosa de neutro e proteção.

## Integração com outras notas

- [[Ar-Condicionado Marine — Sistema Completo]]
- [[CAIS (Pier) (AC)]]
- [[Chaves Seletoras (AC)]]
- [[Contatores (AC)]]
- [[Gerador (AC)]]
- [[Inversora (DC To AC)]]
- [[Linha Leve (AC)]]
- [[Proteção Dr]]

## Perguntas que esta nota responde

- Quando uma carga deve receber circuito dedicado na embarcação?
- Como a linha pesada influencia shore power, gerador e inversor?
- Por que falhas em ar-condicionado, boiler e carregador quase sempre revelam problema maior de arquitetura AC?
