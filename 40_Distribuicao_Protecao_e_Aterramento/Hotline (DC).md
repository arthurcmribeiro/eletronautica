---
title: "Hotline (DC)"
note_type: "technical-note"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "HOTLINE (DC) 77f19734f7fb83e99276817165e87b28.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "62"
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
normas_citadas:
  - "ABYC E-11 (AC and DC Electrical Systems on Boats) — §11.4.7 proteção ≤ 178 mm, §11.10.2 unswitched circuits"
  - "ABYC E-10 (Storage Batteries) — §10.7 limite de conexões no polo"
  - "ABYC A-16 (Electric Navigation Lights) — unswitched em algumas categorias"
  - "ABYC A-22 (Marine Fuel Gauges and Fuel Tank Level Sensors) — algumas aplicações unswitched"
  - "ABYC A-24 (Carbon Monoxide Detection Systems) — requisito unswitched"
  - "ABYC A-28 (Galley stoves)"
  - "ABYC H-22 (Bilge Pumps and Pumping Systems) — bomba automática unswitched"
  - "ISO 10133:2012 (Small craft — Electrical systems — Extra-low-voltage DC) — §6.8 seccionamento"
  - "ISO 15083:2020 (Small craft — Bilge pumping systems)"
  - "ISO 12133:2011 (Small craft — Smoke and heat alarm devices)"
  - "ISO 15371:2015 (Small craft — Fire extinguishing systems)"
  - "IEC 60364-4-42 (Protection against thermal effects)"
  - "IEC 60529 (IP Code)"
  - "UL 2034 (Single and Multiple Station Carbon Monoxide Alarms)"
  - "UL 217 (Smoke Alarms)"
  - "UL 1500 (Ignition Protection for Marine Products)"
  - "SAE J1171 (Marine Ignition Protection)"
  - "NFPA 70 (NEC) art. 230.82 (circuitos always-on permitidos)"
  - "NFPA 302 (Fire Protection Standard for Pleasure and Commercial Motor Craft)"
  - "NFPA 70 art. 555 (Marinas)"
  - "ABNT NBR 5410 (Instalações elétricas de baixa tensão)"
  - "NORMAM-05/DPC (Embarcações de esporte e recreio)"
  - "NORMAM-01/DPC (Embarcações em navegação marítima)"
  - "USCG 33 CFR 183.410 (Ignition protection)"
  - "USCG 33 CFR 183.460 (Conductors)"
  - "USCG 46 CFR 182 (Electrical Systems — Uninspected Passenger Vessels)"
  - "SOLAS Ch. II-2 Reg. 10 (Fire alarm system)"
family_clusters:
  - "ABYC-USCG (EUA)"
  - "ISO-IEC (internacional)"
  - "ABNT-NORMAM (Brasil)"
  - "NFPA-UL (EUA industrial)"
aliases:
  - "HOTLINE (DC)"
  - "Circuito sempre energizado"
  - "Unswitched DC"
  - "Always-on circuit"
  - "Essential loads"
seo_title: "Hotline DC em embarcações: circuitos sempre energizados, proteção e projeto"
seo_description: "Guia técnico sobre circuitos DC sempre energizados em embarcações: quando usar, como proteger, como documentar e quais erros tornam a hotline perigosa."
seo_keywords:
  - "hotline DC embarcação"
  - "circuito sempre energizado náutico"
  - "bomba de porão sempre ativa"
  - "proteção circuito essencial DC"
geo_queries:
  - "Quais circuitos devem ficar sempre energizados em uma embarcação?"
  - "Como projetar corretamente a hotline DC de um barco?"
  - "Bomba de porão pode ficar depois da chave geral?"
related_notes:
  - "Alarme de Alagamento - Sensor de Porão"
  - "Bomba de Porão"
  - "Chaves Gerais (DC)"
  - "Detector de CO — Monóxido de Carbono"
  - "Detector de Gás GLP - GN"
  - "Monitor de Bateria - BMV - Shunt"
  - "Sistema de Alarme Geral - Painel de Alarmes"
  - "VRM / Monitoramento Remoto"
---

# Hotline (DC)

> [!abstract] Resumo técnico
> Hotline DC é o conjunto de circuitos que permanecem alimentados mesmo com a chave geral de serviços desligada. Em projeto profissional, não é um "fio direto na bateria", mas uma **camada controlada de cargas essenciais**, protegidas, documentadas e intencionalmente mantidas ativas. ABYC E-11.10.2 permite explicitamente "unswitched circuits" para cargas críticas (bilge automática, CO detector, gás GLP/GN alarm, memória de inversor), sempre com proteção individual ≤ 178 mm do polo da bateria (ABYC E-11.4.7) e documentação explícita — deixar hotline sem proteção ou sem documentação é violação direta de norma, não "conveniência".

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **Hotline = intenção de projeto, nunca improviso** — cada circuito permanente deve ter justificativa documentada (segurança, monitoramento crítico, memória volátil).
> 2. **Proteção individual por circuito**, sempre — fusível/disjuntor ≤ 178 mm do polo (ABYC E-11.4.7); nunca compartilhe fusível único para bilge + CO + detector de gás + telemetria.
> 3. **Barramento dedicado separado** do barramento principal comutado — facilita manutenção e documentação; Blue Sea 5026 ST-Blade 6 ramais é solução limpa.
> 4. **Lista curta de candidatos**: bomba porão automática (ABYC H-22), CO detector (ABYC A-24), detector gás GLP/GN (ABYC A-26), memória de plotter/inversor, monitor de bateria (shunt ativo), tracker anti-furto, telemetria de geladeira.
> 5. **Bomba de porão — MANUAL e AUTOMÁTICO no mesmo barramento hotline**, nunca só o automático. Se o manual passar pela chave geral e o automático estiver direto na bateria, o acionamento do automático (com a chave desligada e o botão manual do painel acidentalmente em "ON") **retorna corrente pelo ramal manual** e reenergiza o barco inteiro via barramento comutado — é o tipo de backfeed silencioso que só aparece na próxima manutenção ou em sinistro (ver §"Falhas mais comuns" e §"Bomba de porão automática").
> 6. **Orçamento energético obrigatório** — some correntes de repouso × 720 h (mês parado); resultado > 5% da capacidade nominal do banco = descarga profunda iminente.
> 7. **Meio de desenergização total existe** — chave no polo da bateria (battery disconnect) ou fusível MRBF removível; a "chave geral" pode não cortar a hotline, mas o sistema precisa ter desligamento total para serviço.
> 8. **Cabos marine-grade** (cobre estanhado, classe 5) — hotline fica 100% do tempo energizada, qualquer falha na isolação continua ativa sem intervenção; usar BC5W2 / IEC 60092.
> 9. **Documentação visual + etiqueta no cabo** — marcar condutor com fita vermelha ou etiqueta "HOTLINE — ALWAYS LIVE" + indicação no diagrama unifilar.
> 10. **Revisão a cada refit** — cargas "de conveniência" migram para a hotline ao longo do tempo; remover 1-2 circuitos por refit é prática saudável.

> [!danger] Quando chamar um especialista
> Estes 9 cenários exigem engenheiro elétrico náutico ou integrador:
> 1. **Embarcação com banco Li-Fe e hotline permanente** — BMS pode abrir por LVC durante ausência prolongada; exige DC-DC dedicado à hotline a partir de banco auxiliar chumbo de emergência, ou BMS com "always-on output" separado (REC, Victron Lynx Smart).
> 2. **Corrente de repouso total > 500 mA em 12 V** — típico em barco com multiplas câmeras, tracker, inversor em standby, plotter em standby; exige orçamento energético formal e possivelmente carregamento solar de manutenção.
> 3. **Hotline com carga indutiva (bomba porão contínua)** — bomba queimando ciclicamente mesmo sem sinal do sensor = sensor em curto, relé colado ou válvula de retenção ausente; diagnóstico eletro-hidráulico combinado.
> 4. **Integração de sistema de detecção de incêndio conforme SOLAS II-2** (navio comercial) — hotline de alarme integrado com sistema de borrifamento, tripulação alertada em mar — regras de classe DNV/Lloyd's/BV.
> 5. **Retrofit de monitoramento remoto (VRM Victron, Garmin OnDeck, Siren Marine)** em embarcação oceânica — consumo de standby do gateway + roteador 4G/LTE pode drenar banco em 7-14 dias; exige painel solar de manutenção.
> 6. **Detector de gás GLP/GN em compartimento com múltiplos equipamentos a gás** (fogão + aquecedor + motor auxiliar) — zoneamento, sensor primário e secundário, válvula solenoide de corte automático (ABYC A-26); se falhar, vaza → explode.
> 7. **Embarcação de aluguel/charter com rotatividade de operadores** — cada operador esquece qual chave desliga a hotline; exige painel claro com LEDs indicando "hotline ativa", treinamento documentado.
> 8. **Investigação de descarga prematura de banco em barco ancorado** — diagnóstico com clamp amperímetro por trecho, termografia noturna, decomposição por circuito.
> 9. **Certificação USCG, CE/RCD ou ABYC Certified** — dossiê com lista de hotlines, memorial de proteção e corrente de repouso.

## O que é

Chama-se hotline, neste contexto, a **alimentação DC não comutada pela chave geral de serviços**. São circuitos pensados para continuar operando quando o restante do barco é desenergizado pelo usuário.

Isso existe para manter funções críticas mesmo com a embarcação parada, fechada ou desacompanhada — tipicamente segurança (bomba porão, detectores), monitoramento (BMV, VRM) e memória de equipamentos que exigem alimentação contínua.

## O que deve entrar na hotline

A decisão deve ser feita por **criticidade funcional**, não por conveniência. Tipicamente entram:

- **alimentação automática da [[Bomba de Porão]]** (ABYC H-22 recomenda e ISO 15083 exige);
- **[[Alarme de Alagamento - Sensor de Porão]]** (ABYC A-16);
- **detectores de segurança** que exijam alimentação contínua, como [[Detector de CO — Monóxido de Carbono]] (ABYC A-24) e [[Detector de Gás GLP - GN]] (ABYC A-26), quando essa for a estratégia do equipamento e do projeto;
- **[[Monitor de Bateria - BMV - Shunt]]** e sistemas de telemetria (shunt precisa "ver" todo o consumo, incluindo o próprio BMV);
- **[[VRM / Monitoramento Remoto]]** ou rastreamento (Siren Marine, Yacht Sentinel, Boat Command, Garmin OnDeck);
- **memória, relógio ou controle** de equipamentos que explicitamente precisem de alimentação permanente (plotter com waypoints, inversor com configuração, controlador de geladeira);
- **[[Sistema de Alarme Geral - Painel de Alarmes]]** (sirene, strobe, comunicação com central de segurança).

## O que normalmente não deve entrar

Em regra, não devem ficar permanentes:

- cargas de conforto (som, luz, geladeira comum sem telemetria);
- iluminação comum (exceto navegação em embarcação de uso comercial contínuo);
- eletrônica de uso casual (VHF, plotter em uso, radar);
- cargas de alto consumo sem justificativa clara (bomba d'água doce, ventilador);
- qualquer circuito deixado permanente apenas para "evitar passar pela chave".

Hotline mal definida vira **consumo parasita**, risco de manutenção e descontrole da arquitetura DC.

## Arquitetura correta

O arranjo maduro é:

- **barramento ou distribuição dedicada** para cargas permanentes (Blue Sea 5026 ST-Blade 6 ou 5027 ST-Blade 12);
- **proteção individual por circuito** (fusível por ramal, não um fusível único para todos);
- **identificação visível** (etiqueta física + diagrama);
- **documentação no diagrama** unifilar da embarcação;
- **possibilidade de isolamento total** para manutenção e emergência (chave MRBF removível ou battery disconnect no polo da bateria).

Em instalações simples, parte dessa função pode sair diretamente da bateria ou do barramento principal (fusível MRBF no polo + ramal curto). Em instalações melhores, existe um **pequeno subquadro ou barramento específico** para essenciais.

### Topologia em diagrama

```
Banco       MRBF       Battery Switch    Main Bus
[+]─────[F1]──────────────[CHAVE]────────[BUS]
  │
  └────[MRBF2]───────────────────────────[HOTLINE BUS]
                                         │
                                         ├─[F-HL1]─── Bomba porão auto
                                         ├─[F-HL2]─── CO detector
                                         ├─[F-HL3]─── Gás GLP detector
                                         ├─[F-HL4]─── BMV
                                         ├─[F-HL5]─── VRM gateway
                                         └─[F-HL6]─── Memória plotter
```

A **chave geral** desliga tudo que está no "Main Bus" mas não desliga a "Hotline Bus". O **MRBF2** é removível para desenergização total em manutenção.

## Proteção e seccionamento

O erro clássico é tratar hotline como exceção à proteção. Não é.

Circuitos permanentes continuam precisando de:

- **proteção contra sobrecorrente** no condutor não aterrado/positivo, conforme a arquitetura adotada (ABYC E-11.4.7 e ISO 10133 §6.8);
- **derivação protegida o mais próximo possível** da fonte de energia (≤ 178 mm do polo da bateria, ou ≤ 100 mm se passar por anteparo condutivo);
- **bitola coerente com corrente, regime e queda de tensão admissível**;
- **meio de corte total** para manutenção e emergência (chave MRBF, battery disconnect, ou fusível removível).

Uma chave geral "de uso normal" pode não cortar a hotline, mas o sistema precisa ter um modo de **desenergização total do banco** quando a intervenção exigir segurança completa.

## Exemplos corretos de aplicação

### Bomba de porão automática

É o caso didático mais importante. O automático deve continuar ativo com a chave geral desligada. O erro frequente é "proteger" apenas o ramal automático da bomba, deixando o manual pendurado no barramento comutado. **Essa separação cria backfeed.**

#### Regra de projeto: AMBOS os ramais (manual + automático) no MESMO barramento hotline

Em projeto correto, o painel com a chave 3 posições (AUTO / OFF / MANUAL-ON) é alimentado **a partir do mesmo barramento hotline** em que vive o ramal automático. A chave geral de serviços não passa por nenhum dos dois caminhos de alimentação da bomba — ela só passa pela iluminação do painel, pelo indicador de "pump running" e pelos demais circuitos comuns do barco.

> [!info] Convenção brasileira e internacional — chaveamento no positivo (bomba), no negativo (alarme)
> Em bombas de porão recreativas (Rule, Rule-A-Matic, Attwood, Johnson Pump, Jabsco, Seaflo, Shurflo) **o float switch e o sensor eletrônico chaveiam o POSITIVO**. Os bornes da bomba já saem de fábrica rotulados como **"+ auto / + manual / – common"** — o fabricante assume essa topologia. O negativo fica permanentemente conectado ao barramento negativo comum (passando pelo shunt do BMV). É isso que permite ter um só negativo saindo da bomba e dois positivos chegando (um do sensor, outro do painel manual).
>
> Em **alarmes de porão** (alta água, sirene, LED de painel) a convenção inverte: o sensor fecha o **negativo** para disparar o painel de alarmes, que mantém o positivo permanente. Isso reflete a lógica "common-positive" dos painéis de alarme industriais (Borel, MGM, Maretron, Offshore Systems), é mais robusta contra curto acidental ao casco e facilita sensores passivos de dois fios. Não confunda as duas lógicas: bomba = chaveia positivo; alarme = chaveia negativo.

**Arquitetura típica (correta)**:
- barramento hotline → [F-HL-bilge-auto] → float switch / sensor eletrônico (chaveia **positivo**) → terminal **"+ auto"** da bomba;
- barramento hotline → [F-HL-bilge-man] → chave 3 posições no painel → terminal **"+ manual"** da bomba (em paralelo elétrico com o ramo automático no próprio corpo da bomba; diodo de bloqueio entre painel e terminal "+ manual" protege contra backfeed);
- terminal **"– common"** da bomba → barramento negativo comum (passa pelo shunt do BMV).

**Corrente de repouso**: bomba parada ~5-15 mA (sensor de nível); bomba ativa 3-8 A (depende do modelo).

#### Modo de falha documentado: backfeed pelo ramal manual

> [!danger] Falha real observada em campo
> Barco em que **apenas o ramal automático da bomba estava na hotline** e o ramal manual passava pelo painel (alimentado pelo barramento comutado pela chave geral). O operador deixou a embarcação com:
> 1. **chave geral desligada** (barco "apagado" para ele);
> 2. **carregador de bordo desligado**;
> 3. **chave 3 posições do painel esquecida em MANUAL-ON**;
> 4. banco de baterias conectado (hotline ativa).
>
> Quando o nível subiu e **o sensor acionou a bomba pelo ramal automático** (float switch fechando o positivo do ramo "+ auto"), a tensão do barramento hotline chegou ao terminal **"+ auto"** da bomba. Como os terminais **"+ auto"** e **"+ manual"** são internamente o mesmo ponto elétrico no corpo da bomba e o contato manual da chave 3 posições estava fechado, **a tensão subiu pelo ramal manual** em direção ao painel, **entrou no barramento de distribuição comutado a partir da saída da chave 3 posições** e **reenergizou o barco inteiro com a chave geral desligada**. O negativo, que é comum e permanente, apenas fechou o circuito — a culpa do backfeed é 100% do caminho positivo que atravessa o painel comutado.
>
> Consequências possíveis:
> - **iluminação, plotter, rádio** acendem "do nada" com o barco fechado, gerando drain em pleno ciclo de descarga do banco;
> - **equipamentos sensíveis** recebem tensão sem a sequência normal de energização (microcontroladores travam, módulos NMEA 2000 ficam em modo inconsistente);
> - **risco de incêndio em ponto comutado defeituoso** que só seria energizado "com a chave ligada" — agora está energizado com ninguém a bordo;
> - **técnico que abrir o painel no dia seguinte** encontra circuitos vivos onde o diagrama diz "OFF": choque, curto com ferramenta, diagnóstico errado.

#### Como prevenir o backfeed

1. **Ambos os ramais da bomba (manual e automático) no mesmo barramento hotline** — regra 1, não negociável.
2. **Diodo de bloqueio (ou relé de isolação)** no ramal manual, entre a saída da chave 3 posições e o terminal da bomba — bloqueia corrente reversa caso o operador esqueça a chave em "ON". Diodo tipo Schottky ≥ 15 A ou relé automotivo 30 A em aplicações até 8 A.
3. **Lâmpada-piloto "MANUAL" no painel** — LED vermelho ativo enquanto a chave está em MANUAL-ON, para o operador notar ao fechar o barco.
4. **Auto-desarme temporizado** — algumas chaves 3 posições industriais têm retorno automático para AUTO após X minutos (timer 555 ou módulo dedicado).
5. **Teste na entrega e em cada refit** — com chave geral desligada e carregador off, forçar acionamento do automático (jogar água no porão ou levantar o flutuador manualmente) e **medir tensão no barramento comutado**: deve permanecer 0 V. Se subir para ~12/24 V, existe caminho de backfeed e a instalação precisa ser revista.

### Monitoramento e telemetria

Sistemas como [[VRM / Monitoramento Remoto]] só fazem sentido se permanecerem energizados. Isso exige orçamento energético de standby e proteção específica.

**Corrente típica de standby**:
- Victron Cerbo GX + GlobalLink 520 (4G): ~80-150 mA;
- Siren Marine MTC: ~50-100 mA;
- Garmin OnDeck: ~40-80 mA;
- Maretron N2KView standalone: ~30-60 mA.

### Alarmes e detecção

Alarmes de água, gás ou CO não devem depender de o operador "lembrar de deixar a chave ligada", desde que o projeto, o equipamento e a rotina operacional justifiquem a permanência.

**Corrente típica**:
- CO detector (MTI 68-5081-RLY): ~30-50 mA;
- Detector gás GLP Fireboy CMD-4 zona única: ~40-80 mA;
- Detector gás GLP Xintex MS-4 duas zonas: ~60-120 mA.

## Critérios de projeto

### 1. Corrente de repouso

Toda carga permanente deve entrar no balanço energético do barco. Pequenos consumos contínuos, somados por dias ou semanas, descarregam o banco.

**Exemplo de cálculo**:
- bomba porão auto (sensor): 10 mA
- CO detector: 40 mA
- Gás GLP detector: 60 mA
- BMV-712: 10 mA
- Cerbo GX + GlobalLink: 120 mA
- Memória plotter: 15 mA
- **Total**: ~255 mA

Em banco de 400 Ah (AGM): 255 mA × 24 h × 30 dias = 184 Ah = **46% de SoC drop em 30 dias** → banco descarregado profundamente sem carregamento.

### 2. Criticidade real

Se o circuito não gera ganho concreto de segurança, proteção do ativo ou monitoramento relevante, provavelmente não deveria estar na hotline.

Teste: "**Se eu desligar este circuito por 48 h com o barco parado, o que acontece?**" — se nada de grave, não pertence à hotline.

### 3. Manutenção segura

O técnico precisa saber, de forma inequívoca, quais pontos permanecem vivos com a chave desligada. Sem isso, a hotline vira armadilha (risco de choque, curto por ferramenta, erro de diagnóstico).

**Prática**:
- etiqueta vermelha "HOTLINE — ALWAYS LIVE" no cabo;
- marcação no diagrama unifilar com cor distinta;
- briefing no painel principal: "HOTLINE ATIVA — VERIFIQUE MRBF2 ANTES DE SERVIR".

### 4. Queda de tensão

Cargas como bomba automática, eletrônica de segurança e telemetria costumam ser sensíveis a subtensão (alguns detectores de CO desarmam abaixo de 10,8 V em 12 V). A linha permanente precisa ser curta, bem protegida e dimensionada para o pior caso plausível.

**Meta**: ΔV ≤ 3% da tensão nominal sob corrente nominal (ABYC E-11.5).

## Falhas mais comuns em campo

As mais recorrentes são:

- **bomba automática ligada depois da chave geral**, anulando sua função (barco afunda com chave desligada);
- **só o ramal automático da bomba na hotline** — ramal manual no barramento comutado gera **backfeed** quando sensor aciona a bomba com chave 3 posições esquecida em MANUAL: corrente sobe pela bomba, volta pelo contato manual e reenergiza o painel inteiro com a chave geral desligada (caso real documentado — ver §"Bomba de porão automática");
- **vários circuitos permanentes pendurados no mesmo fusível** sem seletividade (uma falha desliga todos os sensores de segurança);
- **hotline não documentada**, confundindo manutenção (técnico trabalha em cabo "morto" que está energizado);
- **consumos fantasma** drenando o banco em períodos de inatividade (inversor em standby 2-5 A puxa sozinho);
- **sensores e monitores ligados em derivação improvisada**, sem proteção adequada (cabo 18 AWG direto no polo com conector faston);
- **ausência de meio de desligamento total** para serviço (técnico precisa desconectar cabo da bateria — risco de faísca);
- **corrosão em terminal de hotline** passa despercebida (ninguém olha porque não há sinal de falha — até a bomba não partir em emergência);
- **chave 3 posições sem LED-piloto** — operador esquece em MANUAL-ON ao fechar o barco e só descobre dias depois, com o banco exaurido ou o painel energizado sem intenção.

## Diagnóstico profissional

O diagnóstico deve responder:

1. **Quais circuitos ficam energizados com a chave desligada?** (mapeamento físico + comparação com diagrama).
2. **Isso foi intencional ou improvisado?** (revisão de histórico de retrofit).
3. **Cada derivação está protegida?** (fusível individual, próximo ao polo, calibre coerente com cabo).
4. **O consumo total de repouso está dentro do previsto?** (clamp amperímetro no cabo da bateria com tudo "desligado").

**Ensaios úteis**:

- **medição de corrente de repouso total** do banco (alicate amperímetro DC no cabo principal);
- **conferência de tensão** nas saídas permanentes com chave desligada;
- **verificação funcional** da bomba automática e alarmes (teste de água no porão + teste de botão dos detectores);
- **inspeção do diagrama versus instalação real** (muitas hotlines "aparecem" em retrofits passados sem documentação);
- **teste de desligamento total** para manutenção (retirar MRBF2 e confirmar V = 0 em todo hotline bus).

## Boas práticas

- manter **barramento dedicado** para cargas permanentes quando a instalação justificar;
- **proteger cada circuito individualmente** (um fusível por ramal, não um fusível para todos);
- **rotular fisicamente os condutores** e pontos sempre energizados (cor vermelha + etiqueta);
- **medir e registrar consumo de repouso** após qualquer alteração (documento de manutenção);
- **revisar periodicamente o que está na hotline** e remover cargas "de conveniência" (anual ou em refit);
- **prever corte total do banco** para emergência e serviço (MRBF removível + chave no polo);
- em sistema Li-Fe, considerar **banco auxiliar chumbo** dedicado à hotline (50-100 Ah AGM) com DC-DC vindo do banco principal — mantém hotline ativa se BMS desligar o banco principal;
- em embarcação oceânica/offshore, adicionar **painel solar de manutenção** (10-50 W) para compensar drop de hotline durante ausência prolongada;
- treinar **operador em briefing**: "chave geral NÃO desliga hotline; para desligamento total, retire MRBF2".

## Erros que fragilizam a base técnica

Estas frases precisam ser evitadas:

- "hotline é só um fio direto na bateria";
- "se é importante, deixa direto";
- "chave desligada significa barco desenergizado";
- "se o fusível está no painel, já protege";
- "é só um pouquinho de corrente, não faz diferença no banco";
- "o sensor já tem fusível interno, não precisa outro fora";
- "na bomba de porão basta deixar o automático direto, o manual pode ficar no painel" — **errado**: sem diodo de bloqueio ou sem manual também na hotline, cria caminho de backfeed que reenergiza o barco pela chave 3 posições esquecida em MANUAL.

Todas elas simplificam demais e induzem instalação ruim.

## Relação com outros sistemas

- **[[Alarme de Alagamento - Sensor de Porão]]** — sensor primário hotline.
- **[[Bomba de Porão]]** — circuito automático obrigatório em hotline.
- **[[Chaves Gerais (DC)]]** — o que NÃO corta a hotline.
- **[[Detector de CO — Monóxido de Carbono]]** — hotline em cabine fechada.
- **[[Detector de Gás GLP - GN]]** — hotline quando há fogão a gás.
- **[[Monitor de Bateria - BMV - Shunt]]** — hotline com shunt integrador.
- **[[Sistema de Alarme Geral - Painel de Alarmes]]** — hotline de segurança.
- **[[VRM / Monitoramento Remoto]]** — hotline de telemetria.
- **[[Barramento DC / Bus Bar / Distribuição DC]]** — barramento hotline dedicado.

## Normas e referências

### Por família e jurisdição

| Família | Norma | Escopo |
| --- | --- | --- |
| **ABYC (EUA)** | E-11 §4.7, §10.2 | proteção e circuitos unswitched |
| ABYC | E-10 §7 | limite polo da bateria |
| ABYC | A-16 | luzes de navegação unswitched |
| ABYC | A-24 | CO detectors |
| ABYC | A-26 | gás GLP/GN detectors |
| ABYC | H-22 | bilge pumps |
| **USCG (EUA)** | 33 CFR 183.410 | ignition protection |
| USCG | 33 CFR 183.460 | conductors |
| USCG | 46 CFR 182 | Uninspected Passenger Vessels |
| **UL (EUA)** | UL 2034 | CO alarms |
| UL | UL 217 | smoke alarms |
| UL | UL 1500 | marine ignition protection |
| **SAE (EUA)** | SAE J1171 | marine ignition protection |
| **NFPA (EUA)** | NFPA 70 art. 230.82, art. 555 | always-on, marinas |
| NFPA | NFPA 302 | fire protection recreio/comercial |
| **ISO (internacional)** | ISO 10133:2012 | DC pequenas embarcações |
| ISO | ISO 15083:2020 | bilge pumping |
| ISO | ISO 12133:2011 | smoke and heat alarms |
| ISO | ISO 15371:2015 | fire extinguishing |
| **IEC (internacional)** | IEC 60364-4-42 | proteção térmica |
| IEC | IEC 60529 | IP |
| **SOLAS** | Ch. II-2 Reg. 10 | fire alarm system (comercial) |
| **ABNT (Brasil)** | NBR 5410 | instalações BT |
| **NORMAM (Brasil)** | NORMAM-05/-01 | recreio / marítimo |

### Comparação prática entre jurisdições

- **EUA (ABYC + NFPA)**: prescreve exatamente quais circuitos devem/podem ser unswitched (bilge, CO, gás, luzes de navegação em comercial); proteção individual obrigatória.
- **Internacional (ISO/IEC)**: abordagem por função (ISO 15083 exige bilge automática); ISO 10133 trata seccionamento geral.
- **Brasil (ABNT + NORMAM)**: NBR 5410 não cobre náutica; NORMAM-05 remete a ABYC/ISO.
- **Navio classificado/SOLAS**: sistema de alarme integrado por regra de classe.

## Glossário rápido

1. **Alarm panel** — painel de alarmes com indicadores e teste.
2. **Always-on circuit** — sinônimo em inglês de hotline.
3. **Auto-on / auto-off (bilge)** — bomba controlada por sensor de nível.
4. **Battery disconnect** — chave principal da bateria (diferente da chave de serviços).
5. **BMV (Battery Monitor)** — monitor de bateria com shunt.
6. **CO detector** — detector de monóxido de carbono.
7. **Consumo parasita** — carga indesejada que drena o banco em repouso.
8. **Cross-over** — ponto de transição entre circuitos comutados e unswitched.
9. **Current draw (standby)** — corrente consumida em modo espera.
10. **Dead-front** — painel com partes energizadas atrás de superfície isolante.
11. **Disconnect means** — meio de desligamento para manutenção.
12. **Essential loads** — cargas essenciais (sinônimo de hotline loads).
13. **Float switch (bilge)** — chave de boia para sensor de nível.
14. **Gas detector (GLP/GN)** — detector de propano/butano/gás natural.
15. **Ground (negative bus)** — barramento negativo comum.
16. **Hotline bus** — barramento dedicado a cargas permanentes.
17. **Ignition protection** — proteção contra ignição de gás (ABYC/USCG).
18. **Key-off** — modo chave desligada.
19. **Lockout/tagout (LOTO)** — procedimento de bloqueio para manutenção.
20. **Manual bypass** — acionamento manual em paralelo ao automático.
21. **Memory circuit** — circuito de memória de equipamento (plotter, inversor).
22. **MRBF (Marine Rated Battery Fuse)** — fusível de polo da bateria.
23. **Offline (boat)** — embarcação desenergizada para manutenção.
24. **Parasitic load** — ver consumo parasita.
25. **Permanent live** — condutor sempre energizado.
26. **Phantom load** — carga fantasma (consome em "off").
27. **Quiescent current** — corrente em repouso.
28. **Redundância dupla** — dois detectores/sensores em paralelo para segurança.
29. **Repouso (corrente de)** — Iq, corrente sem atividade.
30. **Seletividade (fusíveis)** — coordenação para que só a proteção mais próxima atue.
31. **Sensor eletrônico de nível** — alternativa a float switch (sem partes móveis).
32. **Shunt (monitor)** — resistor calibrado para medir corrente total.
33. **Sleep mode** — modo de baixo consumo do equipamento.
34. **Solar maintenance** — painel solar pequeno para compensar hotline.
35. **Standby current** — corrente em espera (tipicamente 10-200 mA por carga).
36. **Strobe alarm** — alarme estroboscópico.
37. **Sub-panel** — subquadro dedicado a hotline.
38. **Switched circuit** — circuito que passa pela chave geral.
39. **Telemetry gateway** — gateway de telemetria (Victron Cerbo, Siren MTC).
40. **Timer circuit** — temporizador em circuito (anti-short-cycle bilge).
41. **Tracker (anti-theft)** — rastreador anti-furto.
42. **Trip rate (BMS)** — corrente/tensão que dispara BMS.
43. **Unswitched bus** — barramento não comutado (ver hotline bus).
44. **VDC (Voltage DC)** — tensão em corrente contínua.
45. **VRM (Victron Remote Management)** — serviço em nuvem da Victron.
46. **Watchdog** — circuito de vigilância (alarme se sinal some).
47. **Week-long standby test** — teste de 7 dias com barco fechado.
48. **Wiring label** — etiqueta impressa em cabo (heat-shrink printed).
49. **Zone 1/2/3** — zoneamento de detecção de gás por compartimento.
50. **Zero-current test** — teste de corrente zero após isolamento.

## FAQ

**Quais circuitos fazem sentido na hotline de uma embarcação?**

Funções de segurança (bilge automática, CO detector, gás GLP/GN detector), monitoramento crítico (BMV, VRM), memória de equipamentos (plotter, inversor), e alguns casos de comunicação (tracker anti-furto, EPIRB em standby).

**Como manter cargas essenciais ativas sem transformar o barco em um emaranhado de fios diretos?**

Use barramento dedicado (Blue Sea 5026 ou similar) com proteção individual por ramal, partindo de MRBF próprio no polo da bateria. Documente tudo no diagrama unifilar. Revise anualmente e remova cargas "de conveniência".

**Como proteger, documentar e manter circuitos permanentes com segurança?**

Proteção: fusível individual ≤ 178 mm do polo, calibre coerente com o cabo. Documentação: diagrama unifilar, etiqueta física no cabo, briefing no painel. Manutenção: MRBF removível, teste anual de corrente de repouso, revisão periódica.

**Bomba de porão pode ficar depois da chave geral?**

Não, e aqui vai a complicação que muita gente perde: **nem o automático nem o manual** devem depender da chave geral. ABYC H-22 e ISO 15083 exigem que a bilge automática permaneça operacional mesmo com a chave desligada, e o detalhe crítico é que **o ramal manual precisa sair do MESMO barramento hotline do automático**. Se só o automático estiver na hotline e o manual passar pela chave geral, um acionamento do automático com a chave 3 posições do painel esquecida em MANUAL gera backfeed: a corrente que entra no motor pelo ramal automático sai pelo ramal manual, sobe ao painel e reenergiza o barco inteiro com a chave "desligada". A solução é ou (i) os dois ramais saindo do mesmo barramento hotline, ou (ii) diodo de bloqueio no ramal manual.

**Como eliminar o backfeed da bomba de porão via chave manual?**

Três camadas combinadas: (1) arquitetura — ambos os ramais (automático e manual) saindo do mesmo barramento hotline, de modo que não haja caminho pelo barramento comutado; (2) diodo Schottky de bloqueio (≥ 15 A) entre a saída da chave 3 posições e o terminal da bomba, para impedir corrente reversa; (3) LED-piloto vermelho ativo sempre que a chave 3 posições estiver em MANUAL-ON, visível do painel principal, para que o operador não feche o barco com a chave esquecida. Um teste pós-instalação consolida o resultado: chave geral OFF + carregador OFF + acionar o automático manualmente (erguer o flutuador) + medir tensão nas barras do painel comutado — precisa permanecer 0 V.

**Qual o limite aceitável de corrente de repouso em um barco?**

Depende do banco e do tempo de inatividade. Regra prática: hotline < 5% da capacidade Ah do banco em 30 dias. Banco 400 Ah: limite ~0,6 A médio (~432 Ah em 30 dias ⇒ ajustar). Em embarcação que fica meses parada, adicione carregamento solar de manutenção.

**Hotline em barco com banco Li-Fe é segura?**

Com cuidado especial. BMS pode desligar o banco Li-Fe por LVC durante ausência prolongada, desligando junto a hotline. Solução: banco auxiliar AGM/gel pequeno (50-100 Ah) dedicado à hotline, mantido carregado pelo solar ou por DC-DC a partir do banco principal.

**Posso colocar câmera de vigilância na hotline?**

Tecnicamente sim, mas o consumo (50-200 mA por câmera) é significativo. Em barco que fica parado semanas, câmeras devem ter painel solar próprio ou ser desligadas ao deixar o barco. Use "scheduled wake-up" (câmera liga em horários programados) para reduzir consumo.

## Integração com outras notas

- [[Alarme de Alagamento - Sensor de Porão]]
- [[Bomba de Porão]]
- [[Chaves Gerais (DC)]]
- [[Detector de CO — Monóxido de Carbono]]
- [[Detector de Gás GLP - GN]]
- [[Monitor de Bateria - BMV - Shunt]]
- [[Sistema de Alarme Geral - Painel de Alarmes]]
- [[VRM / Monitoramento Remoto]]
- [[Barramento DC / Bus Bar / Distribuição DC]]
- [[Divisores de Carga (DC)]]

## Perguntas que esta nota responde

- Quais circuitos fazem sentido na hotline de uma embarcação?
- Como manter cargas essenciais ativas sem transformar o barco em um emaranhado de fios diretos?
- Como proteger, documentar e manter circuitos permanentes com segurança?
- Bomba de porão pode ficar depois da chave geral?
- Qual o limite aceitável de corrente de repouso em um barco?
