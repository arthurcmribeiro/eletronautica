---
title: "NMEA 2000 / NMEA 0183 — Rede de Instrumentos"
note_type: "system"
domain: "50_Navegacao_Instrumentacao_e_Comunicacao"
source_file: "NMEA 2000 NMEA 0183 — REDE DE INSTRUMENTOS 33a19734f7fb81769c8be9e14765b8fc.md"
status: "fase-5-reescrita-premium"
fase_5_reescrita: "06"
prioridade_fase_5: 6.3
reviewed_on: "2026-04-18"
review_jurisdiction:
  - "Brasil"
  - "internacional"
normas_citadas:
  - "NMEA 0183 (última versão NMEA — verificar com a NMEA antes de publicar)"
  - "NMEA 2000 (última versão NMEA — verificar com a NMEA antes de publicar)"
  - "IEC 61162-1:2016"
  - "IEC 61162-3:2008+A2:2019"
  - "ISO 11898-1:2015 (CAN — camada de enlace)"
  - "NORMAM-204/DPC (radiocomunicações marítimas — quando NMEA carrega DSC/AIS)"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://www.nmea.org/standards.html"
  - "https://www.gov.br/anatel/pt-br/regulado/outorga/servico-movel-maritimo"
aliases:
  - "NMEA 2000 NMEA 0183 — REDE DE INSTRUMENTOS"
  - "NMEA 2000 / NMEA 0183 — REDE DE INSTRUMENTOS"
seo_title: "NMEA 2000 / NMEA 0183 — Rede de Instrumentos"
seo_description: "NMEA 2000 / NMEA 0183 — REDE DE INSTRUMENTOS — Protocolos padrão de comunicação entre instrumentos náuticos. NMEA 0183 é serial ponto a ponto (legado, ainda dominant."
seo_keywords:
  - "NMEA"
  - "2000"
  - "0183"
  - "Rede"
  - "Instrumentos"
  - "50 Navegacao Instrumentacao e Comunicacao"
geo_queries:
  - "O que é NMEA 2000 / NMEA 0183 — Rede de Instrumentos em instalações elétricas náuticas?"
  - "Qual é a função de NMEA 2000 / NMEA 0183 — Rede de Instrumentos na embarcação?"
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

# NMEA 2000 / NMEA 0183 — Rede de Instrumentos

> [!abstract] Resumo técnico
> NMEA 2000 / NMEA 0183 — REDE DE INSTRUMENTOS — Protocolos padrão de comunicação entre instrumentos náuticos. NMEA 0183 é serial ponto a ponto, ainda muito presente em retrofit e integrações legadas. NMEA 2000 é rede em barramento CAN com compartilhamento estruturado de dados, mas exige topologia, alimentação e terminação corretas.

> [!tip] Regra de decisão em 30 segundos
> - **0183 = serial ponto-a-ponto** (1 talker → N listeners); **2000 = barramento CAN compartilhado** (todos enxergam todos).
> - **Baud 0183:** 4800 (v2.x, padrão histórico) ou 38400 (v3/HS — AIS, instrumentos rápidos). Misturar = silêncio.
> - **N2K backbone exige 2 terminadores 120Ω** + 1 power tap (fusível 3A, 9–16 V DC).
> - **Resistência ponta-a-ponta do backbone (rede desligada) ≈ 60Ω** — diferente disso = problema antes de ligar nada.
> - **Drop N2K ≤ 6 m por norma; manter < 3 m na prática** (reflexão de sinal corrompe dados).
> - **TX/RX invertido é a falha #1 do 0183.** Em RS-422 diferencial, TX+ → RX+ e TX- → RX-.
> - **SeaTalkNG / SimNet ≠ N2K plug-and-play.** Camada física compatível, mas pinagem, alimentação e suporte do fabricante decidem a interoperabilidade real.

## O que é

**NMEA** = National Marine Electronics Association — organização americana que define os padrões de comunicação entre eletrônicos náuticos.

**NMEA 0183:**

- Protocolo serial assíncrono, definido originalmente sobre interface diferencial do tipo RS-422; na prática, há equipamentos com implementação single-ended ou adaptações proprietárias
- Ponto a ponto: 1 talker (transmissor) → múltiplos listeners (receptores)
- Velocidade padrão: 4800 baud (v2.x) ou 38400 baud (v3.x/HS)
- Dados em texto ASCII: sentences como $GPGGA, $IIMWV, $VDVTG

**NMEA 2000:**

- Protocolo de rede em barramento CAN bus (Controller Area Network)
- Múltiplos talkers e listeners no mesmo cabo (backbone)
- Velocidade: 250 kbps (50x mais rápido que NMEA 0183)
- Dados em binary PGNs (Parameter Group Numbers)
- Plug-and-play com conectores padronizados (Micro-C)

## Função

- Integrar todos os instrumentos da embarcação em uma rede única
- Compartilhar dados de GPS, profundidade, vento, velocidade, heading com múltiplos displays
- Permitir que o piloto automático receba dados de todos os sensores
- Enviar posição GPS para o VHF/DSC automaticamente
- Exibir dados de motor (NMEA 2000) no chartplotter

## Como aparece na prática

**NMEA 0183 (situação típica no Brasil):**

- Fio azul + fio marrom saindo do GPS → entrada NMEA IN do chartplotter
- GPS envia $GPGGA, $GPRMB ao VHF DSC → VHF sabe a posição
- Anemômetro envia $IIMWV → instrumento de vento → piloto automático
- Múltiplos cabos soltos, conectores DB-9 e bornes de parafuso

**NMEA 2000 (moderno):**

- Um único backbone de 5 fios (2 dados + 2 energia + shield)
- Drops de 6 pol saindo do backbone para cada equipamento
- Tee-connectors Micro-C plugados em sequência
- GPS, sonda, radar, piloto, chartplotter todos no mesmo barramento

## Fundamentos mínimos

| Parâmetro | NMEA 0183 | NMEA 2000 |
| --- | --- | --- |
| Velocidade | 4800 / 38400 baud | 250 kbps |
| Topologia | Ponto a ponto | Barramento (bus) |
| Cabos | Par trançado / coaxial | Cabo Micro-C 5 fios |
| Alimentação | Separada | Pelo backbone (LEN) |
| Máx. dispositivos | 1 talker / múltiplos listeners, conforme carga e interface | limitado por LEN, alimentação, backbone e topologia |
| Endereçamento | Não (identificado por conector) | Sim (NAME automático) |
| Padrão elétrico | RS-422 / RS-232 | CAN bus ISO 11898 |
| Conector padrão | Sem padrão (borne, DB-9, RJ45) | Micro-C (padronizado) |

## Sentences NMEA 0183 mais comuns

| Sentence | Significado | Fonte típica |
| --- | --- | --- |
| $GPGGA | Posição GPS + qualidade | GPS |
| $GPRMC | Posição + velocidade + data | GPS |
| $GPVTG | COG + SOG | GPS |
| $IIMWV | Velocidade/direção vento aparente | Anemômetro |
| $IIMWD | Direção vento verdadeiro | Instrumento |
| $IIVHW | Velocidade através da água | Log de água |
| $IIHDG | Heading magnético | Bússola/fluxgate |
| $SDDBT | Profundidade | Sonda |
| $VDVTG | Course Over Ground | GPS/AIS |
| $AIVDM | Mensagem AIS recebida | Transponder AIS |

## PGNs NMEA 2000 mais relevantes

| PGN | Dado | Fonte |
| --- | --- | --- |
| 126992 | System Time | GPS |
| 127250 | Vessel Heading | Compass/HDG |
| 127251 | Rate of Turn | IMU |
| 127258 | Magnetic Variation | GPS |
| 127488 | Engine Parameters (rapid) | Motor gateway |
| 127489 | Engine Parameters (dynamic) | Motor gateway |
| 128259 | Speed Through Water | Log |
| 128267 | Water Depth | Sonda |
| 129025 | Position, Rapid Update | GPS |
| 129026 | COG + SOG | GPS |
| 130306 | Wind Data | Anemômetro |
| 130310 | Environmental Parameters | Múltiplos |

## Configurações e topologias

**NMEA 0183 básica:**

```jsx
GPS ──TX+/TX──► Chartplotter RX+/RX
GPS ──TX+/TX──► VHF NMEA IN
Anemômetro ──► Instrumento de vento
Instrumento ──► Piloto automático
```

**NMEA 2000 completa:**

```jsx
[Terminador] ─── [Backbone] ─── [Terminador]
                    │
        ┌───────────┼───────────┐
      [GPS]    [Chartplotter]  [Piloto]
        │
      [Sonda]──[Anemômetro]──[AIS]──[Motor GW]
```

**Conversores e gateways:**

- **Actisense NGT-1:** converte NMEA 0183 ↔ NMEA 2000 (mais usado no mundo)
- **Garmin GND 10:** bridge NMEA 0183/2000 para equipamentos Garmin
- **Maretron USB100:** interface para computador (monitoramento e diagnóstico)
- **Digital Yacht iKonvert:** NMEA 0183 → NMEA 2000

## Marcas e componentes

| Componente | Fabricante | Observação |
| --- | --- | --- |
| Backbone cable | Garmin, Maretron, Actisense | Usar cabo certificado N2K |
| Tee connectors | Garmin, Maretron, Lowrance | Micro-C padrão |
| Power tap | Garmin, Maretron | Alimenta o backbone (fusível 3A) |
| Terminadores | Qualquer fabricante certificado | Resistor 120Ω em cada ponta |
| NGT-1 gateway | Actisense | Referência para conversão |
| USB100 | Maretron | Monitoramento avançado |
| SeaTalkNG | Raymarine | Proprietário mas compatível N2K |
| SimNet | Simrad | Proprietário mas compatível N2K |

**Importante:** SeaTalkNG (Raymarine) e SimNet (Simrad) compartilham base CAN compatível com o ecossistema NMEA 2000 em muitos cenários, mas a interoperabilidade depende de conectorização, pinagem, alimentação do backbone e suporte do fabricante. Adaptadores físicos não garantem interoperabilidade plena por si só.

## Problemas mais frequentes

| Problema | Causa raiz |
| --- | --- |
| GPS não aparece no chartplotter | TX/RX invertido, baud rate errado, fio partido |
| Todos os dispositivos N2K somem | Terminador faltando ou backbone em curto |
| Leitura errática no N2K | Drop muito longo (>6m), conector Micro-C mal travado |
| VHF não recebe posição | Sentence errada (precisa $GPRMC ou $GPGGA), baud 4800 |
| Piloto não recebe heading | PGN 127250 não presente, sensor não configurado |
| Conflito de endereços N2K | Dois dispositivos com mesmo NAME — reiniciar o que tem problema |

## Causas raiz detalhadas

**TX/RX invertido (NMEA 0183):** Erro clássico. O fio TX do transmissor deve ir ao RX do receptor. Em RS-422 diferencial, TX+ vai a RX+ e TX- vai a RX-. Instaladores amadores frequentemente invertem e o sistema não funciona.

**Baud rate errado:** NMEA 0183 v2 usa 4800 baud. Versão HS (High Speed) usa 38400. Misturar baud rates = sem comunicação. Sempre confirmar no manual do equipamento.

**Terminadores faltando (N2K):** A rede NMEA 2000 exige terminadores de 120Ω em cada extremidade do backbone. Sem eles, reflexões de sinal corrompem os dados. Sintoma: todos os dispositivos somem ou apresentam dados erráticos.

**Drop longo demais (N2K):** Especificação limita drops a 6m. Drops longos causam reflexão de sinal. Na prática, manter abaixo de 3m.

## Diagnóstico prático

```jsx
NMEA 0183:
Passo 1: Confirmar baud rate nos dois equipamentos (manual)
Passo 2: Confirmar atividade serial no transmissor com interface apropriada, analisador ou equipamento de teste compatível
Passo 3: Conectar laptop com Putty (4800 8N1) no RX do receptor
Passo 4: Verificar se chegam sentences legíveis ($GPGGA, etc.)
Passo 5: Se não chega nada → verificar TX/RX invertido
Passo 6: Se chega mas não decodifica → verificar baud rate

NMEA 2000:
Passo 1: Verificar tensão no backbone (deve ser 9–16V DC entre +12V e GND)
Passo 2: Confirmar que ambos os terminadores estão instalados
Passo 3: Medir resistência do backbone (com rede desligada) → deve ser ~60Ω (dois 120Ω em paralelo)
Passo 4: Usar software de diagnóstico (Maretron N2KAnalyzer ou Actisense NMEAReader)
Passo 5: Verificar se o dispositivo problemático aparece na lista de devices
```

## Boas práticas profissionais

- Documentar todo o wiring NMEA 0183: qual sentence vai a qual pino de qual equipamento
- Usar cabo blindado para NMEA 0183 (reduz EMI de inversor e carregador)
- Manter drops N2K tão curtos quanto a instalação permitir e dentro dos limites de comprimento previstos para a topologia adotada
- Alimentar o backbone N2K com fusível de 3A próximo à fonte
- Usar apenas componentes certificados NMEA 2000 no backbone (evitar imitações)
- Testar a rede com software de diagnóstico após qualquer modificação

## Cuidados de instalação

- Não usar conector macho Micro-C com fita isolante como "terminador" — usar terminadores reais
- Rotular cada fio NMEA 0183 na instalação (TX+, TX-, RX+, RX- de cada instrumento)
- Não misturar N2K certificado com cabo genérico no mesmo backbone
- Observar a polaridade em NMEA 0183 RS-422 (diferencial — ambos os fios importam)
- Instalar power tap do backbone próximo ao painel, com fusível 3A

## Cuidados de uso

- Ao trocar um instrumento, verificar se o novo usa o mesmo baud rate do antigo
- Não tratar "50 dispositivos" como regra universal: verificar LEN total, corrente disponível, extensão do backbone e limites da topologia real
- Manter os conectores Micro-C travados (têm anel de travamento)
- Verificar periodicamente se os terminadores N2K estão presentes (podem ser retirados acidentalmente)

> [!danger] Quando chamar especialista
> Há cenários onde insistir no DIY transforma um pequeno erro de rede em parada operacional, equipamento queimado ou risco de comunicação de emergência mal interpretada. Pare e procure profissional/integrador certificado quando:
> - **Integração de motor (J1939 → N2K)** com gateway dedicado — pinagem proprietária do fabricante do motor + risco de injetar PGNs incorretos no backbone.
> - **Backbone com mais de ~20 dispositivos** ou extensão somada > 50 m — entra em território de cálculo de LEN, queda de tensão no backbone e múltiplos power taps.
> - **Mistura de SeaTalkNG, SimNet e N2K certificado** num backbone único — adaptadores físicos resolvem a conexão, não a interoperabilidade lógica.
> - **Conflito de endereços N2K que não some após reboot/reset** — pode indicar firmware corrompido ou dispositivo com NAME duplicado de fábrica.
> - **AIS Class A com integração N2K** — reporting de posição é obrigatório por COLREGS / IMO; erro de timing ou PGN errado vira não-conformidade regulatória.
> - **Multiplexer 0183 com mais de 3 talkers** ou misturando baud rates diferentes na mesma saída — começa a exigir filtragem de sentences por prioridade.
> - **DSC do VHF não recebe posição** após inserção de gateway — risco de chamada de socorro sem coordenadas (vai contra ITU-R M.493 e NORMAM-204/DPC).
>
> Custo de uma hora de integrador certificado é uma fração do custo de um chartplotter premium ou de uma chamada de DSC sem coordenadas em emergência real.

## Erros comuns de instaladores

- Inverter TX e RX no NMEA 0183 (o mais comum de todos)
- Esquecer os terminadores no backbone NMEA 2000
- Usar cabo de alarme ou telefônico comum como cabo de rede N2K
- Não documentar o wiring → próxima manutenção é um pesadelo
- Ligar múltiplos talkers no mesmo par RX sem multiplexer (sinal corrompido)
- Confundir SeaTalkNG / SimNet com NMEA 2000 puro (precisam adaptadores)

## Relação com outros sistemas

- **GPS:** principal talker NMEA (fornece posição, velocidade, tempo)
- **VHF/DSC:** precisa receber posição GPS via NMEA para funcionar no DSC
- **Piloto automático:** recebe COG, SOG, HDG, vento via NMEA
- **Chartplotter/MFD:** hub central que recebe tudo
- **AIS:** transmite e recebe sentences NMEA AIS ($AIVDM, $AIVDO)
- **Motor (gateway):** converte J1939 (diesel) para N2K PGNs de motor
- **Instrumentos de bordo:** speed, depth, wind — todos na rede

## Brasil x Internacional

| Aspecto | Brasil | Internacional |
| --- | --- | --- |
| Protocolo dominante | NMEA 0183 ainda muito presente | NMEA 2000 já é padrão |
| Instalações mistas | Muito comum | Ainda presente em barcos antigos |
| Conhecimento técnico | Baixo na maioria dos instaladores | Maior base técnica |
| Gateways e conversores | Pouco usados | Actisense NGT-1 é comum |
| Diagnóstico | Feito "às cegas" | Software de diagnóstico disponível |

**Muito comum no Brasil:** NMEA 0183 com fiação exposta, baud rate errado, sem documentação.

**Mais presente em embarcações maiores/premium:** backbone NMEA 2000 completo com Maretron ou Garmin.

## Normas e referências

- **NMEA 0183 Standard:** documento controlado pela NMEA — a edição em vigor (e o licenciamento para implementadores) é verificável junto à NMEA ([NMEA.org](https://www.nmea.org/standards.html)). A versão pública mais citada é 4.x (HS define 38400 baud).
- **NMEA 2000 Standard:** documento controlado pela NMEA — edição e certificação verificáveis junto à NMEA. Não confundir com o protocolo CAN puro: NMEA 2000 define PGNs, conector Micro-C, alimentação do backbone e regras de LEN.
- **IEC 61162-1:2016** — equivalente internacional do NMEA 0183 (Maritime navigation and radiocommunication equipment and systems — Digital interfaces — Part 1: Single talker and multiple listeners).
- **IEC 61162-3:2008+A2:2019** — equivalente internacional do NMEA 2000 (Part 3: Serial data instrument network).
- **ISO 11898-1:2015** — base elétrica e camada de enlace do CAN bus que NMEA 2000 utiliza.
- **NORMAM-204/DPC** — radiocomunicações marítimas no Brasil; entra em jogo quando a rede NMEA carrega dados para DSC/AIS/EPIRB.
- **ITU-R M.493** — DSC; a posição GPS levada por NMEA até o VHF/DSC tem que estar correta para chamadas de socorro.

## Como ensinar este tópico

**Sequência recomendada:**

1. Analogia: NMEA 0183 é como telefone fixo (discado, ponto a ponto). NMEA 2000 é como Wi-Fi (todos conectados ao mesmo roteador)
2. Mostrar sentences NMEA 0183 em tela (Putty / NMEAReader)
3. Demonstrar backbone NMEA 2000 montado fisicamente
4. Exercício: montar mini-backbone com 3 dispositivos e identificar no software
5. Troubleshooting: retirar terminador e mostrar o que acontece

## Ideias de vídeos

- "NMEA 0183 na prática: conectando GPS ao chartplotter e VHF"
- "NMEA 2000: montando o backbone do zero em uma lancha"
- "Por que meu GPS não aparece no chartplotter? TX/RX invertido!"
- "Diferença entre NMEA 0183 e NMEA 2000: quando usar cada um"
- "Diagnosticando rede NMEA 2000 com software Actisense"
- "SeaTalkNG, SimNet e NMEA 2000: são compatíveis?"

## Diagramas sugeridos

- Diagrama de wiring completo NMEA 0183: GPS → Chart → VHF → Piloto (com TX+/TX-/RX+/RX-)
- Diagrama de backbone NMEA 2000: backbone + drops + power tap + terminadores
- Tabela comparativa: NMEA 0183 vs NMEA 2000 vs SeaTalkNG vs SimNet
- Fluxograma de diagnóstico para "GPS não aparece no chartplotter"
- Mapa de PGNs NMEA 2000 por tipo de dado (posição, vento, profundidade, motor)

## FAQ

**Posso misturar NMEA 0183 e NMEA 2000 na mesma embarcação?**

Sim, e é a situação mais comum. Use um gateway/conversor (Actisense NGT-1) para integrar os dois mundos.

**Preciso de multiplexer para NMEA 0183?**

Se tiver mais de um talker querendo transmitir para o mesmo receptor, sim. Sem multiplexer, os sinais se sobrepõem e corrompem.

**SeaTalkNG da Raymarine é igual a NMEA 2000?**

Frequentemente é interoperável na camada física, mas não deve ser tratado como equivalência automática. Adaptadores mecânicos resolvem a conexão; a integração final ainda depende de alimentação correta, pinagem, topologia e compatibilidade entre os equipamentos envolvidos.

**Posso usar cabo Ethernet Cat5 como backbone NMEA 2000?**

Tecnicamente funciona em bancada, mas NÃO recomendado a bordo. O cabo certificado N2K tem blindagem específica e resistência a ambiente marinho.

**Qual a velocidade máxima de update no NMEA 0183?**

A 4800 baud, uma sentence $GPGGA leva ~200ms — atualização máxima ~5Hz. A 38400 baud (High Speed), até 20Hz. NMEA 2000 suporta até 100Hz em alguns PGNs.

**Como saber se meu backbone N2K está com problema?**

Com um multímetro: medir resistência entre CAN+ e CAN- (rede desligada) → deve ser ~60Ω. Se for 120Ω falta um terminador. Se for <60Ω tem curto ou dispositivo com problema.

## Visual didático

![NMEA 2000: backbone e drops](../_visuals/generated/nmea-backbone-drops.svg)

Mostrar NMEA 2000 como rede estruturada, nao como extensao livre de cabos.

**Cautela:** Comprimentos, topologia e carga de rede devem seguir especificacoes NMEA e manuais dos fabricantes.

Material de apoio: [NMEA 2000: backbone e drops](../_visuals/generated/nmea-backbone-drops.md)

## Glossário rápido

| Termo | Significado |
| --- | --- |
| **Sentence** | Linha ASCII NMEA 0183 começando com `$` (ex.: `$GPGGA`) |
| **PGN** | Parameter Group Number — pacote binário NMEA 2000 identificado por número (ex.: 127250 = heading) |
| **Talker** | Dispositivo que **transmite** dados na rede (GPS, anemômetro, sonda) |
| **Listener** | Dispositivo que **recebe** dados (chartplotter, piloto, VHF) |
| **Backbone** | Cabo principal da rede N2K, com terminadores nas duas pontas |
| **Drop** | Cabo curto (≤ 6 m) que liga um dispositivo ao backbone via tee |
| **Tee** | Conector em "T" (Micro-C) que insere drops no backbone |
| **Power tap** | Componente que injeta 12 V no backbone (com fusível 3 A) |
| **Terminador** | Resistor 120 Ω plugado em cada extremidade do backbone |
| **LEN** | Load Equivalency Number — quantos "amperes-equivalentes" um dispositivo consome do backbone (cada LEN ≈ 50 mA) |
| **NAME** | Identificador único de 64 bits que cada dispositivo N2K anuncia ao se conectar |
| **Gateway** | Bridge: 0183 ↔ 2000, ou N2K ↔ proprietário (Actisense NGT-1, Garmin GND 10) |
| **Multiplexer** | Combina vários talkers 0183 em uma única saída para um listener |
| **J1939** | Protocolo CAN para motores diesel pesados; precisa gateway dedicado para entrar no N2K |
| **SeaTalkNG** | Protocolo CAN proprietário Raymarine; base física compatível com N2K via adaptador |
| **SimNet** | Protocolo CAN proprietário Simrad/Lowrance; base física compatível com N2K via adaptador |
| **`$GPGGA`** | Posição GPS principal (lat, lon, qualidade do fix) |
| **`$GPRMC`** | Posição + velocidade + data — sentence mínima exigida por DSC |
| **PGN 129025** | Position Rapid Update (N2K, ~10 Hz) |
| **PGN 127250** | Vessel Heading (N2K, ~10 Hz) — dado obrigatório para piloto automático |

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

- O que é NMEA 2000 / NMEA 0183 — Rede de Instrumentos em instalações elétricas náuticas?
- Qual é a função de NMEA 2000 / NMEA 0183 — Rede de Instrumentos na embarcação?

