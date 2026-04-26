---
title: "Inventário Completo — Marcas e Modelos Citados no Corpus"
note_type: "inventory"
domain: "90_Revisao_Manual"
status: "active-curation"
reviewed_on: "2026-04-19"
review_jurisdiction: "Brasil"
aliases:
  - "Inventário Completo de Marcas e Modelos"
  - "Marcas e Modelos do Corpus"
related_notes:
  - "MOC — Revisao Manual"
  - "Acervo de Manuais — Marcas e Modelos Prioritários"
  - "Backlog Operacional — Coleta de Manuais"
  - "Links Oficiais Confirmados — Lote A"
  - "Matriz de Fontes — Fabricantes e Repositórios"
  - "Matriz de Marcas Matriz — Ecossistemas e Subgrupos"
  - "Matriz Dometic — Subgrupos, Linhas e Documentos"
  - "Matriz de Modelos e Versões — Geradores"
---

# Inventário Completo — Marcas e Modelos Citados no Corpus

> [!abstract] Resumo técnico
> Esta nota é a varredura completa do corpus versionado da vault para fins de acervo de manuais. Escopo usado nesta rodada: `193` arquivos Markdown versionados no Git, sendo `148` notas reconhecidas pela validação da vault. Aqui entram as marcas, linhas e modelos que já aparecem nas notas técnicas; o que não aparece aqui ainda não está estruturado no corpus atual.

## Escopo e método

- varredura feita sobre o corpus versionado real do repositório, sem usar cópias em `.claude/worktrees`;
- cobertura integral dos `193` arquivos `.md` rastreados no Git;
- foco prático em marcas, linhas e modelos com utilidade para instalação, diagnóstico, manutenção e futura coleta de manuais;
- consolidação principal por domínio e por nota-fonte;
- esta nota é complementar à [[Acervo de Manuais — Marcas e Modelos Prioritários]], que organiza a ordem de coleta.

## Cobertura já estruturada no corpus

- `22` notas já têm seção explícita de `Principais marcas`, `Marcas e modelos` ou equivalente.
- outras notas relevantes trazem marcas e modelos fora dessas seções, especialmente em energia, shore power, alternador, NMEA e telemetria.
- os domínios `70_` e `80_` ainda têm pouca marcação de fabricante; isso mostra lacuna editorial real e não falha de varredura.

## 20 — Baterias e armazenamento

### [[Bancos de Bateria]]

- AGM ciclo profundo: **Victron Energy AGM Deep Cycle**, **Trojan T-series**, **Fullriver DC-series**, **Moura Estacionária**.
- LiFePO4: **Victron Smart Lithium**, **Battle Born 100Ah**, **SOK 100/200Ah**.
- monitoramento e proteção: **Victron BMV-712**, **Victron SmartShunt**, **Simarine PICO**, **Blue Sea Systems**, **Mastervolt**.

### [[Tipos de Bateria]]

- mercado nacional chumbo/AGM: **Moura**, **Heliar**, **Tudor / Exide**.
- AGM importado: **Victron Energy**, **Fullriver**, **Trojan**.
- GEL: **Victron GEL**, **Sonnenschein (Exide)**, **Banner**.
- LiFePO4: **Victron**, **Battle Born**, **SOK**, **Ampere Time / LiTime**.
- monitoramento citado na nota: **Victron BMV**, **Victron SmartShunt**, **Simarine PICO**.

### [[Lítio LiFePO4 — Instalação e Cuidados Específicos]]

- baterias prontas com BMS integrado: **Battle Born 100Ah / 200Ah**, **Victron Smart Lithium**, **Epoch**, **SOK Battery**, **Ampere Time (LiTime)**.
- células para bancos DIY: **CATL**, **EVE Energy**, **Winston Battery**.

### [[BMS — Battery Management System]]

- BMS DIY / retrofit: **Daly BMS**, **JBD / Overkill Solar**, **Electrodacus**.
- baterias com BMS integrado: **Victron Smart Lithium**, **Battle Born**.
- BMS profissional / CAN bus: **REC BMS**, **Orion BMS**.

### [[Carregador de Bateria (AC To DC)]]

- premium: **Victron Blue Smart IP65**, **Victron Blue Smart IP22**, **Victron Phoenix Charger**, **Victron Skylla TG**, **Mastervolt ChargeMaster**, **ProMariner ProNautic Series**, **Xantrex TrueCharge 2**.
- intermediário / manutenção: **NOCO Genius**, **CTEK**, **Intelbras**.

### [[Monitor de Bateria - BMV - Shunt]]

- monitores principais: **Victron SmartShunt 500A**, **Victron BMV-712**, **Victron BMV-700**, **Simarine PICO**.
- complementares / integração: **Empirbus**, **Garnet SeeLevel**, **Wakespeed WS500**, **Sterling Power BAM**.

## 30 — Energia e conversão

### [[Alternador (DC)]]

- motores de popa citados: **Mercury**, **Yamaha**, **Suzuki**.
- alternadores aftermarket: **Balmar série 6**, **Leece-Neville série 4900**, **Prestolite**.
- reguladores externos: **Balmar MC-614**, **Wakespeed WS500**, **Victron Alternator Controller**.

### [[Gerador (AC)]]

- geradores citados: **Onan (Cummins)** linhas **MDKD** e **MDKBJ**, **Kohler Marine**, **Northern Lights (Lugger)**, **Panda**, **Mase**, **Mastervolt**, **Swell Energy**, **Westerbeke**.

### [[Inversora (DC To AC)]]

- ecossistema Victron: **Phoenix**, **MultiPlus**, **Quattro**.
- ecossistema Mastervolt: **Mass Combi**.
- ecossistema Xantrex / Schneider: **Freedom**, **XW+**.
- outras marcas citadas: **Outback Power**, **Growatt**, **Epever**, **Cotek**, **Must Power**.

### [[CAIS (Pier) (AC)]]

- conectores e shore power: **Marinco**, **Steck**, **Hubbell Marine**.
- isolamento / proteção: **Mastervolt**, **Victron**, **Promariner**, **Charles**.
- pedestais / industrial adaptado: **Palazzoli**, **ABB**.

### [[Transformador Bivolt]]

- fabricantes internacionais citados: **Victron Energy**, **Mastervolt**, **Charles Industries**, **ASEA Power Systems**, **Toroid**.

### [[Transformador Entrada]]

- principais marcas: **Charles Industries**, **Victron Energy**, **Mastervolt MaraTron**, **Hubbell Marine**, **Toroid**.

## 40 — Distribuição, proteção e aterramento

### [[Aterramento]]

- referências de hardware: **Blue Sea Systems**, **Victron Energy**, **Marinco / Hubbell**, **Paneltronics**, **Ancor**.

### [[Bonding — Sistema de Interligação de Massas]]

- componentes e kits: **Blue Sea Systems**, **Ancor**, **Martyr Anodes / MG Duff**, **Perko**, **Shurlock**.

### [[Disjuntores (DC) e (AC)]]

- DC náutico: **Blue Sea Systems**, **Carlingswitch (Sensata)**, **Ancor**.
- AC: **Schneider Electric Acti9 / iC60N**, **ABB S200**, **WEG**.

### [[Proteção Dr]]

- GFCI / painéis: **Leviton**, **Hubbell**, **Blue Sea Systems**.

### [[Isolador Galvânico - Transformador de Isolamento]]

- isoladores galvânicos: **Promariner ProSafe**, **Charles Industries Guardian**, **Victron Energy Galvanic Isolator VGI**, **Yandina**.
- transformadores de isolamento: **Victron Energy Isolation Transformer IT**, **Mastervolt Mass Combi Ultra**, **Charles Industries**, **Toroid Marine**.

## 50 — Navegação, instrumentação e comunicação

### [[Chartplotter - GPS - MFD]]

- muito comum no Brasil: **Garmin GPSMAP 742 / 942 / 1042**, **Simrad NSS**, **Simrad GO**.
- barcos importados: **Raymarine Axiom**, **Garmin GPSMAP 8600**.
- premium / profissional: **Furuno NavNet TZtouch3**, **Garmin GPSMAP 8617**.
- cartografia citada: **Navionics**, **C-MAP**, **Garmin BlueChart**.
- GPS externo em solução tablet: **Bad Elf**, **Garmin GLO**.

### [[AIS (Automatic Identification System)]]

- VHF com AIS integrado: **Standard Horizon GX2400**, **Icom IC-M510**.
- marcas principais: **Vesper Marine** linha **WatchMate**, **Standard Horizon**, **em-trak**, **SRT Marine**, **Garmin** com AIS integrado no **GPSMAP 8400+**, **Digital Yacht**.

### [[Bússola Eletrônica (Compass - HDG Sensor)]]

- GPS compass / AHRS / fluxgate citados:
  - **Garmin GPS 19x HVS**
  - **Simrad HS70**
  - **Furuno SC-50**
  - **B&G Precision 9**
  - **Raymarine EV-1**
  - **Garmin GMC 010**
  - **Simrad RC42N**
  - **ComNav G2 / G2B**

### [[Dsc — Chamada Seletiva Digital]]

- modelos citados:
  - **Standard Horizon GX2400G**
  - **Standard Horizon GX1850G**
  - **Icom IC-M510**
  - **Icom IC-M605**
  - **Garmin VHF 215**
  - **Uniden UM385**
  - **Cobra MR F300FLT**

### [[EPIRB - Beacon de Emergência]]

- modelos citados:
  - **ACR GlobalFix Pro**
  - **ACR RapidFix**
  - **McMurdo Smartfind E8**
  - **McMurdo Smartfind Plus**
  - **Ocean Signal E100G**
  - **Kannad SafePro**
  - **ACR ResQLink 400** como PLB

### [[Estação de Vento - Anemômetro]]

- modelos citados:
  - **Garmin GMI 20 + GWS 10**
  - **B&G Triton2 + WS310**
  - **Raymarine i70s + MastView**
  - **Simrad IS42 + WS310**
  - **Nexus NX2**
  - **Calypso Ultrasonic**
  - **Gill WindSonic**

### [[Mob — Man Overboard — Sistema de Detecção]]

- modelos citados:
  - **Ocean Signal MOB1**
  - **Kannad SafeSea MOB**
  - **McMurdo Fast Find**
  - **ACR ResQLink 400**
  - **Garmin inReach**
  - **Tideline MOB Alert**

### [[NAVEGAÇÃO (BB, BE e Alcançado)]]

- marcas principais de luzes de navegação: **Hella Marine**, **Aqua Signal**, **Perko**, **Attwood**.

### [[NMEA 2000 - NMEA 0183 — Rede de Instrumentos]]

- conversores e gateways: **Actisense NGT-1**, **Garmin GND 10**, **Maretron USB100**, **Digital Yacht iKonvert**.
- componentes do backbone: **Garmin**, **Maretron**, **Actisense**, **Lowrance**.
- ecossistemas proprietários citados: **Raymarine SeaTalkNG**, **Simrad SimNet**.

### [[Piloto Automático]]

- configurações e modelos citados:
  - **Garmin GHP 12**
  - **Simrad AP44**
  - **Raymarine EV-1**
  - **Simrad RPU80**
  - **Garmin GHP 12R**
  - **Garmin Reactor**
  - **Simrad AP70**

### [[Radar]]

- modelos citados:
  - **Garmin GMR 18HD+**
  - **Simrad BR24**
  - **Garmin GMR Fantom 18**
  - **Navico Halo 20**
  - **Furuno DRS4D-NXT**
- famílias principais: **Garmin GMR / GMR Fantom**, **Furuno**, **Simrad**, **Raymarine Quantum**, **Navico/B&G Halo**.

### [[Sonda - Profundímetro - Sonar]]

- conjuntos e modelos citados:
  - **Garmin GPSMAP + GT52 / GT54**
  - **Garmin GPSMAP 8600 + GT56**
  - **Lowrance StructureScan**
  - **Humminbird Down Imaging**
  - **Garmin Panoptix LiveScope**
  - **Furuno GP1971F**
- marcas principais: **Garmin**, **Lowrance**, **Humminbird**, **Furuno**, **Simrad**.

### [[VHF]]

- VHF fixo com DSC: **Standard Horizon GX1850**, **Icom IC-M330G**, **Cobra MR F77**.
- VHF com AIS integrado: **Standard Horizon GX2400**, **Icom IC-M510**.
- VHF portátil de backup: **Icom IC-M25**, **Standard Horizon HX890**.
- marcas principais: **Standard Horizon**, **Icom**, **Cobra**, **Uniden**, **Garmin**.

## 55 — Iluminação e sinalização

### [[Dimmer — Controle de Intensidade Luminosa]]

- marcas citadas: **Blue Sea Systems**, **Victron Energy**, **Clipsal Marine**, **Quick**, **Lumitec**, **Vitrifrigo**, além de PWM genérico.

### [[Farol de Busca]]

- marcas e linhas citadas: **Jabsco Searchmaster**, **Hella Marine**, **Sealite**, **Vega**, **AquaSignal**.

### [[Fitas Led - Iluminação Led]]

- fornecedores citados: **Paulmann**, **Soltek**, **Ledison / Ledvance**, genéricos.

### [[Iluminação de Emergência a Bordo]]

- modelos e referências citadas:
  - **Hella Marine EasyFit Emergency**
  - **Lumitec Emergency LED**
  - **Fire Angel Emergency Light**
  - **3M Safety Sign**
  - **Rule / Attwood LED HOTLINE**

### [[Luz Subaquática]]

- marcas e linhas citadas: **OceanLED**, **Lumitec**, **Aqualuma**, **Bluefin LED**, **SeaBlaze (Lumitec)**.

### [[Luz de Cortesia]]

- marcas citadas: **Hella Marine**, **Lumitec**, **Quick**, **Imtra**.

### [[Luz de Tope]]

- marcas citadas: **Hella Marine**, **Aqua Signal**, **Perko**, **Navisafe**.

### [[Luz de Âncora]]

- marcas citadas: **Hella Marine**, **Aqua Signal**, **Perko**, **Navisafe**, **Ritchie**.

## 60 — Automação, conectividade e monitoramento

### [[Monitoramento Remoto — VRM - Telemetria]]

- ecossistema citado: **Victron Energy VRM**, **GX device**, **GlobalLink 520**, **Multi / Quattro compatíveis**.

### [[Starlink - Internet a Bordo]]

- linhas citadas: **Starlink Mini**, **Starlink Performance**, além das ofertas **Starlink Roam** e **Starlink Maritime**.

## Domínios ainda sem inventário forte de marcas/modelos

- `10_Fundamentos_e_Projeto`: há menções pontuais úteis, mas não um inventário sistemático por equipamento.
- `70_Hidraulica_Climatizacao_e_Utilidades`: domínio de alto valor para manuais, mas ainda pouco marcado por fabricante no corpus atual.
- `80_Seguranca_e_Corrosao`: ainda predominam critérios técnicos e de instalação, não marcas/modelos.

## Lacunas editoriais que valem a próxima rodada

- geladeira/freezer de bordo;
- ar-condicionado marine;
- dessanilizador;
- bombas de porão, água pressurizada e águas negras;
- thruster;
- guincho e windlass;
- detectores de CO e gás;
- extintor automático;
- limpador de parabrisas;
- som, roteador e TV a bordo.

## Encadeamento recomendado

- usar esta nota como fonte base de exaustividade;
- usar [[Acervo de Manuais — Marcas e Modelos Prioritários]] para ordenar a coleta;
- executar a busca e a curadoria em [[Backlog Operacional — Coleta de Manuais]];
- usar [[Links Oficiais Confirmados — Lote A]] como primeira camada de URLs oficiais já verificadas;
- usar [[Matriz de Fontes — Fabricantes e Repositórios]] para a passada `source-first`;
- usar [[Matriz de Marcas Matriz — Ecossistemas e Subgrupos]] quando a marca tiver muitas sublinhas, aliases ou catálogos próprios;
- usar [[Matriz Dometic — Subgrupos, Linhas e Documentos]] para não misturar `Dometic`, `Cruisair`, `Condaria` e `Marine Air`;
- usar [[Matriz de Modelos e Versões — Geradores]] quando marca e modelo mudarem por `spec`, `Hz`, `fase` ou rebranding;
- numa rodada seguinte, abrir uma nota exclusiva para `links oficiais confirmados` e outra para `acervo local baixado`.
