---
title: "EPIRB / Beacon de Emergência"
note_type: "technical-note"
domain: "50_Navegacao_Instrumentacao_e_Comunicacao"
source_file: "EPIRB BEACON DE EMERGÊNCIA 33a19734f7fb81379431eaec13b474b3.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://www.nmea.org/standards.html"
  - "https://www.gov.br/anatel/pt-br/regulado/outorga/servico-movel-maritimo"
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
> EPIRB — Emergency Position Indicating Radio Beacon — Rádio-baliza de socorro em 406 MHz integrada ao sistema Cospas-Sarsat. É recurso de emergência de alta criticidade para cenários severos, especialmente quando a embarcação está fora do alcance útil de meios locais de comunicação.

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
| EPIRB obrigatório (offshore) | verificar conforme NORMAM e enquadramento da embarcação | SOLAS e demais regras aplicáveis conforme classe/uso |
| EPIRB registrado | Baixa conformidade | Maior conformidade |
| GPS integrado | Presente nos novos | Padrão (sem GPS = obsoleto) |
| Bateria substituída no prazo | Raramente verificado | Verificado em inspeções |
| PLB pessoal | Muito raro | Crescente (especialmente velejar solo) |
| MRCC Brasil (Salvamar) | Operacional | Recebe alertas internacionais |

**Muito comum no Brasil:** EPIRB instalado e nunca mais verificado.

**Mais presente em embarcações maiores/premium:** EPIRB Categoria I ACR + PLB para cada tripulante offshore.

## Normas e referências

- **NORMAM / DPC / Marinha do Brasil:** verificar requisito aplicável conforme tipo de embarcação e área de navegação
- **IMO Resolution A.810(19):** Performance standards for EPIRBs
- **COSPAS-SARSAT:** sistema de satélites e protocolo de transmissão
- **USCG 47 CFR Part 80:** EPIRB requirements (EUA — referência)
- **IEC 61097-2:** EPIRB — COSPAS-SARSAT system (padrão técnico)

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
