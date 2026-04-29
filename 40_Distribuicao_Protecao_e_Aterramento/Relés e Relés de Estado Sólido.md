---
title: "Relés e Relés de Estado Sólido"
note_type: "technical-note"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "RELÉS E RELÉS DE ESTADO SÓLIDO 33a19734f7fb81488f55fb058be47993.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "65"
tier_fase_6: "A"
reviewed_on: "2026-04-21"
review_jurisdiction:
  - "Brasil"
  - "internacional"
review_level: "engineering-curated"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
normas_citadas:
  - "IEC 61810-1 (Electromechanical elementary relays — General requirements)"
  - "IEC 61810-2 (Reliability of electromechanical elementary relays)"
  - "IEC 61810-7 (Test and measurement procedures)"
  - "IEC 60947-4-2 (LV switchgear — AC semiconductor motor controllers / contactors and starters)"
  - "IEC 60947-4-3 (LV switchgear — AC semiconductor controllers and contactors for non-motor loads)"
  - "IEC 60255 (Measuring relays and protection equipment)"
  - "IEC 60664-1 (Insulation coordination)"
  - "IEC 60068-2 (Environmental testing — Vibration, shock, damp heat)"
  - "IEC 60529 (IP code)"
  - "UL 508 (Industrial Control Equipment)"
  - "UL 991 (Safety-Related Controls Employing Solid-State Devices)"
  - "UL 1500 (Ignition Protection for Marine Products)"
  - "UL 60730 (Automatic Electrical Controls)"
  - "SAE J1171 (Marine Ignition Protection)"
  - "SAE J1455 (Recommended Environmental Practices for Electronic Equipment Design in Heavy-Duty Vehicle Applications)"
  - "SAE J2030 (Heavy-Duty Electrical Connector Performance)"
  - "ABYC E-11 §11.3 (componentes marinos)"
  - "ABYC E-11 §11.4 (proteção de circuitos)"
  - "ABYC E-11 §11.10 (switches and relays)"
  - "ISO 8846:1990 (Ignition protection — Small craft)"
  - "ISO 10133:2012 (DC electrical systems small craft)"
  - "ISO 13297:2020 (AC electrical systems small craft)"
  - "ABNT NBR IEC 61810-1:2016 (Relés eletromecânicos — Requisitos gerais)"
  - "ABNT NBR IEC 60947-4-2 (Semicondutores AC)"
  - "ABNT NBR IEC 60947-4-3 (Semicondutores AC não-motor)"
  - "NORMAM-05/DPC (Embarcações de recreio)"
  - "NFPA 70 (NEC) art. 725 (Class 2/3 Remote-Control Circuits)"
  - "MIL-STD-202 (Environmental test methods)"
family_clusters:
  - "IEC (internacional)"
  - "UL (EUA industrial)"
  - "ABYC-USCG (EUA náutico)"
  - "ISO (internacional náutico)"
  - "SAE (automotivo e marine)"
  - "ABNT-NORMAM (Brasil)"
aliases:
  - "RELÉS E RELÉS DE ESTADO SÓLIDO"
  - "Relé eletromecânico"
  - "SSR (Solid State Relay)"
  - "MOSFET switch"
  - "Smart switch"
  - "Latching relay"
seo_title: "Relés e SSR em embarcações: seleção, supressão, dissipação e aplicação"
seo_description: "Guia técnico sobre relés eletromecânicos e de estado sólido em embarcações: categorias de carga, supressão de transientes, dissipação térmica, AC vs DC, MOSFET switches."
seo_keywords:
  - "relé marine"
  - "SSR embarcação"
  - "MOSFET switch náutico"
  - "supressão de transientes relé"
geo_queries:
  - "Como escolher relé e SSR em embarcações?"
  - "Qual a diferença entre relé eletromecânico e relé de estado sólido?"
  - "Quando usar MOSFET switch em vez de relé?"
related_notes:
  - "Contatores (AC)"
  - "Chaves Gerais (DC)"
  - "Atuador Linear"
  - "Sistema de Alarme Geral - Painel de Alarmes"
  - "Automação de Bordo - Sistemas Domoticos"
  - "Disjuntores (DC) e (AC)"
  - "Hotline (DC)"
  - "Bomba de Porão"
---

# Relés e Relés de Estado Sólido

> [!abstract] Resumo técnico
> Relé é um **dispositivo de comando que permite a um circuito de baixa potência controlar outro circuito** — em embarcações, o ponto de desacoplamento entre lógica e potência. A escolha correta depende de **tipo de carga** (resistiva/indutiva/capacitiva/eletrônica), **corrente de partida** (inrush de motor/bomba/solenóide pode ser 5-15× a nominal), **frequência de acionamento** (liga-desliga por hora), **ambiente** (sal, vibração, temperatura) e **estratégia de falha** (o que acontece se o relé colar ou abrir?). IEC 61810 normaliza relés eletromecânicos (EMR), IEC 60947-4-2/-3 normaliza semicondutores (SSR/MOSFET switches), ABYC E-11 §11.10 fixa requisitos marinos. As três dores clássicas são: (i) especificar por corrente nominal contínua ignorando inrush; (ii) tratar SSR como categoria homogênea (SSR AC ≠ SSR DC ≠ MOSFET switch); (iii) esquecer supressão de indutivos (cargas como bomba, atuador, solenóide de partida geram BEMF que destrói contatos e semicondutores). Em bordo, o acionamento de **[[Bomba de Porão]]** manual, de **[[Atuador Linear]]** de flap e de **alarmes de [[Hotline (DC)]]** passa quase sempre por relés — projeto errado aqui cola contato e apaga função crítica.

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **Relé não se especifica só por amperes nominais** — tipo de carga (AC-1/AC-3/AC-15, DC-1/DC-3/DC-13), corrente de partida (inrush) e ciclos/hora definem categoria real.
> 2. **Inrush de indutivo é 5-15× a corrente nominal** — bomba de porão 5 A nominal pode ter pico de 25-40 A na partida; relé 10 A automotivo cola no 5º ciclo.
> 3. **SSR AC ≠ SSR DC** — SSR AC usa TRIAC (zero-crossing), **não funciona em DC** (não há cruzamento por zero para extinguir o arco); SSR DC usa MOSFET ou IGBT dedicados.
> 4. **Carga indutiva exige supressão** — varistor + RC snubber em AC; diodo de roda livre + TVS em DC; sem supressão, BEMF de 100-400 V queima contato ou driver em 100-1000 ciclos.
> 5. **Dissipação do SSR é real** — queda típica 1-2 V em condução: 10 A × 1,5 V = 15 W; exige dissipador calculado (0,5-2 °C/W).
> 6. **MOSFET switch marine** (Victron Smart BatteryProtect, Blue Sea Add-A-Battery, Littelfuse MegaFuse) substitui relé em muitos casos DC — zero desgaste, silencioso, proteção integrada.
> 7. **Latching (biestável)** mantém estado sem consumo de bobina contínuo — ideal para chave remota de acionamento raro.
> 8. **Bobina DC vs AC** — nunca intercambiáveis; bobina AC em DC queima em minutos; bobina DC em AC vibra e queima em horas.
> 9. **Relé marine-grade em ambiente salino** — IP67, terminais banhados (tin/nickel), housing policarbonato UV, categoria de vibração IEC 60068-2-6.
> 10. **Falha segura por projeto** — NF (normally closed) para alarme (falha abre = alarme toca); NO (normally open) para bomba (falha abre = bomba desliga); definir e documentar.

> [!danger] Quando chamar um especialista
> Estes 9 cenários exigem engenheiro elétrico/eletrônico náutico ou integrador:
> 1. **Chaveamento DC de alta corrente** (> 100 A em 24/48 V) — relé comum não atende; exige contator DC dedicado (Gigavac, Albright, Tyco Kilovac) ou MOSFET switch em paralelo com limitador de corrente.
> 2. **Carga indutiva DC sem supressão adequada queimando drivers repetidamente** — diagnóstico exige osciloscópio para medir BEMF e selecionar TVS/diodo de roda livre com margem correta (trr, VR, IF).
> 3. **Sistema de automação náutica crítica** (NMEA 2000, CZone, EmpirBus) com relés de saída — cada relé tem estratégia de falha que afeta UX; projeto exige FMEA (Failure Mode and Effects Analysis).
> 4. **Chaveamento de inversor/VFD com SSR** — harmonics, dV/dt alto, ruído conduzido; SSR standard falha; exige SSR com zero-voltage switching + filtro RC snubber bem projetado.
> 5. **Intertravamento de segurança** (emergência de guincho, MOB switch, disjuntor magnético geral) — exige relé de segurança categoria 3/4 (ISO 13849), redundância dupla e monitoração.
> 6. **Retrofit de relés antigos em barco clássico** com contatos oxidados e sem documentação — limpeza elétrica + identificação + substituição por equivalente marine-grade.
> 7. **Temperatura ambiente > 50 °C** no compartimento (sala de máquinas em trópico) — relés standard derratam severamente acima de 40 °C; exige seleção específica com curva de derating do fabricante.
> 8. **Embarcação classificada (SOLAS/DNV/Lloyd's)** — relés com certificação de classe, ensaio de vibração IEC 60068-2-6 severidade 40 Hz/4 g, ensaio de choque.
> 9. **Integração de BMS Li-Fe com relés de desconexão** — BMS precisa comandar um contator DC de 200-500 A com latência < 100 ms; seleção exige spec detalhada do BMS (driver, corrente, tensão).

## O que é

Relés e dispositivos correlatos são elementos de **interface entre lógica de comando e potência**. Em embarcação, eles permitem:

- **acionar cargas** (bomba, motor, luminária, atuador, sirene);
- **isolar circuitos de comando** (botoeira de baixa corrente não carrega 20 A da carga);
- **implementar intertravamentos** (se A ligou, B não pode ligar);
- **permitir automação e supervisão** (interface para MFD, PLC, microcontrolador).

### O que esta nota cobre

- **relé eletromecânico (EMR)** — categorias IEC 60947 (AC-1, AC-3, DC-13, etc.), curva de vida, construção, supressão;
- **relé de estado sólido (SSR)** — SSR AC (TRIAC), SSR DC (MOSFET), derating térmico, snubber;
- **MOSFET switch marine** (Victron BP, Blue Sea, Littelfuse) — substituto moderno de relé DC em bordo;
- **latching / biestável** — sem consumo em estado fixo;
- **relé automotivo standard** (Bosch, Tyco, Hella, Omron) vs. **relé marine-grade** (Blue Sea, Cole Hersee, Del City);
- **tabelas de seleção** por aplicação típica de bordo.

Nem todo dispositivo de comutação é "só um relé". Em certos patamares de corrente, frequência ou criticidade, o componente adequado passa a ser um **[[Contatores (AC)|contator]]**, um MOSFET switch dedicado, um relé de segurança ou outra arquitetura.

## Função na embarcação

- **comandar bombas** (porão manual, circulação água, transferência combustível), **ventiladores** (sala de máquinas, cabine), **atuadores** (flap, trim tab, guincho), **alarmes** (sirene, strobe, buzzer);
- **isolar lógica de controle** da carga principal (painel touch aciona relé, relé comuta 15 A);
- **reduzir corrente** circulando em botoeiras e controles (botão 100 mA comanda bobina 50 mA que chaveia 20 A);
- **viabilizar automação e acionamentos remotos** (MFD comanda via NMEA 2000 → gateway → relé → carga).

## Fundamentos mínimos

### Tipo de carga importa (IEC 60947-5-1 / IEC 61810-1)

| Categoria IEC | Tipo de carga | Exemplo típico | Inrush vs. nominal |
| --- | --- | --- | --- |
| **AC-1** | resistiva | resistência aquecedor, lâmpada incandescente | ≈ 1× |
| **AC-3** | motor a gaiola, partida + desligamento com motor em rotação | bomba centrífuga, ventilador | 5-8× |
| **AC-4** | motor a gaiola, partida + reversão + frenagem por contracorrente | partida reversa | 10-12× |
| **AC-15** | eletroímãs AC (bobinas), comando | contator, solenóide | 3-5× |
| **DC-1** | resistiva DC | aquecedor, lâmpada halógena | ≈ 1× |
| **DC-3** | motor shunt (partida + frenagem dinâmica) | motor elétrico ajustável | 2,5-4× |
| **DC-5** | motor série (partida + frenagem contracorrente) | guincho, starter | 4-15× |
| **DC-13** | eletroímãs DC, solenóide, bobina | solenóide de partida, solenoide de válvula | 1× (mas τ alta) |

**Escolher relé apenas pela "corrente nominal em amperes"** é uma das causas mais comuns de falha. Um relé 20 A AC-1 pode falhar em 5 A AC-3.

### Corrente de partida pode ser muito maior que a de regime

Em bordo, os casos mais problemáticos:

- **bomba de porão**: nominal 3-5 A; pico 15-25 A por 30-100 ms;
- **ventilador de sala de máquinas**: nominal 5-10 A; pico 20-40 A na partida;
- **motor guincho/bow-thruster**: nominal 80-150 A; pico 300-600 A;
- **solenoide de partida do motor**: nominal 50-80 A enquanto segura; pico 200-400 A de inrush;
- **lâmpada incandescente/halogena**: nominal 5-10 A; pico 20-80 A no filamento frio (90% cai em 100 ms).

### SSR não é uma categoria homogênea

- **SSR AC** (Crydom, Omron G3NA, Fotek) — usa **TRIAC**; chaveia em **zero-crossing** (reduz EMI); **não funciona em DC** (TRIAC não extingue em DC porque não há cruzamento por zero);
- **SSR DC** (Crydom D1D, Omron G3NE) — usa **MOSFET ou IGBT**; chaveia rápido; **sem capacidade de extinção de arco** se carga exceder limite;
- **MOSFET switch marine** (Victron BP, Blue Sea Add-A-Battery) — MOSFET de canal N com driver dedicado + proteções integradas (OVP, OCP, térmica);
- **Smart switch** (Garmin Digital Switching, CZone) — módulo de potência com microcontrolador, bus de comunicação e múltiplas saídas.

Tratar todos como equivalentes é **erro técnico**.

### Dissipação térmica faz parte da seleção

Dispositivo de estado sólido pode comutar rápido e sem contatos móveis, **mas dissipa calor em condução**:

- SSR AC típico: **1,0-1,6 V** de queda (TRIAC) → 10 A = **10-16 W**;
- SSR DC MOSFET: **0,01-0,1 Ω** de RDS(on) → 10 A = 1-10 W;
- Relé eletromecânico em contato limpo: **0,1-0,5 mV** de queda → praticamente 0 W em condução (bobina consome 0,5-2 W em alimentado).

**Cálculo do dissipador** (IEC 60747 para MOSFET, Crydom AN para SSR):

```
Rth_total = (Tj_max - Ta) / P_diss
Rth_dissipador = Rth_total - Rth_junção-case - Rth_case-dissipador
```

Exemplo: SSR 10 A DC em 40 °C ambiente, Tj_max = 100 °C, P = 15 W:
- Rth_total = (100 - 40) / 15 = 4 °C/W
- Rth_dissipador ≈ 4 - 0,5 (junção-case) - 0,1 (grease) ≈ **3,4 °C/W**
- Dissipador tipo Aavid 577202 (2,5 °C/W com convecção) atende com folga.

## Tecnologias principais

### Relé eletromecânico (EMR)

**Construção**: bobina + armadura + contatos móveis (prata, ouro banhado, liga AgNi ou AgSnO₂). IEC 61810-1.

**Prós**:
- **isolamento galvânico** total (≥ 4 kV entre comando e carga);
- **queda de tensão desprezível** em condução (contato metálico limpo);
- **bidirecional** — funciona em AC e DC (dentro dos limites de ruptura);
- **tolerante a surto** — contato aguenta curto momentâneo melhor que semicondutor;
- **diagnóstico acessível** — ouve-se o clique, vê-se o contato.

**Contras**:
- **desgaste mecânico** (10⁵-10⁷ ciclos típico);
- **desgaste elétrico** por arco (pior em DC, pior em indutivo sem supressão);
- **ruído** audível;
- **velocidade limitada** (tempo de acionamento 5-20 ms; não serve para PWM);
- **vibração e choque** podem falsamente comutar — ver IEC 60068-2-6.

**Categorias comuns em bordo**:
- **automotivo ISO 280** (ISO 7588) — relé 5-pinos 20/30/40 A 12 V (Bosch 0332019150, Hella 4RA, Tyco V23234) — baratos, disponíveis, mas não marine-grade;
- **relé marine IP67** (Blue Sea 7713, Cole Hersee RB175) — versão selada do relé automotivo;
- **relé DIN rail industrial** (Finder 55.32, Omron MY2, Schneider RXM) — para painel, 8-11 pinos, isolamento 2,5-4 kV;
- **latching / biestável** (Finder 20.23) — dois pulsos (SET/RESET) fixam estado; consumo zero em regime;
- **relé de segurança** (Pilz, Schmersal, Omron G7SA) — categoria 3/4, para emergência.

### Relé de estado sólido (SSR)

**Construção**:
- **SSR AC**: optoacoplador + TRIAC de potência + rede snubber RC + zero-crossing detector (opcional);
- **SSR DC**: optoacoplador + MOSFET(s) em série + drivers + proteções.

IEC 60947-4-2 (motor) / IEC 60947-4-3 (não-motor).

**Prós**:
- **sem desgaste mecânico** (vida útil 10⁸-10¹⁰ ciclos);
- **silencioso** (ideal em cabine);
- **rápido** (ms a µs);
- **adequado para PWM** de lâmpadas, motores, aquecedores;
- **compacto** em alta corrente comparado a contator.

**Contras**:
- **dissipação em condução** (1-2 V em SSR AC TRIAC);
- **corrente de fuga** em OFF (0,1-10 mA) — lâmpada LED pode piscar mesmo "desligada";
- **susceptível a surto** (dV/dt, dI/dt); falha **em curto** tipicamente (perigoso!);
- **necessita de dissipador** em alta corrente;
- **sensível à temperatura** ambiente (derating severo > 40 °C).

### Dispositivos especializados

- **VSR/ACR** (Blue Sea ML-ACR, Arieltek DVSR) — para combinar bancos (ver [[Divisores de Carga (DC)]]);
- **contatores** — para correntes e esforços mais altos (ver [[Contatores (AC)]]);
- **MOSFET switch marine** (Victron Smart BatteryProtect 12/24/48 V, Mastervolt SwitchMaster) — MOSFET com proteção LVC, OVC, curto e telemetria NMEA 2000;
- **Smart switching modules** (CZone, EmpirBus, Garmin Digital Switching) — módulos com 6-16 saídas, comando por bus, configuração por software;
- **relés de proteção** (IEC 60255) — supervisão de tensão, corrente, frequência, isolamento (em sistemas maiores).

### MOSFET switch marine como alternativa moderna

Em barcos com sistemas modernos (Li-Fe, solar, digital switching), **o relé DC comum vem sendo substituído** por módulos MOSFET de bordo:

| Modelo | Corrente | Tensão | Diferencial |
| --- | --- | --- | --- |
| **Victron Smart BatteryProtect 65/100/220** | 65 / 100 / 220 A | 12-48 V | cutoff programável por Bluetooth, LVC |
| **Blue Sea Add-A-Battery** | 65/100 A | 12-24 V | integrado com ACR |
| **Littelfuse MegaFuse Smart** | 100-400 A | 12-48 V | integrado com proteção curto |
| **Mastervolt MasterShunt MOSFET** | 500 A | 12-48 V | telemetria CAN |
| **CZone DC Module 10×10 A** | 10 A × 10 ch | 12-24 V | comando NMEA 2000 |

Vantagens sobre relé: zero desgaste, cutoff programável (LVC, OVC, térmico), diagnóstico via bus, silencioso, proteção integrada.

## Projeto e instalação

### O que precisa ser definido

1. **tensão do comando e da carga** — compatibilidade bobina × carga;
2. **tipo de carga e corrente de partida** — resistivo, motor, solenoide, lâmpada, eletrônica;
3. **frequência de acionamento** — ciclos/hora; > 100/hora descarta EMR comum;
4. **ambiente de instalação** — temperatura, IP, vibração, sal;
5. **estratégia de proteção** da carga e do comando — fusível ramal + supressão de transientes;
6. **comportamento esperado em falha** — NO com falha em aberto = carga desliga; NC com falha aberto = carga liga → escolher conforme "qual falha é mais segura".

### Diretrizes práticas

- **não especificar relé apenas por corrente nominal contínua** — buscar datasheet com corrente de inrush e categoria IEC;
- **prever supressão adequada** para cargas indutivas — varistor + RC snubber em AC; diodo de roda livre + TVS em DC;
- **escolher tecnologia compatível** com o tipo de corrente comutada — nunca SSR AC em DC;
- **proteger e identificar os circuitos** de comando e potência — cores distintas, etiquetas;
- **prever acesso** para substituição e diagnóstico — soquete plug-in > solda direta em muitos casos;
- **dimensionar dissipação** em SSR com margem de 50% sobre o cálculo nominal (temperatura ambiente marine varia);
- **documentar o esquema de comando** — bobina, NO, NC, common, sinal de ativação.

### Supressão de transientes — detalhe técnico

**Em AC (carga indutiva comutada)**:
- **Varistor (MOV)**: absorve pico de BEMF — V_clamp ≈ 1,5-2× V_pico nominal; ex: carga 230 VAC = V_pico 325 V → MOV 430 V (S14K430);
- **RC Snubber**: 100 Ω + 100 nF em série, em paralelo com contato — reduz dV/dt;
- **Relé com contato dourado** para cargas pequenas (< 100 mA) — evita micro-arco.

**Em DC (carga indutiva comutada)**:
- **Diodo de roda livre** (1N4007, 1N5404, UF4007): cátodo no + da bobina, ânodo no −; dissipa a BEMF via corrente de recirculação;
- **Limitação**: diodo comum **aumenta o tempo de desativação** em 5-20× (corrente continua circulando até a energia magnética dissipar);
- **TVS diode** (P6KE50A, SMCJ50) em paralelo com bobina: clamp mais rápido que 1N4007 (reduz tempo de desativação);
- **Diodo zener + diodo comum**: compromisso entre desativação rápida e proteção.

### Escolha por aplicação típica de bordo

| Aplicação | Corrente nominal | Pico (inrush) | Tecnologia recomendada | Por quê |
| --- | --- | --- | --- | --- |
| Bomba porão 12V manual | 3-5 A | 15-25 A | relé marine 30 A (Blue Sea 7713) | inrush alto + ambiente úmido |
| Bomba água doce 12V | 8-10 A | 25-40 A | relé marine 40 A + diodo roda livre | inrush + ciclagem frequente |
| Luzes LED strip 12V dimerizável | 5-10 A | 5-10 A | SSR DC MOSFET | PWM alta frequência |
| Luzes navegação (incand. 12V) | 2-5 A | 10-25 A (fil. frio) | relé marine 20 A | pico de filamento |
| Ventilador sala máquinas 12V | 5-10 A | 20-40 A | relé marine 30 A + TVS | inrush motor |
| Solenoide de partida | 80-120 A (hold) | 300-500 A (inrush) | contator dedicado (Albright SW80) | fora do range de relé |
| Buzina / sirene AC 120V | 1-2 A | 5-10 A | relé 10 A + MOV 275V | indutivo + sonoro |
| Alarme hotline (sirene/strobe) | 0,5-1 A | 2-5 A | relé DIN 8A com diodo | carga mista leve |
| Bow thruster | 300-600 A | 1.000-2.000 A | contator Albright/Gigavac | alta corrente DC |
| Trim tab / atuador linear | 5-20 A | 15-40 A | relé marine 40 A DPDT (reversão) | motor reversível |
| Carga de freezer AC | 5-8 A | 15-30 A | relé 16 A AC-3 + RC snubber | ciclagem compressor |
| Comando via MFD | 1-3 A | 1-3 A | SSR MOSFET 5-10 A | silencioso, compacto |

## Onde costuma dar problema

| Problema | Causa provável | Mitigação |
| --- | --- | --- |
| **relé não aciona** | falha na bobina, ausência de comando, queda de tensão (ΔV > 20% nominal) | medir V na bobina; verificar sinal |
| **contato cola ou degrada** | carga acima do especificado, carga sem supressão, inrush alto | upgrade para relé próxima categoria; supressão |
| **SSR aquece demais** | subdimensionamento térmico, ambiente > 40 °C sem derating | dissipador maior; ventilação; trocar por EMR |
| **acionamento errático** | comando ruidoso, tensão instável, falso contato | filtrar comando; estabilizar fonte |
| **vida útil baixa** | escolha errada para frequência e ambiente | reavaliar ciclagem e categoria |
| **relé DC com bobina AC** | substituição errada em peça de reposição | conferir rótulo sempre |
| **SSR AC com DC** | tentativa de reutilizar SSR | usar SSR específico DC MOSFET |
| **fuga em OFF (SSR)** | corrente de fuga 0,1-10 mA alimenta LED residual | série RC de descarga ou relé EMR |
| **contato oxidado em relé marine antigo** | ambiente salino + corrente baixa (sem burnisher) | limpeza com DeoxIT ou substituição |
| **falha em curto (SSR)** | surto, dV/dt, sobrecarga momentânea | proteção fusível rápido; snubber; TVS |

## Diagnóstico prático

1. **Confirmar se o comando chega** corretamente ao dispositivo — medir tensão na bobina/input no instante do comando.
2. **Medir tensão no comando e na carga em operação** — diferença aponta queda de tensão no relé ou cabo.
3. **Verificar aquecimento e integridade dos terminais** — termômetro IR ou toque cuidadoso; > 60 °C = problema.
4. **Isolar se a falha está** no relé, na lógica de comando ou na carga — substituir por relé conhecido bom em bancada.
5. **Conferir se o dispositivo escolhido é apropriado** para AC ou DC e para o tipo de carga real — confrontar rótulo com aplicação.

**Ferramentas úteis**:
- **multímetro CAT III** — tensão, corrente, resistência de bobina (esperar 60-300 Ω em bobina 12 V standard);
- **osciloscópio** — para ver BEMF, bouncing de contato, EMI;
- **termômetro IR** (Fluke 62 Max+) — aquecimento anormal;
- **contador de ciclos** (integrado em CZone ou externo) — verificar vida útil restante;
- **testador de relé** (Zener 1100, Hypertronics) — bancada dedicada.

## Boas práticas profissionais

- **selecionar componente com base na aplicação real** e não em equivalência genérica ("era 20 A, compro outro 20 A");
- **documentar** tensão de bobina, tipo de contato, função do circuito, data de instalação;
- **considerar supressão de transientes** sempre que a carga tiver indutância (motor, solenoide, bobina, bomba);
- **usar soluções de estado sólido só quando fizerem sentido** térmico e funcional (alta frequência, PWM, silêncio);
- **preferir contatores** quando corrente, duty ou criticidade saírem da zona de conforto do relé comum (> 40 A contínuo, > 1.000 ciclos/dia, segurança de vida);
- **relé marine-grade** em áreas úmidas/salinas (IP67, bronze dourado, policarbonato UV);
- **reserva de 20-30%** em corrente sobre o pior caso (inrush) para vida útil decente;
- **teste funcional após cada intervenção** — acionar carga 3-5 vezes e medir tensão/corrente;
- **ensaio de ciclagem** (burn-in) em aplicação crítica — 100 ciclos antes de considerar confiável.

## Erros que fragilizam a base técnica

- **chamar qualquer módulo eletrônico de "SSR"** e achar que serve para qualquer carga;
- **usar relé pequeno** em motor ou bomba com partida pesada;
- **esquecer dissipação térmica** de comutação sólida;
- **ignorar polaridade** e especificação DC em circuito contínuo;
- **usar relé como substituto** improvisado de arquitetura de proteção (relé não protege contra curto);
- **SSR AC em circuito DC** — o TRIAC não extingue em DC; destrói em segundos;
- **relé automotivo em ambiente marítimo** sem IP67 — 6-18 meses e corrói;
- **sem diodo de roda livre** em bobina DC — surto BEMF queima driver do microcontrolador;
- **contato colado interpretado como "relé ruim"** quando a verdadeira causa é especificação errada;
- **substituir relé queimado por relé igual** sem investigar por que queimou.

## Relação com outros sistemas

- **[[Contatores (AC)]]** — quando a aplicação exige categoria superior de manobra (motor ≥ 40 A, ciclagem alta, segurança de vida).
- **[[Chaves Gerais (DC)]]** — seccionamento manual vs. relé automático.
- **[[Atuador Linear]]** — exemplo prático de comando de movimento com relé reversível (DPDT).
- **[[Sistema de Alarme Geral - Painel de Alarmes]]** — saídas de sirene, sinalização e intertravamento via relé.
- **[[Automação de Bordo - Sistemas Domoticos]]** — lógica de controle e supervisão (CZone, EmpirBus, Garmin Digital Switching).
- **[[Disjuntores (DC) e (AC)]]** — proteção do circuito comutado (relé não substitui disjuntor).
- **[[Hotline (DC)]]** — relés de comando em circuitos sempre-energizados precisam ter falha segura definida.
- **[[Bomba de Porão]]** — uso clássico de relé marine DPDT para manual + automático.
- **[[Divisores de Carga (DC)]]** — VSR/ACR são relés especializados para combinação de bancos.
- **[[Quadro Elétrico e Painel de Distribuição AC-DC]]** — onde relés DIN vivem em barco moderno.

## Normas e referências

### Por família e jurisdição

| Família | Norma | Escopo |
| --- | --- | --- |
| **IEC (internacional)** | IEC 61810-1 | relés eletromecânicos — requisitos |
| IEC | IEC 61810-2 | confiabilidade |
| IEC | IEC 61810-7 | ensaio |
| IEC | IEC 60947-4-2 | semicondutores AC motor |
| IEC | IEC 60947-4-3 | semicondutores AC não-motor |
| IEC | IEC 60947-5-1 | categorias de carga |
| IEC | IEC 60255 | relés de medição/proteção |
| IEC | IEC 60664-1 | coordenação isolação |
| IEC | IEC 60068-2 | ensaio ambiental |
| IEC | IEC 60529 | IP |
| **UL (EUA)** | UL 508 | controle industrial |
| UL | UL 991 | controles SSR de segurança |
| UL | UL 1500 | ignition protection marine |
| UL | UL 60730 | controles automáticos |
| **ABYC (EUA)** | E-11 §11.3 | componentes marine |
| ABYC | E-11 §11.4 | proteção |
| ABYC | E-11 §11.10 | switches and relays |
| **ISO (internacional)** | ISO 8846 | ignition protection |
| ISO | ISO 10133 | DC small craft |
| ISO | ISO 13297 | AC small craft |
| **SAE (EUA)** | SAE J1171 | marine ignition |
| SAE | SAE J1455 | ambiente heavy-duty |
| SAE | SAE J2030 | conectores elétricos |
| **ABNT (Brasil)** | NBR IEC 61810-1 | relés EM requisitos |
| ABNT | NBR IEC 60947-4-2/-3 | semicondutores |
| **NORMAM (Brasil)** | NORMAM-05/-01 | recreio / marítimo |
| **NFPA (EUA)** | NFPA 70 art. 725 | remote-control circuits |
| **MIL-STD** | MIL-STD-202 | ensaio ambiental militar |

### Comparação prática entre jurisdições

- **EUA (ABYC/UL/SAE)**: relé marine com ignition protection (UL 1500, SAE J1171) em compartimento motor; certificação UL 508 para painel industrial; ABYC E-11 §11.10 detalha seleção.
- **Internacional (IEC/ISO)**: IEC 61810 define ensaio padronizado; ISO 10133 cobre DC small craft; IEC 60947-5-1 categorias de carga.
- **Brasil (ABNT/NORMAM)**: tradução direta IEC (NBR IEC 61810-1 e NBR IEC 60947-4-2/-3); NORMAM-05 remete a ABYC/ISO.
- **Europa (CE/RCD)**: conformidade ISO + marcação CE; CE/RCD 2013/53/UE para recreio.
- **Navio classificado (SOLAS/DNV/Lloyd's)**: relés com certificação de classe; ensaios vibração IEC 60068-2-6 severidade 40 Hz/4 g; ambiente salino MIL-STD-810.

## Glossário rápido

1. **AC-1, AC-3, AC-15** — categorias IEC de carga AC (resistiva, motor, bobina).
2. **Armature** — parte móvel da bobina do relé EMR.
3. **BEMF (Back-EMF)** — tensão reversa de bobina ao desenergizar.
4. **Burnisher** — ferramenta de limpeza de contato oxidado.
5. **Coil / bobina** — enrolamento de comando do relé.
6. **Contato AgNi / AgSnO₂** — ligas de contato de relé.
7. **Contato dourado** — contato para pequenas correntes (< 100 mA).
8. **Contator** — relé de maior porte (ver [[Contatores (AC)]]).
9. **Coronas / bouncing** — micro-arcos no fechamento do contato.
10. **DC-13** — categoria IEC para solenoide DC.
11. **Derating** — redução de capacidade com temperatura ambiente.
12. **DPDT** — Double-Pole Double-Throw (dois polos, duas posições).
13. **dV/dt / dI/dt** — taxa de variação de tensão/corrente (estresse semicondutor).
14. **Diodo de roda livre** — diodo anti-paralelo na bobina DC.
15. **Dissipação (P_diss)** — calor gerado em condução.
16. **Driver** — circuito que alimenta a bobina ou o gate do MOSFET.
17. **EMR (Electromechanical Relay)** — relé eletromecânico.
18. **Falha segura** — estado assumido em falha (NO/NC).
19. **FMEA** — Failure Mode and Effects Analysis.
20. **Ignition Protection** — proteção contra ignição de gás (UL 1500, SAE J1171).
21. **Inrush current** — corrente de partida.
22. **IP67 / IP68** — grau de proteção (IEC 60529).
23. **Latching / biestável** — relé que mantém estado sem bobina alimentada.
24. **MOSFET** — Metal-Oxide-Semiconductor FET.
25. **MOV (Metal-Oxide Varistor)** — absorvedor de surto AC.
26. **NC (Normally Closed)** — contato fechado em repouso.
27. **NO (Normally Open)** — contato aberto em repouso.
28. **Opto-isolador** — isolamento óptico entre comando e potência.
29. **PWM (Pulse Width Modulation)** — modulação por largura de pulso.
30. **RC snubber** — rede RC de absorção de transientes.
31. **Rth (thermal resistance)** — resistência térmica (°C/W).
32. **RDS(on)** — resistência do MOSFET em condução.
33. **Relé de segurança** — categoria 3/4 ISO 13849.
34. **SCR** — Silicon-Controlled Rectifier (tiristor).
35. **SPDT** — Single-Pole Double-Throw.
36. **SPST** — Single-Pole Single-Throw.
37. **SSR (Solid State Relay)** — relé estado sólido.
38. **Surto (surge)** — pico transitório de tensão/corrente.
39. **Suppressor / Snubber** — dispositivo de absorção de surto.
40. **Tempo de acionamento** — latência entre comando e contato fechado.
41. **Time constant (τ)** — L/R da bobina (rapidez de desenergização).
42. **TRIAC** — Triode AC (bidirecional).
43. **TVS diode** — Transient Voltage Suppressor.
44. **Tungstênio (W)** — material de contato para alta corrente DC.
45. **V_clamp (MOV)** — tensão de clamp do varistor.
46. **Vibração (IEC 60068-2-6)** — ensaio de vibração senoidal.
47. **Zero-crossing** — chaveamento no cruzamento por zero AC.
48. **Bobina poupadora (economizer)** — circuito que reduz corrente após pick-up.
49. **Cycle / ciclo** — uma ativação + desativação completa.
50. **Pick-up / drop-out (V)** — tensões de acionamento e repouso da bobina.

## FAQ

**SSR é sempre melhor que relé eletromecânico?**

Não. Depende do tipo de carga, corrente, frequência de acionamento, dissipação e estratégia de falha. **SSR vence** em alta frequência (PWM), ambiente silencioso (cabine à noite), ciclagem intensa (10⁷+ ciclos). **EMR vence** em isolamento galvânico, tolerância a surto, diagnóstico acessível, dissipação zero em condução, baixo custo, aplicações clássicas (bomba porão, ventilador). Em barco, **ambos convivem**: SSR em PWM de LEDs e controle de motor BLDC; EMR em bomba porão, ventilador, sirene, alarme, trim tabs.

**Posso usar SSR AC em circuito DC?**

**Não** — premissa não é segura. SSR AC usa **TRIAC**, que só extingue no cruzamento por zero da onda senoidal. Em DC, o TRIAC **não extingue jamais** (não há zero-crossing), fica conduzindo até queimar por sobreaquecimento. Para DC, usar SSR específico com **MOSFET** ou IGBT (Crydom D1D, Omron G3NE, Panasonic AQY).

**Relé comum serve para qualquer motor pequeno?**

**Não necessariamente**. Motor tem corrente de partida (inrush) de 5-15× a nominal e componente indutivo que gera BEMF na desenergização. Relé automotivo 30 A pode aguentar bomba de água doce nominal 5 A em estática — mas queimar o contato em 100-1000 ciclos pelo inrush e pela BEMF sem supressão. Relé marine 40 A + diodo de roda livre resolve no mesmo custo.

**Quando usar MOSFET switch (Victron BP) em vez de relé?**

MOSFET switch vence em: (a) **monitoração remota** (Bluetooth, VE.Direct, NMEA 2000) — dá para saber status via MFD ou app; (b) **proteção integrada** — LVC, OVC, térmica programáveis; (c) **zero ruído mecânico** — bom em cabine e salão; (d) **vida útil essencialmente ilimitada** (10⁹+ ciclos); (e) **sem desgaste em alta frequência**. Relé vence em: custo (10× mais barato), tolerância a surto, diagnóstico acessível ("ouço o clique"), não depende de firmware. Em Li-Fe moderno com BMS, MOSFET switch é o padrão.

**Como dimensionar supressão (varistor, diodo) para carga indutiva?**

**AC**: MOV com V_clamp ≈ 1,5-2× V_pico nominal (230 VAC → 325 V_pico → MOV 430-470 V, S14K430 ou S20K430). RC snubber 100 Ω + 100 nF em série, em paralelo com contato. **DC**: diodo 1N5404 (3 A) ou UF4007 (1 A ultra-fast) em bobinas até 2 A; diodo + TVS em paralelo para desativação mais rápida; TVS SMCJ50A para clamp em 70 V. Calcular I_pico = V_alim / R_bobina e verificar If_surge do diodo ≥ I_pico.

**Por que meu relé de carga AC funciona em bancada e falha em carga real?**

Três causas típicas: (i) **inrush não previsto** — lâmpada halógena ou motor tem pico 10× maior que o regime; (ii) **dV/dt alto** em bancada não reproduzido — fonte chaveada moderna tem transientes que SSR AC precisa filtrar; (iii) **temperatura ambiente real diferente** — bancada 20 °C vs. sala de máquinas 55 °C; derating de SSR pode reduzir capacidade em 50%. Ensaio correto: aplicar carga real + ambiente real + 100-500 ciclos antes de aprovar.

**Relé latching (biestável) é mais eficiente em barco?**

**Sim para cargas de longo período ligadas/desligadas**. Relé standard DC consome 50-200 mA na bobina enquanto ativo (0,6-2,4 W contínuo) — em 10 relés sempre ligados, 5-25 W drena o banco. **Latching** consome só pulsos de 50-100 ms para SET e RESET — consumo médio ≈ zero. Ideal em subsistemas que ficam em estado fixo por horas/dias (chave de iluminação de cabine, modo de operação noturno). **Não recomendado** onde perda do estado em queda de tensão não pode ser tolerada (alarmes, safety) — relé standard falha no estado seguro conhecido; latching mantém o estado pré-queda, pode ficar em NO quando deveria estar em NC.

## Integração com outras notas

- [[Contatores (AC)]]
- [[Chaves Gerais (DC)]]
- [[Atuador Linear]]
- [[Sistema de Alarme Geral - Painel de Alarmes]]
- [[Automação de Bordo - Sistemas Domoticos]]
- [[Disjuntores (DC) e (AC)]]
- [[Hotline (DC)]]
- [[Bomba de Porão]]
- [[Divisores de Carga (DC)]]
- [[Quadro Elétrico e Painel de Distribuição AC-DC]]

## Perguntas que esta nota responde

- Quando usar relé eletromecânico ou estado sólido em embarcações?
- Quais erros técnicos são mais comuns na seleção de relés?
- Como diagnosticar falhas de comando e comutação em bordo?
- Qual a diferença entre SSR AC e SSR DC?
- Quando usar MOSFET switch (Victron BP) em vez de relé?
- Como dimensionar supressão para carga indutiva?
- Relé latching é mais eficiente em barco?
