---
title: "AIS (Automatic Identification System)"
note_type: "technical-note"
domain: "50_Navegacao_Instrumentacao_e_Comunicacao"
source_file: "AIS (Automatic Identification System) 33a19734f7fb81b4b75ffe1f6db19c78.md"
status: "technical-review-l1"
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

- **SOLAS** — AIS Classe A obrigatório para navios > 300 GT em viagens internacionais
- **ITU Radio Regulations** — frequências AIS 161,975 e 162,025 MHz
- **NORMAM-01** — regulação nacional (AIS não claramente obrigatório para recreio)
- **IALA Guidelines** — boas práticas de instalação e uso

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
