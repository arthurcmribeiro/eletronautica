---
title: "Bússola Eletrônica (Compass / HDG Sensor)"
note_type: "component"
domain: "50_Navegacao_Instrumentacao_e_Comunicacao"
source_file: "BÚÓSSOLA ELETRÔNICA — COMPASS E HDG SENSOR 33a19734f7fb816c96d9ced8bfaa4859.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://www.nmea.org/standards.html"
  - "https://www.gov.br/anatel/pt-br/regulado/outorga/servico-movel-maritimo"
aliases:
  - "BÚÓSSOLA ELETRÔNICA — COMPASS E HDG SENSOR"
  - "Bússola Eletrônica (Compass / HDG Sensor)"
seo_title: "Bússola Eletrônica (Compass / HDG Sensor)"
seo_description: "BÚSSOLA ELETRÔNICA — Sensor que fornece o rumo magnético (heading) da embarcação ao piloto automático, chartplotter e demais instrumentos. Mais precisa e prática que."
seo_keywords:
  - "Bússola"
  - "Eletrônica"
  - "Compass"
  - "HDG"
  - "Sensor"
  - "50 Navegacao Instrumentacao e Comunicacao"
geo_queries:
  - "O que é Bússola Eletrônica (Compass / HDG Sensor) em instalações elétricas náuticas?"
  - "Qual é a função de Bússola Eletrônica (Compass / HDG Sensor) na embarcação?"
related_notes:
  - "AIS (Automatic Identification System)"
  - "Buzina"
  - "Chartplotter / GPS / MFD"
  - "Dsc — Chamada Seletiva Digital"
  - "EPIRB / Beacon de Emergência"
  - "Estação de Vento / Anemômetro"
  - "Mob — Man Overboard — Sistema de Detecção"
  - "NAVEGAÇÃO (BB, BE e Alcançado)"
---

# Bússola Eletrônica (Compass / HDG Sensor)

> [!abstract] Resumo técnico
> BÚSSOLA ELETRÔNICA — Sensor que fornece heading à arquitetura de navegação da embarcação. Complementa a bússola magnética tradicional e alimenta piloto automático, chartplotter, radar e demais sistemas, com desempenho dependente da tecnologia escolhida e da qualidade da instalação.

## O que é

Sensor eletrônico que mede o rumo magnético (heading) da embarcação em relação ao norte magnético. Substitui e complementa a bússola magnética convencional, fornecendo dados digitais que alimentam o piloto automático, chartplotter, radar e AIS.

Tipos disponíveis:

- **Fluxgate compass:** mede o campo magnético terrestre através de bobinas de núcleo de ferro. Tecnologia padrão há 30+ anos.
- **AHRS (Attitude and Heading Reference System):** usa acelerômetros e giroscópios MEMS + magnetômetro. Compensa pitch e roll dinamicamente.
- **GPS compass (dual antenna):** usa diferença de fase entre dois receptores GPS para calcular heading verdadeiro — independente de campo magnético.

## Função

- Fornecer rumo magnético preciso e estável para o piloto automático
- Exibir heading no chartplotter (overlay sobre carta)
- Permitir que o radar calcule orientação correta (north-up mode)
- Integrar ao VHF/DSC (heading da embarcação)
- Corrigir vento verdadeiro no instrumento de vento (precisa de HDG + SOG)
- Referência para cálculos de navegação eletrônica

## Como aparece na prática

Em lanchas: sensor fluxgate montado sob o painel principal ou na sentina, conectado ao piloto automático (é o sensor primário de heading do piloto). Mal posicionado → piloto "caça" o rumo sem estabilizar.

Em veleiros: fluxgate ou AHRS montado no mastro ou meia-embarcação, longe de motores e alto-falantes. Integrado à rede NMEA 2000.

Em embarcações premium: GPS compass de dupla antena (sem interferência magnética, heading verdadeiro).

## Fundamentos mínimos

| Parâmetro | Fluxgate | AHRS | GPS Compass |
| --- | --- | --- | --- |
| Precisão heading | ±1–2° | ±0.5–1° | ±0.5° |
| Sensível a metais | Sim | Sim (magnetômetro) | Não |
| Compensa movimento | Parcial | Total (pitch/roll) | Não precisa |
| Velocidade de update | 10–20 Hz | 10–100 Hz | 10 Hz |
| Custo relativo | Baixo | Médio | Alto |
| Interferência magnética | Alta sensibilidade | Alta sensibilidade | Imune |
| NMEA saída | 0183 / N2K | 0183 / N2K | 0183 / N2K |

## Características

**Fluxgate:**

- Núcleo de ferro envolto em bobinas detecta componentes do campo magnético
- Sensível à distância de metais ferrosos, alto-falantes e equipamentos elétricos
- Deve ser instalado longe de motores, baterias, inversores e falantes
- Afastamentos mínimos devem seguir o manual do fabricante e, idealmente, ser confirmados por levantamento prático de interferência magnética no ponto de instalação
- Requer calibração de desvio (swinging the compass) após instalação

**AHRS:**

- Combina magnetômetro + acelerômetro + giroscópio
- Compensa dinamicamente a inclinação da embarcação (pitch/roll)
- Mais preciso em mar agitado (sonda menos headings erráticos)
- Menor influência de perturbações transitórias
- Custo 2–4x maior que fluxgate

**GPS Compass:**

- Usa diferença de fase entre 2 antenas GPS separadas (base ~1m)
- Fornece heading verdadeiro (não magnético) — sem declinação
- Imune a interferências magnéticas
- Requer visibilidade de satélites (não funciona dentro de garagem ou sob cobertura metálica)
- Custo alto (Simrad HS70, Garmin GPS 19x HVS, Furuno SC-50)

## Configurações comuns

```jsx
Configuração básica (fluxgate):
Sensor fluxgate → cabo blindado → controlador do piloto automático
(heading também distribuído via NMEA 0183 → chartplotter)

Configuração NMEA 2000:
AHRS → Micro-C drop → backbone N2K → piloto + chartplotter + radar

Configuração premium:
GPS Compass → NMEA 2000 → todos os instrumentos (heading verdadeiro)
```

## Marcas e modelos

| Marca | Modelo | Tipo | Observação |
| --- | --- | --- | --- |
| **Garmin** | GPS 19x HVS | GPS Compass | Alta precisão, N2K |
| **Simrad** | HS70 | GPS Compass | Integra com AP |
| **Furuno** | SC-50 | GPS Compass | Referência offshore |
| **B&G** | Precision 9 | AHRS | Veleiros, excelente |
| **Raymarine** | EV-1 | AHRS | Integrado ao EV autopilot |
| **Garmin** | GMC 010 | Fluxgate | NMEA 2000 |
| **Simrad** | RC42N | Fluxgate | Comum em AP Simrad |
| **ComNav** | G2/G2B | GPS Compass | Custo-benefício |

**No Brasil:** Fluxgate Simrad/Garmin é o mais comum. GPS Compass presente em embarcações maiores ou offshore.

## Componentes relacionados

- **Piloto automático:** principal consumidor do dado de heading
- **Chartplotter/MFD:** exibe heading e calcula vento verdadeiro
- **Radar:** usa heading para modo north-up e course-up
- **AIS:** heading da embarcação integrado ao transponder
- **NMEA 2000/0183:** rede de distribuição do dado
- **Sensor de velocidade (log):** junto com heading calcula dead reckoning

## Problemas mais frequentes

| Problema | Causa raiz provável |
| --- | --- |
| Piloto caça (oscila) sem estabilizar | Sensor perturbado por metal próximo, calibração errada |
| Heading errado em relação ao norte real | Desvio magnético não calibrado (swinging) |
| Heading treme em mar agitado | Fluxgate sem compensação de roll (usar AHRS) |
| Sensor não aparece no NMEA | Baud rate errado, TX/RX invertido, fio partido |
| Heading varia ao ligar motor | Motor/alternador perturbando campo magnético |
| Heading varia ao ligar alto-falante | Alto-falante próximo ao sensor (campo magnético permanente) |

## Causas raiz

**Perturbação magnética próxima:** é uma das causas mais comuns de erro. Alto-falantes, motores, cabos de alta corrente, massas metálicas e rearranjos de equipamentos podem degradar severamente o heading se o sensor for instalado sem estudo do local.

**Calibração não feita:** após instalação, o sensor precisa ser "girado" (swinging) para mapear o desvio em cada rumo. Sem isso, há erros sistemáticos que variam com a direção.

**Embarcação de aço ou alumínio:** perturbação muito maior. Sensor deve ser posicionado no ponto de menor influência e a calibração é mais crítica.

## Diagnóstico prático

```jsx
Passo 1: Comparar leitura eletrônica com bússola magnética convencional (rumo estável)
Passo 2: Se diferença >5° → suspeitar de desvio não calibrado
Passo 3: Verificar distância de metais e alto-falantes (mínimo 60cm)
Passo 4: Fazer calibração completa (seguir procedimento do fabricante — geralmente girar 360°)
Passo 5: Se tremendo em mar agitado → considerar upgrade para AHRS
Passo 6: Verificar comunicação NMEA (sentences $IIHDG, $IIHDM ou PGN 127250)
```

## Boas práticas profissionais

- Instalar o sensor em local sem vibração excessiva (longe do motor)
- Orientar o sensor conforme marcação do fabricante (horizontal ±10° máximo para fluxgate)
- Usar cabo blindado (reduz interferência do alternador)
- Sempre fazer calibração após instalação e após qualquer modificação elétrica a bordo
- Documentar o valor de desvio residual após calibração

## Cuidados de instalação

- Respeitar os afastamentos e restrições de instalação definidos pelo fabricante para metais ferrosos, alto-falantes, motores e cabos de potência
- Horizontal dentro de ±10° para fluxgate (AHRS aceita mais inclinação)
- Usar calço de material não ferroso (fibra, acrílico, alumínio)
- Passar o cabo longe de cabos de alta corrente DC

## Cuidados de uso

- Refazer calibração se instalar novos equipamentos elétricos próximos ao sensor
- Refazer calibração se trocar motor ou mover baterias
- Em regatas ou navegação de precisão: verificar calibração anualmente
- Em embarcações com gerador: verificar se ligar o gerador altera o heading

## Erros comuns de instaladores

- Instalar próximo ao alto-falante do rádio VHF (causa clássica de heading errático)
- Não fazer calibração após instalação
- Usar suporte de aço inox ferromagnético (o inox magnético perturba o sensor)
- Instalar inclinado em mais de 10° (fluxgate perde precisão)
- Passar cabo de heading junto com cabo de bateria (interferência)

## Relação com outros sistemas

- **Piloto automático:** heading é o dado mais crítico — sem heading preciso, piloto não funciona bem
- **Chartplotter:** usa heading para orientation do barco no mapa
- **Radar:** heading para north-up / course-up display
- **AIS:** transmite heading no Voyage Data com dado do sensor
- **Vento verdadeiro:** calculado com AWA + HDG + SOG (três dados juntos)

## Brasil x Internacional

| Aspecto | Brasil | Internacional |
| --- | --- | --- |
| Tecnologia dominante | Fluxgate | AHRS crescendo rápido |
| GPS Compass | Raro | Presente em lanchas >40' |
| Calibração pós-instalação | Frequentemente ignorada | Feita como protocolo |
| Awareness sobre perturbação magnética | Baixo | Maior |
| Norma de instalação | Sem norma específica | ABYC E-11 (wiring) |

**Muito comum no Brasil:** Fluxgate Simrad RC42 ou Garmin GMC 010 em lanchas de 25–40'.

**Mais presente em embarcações maiores/premium:** AHRS B&G Precision 9, GPS Compass Furuno SC-50.

## Normas e referências

- **ABYC E-11:** wiring e instalação de eletrônicos
- **IEC 60945:** Marine navigation equipment
- **NMEA 2000 PGN 127250:** Vessel Heading
- **NMEA 0183 $IIHDG / $IIHDM:** Heading sentences
- **ISO 11606:** Marine navigation — compass requirements

## Como ensinar este tópico

**Sequência recomendada:**

1. Mostrar como a bússola magnética funciona (campo magnético terrestre)
2. Explicar por que o fluxgate perturba com metais (usando exemplo visual com imã)
3. Demonstrar procedimento de calibração (swinging) no equipamento real
4. Mostrar diferença de heading antes/depois da calibração
5. Comparar fluxgate vs AHRS em embarcação com mar agitado

**Analogia útil:** "O fluxgate é como uma bússola supersensível — funciona muito bem, mas qualquer imã perto confunde. O AHRS é como ter GPS de heading — não se importa com imãs, usa física inercial."

## Ideias de vídeos

- "Por que o piloto automático 'caça'? Diagnóstico de heading"
- "Calibrando bússola eletrônica passo a passo"
- "Fluxgate vs AHRS vs GPS Compass: qual escolher?"
- "Onde NÃO instalar a bússola eletrônica — erros comuns"
- "Integrando heading ao chartplotter via NMEA 2000"

## Diagramas sugeridos

- Diagrama de instalação: posicionamento do sensor em relação a metais e equipamentos
- Fluxo NMEA: heading sensor → piloto AP → chartplotter → radar → AIS
- Comparativo de precisão: fluxgate vs AHRS em mar agitado (gráfico de heading ao longo do tempo)
- Diagrama de calibração: trajetória circular para swinging do compass
- Mapa de perturbação magnética em uma embarcação típica

## FAQ

**Preciso de bússola eletrônica se tenho GPS?**

Sim. O GPS fornece COG (course over ground), não heading. São diferentes — especialmente quando a embarcação está em corrente ou com vento de través.

**AHRS vale o investimento?**

Para piloto automático em embarcações que navegam offshore ou em águas com ondas: sim, claramente. A estabilidade de heading em mar agitado melhora muito o desempenho do piloto.

**O inox perturba o sensor?**

Depende. Inox 316 (não magnético) — perturbação mínima. Inox 304 em algumas ligas — pode ser ligeiramente magnético. Aço carbono — perturba muito. Teste com imã: se prender, é magnético.

**Posso usar a bússola da carta náutica para comparar?**

Sim, é a forma mais simples de verificar o desvio. Em águas calmas e com rumo estável, comparar a leitura eletrônica com a bússola convencional.

**Com GPS Compass, preciso calibrar?**

Não da mesma forma. O GPS Compass não depende do campo magnético — sem swinging. Mas precisa de alinhamento correto das duas antenas (alinhadas com o eixo de proa-popa).

## Integração com outras notas

- [[AIS (Automatic Identification System)]]
- [[Buzina]]
- [[Chartplotter / GPS / MFD]]
- [[Dsc — Chamada Seletiva Digital]]
- [[EPIRB / Beacon de Emergência]]
- [[Estação de Vento / Anemômetro]]
- [[Mob — Man Overboard — Sistema de Detecção]]
- [[NAVEGAÇÃO (BB, BE e Alcançado)]]

## Perguntas que esta nota responde

- O que é Bússola Eletrônica (Compass / HDG Sensor) em instalações elétricas náuticas?
- Qual é a função de Bússola Eletrônica (Compass / HDG Sensor) na embarcação?
