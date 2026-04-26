---
title: "Backlog Operacional — Coleta de Manuais"
note_type: "backlog"
domain: "90_Revisao_Manual"
status: "active-curation"
reviewed_on: "2026-04-19"
review_jurisdiction: "Brasil"
aliases:
  - "Fila Operacional de Manuais"
  - "Coleta de Manuais por Marca e Modelo"
related_notes:
  - "Padrão da Biblioteca de Referência Técnica"
  - "MOC — Revisao Manual"
  - "Inventário Completo — Marcas e Modelos Citados no Corpus"
  - "Acervo de Manuais — Marcas e Modelos Prioritários"
  - "Links Oficiais Confirmados — Lote A"
  - "Tabela-Mestre do Acervo — Biblioteca de Referência"
  - "Matriz de Fontes — Fabricantes e Repositórios"
  - "Matriz de Marcas Matriz — Ecossistemas e Subgrupos"
  - "Matriz Dometic — Subgrupos, Linhas e Documentos"
  - "Matriz de Modelos e Versões — Geradores"
---

# Backlog Operacional — Coleta de Manuais

> [!abstract] Resumo técnico
> Esta nota converte o inventário completo e a fila priorizada em um backlog executável. Cada linha representa uma frente prática de busca oficial, download, triagem e curadoria para compor o acervo técnico da base.

Os links oficiais já consolidados do `Lote A` estão em [[Links Oficiais Confirmados — Lote A]].
Para controle central da biblioteca, usar [[Tabela-Mestre do Acervo — Biblioteca de Referência]].
Para cruzar o backlog com a camada `source-first`, usar [[Matriz de Fontes — Fabricantes e Repositórios]].
Para marcas com várias submarcas e linhas históricas, usar [[Matriz de Marcas Matriz — Ecossistemas e Subgrupos]].
Para o ecossistema Dometic, usar [[Matriz Dometic — Subgrupos, Linhas e Documentos]].
Para geradores com múltiplas variantes, usar [[Matriz de Modelos e Versões — Geradores]].

Usar esta nota junto com [[_Editorial/Padrão da Biblioteca de Referência Técnica|Padrão da Biblioteca de Referência Técnica]].

## Regra operacional desta nota

- uma linha não precisa equivaler a um PDF único; ela pode representar uma família de produto quando o fabricante publica manual consolidado por série;
- o escopo desta fila é `mercado náutico`; não priorizar nesta nota linhas `RV`, `residenciais`, `standby` ou `industriais terrestres` como se fossem biblioteca principal;
- para `geradores`, a coleta mínima útil é o pacote triplo `manual de serviço + manual operacional + parts manual`; `installation manual`, `spec sheet`, `brochure` e `product guide` contam como camada complementar;
- `coleta` mede o estágio de localização e captura do material;
- `curadoria` mede o estágio de organização técnica do material baixado;
- quando o portal oficial ainda não foi mapeado nesta rodada, a coluna `url oficial` fica como `pendente`;
- usar esta nota junto com [[Inventário Completo — Marcas e Modelos Citados no Corpus]] para garantir cobertura e com [[Acervo de Manuais — Marcas e Modelos Prioritários]] para definir a ordem de ataque.
- quando a família começar a ser trabalhada de verdade, espelhar o andamento também em [[Tabela-Mestre do Acervo — Biblioteca de Referência]].
- para `geradores`, preferir avanço por `blocos náuticos de família/plataforma` antes de cair para `um modelo isolado`.
- quando uma linha de `geradores` for aberta de verdade, registrar na [[Tabela-Mestre do Acervo — Biblioteca de Referência]] o `motor-base / modelo do motor` e `cilindros` antes de começar o download em massa.

## Legenda de status

- `pendente`: ainda sem portal oficial confirmado nesta nota.
- `portal mapeado`: fonte oficial principal já identificada.
- `manual localizado`: manual relevante já encontrado no portal oficial.
- `baixado`: arquivo já coletado para o acervo local.
- `curado`: material já triado, nomeado e pronto para uso interno.

## Lote A — Coleta imediata

| ID | Prioridade | Categoria | Marca | Modelos / famílias-alvo | Tipo de manual alvo | URL oficial | Coleta | Curadoria |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MAN-A01 | A | Monitoramento de bateria | Victron Energy | SmartShunt 500A, BMV-712, BMV-700 | instalação, operação, integração VE.Smart | [Victron](https://www.victronenergy.com/support-and-downloads/manuals) | manual localizado | não iniciado |
| MAN-A02 | A | Carregadores AC/DC | Victron Energy | Blue Smart IP65, Blue Smart IP22, Phoenix Charger, Skylla TG | instalação, operação, curva de carga | [Victron](https://www.victronenergy.com/support-and-downloads/manuals) | manual localizado | não iniciado |
| MAN-A03 | A | Inversores e inversores/carregadores | Victron Energy | Phoenix Inverter, MultiPlus, Quattro | instalação, operação, esquemas e configuração | [Victron](https://www.victronenergy.com/support-and-downloads/manuals) | manual localizado | não iniciado |
| MAN-A04 | A | Baterias e lítio | Victron Energy | Smart Lithium, AGM Deep Cycle, GEL | instalação, integração com BMS, fichas técnicas | [Victron](https://www.victronenergy.com/support-and-downloads/manuals) | manual localizado | não iniciado |
| MAN-A05 | A | Telemetria e energia | Victron Energy | Cerbo GX, GlobalLink 520, documentação VRM | instalação, comissionamento, portal remoto | [Victron](https://www.victronenergy.com/support-and-downloads/manuals) | manual localizado | não iniciado |
| MAN-A06 | A | Carregadores AC/DC | Mastervolt | ChargeMaster, Mass Charger, AC Master | instalação, operação, ajuste de carga | [Mastervolt](https://www.mastervolt.com/downloads/) | manual localizado | não iniciado |
| MAN-A07 | A | Inversores/carregadores e shore power | Mastervolt | Mass Combi, Mass Combi Ultra, MaraTron | instalação, wiring, integração AC/DC | [Mastervolt](https://www.mastervolt.com/downloads/) | manual localizado | não iniciado |
| MAN-A08 | A | Chaves, barramentos e proteção | Blue Sea Systems | m-Series, e-Series, 187-Series, 285-Series, barramentos e porta-fusíveis | instalação, circuit protection, seleção de componentes | [Blue Sea](https://www.bluesea.com/resources) | manual localizado | não iniciado |
| MAN-A09 | A | Alternador e regulador externo | Balmar | alternadores série 6, MC-614, MC-618 | instalação, setup, belt load manager | [Balmar](https://balmar.net/operation-manuals/) | manual localizado | não iniciado |
| MAN-A10 | A | Regulador inteligente de alternador | Wakespeed | WS500, WS500 Pro | instalação, configuração CAN, limites térmicos | [Wakespeed](https://www.wakespeed.com/product/ws500-advanced-alternator-regulator/) | manual localizado | não iniciado |
| MAN-A11 | A | Chartplotter e MFD | Garmin | GPSMAP 742, 942, 1042, 4000/5000, 8400, 8600, 8617 | instalação, operação, rede e updates | [Garmin Marine](https://support.garmin.com/marine/) | parcial em acervo local | em andamento |
| MAN-A12 | A | Radar e sonar | Garmin | GMR 18HD+, GMR Fantom 18/24, GT52, GT54, GT56, Panoptix LiveScope | instalação, transdutor, calibração | [Garmin Marine](https://support.garmin.com/marine/) | manual localizado | não iniciado |
| MAN-A13 | A | Piloto automático e sensores | Garmin | Reactor, GHP 12, GHP 12R, GHC 50, GPS 17x HVS, GPS 19x HVS, GMC 010, GMI 20 + GWS 10 | instalação, comissionamento, calibração | [Garmin Marine](https://support.garmin.com/marine/) | parcial em acervo local | em andamento |
| MAN-A14 | A | MFD, piloto, radar e vento | Simrad | GO5, GO7, NSS, AP44, AP70, RC42N, RPU80, Halo 20/24, IS42 + WS310, HS70 | instalação, operação, NMEA, calibração | [Simrad](https://www.simrad-yachting.com/help--support/service-and-support/) | manual localizado | não iniciado |
| MAN-A15 | A | MFD, piloto e radar | Raymarine | Axiom, Axiom Pro, EV-1, Quantum, SmartPilot ST6002, SeaTalk, i70s + MastView | instalação, operação, calibração | [Raymarine](https://www.raymarine.com/en-us/support/document-library) | parcial em acervo local | em andamento |
| MAN-A16 | A | Navegação e radar profissional | Furuno | NavNet TZtouch3, DRS4D-NXT, GP1971F, SC-50, FI-5002, CAN bus | instalação, operação, radar, GPS compass | [Furuno](https://furunousa.com/en/knowledge_base/general/manuals_for_furuno_products) | parcial em acervo local | em andamento |
| MAN-A17 | A | VHF fixo e portátil | Icom | IC-M330G, IC-M510, IC-M605, IC-M25 | instalação, operação, DSC/AIS | [Icom](https://www.icomamerica.com/support/manual/) | manual localizado | não iniciado |
| MAN-A18 | A | Luz subaquática | OceanLED | Explore E6, Explore E9, Sport Colours | instalação, operação, integração elétrica | [OceanLED](https://www.oceanled.com/downloads/) | manual localizado | não iniciado |
| MAN-A19 | A | Rede NMEA 2000 / 0183 | Actisense | NGT-1 | instalação, diagnóstico, conversão N2K/0183 | [Actisense](https://actisense.com/downloads/) | manual localizado | não iniciado |
| MAN-A20 | A | Rede NMEA 2000 / 0183 | Maretron | USB100 | instalação, diagnóstico, monitoramento de backbone | [Maretron](https://www.maretron.com/support/manuals/USB100UM_1.7.pdf) | manual localizado | não iniciado |
| MAN-A21 | A | VHF com AIS integrado | Standard Horizon | GX1850, GX1850G, GX2000, GX2150, GX2400, GX2400G, HX890 | instalação, operação, DSC e AIS | [Standard Horizon](https://www.standardhorizon.com/) | parcial em acervo local | em andamento |
| MAN-A22 | A | Conectividade a bordo | Starlink | Mini, Performance, Roam, Maritime | instalação, alimentação, montagem e uso móvel | [Starlink](https://starlink.com/us/residential/installation) | manual localizado | não iniciado |

## Lote B — Segunda rodada

| ID | Prioridade | Categoria | Marca | Modelos / famílias-alvo | Tipo de manual alvo | URL oficial | Coleta | Curadoria |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MAN-B01 | B | Inversores/carregadores | Xantrex / Schneider Electric | TrueCharge 2, Freedom, XW+ | instalação, operação, troubleshooting | [Xantrex Support](https://xantrex.com/support/get-customer-support/) | manual localizado | não iniciado |
| MAN-B02 | B | Carregadores e isolador galvânico | ProMariner | ProNautic Series, ProSafe | instalação, operação, proteção AC | [ProMariner Resources](https://promariner.navico.com/resources/) | portal mapeado | não iniciado |
| MAN-B03 | B | Shore power e transformadores | Charles Industries | Guardian, isolation transformers, step-up/down marinho | instalação, wiring, isolamento galvânico | [Charles](https://www.charlesindustries.com/support/technical-emergency-support/industrial-solutions/owners-manuals/) | manual localizado | não iniciado |
| MAN-B04 | B | Shore power e conectores | Marinco | conectores de cais e acessórios de shore power | instalação, torque, vedação, montagem | [Marinco Inlets](https://www.marinco.com/en/~/media/inriver/331521-19774.pdf) | manual localizado | não iniciado |
| MAN-B05 | B | Shore power e conectores | Hubbell Marine | conectores de cais e acessórios de shore power | instalação, torque, vedação, montagem | [Hubbell Installation Instructions](https://www.hubbell.com/wiringdevice-kellems/en/installation-instructions) | manual localizado | não iniciado |
| MAN-B06 | B | Transformadores marinhos | Toroid Marine | transformadores de isolamento e step-up/down | instalação, operação, proteção | pendente | pendente | não iniciado |
| MAN-B07 | B | Transformadores e shore power premium | ASEA Power Systems | isolamento e conversão AC marinha | instalação, operação, proteção AC | pendente | pendente | não iniciado |
| MAN-B08 | B | Baterias LiFePO4 | Battle Born | 100Ah, 200Ah | operação, instalação, integração com carregadores | [Battle Born](https://battlebornbatteries.com/manuals/) | portal mapeado | não iniciado |
| MAN-B09 | B | Baterias LiFePO4 | SOK Battery | 100Ah, 200Ah | operação, instalação, integração com carregadores | pendente | pendente | não iniciado |
| MAN-B10 | B | Baterias LiFePO4 | Epoch, Ampere Time / LiTime | linhas de 12 V e 24 V citadas no corpus | operação, instalação, limites de carga | pendente | pendente | não iniciado |
| MAN-B11 | B | BMS | Daly, JBD / Overkill Solar, Electrodacus | BMS de retrofit e DIY | wiring, parâmetros, alarmes, proteções | pendente | pendente | não iniciado |
| MAN-B12 | B | BMS profissional | REC BMS, Orion BMS | integração CAN, contactor, lítio | instalação, configuração, CAN bus | pendente | pendente | não iniciado |
| MAN-B13 | B | EPIRB e PLB | ACR | GlobalFix Pro, RapidFix, ResQLink 400 | operação, registro, teste e inspeção | [ACR](https://www.acrartex.com/support/) | manual localizado | não iniciado |
| MAN-B14 | B | EPIRB e PLB | McMurdo | Smartfind E8, Smartfind Plus, Fast Find | operação, registro, teste e inspeção | pendente | pendente | não iniciado |
| MAN-B15 | B | EPIRB e MOB | Ocean Signal | E100G, MOB1 | operação, registro, teste e integração AIS/MOB | [Ocean Signal](https://oceansignal.com/us/support/documents/) | manual localizado | não iniciado |
| MAN-B16 | B | EPIRB e MOB | Kannad | SafePro, SafeSea MOB | operação, registro, teste e inspeção | pendente | pendente | não iniciado |
| MAN-B17 | B | AIS dedicado | Vesper Marine | linha WatchMate | instalação, operação, integração NMEA | pendente | pendente | não iniciado |
| MAN-B18 | B | AIS dedicado | em-trak | transponders Classe B citados no corpus | instalação, operação, MMSI e GNSS | pendente | pendente | não iniciado |
| MAN-B19 | B | AIS, gateways e integrações | Digital Yacht | iKonvert e soluções AIS modulares | instalação, rede, conversão de dados | pendente | pendente | não iniciado |
| MAN-B20 | B | Instrumentação de vento e veleiro | B&G | Precision 9, Triton2 + WS310, `WTP1` (citado) / `WTP3` (linha oficial atual) | instalação, calibração, rede NMEA, quick start, software/updates | [B&G Downloads](https://www.bandg.com/downloads/) | manual localizado | não iniciado |
| MAN-B21 | B | Sonar e fishfinder | Lowrance | StructureScan | instalação, transdutor, operação | pendente | pendente | não iniciado |
| MAN-B22 | B | Sonar e fishfinder | Humminbird | Down Imaging | instalação, transdutor, operação | pendente | pendente | não iniciado |
| MAN-B23 | B | Luzes de navegação e emergência | Hella Marine | EasyFit Emergency, navegação 2NM/3NM, âncora, cortesia | instalação, homologação, operação | pendente | pendente | não iniciado |
| MAN-B24 | B | Iluminação premium e RGB | Lumitec | SeaBlaze, Emergency LED, cortesia/RGB, dimmers compatíveis | instalação, controle, consumo e zonas | [Lumitec](https://www.lumiteclighting.com/support-center.html) | manual localizado | não iniciado |
| MAN-B25 | B | Luzes de navegação | Aqua Signal | linhas de navegação, tope e âncora | instalação, homologação, substituição | pendente | pendente | não iniciado |
| MAN-B26 | B | Luzes de navegação | Perko | navegação, âncora, masthead | instalação, homologação, substituição | pendente | pendente | não iniciado |
| MAN-B27 | B | Luzes portáteis | Navisafe | âncora e navegação portáteis | operação, autonomia, fixação | [Navisafe](https://navisafe.com/) | portal mapeado | não iniciado |
| MAN-B28 | B | Farol de busca | Jabsco | Searchmaster | instalação, operação, comando remoto | [Jabsco Search Lights](https://www.xylem.com/en-us/products--services/light-power/search-lights-and-flood-lights/135sl-remote-control-searchlight-2dcd11d9/) | manual localizado | não iniciado |
| MAN-B29 | B | Dimmers e iluminação de iate | Quick | dimmers touch, `QNN`, `QCC` e linhas de iluminação | instalação, operação, integração, datasheet e brochure | [Quick Manuals](https://www.quickitaly.com/en/manuals/) | manual localizado | não iniciado |
| MAN-B30 | B | Estabilização | Seakeeper | Seakeeper Ride `450`, `525`, `600`, `750`, `750 Quad` e familia superior no hub oficial | instalação, operação, manutenção, configuração, troubleshooting | [Seakeeper Ride Manuals](https://manuals.seakeeper.com/ride/) | manual localizado | não iniciado |
| MAN-B31 | B | Geradores marítimos | Cummins / Onan | todos os `MDK` marinhos possiveis: `MDKBH`, `MDKBJ`, `MDKBW`, `MDKDL`, `MDKDK`, `MDKDM`, `MDKDN`, `MDKDP`, `MDKDR`, `MDKDV`, `MDKDS`, `MDKDT`, `MDKDU`; legado `MDKBK` ate `MDKBV`; bloco grande `MDDC*` (ex.: `MDDCW`, `MDDCU`, `MDDCY`, `MDDCS`, `MDDCT`, `MDDCH`, `MDDCJ`, `MDDCN`, `MDDCP`, `MDDCR`) | service manual, manual operacional, parts manual, installation manual, spec sheet, troubleshooting, product guide, levantamento de `motor-base / modelo do motor` e `cilindros` | [Cummins Marine Resources](https://www.cummins.com/generators/marine/resources) | portal mapeado | não iniciado |
| MAN-B32 | B | Geradores marítimos | Rehlko / Kohler Marine | bloco náutico pequeno `5EFKOD`, `6EKOD`, `7EFKOZD`; bloco náutico médio `9/11/12/13.5 EKOZD/EFKOZD`; bloco náutico grande `45-175 EFOZDJ/EOZDJ` | service manual, manual operacional, parts manual, installation manual, technical documents, brochures, pocket guide, levantamento de `motor-base / modelo do motor` e `cilindros` | [Rehlko Marine](https://www.marine.rehlko.com/) | parcial em acervo local | em andamento |
| MAN-B33 | B | Dometic climate | Dometic | ECD, DCU, DLU, GT, GTX, GVTX, VARCX, DEGX, fan coils, air handlers, aliases Cruisair / Condaria / Marine Air | instalação, operação, service, displays, painéis, AC guide, climatização | [Dometic Marine Partner Resources](https://www.dometic.com/en-us/lp/marinelp-dometic-marine) | manual localizado | não iniciado |
| MAN-B34 | B | Xylem marine | Jabsco / Rule | Twist 'n' Lock, electric marine toilet, Rule-Mate, Standard Bilge, Dry Bilge, shower drain, engine cooling pumps | instalação, operação, manutenção, troubleshooting, portfolio, pump database | [Xylem Jabsco](https://www.xylem.com/en-us/brand/jabsco/) | manual localizado | não iniciado |
| MAN-B35 | B | Thrusters e utilidades | VETUS | BOW2512B, BOW3512, BOW6012B/BOW6024B, BOW7512/BOW7524, BOW9512/BOW9524, BOW12512B/BOW12524B, BOW28548 | instalação, operação, parts catalogue, utilidades, catálogo corporativo | [VETUS Manuals](https://vetus.com/service-support/manuals/) | manual localizado | não iniciado |
| MAN-B36 | B | Dometic marine control | Dometic SeaStar / BayStar / Optimus / Xtreme | displays ED1700, ED1800, Optimus Link, electronic controls, jack plates, trim tabs, steering systems | instalação, setup, calibração, displays, painéis, catálogos, service | [Marine Control](https://www.dometic.com/en-us/outdoor/boat/marine-control) | manual localizado | não iniciado |
| MAN-B37 | B | Dometic pumps and controls | Dometic | MagDrive P030/P045/P062/P075/P100/P137/P150/P200, ECD digital control, touch-screen chiller control | instalação, operação, painel, troubleshooting, parts, leaflets | [Dometic MagDrive Pump](https://www.dometic.com/en-us/outdoor/boat/marine-air-conditioners/marine-climate-water-pumps/dometic-magdrive-pump-328692) | manual localizado | não iniciado |
| MAN-B38 | B | Dometic sanitation e conforto | Dometic | MasterFlush, toilets, holding tanks & pumps, galley, refrigerators, sinks, blinds, consumíveis | instalação, operação, guides, replacement parts, product literature | [Dometic Marine Partner Resources](https://www.dometic.com/en-us/lp/marinelp-dometic-marine) | manual localizado | não iniciado |
| MAN-B39 | B | Climatização marinha | Webasto | `FCF Classic`, `FCF Platinum`, `BlueCool S-Series`, `BlueCool C-Series`, `BlueCool VX-Series`, `BlueCool A-Series`, `BlueCool MyTouch` | self-contained, chilled water, controls, datasheet, catálogo técnico | [Webasto Cooling](https://www.webasto.com/en-us/cooling.html) | portal mapeado | não iniciado |
| MAN-B40 | B | Climatização marinha DC/AC | Mabru | `SC5DC`, `SC7DC`, `SC12DC`, `SC05VI`, `SC09VI`, `SC17VI`, `12V Dome`, `RadAir` | instalação, operação, wiring, pump, troubleshooting, specs | [Mabru 12V DC Units](https://www.mabrumarine.com/dc-air-conditioning-units) | baixado | não iniciado |
| MAN-B41 | B | Climatização marinha | FRIGOMAR | `SCU07/10/12/16/24 VFD`, `SCU HE 07/10/12/16 VFD`, `CU chillers`, `AH fancoils`, `APDS thermostats` | self-contained, chilled water, thermostats, datasheet, brochure | [FRIGOMAR Download](https://www.frigomar.com/en/download/) | portal mapeado | não iniciado |
| MAN-B42 | B | Climatização náutica Brasil-primeiro | H-Tec | `HFC 8K`, `HFC 12K`, `HFC 16K`, `HFC 21K`, painéis digitais e linha `Acqua` | catálogo técnico, instalação, operação, painéis, dessalinizadores | [H-Tec Náutica](https://www.htecnautica.com.br/) | portal mapeado | não iniciado |

## Lote C — Long tail, apoio técnico e lacunas Brasil-primeiro

| ID | Prioridade | Categoria | Marca | Modelos / famílias-alvo | Tipo de manual alvo | URL oficial | Coleta | Curadoria |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MAN-C01 | C | Baterias chumbo-ácido | Trojan | T-series | operação, ficha técnica, curvas de carga | pendente | pendente | não iniciado |
| MAN-C02 | C | Baterias AGM | Fullriver | DC-series | operação, ficha técnica, limites de carga | pendente | pendente | não iniciado |
| MAN-C03 | C | Baterias Brasil | Moura, Heliar, Tudor / Exide | estacionárias e AGM citadas no corpus | ficha técnica, carga, aplicação | pendente | pendente | não iniciado |
| MAN-C04 | C | Baterias GEL | Sonnenschein, Banner | linhas GEL citadas no corpus | ficha técnica, carga, temperatura | pendente | pendente | não iniciado |
| MAN-C05 | C | Células LiFePO4 | CATL, EVE Energy, Winston Battery | células prismáticas para bancos DIY | ficha técnica, torque, limites térmicos | pendente | pendente | não iniciado |
| MAN-C06 | C | Carregadores de manutenção | NOCO, CTEK, Intelbras | linhas citadas no corpus | operação, curva de carga, manutenção | pendente | pendente | não iniciado |
| MAN-C07 | C | Hardware elétrico | Ancor, Paneltronics | cabos, terminais, painéis e acessórios | instalação, seleção e aplicação | pendente | pendente | não iniciado |
| MAN-C08 | C | Ânodos e corrosão | Martyr Anodes / MG Duff, Yandina | ânodos, isoladores e proteção galvânica | instalação, manutenção, inspeção | pendente | pendente | não iniciado |
| MAN-C09 | C | Iluminação subaquática | Aqualuma, Bluefin LED | linhas subaquáticas citadas no corpus | instalação, vedação, consumo | pendente | pendente | não iniciado |
| MAN-C10 | C | Busca e sinalização | Sealite, Vega | faróis de busca e sinalização | instalação, operação, alcance | pendente | pendente | não iniciado |
| MAN-C11 | C | Iluminação interior | Imtra, Clipsal Marine, Vitrifrigo | cortesia, dimmers e acessórios de cabine | instalação, controle e alimentação | pendente | pendente | não iniciado |
| MAN-C12 | C | Fitas LED e fornecedores gerais | Paulmann, Soltek, Ledison / Ledvance | fitas e drivers citados no corpus | ficha técnica, IP, dissipação térmica | pendente | pendente | não iniciado |
| MAN-C13 | C | Segurança e emergência | Fire Angel, 3M Safety Sign, Rule / Attwood | iluminação de emergência e sinalização | instalação, operação, inspeção | pendente | pendente | não iniciado |
| MAN-C14 | C | Acessórios de GPS externo | Bad Elf, Garmin GLO | receptores GNSS auxiliares | operação, pareamento e integração | pendente | pendente | não iniciado |
| MAN-C15 | C | Refrigeração Brasil-primeiro adjacente | Gelotec | fabricador de gelo em barras, reservatórios térmicos / boilers e linhas inox de refrigeração | catálogo técnico, assistência, peças e documentação de produto | [Gelotec Refrigeração](https://gelotecrefrigeracao.com.br/) | portal mapeado | não iniciado |
| MAN-C16 | C | Marca nacional a validar | Schutz | grafia, fabricante e aplicação náutica a confirmar | portal, catálogo e documentação técnica | pendente | pendente | não iniciado |

## Rotina recomendada de execução

1. Fechar primeiro todas as linhas com `coleta = portal mapeado`.
2. Em seguida, mapear portal oficial das linhas `pendente` e atualizar somente a coluna `url oficial`.
3. Depois da localização do PDF correto, mudar `coleta` para `manual localizado`.
   Para `geradores`, só promover a linha quando o pacote triplo `serviço + operacional + parts` estiver claramente identificado.
4. Após download, padronizar nome de arquivo no formato `marca__familia-modelo__tipo-manual__rev-ano`.
5. Quando o material estiver triado, renomeado e tecnicamente útil, marcar `curadoria = curado`.

## Próximos desdobramentos úteis

- exportar esta tabela para Notion/Base44 como base operacional;
- criar uma pasta-padrão de acervo por `marca > família > tipo de manual`;
- separar depois uma nota só para `links oficiais confirmados`;
- abrir a próxima rodada editorial para `70_` e `80_`, onde ainda faltam fabricantes e modelos no corpus.
