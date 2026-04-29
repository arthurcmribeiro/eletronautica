---
title: "AIS (Automatic Identification System)"
note_type: "technical-note"
domain: "50_Navegacao_Instrumentacao_e_Comunicacao"
source_file: "AIS (Automatic Identification System) 33a19734f7fb81b4b75ffe1f6db19c78.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "21"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
normas_citadas:
  - "SOLAS Cap. V, Regra 19 — Carriage requirements for shipborne navigational systems (AIS obrigatório)"
  - "IMO Resolution A.1106(29) — Revised guidelines for onboard operational use of shipborne AIS"
  - "IMO Resolution MSC.74(69) — Performance standards for AIS (base técnica)"
  - "ITU-R M.1371 — Technical characteristics for AIS using TDMA in the VHF maritime mobile band"
  - "ITU-R M.2092 — Technical characteristics for a VHF data exchange system (VDES) in the maritime mobile band"
  - "ITU Radio Regulations — Apêndice 18 (canais AIS-1 161,975 MHz e AIS-2 162,025 MHz)"
  - "IEC 61993-2 — AIS — Class A shipborne equipment"
  - "IEC 62287-1 — AIS Class B CSTDMA equipment"
  - "IEC 62287-2 — AIS Class B SOTDMA equipment"
  - "IEC 60945 — Maritime navigation and radiocommunication equipment — General requirements"
  - "IEC 61162-1/-2 (NMEA 0183) — Digital interfaces"
  - "IEC 61162-3 (NMEA 2000) — Network-based digital interface"
  - "IALA Guideline G-1028 — Operational use of AIS"
  - "IALA A-126 — Use of AIS in marine aids to navigation"
  - "RIPEAM/COLREGs Rule 5 — Look-out (AIS integra o lookout eletrônico)"
  - "NORMAM-204/DPC — Serviço Móvel Marítimo"
  - "NORMAM-201/DPC — Tráfego e Permanência de Embarcações"
  - "NORMAM-211/DPC — Embarcações de esporte e recreio"
  - "Resoluções ANATEL aplicáveis — homologação de AIS e alocação de MMSI"
  - "ABYC E-11 (2023) — AC and DC Electrical Systems on Boats"
  - "ABNT NBR 5410:2004 + emendas — Instalações elétricas de baixa tensão"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://www.nmea.org/standards.html"
  - "https://www.gov.br/anatel/pt-br/regulado/outorga/servico-movel-maritimo"
  - "https://www.itu.int/pub/R-REC"
  - "https://www.iala-aism.org/"
aliases:
  - "AIS (Automatic Identification System)"
seo_title: "AIS (Automatic Identification System)"
seo_description: "AIS — AUTOMATIC IDENTIFICATION SYSTEM — Sistema de identificação automática que transmite e recebe dados de embarcações (nome, posição, velocidade, rumo, MMSI) via V."
seo_keywords:
  - "AIS"
  - "Automatic"
  - "Identification"
  - "System"
  - "50 Navegacao Instrumentacao e Comunicacao"
geo_queries:
  - "O que é AIS (Automatic Identification System) em instalações elétricas náuticas?"
  - "Qual é a função de AIS (Automatic Identification System) na embarcação?"
related_notes:
  - "Buzina"
  - "Bússola Eletrônica (Compass / HDG Sensor)"
  - "Chartplotter / GPS / MFD"
  - "Dsc — Chamada Seletiva Digital"
  - "EPIRB / Beacon de Emergência"
  - "Estação de Vento / Anemômetro"
  - "Mob — Man Overboard — Sistema de Detecção"
  - "NAVEGAÇÃO (BB, BE e Alcançado)"
---

# AIS (Automatic Identification System)

> [!abstract] Resumo técnico
> AIS — AUTOMATIC IDENTIFICATION SYSTEM — Sistema de identificação automática que transmite e recebe dados de embarcações (nome, posição, velocidade, rumo, MMSI) via VHF digital. Classe A (obrigatório para embarcações comerciais) ou Classe B.

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **Classe A vs Classe B não é questão de "qualidade", é de protocolo** — Classe A (SOTDMA, 12,5 W, atualização 2-10 s) é obrigatório SOLAS para embarcações comerciais > 300 GT; Classe B CSTDMA (2 W, 30 s parado, escuta antes de transmitir) é padrão recreio; Classe B SOTDMA (5 W, 5-30 s, prioridade de slot) é o "upgrade" recreio para áreas densas.
> 2. **MMSI não é opcional e não é genérico** — transponder sem MMSI oficial registrado é juridicamente invisível (NORMAM-204/ITU MARS); programar 0000000, 1234567 ou copiar de outra embarcação é infração regulatória e pode impedir SAR de identificar o alvo.
> 3. **Recepção não é transmissão** — receptor AIS (RX-only) embutido em chartplotters NÃO torna você visível para outros; você vê, mas não é visto. Para ser visto por SAR, tráfego comercial e plataformas públicas, obrigatoriamente transponder.
> 4. **CPA/TCPA é a única função "útil" do AIS em tempo real** — configurar CPA ≤ 0,5 mn e TCPA ≤ 10-15 min como alarme audível. Sem alarme configurado, o AIS vira enfeite no chartplotter.
> 5. **AIS não substitui radar, substitui rádio binocular** — AIS só detecta alvos com transponder ligado; veleiros pequenos, jangadas, pesqueiros artesanais, obstáculos físicos e balsas sem AIS são invisíveis. Radar + AIS + lookout visual (COLREGs Regra 5) são camadas complementares.
> 6. **Antena compartilhada via splitter ativo é a norma recreio** — splitter passivo barato atenua 3-6 dB (perde metade do alcance); splitter ativo tipo Vesper/Digital Yacht mantém <1 dB de perda e prioriza VHF em TX. Antena dedicada AIS é preferível em embarcações > 15 m.
> 7. **Alcance AIS é linha de visada VHF** — antena a 3 m = ~20 mn; antena a 15 m = ~40 mn; navios comerciais com antena a 30 m transmitindo 12,5 W = visíveis a 60+ mn. Planejar a partir da altura real da antena, não de especificações fabricante.
> 8. **GPS sem fix = AIS sem transmissão** — Classe B exige posição válida para transmitir. GPS integrado (AIS com GNSS interno) é o padrão moderno; alternativamente, feed de GPS externo via NMEA 0183/2000 estável.
> 9. **NMEA 2000 é backbone preferido para AIS** — PGN 129038 (Class A position), 129039 (Class B position), 129794 (static data), 129808 (DSC data). NMEA 0183 (AIVDM/AIVDO, 38400 baud) ainda funciona, mas exige fiação dedicada em 38400 (não 4800).

> [!danger] Quando chamar um especialista (engenheiro ou técnico com formação em navegação eletrônica)
> 1. **MMSI programado com erro (típico de equipamento segunda mão)** — Classe B permite 1 reprogramação em fábrica (ou DESN na Vesper); outros modelos exigem devolução ao fabricante. Antes de comprar AIS usado, confirmar com o vendedor o MMSI atual.
> 2. **Upgrade SOLAS (> 300 GT ou > 500 GT)** — transição de Classe B para Classe A envolve homologação IEC 61993-2, Pilot Port, conexão ECDIS, verificação IMO e certificação de estação pela ANATEL; escopo de projeto naval/eletrônico, não retrofit DIY.
> 3. **Splitter de antena com atenuação suspeita** — se alcance AIS caiu para < 8 mn com antena > 5 m de altura, splitter passivo ou cabo coaxial de baixa qualidade (RG-58 em lances > 10 m) tipicamente degradou o sinal; medição com analisador de espectro e VSWR obrigatória antes de trocar peças.
> 4. **Transmissor AIS "cegando" o próprio receptor VHF** — sintoma: VHF fica mudo enquanto AIS transmite slot (2-10 s). Causa: antena compartilhada sem splitter ou splitter passivo inadequado; requer reengenharia do plano RF de bordo.
> 5. **Dark/silent mode intencional em áreas de pirataria** — em regiões MSCHOA/NATO (Golfo de Áden, Estreito de Malaca, partes do Caribe), desligar AIS é prática recomendada por SOLAS Reg 19 mas exige documentação e permissão do comandante; decisão jurídica, não técnica.
> 6. **Perícia sinistro com uso de AIS histórico** — dados de MarineTraffic/VesselFinder/AIS Hub têm latência, cobertura intermitente e gaps; prova judicial requer AIS recorder homologado (IEC 61993-2 SOLAS) ou dados oficiais MRCC, não captura de tela de plataforma pública.
> 7. **Importação sem homologação ANATEL** — AIS Classe B SOTDMA importado direto dos EUA (FCC) frequentemente opera em 161,975/162,025 MHz mas sem homologação brasileira; operar é infração ANATEL e pode ser motivo de apreensão pela Marinha em inspeção.
> 8. **Integração multi-chartplotter com alertas CPA duplicados** — em instalações com Garmin + B&G + Simrad no mesmo backbone NMEA 2000, alertas CPA podem ser emitidos simultaneamente por vários MFDs; planejamento de qual unidade é "master" para alarme é decisão de projeto.
> 9. **Frota comercial com AIS Classe A + AIS-SART + VDR** — Classe A integrado a Voyage Data Recorder (VDR, IMO SOLAS) e AIS-SART (IEC 61097-14) para dispositivos de emergência requer comissionamento por empresa homologada, auditoria DPC/ANATEL e treinamento GOC (General Operator Certificate) da tripulação.

> [!info] Glossário rápido (≈ 45 termos)
> - **AIS** — Automatic Identification System, IMO SOLAS Cap V Reg 19 + ITU-R M.1371.
> - **Classe A** — transponder obrigatório SOLAS, SOTDMA, 12,5 W, atualização 2-10 s, mensagens 1/2/3/5.
> - **Classe B CSTDMA** — recreio simplificado, 2 W, 30 s parado, escuta canal antes de transmitir.
> - **Classe B SOTDMA** — recreio premium, 5 W, slot reservado, 5-30 s, prioridade maior na rede.
> - **AIS RX-only** — receptor passivo, não transmite, comum em chartplotters modernos.
> - **AIS-SART** — Search and Rescue Transmitter baseado em AIS (IEC 61097-14), substituto do SART radar.
> - **MOB-AIS** — dispositivo pessoal AIS para Homem ao Mar, transmite em 161,975 MHz.
> - **VDES** — VHF Data Exchange System, ITU-R M.2092, evolução futura do AIS.
> - **SOTDMA** — Self-Organized TDMA, protocolo Classe A e Classe B premium, slots auto-organizados.
> - **CSTDMA** — Carrier Sense TDMA, protocolo Classe B simples, escuta antes de transmitir.
> - **ITDMA** — Incremental TDMA, variante usada para alocação de slot inicial.
> - **Slot** — intervalo de tempo de 26,67 ms; 2250 slots por minuto por canal.
> - **Frame** — sequência de 2250 slots = 1 min no canal AIS.
> - **AIS-1 / AIS-2** — canais 161,975 MHz (87B) e 162,025 MHz (88B); operação bi-canal.
> - **Apêndice 18 (ITU RR)** — alocação das frequências marítimas VHF, inclui AIS-1/AIS-2.
> - **MMSI** — Maritime Mobile Service Identity, 9 dígitos, Brasil MID 710-719.
> - **MID** — Maritime Identification Digits, prefixo do país no MMSI.
> - **ITU MARS** — Maritime mobile Access and Retrieval System, banco mundial de MMSIs.
> - **Static data** — nome, MMSI, IMO, call sign, tipo, dimensões (mensagem 5 Classe A).
> - **Dynamic data** — posição, SOG, COG, HDG, ROT, status nav (mensagens 1/2/3).
> - **Voyage data** — destino, ETA, draft, tipo de carga (mensagem 5 Classe A).
> - **ROT** — Rate of Turn, grau/min, sensor ROT dedicado para Classe A.
> - **SOG/COG** — Speed Over Ground / Course Over Ground (do GPS).
> - **HDG** — Heading (True), bússola/girocompass, não COG.
> - **CPA** — Closest Point of Approach, distância mínima de aproximação prevista.
> - **TCPA** — Time to CPA, minutos até o ponto de maior aproximação.
> - **BCPA** — Bow CPA, variante considerando a proa da embarcação.
> - **AIS Target** — alvo AIS no chartplotter; ícone triangular.
> - **Ghost target** — alvo duplicado/fantasma por reflexão VHF ou multi-path.
> - **Antenna Splitter** — dispositivo que compartilha antena VHF entre VHF e AIS.
> - **Splitter ativo** — amplifica/reduz perda (<1 dB), prioriza VHF em TX.
> - **Splitter passivo** — divisor resistivo, atenua 3-6 dB, uso em embarcações pequenas.
> - **PGN 129038** — NMEA 2000 Class A Position Report.
> - **PGN 129039** — NMEA 2000 Class B Position Report.
> - **PGN 129794** — NMEA 2000 AIS Voyage Static Data.
> - **AIVDM** — sentença NMEA 0183 recebida de outra estação.
> - **AIVDO** — sentença NMEA 0183 transmitida pela própria estação.
> - **BIIT** — Built-In Integrity Test, autoteste contínuo (IEC 61993-2).
> - **Silent mode / dark** — AIS desligado (autorizado somente em áreas SOLAS Reg 19).
> - **IALA G-1028** — Guideline operacional do AIS (boas práticas).
> - **IALA A-126** — uso de AIS em sinalização náutica (AtoN).
> - **AIS AtoN** — estação AIS virtual/sintética em boia, farol ou ponto fixo.
> - **Base station** — estação costeira AIS operada por autoridade marítima.
> - **MarineTraffic / VesselFinder** — plataformas públicas de visualização (não oficiais).
> - **Lookout (COLREGs Rule 5)** — obrigação legal de vigilância por todos os meios, incluindo AIS.

## O que é

O AIS (Automatic Identification System) é um sistema de transmissão e recepção de dados via rádio VHF digital (161,975 MHz e 162,025 MHz) que permite que embarcações e estações costeiras se "vejam" em tempo real com informações detalhadas: posição, velocidade, rumo, nome, MMSI, dimensões e tipo de embarcação.

Funciona como um "radar cooperativo" — mas só identifica embarcações que também têm AIS ativo. Complementa, não substitui, o radar.

## Função na embarcação

- Receber dados de identificação de outras embarcações ao redor
- Transmitir os dados da própria embarcação para outros (Classe B)
- Exibir alvos AIS sobrepostos na carta do chartplotter
- Receber alertas de embarcações em rota de colisão (CPA/TCPA)
- Identificar embarcações de tráfego sem contato por rádio
- Aumentar a visibilidade eletrônica da embarcação e facilitar a identificação por terceiros em cenários de tráfego e coordenação

## Como aparece na prática

**Muito comum no Brasil:**

- Receptor AIS simples (somente RX) integrado a chartplotters mais novos
- Transponder Classe B em veleiros de cruzeiro e lanchas de maior porte
- Alvos AIS exibidos no MFD Garmin/Simrad

**Comum em barcos importados:**

- Transponder Classe B SOTDMA (Standard Horizon, Vesper, Em-Trak) integrado ao VHF
- Alerta de CPA (Closest Point of Approach) configurado no chartplotter
- Integração total via NMEA 2000

**Mais presente em embarcações maiores/premium:**

- AIS Classe B SOTDMA de alta atualização (5 segundos em velocidade alta)
- AIS integrado ao VHF (Standard Horizon GX2400, Icom IC-M510)
- Monitoramento remoto via AIS web (MarineTraffic, VesselFinder)

## Fundamentos mínimos

**Classe A vs. Classe B:**

- **Classe A:** Obrigatório para embarcações comerciais (navios > 300 GT, ferry boats, etc.). Alta taxa de atualização (2–10 segundos). Transmite dados estendidos.
- **Classe B:** Para recreio e pequenas embarcações. Taxa menor (30 segundos parado, 5–30 segundos em movimento). Dois subtipos: CSTDMA (mais simples) e SOTDMA (maior prioridade na rede, melhor para áreas densas).
- **Receptor simples (AIS RX):** Somente recebe — não transmite. Incluso em muitos chartplotters. Útil para tráfego mas não transmite a própria posição.

**CPA/TCPA:** Closest Point of Approach / Time to CPA. O chartplotter calcula o ponto de maior aproximação entre a própria embarcação e um alvo AIS, e o tempo para chegar lá. Alertas configuráveis: ex., CPA < 0,5 mn em < 10 minutos = alarme.

**Alcance:** Linha de visada VHF. Antena a 3m: ~20 mn de alcance AIS. Antena no mastro a 15m: ~40 mn.

**MMSI:** Em embarcações recreativas e comerciais usuais, o transponder AIS utiliza a identidade MMSI oficial da estação/embarcação, em coerência com o ecossistema DSC/VHF. O número deve ser oficial e corretamente registrado; não se deve programar identificadores de teste ou improvisados.

## Características principais

| Parâmetro | Receptor AIS (RX only) | Transponder Classe B |
| --- | --- | --- |
| Transmissão | Não | Sim (2W) |
| Taxa de atualização | Recepção contínua | 30s parado / 5–30s em mov. |
| Corrente | 0,1–0,5A | 0,5–2A |
| Antena | Compartilhada com VHF ou dedicada | Compartilhada com VHF ou dedicada |
| MMSI necessário | Não para RX | Sim, obrigatório |
| Visível para outros | Não | Sim |

## Configurações e variações comuns

**Receptor AIS integrado ao chartplotter (mais comum)**

- Muitos chartplotters Garmin, Simrad, Raymarine incluem receptor AIS interno
- Recebe alvos mas não transmite a própria posição
- Antena VHF compartilhada via splitter de antena

**Transponder Classe B standalone**

- Caixa dedicada com antena VHF própria ou compartilhada
- Vesper Marine XB-8000, Em-Trak B954, SRT MX510
- Integra via NMEA 0183 ou NMEA 2000 ao chartplotter

**VHF com AIS integrado**

- Standard Horizon GX2400, Icom IC-M510
- Um dispositivo faz VHF + AIS + DSC
- Solução compacta e integrada

**Splitter de antena VHF**

- Permite compartilhar a antena VHF entre o VHF e o AIS
- Evita segunda antena
- Pequena perda de sinal (~1dB) — aceitável

## Principais marcas

- **Vesper Marine** — referência em AIS para recreio, excelente APP (WatchMate)
- **Standard Horizon** — AIS integrado ao VHF (GX2400)
- **Em-Trak** — qualidade europeia, boa reputação
- **SRT Marine** — sistemas OEM para vários fabricantes
- **Garmin** — receptor AIS integrado nos chartplotters GPSMAP 8400+
- **Digital Yacht** — linha completa de AIS para veleiros

## Componentes e sistemas relacionados

- **Antena VHF** — compartilhada ou dedicada para AIS
- **Splitter de antena** — quando antena compartilhada
- **NMEA 2000 ou NMEA 0183** — integração com chartplotter
- **Chartplotter/MFD** — display dos alvos AIS
- **GPS** — posição para transmissão do transponder
- **VHF** — rádio complementar (comunicação) ao AIS (identificação)
- **MMSI** — número de registro obrigatório

## Onde costuma dar problema

| Problema | Sintoma | Causa |
| --- | --- | --- |
| Sem alvos no chartplotter | AIS ativo mas sem embarcações visíveis | NMEA não conectado, antena sem sinal |
| Própria embarcação não aparece para outros | Transponder ativo mas sem transmissão | MMSI errado, GPS sem fix, antena ruim |
| Alcance muito curto | Alvos visíveis apenas a 5–8 mn | Antena compartilhada mal configurada, splitter de baixa qualidade |
| Alarme CPA constante | Alertas falsos frequentes | Parâmetros CPA/TCPA muito sensíveis |
| Dados incorretos de outros navios | Dados erráticos | Mensagem AIS Classe A corrompida por múltiplos transmissores simultâneos |

## Causas raiz

**Sem alvos no chartplotter:**

- NMEA 0183 sem conexão (verificar pinos TX/RX entre AIS e chartplotter)
- Antena VHF com conector oxidado (afeta tanto VHF quanto AIS)

**Transponder não visível:**

- MMSI não programado ou programado incorretamente
- GPS sem fix — AIS não transmite sem posição
- Antena de baixa qualidade ou splitter com atenuação excessiva

## Diagnóstico prático

**Passo 1:** Sem alvos → verificar se a antena tem sinal (testar VHF — se VHF funciona, antena está ok).

**Passo 2:** Verificar integração NMEA: no chartplotter, confirmar se há dados de AIS (Settings → System → Communication).

**Passo 3:** Transponder não transmite → verificar se GPS tem fix e se MMSI está programado corretamente no transponder.

**Passo 4:** Plataformas públicas como [MarineTraffic](http://MarineTraffic.com) ou equivalentes podem servir como verificação complementar, mas não constituem prova definitiva de funcionamento contínuo, já que dependem de cobertura costeira, estações receptoras de terceiros e latência da rede.

## Boas práticas

- Programar MMSI oficial registrado — nunca MMSI de teste (0000000 ou 1234567)
- Conectar GPS ao transponder (para posição precisa na transmissão)
- Integrar ao chartplotter via NMEA 2000 para melhor visualização
- Configurar alertas CPA/TCPA em valores razoáveis (CPA < 0,5 mn, TCPA < 15 min)
- Usar plataformas públicas apenas como confirmação complementar; a validação principal deve considerar autoteste do equipamento, integração local e verificação por outra estação quando possível
- Manter antena VHF em bom estado — afeta diretamente o AIS

## Erros comuns

❌ **MMSI de teste programado** — embarcação não identificável oficialmente

❌ **Receptor AIS apenas (sem transponder)** — embarcação invisível para outros

❌ **Sem GPS conectado ao transponder** — transmite posição errada ou sem posição

❌ **Confiar somente no AIS para navegação** — embarcações sem AIS (veleiros pequenos, barcos locais, pesqueiros) são invisíveis no AIS

❌ **Alertas CPA desativados** — perde a função de prevenção de colisão

## Relação com outros sistemas

- **VHF** — usa a mesma frequência e antena; comunicação complementar à identificação
- **Chartplotter/MFD** — display dos alvos AIS na carta
- **Radar** — complementar: radar detecta sem transponder; AIS identifica com transponder
- **NMEA 2000** — backbone de integração
- **GPS** — posição para transmissão do próprio AIS
- **DSC** — compartilha a lógica de identidade marítima digital e complementa o AIS em comunicação de emergência e chamada seletiva

## Brasil x referências internacionais

### Prática comum no Brasil

Receptor AIS embutido no chartplotter sem transponder. Quando há transponder: frequentemente sem MMSI registrado.

### Referência internacional

Transponder Classe B SOTDMA como padrão em qualquer veleiro ou iate de recreio que navegue em áreas com tráfego comercial. MMSI obrigatório e registrado.

### Ponto de conflito

No Brasil, a obrigatoriedade de AIS para embarcações de recreio não é clara na NORMAM — mas a presença de tráfego comercial em costas como Santos, Sepetiba e demais portos torna o AIS equipamento de segurança crítico mesmo sem obrigação legal explícita.

## Normas e referências aplicáveis

- **SOLAS Cap. V, Regra 19** — Carriage requirements for shipborne navigational systems (AIS obrigatório navios > 300 GT em viagens internacionais e > 500 GT em geral; passenger ships independente de tonelagem).
- **IMO Resolution A.1106(29)** — Revised guidelines for onboard operational use of shipborne AIS (uso operacional).
- **IMO Resolution MSC.74(69), Anexo 3** — Performance standards for AIS (requisitos mínimos de desempenho para equipamentos Classe A).
- **ITU-R M.1371** — Technical characteristics for an AIS using time division multiple access in the VHF maritime mobile band (documento-raiz técnico do AIS; slot, SOTDMA/CSTDMA, mensagens 1-27).
- **ITU-R M.2092** — Technical characteristics for a VHF data exchange system (VDES) in the maritime mobile band (evolução AIS, canais ASM e VDE).
- **ITU Radio Regulations — Apêndice 18** — Frequências marítimas VHF; aloca AIS-1 (161,975 MHz) e AIS-2 (162,025 MHz), canais 75/76 ASM.
- **IEC 61993-2** — Maritime navigation and radiocommunication equipment and systems — AIS — Part 2: Class A shipborne equipment (ensaio, BIIT, certificação SOLAS).
- **IEC 62287-1** — Class B AIS CSTDMA equipment (padrão barato recreio, 2 W, 30 s).
- **IEC 62287-2** — Class B AIS SOTDMA equipment (premium recreio, 5 W, slot reservado).
- **IEC 60945** — Maritime navigation and radiocommunication equipment — General requirements (EMC, IP, vibração, temperatura para toda eletrônica marítima).
- **IEC 61162-1 / -2 (NMEA 0183)** — Digital interfaces (AIVDM/AIVDO, 38400 baud para AIS, distinto dos 4800 baud típicos do NMEA 0183).
- **IEC 61162-3 (NMEA 2000)** — Network-based digital interface, PGNs 129038/129039/129794/129808.
- **IALA Guideline G-1028** — Operational use of AIS (boas práticas, mensagens de segurança, conduta operador).
- **IALA A-126** — Use of AIS in marine aids to navigation (AtoN virtuais, sintéticos, reais em boias e faróis).
- **RIPEAM/COLREGs Rule 5** — Look-out: obrigação de usar TODOS os meios disponíveis (AIS explicitamente inclui-se no lookout eletrônico).
- **NORMAM-204/DPC** — Serviço Móvel Marítimo (alocação de MMSI, registro de estações, licenças ROC/GOC).
- **NORMAM-201/DPC** — Tráfego e Permanência de Embarcações (documentação da estação, AIS em embarcações comerciais nacionais).
- **NORMAM-211/DPC** — Embarcações de esporte e recreio (aplicabilidade a recreio com regra diferenciada para AIS).
- **Resoluções ANATEL aplicáveis** — homologação de equipamentos AIS (Resolução 242/2000, demais atos do SMM), alocação de indicativo de chamada.
- **ABYC E-11 (2023)** — AC and DC Electrical Systems on Boats (fiação, fusíveis e proteção da fonte DC do AIS).
- **ABNT NBR 5410:2004 + emendas** — Instalações elétricas de baixa tensão (aplicável a partes AC quando AIS alimentado por conversor DC-AC).

## Destaques para ensino

- Por que o AIS não substitui o radar (embarcações sem transponder são invisíveis)
- CPA/TCPA: como calcular e o que os alertas significam na prática
- MMSI: a identidade digital da embarcação — como obter e programar
- Receptor vs. transponder: a diferença que significa ser invisível ou visível
- Verificação via MarineTraffic: como confirmar que o sistema funciona

## FAQ

**AIS substitui o radar?**

Não. Radar detecta qualquer alvo físico com ou sem AIS. AIS identifica somente embarcações com transponder ativo. São sistemas complementares.

**Preciso de AIS se tenho radar?**

Em áreas com tráfego comercial intenso: sim — o AIS identifica o navio pelo nome, MMSI e CPA, permitindo contato por VHF. O radar mostra o alvo sem identificação.

**Receptor AIS é suficiente?**

Para ver outros: sim. Para ser visto pelos outros (incluindo navios e serviços de busca e salvamento): não — precisa de transponder.

**Posso usar o MMSI do VHF no AIS?**

Em geral, o AIS e o VHF/DSC da mesma embarcação devem operar com a mesma identidade MMSI oficial. Já o EPIRB segue lógica própria de codificação, registro e programação, ainda que associado à mesma embarcação no cadastro de busca e salvamento. Não convém tratar todos os equipamentos como se fossem programados exatamente do mesmo modo.

## Integração com outras notas

- [[Buzina]]
- [[Bússola Eletrônica (Compass / HDG Sensor)]]
- [[Chartplotter / GPS / MFD]]
- [[Dsc — Chamada Seletiva Digital]]
- [[EPIRB / Beacon de Emergência]]
- [[Estação de Vento / Anemômetro]]
- [[Mob — Man Overboard — Sistema de Detecção]]
- [[NAVEGAÇÃO (BB, BE e Alcançado)]]

## Perguntas que esta nota responde

- O que é AIS (Automatic Identification System) em instalações elétricas náuticas?
- Qual é a função de AIS (Automatic Identification System) na embarcação?
