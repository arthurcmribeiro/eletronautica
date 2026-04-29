---
title: "Mob — Man Overboard — Sistema de Detecção"
note_type: "system"
domain: "50_Navegacao_Instrumentacao_e_Comunicacao"
source_file: "MOB — MAN OVERBOARD — SISTEMA DE DETECÇÃO 33a19734f7fb81db8ef6d25c8985db66.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "23"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
normas_citadas:
  - "SOLAS Cap. III — Life-saving appliances and arrangements (arranjos de salvatagem e busca)"
  - "SOLAS Cap. IV — Radiocommunications (GMDSS, Dispositivos MOB associados)"
  - "IMO Resolution MSC.246(83) — Performance standards for AIS-SART"
  - "IMO Resolution A.810(19) — Float-free satellite EPIRB (referência para PLB)"
  - "IEC 61097-14 — AIS-SART (Search and Rescue Transmitter) e MOB-AIS"
  - "IEC 61097-2 / IEC 61097-13 — EPIRB 406 MHz (referência para PLB Cospas-Sarsat)"
  - "IEC 60945 — Maritime navigation and radiocommunication equipment — General requirements"
  - "IEC 61993-2 / IEC 62287-1/-2 — AIS Class A / Class B (recepção de alvos MOB-AIS)"
  - "ISO 12402 (série) — Personal flotation devices — Classes e ensaios (PFD, coletes salva-vidas)"
  - "ISO 12401 — Deck safety harness and safety line"
  - "ITU-R M.1371 — AIS TDMA (suporta mensagens MOB-AIS, ID 1-9)"
  - "ITU-R M.493 / M.541 — DSC (MOB via chamada distress individual)"
  - "Cospas-Sarsat C/S T.001 — 406 MHz Distress Beacons (PLB)"
  - "Cospas-Sarsat C/S T.018 — Second-generation beacons (PLB moderno)"
  - "ISAF Offshore Special Regulations (OSR) — obrigação de MOB-AIS/PLB em regatas oceânicas"
  - "RIPEAM/COLREGs Rule 5 — Look-out (vigilância é o primeiro elo do MOB)"
  - "NORMAM-204/DPC — Serviço Móvel Marítimo (PLB, registro SISEPIRB para PLB)"
  - "NORMAM-201/DPC — Tráfego e Permanência de Embarcações"
  - "NORMAM-211/DPC — Embarcações de esporte e recreio (salvatagem recreio)"
  - "Resoluções ANATEL — homologação de dispositivos MOB-AIS e PLB"
  - "ABYC A-4 (2023) — Fire fighting equipment (correlato a arranjos de segurança)"
  - "ABYC T-31 — Swim platforms, ladders, boarding equipment (escada de resgate)"
  - "ABYC E-11 (2023) — AC and DC Electrical Systems on Boats"
  - "ABNT NBR 5410:2004 + emendas — Instalações elétricas de baixa tensão"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://www.nmea.org/standards.html"
  - "https://www.gov.br/anatel/pt-br/regulado/outorga/servico-movel-maritimo"
  - "https://www.cospas-sarsat.int/"
  - "https://www.sailing.org/tools/documents/ISAFOffshoreSpecialRegulations"
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

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **MOB é protocolo + equipamento, nunca só equipamento** — os primeiros 10 segundos (gritar "Homem ao Mar" + pressionar botão MOB + jogar boia + designar vigia) valem mais que qualquer dispositivo no colete; treinar a sequência semestralmente é obrigação do comandante.
> 2. **Botão MOB no chartplotter é linha base não-negociável** — todo MFD tem um atalho dedicado (físico ou touchscreen); se o GPS estiver sem fix ou o botão não funcionar, você NÃO está preparado para sair. Teste antes de cada saída.
> 3. **AIS-SART/MOB-AIS pessoal (IEC 61097-14) é o padrão offshore** — dispositivo no colete/suspensório transmite em 161,975 MHz quando ativado por imersão ou manualmente; aparece como alvo de emergência em todos os AIS receivers no raio de ~5-8 mn.
> 4. **PLB pessoal (Cospas-Sarsat 406 MHz) cobre o cenário "sem AIS ao redor"** — AIS-SART só funciona se outra embarcação com AIS estiver em alcance VHF; PLB transmite para satélites e aciona MRCC diretamente. Oceano aberto = PLB obrigatório.
> 5. **MOB-AIS ≠ EPIRB** — EPIRB é da embarcação (registro no nome do barco); MOB-AIS/PLB é pessoal (registro no nome do tripulante, com vinculação à embarcação no SISEPIRB para PLB brasileiro). Nunca confundir.
> 6. **Ativação por imersão é padrão moderno, mas ativação manual é sempre possível** — Ocean Signal MOB1, Kannad SafeSea MOB, McMurdo FastFind usam sensor de imersão + botão; pessoa inconsciente no mar ativa automaticamente em < 5 s.
> 7. **Integração MOB-AIS → chartplotter → piloto automático é configurável, não automática** — dispositivo transmite, mas o chartplotter precisa estar configurado para tratar alvos MOB-AIS com prioridade e notificar piloto automático; testar essa cadeia no cais antes de offshore.
> 8. **Escada de resgate (ABYC T-31) é o elo frequentemente esquecido** — recuperar pessoa no mar após 10 min em água fria é impossível sem escada que chegue a 30 cm abaixo da linha d'água; sem ela, a pessoa pode estar marcada no GPS mas inacessível.
> 9. **ISAF OSR define níveis (Category 0-5)** — regatas oceânicas exigem AIS-SART/PLB por tripulante, colete ISO 12402-3 + harness ISO 12401, escada de resgate, sarilhos, boia MOB com mastro e luz; referência voluntária excelente para cruzeiro recreio offshore.

> [!danger] Quando chamar um especialista (engenheiro/instrutor com formação em salvatagem e GMDSS)
> 1. **Configuração MOB-AIS → piloto automático com retorno automático (Return-to-MOB)** — integração Garmin GHP Reactor, Raymarine Evolution, Simrad AP44 para que o piloto gire automaticamente ao receber alvo MOB-AIS requer parametrização (rumo, velocidade reduzida, parada a 20-30 m do alvo) e treino; erro de config pode virar para direção errada.
> 2. **Homologação ANATEL + registro SISEPIRB de PLB importado** — PLB comprado nos EUA (FCC) sem homologação ANATEL: registro SISEPIRB recusa, sinal pode ser ignorado por MRCC brasileiro em emergência; processo de homologação individual é complexo e caro.
> 3. **Tripulação de 6+ em regata offshore (ISAF Category 0-2)** — cada tripulante com AIS-SART + PLB, + MOB boat (pedestal com mastro + bolsa de recuperação + sarilho elétrico), plano de emergência documentado, radar/chartplotter com MARPA ativo; projeto de safety by design.
> 4. **Falha de ativação por imersão (MOB ativou sem motivo ou não ativou em teste)** — unidades Ocean Signal/Kannad/McMurdo com falha de sensor de imersão não devem ser "consertadas" DIY; substituir ou enviar ao fabricante; em PLB, substituição da bateria também é feita só em central autorizada Cospas-Sarsat.
> 5. **Testes reais antes de expedição oceânica** — testar MOB-AIS em terra (modo teste) não garante funcionamento ativado em água; teste em cais ao lado do chartplotter receptor, com MRCC ou operadora de AIS informada para evitar alarme falso regional.
> 6. **MOB durante piloto automático em cruzeiro solo (single-handed)** — pessoa sozinha no barco e cai ao mar com piloto mantendo rumo: o AIS-SART ativa mas ninguém a bordo para ajudar; protocolo inclui tether harness ISO 12401 obrigatório, PLB com contato emergencial, + possivelmente sistema de kill-switch automático do motor (MOB lanyard).
> 7. **Recuperação de vítima em hipotermia** — pessoa resgatada após > 15 min em água < 15°C tem risco alto de choque pós-resgate (arrhythmia rewarming); treinamento de primeiros socorros hipotermia (horizontal posture, rewarming gradual) vai além do tema MOB puro e requer curso offshore safety.
> 8. **Perícia sinistro em caso de afogamento com MOB documentado** — laudo forense envolvendo "o MOB foi acionado" requer leitura de logs do chartplotter (se existir), timestamp AIS no MRCC, verificação de registro SISEPIRB; escopo jurídico, não manutenção.
> 9. **Alarme falso de MOB-AIS em marina (ativação acidental)** — dispositivo ativado por chuva, lavagem ou limpeza genera distress AIS em canal 161,975 MHz; procedimento: desligar imediatamente, notificar MRCC para cancelamento, documentar; repetição pode gerar autuação ANATEL.

> [!info] Glossário rápido (≈ 47 termos)
> - **MOB** — Man Overboard, Homem ao Mar.
> - **MOB button** — botão físico/virtual no MFD que marca posição GPS instantânea.
> - **MOB waypoint** — ponto GPS marcado pelo MOB button, padrão WPL NMEA 0183.
> - **MOB-AIS** — dispositivo pessoal AIS-SART em 161,975 MHz (IEC 61097-14).
> - **AIS-SART** — AIS Search and Rescue Transmitter, para embarcação ou pessoal.
> - **SART (radar, legado)** — Search and Rescue Transponder em 9 GHz, substituído por AIS-SART.
> - **PLB** — Personal Locator Beacon, 406 MHz Cospas-Sarsat (pessoal).
> - **EPIRB** — Emergency Position Indicating Radio Beacon (embarcação).
> - **Cospas-Sarsat** — sistema internacional de satélites SAR.
> - **MEOSAR** — Medium Earth Orbit SAR (constelação moderna, < 5 min).
> - **MRCC** — Maritime Rescue Coordination Centre (Salvamar Brasil).
> - **SISEPIRB** — Sistema Brasileiro de Registro de EPIRB/PLB (DPC).
> - **Distress alert (AIS)** — mensagem AIS tipo 14 ou 1-9 com ID de MOB.
> - **Ativação por imersão** — sensor de água ativa dispositivo automaticamente.
> - **Ativação manual** — botão + trava de segurança (2-3 s pressionados).
> - **UIN** — Unique Identifier Number de PLB (15 HEX).
> - **MID** — Maritime Identification Digits (Brasil 710-719) em MOB-AIS.
> - **Nav status 14 (AIS)** — "AIS-SART/MOB/EPIRB active".
> - **Safe harness** — ISO 12401, cinto-linha-gancho para deck de veleiro.
> - **Jackline** — linha fixa ao longo do deck onde o harness engata.
> - **Tether** — cabo curto do harness ao jackline.
> - **PFD** — Personal Flotation Device (colete salva-vidas).
> - **ISO 12402-2** — colete 275N, offshore ocean service.
> - **ISO 12402-3** — colete 150N, offshore standard.
> - **ISO 12402-5** — auxiliares de flutuação 50N (esporte).
> - **Lifering / Horseshoe buoy** — boia salva-vidas circular ou em ferradura.
> - **Dan buoy / MOB pole** — mastro com luz e bandeira para marcar posição no mar.
> - **MOB light** — luz estroboscópica no colete/boia.
> - **Return-to-MOB** — função do piloto automático de retornar ao ponto.
> - **MARPA** — Mini Automatic Radar Plotting Aid (rastrear alvo no radar).
> - **Escada de resgate (ABYC T-31)** — com degrau a 30 cm abaixo da linha d'água.
> - **Rescue sling** — bolsa/alça de içamento com sistema de roldanas.
> - **Lifesling** — marca de rescue sling padrão offshore.
> - **Kill switch (MOB lanyard)** — cordão que desliga motor ao cair ao mar.
> - **Cat 0-5 ISAF OSR** — categorias de regata offshore (0 trans-oceânica, 5 baía).
> - **Quick-release boarding ladder** — escada abatível com rápido acionamento.
> - **SAR (Search and Rescue)** — busca e salvamento coordenado.
> - **Salvamar Brasil** — autoridade SAR brasileira (Marinha/DPC).
> - **Hipotermia** — <35°C temperatura central; risco crítico após > 15 min em água fria.
> - **Cold shock** — resposta autonômica nos 1-3 min iniciais em água fria.
> - **Dry suit / Wet suit** — proteção térmica (offshore frio).
> - **LED strobe** — luz estroboscópica brilhante para ser vista no escuro.
> - **Retroreflective tape** — fita reflexiva SOLAS no colete.
> - **Personal GPS tracker** — Garmin inReach, Spot (bidirecional satélite).
> - **Man-overboard drill** — treinamento operacional de MOB.
> - **Quick-stop maneuver** — manobra de retorno clássica à vela.
> - **Williamson turn** — manobra de retorno a motor (250°/20° corrigido).
> - **Ficha de tripulação** — registro nominal obrigatório em regata/offshore.

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

- **SOLAS Cap. III** — Life-saving appliances and arrangements (coletes, botes, escadas; base de arranjo de salvatagem).
- **SOLAS Cap. IV** — Radiocommunications (GMDSS, integração MOB-AIS/DSC/EPIRB).
- **IMO Resolution MSC.246(83)** — Performance standards for AIS-SART (base técnica para dispositivos AIS-SART/MOB-AIS).
- **IMO Resolution A.810(19)** — Float-free satellite EPIRB (referência para PLB Cospas-Sarsat 406 MHz).
- **IEC 61097-14** — AIS Search and Rescue Transmitter (AIS-SART) e MOB-AIS pessoal (161,975 MHz).
- **IEC 61097-2 / IEC 61097-13** — EPIRB 406 MHz primeira e segunda geração (base técnica para PLB).
- **IEC 60945** — Maritime navigation and radiocommunication equipment — General requirements (EMC, IP, ambiente marítimo).
- **IEC 61993-2** — AIS Class A shipborne equipment (recepção de alvos MOB-AIS em embarcações grandes).
- **IEC 62287-1 / -2** — AIS Class B CSTDMA/SOTDMA (recepção MOB-AIS em recreio).
- **ISO 12402 (série)** — Personal flotation devices — Classes 275N/150N/100N/50N (coletes salva-vidas).
- **ISO 12401** — Small craft — Deck safety harness and safety line (harness + tether).
- **ITU-R M.1371** — AIS TDMA (suporta mensagens MOB-AIS ID 1-9).
- **ITU-R M.493 / M.541** — DSC (chamada distress individual integrada a MOB, quando VHF DSC disponível).
- **Cospas-Sarsat C/S T.001** — 406 MHz Distress Beacons (PLB primeira geração).
- **Cospas-Sarsat C/S T.018** — Second-generation beacons — General specification (PLB moderno, Return Link Service).
- **Cospas-Sarsat C/S G.005** — Beacon coding (protocolo PLB).
- **ISAF Offshore Special Regulations (OSR)** — Categorias 0-5; obrigação de MOB-AIS/PLB por tripulante, colete 275N, escada de resgate, boia MOB pole (regatas oceânicas).
- **RIPEAM/COLREGs Rule 5** — Look-out (vigia é o primeiro elo do MOB; sem olho no mar, o botão é inútil).
- **RIPEAM/COLREGs Rule 7** — Risk of collision (MOB em alvo AIS deve ser tratado como emergência prioritária).
- **NORMAM-204/DPC** — Serviço Móvel Marítimo (MOB-AIS licenciamento, PLB registro SISEPIRB).
- **NORMAM-201/DPC** — Tráfego e Permanência de Embarcações.
- **NORMAM-211/DPC** — Embarcações de esporte e recreio (salvatagem recreio brasileira).
- **Resoluções ANATEL** — homologação de dispositivos MOB-AIS e PLB para uso no Brasil.
- **ABYC A-4 (2023)** — Fire fighting equipment (correlato, arranjos de segurança).
- **ABYC T-31** — Swim platforms, ladders, boarding equipment (escada de resgate com degrau abaixo da linha d'água).
- **ABYC E-11 (2023)** — AC and DC Electrical Systems on Boats (fiação das unidades MOB fixas e integração chartplotter/piloto).
- **ABNT NBR 5410:2004 + emendas** — Instalações elétricas de baixa tensão (parte AC quando houver).

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
