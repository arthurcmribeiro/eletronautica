---
title: "Radar"
note_type: "technical-note"
domain: "50_Navegacao_Instrumentacao_e_Comunicacao"
source_file: "RADAR 0f919734f7fb83d4a90e81c518fd4608.md"
status: "technical-review-l1"
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

- **COLREGS** — obriga a uso de todos os meios disponíveis para evitar colisão — radar quando disponível
- **SOLAS** — obrigatório em embarcações comerciais de porte (referência)
- **Manual do fabricante** — instalação e calibração

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
