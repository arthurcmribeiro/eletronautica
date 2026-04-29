---
title: "Dsc — Chamada Seletiva Digital"
note_type: "technical-note"
domain: "50_Navegacao_Instrumentacao_e_Comunicacao"
source_file: "DSC — CHAMADA SELETIVA DIGITAL 33a19734f7fb81b9a8a4c4bd78298cb7.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "19"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
normas_citadas:
  - "GMDSS (IMO) — Global Maritime Distress and Safety System"
  - "SOLAS Cap. IV — Radiocommunications"
  - "ITU-R M.493 — Digital Selective Calling system for use in the maritime mobile service"
  - "ITU-R M.541 — Operational procedures for the use of DSC equipment in the maritime mobile service"
  - "ITU-R M.821 — Optional expansion of the Digital Selective-Calling system for use in the maritime mobile service"
  - "ITU Radio Regulations — Appendix 18 (alocação do Canal 70 DSC)"
  - "IEC 62238 — Maritime VHF radiotelephone equipment and systems with integrated Class D DSC"
  - "IEC 61097-3 — DSC equipment operating in MF, MF/HF and VHF bands"
  - "IEC 61097-7 — Shipborne VHF radiotelephone transmitter and receiver"
  - "IEC 60945 — Maritime navigation and radiocommunication equipment — General requirements"
  - "IEC 61162-1/-2 (NMEA 0183) — Digital interfaces for navigational devices"
  - "IEC 61162-3 (NMEA 2000) — Network-based digital interface"
  - "NORMAM-204/DPC — Serviço Móvel Marítimo e Serviço Móvel Marítimo por Satélite"
  - "NORMAM-201/DPC — Tráfego e Permanência de Embarcações"
  - "NORMAM-211/DPC — Embarcações de esporte e recreio"
  - "Resoluções ANATEL aplicáveis — Serviço Móvel Marítimo e registro de MMSI"
  - "ABYC E-11 (2023) — AC and DC Electrical Systems on Boats (alimentação do VHF/DSC)"
  - "ABNT NBR 5410:2004 + emendas — Instalações elétricas de baixa tensão"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://www.nmea.org/standards.html"
  - "https://www.gov.br/anatel/pt-br/regulado/outorga/servico-movel-maritimo"
  - "https://www.itu.int/pub/R-REC"
  - "https://www.imo.org/en/OurWork/Safety/Pages/GMDSS.aspx"
aliases:
  - "DSC — CHAMADA SELETIVA DIGITAL"
seo_title: "Dsc — Chamada Seletiva Digital"
seo_description: "DSC — CHAMADA SELETIVA DIGITAL — Sistema de chamada de emergência e seleção digital integrado ao rádio VHF. Permite enviar distress call automático com posição GPS e."
seo_keywords:
  - "Dsc"
  - "Chamada"
  - "Seletiva"
  - "Digital"
  - "50 Navegacao Instrumentacao e Comunicacao"
geo_queries:
  - "O que é Dsc — Chamada Seletiva Digital em instalações elétricas náuticas?"
  - "Qual é a função de Dsc — Chamada Seletiva Digital na embarcação?"
related_notes:
  - "AIS (Automatic Identification System)"
  - "Buzina"
  - "Bússola Eletrônica (Compass / HDG Sensor)"
  - "Chartplotter / GPS / MFD"
  - "EPIRB / Beacon de Emergência"
  - "Estação de Vento / Anemômetro"
  - "Mob — Man Overboard — Sistema de Detecção"
  - "NAVEGAÇÃO (BB, BE e Alcançado)"
---

# Dsc — Chamada Seletiva Digital

> [!abstract] Resumo técnico
> DSC — CHAMADA SELETIVA DIGITAL — Sistema de chamada seletiva e socorro digital integrado ao rádio VHF. Permite transmitir identidade e, quando corretamente integrado, posição GNSS ao acionar uma chamada de emergência. Requisitos de porte e configuração devem ser confirmados conforme o enquadramento regulatório aplicável. Sem MMSI válido e sem GPS integrado, o DSC é apenas um botão vermelho decorativo.

> [!tip] Regra de decisão em 30 segundos
> 1. **DSC = MMSI + GPS. Faltou um, não é DSC — é rádio de voz.** Distress acionado sem GPS transmite apenas MMSI e natureza da emergência; socorro chega sem posição. Distress sem MMSI programado é ignorado pelas estações costeiras (sem identificação válida).
> 2. **Canal 70 é exclusivo para DSC — nunca voz.** 156,525 MHz é canal digital reservado mundialmente. Transmitir voz no Canal 70 = interferência no socorro de outras embarcações + violação regulatória.
> 3. **Distress acionado acidentalmente é falso alerta — tem protocolo obrigatório.** Assim que perceber: Canal 16 → "CANCEL DISTRESS — FALSE ALERT — MMSI XXXXXXXXX — nome do barco — posição". Não cancelar agrava (multa + investigação de desvio de recursos SAR).
> 4. **MMSI só se programa 1× em Classe D típica.** O segundo reset exige laboratório autorizado ou substituição do rádio. Programar sem certeza do número **oficial** = perder o rádio para o DSC.
> 5. **NMEA 0183 para DSC: pinos e sentenças certas.** GPS TX+ → VHF NMEA IN+ / GPS TX− → VHF NMEA IN− / baud 4800 / sentença **$GPRMC** (ou RMC + GLL). Muitos instaladores invertem TX/RX ou usam só GLL — resultado: "No position data".
> 6. **NMEA 2000 é mais simples e mais confiável para DSC moderno.** Um cabo Micro-C em backbone ativo entrega PGN 129025/129029 automaticamente. Não exige cabeamento seriado ponto-a-ponto.
> 7. **Dual Watch / Tri Watch deve estar sempre ligado.** O DSC do Canal 70 é monitorado em background pelo rádio, mesmo enquanto você escuta outro canal. Desativar para "economizar bateria" = cegueira digital.
> 8. **Chamada individual DSC é o telefone marítimo.** Em vez de gritar no Canal 16 e escolher canal de trabalho, chama o MMSI destino com canal sugerido → o outro rádio toca e propõe aceitar. Uso profissional reduz poluição no Canal 16.
> 9. **Registro oficial do MMSI no Brasil é via ANATEL + base DPC/GMDSS.** Número "tirado da internet" ou "mesmo do rádio anterior" → não consta no ITU MARS nem em SAR database → socorro demora. Registro regular leva alguns dias; pagar taxa e manter atualizado vale a segurança.

> [!danger] Quando chamar um especialista
> - **Rádio classe D com MMSI travado pelo instalador anterior:** laboratório autorizado do fabricante (Standard Horizon, Icom, Garmin). Nunca abrir o rádio para "resetar" — a reprogramação é por software proprietário com senha.
> - **Acidente com Distress não cancelado:** após 24–48h, o SAR/Salvamar registra falso alerta, abre investigação e pode aplicar multa. Se a emergência real ocorreu e o rádio perdeu a chamada, perícia precisa do log do equipamento.
> - **Registro MMSI em embarcação com histórico fiscal/regulatório complexo (mudança de bandeira, cessão, frota comercial):** despachante naval ou corretora marítima. Erro no cadastro impede liberação da estação de navio.
> - **Instalação de DSC em barco com múltiplas antenas RF próximas (VHF dual, radar, HF-SSB, satcom):** o rádio pode receber falsos alertas ou falhar ao transmitir por intermodulação. Engenheiro de RF naval com analisador de espectro.
> - **Falha sistemática de chamadas individuais DSC (nenhuma outra embarcação responde):** verificar código de país do MMSI, compatibilidade Classe D×Classe B, atualização de firmware, senha de DSC, tabela de MMSIs cadastrados no rádio. Técnico com bancada de teste.
> - **Embarcação SOLAS ou em missão de trabalho offshore:** Class A DSC + GMDSS área A1/A2/A3/A4, redundância, fonte reserva, gravador de dados. Instalação e inspeção por prestador homologado DPC + órgão de bandeira.
> - **Importação de rádio de outro país sem homologação Anatel:** equipamento pode funcionar mas não terá suporte legal em emergência — autoridades podem rastrear o MMSI e identificar irregularidade na homologação. Consultar despachante/advogado.
> - **DSC disparando distress sozinho (botão preso, relé interno):** risco de arresto pela Capitania e perda de confiança da rede SAR. Desligar o rádio, remover antena, procurar assistência. Não desconectar apenas a alimentação sem comunicação — o log continua.
> - **Teste real de distress em barco novo (comissionamento):** somente com coordenação prévia com MRCC/Salvamar. Nunca acionar o Distress "para testar" sem aviso — a cadeia de resposta é acionada e recursos SAR são mobilizados.

## O que é

DSC (Digital Selective Calling) é um protocolo digital padronizado (ITU-R M.493) que opera no Canal 70 do VHF marítimo. Permite:

- **Chamada de socorro (Distress):** transmissão automática de ID da embarcação + posição + natureza da emergência
- **Chamada individual:** contato direto com outra embarcação ou estação costeira pelo MMSI
- **Chamada de grupo:** para múltiplas embarcações
- **Chamada geográfica:** para todas as embarcações em uma área
- **Confirmação de recebimento:** sistema bidirecional (ACK)

O DSC opera exclusivamente no Canal 70 — canal reservado mundialmente para chamadas DSC. A voz continua no Canal 16.

## Função

- Enviar chamada de socorro digital com identificação da estação e, quando disponível, posição GNSS associada
- Permitir que estações de guarda (Guardião, Marinha, USCG) identifiquem imediatamente a embarcação
- Registrar a posição do momento do Distress (mesmo que a embarcação seja perdida depois)
- Comunicação ship-to-ship sem ocupar Canal 16 para voz
- Relay automático de emergência entre estações (coast guard → outras embarcações na área)

## Como aparece na prática

Um VHF com DSC classe D (padrão doméstico) tem um botão vermelho protegido por tampa plástica. Em caso de emergência:

1. Abrir a tampa
2. Pressionar e segurar o botão MAYDAY por 3 segundos
3. O rádio transmite automaticamente no Canal 70: MMSI + posição + natureza da emergência
4. Muda para Canal 16 para comunicação de voz

Sem GPS integrado → o DSC transmite sem posição → socorro demora muito mais.

## Fundamentos mínimos

| Parâmetro | Detalhe |
| --- | --- |
| Canal de operação | Canal 70 VHF (156.525 MHz) — exclusivo |
| Padrão | ITU-R M.493 |
| Identificador | MMSI (Maritime Mobile Service Identity) — 9 dígitos |
| Classes | Classe D (lazer/recreio) / Classe C (antigo) / Classe B/A (comercial) |
| Integração GPS | necessária para transmitir posição automaticamente no distress |
| Alcance típico | 20–40 nm (igual ao VHF) |
| Potência de transmissão DSC | 25W (igual ao VHF) |
| Registro MMSI | deve seguir o processo regulatório vigente para a estação/embarcação |

## MMSI — Maritime Mobile Service Identity

O MMSI é a identidade digital da estação marítima/embarcação no sistema de radiocomunicação. Trata-se de um número de 9 dígitos cuja atribuição e uso precisam seguir o processo regulatório aplicável.

**Estrutura do MMSI:**

- Embarcações: começa com código do país (710–719 para Brasil)
- Exemplo Brasil: 710XXXXXX
- Estações costeiras: começa com 00
- Grupos: começa com 0

**Registro no Brasil:**

- Confirmar o processo vigente junto aos órgãos competentes e à regulamentação aplicável à estação/embarcação
- Registrar apenas uma vez por embarcação
- Ao vender a embarcação: cancelar e registrar novo MMSI para o novo proprietário

**Base de dados:** cadastros regulatórios e bases marítimas são úteis para identificação, mas a presença ou ausência em plataformas públicas não deve ser tratada como único critério de conformidade operacional.

## Integração GPS — ponto crítico

O DSC é inútil sem GPS integrado. A posição só é transmitida no Distress se o rádio receber dados de GPS (via NMEA 0183 ou NMEA 2000).

**Conexão NMEA 0183 (mais comum):**

```jsx
GPS TX+ → VHF NMEA IN+
GPS TX- → VHF NMEA IN-
Baud rate: 4800 bps
Sentences necessárias: $GPRMC (posição + velocidade + data)
```

**Conexão NMEA 2000:**

Rádios modernos com Micro-C conector recebem posição diretamente do backbone N2K (mais simples e confiável).

**Verificação:** no menu do VHF, a posição deve aparecer exibida numericamente. Se aparecer "No GPS" → a integração não está funcionando.

## Classes de DSC

| Classe | Onde Usada | Características |
| --- | --- | --- |
| **Classe D** | Lazer e recreio | Distress + individual + Canal 70 watch |
| **Classe C** | Legado (raro) | Sem watch automático no C70 |
| **Classe B** | Comercial menor | Mais funções que D |
| **Classe A** | Comercial / SOLAS (edição a verificar) | Funcionalidade completa, GMDSS |

Para embarcações de esporte e recreio: Classe D é o padrão e o suficiente.

## Marcas e modelos

| Marca | Modelo | Classe DSC | Observação |
| --- | --- | --- | --- |
| **Standard Horizon** | GX2400G | D | Com GPS integrado — recomendado |
| **Standard Horizon** | GX1850G | D | Com GPS integrado |
| **Icom** | IC-M510 | D | NMEA 2000 nativo |
| **Icom** | IC-M605 | D | Classe D, robusto |
| **Garmin** | VHF 215 | D | Integra com N2K |
| **Uniden** | UM385 | D | Custo-benefício |
| **Cobra** | MR F300FLT | D | Flutuante (MOB) |

**Recomendação prática:** Modelos com GPS **integrado** na própria antena do VHF (como Standard Horizon GX2400G) eliminam a necessidade de cabeamento NMEA adicional.

## Problemas mais frequentes

| Problema | Causa raiz provável |
| --- | --- |
| DSC transmite "no position" | GPS não integrado ou cable NMEA errado |
| MMSI não programado | Nunca foi configurado ou foi resetado |
| Rádio não aparece em plataformas públicas | cadastro incompleto, ausência de cobertura pública ou expectativa incorreta sobre o sistema |
| Botão DISTRESS não responde | Precisa segurar 3–5s (proteção contra acionamento acidental) |
| Nenhum ACK de distress recebido | Fora de alcance ou sem estação de guarda ativa |
| Senha bloqueada | Instalador programou senha e não documentou |

## Causas raiz

**GPS não integrado:** o erro mais grave. Muitas embarcações têm VHF com DSC mas sem GPS conectado. Em emergência, o Distress transmite sem posição → socorro demora horas ou não chega.

**MMSI não programado:** segundo erro mais comum. Muitos VHFs saem de fábrica sem MMSI definido. Sem esse dado, o DSC não cumpre corretamente sua função de identificação. A programação deve ser feita com o número oficial correto e seguindo o procedimento do fabricante.

**MMSI programado mas inconsistente com o cadastro:** o rádio até pode transmitir, mas a resposta das autoridades e a identificação da embarcação ficam comprometidas quando a base de dados regulatória está errada, desatualizada ou incompatível.

## Diagnóstico prático

```jsx
Verificação completa do DSC:

1. Menu do VHF → MMSI: verificar se está programado (9 dígitos)
2. Menu → Position: verificar se aparece lat/long (GPS integrado funcionando)
3. Testar chamada DSC individual para outra embarcação (não usar Canal 70 para teste aleatório)
4. Verificar em bases oficiais e plataformas de consulta apropriadas se o cadastro da estação está coerente
5. Verificar cabeamento NMEA (se GPS externo):
   - GPS TX+ → VHF NMEA IN+
   - GPS TX- → VHF NMEA IN-
   - Baud 4800
6. Confirmar que o equipamento está operando conforme a configuração DSC prevista pelo fabricante e pela rotina operacional adotada
```

**Teste de emergência real:** nunca testar o botão DISTRESS sem informar previamente a Marinha/Guardião. Em caso de acionamento acidental, chamar imediatamente o Canal 16 e informar o falso alerta (obrigação legal).

## Boas práticas profissionais

- Sempre integrar GPS ao VHF no momento da instalação — nunca deixar para depois
- Regularizar o MMSI e a configuração DSC conforme o processo vigente antes de depender do sistema em navegação real
- Anotar o MMSI em local visível a bordo (junto às informações da embarcação)
- Incluir no checklist de saída: "GPS aparecendo no VHF?"
- Orientar todos os tripulantes sobre o uso do botão DISTRESS e as consequências de acionamento acidental

## Cuidados de instalação

- Usar o cabo de antena correto (RG-8X mínimo, PL-259 bem crimpado)
- Proteger os conectores NMEA da umidade (fita autovulcanizante)
- Instalar o microfone em local de fácil acesso na estação de comando
- Considerar VHF secundário na popa ou no flybridge para embarcações grandes
- Em barcos offshore: instalar VHF fixo + VHF portátil (redundância)

## Cuidados de uso

- Verificar antes de cada saída: GPS aparece no display do VHF
- Manter disciplina operacional de escuta e configuração DSC compatível com o tipo de operação e com o equipamento instalado
- Nunca testar o DISTRESS sem notificar as autoridades
- Após qualquer acionamento acidental: Canal 16, informar falso alerta imediatamente
- Trocar a bateria do VHF portátil a cada 1–2 anos

## Erros comuns de instaladores

- Instalar o VHF sem conectar o GPS (DSC inútil)
- Não programar o MMSI (DSC inútil)
- Programar MMSI mas não registrar na ANATEL (edição a verificar)
- Usar cabo de antena RG-58 em vez de RG-8X (perda de sinal)
- Inverter TX/RX do NMEA (GPS não chega ao VHF)
- Instalar a antena VHF próxima à antena de GPS (interferência)

## Relação com outros sistemas

- **GPS/Chartplotter:** fornece posição via NMEA para o VHF/DSC
- **EPIRB:** complementar ao DSC — EPIRB opera em 406 MHz via satélite (alcance global)
- **AIS:** também usa MMSI, mas opera como sistema separado (visibilidade de tráfego)
- **Rádio HF/SSB:** complementa para comunicação oceânica onde VHF não alcança
- **NMEA 0183/2000:** protocolo de integração GPS→VHF

## Brasil x Internacional

| Aspecto | Brasil | Internacional |
| --- | --- | --- |
| Obrigatoriedade VHF | NORMAM-01 (edição a verificar) (embarcações ≥8m offshore) | Varies por bandeira |
| MMSI registrado | Maioria não fez | Padrão nos EUA/Europa |
| GPS integrado ao VHF | Raramente feito por instaladores | Considerado básico |
| Conhecimento de acionamento DSC | Muito baixo | Maior (treinamento obrigatório) |
| Habilitação para operar VHF | ROC (Restricted Operator Certificate) | Exigida |

**Muito comum no Brasil:** VHF instalado sem GPS integrado e sem MMSI registrado.

**Mais presente em embarcações maiores/premium:** Icom IC-M510 com N2K, VHF duplo (painel + flybridge).

## Glossário rápido

- **DSC (Digital Selective Calling):** chamada seletiva digital definida pela ITU-R M.493. Protocolo digital para distress, urgência, segurança, chamadas individuais, de grupo e geográficas.
- **Canal 70 (156,525 MHz):** canal VHF exclusivo para tráfego DSC. Zero voz.
- **Canal 16 (156,800 MHz):** canal de voz para socorro, urgência, segurança e chamada. DSC chama → confirmação e voz acontecem no 16.
- **MMSI (Maritime Mobile Service Identity):** identificador numérico de 9 dígitos da estação marítima.
- **MID (Maritime Identification Digits):** 3 primeiros dígitos do MMSI que identificam o país. Brasil: 710–719.
- **Classe A DSC:** conjunto completo exigido em navios SOLAS. Todas as categorias de chamada, múltiplos canais, integração GMDSS total.
- **Classe B DSC:** legado, menos comum. Mais recursos que Classe D, menos que Classe A.
- **Classe C DSC:** legado/aposentada. Sem watch automático no Canal 70.
- **Classe D DSC:** padrão em rádio de recreio. IEC 62238. Distress + individual + watch Canal 70.
- **Classe E DSC:** legado associado ao SSB/HF.
- **Distress Alert:** chamada de socorro digital com MMSI + posição (se GPS integrado) + natureza da emergência.
- **Distress Relay:** retransmissão automática do alerta por outras estações que ouviram o distress.
- **Distress Ack (Acknowledgement):** confirmação de recebimento emitida pela estação costeira / Coast Guard.
- **All Ships Call:** chamada DSC para todas as estações em alcance. Usada para avisos gerais não-emergency.
- **Individual Call:** chamada DSC ponto-a-ponto pelo MMSI destino — equivalente ao "telefone" marítimo.
- **Group Call:** chamada a um MMSI de grupo (frota, clube).
- **Geographic Area Call:** chamada DSC a todas as estações em uma área geográfica (lat/lon + raio).
- **Position Request:** solicitação DSC da posição de outra embarcação (autorização pode ser requerida).
- **Position Report:** resposta à Position Request ou envio voluntário de posição.
- **Urgency Call:** prioridade 2 (Pan-Pan).
- **Safety Call:** prioridade 3 (Sécurité — aviso à navegação).
- **Routine Call:** prioridade 4 (chamadas operacionais comuns).
- **Natureza da emergência (Distress Nature):** código escolhido no menu do Distress — Fire/Explosion, Flooding, Collision, Grounding, Listing, Sinking, Disabled and adrift, Abandoning ship, Piracy, Man overboard, Undesignated.
- **Self-ID:** identificação automática do MMSI + nome programado no rádio.
- **Watch mode:** escuta do Canal 70 DSC em segundo plano mesmo quando rádio está em outro canal.
- **Dual Watch:** monitora Canal 16 + 1 canal de trabalho.
- **Tri Watch:** monitora Canal 16 + Canal 70 + 1 canal de trabalho.
- **GMDSS (Global Maritime Distress and Safety System):** sistema IMO integrando DSC, EPIRB, SART, NAVTEX, Inmarsat.
- **Área A1/A2/A3/A4:** cobertura GMDSS (A1 = VHF DSC costeiro).
- **MRCC (Maritime Rescue Coordination Centre):** centro coordenador SAR. Brasil: Salvamar Brasil (Marinha do Brasil).
- **SAR (Search and Rescue):** busca e salvamento marítimo.
- **ITU MARS (Maritime mobile Access and Retrieval System):** base de dados ITU que lista MMSIs registrados mundialmente.
- **EPIRB (Emergency Position-Indicating Radio Beacon):** rádio-baliza 406 MHz via satélite (Cospas-Sarsat) — complementar ao DSC em alto-mar.
- **SART (Search And Rescue Transponder):** respondedor radar 9 GHz para localização de sobreviventes.
- **NAVTEX:** serviço de boletins meteorológicos e de segurança em texto (MF 518 kHz).
- **Posição via NMEA:** o VHF/DSC obtém lat/lon via NMEA 0183 ($GPRMC, $GPGLL) ou NMEA 2000 (PGN 129025/129029).
- **Sentença $GPRMC:** posição + velocidade + data + hora UTC — base mínima para o DSC.
- **PGN 129808 (NMEA 2000):** DSC Call Information — o chartplotter exibe o distress recebido em tempo real.
- **Heartbeat NMEA:** periodicidade em que o VHF verifica se o GPS ainda está fornecendo posição válida.
- **No Position Data:** mensagem indicando que o VHF não recebe posição — DSC transmitirá distress sem lat/lon.
- **Botão Distress / tampa protetora:** botão vermelho protegido; pressionar 3–5 s envia o distress.
- **Canal 13 Bridge-to-Bridge:** canal operacional para comunicação entre pontes de navios (complemento, não DSC).
- **Anatel — Serviço Móvel Marítimo:** atribuição de MMSI, indicativo e licenciamento no Brasil.
- **ROC (Restricted Operator Certificate):** certificado de operador restrito VHF — exigido em várias jurisdições; no Brasil, consulte regulamentação vigente.
- **GOC / LRC:** certificados para operador GMDSS (comercial/profissional).
- **ATIS:** identificação automática exigida em hidrovias europeias — distinto de DSC.

## Normas e referências

- **GMDSS (IMO — Global Maritime Distress and Safety System)** — arcabouço global onde o DSC está inserido.
- **SOLAS, Cap. IV — Radiocommunications** — convenção IMO para equipamentos de comunicação em navios.
- **ITU-R M.493** — *Digital Selective Calling system for use in the maritime mobile service.* Especificação técnica do protocolo DSC.
- **ITU-R M.541** — *Operational procedures for the use of DSC equipment.* Procedimentos operacionais, obrigações de escuta.
- **ITU-R M.821** — *Optional expansion of the DSC system.* Extensões e chamadas adicionais.
- **ITU Radio Regulations, Apêndice 18** — alocação do Canal 70 e demais canais VHF marítimos.
- **IEC 62238** — *Maritime VHF radiotelephone equipment and systems with integrated Class D DSC.* Referência para rádio de recreio.
- **IEC 61097-3** — *DSC equipment operating in MF, MF/HF and VHF bands.*
- **IEC 61097-7** — *Shipborne VHF radiotelephone transmitter and receiver.*
- **IEC 60945** — *Maritime navigation and radiocommunication equipment — General requirements.*
- **IEC 61162-1/-2 (NMEA 0183)** — interface serial para integração GPS ↔ VHF/DSC.
- **IEC 61162-3 (NMEA 2000)** — rede CAN-based com PGN 129808 (DSC Call Information).
- **NORMAM-204/DPC** — *Serviço Móvel Marítimo e Serviço Móvel Marítimo por Satélite.*
- **NORMAM-201/DPC** — *Tráfego e Permanência de Embarcações.*
- **NORMAM-211/DPC** — *Embarcações de esporte e recreio.*
- **Resoluções ANATEL aplicáveis** — Serviço Móvel Marítimo, registro de MMSI, indicativo de chamada. Verificar edição vigente caso a caso.
- **ABYC E-11 (2023)** — *AC and DC Electrical Systems on Boats.* Base para alimentação e proteção do VHF/DSC.
- **ABNT NBR 5410:2004 + emendas** — *Instalações elétricas de baixa tensão.* Complemento nacional.

## Como ensinar este tópico

**Sequência recomendada:**

1. Demonstrar o que acontece quando o DISTRESS é acionado (simulação via manual)
2. Mostrar a importância do MMSI e da posição GPS com caso real (barco desapareceu — sem posição no DSC)
3. Prática: configurar MMSI no VHF (em rádio desligado da antena)
4. Verificar integração GPS no menu
5. Simular chamada individual DSC para outra embarcação

**Mensagem central:** "Um VHF sem GPS e sem MMSI é só um rádio de voz. O DSC é o que salva vidas — mas só se estiver configurado."

## Ideias de vídeos

- "Como registrar seu MMSI na ANATEL (edição a verificar) — passo a passo"
- "Por que seu VHF não vai te salvar se não tiver GPS conectado"
- "Configurando DSC no VHF: MMSI + integração GPS"
- "Teste de DSC: o que acontece quando você aperta o botão MAYDAY"
- "VHF com GPS integrado vs GPS externo — qual instalar?"
- "EPIRB vs VHF DSC: qual a diferença e quando usar cada um"

## Diagramas sugeridos

- Diagrama de conexão: GPS → VHF via NMEA 0183 (TX+, TX-, IN+, IN-, GND)
- Fluxograma de emergência DSC: botão → Canal 70 → Coast Guard → Canal 16
- Tabela de classes DSC: D vs B vs A com casos de uso
- Diagrama GMDSS simplificado: DSC + EPIRB + SART na pirâmide de socorro
- Mapa de cobertura VHF DSC costeiro Brasil (estações Marinha)

## FAQ

**O DSC funciona se o rádio estiver no canal de escuta (não no 70)?**

Sim. Rádios com dual/tri-watch monitoram simultaneamente o Canal 16 e o Canal 70 — mesmo que você esteja ouvindo outra frequência.

**Posso registrar o MMSI eu mesmo?**

Sim, diretamente no site da ANATEL (edição a verificar) (gratuito para embarcações de lazer). Em alguns países, associações náuticas também fazem o registro.

**Se eu vender minha embarcação, o MMSI vai junto?**

Não deve. O comprador precisa registrar um novo MMSI. O antigo deve ser cancelado. MMSI vinculado ao proprietário.

**O Canal 70 pode ser usado para conversas normais?**

NÃO. O Canal 70 é exclusivo para sinais DSC digitais — nunca para voz. Usar voz no 70 interfere nas chamadas de emergência de outras embarcações.

**Em quantos km o DSC é efetivo?**

O alcance do VHF é linha de visão (20–40 nm tipicamente). Em alto mar, longe da costa, o DSC pode não alcançar estação costeira — para isso, existe o EPIRB (satélite, alcance global).

**O que fazer se acionar o DISTRESS acidentalmente?**

Imediatamente: chamar no Canal 16 e informar "Cancel Distress — False Alert — MMSI XXXXXXXXX". Reportar ao Guardião. O acionamento acidental não é crime, mas o silêncio após o falso alerta sim.

## Integração com outras notas

- [[AIS (Automatic Identification System)]]
- [[Buzina]]
- [[Bússola Eletrônica (Compass / HDG Sensor)]]
- [[Chartplotter / GPS / MFD]]
- [[EPIRB / Beacon de Emergência]]
- [[Estação de Vento / Anemômetro]]
- [[Mob — Man Overboard — Sistema de Detecção]]
- [[NAVEGAÇÃO (BB, BE e Alcançado)]]

## Perguntas que esta nota responde

- O que é Dsc — Chamada Seletiva Digital em instalações elétricas náuticas?
- Qual é a função de Dsc — Chamada Seletiva Digital na embarcação?
