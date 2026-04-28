---
title: "Carregador Elétrico para Tender e Jet Ski"
note_type: "technical-note"
domain: "30_Energia_e_Conversao"
status: "premium-l3"
fase_6_reescrita: 104
reviewed_on: "2026-04-26"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://webstore.iec.ch/publication/2697"
review_level: "engineering-curated"
aliases:
  - "Carregador tender"
  - "Carregador jet ski"
  - "Tender charger"
  - "Jet ski charger"
  - "PWC charger"
  - "Onboard charger marine"
seo_title: "Carregador para tender e jet ski: ABYC E-11, IEC 60364, 12V/24V/48V/72V, multi-stage, AC shore-power"
seo_description: "Guia técnico premium do carregador AC-DC para tender (RIB / dinghy elétrico) e jet ski (PWC) embarcado em yacht: integração com shore-power do barco-mãe, ABYC E-11, IEC 60364, multi-stage charger (Bulk-Absorption-Float), tipos de bateria embarcada (chumbo × LFP), proteção (ELCI 30mA + bonding), modelos típicos (CTEK, Mastervolt, Victron, Sterling, ProMariner)."
seo_keywords:
  - "carregador tender"
  - "carregador jet ski"
  - "PWC charger marine"
  - "shore-power tender"
  - "CTEK Multi US"
  - "Mastervolt ChargeMaster"
  - "Victron Blue Smart"
  - "Sterling Pro Charge"
  - "ProMariner ProSport"
  - "ELCI 30mA tender"
geo_queries:
  - "Como carregar tender elétrico embarcado em yacht?"
  - "Jet ski no mega-iate — como recarregar bateria?"
  - "Onboard charger AC vs DC para tender?"
  - "Bateria LFP em tender: carregador específico?"
  - "Pode usar carregador automotivo no jet ski marine?"
  - "Cabo de tender ao yacht — bitola?"
  - "Carregamento durante navegação ou só em marina?"
  - "Multi-stage charging vs trickle?"
  - "Tender 12V vs jet ski 12V: mesmo carregador?"
  - "ELCI obrigatório no circuito do tender?"
normas_citadas:
  - "ABYC E-11 (AC and DC Electrical Systems on Boats)"
  - "ABYC E-11.5 (Overcurrent protection)"
  - "ABYC E-11.16 (Bonding)"
  - "ABYC E-11.11.1.6 (ELCI 30mA)"
  - "ABYC TE-04 (Lightning protection)"
  - "ABYC E-13 (Hybrid/Electric Propulsion — emergente)"
  - "IEC 60364-7-709 (Marinas)"
  - "IEC 60092-507 (Pleasure craft)"
  - "IEC 61851 (Electric Vehicle Conductive Charging — referência cruzada)"
  - "IEC 62196 (Plugs/connectors)"
  - "IEC 60529 (IP)"
  - "ISO 13297 (AC installations)"
  - "ISO 28848 (DC installations)"
  - "ISO 6185 (Inflatable boats — tender RIB)"
  - "SAE J1772 (EV charging connector — referência)"
  - "USCG 33 CFR 183 (Electrical systems)"
  - "USCG 33 CFR 175 (Carriage requirements)"
  - "EU Directive 2014/35/EU (LVD)"
  - "EU Directive 2014/30/EU (EMC)"
  - "EU Directive 2013/53/EU (RCD)"
  - "ABNT NBR 14728"
  - "ABNT NBR 5410"
  - "ABNT NBR IEC 61851"
  - "INMETRO Portaria 144/2015"
  - "ANATEL Resolução 715/2019"
  - "DPC NORMAM-211/DPC"
  - "DPC NORMAM-201/DPC"
  - "Manual técnico CTEK Multi US 7002 / MXS 5.0 / D250SE"
  - "Manual técnico Mastervolt ChargeMaster Plus / Mass Charger"
  - "Manual técnico Victron Blue Smart IP65/IP67 / Phoenix Charger"
  - "Manual técnico Sterling Pro Charge B / Pro Charge Ultra"
  - "Manual técnico ProMariner ProSport / ProTech / ProSport Plus"
  - "Manual técnico Noco Genius series"
  - "Manual técnico Torqeedo Travel / Cruise (tender elétrico)"
  - "Manual técnico Yamaha / Sea-Doo / Kawasaki PWC chargers"
related_notes:
  - "Tipos de Bateria"
  - "Bancos de Bateria"
  - "Carregador de Bateria (AC To DC)"
  - "Inversora (DC To AC)"
  - "CAIS (Pier) (AC)"
  - "Cabeamento Náutico"
  - "Dimensionamento de Cabos DC — Cálculo Prático"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Disjuntores (DC) e (AC)"
  - "Bonding — Sistema de Interligação de Massas"
  - "DR (Dispositivo Diferencial Residual)"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
  - "Davit - Munk - Guindaste de Bote - Tender Lift"
---

# Carregador Elétrico para Tender e Jet Ski

> [!abstract] Resumo técnico
> O **carregador elétrico para tender (RIB / dinghy / annex) e jet ski (PWC — Personal Watercraft) embarcado em yacht** é o sistema **AC-DC ou DC-DC** que recarrega a bateria do bote auxiliar / jet ski quando a embarcação principal está em marina (shore-power) ou em viagem (gerador / banco). **Tender elétrico** está em forte expansão (Torqeedo, Bellmarine, Oceanvolt, Highfield Sport — banco LFP de 1-15 kWh em 24V/48V); **jet ski** ainda predominantemente combustão interna mas com bateria 12V para partida + acessórios. **Carregador específico** dimensionado por: **química de bateria (chumbo-ácido × AGM × LFP)**, **tensão (12V/24V/48V/72V)**, **capacidade Ah**, **fonte AC (110V/220V) ou DC (12/24/48V via banco mãe)**. Padrões: **ABYC E-11** + **E-11.11.1.6** (ELCI 30 mA obrigatório) + **E-11.16** (bonding) + **IEC 60364-7-709** (marinas) + **ABYC E-13** (hybrid/electric propulsion — emergente). Fabricantes: **CTEK, Mastervolt, Victron, Sterling, ProMariner, Noco** + OEM (Torqeedo, Yamaha, Sea-Doo, Kawasaki).

> [!tldr] TL;DR — 9 regras inegociáveis
> 1. **Carregador específico para a química de bateria.** Chumbo-ácido (FLA/AGM/Gel): multi-stage clássico. **LFP requer carregador certificado para LFP** (perfil de tensão diferente; nunca usar chumbo charger em LFP).
> 2. **Tensão correta** — tender 24V/48V/72V não-ambíguo; jet ski 12V; mega-iate pode ter mistura.
> 3. **Cabo dimensionado** para corrente máxima + queda <3%; fusível ANL/MIDI a 125% nominal (ABYC E-11.5).
> 4. **ELCI 30 mA / 100 ms** no circuito AC do shore-power (ABYC E-11.11.1.6) — proteção pessoa em ambiente molhado. **DR diferencial em BR/UE** (NBR 5410 + IEC 60364).
> 5. **Bonding da carcaça do carregador** (ABYC E-11.16) — corrosão galvânica + segurança.
> 6. **Multi-stage charger** preferível: Bulk → Absorption → Float (chumbo); Bulk → Absorption (LFP, sem float alto contínuo).
> 7. **Localização ventilada e seca** — calor do carregador em compartimento fechado reduz vida; umidade corrói.
> 8. **Conexão tender → yacht** via cabo dedicado + plugue marine (Marinco / Hubbell) ou conexão DC direta com fusível de cada lado.
> 9. **Backup AC + DC** para tender crítico — não confiar em só uma fonte.

> [!danger] Cenários de risco
> - **Carregador chumbo em bateria LFP:** perfil de tensão errado (chumbo float 13,5-13,8V mantém LFP "cheia" continuamente fora de spec) → desbalanceamento de células → BMS desliga ou célula em risco. **Prevenção:** carregador certificado LFP (Victron Smart / Mastervolt LFP charge).
> - **ELCI ausente no tender em marina:** falha de isolação AC → casco da marina aterrado → corrente em água → choque grave em swimmer. **Prevenção:** ABYC E-11.11.1.6 ELCI 30 mA obrigatório.
> - **Cabo subdimensionado** carregando tender 48V × 30A: queda excessiva → carregamento ineficiente + sobreaquecimento de cabo → fogo. **Prevenção:** AWG dimensionado para corrente + queda <3%.
> - **Carregador automotivo em jet ski marine:** sem ignition protection (vapor de gasolina) → arco do circuito interno → ignição. **Prevenção:** marine-grade only; ISO 8846 / SAE J1171 / UL 1500.
> - **Sobrecarga em LFP sem BMS adequado:** tensão > 14,6V (LFP 4-cell) → célula sobre-carregada → thermal runaway → fogo. **Prevenção:** BMS no tender; carregador com proteção de fim-de-carga.
> - **Surge atmosférico via cabo de carregamento** queima banco do tender + carregador: cabo longo entre yacht e tender atado em mastro = antena para raio. **Prevenção:** ABYC TE-04 surge protection; desconectar em tempestade.
> - **Tender alagado em chuva** + carregador conectado: água em circuito DC → curto + corrosão acelerada. **Prevenção:** capa do tender; conector estanque IP67; desligar antes de tempestade.
> - **Bateria descarregada por tempo prolongado em tender desconectado:** chumbo abaixo de 11V em meses → sulfatação irreversível. **Prevenção:** desconectar cargas; trickle charge mensal; banco LFP tem auto-discharge baixo.
> - **Cabo de carregamento desconectado durante manobra de davit:** plugue não desabilitado antes de içar tender → cabo arrebenta → curto + risco a tripulação. **Prevenção:** procedimento operacional (desconectar antes de davit); chave de segurança; vide [[Davit - Munk - Guindaste de Bote - Tender Lift]].
> - **Choque elétrico em swimmer próximo a tender carregando:** falha de isolação + ELCI defeituoso → corrente na água → eletrocussão em metros de distância. **Prevenção:** ELCI testado mensalmente; bonding íntegro; "no swimming when charging".

## O que é (definição rigorosa)

O **carregador para tender / jet ski embarcado** é o equipamento de **conversão AC-DC ou DC-DC** dedicado a recarregar baterias auxiliares de embarcação anexa (RIB, dinghy, jet ski) quando a embarcação principal:

- Está em **marina (shore-power)** — fonte AC 110/220V.
- Está em **viagem com gerador** — AC do gerador.
- Está usando **banco mãe** — DC-DC para tender em DC mais alto.

### Categorias de aplicação

#### Tender elétrico (Torqeedo / Bellmarine / Oceanvolt / Highfield Sport)

- **Banco LFP** 1-15 kWh em 24V/48V/72V.
- **Carregador LFP-specific** com BMS comm.
- **Plugue marine** dedicado.
- Cresce em popularidade (zero emissões + silencioso).

#### Tender combustão (RIB / dinghy típico)

- **Bateria 12V** AGM 50-100 Ah.
- **Carregador chumbo multi-stage**.
- **Carregamento ocasional** (a cada poucos meses).

#### Jet ski (PWC — Personal Watercraft)

- **Bateria 12V** AGM 18-30 Ah.
- **Carregador trickle** ou multi-stage pequeno.
- **Manutenção** após cada temporada ou armazenamento.

## Comparação técnica

| Aplicação | Banco | Carregador típico | Corrente | Tempo recarga |
|-----------|-------|--------------------|----------|----------------|
| **PWC 12V/20Ah** | Chumbo / AGM | 5A multi-stage | 5A | 4-6 h |
| **Tender combustão 12V/100Ah** | AGM | 15A multi-stage | 15A | 8-12 h |
| **Tender elétrico 24V/3kWh** | LFP | 30A LFP | 30A | 4-6 h |
| **Tender elétrico 48V/15kWh** | LFP | 60A LFP / 220V | 60A | 5-8 h |
| **Tender elétrico premium 72V** | LFP high-volt | OEM specific | Variável | Variável |

## Fabricantes e modelos dominantes

### Generalistas marine

- **CTEK Multi US 7002** — 7A multi-stage.
- **CTEK MXS 5.0** — 5A multi-stage.
- **CTEK D250SE** — DC-DC charger.

### Mastervolt (Holanda — referência)

- **ChargeMaster Plus** — 25-100A.
- **Mass Charger** — premium high-power.

### Victron (Holanda — top sales)

- **Blue Smart IP65/IP67** — Bluetooth + multi-stage.
- **Phoenix Charger** — high-power.

### Sterling (UK)

- **Pro Charge B** — chumbo-LFP combinado.
- **Pro Charge Ultra** — high-power.

### ProMariner (USA)

- **ProSport** — 6-25A multi-stage.
- **ProTech** — 12-40A premium.
- **ProSport Plus** — multi-bank.

### Noco (USA)

- **Genius series** — entry-level smart.

### OEM specific

- **Torqeedo Travel / Cruise / Deep Blue** — chargers proprietários.
- **Yamaha / Sea-Doo / Kawasaki** — PWC chargers OEM.

> [!example] Comparação Brasil 2024-2026
> | Modelo | Aplicação | Preço (R$) |
> |--------|-----------|------------|
> | Noco Genius 5 | PWC / tender pequeno | 350-700 |
> | CTEK Multi US 7002 | Tender / PWC | 800-1.500 |
> | Victron Blue Smart 12V/15A IP65 | Tender 12V | 1.500-2.800 |
> | ProMariner ProSport 20+ | Tender multi-bank | 2.500-4.500 |
> | Mastervolt ChargeMaster Plus 12/25 | Tender premium | 4.500-9.000 |
> | Sterling Pro Charge Ultra 24/40 | Tender elétrico 24V | 6.000-12.000 |
> | Torqeedo Travel Charger OEM | Tender Torqeedo Travel | 3.500-7.000 |
> | Torqeedo Cruise Charger | Tender Cruise 4.0 | 12.000-25.000 |

## Instalação correta

### Localização

- **Compartimento ventilado e seco** próximo ao tender / PWC.
- **Acessível para manutenção**.
- **Não-bloqueado** por equipamento.

### Cabeamento AC

- **Cabo dedicado** com fusível na origem.
- **ELCI 30 mA** entre shore-power e carregador.
- **Bonding** da carcaça.

### Cabeamento DC (saída do carregador)

- **Plugue marine** (Marinco, Hubbell) ou conexão direta com fusível.
- **Cabo dimensionado** para corrente nominal.
- **Polaridade rigorosa**.

### Proteção

- **ELCI 30 mA** (ABYC E-11.11.1.6).
- **Disjuntor AC** dedicado.
- **Fusível DC** entre carregador e bateria do tender.
- **Bonding** carcaça.
- **Surge protector** se mastro próximo.

## Boas práticas

- **Carregador específico** para a química.
- **ELCI 30 mA** mandatório.
- **Manutenção periódica** das conexões.
- **Trickle charge** em armazenamento.
- **Inspecionar** cabo antes de cada uso.
- **Backup AC + DC** se crítico.
- **Documentar** modelo + tensão + Ah.
- **Treinamento** da tripulação em desconexão / conexão.
- **Procedimento de davit** — desconectar antes de içar.

## Erros comuns

- "Qualquer carregador serve." → Falso. LFP precisa específico.
- "Sem ELCI funciona." → Risco grave em ambiente molhado.
- "Cabo automotivo OK." → Marine-grade tinned é necessário.
- "Pode deixar conectado meses." → Chumbo OK em float; LFP NÃO.

## Glossário

- **Tender:** bote auxiliar.
- **RIB:** Rigid Inflatable Boat.
- **Dinghy:** bote pequeno.
- **PWC:** Personal Watercraft (jet ski).
- **Onboard charger:** embarcado.
- **Multi-stage charger:** Bulk / Absorption / Float.
- **Trickle charge:** carga lenta de manutenção.
- **DC-DC charger:** isola e converte DC↔DC.
- **AC-DC charger:** padrão para shore-power.
- **LFP:** LiFePO4.
- **AGM:** Absorbed Glass Mat (chumbo).
- **FLA:** Flooded Lead-Acid.
- **ELCI:** Equipment Leakage Circuit Interrupter (30 mA marine).
- **GFCI:** Ground Fault Circuit Interrupter (5 mA).
- **DR:** diferencial residencial BR.
- **Plugue Marinco / Hubbell:** padrões marine de conector.
- **Bonding:** ABYC E-11.16.
- **Vide [[Tipos de Bateria]] + [[Bancos de Bateria]] + [[Carregador de Bateria (AC To DC)]]**.

## Integração com outras notas

- [[Tipos de Bateria]] / [[Bancos de Bateria]] — bancos do tender.
- [[Carregador de Bateria (AC To DC)]] — carregador principal do yacht.
- [[Inversora (DC To AC)]] — fonte alternativa.
- [[CAIS (Pier) (AC)]] — shore-power.
- [[Cabeamento Náutico]] / [[Dimensionamento de Cabos DC — Cálculo Prático]].
- [[Fusíveis DC — Proteção Contra Sobrecorrente]] / [[Disjuntores (DC) e (AC)]].
- [[Bonding — Sistema de Interligação de Massas]].
- [[DR (Dispositivo Diferencial Residual)]] — proteção AC.
- [[Quadro Elétrico e Painel de Distribuição AC-DC]].
- [[Davit - Munk - Guindaste de Bote - Tender Lift]] — manuseio do tender.

## Perguntas que esta nota responde

- Como carregar tender elétrico embarcado em yacht?
- Jet ski no mega-iate — como recarregar bateria?
- Onboard charger AC vs DC para tender?
- Bateria LFP em tender: carregador específico?
- Pode usar carregador automotivo no jet ski marine?
- Cabo de tender ao yacht — bitola?
- Carregamento durante navegação ou só em marina?
- Multi-stage charging vs trickle?
- Tender 12V vs jet ski 12V: mesmo carregador?
- ELCI obrigatório no circuito do tender?
- Torqeedo / Bellmarine charger: o que é diferente?
- Procedimento de davit e cabo do tender?
