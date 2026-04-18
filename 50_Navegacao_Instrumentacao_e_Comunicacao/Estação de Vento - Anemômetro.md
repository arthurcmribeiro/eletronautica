---
title: "Estação de Vento / Anemômetro"
note_type: "technical-note"
domain: "50_Navegacao_Instrumentacao_e_Comunicacao"
source_file: "ESTAÇÃO DE VENTO ANEMÔMETRO 33a19734f7fb81259cdac88a695c2ae9.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://www.nmea.org/standards.html"
  - "https://www.gov.br/anatel/pt-br/regulado/outorga/servico-movel-maritimo"
aliases:
  - "ESTAÇÃO DE VENTO ANEMÔMETRO"
  - "ESTAÇÃO DE VENTO / ANEMÔMETRO"
seo_title: "Estação de Vento / Anemômetro"
seo_description: "ESTAÇÃO DE VENTO / ANEMÔMETRO — Instrumento que mede velocidade e direção do vento. Essencial em veleiros e embarcações de pesca offshore. Integra via NMEA ao chartp."
seo_keywords:
  - "Estação"
  - "Vento"
  - "Anemômetro"
  - "50 Navegacao Instrumentacao e Comunicacao"
geo_queries:
  - "O que é Estação de Vento / Anemômetro em instalações elétricas náuticas?"
  - "Qual é a função de Estação de Vento / Anemômetro na embarcação?"
related_notes:
  - "AIS (Automatic Identification System)"
  - "Buzina"
  - "Bússola Eletrônica (Compass / HDG Sensor)"
  - "Chartplotter / GPS / MFD"
  - "Dsc — Chamada Seletiva Digital"
  - "EPIRB / Beacon de Emergência"
  - "Mob — Man Overboard — Sistema de Detecção"
  - "NAVEGAÇÃO (BB, BE e Alcançado)"
---

# Estação de Vento / Anemômetro

> [!abstract] Resumo técnico
> ESTAÇÃO DE VENTO / ANEMÔMETRO — Instrumento que mede velocidade e direção do vento. Essencial em veleiros e embarcações de pesca offshore. Integra via NMEA ao chartplotter e piloto automático. Problemas elétricos são a principal causa de le.

## O que é

Anemômetro náutico é o conjunto sensor + display que mede:

- **Velocidade do vento** — em nós (kts), km/h ou m/s
- **Direção do vento** — em graus relativos à proa (vento aparente) ou como grandeza referenciada/derivada pelo sistema a partir de outras entradas de navegação

Dois tipos de vento medidos:

- **Vento aparente (AWA/AWS):** o que o sensor percebe fisicamente no topo do mastro
- **Vento verdadeiro (TWA/TWS):** grandeza derivada a partir do vento aparente e de outras variáveis de navegação, como heading, velocidade e referência de movimento, conforme a arquitetura do sistema

## Função

- Navegar com vela de forma eficiente (ponto de vela ideal)
- Segurança: alertas de rajada, risco de arriamento
- Pesca offshore: identificar condições operacionais
- Integração com piloto automático para navegação a vela automática
- Registro histórico de vento para análise de rota

## Como aparece na prática

Em veleiros: o anemômetro fica no topo do mastro (cima de tudo), conectado por cabo que desce pelo interior do mastro até o painel de instrumentos. Falha mais comum: oxidação dos contatos na base do mastro.

Em lanchas e barcos a motor: menos comum, mas presente em embarcações offshore de pesca, onde a leitura do vento ajuda a decidir sobre saída ou permanência no mar.

Em embarcações maiores: sistema de múltiplos sensores com redundância.

## Fundamentos mínimos

| Parâmetro | Detalhe |
| --- | --- |
| Alimentação | 12V DC tipicamente |
| Sinal | NMEA 0183 (serial) ou NMEA 2000 |
| Sensor de velocidade | Anemômetro de copo (cups) ou ultrassônico |
| Sensor de direção | Cata-vento (wind vane) ou ultrassônico |
| Faixa de velocidade | 0–60 kts típico / 0–100 kts premium |
| Precisão | ±2% velocidade / ±3° direção (bons modelos) |

## Características

**Sensor de copo (cup anemometer):**

- Mecanismo físico com 3 conchas rotativas
- Simples, confiável, barato
- Desvantagem: tem partes móveis sujeitas a desgaste
- Não funciona bem com vento muito fraco (<3 kts)

**Sensor ultrassônico:**

- Sem partes móveis — maior durabilidade
- Mede por tempo de propagação do som entre transdutores
- Mais preciso em velocidades baixas
- Custo 3–5x maior
- Presente em equipamentos premium (Garmin, B&G)

**Integração:**

- NMEA 0183 (sentences $IIMWV, $IIMWD) via RS-422 serial
- NMEA 2000 (PGN 130306 Wind Data)
- Wireless (RF 2.4GHz) em alguns modelos sem fio para mastro

## Configurações comuns

```jsx
Configuração básica (veleiro):
Sensor no topo do mastro → cabo interno → caixa de instrumento → display

Configuração integrada (NMEA 2000):
Sensor → backbone N2K → MFD/chartplotter → piloto automático (modo vela)

Configuração offshore (lancha):
Sensor no t-top ou antena principal → display na estação de comando
```

## Marcas e modelos

| Marca | Modelo | Tecnologia | Observação |
| --- | --- | --- | --- |
| **Garmin** | GMI 20 + GWS 10 | Cups | NMEA 2000, muito usada no Brasil |
| **B&G** | Triton2 + WS310 | Cups | Referência em veleiros |
| **Raymarine** | i70s + MastView | Cups | Integra com EV autopilot |
| **Simrad** | IS42 + WS310 | Cups | Linha IS |
| **Nexus** | NX2 | Cups | Clássico, ainda presente |
| **Calypso** | Ultrasonic | Ultrassônico | Sem fio, app Bluetooth |
| **Gill** | WindSonic | Ultrassônico | Industrial/premium |

**No Brasil:** Garmin e Simrad dominam lanchas. B&G é referência em veleiros.

## Componentes relacionados

- **MFD/Chartplotter:** recebe dados e exibe na tela
- **Piloto automático:** usa TWA/TWS para modo vela
- **Display de instrumento:** exibe leitura dedicada
- **Backbone NMEA 2000:** rede de distribuição dos dados
- **Mastro:** estrutura de passagem do cabo (veleiros)
- **GPS/HDG:** necessários para calcular vento verdadeiro

## Problemas mais frequentes

| Problema | Causa raiz provável |
| --- | --- |
| Leitura de velocidade zerada | Sensor travado, cabo partido, conector oxidado |
| Leitura errática ou oscilante | Cabo mal crimpado, interferência EMI, conector na base do mastro |
| Direção sempre errada | Sensor girado na instalação, calibração não feita |
| Sem comunicação NMEA | Baud rate errado (4800 vs 38400), fios invertidos TX/RX |
| Sensor fisicamente destruído | Marretadas de cabo de talha, objeto arremessado por rajada |
| Consumo alto anormal | Curto no cabo ao longo do mastro |

## Causas raiz

**Oxidação no conector da base do mastro:** ponto mais crítico. Conector exposto a água salgada, com correntes parasitas pelo mastro. Resistência de contato aumenta → leitura flutuante ou ausente.

**Cabo partido internamente:** dentro do mastro, o cabo flexiona toda vez que o mastro oscila. Em veleiros usados offshore, o cabo pode partir em 2–5 anos se for subqualidade.

**Calibração não feita:** instalação sem alinhamento do sensor à proa → direção sistematicamente desviada.

**Inversão TX/RX:** muito comum em instalações amadoras de NMEA 0183.

## Diagnóstico prático

```jsx
Passo 1: Verifique tensão na alimentação do sensor (12V ±0.5V)
Passo 2: Inspecione o conector na base do mastro (oxidação, pinos dobrados)
Passo 3: Teste resistência do cabo (ohmímetro entre sensor e painel)
Passo 4: Verifique comunicação no terminal NMEA (monitor serial 4800 baud)
Passo 5: Compare leitura com vento percebido manualmente
Passo 6: Faça calibração de offset de direção conforme manual
```

**Ferramenta útil:** monitor serial (laptop com Putty ou app de celular NMEA Monitor) — permite ver as sentences NMEA brutas e confirmar se o sensor está transmitindo.

## Boas práticas profissionais

- Usar cabo blindado específico para instrumento (Belden ou similar) — reduz interferência
- Cravar conector da base do mastro com vedação (dielectric grease + fita autovulcanizante)
- Respeitar afastamentos mecânicos e eletromagnéticos recomendados pelo fabricante em relação a antenas, mastreação e outros equipamentos
- Fazer calibração de offset logo após a instalação com vento estável
- Documentar baud rate e wiring no diário de bordo elétrico

## Cuidados de instalação

- Orientar o sensor com a referência correta em relação à proa
- Fixar cabo com clips no interior do mastro a cada 60cm (evita vibração e atrito)
- Usar cabo de aço inox para içamento do sensor dentro do mastro (não cordão de nylon)
- Fazer furo de passagem pelo convés com bucim estanque apropriado
- Proteger o conector externo do mastro com capa de borracha ou similar

## Cuidados de uso

- Em rajadas extremas (>60 kts): sensor de copo pode ser danificado — confirmar especificação do fabricante
- Não escalar o mastro sem desligar a alimentação do sensor
- Inspecionar o sensor a cada temporada (giro suave das conchas, sem folga na cata-vento)
- Seguir o procedimento de limpeza e lubrificação especificado pelo fabricante; muitos sensores modernos não devem receber lubrificantes genéricos

## Erros comuns de instaladores

- Não calibrar o offset de direção após instalação
- Usar cabo não blindado (induz leitura errática)
- Deixar conector da base do mastro sem proteção contra água
- Instalar o sensor próximo de antenas (interferência em ultrassônico)
- Inverter TX/RX no NMEA 0183 (instrumento não aparece no chartplotter)
- Não travar o parafuso de fixação do sensor → sensor gira com o vento

## Relação com outros sistemas

- **Piloto automático:** usa vento aparente para modo vela (sail mode) — sem anemômetro, não há modo vela
- **Chartplotter/MFD:** exibe Wind Rose, True Wind overlay no mapa
- **NMEA 2000/0183:** protocolo de transmissão dos dados
- **GPS:** fornece COG/SOG para calcular vento verdadeiro a partir do aparente
- **Bússola/Heading:** necessário para cálculo de vento verdadeiro

## Brasil x Internacional

| Aspecto | Brasil | Internacional |
| --- | --- | --- |
| Uso em veleiros | muito recomendado | amplamente adotado |
| Uso em lanchas | Raro, só offshore | Mais comum (EUA/Europa) |
| Tecnologia dominante | Cups (mecânico) | Ultrassônico crescendo |
| Norma de instalação | Sem norma específica | ABYC E-11 (2023) (wiring) |
| Certificação do sensor | Não exigida | CE Mark Europa |
| Manutenção | Raramente feita | Inspecionado anualmente |

**Muito comum no Brasil:** B&G em veleiros de regata, Garmin em lanchas offshore de pesca.

**Mais presente em embarcações maiores/premium:** sistemas ultrassônicos integrados com redundância.

## Normas e referências

- **ABYC E-11 (2023):** Wiring standards (cableamento do sensor)
- **IEC 60945 (edição a verificar):** Marine navigation equipment (standard de construção)
- **NMEA 0183 v4.10:** Sentences MWV, MWD para wind data
- **NMEA 2000 PGN 130306:** Wind Data (speed + angle)
- **NMEA 2000 PGN 130310:** Environmental parameters

## Como ensinar este tópico

**Sequência recomendada:**

1. Mostrar sensor físico — tipos de copo e cata-vento
2. Explicar vento aparente vs verdadeiro (diagrama vetorial)
3. Demonstrar leitura NMEA no terminal serial
4. Prática de calibração de offset
5. Simulação de falha: desconectar fio TX e ver resultado no display

**Analogia útil:** "O anemômetro é como o velocímetro e bússola do vento — sem ele, você navega a vela no escuro."

## Ideias de vídeos

- "Como instalar anemômetro no mastro passo a passo"
- "Por que minha leitura de vento oscila? Diagnóstico completo"
- "Vento aparente vs vento verdadeiro: diferença que todo velejador precisa entender"
- "NMEA 0183: conectando o anemômetro ao chartplotter"
- "Inspecionando e trocando sensor de vento em veleiro"

## Diagramas sugeridos

- Diagrama de fiação: sensor → conector mastro → display/MFD (com identificação de cada fio)
- Vetor: cálculo de vento verdadeiro (TWA/TWS) a partir de AWA/AWS + HDG + SOG
- Fluxo NMEA 2000: sensor → backbone → múltiplos instrumentos
- Foto real: conector oxidado na base do mastro (antes/depois da limpeza)
- Diagrama de calibração: offset de direção em relação à proa

## FAQ

**O sensor de copo precisa de lubrificação?**

Não use óleos. Apenas PTFE seco se necessário. Graxa ou WD-40 atraem sujeira e podem emperrar.

**Posso usar o anemômetro sem display dedicado?**

Sim — se tiver NMEA 2000, o chartplotter exibe os dados. Display dedicado é mais prático para navegação a vela em tempo real.

**Qual a diferença entre vento aparente e verdadeiro na prática?**

Aparente é o que o sensor mede fisicamente. Verdadeiro é calculado considerando que a embarcação está em movimento. Para a vela, trabalha-se com aparente. Para meteorologia e segurança, usa-se verdadeiro.

**O sensor sem fio (wireless) é confiável?**

Modelos como Calypso Ultrasonic funcionam bem, mas têm bateria no sensor (trocar a cada 1–2 anos) e podem sofrer interferência de outros equipamentos RF a bordo.

**Instalei mas a direção está sempre 30° errada — o que faço?**

É offset de instalação. O sensor não foi alinhado perfeitamente à proa. Corrija via calibração no menu do instrumento (maioria dos fabricantes permite ajuste de ±180°).

## Integração com outras notas

- [[AIS (Automatic Identification System)]]
- [[Buzina]]
- [[Bússola Eletrônica (Compass / HDG Sensor)]]
- [[Chartplotter / GPS / MFD]]
- [[Dsc — Chamada Seletiva Digital]]
- [[EPIRB / Beacon de Emergência]]
- [[Mob — Man Overboard — Sistema de Detecção]]
- [[NAVEGAÇÃO (BB, BE e Alcançado)]]

## Perguntas que esta nota responde

- O que é Estação de Vento / Anemômetro em instalações elétricas náuticas?
- Qual é a função de Estação de Vento / Anemômetro na embarcação?
