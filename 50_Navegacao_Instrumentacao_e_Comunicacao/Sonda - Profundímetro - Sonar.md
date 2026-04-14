---
title: "Sonda / Profundímetro / Sonar"
note_type: "technical-note"
domain: "50_Navegacao_Instrumentacao_e_Comunicacao"
source_file: "SONDA PROFUNDÍMETRO SONAR 33a19734f7fb8168ae2befc62906f0a7.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://www.nmea.org/standards.html"
  - "https://www.gov.br/anatel/pt-br/regulado/outorga/servico-movel-maritimo"
aliases:
  - "SONDA PROFUNDÍMETRO SONAR"
  - "SONDA / PROFUNDÍMETRO / SONAR"
seo_title: "Sonda / Profundímetro / Sonar"
seo_description: "SONDA / PROFUNDÍMETRO / SONAR — Sistema que usa ondas ultrassônicas para medir a profundidade da água e localizar estruturas subaquáticas (peixes, fundo, vegetação)."
seo_keywords:
  - "Sonda"
  - "Profundímetro"
  - "Sonar"
  - "50 Navegacao Instrumentacao e Comunicacao"
geo_queries:
  - "O que é Sonda / Profundímetro / Sonar em instalações elétricas náuticas?"
  - "Qual é a função de Sonda / Profundímetro / Sonar na embarcação?"
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

# Sonda / Profundímetro / Sonar

> [!abstract] Resumo técnico
> SONDA / PROFUNDÍMETRO / SONAR — Sistema acústico para medir profundidade e interpretar ecos do meio subaquático. O desempenho depende do transdutor, da frequência/faixa utilizada, do processamento, da instalação e das condições hidrodinâmicas da embarcação.

## O que é

A sonda (depth sounder) ou profundímetro é o instrumento que mede a profundidade da água abaixo da embarcação usando o princípio do sonar — emissão de pulsos ultrassônicos e recepção do eco refletido no fundo. O tempo entre emissão e recepção determina a profundidade.

O sonar moderno vai além da simples profundidade: identifica a composição do fundo (areia, rocha, lama), localiza cardumes de peixe, detecta estruturas subaquáticas e, nas versões premium, gera imagens em alta resolução do fundo (CHIRP, Side Scan, DownScan).

## Função na embarcação

- Medir a profundidade da água para segurança de navegação (evitar encalhes)
- Localizar cardumes de peixe para pesca esportiva
- Identificar o tipo de fundo (relevante para ancoragem)
- Detectar obstáculos subaquáticos
- Em versões avançadas: criar mapa 3D do fundo (Garmin Quickdraw, Lowrance Genesis)

## Como aparece na prática

**Muito comum no Brasil:**

- Sonda integrada ao chartplotter Garmin/Lowrance
- Transdutor de popa (transom mount) em lanchas até 30 pés
- Frequência dupla 50/200 kHz
- Display numérico simples de profundidade em embarcações mais antigas

**Comum em barcos importados:**

- Transdutor de casco (in-hull ou thruhull) em embarcações maiores
- CHIRP sonar para imagem de alta resolução
- Integrado ao MFD via NMEA 2000

**Mais presente em embarcações maiores/premium:**

- Side Scan e DownVision para imagem lateral e vertical em alta resolução
- Transdutor de quilha em veleiros (sem intrusão no casco)
- Garmin Panoptix LiveScope para visão ao vivo em tempo real
- Furuno GP1971F com sonar de baixa frequência para grande profundidade

## Fundamentos mínimos

**Princípio do sonar:** O transdutor emite pulso ultrassônico; o eco retorna do fundo; o tempo de ida e volta × velocidade do som na água ÷ 2 = profundidade. Velocidade do som na água: ~1500 m/s (varia com temperatura e salinidade).

**Frequências:**

- **50 kHz:** geralmente favorece maior penetração e alcance em comparação com frequências mais altas, com menor resolução espacial
- **200 kHz:** geralmente favorece melhor definição em profundidades menores e médias, com menor alcance útil que frequências mais baixas
- **CHIRP:** Pulso de frequência variável — melhor resolução em maior profundidade, separação de ecos sobrepostos

**Transdutor:** O componente físico que converte sinal elétrico em onda sônica (piezoelétrico). Sua posição no casco é crítica — deve estar livre de turbulência de água e bolhas de ar.

**Tipos de transdutor:**

- **Transom mount:** Fixado na popa externamente — simples, acessível, sujeito a turbulência em alta velocidade
- **In-hull (shoot-through):** Colado internamente ao casco de fibra — sem furo no casco, mas perde sinal em alta velocidade e com casco espesso
- **Thruhull:** Atravessa o casco — melhor sinal, requer passacascos

## Características principais

| Parâmetro | Valor típico |
| --- | --- |
| Tensão | 12V DC |
| Corrente | 0,3–2A |
| Frequências | 50 kHz / 200 kHz / CHIRP |
| Alcance máximo | 10–600m (depende da frequência e do fundo) |
| Ângulo do cone | 10–60° (depende da frequência) |
| Velocidade máxima de leitura | depende fortemente da instalação do transdutor, do casco e da qualidade do escoamento no ponto de montagem |

## Configurações e variações comuns

**Sonda básica integrada ao chartplotter**

- Transdutor dupla frequência incluso na compra
- Exibe profundidade, temperatura, perfil do fundo
- Garmin GPSMAP com transdutor GT52 ou GT54

**CHIRP sonar de alta resolução**

- Pulso de frequência variável
- Imagem mais nítida, separação de ecos
- Garmin GPSMAP 8600 com transdutor GT56

**DownScan / DownVision**

- Feixe muito estreito apontado para baixo
- Imagem quase fotográfica do fundo
- Lowrance StructureScan, Humminbird Down Imaging

**Side Scan / SideVision**

- Varredura lateral do fundo (até 60–90m para cada lado)
- Mapeamento de área, localização de estruturas
- Ideal para pesca esportiva e inspeção de fundo

**Garmin Panoptix LiveScope**

- Imagem ao vivo em tempo real do que está abaixo e ao redor
- Revolução para pesca esportiva
- Visualiza peixes individuais se movendo em tempo real

## Principais marcas

- **Garmin** — líder de mercado no Brasil, ampla linha CHIRP e Panoptix
- **Lowrance** — forte em pesca esportiva, StructureScan 3D
- **Humminbird** — especialidade em sonar de alta resolução, MEGA Imaging
- **Furuno** — referência profissional, profundidade extrema, uso comercial
- **Simrad** — boa integração com sistemas de navegação maiores

## Componentes e sistemas relacionados

- **Chartplotter/MFD** — display dos dados de sonda
- **Transdutor** — sensor físico no casco
- **NMEA 2000** — comunicação dos dados de profundidade a outros instrumentos
- **Passacascos** — quando transdutor thruhull (ver requisitos de instalação)
- **Piloto automático** — pode receber alerta de profundidade em alguns sistemas
- **Ancoragem** — profundidade determina comprimento de cadeia a largar

## Onde costuma dar problema

| Problema | Sintoma | Causa |
| --- | --- | --- |
| Sem leitura acima de 15–20 nós | Profundidade "???" em alta velocidade | Bolhas de ar no transdutor (transom mount) |
| Leitura instável / errática | Profundidade pulsa sem sentido | Turbulência, transdutor mal posicionado |
| Sem ecos de peixe | Sonar lendo apenas o fundo | Ganho muito baixo ou frequência inadequada |
| Transdutor solto | Sem leitura + risco de entrada d'água | Fixação inadequada (transom mount) |
| Sonda não aparece no MFD | Sem comunicação | Cabo danificado, conector oxidado, N2K sem terminador |

## Causas raiz

**Sem leitura em alta velocidade:**

- Transdutor transom mount saindo da água ou preso em zona de bolhas de ar
- Solução: reposicionar o transdutor mais para dentro da popa, mais próximo da linha de centro

**Leitura errática:**

- Transdutor próximo ao motor ou à hélice — turbulência intensa
- Transdutor in-hull sobre stringer (reforço interno) — bloqueia o sinal

**Causa raiz:** Posicionamento do transdutor é a decisão mais crítica da instalação — e a mais ignorada.

## Diagnóstico prático

**Passo 1:** Sem leitura → verificar alimentação no conector do transdutor. Verificar continuidade do cabo.

**Passo 2:** Leitura instável → testar com embarcação parada (se estabilizar, problema de turbulência em velocidade).

**Passo 3:** Transdutor transom mount perdendo leitura em velocidade → mover o transdutor mais para dentro (mais próximo da quilha).

**Passo 4:** In-hull sem sinal → verificar se há reforço interno (stringer) abaixo do ponto de instalação. Testar enchendo o espaço com água (melhora o acoplamento acústico).

## Boas práticas

- Posicionar o transdutor longe da hélice, da quilha e de saídas de água
- Para transom mount: definir a posição após avaliar fluxo d'água, turbulência, proximidade da hélice, strakes e geometria do espelho
- Para in-hull: usar gel acústico ou água no alojamento para melhor acoplamento
- Ajustar offset de profundidade e parâmetros disponíveis no equipamento conforme o manual e a necessidade operacional da embarcação
- Ajustar o ganho do sonar conforme o tipo de fundo e profundidade

## Erros comuns

❌ **Transdutor próximo à hélice** — turbulência destrói a leitura em velocidade

❌ **Transdutor in-hull sobre stringer** — bloqueia o feixe sônico

❌ **Sem gel acústico in-hull** — ar entre o transdutor e o casco atenua o sinal

❌ **Cabo do transdutor com emenda não prevista pelo fabricante** — pode degradar sinal, vedação e confiabilidade do sistema

❌ **Ganho muito baixo** — sonar não detecta peixes nem fundo mole

## Relação com outros sistemas

- **Chartplotter/MFD** — display e integração principal
- **NMEA 2000** — profundidade para outros instrumentos
- **Piloto automático** — em sistemas avançados, recebe alerta de fundo raso
- **Âncora** — profundidade determina comprimento de cadeia

## Brasil x referências internacionais

### Prática comum no Brasil

Transdutor transom mount posicionado sem cuidado, sem teste de posição em velocidade, ganho na configuração padrão de fábrica.

### Referência internacional

Transdutor selecionado conforme uso (pesca, navegação, profissional), posicionado após testes, in-hull ou thruhull em embarcações médias+.

### Ponto de conflito

No Brasil, o uso de sonda é fortemente associado à pesca esportiva — a função de segurança de navegação (evitar encalhe) é subutilizada. Em muitas regiões com baixa profundidade (litoral nordestino, pantanal), a sonda é instrumento de segurança crítico.

## Normas e referências aplicáveis

- **Manual do fabricante** — instalação do transdutor (documento mais importante)
- **ABYC A-28** — thruhull fittings (quando transdutor thruhull)

## Destaques para ensino

- Princípio do sonar: o que é o eco e como se calcula a profundidade
- Frequência e resolução: 50 kHz vs. 200 kHz vs. CHIRP
- Posicionamento do transdutor: a decisão mais crítica da instalação
- Sonda como instrumento de segurança, não só de pesca

## FAQ

**Por que minha sonda não lê em alta velocidade?**

Bolhas de ar passando sobre o transdutor (transom mount). Reposicionar mais para o centro da popa ou usar transdutor in-hull.

**Qual a diferença entre profundímetro e sonar?**

Profundímetro: apenas a profundidade. Sonar: profundidade + imagem do fundo + localização de peixes + temperatura. Praticamente todos os equipamentos modernos são sonares completos.

**Posso instalar o transdutor sem tirar o barco da água?**

Para transom mount: sim. Para in-hull (colado): sim. Para thruhull: não — requer estaleiro com barco fora da água.

**Que profundidade a sonda alcança?**

Depende da frequência e do equipamento. 200 kHz: 100–200m. 50 kHz: 300–600m. CHIRP moderno de baixa frequência: > 1.000m em algumas configurações profissionais.

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

- O que é Sonda / Profundímetro / Sonar em instalações elétricas náuticas?
- Qual é a função de Sonda / Profundímetro / Sonar na embarcação?
