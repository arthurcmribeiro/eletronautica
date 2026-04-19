---
title: "EPIRB / Beacon de Emergência"
note_type: "technical-note"
domain: "50_Navegacao_Instrumentacao_e_Comunicacao"
source_file: "EPIRB BEACON DE EMERGÊNCIA 33a19734f7fb81379431eaec13b474b3.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "20"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
normas_citadas:
  - "IMO SOLAS Cap. IV — Radiocommunications"
  - "IMO Resolution A.810(19) — Performance standards for float-free satellite EPIRBs operating on 406 MHz"
  - "IMO Resolution A.1001(25) — Maritime Safety Information"
  - "Cospas-Sarsat C/S T.001 — Specification for Cospas-Sarsat 406 MHz Distress Beacons"
  - "Cospas-Sarsat C/S T.018 — Type Approval Standard for 406 MHz Distress Beacons"
  - "Cospas-Sarsat C/S G.005 — Guidelines on 406 MHz Beacon Coding, Registration, and Type Approval"
  - "IEC 61097-2 — Float-free satellite EPIRB operating on 406 MHz (Cospas-Sarsat)"
  - "IEC 61097-13 — 406 MHz satellite EPIRBs compatible with MEOSAR"
  - "IEC 61097-14 — AIS-SART (complementar ao EPIRB)"
  - "IEC 61108-1 — GNSS receivers — Global Positioning System (GPS)"
  - "IEC 60945 — Maritime navigation and radiocommunication equipment — General requirements"
  - "ITU-R M.633 — Transmission characteristics of a satellite EPIRB"
  - "ETSI EN 300 066 — Float-free maritime satellite EPIRBs (Europa)"
  - "RTCM SC-110 — EPIRB performance standards (EUA)"
  - "FCC 47 CFR Part 80 — Stations in the Maritime Services (EUA)"
  - "NORMAM-204/DPC — Serviço Móvel Marítimo e Serviço Móvel Marítimo por Satélite"
  - "NORMAM-201/DPC — Tráfego e Permanência de Embarcações"
  - "NORMAM-211/DPC — Embarcações de esporte e recreio"
  - "SISEPIRB / MRCC Brasil (Salvamar) — sistema de registro de EPIRB nacional"
  - "Resoluções ANATEL aplicáveis — registro de EPIRB e homologação de equipamentos"
  - "ABNT NBR 5410:2004 + emendas — Instalações elétricas de baixa tensão"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://www.nmea.org/standards.html"
  - "https://www.gov.br/anatel/pt-br/regulado/outorga/servico-movel-maritimo"
  - "https://www.cospas-sarsat.int/"
  - "https://www.imo.org/en/OurWork/Safety/Pages/GMDSS.aspx"
aliases:
  - "EPIRB BEACON DE EMERGÊNCIA"
  - "EPIRB / BEACON DE EMERGÊNCIA"
seo_title: "EPIRB / Beacon de Emergência"
seo_description: "EPIRB — Emergency Position Indicating Radio Beacon — Rádio baliza de socorro que transmite posição via satélite (Cospas-Sarsat) em 406 MHz com alcance global. É o úl."
seo_keywords:
  - "EPIRB"
  - "Beacon"
  - "Emergência"
  - "50 Navegacao Instrumentacao e Comunicacao"
geo_queries:
  - "O que é EPIRB / Beacon de Emergência em instalações elétricas náuticas?"
  - "Qual é a função de EPIRB / Beacon de Emergência na embarcação?"
related_notes:
  - "AIS (Automatic Identification System)"
  - "Buzina"
  - "Bússola Eletrônica (Compass / HDG Sensor)"
  - "Chartplotter / GPS / MFD"
  - "Dsc — Chamada Seletiva Digital"
  - "Estação de Vento / Anemômetro"
  - "Mob — Man Overboard — Sistema de Detecção"
  - "NAVEGAÇÃO (BB, BE e Alcançado)"
---

# EPIRB / Beacon de Emergência

> [!abstract] Resumo técnico
> EPIRB — Emergency Position Indicating Radio Beacon — Rádio-baliza de socorro em 406 MHz integrada ao sistema Cospas-Sarsat. É recurso de emergência de alta criticidade para cenários severos, especialmente quando a embarcação está fora do alcance útil de meios locais de comunicação. Registrada e com bateria em dia, é o último elo entre náufrago e resgate em qualquer ponto do globo.

> [!tip] Regra de decisão em 30 segundos
> 1. **EPIRB não substitui VHF DSC — complementa.** DSC cobre até 30–40 mn da costa; EPIRB cobre **todo o globo** via Cospas-Sarsat. Para costeira curta, VHF DSC é a primeira linha. Para travessia, offshore, pesca oceânica ou velejar solo: os dois são obrigatórios — **e registrados**.
> 2. **EPIRB sem registro é sinal mudo.** O 15HEX do beacon identifica a embarcação, o proprietário e os contatos de emergência no banco de dados nacional (SISEPIRB via Salvamar Brasil) e internacional (Cospas-Sarsat IBRD). Sem registro → MRCC recebe o alerta e não sabe quem procurar → horas ou dias a mais no SAR.
> 3. **GPS integrado é requisito moderno, não luxo.** Sem GPS, a primeira posição vem por Doppler em 60–90 min (LEOSAR) ou instantânea em constelação MEOSAR parcial. Com GPS integrado, o primeiro burst já contém lat/lon com precisão de 100 m. Diferença entre minutos e horas no mar.
> 4. **Categoria I (float-free hidrostático) para alto-mar; Categoria II (manual) para costeiro curto.** Cat I libera automaticamente se o barco afundar; Cat II depende de alguém ativá-lo. Para travessia, Cat I no suporte externo é o padrão.
> 5. **Bateria do EPIRB tem validade impressa — 5 a 10 anos.** Após o prazo, autonomia de 48h não é garantida. Substituição é feita pelo fabricante (ou importador autorizado); não é pilha de loja de conveniência.
> 6. **Suporte hidrostático (hidrostat) também tem validade.** 2 a 5 anos conforme modelo. Mecanismo de liberação envelhece em ambiente salino — trocar no prazo, não esperar inspeção falhar.
> 7. **Ativação acidental é protocolo obrigatório, não opcional.** Em no máximo 5 min: desligar EPIRB → Canal 16 VHF → "CANCEL DISTRESS — FALSE ALERT — [embarcação], [MMSI], [posição]" → contactar MRCC (Salvamar +55-21-2104-6119). Silêncio após falso alerta = multa + investigação.
> 8. **Teste mensal é pelo botão TEST do fabricante, nunca pelo botão DISTRESS.** Modo teste simula o beacon com identificação diferente. Ativar distress real "para testar" aciona cadeia SAR e gera falso alerta registrado internacionalmente.
> 9. **PLB é pessoal, não substitui o EPIRB da embarcação.** Personal Locator Beacon tem autonomia menor (24h vs 48h), antena menor, sem liberação automática. Em velejar solo, pesca esportiva ou multitripulação offshore: cada tripulante com PLB **+** EPIRB fixo é a arquitetura recomendada.

> [!danger] Quando chamar um especialista
> - **Registro ou atualização do EPIRB após compra, transferência ou mudança de proprietário:** processo via SISEPIRB (Salvamar) e Cospas-Sarsat IBRD. Erro no cadastro = resgate direcionado para embarcação errada. Despachante naval ou importador autorizado fazem o procedimento.
> - **Troca de bateria ou substituição do hidrostat:** serviço do fabricante ou representante autorizado. Abrir o EPIRB sem ferramenta correta rompe a vedação IP68 e invalida a certificação Cospas-Sarsat. Não é manutenção DIY.
> - **EPIRB ativado acidentalmente e não cancelado a tempo:** MRCC e Aeronaves/embarcações SAR são mobilizadas. Contato imediato com Salvamar Brasil, preservar o equipamento íntegro, aguardar laudo técnico do fabricante. Implicação legal real.
> - **EPIRB com LED de status intermitente anormal, falha no self-test ou comunicação errada com chartplotter (AIS-SART):** laudo do fabricante. Manter desligado até diagnóstico. Operar um beacon defeituoso em emergência real = pior cenário possível.
> - **Instalação de EPIRB Cat I em barco com tug-top metálico ou fly bridge cobertos:** antena precisa ter visada do céu. Metal/fibra de vidro carbonada bloqueiam o sinal 406 MHz. Engenheiro náutico dimensiona o suporte externo correto.
> - **Frotas comerciais ou charter com múltiplos EPIRBs sob mesmo CNPJ:** gestão de vencimentos, registros, inspeções periódicas, histórico de testes. Empresa especializada em equipamentos de segurança marítima.
> - **Importação direta de EPIRB dos EUA ou Europa sem homologação Anatel:** beacon transmite em 406 MHz, mas o canal está regulado pela Anatel. Equipamento não homologado pode ter firmware do país de origem (código de país errado no 15HEX) — resgate mobilizado para país errado.
> - **Perícia de sinistro marítimo envolvendo EPIRB (beacon ativou e barco não foi encontrado, ou ativou tarde):** preservar todo o conjunto (beacon + suporte + hidrostat), documentar história de manutenção, logs do fabricante. Perícia técnica e jurídica especializada.
> - **Embarcação SOLAS ou sob GMDSS Área A2/A3/A4:** EPIRB é apenas um dos componentes (EPIRB + SART + NAVTEX + Inmarsat). Instalação, teste e inspeção por prestador homologado DPC + órgão de bandeira.

## O que é

EPIRB (Emergency Position Indicating Radio Beacon) é uma rádio baliza de emergência que, ao ser ativada, transmite um sinal de socorro em 406 MHz para o sistema de satélites Cospas-Sarsat. O sistema detecta, decodifica e retransmite o alerta para o MRCC (Maritime Rescue Coordination Centre) mais próximo com as seguintes informações:

- Identificação única da embarcação (código de 15 dígitos encodado)
- Posição GPS (modelos com GPS interno integrado)
- Natureza da emergência (socorro marítimo)

## Função

- Sinalização de socorro em emergência marítima severa (naufrágio, pessoa a bordo em risco de vida)
- Cobertura global — funciona em alto mar, longe de toda cobertura VHF e celular
- Identificação da embarcação pelo MRCC para mobilização de busca e resgate
- Localização mais rápida e precisa quando o modelo possui GNSS integrado e consegue fix válido no momento da ativação
- Operação autônoma: flutua e transmite automaticamente ao ser ativado na água (tipo EPIRB automático)

## Como aparece na prática

Embarcações offshore e de cruzeiro: EPIRB instalado em suporte hidrostático na parte exterior da embarcação. Se o barco afundar, o EPIRB flutua, o mecanismo hidrostático o libera automaticamente e começa a transmitir.

Embarcações costeiras: EPIRB portátil guardado dentro da embarcação, ativado manualmente em emergência.

O EPIRB transmite continuamente durante 48 horas mínimas — tempo suficiente para o resgate ser organizado.

## Fundamentos mínimos

| Parâmetro | Detalhe |
| --- | --- |
| Frequência de transmissão | 406 MHz (satélite) + 121.5 MHz (homing) |
| Potência de transmissão | 5W (406 MHz) |
| Sistema de satélites | Cospas-Sarsat (LEO + GEO + MEO) |
| Tempo de alerta ao MRCC | depende da constelação disponível, do tipo de beacon, da cobertura e da disponibilidade de posição válida |
| Autonomia da bateria | Mínimo 48 horas de transmissão |
| Temperatura de operação | -20°C a +55°C |
| Flutuabilidade | Positiva (flutua) |
| Resistência à imersão | IP68 (10m/1h mínimo) |
| GPS integrado | Sim (modelos modernos — recomendado) |
| Vida útil da bateria | 5–10 anos (substituição obrigatória) |

## Categorias de EPIRB

| Categoria | Ativação | Instalação | Uso |
| --- | --- | --- | --- |
| **Categoria I** | Automática (hidrostático) + manual | Suporte externo com liberação hidrostática | Offshore, alto mar |
| **Categoria II** | Manual | Qualquer local | Costeiro, portátil |
| **PLB (Personal Locator Beacon)** | Manual | Pessoal (colete, cinturão) | Complementar ao EPIRB |

**O porte obrigatório de EPIRB e a categoria aplicável devem ser confirmados na regulamentação vigente para a embarcação, área de navegação e enquadramento operacional.**

## Registro — obrigatório e crítico

O EPIRB possui identificação codificada que precisa estar corretamente registrada e associada à embarcação para que a resposta SAR seja rápida e precisa.

**Registro no Brasil:**

- Via Marinha do Brasil (SALVAMAR) — sistema SISEPIRB
- Registrar: nome da embarcação, MMSI, dados do proprietário, contatos de emergência
- Atualizar sempre que trocar de embarcação ou dados de contato

**Consequência de não registrar:** o MRCC recebe o sinal mas não consegue identificar a embarcação nem os contatos de emergência — demora muito mais para organizar o resgate.

## Sistema Cospas-Sarsat — como funciona

```jsx
EPIRB ativado → transmissão em 406 MHz
→ Satélites LEO (órbita baixa) / GEO (geoestacionário) / MEO (GPS)
→ Estação de rastreamento terrestre (LUT — Local User Terminal)
→ Centro de Controle de Missão (MCC)
→ MRCC Brasil (Salvamar) / USCG / outros
→ Mobilização de busca e resgate
```

**Tempo de resposta:**

- Beacons com GNSS integrado tendem a entregar localização útil mais rapidamente
- Sem posição válida, a localização pode depender mais de processamento do sistema e de geolocalização indireta
- Modelos com GNSS integrado são preferíveis para reduzir incerteza e tempo de localização

## Marcas e modelos

| Marca | Modelo | Categoria | GPS integrado |
| --- | --- | --- | --- |
| **ACR** | GlobalFix Pro | Cat I | Sim |
| **ACR** | RapidFix | Cat I | Sim |
| **McMurdo** | Smartfind E8 | Cat I | Sim |
| **McMurdo** | Smartfind Plus | Cat II | Sim |
| **Ocean Signal** | E100G | Cat I | Sim |
| **Kannad** | SafePro | Cat I | Sim |
| **ACR** | ResQLink 400 | PLB | Sim |

**No Brasil:** ACR e McMurdo são os mais comuns. Importados dos EUA ou Europa.

## Problemas mais frequentes

| Problema | Causa raiz provável |
| --- | --- |
| EPIRB ativado acidentalmente | Ativação manual inadvertida, imersão acidental durante lavagem |
| Bateria vencida | Não substituída no prazo (5–10 anos conforme modelo) |
| EPIRB não registrado | Proprietário desconhecia a obrigação |
| GPS sem fix no momento da ativação | Sem visibilidade de satélites (deck metálico cobrindo o EPIRB) |
| Suporte hidrostático com problema | Mecanismo de liberação enferrujado → não libera automaticamente |
| Testes inadvertidos | Ativação durante manutenção sem seguir protocolo correto |

## Causas raiz

**Bateria vencida:** cada EPIRB tem data de validade da bateria impressa. Após esse prazo, a autonomia de 48h não é garantida. O EPIRB parece funcional mas pode parar de transmitir horas após ativação em emergência.

**Suporte hidrostático degradado:** o mecanismo de liberação automática depende de componentes que envelhecem em ambiente salino. Deve ser inspecionado e substituído conforme critérios e intervalos do fabricante; não convém improvisar manutenção que altere seu funcionamento certificado.

## Diagnóstico e manutenção

```jsx
Verificação regular (mínimo anual):
Passo 1: Verificar data de validade da bateria (impressa no EPIRB)
Passo 2: Verificar data de validade do suporte hidrostático (se Categoria I)
Passo 3: Verificar que o EPIRB está registrado (confirmar no banco de dados)
Passo 4: Verificar LED de status (maioria pisca regularmente indicando OK)
Passo 5: Inspecionar o mecanismo do suporte hidrostático (liberação livre)
Passo 6: Verificar que o GPS do EPIRB ainda funciona (botão de self-test)

Ativação acidental (protocolo obrigatório):
Passo 1: Desligar o EPIRB imediatamente
Passo 2: Ligar o VHF e chamar no Canal 16: informar o falso alerta
Passo 3: Contatar o MRCC Brasil (Salvamar) pelo canal adequado
Passo 4: O falso alerta é responsabilidade do proprietário — reportar é obrigatório
```

## Boas práticas profissionais

- Registrar o EPIRB imediatamente após a compra (antes de qualquer saída)
- Verificar a data de validade da bateria antes de cada temporada
- Instalar o EPIRB Categoria I no suporte externo correto (não dentro da embarcação)
- Cobrir com tampa antipoeira quando não em uso (previne ativação acidental)
- Treinar toda a tripulação no uso correto e no protocolo de ativação acidental

## Cuidados de instalação

- Instalar em suporte externo homologado pelo fabricante
- Suporte deve ser do tipo quick-release (liberação manual rápida + liberação hidrostática automática)
- Posição: local de fácil acesso, mas não sujeito a ondas constantes (evita ativação acidental)
- Antena deve ter linha de visão para o céu (não obstruída por metal)
- Verificar que o suporte está bem fixado à estrutura da embarcação

## Cuidados de uso

- Nunca ativar para teste (protocolo de teste especial do fabricante — diferente da ativação real)
- Verificar data de validade antes de qualquer saída offshore
- Manter atualizado o registro com dados corretos de contato de emergência
- Em caso de ativação acidental: reportar imediatamente ao MRCC

## Erros comuns

- Não registrar no banco de dados nacional
- Não substituir a bateria no prazo
- Instalar Categoria I dentro da embarcação (não flutua para fora se o barco afundar)
- Ativar fora do procedimento de teste do fabricante, gerando falso alerta e mobilização indevida de busca e salvamento
- Usar EPIRB vencido acreditando que ainda funciona

## Relação com outros sistemas

- **VHF DSC:** complementar — VHF para costais, EPIRB para offshore. VHF DSC alcance 20–40nm; EPIRB: global
- **AIS:** transponder de visibilidade mas não de socorro direto
- **PLB:** equipamento pessoal — complementar ao EPIRB da embarcação
- **SART (Search and Rescue Transponder):** auxiliar no homing durante busca e resgate
- **GPS do chartplotter:** EPIRB tem GPS próprio — independente do chartplotter

## Brasil x Internacional

| Aspecto | Brasil | Internacional |
| --- | --- | --- |
| EPIRB obrigatório (offshore) | verificar conforme NORMAM e enquadramento da embarcação | SOLAS (edição a verificar) e demais regras aplicáveis conforme classe/uso |
| EPIRB registrado | Baixa conformidade | Maior conformidade |
| GPS integrado | Presente nos novos | Padrão (sem GPS = obsoleto) |
| Bateria substituída no prazo | Raramente verificado | Verificado em inspeções |
| PLB pessoal | Muito raro | Crescente (especialmente velejar solo) |
| MRCC Brasil (Salvamar) | Operacional | Recebe alertas internacionais |

**Muito comum no Brasil:** EPIRB instalado e nunca mais verificado.

**Mais presente em embarcações maiores/premium:** EPIRB Categoria I ACR + PLB para cada tripulante offshore.

## Glossário rápido

- **EPIRB (Emergency Position Indicating Radio Beacon):** rádio-baliza de socorro em 406 MHz via satélite Cospas-Sarsat, específica para embarcações.
- **PLB (Personal Locator Beacon):** equivalente pessoal do EPIRB, menor, menor autonomia (24h típico), ativação manual.
- **ELT (Emergency Locator Transmitter):** equivalente aeronáutico do EPIRB.
- **Cospas-Sarsat:** sistema internacional de satélites para distress de beacons 406 MHz. Resultado da cooperação CA-FR-RU-US (anos 80) expandido mundialmente.
- **406 MHz:** frequência exclusiva dos beacons de distress. Burst digital de 0,5 s a cada 50 s.
- **121,5 MHz:** frequência de **homing** analógico auxiliar para as equipes de busca locais (aeronave ou embarcação SAR). Não tem mais função de alarme via satélite desde 2009.
- **243 MHz:** homing militar (legado).
- **LEOSAR:** satélites Cospas-Sarsat em órbita baixa (Low Earth Orbit). Detectam por efeito Doppler — podem demorar 60–90 min para 1º fix.
- **GEOSAR:** satélites geoestacionários (GEO). Alertam quase instantaneamente, mas **não** geram posição sozinhos (sem Doppler).
- **MEOSAR:** satélites em órbita média (GPS/Galileo/GLONASS). Geram posição instantânea por trilateração. Padrão moderno.
- **Cospas-Sarsat Return Link:** canal de retorno que confirma ao beacon (via satélite/Galileo) que o alerta foi recebido. Beacons modernos têm LED específico.
- **15HEX:** identificação única do beacon em 15 caracteres hexadecimais. Contém country code + model + serial.
- **UIN (Unique Identifier Number):** mesmo que 15HEX.
- **Country Code (MID):** 3 primeiros dígitos do MMSI; código do país do beacon deriva do MID. Brasil: 710–719.
- **Hex ID / Beacon ID:** mesmo que 15HEX.
- **IBRD (International Beacon Registration Database):** banco de dados internacional Cospas-Sarsat para beacons sem registro nacional.
- **SISEPIRB (Salvamar Brasil / MRCC Brasil):** sistema nacional brasileiro de registro de EPIRB.
- **MRCC (Maritime Rescue Coordination Centre):** centro coordenador de busca e salvamento marítimo. No Brasil: Salvamar Brasil (Marinha do Brasil, Rio de Janeiro).
- **LUT (Local User Terminal):** estação de rastreamento terrestre que recebe os sinais Cospas-Sarsat e os processa.
- **MCC (Mission Control Centre):** centro de controle de missão Cospas-Sarsat que coordena LUTs e encaminha alertas a MRCCs.
- **SAR (Search and Rescue):** busca e salvamento marítimo.
- **SART (Search And Rescue Transponder):** respondedor radar 9 GHz usado a bordo de balsa salva-vidas, complementar ao EPIRB.
- **AIS-SART:** variante AIS do SART — mostra marcador visual em chartplotters AIS.
- **NAVTEX:** serviço de boletins meteorológicos e de segurança em texto (MF 518 kHz).
- **Cat I (Categoria I):** EPIRB montado em suporte externo com liberação hidrostática automática + manual. Float-free.
- **Cat II (Categoria II):** EPIRB manual, guardado dentro do barco.
- **Float-free:** capacidade de flutuar livremente fora do barco após liberação automática.
- **Hidrostato / hidrostat / HRU (Hydrostatic Release Unit):** mecanismo que libera o EPIRB a 2–4 m de profundidade por pressão hidrostática.
- **Suporte quick-release:** suporte com liberação manual rápida para uso imediato.
- **Self-test (botão TEST):** função que verifica transmissor, bateria e GPS sem acionar alerta real. Faz burst em frequência de teste, não em 406 MHz operacional.
- **GNSS-encoded position:** beacon envia coordenadas geradas pelo próprio GPS no protocolo Cospas-Sarsat.
- **Doppler-only / Legacy beacon:** beacon sem GPS — depende de LEOSAR para posição.
- **Registration renewal:** renovação do registro (em geral bianual). EPIRB não registrado ou com dados desatualizados entra em "orphan alerts".
- **Orphan alert:** alerta recebido sem registro conhecido; SAR demora mais para mobilizar.
- **False alert:** alerta indevido, acidental ou sem emergência real. Obrigatório cancelar no Canal 16 + MRCC.
- **Drill / exercício:** teste pré-autorizado com MRCC; não é self-test.
- **Bateria primária (lítio-clorato, LiMnO2 ou LiSO2):** química específica de alta energia para longa vida útil em standby.
- **Antena helicoidal quadrifilar:** antena típica do EPIRB, omnidirecional, impermeável.
- **Duty cycle 406 MHz:** pulso de 0,5 s a cada 50 s — economiza bateria e permite correlação Doppler.
- **Duty cycle 121,5 MHz:** contínuo ou modulado para homing local.
- **SOLAS Cap. IV:** base dos requisitos de GMDSS em navios SOLAS.
- **GMDSS Area A1/A2/A3/A4:** zonas de cobertura por capacidades de equipamento (A1 = VHF DSC costeiro; A4 = polar com HF).
- **EPIRB de Classe 1 / 2 (legado IMO):** terminologia antiga distinguia faixa de temperatura de operação (−20 °C vs −40 °C).
- **Proof load test:** teste de resistência mecânica do suporte.
- **FCC 47 CFR Part 80:** regulamentação americana para estações marítimas (referência).
- **Anatel — homologação:** EPIRB importado deve estar homologado pela Anatel para funcionar legalmente no Brasil.
- **Decommissioning:** procedimento de descarte seguro do EPIRB com remoção da bateria de lítio.

## Normas e referências

- **SOLAS, Cap. IV — Radiocommunications** — convenção IMO que fundamenta o GMDSS.
- **IMO Resolution A.810(19)** — *Performance standards for float-free satellite EPIRBs operating on 406 MHz.*
- **IMO Resolution A.1001(25)** — Maritime Safety Information (contexto GMDSS).
- **Cospas-Sarsat C/S T.001** — *Specification for Cospas-Sarsat 406 MHz Distress Beacons.* Especificação técnica fundamental.
- **Cospas-Sarsat C/S T.018** — *Type Approval Standard for 406 MHz Distress Beacons.*
- **Cospas-Sarsat C/S G.005** — *Guidelines on 406 MHz Beacon Coding, Registration, and Type Approval.*
- **IEC 61097-2** — *Float-free satellite EPIRB operating on 406 MHz.* Norma técnica para EPIRB marítimo.
- **IEC 61097-13** — *406 MHz satellite EPIRBs compatible with MEOSAR.* EPIRB moderno com Galileo Return Link.
- **IEC 61097-14** — *AIS-SART.* SART via AIS — complemento ao EPIRB.
- **IEC 61108-1** — *GNSS receivers — GPS.* Requisitos para GNSS integrado.
- **IEC 60945** — *Maritime navigation and radiocommunication equipment — General requirements.*
- **ITU-R M.633** — *Transmission characteristics of a satellite EPIRB.*
- **ETSI EN 300 066** — *Float-free maritime satellite EPIRBs* (Europa).
- **RTCM SC-110** — EPIRB performance standards (EUA).
- **FCC 47 CFR Part 80** — *Stations in the Maritime Services* (regulamentação americana — referência internacional).
- **NORMAM-204/DPC** — *Serviço Móvel Marítimo e Serviço Móvel Marítimo por Satélite.*
- **NORMAM-201/DPC** — *Tráfego e Permanência de Embarcações.*
- **NORMAM-211/DPC** — *Embarcações de esporte e recreio.*
- **SISEPIRB / MRCC Brasil (Salvamar)** — sistema nacional de registro do EPIRB; contato 24h para falso alerta e distress.
- **Resoluções ANATEL aplicáveis** — homologação do equipamento para uso em águas jurisdicionais brasileiras.
- **ABNT NBR 5410:2004 + emendas** — *Instalações elétricas de baixa tensão.* Complemento nacional para suporte e iluminação associada.

## Como ensinar este tópico

**Sequência recomendada:**

1. Comparar EPIRB com VHF DSC: alcance, situação de uso, complementaridade
2. Explicar o sistema Cospas-Sarsat com diagrama
3. Mostrar a importância do registro (caso real: EPIRB sem registro → demora no resgate)
4. Demonstrar o procedimento de verificação anual
5. Protocolo de falso alerta (responsabilidade legal)

**Mensagem central:** "O VHF te salva perto da costa. O EPIRB te salva em qualquer lugar do mundo. Para offshore, os dois são obrigatórios — e registrados."

## Ideias de vídeos

- "EPIRB: o que é, como funciona e por que é obrigatório offshore"
- "Registrando seu EPIRB no Brasil — passo a passo pelo Salvamar"
- "EPIRB vs VHF DSC: a diferença que salva vidas em alto mar"
- "Manutenção do EPIRB: bateria, suporte hidrostático e registro"
- "O que fazer quando o EPIRB dispara acidentalmente"

## Diagramas sugeridos

- Fluxo do sistema Cospas-Sarsat: EPIRB → satélite → LUT → MCC → MRCC → resgate
- Comparativo de alcance: VHF DSC (20–40nm) vs EPIRB (global)
- Diagrama de instalação: suporte hidrostático → liberação automática ao afundar
- Comparativo de tipos: EPIRB Cat I vs Cat II vs PLB (quando usar cada)
- Timeline de alerta: com GPS integrado (<5min) vs sem GPS (até 2h)

## FAQ

**O EPIRB funciona em qualquer lugar do mundo?**

Sim — o sistema Cospas-Sarsat tem cobertura global (exceto os polos com alguns buracos de cobertura). Esta é a principal vantagem sobre o VHF.

**Posso usar o EPIRB em mar próximo?**

O EPIRB é o último recurso — para qualquer emergência grave. Mas se você ainda tem cobertura VHF (perto da costa), use o DSC Canal 70 primeiro. EPIRB quando VHF não alcança ou falhou.

**O PLB substitui o EPIRB da embarcação?**

Não completamente. PLB é menor e para uso pessoal (coletes, cinturão). Tem autonomia menor. O EPIRB da embarcação tem maior potência, maior autonomia e liberação automática ao afundar.

**Posso vender meu EPIRB e comprar outro?**

Sim. Ao vender: cancelar o registro. O novo comprador deve registrar em seu nome. EPIRB com registro de outra pessoa em emergência confunde o MRCC.

**Quanto custa substituir a bateria?**

Depende do modelo. Tipicamente US$150–300 (importação). Algumas empresas fazem a substituição completa. Verificar com o fabricante ou importador nacional.

## Integração com outras notas

- [[AIS (Automatic Identification System)]]
- [[Buzina]]
- [[Bússola Eletrônica (Compass / HDG Sensor)]]
- [[Chartplotter / GPS / MFD]]
- [[Dsc — Chamada Seletiva Digital]]
- [[Estação de Vento / Anemômetro]]
- [[Mob — Man Overboard — Sistema de Detecção]]
- [[NAVEGAÇÃO (BB, BE e Alcançado)]]

## Perguntas que esta nota responde

- O que é EPIRB / Beacon de Emergência em instalações elétricas náuticas?
- Qual é a função de EPIRB / Beacon de Emergência na embarcação?
