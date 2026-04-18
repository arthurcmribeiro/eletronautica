---
title: "Mob — Man Overboard — Sistema de Detecção"
note_type: "system"
domain: "50_Navegacao_Instrumentacao_e_Comunicacao"
source_file: "MOB — MAN OVERBOARD — SISTEMA DE DETECÇÃO 33a19734f7fb81db8ef6d25c8985db66.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://www.nmea.org/standards.html"
  - "https://www.gov.br/anatel/pt-br/regulado/outorga/servico-movel-maritimo"
aliases:
  - "MOB — MAN OVERBOARD — SISTEMA DE DETECÇÃO"
seo_title: "Mob — Man Overboard — Sistema de Detecção"
seo_description: "MOB — MAN OVERBOARD (Homem ao Mar) — Sistema eletrônico de detecção e localização de pessoa que caiu ao mar. Pode ser um simples botão que marca a posição GPS no cha."
seo_keywords:
  - "Mob"
  - "Man"
  - "Overboard"
  - "Detecção"
  - "50 Navegacao Instrumentacao e Comunicacao"
geo_queries:
  - "O que é Mob — Man Overboard — Sistema de Detecção em instalações elétricas náuticas?"
  - "Qual é a função de Mob — Man Overboard — Sistema de Detecção na embarcação?"
related_notes:
  - "AIS (Automatic Identification System)"
  - "Buzina"
  - "Bússola Eletrônica (Compass / HDG Sensor)"
  - "Chartplotter / GPS / MFD"
  - "Dsc — Chamada Seletiva Digital"
  - "EPIRB / Beacon de Emergência"
  - "Estação de Vento / Anemômetro"
  - "NAVEGAÇÃO (BB, BE e Alcançado)"
---

# Mob — Man Overboard — Sistema de Detecção

> [!abstract] Resumo técnico
> MOB — MAN OVERBOARD (Homem ao Mar) — Sistema eletrônico de detecção e localização de pessoa que caiu ao mar. Pode ser um simples botão que marca a posição GPS no chartplotter, ou um sistema completo com AIS pessoal, alarme automático e rast.

## O que é

Sistema de detecção, marcação e localização de pessoa que caiu ao mar. Pode variar de simples (botão MOB no chartplotter) a complexo (transponder AIS pessoal com alarme automático ao cair na água):

- **Botão MOB no chartplotter:** marca a posição GPS instantaneamente ao pressionar — guia o retorno ao ponto
- **MOB AIS (AIS-SART):** transponder pessoal que o tripulante usa no colete — transmite posição via AIS quando ativado
- **MOB DSC:** transmite chamada MOB via VHF com posição GPS
- **Sistema automático (wearable):** dispositivo no colete que detecta imersão e transmite automaticamente

## Função

- Marcar a posição exata onde a pessoa caiu (GPS)
- Guiar o retorno ao ponto de queda
- Transmitir a localização para outras embarcações (AIS) e costa (VHF DSC)
- Disparar alarme automático para a tripulação remanescente
- Reduzir o tempo de busca — segundos podem ser decisivos

## Como aparece na prática

Em todas as embarcações com chartplotter: botão MOB configurado e acessível (geralmente um botão dedicado ou atalho no MFD). Todo tripulante deve saber onde está e como acionar.

Em embarcações offshore mais preparadas, é comum adotar dispositivos pessoais de localização/alerta no colete. A tecnologia, o método de ativação e o canal de alerta variam conforme o dispositivo; isso precisa ser conhecido e treinado antes do uso real.

Em veleiros de cruzeiro com piloto automático: sistemas que, ao receber sinal MOB do AIS, automaticamente mudam o rumo do piloto para retornar ao ponto.

## Fundamentos mínimos

| Sistema | Custo | Precisão | Automático | Alcance |
| --- | --- | --- | --- | --- |
| Botão MOB no chartplotter | Zero (já incluso) | GPS do barco | Não | Ponto marcado |
| MOB via VHF DSC | Zero (incluso no VHF) | GPS do barco | Não | 20–40nm (VHF) |
| AIS-SART pessoal | Médio | GPS pessoal | Não (manual) | ~40nm (AIS) |
| MOB automático (imersão) | Alto | GPS pessoal | Sim | Depende da tecnologia |
| PLB pessoal | Médio | GPS pessoal | Manual | Global (satélite) |

## Procedimento MOB — o que fazer

```jsx
Sequência imediata após pessoa cair ao mar:

1. GRITAR "HOMEM AO MAR" — alertar toda a tripulação
2. PRESSIONAR O BOTÃO MOB no chartplotter — marcar a posição imediatamente
3. JOGAR boia salva-vidas na direção da pessoa
4. MANTER A VISTA na pessoa — designar uma pessoa só para isso
5. GIRAR o barco para retornar ao ponto
6. ACIONAR VHF Canal 16 — chamar socorro
7. Aproximar do MOB pelo lado de barlavento
8. RESGATAR — ter plano de como trazer a pessoa a bordo (escada, linha)
```

**Os primeiros 3 passos devem ser executados em menos de 5 segundos.**

## Botão MOB no chartplotter — configuração correta

- O botão MOB deve estar acessível do posto de pilotagem **sem** navegar menus
- Na maioria dos MFDs: botão físico dedicado ou atalho na tela de ativação rápida
- Ao pressionar: marca a posição GPS, exibe cursor no mapa, calcula o melhor rumo de retorno
- Configurar para que o piloto automático receba o ponto MOB automaticamente

**Garmin:** botão MOB = pressionar e segurar o botão "Home" ou ícone MOB na tela

**Simrad:** botão SOS / MOB na interface principal

**Raymarine:** botão MOB no painel de controle

## Dispositivos MOB pessoais — wearables

**Ocean Signal MOB1:**

- AIS (classe S — AIS-SART)
- Ativação manual ou por imersão
- Transmite posição via AIS para todas as embarcações com AIS a bordo
- Alcance: ~40nm (AIS)
- Bateria: 24h de transmissão

**Kannad SafeSea MOB:**

- AIS + DSC simultâneo
- Ativação por imersão automática
- Transmite para AIS e VHF DSC simultaneamente
- Integra ao sistema de chartplotter via AIS

**McMurdo FastFind:**

- PLB para uso marinho
- Ativação manual + imersão
- Transmite via satélite (Cospas-Sarsat) + AIS
- Alcance global

**ACR ResQLink:**

- PLB pessoal
- GPS integrado
- Alcance global

## Integração MOB com piloto automático

Chartplotters modernos integram o sinal MOB (via AIS ou botão) ao piloto automático:

- Alguns sistemas podem auxiliar o retorno ao ponto MOB ou sugerir rota/manobra ao operador
- A capacidade de executar manobra automática depende do fabricante, da integração instalada e do modo de operação efetivamente configurado
- Exibe countdown e vetor de rumo para o MOB

**Configurar essa integração antes de precisar usar — nunca durante a emergência.**

## Marcas e modelos

| Marca | Modelo | Tipo | Observação |
| --- | --- | --- | --- |
| **Ocean Signal** | MOB1 | AIS-SART pessoal | Muito compacto, colete |
| **Kannad** | SafeSea MOB | AIS + DSC | Ativação automática |
| **McMurdo** | Fast Find | PLB | Satélite + AIS |
| **ACR** | ResQLink 400 | PLB pessoal | Padrão offshore |
| **Garmin** | inReach (complementar) | Satélite bidirecional | Comunicação + localização |
| **Tideline** | MOB Alert | AIS | Custo-benefício |

## Problemas mais frequentes

| Problema | Causa raiz provável |
| --- | --- |
| Ninguém sabe onde está o botão MOB | Tripulação não treinada |
| MOB ativado acidentalmente | Botão muito acessível sem proteção |
| AIS-SART não aparece no chartplotter | Chartplotter com AIS não configurado para receber MOB |
| PLB sem bateria válida | Não substituída no prazo |
| Pessoa resgatada mas sem como subir a bordo | Sem escada de resgate ou sistema de içamento |

## Diagnóstico e treinamento prático

```jsx
Teste semestral recomendado:
Passo 1: Simular MOB — pressionar o botão e confirmar que a posição é marcada
Passo 2: Verificar que o chartplotter exibe o ponto e o cursor de retorno
Passo 3: Verificar integração com piloto automático (se configurado)
Passo 4: Treinar a manobra de retorno com toda a tripulação (sem MOB real)
Passo 5: Verificar que todos sabem onde estão as boias salva-vidas
Passo 6: Testar o procedimento de içamento de pessoa a bordo
```

## Boas práticas profissionais

- Configurar o botão MOB antes de qualquer saída (verificar que funciona)
- Treinar TODA a tripulação — não apenas o comandante
- Instalar escada de banho com acesso fácil na popa (essencial para içar pessoa)
- Em saídas offshore: equipar cada tripulante com dispositivo MOB pessoal
- Praticar o procedimento de retorno ao MOB com toda a tripulação pelo menos uma vez por ano

## Cuidados de instalação

- Botão MOB deve ter proteção física contra acionamento acidental (tampa)
- Mas acessível em menos de 2 segundos (equilíbrio entre proteção e rapidez)
- Verificar que o chartplotter tem GPS fix antes de sair (MOB sem GPS = posição inválida)
- Dispositivos pessoais: seguir estritamente o procedimento de teste do fabricante, evitando acionar funções reais de emergência ou comprometer consumíveis do equipamento

## Cuidados de uso

- Verificar o GPS fix do chartplotter antes de sair (sem GPS, o botão MOB não funciona adequadamente)
- Verificar bateria dos dispositivos pessoais antes de cada saída offshore
- Não colocar o dispositivo MOB pessoal no fundo da mochila — deve estar acessível e visível

## Erros comuns

- Não configurar o botão MOB no chartplotter
- Tripulação não sabe o procedimento de retorno ao MOB
- Não ter escada para içar a pessoa a bordo (o mais fatal: pessoa no mar, barco parado, sem como subir)
- Depender apenas do botão MOB sem ter dispositivo pessoal em saídas offshore
- Não testar o sistema regularmente (acreditar que funciona sem verificar)

## Relação com outros sistemas

- **Chartplotter/MFD:** recebe e exibe o ponto MOB
- **Piloto automático:** integra ao MOB para manobra automática de retorno
- **AIS:** recebe sinal do dispositivo AIS-SART pessoal
- **VHF DSC:** transmite chamada de socorro com posição do MOB
- **EPIRB:** último recurso — complementar ao MOB pessoal
- **GPS:** base para o sistema MOB funcionar corretamente

## Brasil x Internacional

| Aspecto | Brasil | Internacional |
| --- | --- | --- |
| Botão MOB configurado | Frequentemente não configurado | Verificado em treinamentos |
| Dispositivo MOB pessoal | Muito raro | Obrigatório em regatas oceânicas |
| Treinamento de tripulação | Raramente feito | Parte do safety briefing |
| Escada de açude (rescue step) | Frequentemente ausente | Recomendada como padrão |
| Integração MOB + piloto automático | Rara | Presente em embarcações modernas |

**Muito comum no Brasil:** barco com chartplotter e botão MOB nunca configurado, tripulação sem treinamento.

**Mais presente em embarcações maiores/premium:** dispositivo MOB para cada tripulante + integração com piloto automático + escada de resgate.

## Normas e referências

- **COLREGS:** regras de prevenção de colisão (contexto de emergência)
- **ABYC A-7 (edição a verificar):** recomendações de segurança (MOB)
- **ISO 15085:** Safety equipment — MOB procedures
- **NORMAM-01 (edição a verificar):** equipamentos de segurança obrigatórios
- **IEC 61097-14:** AIS-SART (dispositivos pessoais AIS de socorro)
- **ISAF OSR (Offshore Special Regulations):** obrigatoriedade de MOB em regatas oceânicas

## Como ensinar este tópico

**Sequência recomendada:**

1. Impacto emocional: taxa de sobrevivência por tempo (10min → muito menor)
2. Demonstração do botão MOB no chartplotter (toda a tripulação)
3. Treino prático de manobra de retorno (com boia jogada)
4. Apresentar dispositivos pessoais MOB (mostrar fisicamente)
5. Treino de içamento de pessoa a bordo (o passo mais ignorado)

**Mensagem central:** "Você tem 10 segundos para marcar a posição e começar a retornar. O restante do resgate é mais simples — mas esses 10 segundos são tudo."

## Ideias de vídeos

- "MOB: como configurar o botão no chartplotter antes de sair"
- "Treinamento MOB: o procedimento que todo tripulante precisa saber"
- "Dispositivos MOB pessoais: AIS-SART vs PLB — diferenças e quando usar"
- "O passo esquecido do MOB: como você vai içar a pessoa a bordo?"
- "MOB integrado ao piloto automático: como configurar no Garmin/Simrad"

## Diagramas sugeridos

- Fluxograma de procedimento MOB: os 8 passos em sequência (poster para o barco)
- Mapa de manobra: retorno ao ponto MOB (abordagem de barlavento)
- Comparativo de sistemas: botão MOB vs AIS-SART vs PLB (tabela de decisão)
- Diagrama de integração: MOB pessoal → AIS → chartplotter → piloto automático
- Gráfico de sobrevivência: probabilidade × tempo no mar (impacto visual)

## FAQ

**O botão MOB do chartplotter já está configurado de fábrica?**

O botão existe, mas precisa ser verificado. Confirmar que: (1) o GPS tem fix, (2) o botão marca a posição imediatamente, (3) exibe o cursor de retorno. Testar antes de sair.

**AIS-SART e PLB — qual é melhor para MOB?**

AIS-SART: funciona só onde há AIS no alcance (~40nm). Mais eficiente em rotas movimentadas. PLB: funciona globalmente via satélite. Mais eficiente em alto mar isolado. Ideal: AIS-SART para costeiro, PLB para offshore.

**Se eu não tiver escada de popa, como resgato a pessoa?**

Com dificuldade enorme. Uma pessoa no mar após tempo exposta tem força reduzida. Soluções alternativas: jogar uma linha de resgate com nó, usar o bote inflável. A escada permanente com degrau abaixo d'água é a solução correta.

**O sinal AIS do MOB aparece no chartplotter automaticamente?**

Sim, se o chartplotter tiver receptor AIS ativo. O dispositivo MOB aparece como alvo AIS especial com ícone de emergência.

**Posso treinar o MOB sem ativar o sistema de resgate real?**

Sim. A maioria dos chartplotters permite simular o MOB sem transmitir para outras embarcações. Para dispositivos AIS: testar apenas o mecanismo de ativação (sem transmitir) — seguir as instruções do fabricante para modo de teste.

## Integração com outras notas

- [[AIS (Automatic Identification System)]]
- [[Buzina]]
- [[Bússola Eletrônica (Compass / HDG Sensor)]]
- [[Chartplotter / GPS / MFD]]
- [[Dsc — Chamada Seletiva Digital]]
- [[EPIRB / Beacon de Emergência]]
- [[Estação de Vento / Anemômetro]]
- [[NAVEGAÇÃO (BB, BE e Alcançado)]]

## Perguntas que esta nota responde

- O que é Mob — Man Overboard — Sistema de Detecção em instalações elétricas náuticas?
- Qual é a função de Mob — Man Overboard — Sistema de Detecção na embarcação?
