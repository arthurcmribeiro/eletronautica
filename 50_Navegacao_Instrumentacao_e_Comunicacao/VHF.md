---
title: "VHF"
note_type: "technical-note"
domain: "50_Navegacao_Instrumentacao_e_Comunicacao"
source_file: "VHF e5319734f7fb835c9aaa01e0b5de4318.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "18"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
normas_citadas:
  - "GMDSS (IMO) — Global Maritime Distress and Safety System"
  - "SOLAS Cap. IV — Radiocommunications"
  - "ITU-R M.493 — Digital Selective Calling system for use in the maritime mobile service"
  - "ITU-R M.1084 — Interim solutions for improved efficiency in the use of the band 156-174 MHz"
  - "ITU Radio Regulations — Appendix 18 (VHF maritime channels)"
  - "IEC 60945 — Maritime navigation and radiocommunication equipment — General requirements"
  - "IEC 62238 — Maritime VHF radiotelephone equipment with integrated DSC Class D"
  - "IEC 61097-7 — Shipborne VHF radiotelephone transmitter and receiver"
  - "IEC 61097-3 — Digital Selective Calling equipment operating in MF, MF/HF and VHF"
  - "IEC 61162-1/-2 (NMEA 0183) — Digital interfaces for navigational devices"
  - "IEC 61162-3 (NMEA 2000) — Network-based digital interface for navigational devices"
  - "NORMAM-204/DPC — Serviço Móvel Marítimo e Serviço Móvel Marítimo por Satélite"
  - "NORMAM-201/DPC — Tráfego e Permanência de Embarcações"
  - "NORMAM-211/DPC — Embarcações de esporte e recreio"
  - "Resoluções ANATEL aplicáveis — Serviço Móvel Marítimo e licenciamento de estações de navio"
  - "RIPEAM/COLREGS — Regulamento Internacional para Evitar Abalroamentos no Mar"
  - "ABYC E-11 (2023) — AC and DC Electrical Systems on Boats (alimentação e proteção do VHF)"
  - "ABNT NBR 5410:2004 + emendas — Instalações elétricas de baixa tensão"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://www.nmea.org/standards.html"
  - "https://www.gov.br/anatel/pt-br/regulado/outorga/servico-movel-maritimo"
  - "https://www.itu.int/pub/R-REC"
  - "https://www.imo.org/en/OurWork/Safety/Pages/GMDSS.aspx"
aliases:
  - "VHF"
seo_title: "VHF"
seo_description: "VHF MARINO — Rádio de comunicação marítima na faixa VHF (156–174 MHz). Equipamento central de comunicação e socorro a bordo. Requisitos regulatórios variam conforme classe, área e enquadramento da embarcação."
seo_keywords:
  - "VHF"
  - "50 Navegacao Instrumentacao e Comunicacao"
geo_queries:
  - "O que é VHF em instalações elétricas náuticas?"
  - "Qual é a função de VHF na embarcação?"
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

# VHF

> [!abstract] Resumo técnico
> VHF MARINO — Rádio de comunicação marítima na faixa VHF (156–174 MHz). Equipamento central de comunicação e socorro a bordo. Requisitos regulatórios, obrigação de porte e rotinas de escuta dependem da classe da embarcação, área de navegação e enquadramento aplicável. O VHF com DSC integrado ao GPS é a linha de frente do GMDSS — antecede celular em cobertura, reconhecimento por autoridades e função de emergência.

> [!tip] Regra de decisão em 30 segundos
> 1. **VHF não é opcional em embarcação que sai do abrigo.** Celular não tem cobertura em mar aberto, não é reconhecido pelo MRCC/Salvamar e não transmite posição automática. Para travessia, costeira longa ou área de pesca, VHF fixo com DSC é requisito de segurança — sem exceção.
> 2. **MMSI programado + GPS conectado via NMEA é o que torna o DSC útil.** VHF sem MMSI = DSC inoperante. VHF com MMSI mas sem NMEA = Mayday **sem posição** — o socorro vai chegar em qualquer lugar. Conectar e testar a integração é parte da instalação, não opcional.
> 3. **Canal 16 (156,800 MHz) é o canal de socorro e chamada.** Monitoramento conforme o enquadramento operacional da embarcação e o GMDSS. Não é "canal que pode estar ligado" — é o canal que o navio/estação escuta de forma coerente com sua rotina e sua classe.
> 4. **Alcance em linha de visada: altura da antena é rei.** 25W em antena baixa (T-top de 2m) = 8–12 mn. Mesmo rádio em antena de mastro a 12m = 25–40 mn. Antena e cabo coaxial definem mais alcance do que a potência do rádio.
> 5. **Cabo coaxial: RG-8X ou RG-8/213 — nunca RG-58.** RG-58 perde 3 dB em 10 m no VHF (metade da potência chega à antena). RG-8X é mínimo aceitável; RG-213 ou LMR-400 em corridas longas (>15 m).
> 6. **Conector PL-259/SO-239 é o calcanhar de Aquiles.** 80% dos problemas de alcance resolvem com re-crimpagem ou substituição do conector da base da antena. Oxidação verde = troca imediata. Vedar com autofusão e cinta termo-retrátil marinizada.
> 7. **Sem DSC operante, o VHF não atende o padrão mundial de socorro.** Mayday-voz funciona, mas só quem estiver escutando no momento ouve. DSC com MMSI + GPS envia o distress digital para todo barco/estação no alcance, com posição e identificação — muda o nível da resposta.
> 8. **Portátil não é primário — é backup.** 5–6W contra 25W do fixo, bateria interna limitada, antena curta. Obrigatório ter, mas para emergência primária a cadeia é fixo → DSC → GMDSS.
> 9. **Antena VHF nunca na mesma altura de outras antenas de alta potência.** Convivência com radar, Iridium, celular 4G, outra antena VHF (2ª estação) exige separação vertical e espacial. Acoplamento queima front-end do receptor ou corta a transmissão em redes de alta RF.

> [!danger] Quando chamar um especialista
> - **Programação de MMSI em rádio que já foi programado:** muitos VHFs permitem **apenas uma** programação de MMSI pelo usuário; a segunda vez exige reset em laboratório autorizado ou substituição do rádio. Não tentar reprogramar sem confirmar o modelo e a regra do fabricante.
> - **Licenciamento de estação de navio / MMSI em embarcação com mudança de bandeira ou proprietário:** procedimento envolve ANATEL, DPC e cadastro internacional. Confundir MMSI "de fábrica" ou pedir número não autorizado = multa e invalidade do DSC em emergência real. Despachante ou armador com experiência é regra.
> - **VHF GMDSS tipo Class A com duty cycle de travessia oceânica:** o regime regulatório (SOLAS, STCW, GMDSS área A1/A2/A3/A4) define redundância, fonte reserva e procedimentos. Instalação deve ser por prestador homologado, com inspeção DPC/MRCC.
> - **Sinistro marítimo com Mayday acionado mas socorro sem posição:** revisar cabeamento NMEA, firmware do VHF, configuração do DSC, log do GPS. Perícia precisa de evidência preservada — não apagar o log do equipamento antes do laudo.
> - **Interferência entre VHF e radar / celular / Starlink / Iridium / auto-pilot:** problema de planta de antenas (proximidade, acoplamento, intermodulação). Engenheiro de RF naval faz site survey com analisador de espectro.
> - **Instalação em embarcação metálica (alumínio, aço):** aterramento da malha de plano-terra do dipolo, bonding do cabo coaxial, proteção contra descarga atmosférica, isolação contra correntes galvânicas. Diferente de instalação em casco de fibra — projeto específico.
> - **VHF travando/resetando durante transmissão de alta potência:** queda de tensão > 10% nos terminais durante TX. Pode ser banco subdimensionado, cabo de alimentação inadequado ou bateria com alta impedância interna. Diagnóstico com multímetro registrador + scope.
> - **Certificação de embarcação nova ou importada exigindo homologação DPC/ANATEL:** o equipamento precisa constar da lista de rádios homologados, com etiqueta Anatel e compatibilidade com canais brasileiros. Importação direta sem homologação = bloqueio na vistoria.
> - **Coexistência VHF + AIS + DSC no mesmo rádio "combo":** sincronização, divisão de recepção, prioridades de canal, comportamento em standby. Configuração errada = AIS desativado sem alerta ao operador ou DSC sem GPS.

## O que é

O rádio VHF (Very High Frequency) marino opera na faixa de 156–174 MHz e é o sistema de comunicação voz padrão entre embarcações e entre embarcações e estações costeiras. É o equipamento de socorro e comunicação mais importante a bordo — antecede o telefone celular em cobertura em mar aberto e em reconhecimento pelas autoridades marítimas.

O VHF com DSC (Digital Selective Calling) integra dados de GPS e permite chamada de emergência com posição automática — é o equivalente ao "9-1-1 náutico".

## Função na embarcação

- Comunicação voz entre embarcações e com estações costeiras
- Solicitação de socorro e emergência (Canal 16, DSC)
- Recepção de previsão meteorológica marinha (serviço Meteomar)
- Coordenação de manobras em porto e marina
- Identificação de embarcações e tráfego marítimo
- Integração com AIS para identificação de alvos

## Como aparece na prática

**Muito comum no Brasil:**

- VHF fixo Standard Horizon ou Icom na console de comando
- Antena de fibra de vidro no T-top ou mastro
- Rotina operacional de escuta no Canal 16, conforme o enquadramento operacional e regulatório da embarcação
- VHF portátil como backup em embarcações menores

**Comum em barcos importados:**

- VHF com DSC integrado ao GPS do chartplotter (Standard Horizon Matrix, Icom IC-M506)
- Conexão NMEA 0183 entre GPS e VHF para envio automático de posição
- Antena de alto ganho em mastro ou fly bridge

**Mais presente em embarcações maiores/premium:**

- VHF com AIS integrado (recepção de alvos AIS no mesmo display)
- Duas antenas (principal + backup) com seletor
- MMSI programado de acordo com o processo regulatório vigente e com a configuração DSC adotada

## Fundamentos mínimos

**MMSI (Maritime Mobile Service Identity):** Número de 9 dígitos que identifica a estação marítima/embarcação no ecossistema de radiocomunicação. É indispensável para o uso correto do DSC. O processo de obtenção, licenciamento e registro deve ser confirmado conforme a regulamentação brasileira vigente e a categoria da estação.

**Canal 16:** Canal internacional de emergência e chamada. É o canal de escuta e acionamento inicial mais relevante na rotina marítima, mas a obrigação prática de monitoramento deve ser lida à luz das regras operacionais e regulatórias aplicáveis a cada embarcação e contexto de navegação.

**DSC (Digital Selective Calling):** Sistema digital que permite enviar um sinal de Mayday com posição GPS automaticamente, identificando a embarcação pelo MMSI. Alcance: até 30–40 milhas náuticas. Estações costeiras e outras embarcações com DSC recebem e alertam.

**Potência e alcance:**

- 25W (potência máxima): alcance de 25–40 milhas náuticas (linha de visada + curvatura)
- 1W (potência reduzida): para comunicações locais em marina/porto — preserva bateria e reduz interferência

**Antena:** A antena é determinante para o alcance. Antena de 3dB (1/4 de onda) em T-top vs. antena de 6dB em mastro = diferença significativa de alcance.

## Características principais

| Parâmetro | VHF fixo | VHF portátil |
| --- | --- | --- |
| Potência máxima | 25W | 5–6W |
| Alcance típico | 25–40 mn | 3–8 mn |
| Corrente TX | 4–6A | 1,5–2A |
| Corrente RX | 0,5–1A | 0,2–0,5A |
| DSC | Sim (maioria) | Sim (maioria) |
| IP | IP55–IP67 | IPX7 (flutuante) |
| Conexão GPS | NMEA 0183 ou 2000 | Interna ou externa |

## Configurações e variações comuns

**VHF fixo com DSC (configuração padrão)**

- Standard Horizon GX1850, Icom IC-M330G, Cobra MR F77
- DSC programado com MMSI
- Conexão NMEA com GPS para posição automática

**VHF com AIS integrado**

- Recepção de alvos AIS no display do VHF
- Standard Horizon GX2400, Icom IC-M510
- Exibe embarcações ao redor sem necessidade de display separado

**VHF portátil como backup**

- Icom IC-M25, Standard Horizon HX890
- Flutuante e resistente à imersão
- Para uso em bote, emergência ou quando o fixo falhar

**VHF de cabine (segunda estação)**

- Montado na nav station, fly bridge ou popa
- Conectado à mesma antena do principal (seletor de antena)
- Em iates com múltiplos postos de comando

## Principais marcas

- **Standard Horizon** — líder no Brasil, ampla linha, excelente reputação
- **Icom** — japonesa, qualidade premium, presente em embarcações profissionais
- **Cobra** — acessível, boa relação custo/benefício
- **Uniden** — americana, popular em embarcações de recreio
- **Garmin** — VHF com integração total ao ecossistema Garmin (GHS 10, GMR VHF)

## Componentes e sistemas relacionados

- **Antena VHF** — 3dB ou 6dB, fibra de vidro, SO-239 conector
- **Cabo coaxial** — RG-8X ou RG-8 (baixa perda para VHF), comprimento minimizado
- **GPS/chartplotter** — integração NMEA para posição no DSC
- **MMSI** — número de registro obrigatório para DSC
- **AIS** — complementar ao VHF (identificação de embarcações)
- **Disjuntor dedicado** — no painel, protegendo o circuito do VHF

## Onde costuma dar problema

| Problema | Sintoma | Causa |
| --- | --- | --- |
| Alcance muito curto | Só ouve/transmite a poucos km | Antena com defeito, cabo ruim, conexões oxidadas |
| Áudio distorcido | Voz incompreensível na transmissão | Microfone defeituoso, modulação mal ajustada |
| DSC sem posição | "No position data" na tela | NMEA não conectado ou GPS sem fix |
| Sem áudio na recepção | Canal 16 silencioso | Volume, squelch fechado demais, antena |
| Interferência | Ruído em outros instrumentos | Cabo de alimentação do VHF causando EMI |
| VHF não liga | Sem display | Fusível queimado, cabo de alimentação |

## Causas raiz

**Alcance curto:**

- Conector PL-259 (SO-239) oxidado na antena — principal causa de perda de alcance
- Cabo coaxial de baixa qualidade ou muito longo (perda de sinal)
- Antena danificada (fibra trincada deixa entrar água no radome)

**DSC sem posição:**

- NMEA 0183 não conectado ao VHF (verificar pinos TX e RX no conector)
- GPS com fix mas outputting em NMEA 2000 (VHF lê NMEA 0183 — verificar protocolo)

**Causa raiz mais comum:** Conector de antena oxidado. A maioria dos problemas de alcance no VHF é resolvida simplesmente limpando ou substituindo o conector PL-259 na base da antena.

## Diagnóstico prático

**Passo 1:** Alcance curto → inspecionar conector na base da antena. Oxidação verde = problema. Substituir ou limpar com contato elétrico.

**Passo 2:** Verificar continuidade do cabo coaxial do VHF à antena. Qualquer resistência no centro (além do resistor de terminação) indica problema.

**Passo 3:** DSC sem posição → verificar cabo NMEA entre GPS e VHF. Testar com NMEA viewer no chartplotter para confirmar que o GPS está enviando dados.

**Passo 4:** Verificar transmissão → pedir a outra embarcação ou rádio para confirmar qualidade de áudio e alcance.

## Boas práticas

- Programar o MMSI somente após confirmar o dado oficial correto e o procedimento do fabricante, pois muitos equipamentos limitam reprogramação sem assistência técnica
- Conectar o GPS ao VHF via NMEA 0183 — posição automática no DSC é essencial para emergências
- Manter rotina de escuta e disciplina operacional compatíveis com o uso seguro do VHF e com a regulamentação aplicável ao tipo de operação
- Usar cabo coaxial RG-8X ou RG-8 (não RG-58 — perda excessiva no VHF)
- Limpar e inspecionar conector da antena anualmente
- Ter redundância de comunicação portátil é altamente recomendável, sobretudo em navegação costeira mais longa, travessias e embarcações com dependência crítica do posto principal

## Erros comuns

❌ **VHF sem MMSI programado** — DSC inoperante, emergência sem identificação

❌ **Sem conexão GPS-VHF** — no Mayday, posição não é enviada automaticamente

❌ **Cabo coaxial RG-58** — perda de 3dB+ em comprimentos de 10m — prejudica significativamente o alcance

❌ **Conector PL-259 mal feito** — perda de sinal na junção, alcance reduzido

❌ **Volume e squelch mal ajustados** — não ouve chamadas no canal 16

❌ **Canal 16 ignorado sem critério operacional** — perda de consciência situacional e pior resposta em chamadas de socorro ou segurança

## Relação com outros sistemas

- **GPS/chartplotter** — integração NMEA para posição no DSC
- **AIS** — complementar: VHF comunica, AIS identifica
- **Antena** — componente crítico para desempenho
- **Banco de bateria** — corrente de TX considerável em uso intenso
- **EPIRB** — backup de emergência quando VHF não tem alcance

## Brasil x referências internacionais

### Prática comum no Brasil

VHF instalado mas sem MMSI, sem conexão GPS, Canal 16 não monitorado. VHF portátil sem bateria carregada.

### Referência internacional

MMSI obrigatório, DSC com GPS integrado, Canal 16 sempre monitorado, VHF portátil como backup padrão de segurança.

### Ponto de conflito

No Brasil, a NORMAM exige VHF mas não detalha o requisito de MMSI com o mesmo rigor dos países do hemisfério norte. Na prática, muitos VHFs instalados são "decoração" sem função real de emergência.

### Leitura equilibrada

O VHF é mais útil que o celular em mar por cobertura, reconhecimento pelas autoridades e função DSC. Em emergência: VHF com MMSI programado e posição GPS integrada vale mais que qualquer celular.

## Glossário rápido

- **VHF marítimo:** faixa 156–174 MHz alocada pela ITU para comunicação marítima.
- **Canal 16 (156,800 MHz):** canal internacional de socorro, segurança e chamada. Escuta obrigatória conforme enquadramento/GMDSS.
- **Canal 70 (156,525 MHz):** canal exclusivo para Chamada Seletiva Digital (DSC) — não é usado para voz.
- **Canal 06 / 13 / 22A:** canal de comunicação ship-to-ship, ponte-a-ponte (bridge-to-bridge) e coordenação com Guarda Costeira (22A nos EUA).
- **Dual Watch / Tri Watch:** função que monitora simultaneamente Canal 16 + outro canal (Dual) ou Canal 16 + 2 canais (Tri).
- **Scan (varredura):** varre todos os canais memorizados, parando quando detecta transmissão.
- **DSC (Digital Selective Calling):** protocolo digital que envia chamadas (distress, urgency, routine) com identificação MMSI e posição GPS automaticamente pelo Canal 70.
- **MMSI (Maritime Mobile Service Identity):** número de 9 dígitos que identifica a estação marítima. Obrigatório para DSC. Obtenção no Brasil via ANATEL/DPC.
- **Mayday:** sinal de socorro de **risco imediato de vida ou navio**. Maior prioridade. Formato: "Mayday-Mayday-Mayday, este é [MMSI], posição, natureza da emergência, assistência requerida".
- **Pan-Pan:** sinal de **urgência sem risco imediato de vida** (avaria, medical, pessoa doente).
- **Sécurité:** sinal de **segurança** (aviso à navegação, meteorológico, objeto flutuante).
- **GMDSS (Global Maritime Distress and Safety System):** sistema global de socorro que integra DSC, EPIRB, SART, NAVTEX, Inmarsat e VHF.
- **GMDSS Área A1:** cobertura VHF com DSC (até ~20–30 mn da costa).
- **GMDSS Área A2:** cobertura MF/HF com DSC (até ~150 mn da costa).
- **GMDSS Área A3/A4:** cobertura Inmarsat / polar por HF.
- **MRCC (Maritime Rescue Coordination Centre):** centro de coordenação de salvamento marítimo. No Brasil: Salvamar Brasil (Marinha do Brasil).
- **SOLAS:** Safety of Life at Sea — convenção IMO que define requisitos de equipamentos para navios mercantes e exemplifica o pano de fundo do GMDSS.
- **RIPEAM / COLREGS:** regras internacionais para evitar abalroamento — ponto-a-ponto também pode usar VHF (Canal 13).
- **VHF fixo:** rádio 25W instalado permanentemente, alimentado por banco DC, antena externa.
- **VHF portátil (hand-held):** 5–6W, bateria interna, à prova d'água (IPX7 ou IPX8), flutuante em modelos marinos.
- **Potência alta (HI):** 25W para comunicação de longo alcance.
- **Potência baixa (LO / 1W):** para comunicação local (marina, porto) e redução de bateria.
- **Squelch (silenciador):** supressão de ruído quando não há sinal — abrir demais → só ouve chiado; fechar demais → não ouve chamadas fracas.
- **Gain (ganho):** em dBi (dipolo isotrópico) ou dBd (dipolo de referência). Antena de 6 dBd ≈ 8 dBi.
- **Dipolo 1/2 onda:** antena típica de 6 dBd usada em mastro de veleiro.
- **Colinear 5/8 onda:** antena típica de 3 dBd usada em T-top de lancha — mais curta, menos direcional em rolagem.
- **Plano-terra / ground plane:** referência elétrica necessária para antena vertical. Em casco metálico = o próprio casco; em fibra = radiais ou plano planeado.
- **VSWR / ROE (Razão de Onda Estacionária):** relação entre potência refletida e incidente na antena. Ideal < 1,5:1; acima de 2:1 há risco de danificar o PA do rádio.
- **PL-259 / SO-239:** conector coaxial padrão em VHF marítimo (macho PL-259, fêmea SO-239).
- **N connector:** conector alternativo de alta qualidade, à prova d'água, usado em instalações premium.
- **Coaxial RG-58:** cabo de baixa qualidade (perda ~3 dB/10 m em VHF). **Não recomendado** para VHF fixo.
- **Coaxial RG-8X (Mini-8):** cabo intermediário (perda ~1,5 dB/10 m). Mínimo aceitável.
- **Coaxial RG-8/213:** cabo de baixa perda (~0,8 dB/10 m). Recomendado em corridas longas.
- **Coaxial LMR-400:** equivalente americano de alta qualidade, baixíssima perda.
- **dB (decibel):** escala logarítmica de potência. 3 dB = dobro/metade; 10 dB = 10×/0,1×.
- **Audio noise blanker:** filtro que reduz ruído pulsado (ignição do motor, alternador).
- **Class A DSC:** exigido em navios SOLAS. Mais recursos, múltiplas classes de chamadas.
- **Class B DSC:** simplificado, usado em não-SOLAS (pesca costeira).
- **Class D DSC:** classe mais comum em rádios de recreio. IEC 62238.
- **ATIS (Automatic Transmitter Identification System):** identificação automática exigida em hidrovias europeias (CEVNI/Rhine).
- **Rx/Tx (Recepção/Transmissão):** estado do rádio. Corrente Tx fixo ≈ 4–6 A em HI.
- **Distress button:** botão vermelho protegido do DSC; pressionar >3s envia Mayday automático.
- **Position Request:** função DSC para solicitar posição de outra estação (buddy tracking).
- **All Ships Call:** chamada DSC para todas as estações em alcance (não-emergency, ex. aviso local).
- **Group Call:** chamada a MMSI de grupo (frota, clube, marina).
- **NMEA sentence "DSC" / "DSE" (0183):** sentenças que o VHF envia ao chartplotter com info do DSC recebido.
- **PGN 129808 (NMEA 2000):** DSC Call Information — equivalente moderno em rede.
- **ANATEL:** Agência Nacional de Telecomunicações — licenciamento de estação e indicativo de chamada no Brasil.
- **Indicativo de chamada (call sign):** identificação alfanumérica atribuída à estação (ex. PU0XYZ).
- **VHF com AIS:** rádio que integra receptor AIS Classe B — exibe alvos AIS no display.
- **ECLI/RF exposure:** limites de exposição a radiofrequência — VHF portátil mais relevante (antena próxima ao corpo).

## Normas e referências aplicáveis

- **GMDSS (IMO — Global Maritime Distress and Safety System)** — sistema global de socorro para navegação marítima.
- **SOLAS, Cap. IV — Radiocommunications** — requisitos de equipamentos de radiocomunicação para navios mercantes (base conceitual do GMDSS).
- **ITU-R M.493** — *Digital Selective Calling system for use in the maritime mobile service.* Define o protocolo DSC.
- **ITU-R M.1084** — *Interim solutions for improved efficiency in the use of the band 156-174 MHz by stations in the maritime mobile service.*
- **ITU Radio Regulations, Apêndice 18** — alocação de canais VHF marítimos internacionais.
- **IEC 60945** — *Maritime navigation and radiocommunication equipment and systems — General requirements.* Requisitos ambientais, EMC, segurança elétrica.
- **IEC 62238** — *Maritime VHF radiotelephone equipment and systems with integrated Class D DSC — Operational and performance requirements.* Referência para VHF de recreio com DSC.
- **IEC 61097-7** — *Shipborne VHF radiotelephone transmitter and receiver.* Requisitos técnicos.
- **IEC 61097-3** — *Digital Selective Calling (DSC) equipment operating in MF, MF/HF and VHF bands.*
- **IEC 61162-1/-2 (NMEA 0183)** — sentenças de comunicação entre o VHF (DSC) e o GPS/chartplotter.
- **IEC 61162-3 (NMEA 2000)** — rede digital moderna para troca de PGNs (ex. 129808 DSC Call).
- **NORMAM-204/DPC** — *Serviço Móvel Marítimo e Serviço Móvel Marítimo por Satélite.* Base brasileira para uso, licenciamento e inspeção.
- **NORMAM-201/DPC** — *Tráfego e Permanência de Embarcações em Águas Jurisdicionais Brasileiras.*
- **NORMAM-211/DPC** — *Embarcações de esporte e recreio.* Requisitos para amadores.
- **Resoluções ANATEL aplicáveis** — Serviço Móvel Marítimo (SMM), homologação de equipamentos, atribuição de MMSI e indicativo de chamada. Verificar edição vigente caso a caso.
- **RIPEAM/COLREGS** — *Regulamento Internacional para Evitar Abalroamentos no Mar.* Canal 13 (bridge-to-bridge) é ferramenta operacional.
- **ABYC E-11 (2023)** — *AC and DC Electrical Systems on Boats.* Base para alimentação DC do VHF fixo, fusível e aterramento RF.
- **ABNT NBR 5410:2004 + emendas** — *Instalações elétricas de baixa tensão.* Complemento nacional.

## Destaques para ensino

- Canal 16: o que é, por que deve ser monitorado e o que fazer quando alguém chama Mayday
- DSC: como funciona o sistema, por que o MMSI é obrigatório
- Alcance VHF: linha de visada, curvatura da Terra, efeito da antena
- Cabos coaxiais: RG-8X vs RG-58 — a diferença no alcance
- Procedimento de Mayday: como chamar corretamente

## Ideias de vídeo, aula prática ou demonstração

- Demonstração de chamada DSC: procedimento passo a passo
- Teste de alcance real: VHF vs. celular em mar aberto
- Limpeza de conector PL-259: antes e depois do alcance
- Como programar MMSI no VHF (Standard Horizon e Icom)
- Procedimento de Mayday: treinamento prático a bordo

## FAQ

**O celular substitui o VHF?**

Não para emergências marítimas. O VHF tem cobertura em mar aberto onde não há sinal celular, é reconhecido pelo Salvamento Marítimo e pelo MRCC (Maritime Rescue Coordination Center), e tem alcance de 25–40 milhas (vs. 2–5 do celular em condições normais).

**O que é o MMSI e onde obter?**

Maritime Mobile Service Identity — número de 9 dígitos usado na identificação digital da estação marítima/embarcação. O caminho exato para obtenção e registro deve ser confirmado conforme a regulamentação vigente; o ponto importante aqui é não programar um número informal ou não autorizado.

**Canal 16 sempre ligado não gasta muita bateria?**

No modo de recepção (RX), o VHF consome ~0,5–1A. Em 10 horas: 5–10Ah — aceitável para qualquer banco de bateria de embarcação. Vale o consumo pelo que representa em segurança.

**Posso usar o VHF portátil como sistema principal?**

Temporariamente sim. Como sistema permanente: potência de 5W vs. 25W do fixo = alcance muito menor. Portátil é backup, não primário.

## Visual didático

![Comunicacao e seguranca: AIS, VHF, DSC e EPIRB](../_visuals/generated/ais-vhf-dsc-epirb-camadas.svg)

Mostrar que AIS, VHF, DSC e EPIRB sao complementares, nao substitutos diretos.

**Cautela:** Requisitos de licenciamento, MMSI, programacao e uso variam por jurisdicao e equipamento.

Material de apoio: [Comunicacao e seguranca: AIS, VHF, DSC e EPIRB](../_visuals/generated/ais-vhf-dsc-epirb-camadas.md)

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

- O que é VHF em instalações elétricas náuticas?
- Qual é a função de VHF na embarcação?
