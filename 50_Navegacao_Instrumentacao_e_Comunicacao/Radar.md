---
title: "Radar"
note_type: "technical-note"
domain: "50_Navegacao_Instrumentacao_e_Comunicacao"
source_file: "RADAR 0f919734f7fb83d4a90e81c518fd4608.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "22"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
normas_citadas:
  - "SOLAS Cap. V, Regra 19 — Carriage requirements (radar obrigatório para embarcações comerciais)"
  - "IMO Resolution MSC.192(79) — Revised performance standards for radar equipment"
  - "IMO Resolution A.823(19) — Performance standards for ARPA (Automatic Radar Plotting Aid)"
  - "IMO Resolution MSC.252(83) — Integrated Navigation System (INS)"
  - "IEC 62388 — Maritime navigation and radiocommunication equipment — Shipborne radar"
  - "IEC 60936-1 / -2 / -3 — Shipborne radar (CAT 1/2/3 ship)"
  - "IEC 60945 — Maritime navigation and radiocommunication equipment — General requirements"
  - "IEC 62388 + IEC 62932 — Radar plotting (ARPA/ATA/EPA funções)"
  - "IEC 61162-1/-2/-3 — NMEA 0183 / NMEA 2000 (heading input, GPS, AIS target overlay)"
  - "ITU-R M.1313 — Technical characteristics of maritime radionavigation radars"
  - "ITU Radio Regulations — banda X (9,3-9,5 GHz) e banda S (2,9-3,1 GHz) para radar marítimo"
  - "ICNIRP 1998/2020 — Guidelines on limiting exposure to RF electromagnetic fields"
  - "FCC 47 CFR Part 80 / Part 87 — Marine radar equipment authorization"
  - "NORMAM-204/DPC — Serviço Móvel Marítimo (autorização de estação para radar)"
  - "NORMAM-201/DPC — Tráfego e Permanência de Embarcações"
  - "NORMAM-211/DPC — Embarcações de esporte e recreio"
  - "Resoluções ANATEL — homologação de radares marítimos"
  - "COLREGs/RIPEAM Rule 5 — Look-out (radar integra o lookout obrigatório)"
  - "COLREGs/RIPEAM Rule 6 — Safe speed (radar deve ser considerado em decisão de velocidade segura)"
  - "COLREGs/RIPEAM Rule 7 — Risk of collision (obrigação de uso adequado do radar)"
  - "ABYC E-11 (2023) — AC and DC Electrical Systems on Boats"
  - "ABYC TE-4 (2021) — Lightning Protection (proteção de mastros com radar)"
  - "ABNT NBR 5410:2004 + emendas — Instalações elétricas de baixa tensão"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://www.nmea.org/standards.html"
  - "https://www.gov.br/anatel/pt-br/regulado/outorga/servico-movel-maritimo"
  - "https://www.itu.int/pub/R-REC"
  - "https://www.icnirp.org/"
aliases:
  - "RADAR"
seo_title: "Radar"
seo_description: "RADAR — Sistema de detecção de alvos por microondas. Detecta embarcações, terra, chuva e obstáculos em qualquer condição de visibilidade. Potência: 2–25 kW (magnetro."
seo_keywords:
  - "Radar"
  - "50 Navegacao Instrumentacao e Comunicacao"
geo_queries:
  - "O que é Radar em instalações elétricas náuticas?"
  - "Qual é a função de Radar na embarcação?"
related_notes:
  - "AIS (Automatic Identification System)"
  - "Buzina"
  - "Bússola Eletrônica (Compass / HDG Sensor)"
  - "Chartplotter / GPS / MFD"
  - "Dsc — Chamada Seletiva Digital"
  - "EPIRB / Beacon de Emergência"
  - "Estação de Vento / Anemômetro"
  - "Mob — Man Overboard — Sistema de Detecção"
---

# Radar

> [!abstract] Resumo técnico
> RADAR — Sistema de detecção de alvos por micro-ondas para apoio à navegação e prevenção de colisão. Detecta ecos de embarcações, terra, chuva e outros alvos conforme instalação, ajuste do operador, estado do mar e capacidade do equipamento. Potência e consumo variam conforme a tecnologia empregada.

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **Magnetron vs Solid State (FMCW/Doppler) é decisão de uso, não de "qualidade"** — magnetron 4-25 kW ainda domina em alcance > 48 mn e offshore; solid state <100 W domina em manobra fechada, detecção Doppler (alvos em movimento destacados em cor) e partida instantânea sem zona cega apreciável.
> 2. **Altura de antena = alcance útil, não potência** — antena a 3 m vê ~8 mn até o horizonte radar; antena a 10 m vê ~15 mn; antena a 20 m vê ~22 mn. Potência nominal do transmissor só importa até o horizonte físico.
> 3. **ARPA/MARPA não é radar comum, é plotter automático de alvos** — ARPA (Automatic Radar Plotting Aid, IMO A.823(19)) é obrigatório SOLAS; MARPA (Mini-ARPA) é simplificado e comum em MFDs recreio. Ambos exigem heading sensor (bússola fluxgate ou girocompass).
> 4. **Heading sensor estável é pré-requisito para qualquer radar overlay** — sem heading sensor (bússola eletrônica ou girocompass), radar funciona em "head-up" mas não consegue overlay na carta nem MARPA; fluxgate compass (compass Airmar H2183, B&G Precision-9) é o mínimo prático.
> 5. **COLREGs Rule 7 é legalmente explícita: "todas as informações disponíveis", radar incluso** — navegar com radar desligado em baixa visibilidade é violação direta. Em pós-sinistro, log de ligado/desligado do radar é requerido em perícia de colisão.
> 6. **Interferência entre radares próximos (anti-collision interference) existe** — dois radares magnetron na mesma embarcação ou em embarcações vizinhas em 9 GHz geram linhas espirais/ruído; solid state sofre menos. Ativar "Interference Rejection" no MFD.
> 7. **Exposição humana a microondas é real mas baixa em uso normal** — ICNIRP 1998 limita exposição contínua a 10 W/m² em 9 GHz; em 1 m da antena magnetron 4 kW durante rotação = <1 W/m². Nunca ficar < 1 m da antena em operação, especialmente em standby/stationary.
> 8. **Radar dome vs open array é decisão de pedestal mais que de performance** — radome 18-24" é padrão recreio (compacto, baixa manutenção); open array 3-6 pés oferece largura de feixe horizontal menor (1-2° vs 4-6°) e maior resolução angular, mas requer pedestal robusto e aumenta consumo.
> 9. **Ethernet proprietário é a norma; integração cross-brand é exceção** — Garmin (GRID/J1939+Ethernet), Raymarine (RayNet), Simrad/Navico (NEP-2 Halo), Furuno (HUB-101): cada fabricante usa seu ecossistema, integração cross-brand via NMEA 2000 traz apenas AIS/heading, não imagem radar.

> [!danger] Quando chamar um especialista (engenheiro naval ou técnico radar com formação em navegação eletrônica)
> 1. **Instalação inicial com alinhamento de heading offset** — radar overlay depende de calibração precisa (± 0,5°) entre norte do radar e norte da bússola/GPS; erros de 2-3° fazem alvos aparecerem fora de lugar na carta; requer bench pattern e referência visual em cais conhecido.
> 2. **Retrofit SOLAS (embarcação > 300 GT ou > 500 GT)** — upgrade para radar IMO performance standard MSC.192(79) + ARPA + integração ECDIS/INS é projeto naval completo com ensaios IACS, homologação DPC e auditoria de sociedade classificadora.
> 3. **Dual radar (curto + longo alcance simultâneos)** — instalação de 2 antenas (uma banda X + uma banda S, ou 2 bandas X com alcances diferentes) requer planejamento RF para evitar interferência mútua, isolamento de antenas (> 3 m físico + blindagem) e licenciamento ANATEL separado.
> 4. **Sinal suspeito de degradação do magnetron (sem "picos" de alcance, zona cega crescente)** — magnetron tem vida útil 2.000-4.000 h; após degradação, substituição requer técnico certificado, alinhamento, verificação de tensão do modulador e teste RF em bancada; tentativa DIY pode resultar em choque elétrico fatal (alta tensão 10-20 kV residual).
> 5. **Integração radar + AIS + câmera térmica (FLIR) + chartplotter em MFD único** — arquitetura Furuno NavNet TZT3 ou Garmin GPSMAP 8600 com múltiplos sensores exige projeto de cabeamento Ethernet protegido, UPS dedicado para preservação de logs e configuração de failover.
> 6. **Perícia pós-colisão envolvendo uso de radar** — laudo envolvendo "o radar detectou/não detectou o alvo X" requer leitura de logs internos (VDR, IEC 61996-1 para Classe A), calibração documentada e análise de interferência; escopo forense, não manutenção.
> 7. **Radar em embarcação com GPS+antena VHF+antena AIS+antena Wi-Fi próximos** — plano RF de mastro/arco com < 1,5 m entre antenas gera interferência cruzada; estudo de compatibilidade eletromagnética (EMC, IEC 60945) é obrigatório em comissionamento de embarcações novas.
> 8. **Ativação do radar em áreas de restrição militar (Fernando de Noronha, Trindade, terminais petrolíferos)** — algumas áreas exigem notificação prévia à Marinha (NORMAM-201) ou desligamento do radar em zonas específicas; documentação operacional obrigatória.
> 9. **Raio e surto em antena no mastro** — radar no topo de mastro de veleiro sem aterramento a TE-4 vira para-raios natural; após tempestade, inspeção e teste completo da eletrônica (magnetron, módulo Ethernet, fonte) antes de nova operação; ABYC TE-4 e análise de continuidade do aterramento são obrigatórios.

> [!info] Glossário rápido (≈ 46 termos)
> - **Radar** — RAdio Detection And Ranging, detecção ativa por micro-ondas.
> - **Banda X (9,3-9,5 GHz)** — padrão marítimo recreio e comercial < 10k GT.
> - **Banda S (2,9-3,1 GHz)** — embarcações oceânicas grandes, penetração em chuva.
> - **Magnetron** — válvula geradora de micro-ondas de alta potência (2-25 kW).
> - **Solid State / FMCW** — Frequency-Modulated Continuous Wave, <100 W, sem magnetron.
> - **Doppler radar** — detecção de velocidade radial (alvos em movimento destacados).
> - **PRF** — Pulse Repetition Frequency, pulsos por segundo.
> - **Pulso curto / longo** — alcance menor com maior resolução / alcance maior com menor resolução.
> - **Largura de feixe horizontal (HBW)** — ângulo; 1-2° para open array, 4-6° para radome.
> - **Rotação** — velocidade de giro, 24-48 RPM.
> - **Zona cega** — distância mínima de detecção; magnetron 50-70 m, FMCW 6-20 m.
> - **Horizonte radar** — distância máxima geométrica (√(2h) em mn; h em m).
> - **ARPA** — Automatic Radar Plotting Aid, IMO A.823(19), SOLAS.
> - **MARPA** — Mini-ARPA, versão recreio simplificada.
> - **ATA/EPA** — Automatic Tracking Aid / Electronic Plotting Aid (variações ARPA).
> - **CPA/TCPA** — Closest Point of Approach / Time to CPA.
> - **Target tracking** — rastreamento automático de alvo.
> - **Clutter** — retorno indesejado de mar, chuva ou terra.
> - **Sea clutter (STC)** — Sensitivity Time Control, atenua retorno de mar próximo.
> - **Rain clutter (FTC)** — Fast Time Constant, atenua retorno de chuva.
> - **Gain** — ganho do receptor, ajuste manual/automático.
> - **Tune** — sintonia fina do receptor (magnetron); automática em FMCW.
> - **Interference Rejection (IR)** — filtro para suprimir radares próximos.
> - **Echo trails** — rastro do alvo em imagens sucessivas.
> - **MARPA guard zone** — zona circular configurável para alarme de alvos.
> - **Head-up / North-up / Course-up** — orientação da imagem.
> - **Relative Motion / True Motion** — alvo move em relação a mim / em relação à terra.
> - **Heading sensor** — sensor de rumo (fluxgate, girocompass, satellite compass).
> - **Heading offset** — correção de alinhamento norte-radar vs norte-bússola.
> - **Open array** — antena em viga horizontal (3-6 pés), maior resolução.
> - **Radome (dome)** — antena em cúpula (18-24"), padrão recreio.
> - **Pedestal** — suporte rotativo motorizado da antena.
> - **Ethernet radar** — protocolo proprietário (GRID, RayNet, NEP-2, HUB-101).
> - **PGN 130842** — NMEA 2000 Radar Data (não é overlay, só status).
> - **X-band weather mode** — modo específico para detecção de células de chuva.
> - **Bird mode** — detecção de aves (usado em pesca esportiva).
> - **Radar overlay** — imagem do radar sobreposta à carta do chartplotter.
> - **VRM/EBL** — Variable Range Marker / Electronic Bearing Line.
> - **AIS overlay** — alvos AIS exibidos sobre imagem radar.
> - **MIC** — Magnetron Interlock (travamento de segurança).
> - **RF exposure limit** — 10 W/m² (ICNIRP 1998, banda X).
> - **Radar reflector** — superfície passiva para ampliar retorno em alvos pequenos (SOLAS).
> - **SART (radar)** — Search and Rescue Transponder (legado, substituído por AIS-SART).
> - **Racon** — radar beacon em sinalizações náuticas (boias, faróis).
> - **Lookout (COLREGs Rule 5)** — vigilância por todos os meios, incluindo radar.
> - **Safe speed (Rule 6)** — velocidade segura, radar é fator determinante.

## O que é

O radar naval é um sistema de detecção ativa que emite energia eletromagnética e analisa os ecos refletidos pelos objetos ao redor da embarcação. Não depende de luz ambiente, o que o torna valioso em nevoeiro, chuva, escuridão e visibilidade degradada. Ainda assim, seu desempenho real depende de instalação, regulagem, treinamento do operador, altura da antena, tipo de alvo e condições meteorológicas.

## Função na embarcação

- Detectar embarcações, terra, ilhas, boias e obstáculos ao redor
- Apoiar a navegação em condições de visibilidade severamente degradada, sem substituir vigia, carta, AIS e julgamento do navegador
- Identificar células de chuva para desvio de tempestades
- Complementar o AIS (detecta alvos sem transponder)
- Medir distância e direção de alvos com precisão

## Como aparece na prática

**Comum em barcos importados:**

- Radar de 4 kW com antena de 18" em veleiros de cruzeiro (> 40 pés)
- Integrado ao MFD Garmin/Simrad com overlay na carta
- Antena montada no topo do mastro (veleiro) ou no fly bridge (lancha)

**Mais presente em embarcações maiores/premium:**

- Radar solid state (Broadband/FMCW) de menor potência mas maior resolução
- Dual radar (2 antenas) em iates de grande porte para cobertura total
- Furuno DRS4D-NXT ou Garmin GMR Fantom para desempenho premium

**No Brasil:**

- Radar ainda é item raro em lanchas de recreio nacionais < 40 pés
- Cresce em veleiros de cruzeiro oceânico e embarcações de trabalho
- Presente em embarcações de pesca esportiva de médio e grande porte

## Fundamentos mínimos

**Princípio:** O radar emite pulsos de microondas em rotação (360°). Quando o pulso encontra um objeto, parte da energia é refletida de volta. O radar mede o tempo do eco (distância) e o ângulo da antena (direção) para plotar o alvo no display.

**Magnetron vs. Solid State (FMCW):**

- **Magnetron:** Emite pulsos de alta potência. Costuma oferecer bom desempenho em alcance, mas requer aquecimento e normalmente apresenta limitação maior em curtas distâncias, dependendo do modelo e da instalação.
- **Solid State (Broadband/FMCW):** Opera com eletrônica de estado sólido e tende a oferecer melhor resposta em curtas distâncias, partida imediata e recursos avançados de processamento. Os resultados práticos variam conforme o fabricante, a antena e o processamento embarcado.

**Alcance:** Determinado principalmente pela altura da antena, altura do alvo, horizonte radar, sensibilidade do receptor, processamento, estado do mar e potência efetiva do conjunto. Cálculos geométricos dão referência, mas não substituem ensaio real nem garantem detecção útil de todos os alvos.

**Zona cega:** Todo radar tem limitações em curta distância, embora alguns sistemas solid state reduzam significativamente esse problema. Os valores reais dependem do modelo, largura de pulso, processamento e geometria de instalação.

## Características principais

| Parâmetro | Magnetron 4kW | Solid State (Broadband) |
| --- | --- | --- |
| Potência de emissão | 4 kW | < 100W |
| Alcance máximo | 24–48 mn | 24 mn |
| Zona cega | 50–70m | 6–20m |
| Aquecimento | 30–90 segundos | Instantâneo |
| Corrente em 12V | 4–8A | 2–4A |
| Frequência | 9 GHz (X-band) | 9 GHz (X-band) |
| Detecção de chuva | Boa | Excelente (doppler em alguns) |

## Configurações e variações comuns

**Radar de 18" com magnetron 4kW (mais comum)**

- Boa relação custo/desempenho
- Alcance 24–48 mn (dependendo da posição)
- Garmin GMR 18HD+, Simrad BR24

**Radar solid state (Garmin GMR Fantom, Navico Halo)**

- Sem zona cega, liga imediatamente
- Melhor para manobra e cais em baixa visibilidade
- Custo mais alto
- Garmin GMR Fantom 18, Navico Halo 20

**Radar de pedestal (open array)**

- Antena direcional maior (3–6 pés)
- Maior precisão e resolução
- Comum em iates e embarcações profissionais
- Mais caro, requer estrutura de suporte

**Dual radar**

- Dois radares simultâneos (curto + longo alcance, ou dois ângulos)
- Para iates de grande porte
- Furuno e Garmin oferecem suporte dual radar

## Principais marcas

- **Garmin** — GMR e GMR Fantom, boa integração com GPSMAP, disponível no Brasil
- **Furuno** — referência profissional, alta qualidade, presença em embarcações de trabalho
- **Simrad** — forte em veleiros e embarcações profissionais
- **Raymarine** — Quantum radar solid state, integração Lighthouse
- **Navico/B&G** — Halo radar solid state, especialidade em veleiros

## Componentes e sistemas relacionados

- **MFD/chartplotter** — display e controle do radar
- **Cabo Ethernet** — conexão radar → MFD (maioria dos modelos atuais)
- **Suporte de antena** — no fly bridge, T-top, mastro ou arco de popa
- **AIS** — complemento: radar detecta sem transponder; AIS identifica com transponder
- **NMEA 2000** — alguns dados de radar compartilhados na rede
- **Câmera** — integração no MFD para visão real do alvo identificado pelo radar

## Onde costuma dar problema

| Problema | Sintoma | Causa |
| --- | --- | --- |
| Sem imagem no MFD | Display mostra "sem radar" | Ethernet com falha, antena sem alimentação |
| Imagem granulada/ruidosa | Muitos pontos falsos (clutter) | Ganho muito alto, ganho de mar ou chuva não ajustado |
| Zona morta grande | Alvos próximos invisíveis | Magnetron com potência reduzida (desgaste) |
| Travamento da antena | Para de girar | Motor de giro com defeito, conector oxidado |
| Imagem distorcida | Elipse em vez de círculo | Antena sem nível, instalação inclinada |

## Causas raiz

**Sem imagem:**

- Cabo Ethernet danificado ou com conector oxidado
- Falha de alimentação na antena (verificar fusível e tensão no conector da antena)
- Magnetron desgastado após 2.000–3.000 horas de operação

**Antena parada:**

- Motor de giro queimado (mecanismo interno)
- Conector de alimentação oxidado
- Objeto físico bloqueando a rotação

**Causa raiz de degradação:** Sistemas com magnetron têm componente emissor sujeito a desgaste e perda de desempenho ao longo da vida útil. Em radares solid state esse ponto específico muda, mas continuam existindo riscos de falha em fonte, motor, radome, conectores e eletrônica associada.

## Diagnóstico prático

**Passo 1:** Sem imagem → verificar alimentação no conector da antena (tensão e corrente).

**Passo 2:** Alimentação ok, sem imagem → verificar cabo Ethernet (testar com cabo de substituição).

**Passo 3:** Imagem com muito clutter → ajustar controles de ganho, clutter de mar e clutter de chuva.

**Passo 4:** Antena não gira → verificar corrente de alimentação (motor de giro consome ~1A adicional). Motor parado = sem rotação = sem varredura.

## Boas práticas

- Instalar a antena no ponto mais alto para maximizar o alcance
- Manter distância mínima de 1,5–2m de outras antenas (VHF, GPS)
- Não ficar na linha de visada do feixe de radar em operação (exposição à microondas)
- Calibrar o ajuste de norte (heading offset) após instalação
- Em radares com magnetron: acompanhar horas de operação, sintomas de degradação e critérios do fabricante para manutenção ou substituição

## Erros comuns

❌ **Antena próxima ao GPS** — interferência no receptor GPS

❌ **Ganho máximo sempre** — clutter excessivo que mascara alvos reais

❌ **Nunca ajustar clutter de mar** — falsos alvos que confundem o operador

❌ **Ficar na linha da antena girando** — exposição desnecessária à radiação de microondas

❌ **Cabo de alimentação subdimensionado** — queda de tensão, magnetron não atinge potência nominal

## Relação com outros sistemas

- **Chartplotter/MFD** — display e integração (radar overlay na carta)
- **AIS** — complementar: radar vê tudo, AIS identifica
- **NMEA 2000** — heading sensor envia rumo para o radar (norte referenciado)
- **Piloto automático** — em sistemas avançados, integração para ARPA (Automatic Radar Plotting Aid)
- **VHF** — identificação de alvos por comunicação

## Brasil x referências internacionais

### Prática comum no Brasil

Radar raro em embarcações de recreio nacionais. Quando há, frequentemente sem operador treinado para interpretar a imagem.

### Referência internacional

Radar é considerado equipamento essencial em qualquer embarcação que navegue à noite ou em condições de baixa visibilidade. Treinamento de operação é requisito.

### Leitura equilibrada

Para embarcações que navegam exclusivamente de dia em costas conhecidas: radar é opcional mas desejável. Para navegação noturna, cruzeiros offshore ou qualquer navegação em condições de baixa visibilidade: o radar é equipamento de segurança crítico.

## Normas e referências aplicáveis

- **SOLAS Cap. V, Regra 19** — Carriage requirements for shipborne navigational systems: radar obrigatório em embarcações comerciais (> 300 GT em viagens internacionais; > 500 GT em geral) e em passenger ships.
- **IMO Resolution MSC.192(79)** — Revised performance standards for radar equipment (define padrões de desempenho para SOLAS).
- **IMO Resolution A.823(19)** — Performance standards for ARPA (Automatic Radar Plotting Aid).
- **IMO Resolution MSC.252(83)** — Integrated Navigation System (INS) (radar como sensor de INS).
- **IEC 62388** — Maritime navigation and radiocommunication equipment — Shipborne radar — Operational and performance requirements (documento técnico-raiz para ensaio e homologação).
- **IEC 60936-1 / -2 / -3** — Shipborne radar equipment for CAT 1/2/3 ships (classificação por porte).
- **IEC 60945** — Maritime navigation and radiocommunication equipment — General requirements (EMC, IP, vibração, temperatura).
- **IEC 62388 + IEC 62932** — Radar plotting functions (ARPA/ATA/EPA).
- **IEC 61162-1 / -2 / -3 (NMEA 0183 / NMEA 2000)** — interfaces digitais (heading input HDG/HDT, GPS RMC/GGA, AIS target overlay).
- **ITU-R M.1313** — Technical characteristics of maritime radionavigation radars (parâmetros eletromagnéticos).
- **ITU Radio Regulations** — alocação de banda X (9,3-9,5 GHz) e banda S (2,9-3,1 GHz) para radar marítimo.
- **ICNIRP 1998 / 2020** — Guidelines on limiting exposure to time-varying electric, magnetic and electromagnetic fields (limite 10 W/m² em 9 GHz para exposição contínua).
- **FCC 47 CFR Part 80 / Part 87** — Marine radar equipment authorization (referência para radares americanos importados).
- **NORMAM-204/DPC** — Serviço Móvel Marítimo (autorização de estação para radar em embarcações brasileiras).
- **NORMAM-201/DPC** — Tráfego e Permanência de Embarcações (aplicabilidade a embarcações comerciais).
- **NORMAM-211/DPC** — Embarcações de esporte e recreio (radar opcional em recreio; recomendado offshore).
- **Resoluções ANATEL** — homologação de radares marítimos (emissor em 9 GHz requer certificação).
- **COLREGs/RIPEAM Rule 5** — Look-out (vigilância por TODOS os meios; radar é um deles quando disponível).
- **COLREGs/RIPEAM Rule 6** — Safe speed (velocidade segura deve considerar capacidade do radar, clutter, estado do mar).
- **COLREGs/RIPEAM Rule 7** — Risk of collision (uso correto do radar + observação sistemática de alvos).
- **ABYC E-11 (2023)** — AC and DC Electrical Systems on Boats (fiação, fusíveis e proteção DC do radar).
- **ABYC TE-4 (2021)** — Lightning Protection (proteção de mastros e antenas contra descargas atmosféricas).
- **ABNT NBR 5410:2004 + emendas** — Instalações elétricas de baixa tensão (aplicável a partes AC do sistema).

## Destaques para ensino

- Magnetron vs. solid state: quando cada tecnologia faz sentido
- Zona cega: o risco crítico do magnetron próximo ao cais
- Interpretação da imagem de radar: o que é alvo real, o que é clutter
- Integração radar + carta: o overlay que une os dois mundos
- AIS como complemento — por que não substitui o radar

## FAQ

**O radar substitui o AIS?**

Não. Radar detecta fisicamente todos os alvos (com ou sem transponder). AIS identifica embarcações com transponder ativo (nome, rumo, velocidade, MMSI). São sistemas complementares.

**Solid state vale o custo extra?**

Para embarcações que manobram em marinas e cais em baixa visibilidade: sim — a ausência de zona cega é valiosa. Para navegação oceânica: o magnetron com maior alcance pode ser melhor.

**Posso usar radar e VHF com antenas próximas?**

Manter pelo menos 1,5–2m de separação. Radar pode causar interferência na recepção VHF se as antenas estiverem muito próximas.

**Quanto tempo o magnetron dura?**

A vida útil do magnetron varia com fabricante, ciclo térmico, ambiente de operação e regime de uso. O ponto correto não é memorizar um número único, mas acompanhar sintomas de perda de desempenho, horas de operação e recomendações de manutenção do fabricante.

## Integração com outras notas

- [[AIS (Automatic Identification System)]]
- [[Buzina]]
- [[Bússola Eletrônica (Compass / HDG Sensor)]]
- [[Chartplotter / GPS / MFD]]
- [[Dsc — Chamada Seletiva Digital]]
- [[EPIRB / Beacon de Emergência]]
- [[Estação de Vento / Anemômetro]]
- [[Mob — Man Overboard — Sistema de Detecção]]

## Perguntas que esta nota responde

- O que é Radar em instalações elétricas náuticas?
- Qual é a função de Radar na embarcação?
