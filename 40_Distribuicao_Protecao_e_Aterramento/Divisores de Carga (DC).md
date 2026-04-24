---
title: "Divisores de Carga (DC)"
note_type: "technical-note"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "DIVISORES DE CARGA (DC) 2f419734f7fb831cad5d81f3bc9880ae.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "61"
tier_fase_6: "A"
reviewed_on: "2026-04-21"
review_jurisdiction:
  - "Brasil"
  - "internacional"
review_level: "engineering-curated"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
  - "https://www.victronenergy.com/upload/documents/Datasheet-Cyrix-Battery-Combiners.pdf"
normas_citadas:
  - "ABYC E-11 (AC and DC Electrical Systems on Boats)"
  - "ABYC E-10 (Storage Batteries) — interligação e isolação de bancos"
  - "ABYC A-31 (Battery Chargers and Inverters)"
  - "ABYC E-13 (Lithium Ion Batteries) — banco Li-Fe"
  - "ABYC E-30 (Electric Propulsion Systems)"
  - "ISO 10133:2012 (Small craft — Electrical systems — Extra-low-voltage DC)"
  - "ISO 16315:2016 (Small craft — Electric propulsion system)"
  - "ISO 18246:2015 (Electric mopeds and motorcycles — Safety specifications — Conductive connection to an external electric power supply) — referência de isolamento galvânico"
  - "IEC 60364-7-712 (Photovoltaic power supply systems) — aplicável em solar a bordo"
  - "IEC 62040 (Uninterruptible power systems — UPS)"
  - "IEC 62619 (Secondary cells and batteries containing alkaline or other non-acid electrolytes — Safety requirements for secondary lithium cells and batteries for use in industrial applications)"
  - "IEC 62485-2 (Safety requirements for secondary batteries — Stationary batteries)"
  - "IEC 60529 (IP Code)"
  - "UL 1236 (Battery Chargers for Charging Engine-Starter Batteries)"
  - "UL 1741 (Inverters, Converters, Controllers — interação com banco)"
  - "UL 458 (Power Converters/Inverters for Land Vehicles and Marine Crafts)"
  - "UL 2743 (Portable Power Packs) — parcialmente aplicável a DC-DC"
  - "SAE J537 (Storage Batteries)"
  - "SAE J1495 (Test procedure for battery separators)"
  - "SAE J1766 (Electric and hybrid vehicle battery systems crash integrity testing)"
  - "NFPA 70 (NEC) art. 480 (Storage Batteries) e art. 706 (Energy Storage Systems)"
  - "NFPA 855 (Installation of Stationary Energy Storage Systems)"
  - "ABNT NBR 5410 (Instalações elétricas de baixa tensão)"
  - "ABNT NBR 14039 (Instalações elétricas de média tensão)"
  - "ABNT NBR 16690 (Instalação fotovoltaica — arranjos elétricos)"
  - "NORMAM-05/DPC (Embarcações de esporte e recreio)"
  - "NORMAM-01/DPC (Embarcações em navegação marítima)"
  - "USCG 33 CFR 183 Subpart I"
family_clusters:
  - "ABYC-USCG (EUA)"
  - "ISO-IEC (internacional)"
  - "ABNT-NORMAM (Brasil)"
  - "UL-NFPA (EUA industrial)"
aliases:
  - "DIVISORES DE CARGA (DC)"
  - "Isolação de bancos"
  - "Battery isolator"
  - "ACR / VSR"
  - "Charge splitter"
seo_title: "Divisores de carga DC: ACR, isoladores, seletores e DC-DC em embarcações"
seo_description: "Guia técnico para separar e carregar bancos DC em embarcações sem confundir ACR, isolador por diodo/FET, chave seletora e carregador DC-DC."
seo_keywords:
  - "divisor de carga DC embarcação"
  - "ACR VSR náutico"
  - "isolador de baterias"
  - "carregador DC-DC banco de baterias"
geo_queries:
  - "Qual a diferença entre ACR, isolador de baterias e carregador DC-DC?"
  - "Como separar banco de partida e banco de serviço em uma embarcação?"
  - "Posso misturar chumbo e lítio com ACR?"
related_notes:
  - "Alternador (DC)"
  - "Bancos de Bateria"
  - "BMS — Battery Management System"
  - "Carregador de Bateria (AC To DC)"
  - "Chaves Gerais (DC)"
  - "Lítio LiFePO4 — Instalação e Cuidados Específicos"
  - "Monitor de Bateria - BMV - Shunt"
  - "Tipos de Bateria"
---

# Divisores de Carga (DC)

> [!abstract] Resumo técnico
> "Divisor de carga" (ou "separador de carga") é um nome guarda-chuva para estratégias de separação e compartilhamento de carga entre bancos DC. O guarda-chuva abre em duas famílias principais — **combinadores** (juntam bancos sob tensão de carga e separam em repouso: ACR/VSR) e **isoladores** (mantêm saídas elétricas separadas permanentemente: diodo/FET) — mais duas soluções periféricas (chave seletora manual e carregador DC-DC). Em engenharia, é essencial não tratar os quatro como equivalentes: cada um resolve um problema diferente. ABYC E-10 e E-13 (para Li-Fe) + ISO 10133 orientam arquitetura de múltiplos bancos; a regra prática é que **banco de partida e banco de serviço devem ter química, perfil de uso e caminho de carga distintos**, e a interligação entre eles precisa ser controlada por dispositivo com lógica explícita, não por chave "BOTH" permanente.
>
> **Evolução histórica resumida**: isolador por diodo (anos 70-90, queda de 0,6-0,9 V) → isolador por FET (anos 90-2000, queda < 0,1 V) → ACR/VSR (combinadores automáticos eletromecânicos/eletrônicos, 2000-hoje) → DC-DC charger (2010-hoje, para cenários com químicas mistas). **Combinador moderno substituiu o isolador por diodo em quase toda aplicação náutica de recreio** porque a queda de tensão do diodo fazia o alternador trabalhar em tensão insuficiente para completar o SoC do banco, acelerando sulfatação em chumbo. As referências comerciais de combinador são hoje **Blue Sea (EUA)** — linha ML-ACR, SI-ACR, ACR — e **Arieltek (Brasil)** — linha DVSR/Automotive VSR — além de Victron Cyrix, Sterling Power ProSplit-R, BEP VSR, Perko Smart Battery Switch.

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **4 soluções ≠ intercambiáveis** — chave seletora (manual), ACR/VSR (automático simples), isolador diodo/FET (topologia), DC-DC (perfil de carga por banco). Escolha pela arquitetura, não pelo preço.
> 2. **Chumbo + chumbo homogêneo (mesma química/idade/capacidade)**: ACR/VSR basta — Blue Sea ML-ACR, Victron Cyrix-ct, BEP VSR.
> 3. **Chumbo + Lítio OU bancos heterogêneos**: carregador DC-DC obrigatório — Victron Orion-Tr Smart, Sterling Power, Mastervolt Mass ChargeMaster DC-DC; ACR mistura químicas e arruína ambos.
> 4. **Isolador diodo** (Hellroaring, Yandina) = obsoleto por queda de 0,6-0,9 V; **isolador FET** (Sterling PDR) = aceitável mas tensão do alternador precisa ser "battery-to-battery sensed".
> 5. **Banco de partida sempre isolado do banco de serviço em repouso** — evita descarga via carga parasita; ACR abre com V < 12,8 V em 12 V (chumbo) ou V < 13,3 V (lítio).
> 6. **Cabo entre bancos protegido nas DUAS pontas** — fusível MRBF/ANL em cada polo, pois cada banco pode ser a fonte em curto (ABYC E-11.4.7).
> 7. **Shunt de monitor UM por banco** — monitor de bateria compartilhado entre bancos (BMV em "Load") falseia SoC se os bancos combinam automaticamente.
> 8. **Alternador com lítio = load dump obrigatório** — se o BMS abrir sob carga, a tensão do alternador dispara e queima diodos; use alternador com regulador externo Balmar/Wakespeed/Mastervolt Alpha Pro com proteção de load dump, ou DC-DC que desacople.
> 9. **Modo emergência documentado** — a topologia deve permitir paralelo manual temporário para partida (botão "cross-over", chave 1-2-BOTH com AFD); nunca deixe permanente.

> [!danger] Quando chamar um especialista
> Estes 9 cenários exigem engenheiro elétrico náutico ou integrador:
> 1. **Conversão chumbo → lítio com manutenção do alternador original** — exige análise de regulador, load dump, BMS disconnect e usualmente retrofit com DC-DC ou regulador externo Balmar Max Charge / Wakespeed WS500.
> 2. **Banco Li-Fe > 400 Ah ou > 48 V** — ABYC E-13 exige BMS com contator classe T ou soft-disconnect, pre-charge resistor, alarme externo; arquitetura de divisão vira sistema BMS, não mais "divisor".
> 3. **Três ou mais bancos paralelos com químicas diferentes** — chumbo (start) + lítio (house) + chumbo de emergência (backup) + solar — gerenciamento multi-fonte exige Cerbo GX ou MasterBus com lógica de prioridade.
> 4. **Integração com energy storage system (ESS) de maré/solar > 5 kWh** — NFPA 855 passa a aplicar; exige estudo de propagação térmica, ventilação, separação física entre módulos.
> 5. **Propulsão elétrica/híbrida (tração > 10 kW)** — ISO 16315 e ABYC E-30; divisão entre banco de tração e banco house vira arquitetura crítica de segurança (faults em um banco não podem propagar ao outro).
> 6. **Retrofit de embarcação com alternador original não sensed (regulador interno tradicional)** — pode superaquecer com Li-Fe (BMS aceita corrente ilimitada até a temperatura) — exige alternador com sensor de temperatura ou desaceleração eletrônica.
> 7. **Sistema com BMS de diferentes fabricantes em paralelo** — comunicação CAN/Bluetooth entre BMS pode conflitar (Victron Lynx Smart BMS não fala com REC BMS ou JK BMS sem gateway); risco de abertura simultânea ou prioridade errada.
> 8. **Navio comercial sob classificadora** — IEC 62619 + regras de classe (DNV/Lloyd's) — divisor de recreio não é aceito.
> 9. **Falha recorrente de ACR oscilando, DC-DC superaquecendo, banco desbalanceando** — diagnóstico profissional com medição de perfil de corrente/tensão/temperatura ao longo de ciclo completo.

## O que esta nota realmente cobre

Na prática náutica, o termo "divisor de carga" (às vezes chamado "separador de carga") costuma ser usado de forma imprecisa. Aqui, ele será tratado como **arquitetura de gerenciamento entre bancos DC**, especialmente entre:

- banco de partida (start / engine);
- banco de serviço (house / domestic);
- bancos auxiliares ou dedicados (thruster, electronics, propulsão elétrica);
- fontes como [[Alternador (DC)]], [[Carregador de Bateria (AC To DC)]] e solar.

### Taxonomia — separador de carga como guarda-chuva

No uso técnico contemporâneo, **separador de carga** engloba qualquer dispositivo/estratégia que gerencie o caminho elétrico entre múltiplos bancos. Dentro desse guarda-chuva existem famílias distintas:

| Família | O que faz | Estado em repouso | Estado sob carga | Exemplo |
| --- | --- | --- | --- | --- |
| **Combinador** (ACR/VSR) | junta bancos AO DETECTAR tensão de carga | **separados** | **juntos** (paralelo transitório) | Blue Sea ML-ACR, Arieltek DVSR |
| **Isolador** (diodo/FET) | mantém saídas SEMPRE separadas | **separados** | **separados** (fonte distribui sem juntar) | Sterling PDR, legado Hellroaring |
| **Chave seletora manual** | operador escolhe qual banco | conforme o operador | conforme o operador | Blue Sea 9001e, Perko 8501 |
| **Carregador DC-DC** | converte e regula perfil de carga específico por banco | saída DC-DC desligada ou em standby | saída regula perfil CC-CV do destino | Victron Orion-Tr Smart, Sterling BB1230 |

**A confusão mais comum** no mercado brasileiro e internacional é chamar genericamente de "isolador" qualquer dispositivo com duas saídas, incluindo combinadores. Tecnicamente:

- **Combinador** (combiner / ACR / VSR / battery combiner): paraleliza os bancos quando a tensão sobe (carga em curso) e abre quando cai (consumo). O **terminal de bateria 1 fica ligado no terminal de bateria 2** por um contato mecânico ou FET durante a carga.
- **Isolador** (isolator / charge splitter / battery isolator): os bancos **NUNCA** se tocam eletricamente. A fonte (alternador, charger) alimenta cada banco por um caminho independente — tipicamente via diodo ou FET em série que permite corrente do alternador para o banco, mas bloqueia corrente reversa entre os bancos.

Essa diferença é fundamental para escolher o equipamento correto e entender o que acontece quando algo falha.

## Problema técnico que precisa ser resolvido

Quando a embarcação tem mais de um banco, a arquitetura precisa responder a quatro perguntas:

1. **Como garantir reserva para partida?** (banco de start não pode ser drenado pelo consumo do banco house).
2. **Como carregar múltiplos bancos sem criar desequilíbrios?** (alternador e charger veem tensão diferente de cada banco).
3. **Como compatibilizar químicas diferentes?** (perfil de carga de chumbo é CC-CV bulk+absorption+float; lítio é CC-CV com float baixo ou sem float).
4. **Como manter operação de emergência simples e previsível?** (paralelo manual para partida, sem virar topologia confusa).

Se a solução não responde a essas quatro perguntas, ela não está madura o suficiente.

## Tipos de solução e suas diferenças

### 1. Chave seletora manual

É a solução mais simples. O operador seleciona banco 1, banco 2, ambos ou off, conforme a arquitetura.

**Vantagens:**

- simplicidade;
- baixo custo;
- fácil entendimento em sistemas pequenos (< 100 Ah, < 24 V, sem lítio).

**Limitações:**

- depende de disciplina operacional (operador precisa lembrar de combinar/separar);
- não compensa perfil de carga;
- aumenta risco de erro humano (chave NÃO-AFD com motor ligado destrói alternador);
- não resolve adequadamente sistemas com lítio, alta corrente ou carga complexa.

**Exemplos:** Blue Sea 9001e (1-2-BOTH-OFF com AFD), Perko 8501.

### 2. ACR / VSR / combinador automático

Dispositivo que conecta bancos quando detecta tensão de carga (tipicamente > 13,3 V em 12 V) e os separa quando essa condição desaparece (tipicamente < 12,8 V em 12 V). É muito útil em sistemas chumbo-chumbo bem comportados e com alternador convencional.

**Vantagens:**

- operação automática (sem intervenção do operador);
- queda de tensão muito baixa quando fechado (< 0,1 V);
- boa relação custo-benefício em sistemas simples.

**Limitações:**

- não controla perfil de carga — quando combina, os bancos veem a mesma tensão, ruim para químicas diferentes;
- não substitui regulador inteligente;
- pode ser inadequado em arquiteturas com lítio, BMS ou alternadores sensíveis (BMS abre → load dump);
- pode combinar bancos em momentos que a estratégia do projeto não deseja (oscilação se a tensão flutuar perto do threshold).

**Exemplos:** Blue Sea ML-ACR (500 A), Blue Sea SI-ACR (120 A), Victron Cyrix-ct/Cyrix-i, BEP VSR, Sterling Power ProSplit-R.

### 3. Isolador por diodo ou FET

Recebe uma fonte e a distribui a bancos separados sem conectá-los diretamente entre si.

#### 3a. Isolador por diodo — a tecnologia legada (anos 70-90)

Usava **diodos retificadores** em série entre a fonte e cada banco. O diodo permite corrente "alternador → banco" mas bloqueia corrente reversa entre bancos. Era uma das poucas soluções disponíveis antes da eletrônica de potência barata.

**Por que foi substituído**:

- **queda de tensão de 0,6-0,9 V** (diodo comum silicon) ou 0,3 V (Schottky) — o alternador fornece 14,4 V, o banco recebe apenas 13,5-13,8 V → **absorption incompleta** → sulfatação progressiva em chumbo, vida útil reduzida em 30-50%;
- **sem compensação**, o banco nunca atinge SoC 100% (fica "eternamente" em 85-90%);
- alternadores modernos com "sensing" eram pouco disponíveis na época do diodo;
- dissipação térmica significativa (15-30 W por banco em corrente nominal 40-80 A) exigia dissipador volumoso;
- sem inteligência: não separa em consumo, não combina para emergência.

Ainda é encontrado em embarcações antigas (anos 80-90) como Yacht antigos, sailboats com instalação original.

**Exemplos legados**: Sterling Power Pro Diode Splitter, Hellroaring, Suresine (fora de fabricação), Powerstream Diode Isolator.

#### 3b. Isolador por FET — evolução do conceito (anos 90-2000)

Substitui o diodo por **MOSFET de potência** funcionando como chave quase-ideal: queda de **0,02-0,1 V** (10-20× menor que diodo). Dissipação térmica 3-5× menor.

**Vantagens** sobre o diodo:

- tensão efetiva de carga preservada (banco recebe praticamente 14,4 V do alternador);
- menor dissipação → gabinete menor e mais confiável;
- alguns modelos integram sensing automático ou battery-to-battery sensing;
- proteção contra sobrecorrente eletrônica.

**Limitações ainda presentes**:

- topologia continua sendo "uma fonte → N bancos sem conectar bancos entre si" → não permite combinar para emergência sem operação manual;
- alternador precisa ser "battery-to-battery sensed" ou o regulador vê tensão ligeiramente maior (FET drop) e reduz output prematuramente;
- não mede corrente por banco (monitor de bateria fica complicado);
- não corrige incompatibilidades entre químicas (só transporta a mesma tensão de carga para os dois bancos, que pode ser errada para o banco B se ele é de química diferente).

**Exemplos**: Sterling Power PDR (Pro Digital Regulator splitter), Yandina Combiner 100 (híbrido FET + temporizador).

#### Por que combinadores substituíram isoladores na maioria das aplicações

O **combinador (ACR/VSR)** resolve limitações históricas do isolador:

- **sem queda de tensão** (contato ou FET de alta corrente em paralelo, não em série) — banco recebe tensão plena do alternador;
- **separação automática em repouso** evita que um banco descarregue o outro por diferença de química/SoC;
- **simplicidade de cabeamento** (dois polos principais + um controle);
- **custo menor** para a mesma corrente (a partir dos anos 2000);
- **inteligência de combinação** (delay, histerese, override manual para emergência).

Para chumbo-chumbo homogêneo o combinador é simplesmente melhor que o isolador em tudo. Isolador por FET ainda é útil em cenários de nicho: saídas múltiplas de uma mesma fonte (3+ bancos alimentados por um alternador grande), ou onde se queira **garantir separação permanente** (bancos de química diferente sem DC-DC — mas aqui o DC-DC é a solução correta).

**Referências comerciais de combinador mais usadas**:

- **Blue Sea Systems (EUA)**: linha mais disseminada em recreio e pequeno comercial. ML-ACR (500 A contínuo, 700 A inrush, com override manual), SI-ACR (120 A), Add-A-Battery kit (9 V-32 V DC), BatteryLink 120 A/500 A. Padrão ABYC compliance, UL 1107 marine.
- **Arieltek (Brasil)**: fabricante nacional com boa presença em recreio brasileiro. Linha DVSR (Dual VSR) 125 A/250 A, Automotive VSR 140 A. Custo-benefício para retrofits no mercado BR, compatível com chumbo-chumbo em 12 V e 24 V.
- **Victron Energy (internacional)**: Cyrix-ct (120 A/230 A), Cyrix-i (intelligent 120 A/230 A/400 A), Cyrix Li-ct (200 A com lógica para Li-Fe em compatibilidade limitada). Integração com Cerbo GX e app VictronConnect.
- **Sterling Power (UK)**: ProSplit-R (relay-based combiner) e Pro Digital Regulator (FET isolator + regulator) para cenários onde o isolamento permanente é desejado.
- **BEP Marine** (filial Power Products): VSR 140 A com indicador LED.
- **Perko (EUA)**: Smart Battery Switch com combiner integrado.

Em instalação nova, raramente se justifica usar isolador por diodo. Isolador por FET permanece válido em aplicações muito específicas (alternador com 3-4 saídas dedicadas, aplicações de yacht comercial onde a separação permanente é regra de classe).

### 4. Carregador DC-DC

É a solução mais robusta quando se quer controlar de forma explícita o perfil de carga entre bancos diferentes ou quando a fonte primária não deve ser conectada diretamente ao banco de destino.

**Vantagens:**

- **perfil de carga definido** por banco (CC-CV específico, float, equalização);
- **melhor compatibilidade entre chumbo e lítio** (fontes incompatíveis são desacopladas);
- **desacoplamento elétrico e operacional** mais limpo (alternador não "vê" o lítio);
- **proteção do alternador** em muitas arquiteturas modernas (corrente máxima limitada = sem overload);
- pode **subir tensão** (12 V → 24 V) ou baixar (24 V → 12 V) entre bancos de tensões diferentes.

**Limitações:**

- custo maior (~4-10× o de um ACR);
- potência limitada pelo modelo escolhido (típicos 18 A, 30 A, 60 A; grandes até 90-120 A);
- exige projeto mais consciente de ventilação (dissipa 5-15% como calor), proteção (fusível nas duas entradas) e cabos;
- retardo de ativação (alguns modelos levam 2-5 s após engine-on a começar a carregar).

**Exemplos:** Victron Orion-Tr Smart (30 A), Sterling Power BB1230 (30 A), Mastervolt Mass ChargeMaster DC-DC, Redarc BCDC, Renogy DCC (híbrido solar + DC-DC).

## Tabela comparativa

| Solução | Custo | Queda V | Auto | Compat. química | Uso indicado |
| --- | --- | --- | --- | --- | --- |
| Chave manual | $ | 0,05 V | não | neutro | sistemas pequenos, recreio básico |
| ACR/VSR | $$ | 0,1 V | sim | só chumbo-chumbo | cruiser médio chumbo-chumbo |
| Isolador diodo | $$ | 0,6-0,9 V | sim | limitado | legado, sistemas antigos |
| Isolador FET | $$$ | 0,02-0,1 V | sim | limitado | saídas múltiplas do alternador |
| DC-DC | $$$$ | — (converte) | sim | lítio + chumbo ok | barcos modernos, retrofits |

## O erro mais comum

O erro mais recorrente é usar "divisor de carga" como se qualquer solução servisse para qualquer sistema. Isso é falso.

Exemplos:

- **ACR não é sinônimo de carregador DC-DC**;
- **chave manual não substitui gerenciamento automático** em sistemas complexos;
- **isolador FET não resolve, por si só**, um banco de lítio com BMS agressivo (BMS pode abrir e deixar alternador em load dump);
- **paralelar bancos de químicas diferentes sem estratégia** costuma gerar comportamento ruim e, em alguns casos, perigoso (chumbo puxa lítio para tensão baixa → BMS abre → load dump).

## Critérios corretos de escolha

### Separar por função

Antes de escolher o equipamento, definir:

- qual banco é de **partida** (start / engine — normalmente AGM ou flooded 100-200 Ah);
- qual banco é de **serviço** (house — pode ser AGM, GEL ou Li-Fe 200-600+ Ah);
- se existe banco dedicado a **thruster, eletrônica ou emergência** (Li-Fe em thruster é comum; emergência em AGM é comum);
- quais fontes carregam cada banco (alternador, charger AC, solar, gerador DC, hidrogerador);
- se haverá possibilidade de auxílio de partida entre bancos (botão "cross-over" manual).

### Verificar a química

Arquiteturas **chumbo-chumbo** (flooded-flooded, AGM-AGM, GEL-GEL, mistura chumbo) são mais tolerantes. Arquiteturas com [[Lítio LiFePO4 — Instalação e Cuidados Específicos]] exigem muito mais cuidado, especialmente quando há:

- **BMS que pode abrir o circuito** (HVC, LVC, overcurrent, overtemp);
- **alternador sem proteção contra load dump** (alternador original 80-100 A com regulador interno);
- **grande diferença de capacidade** entre bancos (start 100 Ah + house Li-Fe 600 Ah em ACR = start descarregado pelo consumo do house se o BMS abrir);
- **necessidade de perfil de carga específico** (Li-Fe pede absorption a 14,2-14,4 V por tempo definido, sem float; chumbo pede 14,4-14,8 V bulk + 13,5-13,8 V float).

### Verificar a fonte de energia

A escolha muda conforme a fonte principal:

- [[Alternador (DC)]] pede atenção a corrente, temperatura e resposta do regulador — com lítio, regulador externo Balmar/Wakespeed/Mastervolt é fortemente recomendado;
- [[Carregador de Bateria (AC To DC)]] já pode ter **saídas independentes** (Mastervolt Mass ChargeMaster 3 out, Victron Phoenix IP22 ou Skylla tem versões multi-output);
- **solar** pode exigir prioridade ou caminho próprio de carga (MPPT com saída para banco principal + DC-DC para secundário);
- **inversores/carregadores** podem introduzir lógica adicional (Victron Multiplus com carregador interno atende house; DC-DC a partir do house atende start).

### Verificar operação de emergência

Toda arquitetura com mais de um banco deve prever:

- **isolamento normal** (bancos separados em repouso);
- **meio claro de paralelo de emergência** (botão momentâneo tipo "emergency parallel", chave 1-2-BOTH com AFD, contactor Blue Sea ML-ACR com override);
- **documentação visível** para operação e manutenção (etiqueta ao lado da chave + diagrama unifilar a bordo).

## Falhas típicas em campo

As mais comuns são:

- **banco de partida sendo drenado** pelo banco de serviço (ACR não abre, seletora em BOTH permanente);
- **alternador trabalhando fora de sua zona segura** por conexão inadequada com lítio (sem limite de corrente, sem load dump protection, sem sensor de temperatura);
- **ACR oscilando** por causa de tensão instável (carga cíclica próxima do threshold);
- **queda excessiva de tensão em isoladores diodos** mal aplicados (alternador sem sensing correto);
- **cabos entre bancos sem proteção adequada** (ABYC E-11.4.7 exige fusível ≤ 178 mm do polo EM CADA ponta, pois cada banco pode ser a fonte em curto);
- **monitoramento ruim** porque o [[Monitor de Bateria - BMV - Shunt]] está no lugar errado (shunt em "Battery" com ACR fechado mede tanto banco quanto ambos, SoC fica errado);
- **DC-DC superaquecendo** por instalação em compartimento sem ventilação (derating por T° ambiente);
- **BMS de lítio abrindo de surpresa** (LVC, HVC, BTC/BTC — sem alarme prévio) — arquitetura deve ter fallback.

## Diagnóstico profissional

O diagnóstico deve responder:

1. **Os bancos estão realmente separados** quando deveriam? (medir tensão individual em repouso após 6h sem carga).
2. **A fonte está chegando com tensão e corrente compatíveis** ao banco de destino? (alternador gera 14,4 V mas banco house vê 13,2 V por queda em isolador antigo).
3. **O sistema está carregando como a química exige?** (Li-Fe precisa absorption 14,2-14,4 V por 2-4 h após SoC 90%; chumbo precisa float 13,5-13,8 V contínuo).
4. **Existe caminho de emergência funcional e documentado?** (testar "emergency parallel" com motor desligado).

**Medições úteis:**

- tensão de cada banco em repouso (após 6-24 h sem carga);
- tensão de cada banco durante carga (monitoramento contínuo com BMV por banco);
- corrente entre bancos (alicate amperímetro no cabo interbanco);
- resposta do sistema com motor ligado e desligado;
- atuação do BMS, quando houver (logs via app Victron/Renogy/REC/JK);
- temperatura de cabos e conexões sob carga (termografia se disponível);
- SoC real (% remanescente) × SoC reportado pelo monitor.

## Boas práticas de arquitetura

- manter **banco de partida e banco de serviço** com funções bem definidas;
- evitar **paralelos permanentes sem justificativa** de projeto;
- **proteger cabos interbancos** o mais próximo possível das fontes (fusível nas duas pontas);
- preferir **solução controlada por perfil** (DC-DC) quando houver lítio ou bancos muito diferentes;
- **documentar a topologia** com diagrama simples e legível (atualizado após retrofit);
- prever **modo de emergência** sem comprometer a operação normal;
- alinhar a solução de separação com a **estratégia do alternador** (sensed × não-sensed, regulador interno × externo);
- em sistemas com lítio, usar **BMS com saída de contactor** e integrar na arquitetura — ACR/DC-DC entende sinal do BMS;
- prever **monitor de bateria independente por banco** crítico (house + start + eventualmente thruster);
- **ventilação do compartimento** do DC-DC (dissipa 5-15% em calor);
- em embarcação com solar, MPPT com saída para house + DC-DC do house para start é arquitetura limpa.

## O que geralmente merece reedição no conteúdo de campo

Há quatro simplificações que precisam ser combatidas:

- "ACR serve para qualquer sistema" → **falso**, ACR só é adequado para chumbo-chumbo homogêneo.
- "Divisor por diodo e combinador automático fazem a mesma coisa" → **falso**, isolador diodo é passivo-topológico; ACR é ativo-temporal.
- "Se carrega, está certo" → **falso**, carregar com perfil errado encurta vida em 50-70%.
- "Lítio aceita qualquer arquitetura desde que tenha BMS" → **falso**, BMS protege a célula em emergência, não gerencia o carregamento; o carregador (AC ou DC-DC) é quem precisa seguir perfil Li-Fe.

Nenhuma dessas frases é tecnicamente robusta.

## Relação com outros sistemas

- **[[Alternador (DC)]]** — fonte principal de carga em navegação.
- **[[Bancos de Bateria]]** — arquitetura de bancos múltiplos.
- **[[BMS — Battery Management System]]** — proteção e gerenciamento de células Li-Fe.
- **[[Carregador de Bateria (AC To DC)]]** — fonte AC para carregamento em cais.
- **[[Chaves Gerais (DC)]]** — seccionamento e seletor manual.
- **[[Lítio LiFePO4 — Instalação e Cuidados Específicos]]** — química que exige cuidado especial.
- **[[Monitor de Bateria - BMV - Shunt]]** — posicionamento do shunt por banco.
- **[[Tipos de Bateria]]** — características de cada química.
- **[[Barramento DC / Bus Bar / Distribuição DC]]** — arquitetura de distribuição.

## Normas e referências

### Por família e jurisdição

| Família | Norma | Escopo |
| --- | --- | --- |
| **ABYC (EUA)** | E-11 | sistemas AC/DC |
| ABYC | E-10 | storage batteries — interligação |
| ABYC | E-13 | Li-Fe specifically |
| ABYC | A-31 | chargers and inverters |
| ABYC | E-30 | propulsão elétrica |
| **USCG (EUA)** | 33 CFR 183 Subpart I | sistemas elétricos em recreio |
| **UL (EUA)** | UL 1236 | battery chargers |
| UL | UL 458 | power converters marine |
| UL | UL 2743 | portable power packs |
| **NFPA (EUA)** | NFPA 70 art. 480, art. 706 | baterias, ESS |
| NFPA | NFPA 855 | ESS instalações estacionárias |
| **SAE (EUA)** | SAE J537 | baterias de partida |
| **ISO (internacional)** | ISO 10133:2012 | sistemas DC em pequenas embarcações |
| ISO | ISO 16315:2016 | propulsão elétrica |
| **IEC (internacional)** | IEC 62619 | Li-Fe industrial |
| IEC | IEC 62485-2 | baterias estacionárias |
| IEC | IEC 60364-7-712 | sistemas fotovoltaicos |
| IEC | IEC 60529 | IP |
| **ABNT (Brasil)** | NBR 5410 / 14039 | instalações BT/MT |
| ABNT | NBR 16690 | arranjos fotovoltaicos |
| **NORMAM (Brasil)** | NORMAM-05/-01 | recreio / marítimo |

### Comparação prática entre jurisdições

- **EUA (ABYC + UL)**: E-10 prescreve separação de start e house; E-13 dedica-se a Li-Fe com regras específicas de BMS, monitoramento e instalação.
- **Internacional (ISO/IEC)**: ISO 10133 trata sistemas DC de forma geral; IEC 62619 aplica-se a Li-Fe industrial, crescentemente adotada em marine comercial.
- **Brasil (ABNT + NORMAM)**: NBR 5410 não cobre náutica; NORMAM-05 remete a ABYC/ISO; falta norma brasileira específica de arquitetura de bancos — uso de referência ABYC/ISO é regra.

## Glossário rápido

1. **ACR (Automatic Charging Relay)** — relé que combina bancos automaticamente ao detectar tensão de carga.
2. **Absorption phase** — fase CV (tensão constante) após bulk no perfil de carga.
3. **Alternator load dump** — sobretensão do alternador quando a carga é removida abruptamente (BMS abre).
4. **Banco auxiliar** — banco adicional além de start e house (emergência, thruster).
5. **Banco house / service** — banco para cargas gerais da embarcação.
6. **Banco start / engine** — banco dedicado à partida do motor.
7. **Battery combiner** — sinônimo de ACR.
8. **Battery-to-battery sensed (B2B)** — regulação do alternador via sensor direto no banco de destino.
9. **BMS (Battery Management System)** — sistema de gerenciamento de banco Li-Fe.
10. **Bulk phase** — fase CC (corrente constante) do perfil de carga.
11. **CC-CV** — constant current / constant voltage.
12. **Combined mode (ACR)** — modo em que ACR está fechado, bancos em paralelo.
13. **Cross-over / emergency parallel** — paralelo manual temporário para partida.
14. **DC-DC charger** — conversor DC-DC com perfil de carga programável.
15. **Diode isolator** — isolador passivo por diodos retificadores.
16. **Drop-out voltage (ACR)** — tensão em que ACR abre (típico 12,8 V em 12 V nominal).
17. **Equalization** — carga de equalização em chumbo flooded (tensão alta, curta duração).
18. **Failover** — fallback manual para operação sob falha do automático.
19. **FET isolator** — isolador ativo por MOSFET.
20. **Float phase** — fase de manutenção contínua em tensão baixa (13,5-13,8 V em chumbo; Li-Fe não usa).
21. **Gasification (chumbo)** — liberação de H₂ acima de 14,4-14,8 V.
22. **HVC (High Voltage Cut-off)** — corte do BMS por sobretensão.
23. **Hybrid architecture** — chumbo + lítio + solar + gerador em arquitetura integrada.
24. **Interlock (emergência)** — botão ou chave para paralelo momentâneo.
25. **Isolation / galvanic separation** — separação elétrica entre circuitos.
26. **Li-Fe / LFP (LiFePO4)** — Lithium Iron Phosphate — química de lítio mais segura em marine.
27. **Load dump** — ver alternator load dump.
28. **LVC (Low Voltage Cut-off)** — corte do BMS por subtensão.
29. **Main battery switch** — chave geral do banco.
30. **Monitor de bateria (BMV)** — Battery Monitor com shunt.
31. **Multi-output charger** — charger AC com várias saídas independentes.
32. **MRBF (Marine Rated Battery Fuse)** — fusível montado no polo.
33. **Orion-Tr Smart (Victron)** — família de DC-DC com Bluetooth.
34. **Parallel cross-over** — chave de paralelo momentâneo.
35. **Peukert (fator de)** — redução de capacidade chumbo em alta corrente.
36. **Pre-charge resistor** — resistor que pré-carrega capacitor de inversor antes do BMS fechar.
37. **Prioridade de carga** — ordem de carregamento entre bancos múltiplos.
38. **Regulator (alternator)** — regulador de tensão do alternador (interno ou externo).
39. **Sensed alternator** — alternador com terminal de sensing no polo da bateria.
40. **Shore charger** — carregador AC em cais.
41. **Shunt** — resistor calibrado para medir corrente.
42. **SLI (Starting, Lighting, Ignition)** — bateria tradicional de partida.
43. **SoC (State of Charge)** — estado de carga em %.
44. **SoH (State of Health)** — estado de saúde (capacidade / nominal).
45. **Sterling PDR** — Pro Digital Regulator — regulador externo para alternador.
46. **Switch 1-2-BOTH-OFF** — chave seletora manual náutica.
47. **Temperature compensation (TC)** — compensação de tensão de carga por temperatura.
48. **Thermistor** — sensor de temperatura.
49. **Time-based combiner** — ACR com delay configurável antes de fechar/abrir.
50. **VSR (Voltage Sensitive Relay)** — sinônimo de ACR.

## FAQ

**Qual a diferença entre ACR, isolador por diodo/FET, chave seletora e carregador DC-DC?**

- **ACR/VSR**: relé automático que combina bancos ao detectar carga. Simples e barato, mas não gerencia perfil.
- **Isolador diodo/FET**: topologia passiva — uma fonte alimenta múltiplos bancos sem conectá-los. Diodo tem queda, FET não.
- **Chave seletora**: operação manual (BOTH = paralelo). Simples, mas depende do operador.
- **DC-DC**: conversor com perfil de carga programável. Melhor para químicas diferentes; mais caro.

**Como separar banco de partida e banco de serviço sem comprometer a carga?**

Arquitetura recomendada: alternador carrega start direto → ACR/DC-DC combina start e house quando tensão de carga sobe. Ou: alternador → isolador FET → start + house em paralelo. Ou (mais moderno): alternador → house → DC-DC → start (inversão típica em embarcação com Li-Fe no house).

**Em que situações ACR deixa de ser a melhor solução?**

- Qualquer arquitetura com lítio no house e chumbo no start (ou vice-versa);
- Bancos com capacidade muito diferente (start 100 Ah + house 600 Ah);
- Alternador sem proteção de load dump + Li-Fe (BMS pode abrir);
- Necessidade de perfil de carga específico por banco (sempre que o carregador precisa "saber" que banco está atrás);
- Sistemas com múltiplas fontes (solar + alternador + gerador).

**Posso misturar chumbo e lítio com ACR?**

**Não** como arquitetura limpa. O ACR iguala tensão entre bancos, mas chumbo e lítio têm curvas de tensão x SoC muito diferentes. Quando ACR fecha: lítio (13,3 V @ 50% SoC) puxa chumbo (12,2 V @ 50% SoC) para 12,6 V — chumbo nunca completa carga, lítio descarrega artificialmente. Use DC-DC.

**Qual a vantagem do DC-DC sobre um charger AC multi-output?**

DC-DC funciona em movimento (durante navegação) com o alternador como fonte. Charger AC multi-output só funciona em cais. Em embarcação que navega muito, DC-DC é o "segundo charger".

**Preciso de DC-DC se tenho MPPT solar e o banco é só Li-Fe?**

Se só existe um banco Li-Fe e o MPPT faz o perfil Li-Fe, não precisa de DC-DC. Se existe um segundo banco (start chumbo para backup de motor), sim — use DC-DC saindo do house Li-Fe para o start chumbo, com perfil chumbo correto.

## Integração com outras notas

- [[Alternador (DC)]]
- [[Bancos de Bateria]]
- [[BMS — Battery Management System]]
- [[Carregador de Bateria (AC To DC)]]
- [[Chaves Gerais (DC)]]
- [[Lítio LiFePO4 — Instalação e Cuidados Específicos]]
- [[Monitor de Bateria - BMV - Shunt]]
- [[Tipos de Bateria]]
- [[Barramento DC / Bus Bar / Distribuição DC]]

## Perguntas que esta nota responde

- Qual a diferença entre ACR, isolador por diodo/FET, chave seletora e carregador DC-DC?
- Como separar banco de partida e banco de serviço sem comprometer a carga?
- Em que situações ACR deixa de ser a melhor solução?
- Posso misturar chumbo e lítio com o mesmo divisor?
- Quando o carregador DC-DC é obrigatório e quando é exagero?
