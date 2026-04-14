---
title: "Piloto Automático"
note_type: "technical-note"
domain: "50_Navegacao_Instrumentacao_e_Comunicacao"
source_file: "PILOTO AUTOMÁTICO 4b019734f7fb826ebeac810548e8c64d.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://www.nmea.org/standards.html"
  - "https://www.gov.br/anatel/pt-br/regulado/outorga/servico-movel-maritimo"
aliases:
  - "PILOTO AUTOMÁTICO"
seo_title: "Piloto Automático"
seo_description: "PILOTO AUTOMÁTICO (AUTOPILOT) — Sistema que controla automaticamente o leme para manter um rumo definido. Atuador (linear ou rotativo) move o leme; computador corrig."
seo_keywords:
  - "Piloto"
  - "Automático"
  - "50 Navegacao Instrumentacao e Comunicacao"
geo_queries:
  - "O que é Piloto Automático em instalações elétricas náuticas?"
  - "Qual é a função de Piloto Automático na embarcação?"
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

# Piloto Automático

> [!abstract] Resumo técnico
> PILOTO AUTOMÁTICO (AUTOPILOT) — Sistema que controla automaticamente o leme para manter um rumo definido. Atuador (linear ou rotativo) move o leme; computador corrige desvios. Corrente: 2–20A dependendo do tamanho do barco e das condições.

## O que é

O piloto automático é um sistema de controle de leme que mantém a embarcação em um rumo definido automaticamente, sem intervenção contínua do piloto humano. É composto por: sensor de rumo (compass), computador de controle (pilot computer), atuador de leme (linear ou rotativo) e interface de controle (remoto).

Em sua forma mais integrada, recebe dados de GPS (para manter rota, não só rumo), vento (para veleiros) e NMEA 2000 para integração total com o sistema de navegação.

## Função na embarcação

- Manter o rumo definido sem intervenção contínua do timoneiro
- Liberar o piloto para observação, navegação e tarefas a bordo
- Reduzir fadiga em navegações longas
- Em versões avançadas: seguir rota automaticamente (GPS track)
- Em veleiros: manter ângulo de vento (wind vane mode)

## Como aparece na prática

**Muito comum no Brasil:**

- Raymarine ST60/ST70 em veleiros de cruzeiro nacionais
- Simrad AP70 em lanchas de pesca esportiva
- Garmin GHP 12 em embarcações de médio porte

**Comum em barcos importados:**

- Sistemas integrados ao MFD (Garmin, Simrad, Raymarine) com controle na tela
- Atuador linear na barra do leme ou atuador rotativo na coluna
- Sensor AHRS (Attitude and Heading Reference System) para melhor desempenho em mar

**Mais presente em embarcações maiores/premium:**

- Piloto automático de alta potência com bomba hidráulica dedicada
- Integração NMEA 2000 com chartplotter, sonda e instrumentos de vento
- Controle remoto sem fio e múltiplos pontos de controle (fly bridge + helm)

## Fundamentos mínimos

**Sensor de heading (fluxgate compass):** Detecta a direção do campo magnético terrestre para determinar o rumo magnético. Sensível a interferências de motores, alto-falantes e massas metálicas próximas — instalação em local adequado é crítica.

**AHRS (Attitude and Heading Reference System):** Sensor mais moderno que combina bússola, acelerômetro e giroscópio. Compensa movimento do casco (pitch, roll) para heading mais estável — melhor desempenho em mar agitado.

**Ganho PID (Proportional-Integral-Derivative):** O algoritmo de controle que determina quão agressivamente o piloto corrige desvios. Mal calibrado = leme oscilando constantemente (serpentear) ou lento para corrigir (deriva).

**Modos de operação:**

- **Heading mode:** Mantém rumo magnético fixo
- **Track mode:** Segue rota GPS (corrente e vento são compensados)
- **Wind mode (veleiros):** Mantém ângulo relativo ao vento
- **Standby:** Piloto desativado, controle manual

**Atuador linear vs. rotativo:**

- Linear: barra de tração que atua sobre o braço do leme; aplicação depende de carga de leme, geometria, deslocamento e recomendação do fabricante
- Rotativo: acoplado à coluna de direção — para sistemas de volante
- Hidráulico: para embarcações maiores com direção hidráulica

## Características principais

| Parâmetro | Barcos < 12m | Barcos 12–18m | Barcos > 18m |
| --- | --- | --- | --- |
| Atuador | Linear 12V | Linear ou rotativo 12/24V | Hidráulico 24V |
| Corrente típica | 2–5A | 5–12A | 10–25A |
| Corrente de pico | 15–30A | 25–50A | 50–100A+ |
| Torque | Baixo–médio | Médio–alto | Alto |
| Autonomia por hora | 5–15Ah | 15–40Ah | 40–100Ah+ |

## Configurações e variações comuns

**Sistema linear básico (< 40 pés)**

- Atuador linear com curso de 200–300mm
- Computador de bordo com sensor fluxgate
- Controle por remoto ou painel
- Garmin GHP 12, Simrad AP44, Raymarine EV-1

**Sistema rotativo (volante)**

- Motor rotativo acoplado à coluna do volante
- Acionamento direto, instalação mais simples
- Simrad RPU80, Garmin GHP 12R

**Sistema hidráulico (> 40 pés)**

- Bomba hidráulica DC com reservatório
- Cilindro hidráulico no sistema de direção
- Alta força, necessário para embarcações pesadas
- Garmin GHP Reactor, Simrad AP70 + bomba hidráulica

**Integração total com MFD**

- Piloto controlado pelo chartplotter (enviar rota e ativar autopiloto direto)
- Garmin Reactor, Simrad AP70 com NMEA 2000
- Alertas de desvio de rota no MFD

## Principais marcas

- **Garmin** — GHP 12 e Reactor, boa integração GPSMAP, suporte no Brasil
- **Simrad** — AP44, AP70, referência em veleiros e embarcações profissionais
- **Raymarine** — Evolution e SmartPilot, popular em veleiros europeus
- **Furuno** — pilotos profissionais de alta durabilidade
- **Navico/B&G** — WTP1, especialidade em veleiros de regata e cruzeiro

## Componentes e sistemas relacionados

- **Sensor de heading (fluxgate ou AHRS)** — o componente mais crítico de precisão
- **Computador/controlador** — processamento e algoritmo PID
- **Atuador** — linear, rotativo ou hidráulico
- **Remoto de controle** — interface do operador
- **NMEA 2000** — integração com GPS, vento e MFD
- **Banco de bateria** — corrente de pico significativa em mar agitado
- **Disjuntor dedicado** — corrente de pico justifica proteção própria

## Onde costuma dar problema

| Problema | Sintoma | Causa |
| --- | --- | --- |
| Serpentear constante | Leme oscila de um lado ao outro | Ganho muito alto, sensor de heading com interferência |
| Deriva de rumo | Barco vai desviando gradualmente | Ganho muito baixo, sensor mal calibrado |
| Piloto desativa sozinho | "Piloto desligado" sem motivo | Queda de tensão, disjuntor disparando por pico |
| Sem resposta do atuador | Piloto ativo mas leme não move | Atuador travado, falha mecânica, corrente insuficiente |
| Heading errado | Rumo indicado ≠ rumo real | Sensor de heading com interferência ou mal calibrado |

## Causas raiz

**Serpentear constante:**

- Ganho (sea state) muito alto para as condições — piloto supercompensando
- Sensor fluxgate muito próximo ao motor ou ao alto-falante (interferência magnética)

**Piloto desativa por queda de tensão:**

- Banco insuficiente para o pico de corrente em mar agitado
- Cabo de alimentação fino para a corrente de pico

**Heading errado:**

- Sensor de heading instalado próximo a objetos magnéticos (motores, alto-falantes, âncora)
- Desvio magnético do casco não compensado (calibração obrigatória)
- Sensor necessita recalibração após rearranjo de equipamentos

**Causa raiz mais comum:** Instalação sem calibração completa + ganho não ajustado às condições reais de uso.

## Diagnóstico prático

**Passo 1:** Serpentear → reduzir ganho (sea state/gain). Se melhora: era o ganho. Se não: verificar sensor de heading.

**Passo 2:** Desliga sozinho → verificar tensão e queda de tensão no ponto de alimentação durante uso ativo. Queda relevante em relação ao nominal indica limitação de banco, cabeamento, conexões ou proteção.

**Passo 3:** Heading errado → afastar a embarcação de estruturas metálicas, calibrar o sensor (seguir protocolo do fabricante — geralmente círculos lentos em 360°).

**Passo 4:** Sem resposta do atuador → verificar corrente no atuador. Medir com alicate amperímetro. Atuador bloqueado = alta corrente sem movimento.

## Boas práticas

- Instalar o sensor de heading conforme o afastamento mínimo e o levantamento de interferências recomendados pelo fabricante
- Calibrar o sensor após instalação e repetir após qualquer mudança de equipamentos
- Ajustar o ganho (sea state) para as condições reais de uso — não deixar no padrão de fábrica
- Disjuntor de alta corrente dedicado ao piloto automático
- Dimensionar alimentação, proteção e retorno para os picos reais do atuador e para o ciclo de serviço esperado em mar formado
- Testar o botão de desativação de emergência (standby) antes de cada uso

## Erros comuns

❌ **Sensor de heading próximo ao motor** — interferência magnética causa erro de rumo

❌ **Sem calibração após instalação** — erro sistemático de rumo desde o início

❌ **Cabo de alimentação fino** — piloto desativa em pico de corrente

❌ **Ganho padrão de fábrica** — não adequado para as condições reais do barco

❌ **Sem verificação de standby** — em emergência, o operador não sabe como desligar rapidamente

❌ **Confiar cegamente no piloto sem vigília** — piloto automático requer vigilância permanente

## Relação com outros sistemas

- **Chartplotter/MFD** — integração de rota (track mode)
- **NMEA 2000** — dados de vento (veleiros), GPS, instrumentos de navegação
- **Banco de bateria** — corrente de pico significativa
- **Sistema de direção** — integração mecânica do atuador
- **VHF** — comunicação quando o piloto mantém o rumo

## Brasil x referências internacionais

### Prática comum no Brasil

Piloto automático comum em lanchas de pesca esportiva e veleiros de cruzeiro. Raro em lanchas de passeio < 35 pés. Calibração frequentemente ignorada.

### Referência internacional

Piloto automático considerado equipamento padrão em qualquer embarcação de cruzeiro. Treinamento de operação e calibração rigorosa.

### Leitura equilibrada

Para cruzeiros costeiros de dia: piloto automático aumenta conforto e segurança (piloto disponível para observação). Para navegação noturna ou offshore: é equipamento de segurança — a fadiga do timoneiro é uma das principais causas de acidentes em longas travessias.

## Normas e referências aplicáveis

- **COLREGS** — obriga vigilância permanente — piloto automático não substitui o operador
- **Manual do fabricante** — calibração e ajuste de ganho (documento essencial)
- **ABYC E-11** — proteção e bitola do circuito

## Destaques para ensino

- Como funciona o controle PID: proporção, integral e derivada no contexto do piloto
- Sensor de heading: por que a posição é tão crítica quanto a qualidade
- Calibração: o procedimento obrigatório que todos ignoram
- Ganho vs. condições de mar: como ajustar na prática
- O piloto automático não navega — apenas mantém o rumo ou a rota

## FAQ

**Posso deixar o piloto no leme e descansar?**

Não — COLREGS exige vigília permanente. O piloto mantém o rumo, mas não desvia de obstáculos, outras embarcações ou condições meteorológicas. Alguém deve estar sempre observando.

**Por que o barco serpenteia com o piloto ativo?**

Ganho muito alto ou sensor de heading com interferência. Reduzir o ganho (sea state) é o primeiro ajuste.

**O piloto automático consume muito do banco?**

Em mar calmo: 2–5A (mínimo). Em mar agitado com muitas correções: 10–20A de média. Dimensionar o banco considerando 8–12h de navegação autônoma.

**Preciso de piloto automático se tenho um VHF e GPS?**

São sistemas independentes. Piloto automático é de controle de leme — os outros são de comunicação e navegação. São complementares, não substituíveis.

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

- O que é Piloto Automático em instalações elétricas náuticas?
- Qual é a função de Piloto Automático na embarcação?
