---
title: "Catraca"
note_type: "technical-note"
domain: "70_Hidraulica_Climatizacao_e_Utilidades"
source_file: "CATRACA 93e19734f7fb835188a50199d626ca56.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "55"
tier_fase_6: "A"
reviewed_on: "2026-04-21"
review_jurisdiction:
  - "Brasil"
  - "internacional"
review_level: "engineering-curated"
normas_citadas:
  - "ABYC E-11 — AC and DC Electrical Systems on Boats"
  - "ABYC H-40 — Anchoring, Mooring and Strong Points"
  - "ABYC TE-4 — Lightning Protection"
  - "ISO 10133 — Small craft — Electrical systems — Extra-low-voltage DC"
  - "ISO 13297 — Small craft — Electrical systems — AC installations"
  - "ISO 12401 — Small craft — Deck safety harness and safety line"
  - "ISO 12217 — Small craft — Stability and buoyancy assessment (relevante a carga em convés)"
  - "ISO 4309 — Cranes — Wire ropes — Inspection and discard"
  - "ISO 2408 — Steel wire ropes for general purposes"
  - "ISO 6743-4 — Lubricants — Family H (Hydraulic systems)"
  - "ISO 11158 — Lubricants — Family H specifications"
  - "ISO 3448 — Viscosity classification"
  - "ISO 4406 — Fluid contamination code"
  - "SAE J306 — Gear Lubricant Viscosity Classification"
  - "SAE J1614 — Wire Rope Marine Grade"
  - "API GL-4 / GL-5 — Gear Oil Service Classification"
  - "DIN 51524-2 — HLP hydraulic oils"
  - "DIN 51524-3 — HVLP hydraulic oils"
  - "DIN 51517-3 — CLP industrial gear oils"
  - "DIN 766 — Short link chain for lifting purposes"
  - "EN 14492-1 — Cranes — Power driven winches"
  - "EN 60204-32 — Electrical equipment — Hoisting machines"
  - "CE 2006/42/EC — Machinery Directive"
  - "EN ISO 12100 — Safety of machinery"
  - "EN ISO 13849-1 — Safety-related parts of control systems"
  - "IEC 60529 — IP Code"
  - "IEC 60364 — Low-voltage electrical installations"
  - "IMS / WS — World Sailing Racing Rules (referência a catraca de vela em regata)"
  - "NR-12 — Segurança em Máquinas e Equipamentos (Brasil)"
  - "NR-11 — Transporte, Movimentação, Armazenagem e Manuseio de Materiais"
  - "NBR 5410 — Instalações elétricas de baixa tensão"
  - "NBR 14134 — Acionamento hidráulico industrial (referência)"
  - "NBR 8400 — Cálculo de equipamento de içamento"
  - "NORMAM-05/DPC — Marinha do Brasil"
related_notes:
  - "Óleos Hidráulicos Marine — Guia Completo"
  - "Guincho"
  - "Bancos de Bateria"
  - "Dimensionamento de Cabos DC — Cálculo Prático"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Thruster"
  - "Davit - Munk - Guindaste de Bote - Tender Lift"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
source_urls:
  - "https://www.harken.com/en/support/tech-articles/choosing-winches/"
  - "https://www.harken.com/en/shop/radial/60-electric-self-tailing-radial-aluminum-winch-3-speed/"
  - "https://www.lewmar.com/evo-electric-winch-kit"
  - "https://www.quickitaly.com/en/products/windlasses-and-capstans/capstans/"
  - "https://webstore.ansi.org/standards/abyc/abyc112025"
aliases:
  - "CATRACA"
  - "Capstan"
  - "Winch elétrico"
  - "Self-tailing winch"
  - "Catraca de vela"
  - "Catraca de convés"
seo_title: "Catraca elétrica em embarcações: capstan, self-tailing, óleo, cabos e falhas"
seo_description: "Guia técnico sobre catraca elétrica, capstan e self-tailing winch: tração de cabos, diferença para guincho de âncora, demanda de corrente, contatores, óleo do redutor, ergonomia e falhas em convés."
seo_keywords:
  - "catraca elétrica barco"
  - "capstan marine"
  - "self-tailing winch"
  - "winch elétrico embarcação"
  - "óleo catraca"
  - "Harken winch"
  - "Lewmar winch"
  - "Andersen winch"
  - "Antal winch"
geo_queries:
  - "Qual a diferença entre catraca elétrica e guincho de âncora?"
  - "Por que a catraca fica fraca ou para sob carga no barco?"
  - "Como dimensionar cabo e bateria para catraca elétrica?"
  - "Que óleo usar em catraca elétrica self-tailing?"
  - "Catraca de vela queima com que frequência?"
---

# Catraca

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **Catraca ≠ guincho de âncora** (windlass). Catraca tracia cabo/linha em convés; windlass trabalha com corrente e âncora. Normas, proteção, óleo e procedimento são diferentes.
> 2. **Em veleiro, catraca self-tailing elétrica** (Harken, Lewmar, Andersen, Antal) substitui manivela para izamento de vela, cunningham, escota. Em lancha/iate a motor, **capstan** (catraca vertical sem tambor cativo) é usado para tração de espia em manobra.
> 3. **Potência e torque** — catracas de vela elétricas costumam ser **200–500 W DC** (pico 20–40 A @ 12 V); capstans pesados em iate 30 m+ podem ser 1–3 kW hidráulicos.
> 4. **Relação de redução** muda tudo: catracas self-tailing trabalham em 2, 3 ou 4 velocidades. Elétricas geralmente usam a velocidade mais lenta (mais torque), limitando carga efetiva a algo entre 600 kg e 3.500 kg dependendo do modelo.
> 5. **Duty cycle curto**: S2 de 30–90 s por ciclo em catracas de vela DC. Exceder derrete o motor. Em capstan hidráulico, S3 pode ser 25–40%.
> 6. **Queda de tensão na corrida** — cabo de 6–12 m do banco à catraca da vela é comum em veleiro. Dimensionar para manter ≥ 11,5 V no motor em pico.
> 7. **Óleo do redutor** — catracas self-tailing mecânicas usam **graxa específica** (Harken Winch Grease, Lewmar Grease). Elétricas com redutor banhado em óleo usam **SAE 75W-90 GL-4** ou óleo de engrenagem leve (nunca GL-5 em redutores de bronze).
> 8. **Cabo / linha** — nunca tracionar cabo de aço em catraca projetada para cabo têxtil. Dyneema em catraca aceita, com cautela (escorrega menos, mais calor no tambor).
> 9. **Chicote (cable whip) e aprisionamento de dedos** são os riscos de segurança principais. Comando com dead-man obrigatório. Nunca enrolar cabo na mão ao operar.

> [!danger] Quando chamar um especialista — 9 cenários
> 1. **Catraca liga sozinha** (sem comando) — botão travado, relé/contator soldado. Risco de aprisionamento/chicote. **Desligar a chave geral imediatamente**; substituir botão e contator.
> 2. **Motor aquece em < 30 s de uso** ou cheira queimado — subdimensionamento severo ou enrolamento danificado. Parar, diagnosticar antes de religar.
> 3. **Catraca trava carregada** — pode ser bronzina do redutor agarrada, embreagem self-tailing queimada, ou cabo preso. Não forçar. Aliviar carga antes de inspecionar.
> 4. **Cabo escorrega no tambor em pleno uso** — superfície lisa (polida pelo uso), dentado da mordente gasto, ou linha inadequada. Risco de controle perdido da vela. Inspecionar tambor e substituir dentado ou tambor.
> 5. **Óleo saindo pela vedação do redutor** — selo rompido, água entrou por fora. Trocar selo + óleo antes da próxima temporada; se operar com selo comprometido, destrói rolamento.
> 6. **Capstan hidráulico com ruído alto, cavitação, ou aquecimento do óleo** — filtro saturado, ar no circuito, válvula proporcional com deriva. Parar e analisar óleo + filtros.
> 7. **Queda de tensão > 15% no pico** — cabo subdimensionado, bateria descarregada, conexões oxidadas. Pode gerar aquecimento localizado em terminal e incêndio. Refazer cabeamento.
> 8. **Self-tailing não prende a linha** (escorrega no tailer) — desgaste das mandíbulas ou linha errada. Substituir conjunto tailer. Em regata, risco de perda de controle da vela sob vento forte.
> 9. **Perícia em ferimento por catraca** (dedo esmagado, laceração por chicote) — laudo técnico obrigatório sobre ergonomia, estado do comando, disponibilidade de dead-man, treinamento e conformidade com NR-12.

## O que é

Nesta base, **Catraca** refere-se ao equipamento motorizado usado para **tracionar cabo, corda ou linha de convés** — não ao `windlass` de âncora. O termo é usado em várias formas:

### Tipos de catraca

- **Self-tailing winch (vela)** — catraca com mordente automático; padrão em veleiros para izar vela, escotar, cunningham. Marcas: Harken, Lewmar, Andersen, Antal, Barient (legacy), Pontos.
- **Capstan (cabeço de halar)** — catraca vertical simples sem mordente; usado para tração de espia em manobra de atracação. Marcas: Muir, Maxwell, Quick, Lofrans.
- **Catraca de içamento leve** — usada em convés industrial ou comercial para levantar equipamento; raramente em iate de lazer.
- **Catraca horizontal drum (tambor horizontal)** — guincho horizontal com tambor cativo; caso intermediário entre catraca vertical e windlass.

### Funções típicas

- Içar vela grande sem esforço braçal (self-tailing elétrica).
- Tracionar espia para atracação ou desatracação.
- Auxiliar içamento leve de convés (spinnaker pole, gennaker halyard).
- Apoio a operações de convés em embarcações específicas (regata, charter, escola de vela).

## Diferença crítica para o guincho de âncora (windlass)

Essa distinção precisa ser **muito clara** — é a fonte mais comum de confusão:

| Aspecto | Catraca (capstan / self-tailing) | Guincho de âncora ([[Guincho]] / windlass) |
|---|---|---|
| Carga típica | 300–3.500 kg | 1.500–15.000 kg |
| Cabo/linha | Têxtil (poliéster, HMPE/Dyneema) | Corrente de ferro (DIN 766 / BBB) + cabo |
| Velocidade | Mais alta (~10–30 m/min) | Baixa (~10–15 m/min) |
| Duty cycle | S2 curto (30–90 s) | S3 ~25% |
| Gypsy (polegar de corrente) | Não tem (tambor liso) | **Sim** — dimensionado para DIN 766 / ISO 4565 / BBB |
| Proteção padrão | Fusível DC genérico | Class T ou MRBF dedicado |
| Norma primária | EN 14492-1 (hoist) / ISO 4309 (cabos) | ABYC H-40 |
| Operação | Auxiliar de manobra | Fundeio, operação crítica |

Misturar os dois assuntos confunde seleção, proteção e manutenção. O erro mais comum é **usar capstan para fundeio**; quase sempre acaba em falha mecânica ou elétrica.

## Famílias e fabricantes

### Self-tailing winches (vela)

- **Harken (EUA)** — referência mundial; linhas Performa, Radial, Classic; versões elétricas e hidráulicas. Modelos mais comuns: 40.2 ST até 1130.
- **Lewmar (Reino Unido)** — linhas Evo, Ocean, Racing, Pro-Series. Presente em cruisers.
- **Andersen (Dinamarca)** — all-stainless; linhas Compact, Full Stainless, Electric.
- **Antal (Itália)** — performance e regata; linha R, W.
- **Pontos (França)** — catracas multispeed 4-speed.
- **Barient (legacy / EUA)** — marca clássica descontinuada; ainda comum em veleiros antigos.

### Capstans (lancha e iate a motor)

- **Muir (Austrália)** — Cougar, Mariner, Stockton.
- **Maxwell (Nova Zelândia)** — VC500, VWC3500.
- **Lewmar** — linha Horizon e Pro-Series Capstan.
- **Quick (Itália)** — BCM, BCB.
- **Lofrans (Itália)** — Cabestan, Progress.

### Capstans hidráulicos (iate 30 m+)

- **Muir** — Pacific/Atlantic hidráulicos.
- **Maxwell** — Freedom hidráulico.
- **Data Hidráulica** — soluções custom.

### Porte típico e tecnologia

| Aplicação | Carga linha | Potência | Tecnologia |
|---|---|---|---|
| Veleiro 9–12 m | 500–1.500 kg | 200–400 W DC 12 V | Self-tailing manual ou elétrica leve |
| Veleiro 12–18 m | 1.500–3.000 kg | 400–800 W DC 12/24 V | Self-tailing elétrica |
| Veleiro 18–30 m (mini super-yacht) | 3.000–5.000 kg | 1–2 kW DC 24 V ou hidráulico | Self-tailing elétrica/hidráulica |
| Lancha 10–18 m (capstan) | 300–1.500 kg | 500–1.500 W DC 12/24 V | Capstan elétrico |
| Iate 18–30 m (capstan) | 1.500–5.000 kg | 1–3 kW hidráulico ou AC | Capstan hidráulico |
| Mega-yacht 30 m+ | 5.000 kg+ | 3 kW+ hidráulico | Capstan hidráulico com HPU central |

## Carga real e regime de uso

A carga não é apenas o "peso" teórico do que se move. É preciso considerar:

- **Atrito** — cabo passando por roldanas, bloqueios, stoppers acumulam perda.
- **Enrolamento no tambor** — primeira volta trabalha em raio pequeno (torque maior); 5ª volta trabalha em raio maior (carga linear menor por unidade de torque).
- **Ângulo de entrada da linha (fleet angle)** — desalinhamento gera carga lateral e desgaste.
- **Choques de carga** — rajada de vento na vela, queda de espia, impacto de mar.
- **Operação intermitente** — duty cycle S2 precisa ser respeitado.
- **Sobrecarga por manobra inadequada** — cabo bloqueado em stopper enquanto catraca continua tracionando.

### Regra prática veleiros

Catraca self-tailing elétrica em **velocidade 1 (mais lenta, mais torque)** entrega ~3× a carga da velocidade 3. Muitas falhas vêm de operar em velocidade alta com vento forte.

Em convés, **a carga dinâmica costuma ser mais severa do que o operador imagina**.

## Arquitetura do sistema

### Elementos típicos

- **Motor elétrico** — DC (12 V, 24 V) ou AC trifásico com variador.
- **Redutor** — redução epicicloidal (planetária) tipicamente 40:1 a 120:1 em catraca de vela; sinfim-coroa em capstan.
- **Embreagem multispeed** — mecanismo que seleciona velocidade conforme sentido da manivela/motor (em catracas self-tailing).
- **Tambor** — polido ou gravado, com mordente self-tailing no topo.
- **Self-tailing jaws** — mandíbula automática que "morde" a linha; dimensão específica por diâmetro de cabo (6–12 mm, 10–16 mm, etc.).
- **Contatores/relés de potência** — geralmente bipolares para inverter sentido (onde aplicável; muitas catracas operam em sentido único).
- **Controle** — botoeira no convés, pedal no pé do mastro, ou controle remoto.
- **Circuito de proteção** — fusível DC + disjuntor.
- **Estrutura mecânica de convés** — base parafusada em reforço estrutural; carga pode chegar a 2.000+ kg transmitidos ao laminado ou alumínio.

## Integração elétrica

Como em outros atuadores de convés, os pontos críticos são:

- **Corrente de pico** — catraca de vela 40 ST elétrica puxa ~40 A em 12 V @ 500 W; capstan 1,5 kW puxa 125 A em 12 V.
- **Queda de tensão em percursos longos** — banco no motor, catraca no convés de proa, 10–15 m de cabo.
- **Qualidade das conexões expostas** — ambiente marítimo ataca terminais de cobre; usar terminais estanhados (tin-plated) e heat-shrink com adesivo.
- **Coordenação de fusível/disjuntor e contatores** — fusível protege o cabo, disjuntor protege o motor; coordenar.
- **Retorno elétrico confiável** — negativo ao banco em seção adequada e com terminal crimpado (não apertar parafuso sobre olhal mal crimpado).

### Dimensionamento prático DC

| Catraca | Tensão | Pico | Seção cabo (ida+volta 12 m) | Fusível |
|---|---|---|---|---|
| Self-tailing 40 ST elétrica | 12 V | 40 A | 6 mm² (10 AWG) | 60 A |
| Self-tailing 60 ST elétrica | 12 V | 70 A | 16 mm² (6 AWG) | 100 A |
| Self-tailing 80 ST elétrica | 24 V | 55 A | 16 mm² (6 AWG) | 80 A |
| Capstan 1,5 kW | 12 V | 125 A | 35 mm² (2 AWG) | 175 A |
| Capstan 2,5 kW | 24 V | 100 A | 25 mm² (4 AWG) | 150 A |

Ver também:

- [[Bancos de Bateria]]
- [[Dimensionamento de Cabos DC — Cálculo Prático]]
- [[Fusíveis DC — Proteção Contra Sobrecorrente]]

## Controles e segurança operacional

O sistema precisa permitir:

- **Operação com boa visibilidade** da manobra — operador vê a linha e o destino.
- **Parada imediata** — botão de emergência acessível sem desvio visual.
- **Controle compatível com risco** — aprisionamento de dedos, chicote de cabo.
- **Entendimento claro de sentido e resposta** — rotulagem clara dos botões; botão único (start-stop) ou duplo (sentido-velocidade).
- **Dead-man control** — catraca só move enquanto botão estiver pressionado; solta = para.

### Riscos específicos de convés

- **Chicote de cabo** — cabo sob alta tração rompe e chicoteia; fatal se atingir rosto.
- **Aprisionamento de dedos** — dedos entre cabo e mordente; lesões graves. Nunca enrolar cabo na mão.
- **Tropeço no cabo** — cabo no convés é perigo de queda, especialmente com onda.
- **Queda sobre a catraca** — topo da catraca de vela é alto, operador desequilibrado pode cair sobre ela.

Em equipamentos de convés, **ergonomia ruim vira risco real** — norma NR-12 (BR) e EN ISO 12100 (EU) tratam explicitamente deste ponto.

## Óleo e graxa

### Catracas self-tailing mecânicas / elétricas

As catracas de vela são um caso especial: a **maior parte das superfícies de contato é lubrificada com graxa específica**, não óleo:

| Componente | Lubrificante | Intervalo |
|---|---|---|
| Engrenagens planetárias (serviço seco) | Harken Winch Grease ou Lewmar/Andersen Winch Grease | 1 temporada (anual) |
| Rolamentos do tambor | Graxa marítima NLGI 2 lítio complexo | 1 temporada |
| Pinhões da embreagem multispeed | Óleo leve SAE 20 ou graxa específica | 1 temporada |
| Dentado dos pawls (catracas de trava) | Óleo leve (teflon) ou graxa leve | 1 temporada |

> [!warning] Não use graxa genérica em catraca de vela
> Graxa automotiva pesada (lítio NLGI 3 ou cálcio) atrai sal e forma pasta abrasiva. Graxa marinha pesada trava a catraca em temperatura baixa. Use a graxa específica do fabricante ou graxa de lítio complexo NLGI 2 com aditivos antifricção PTFE.

### Catracas elétricas com redutor em banho de óleo

Modelos como Lewmar Evo Electric, Harken Rewind Electric, ou capstans de maior porte têm redutor fechado em banho de óleo:

| Tipo redutor | Óleo | Capacidade | Troca |
|---|---|---|---|
| Planetário (Lewmar Evo Electric, Harken Rewind) | SAE 75W-90 GL-4 ou sintético leve | 0,2–0,5 L | 1.000 h ou 2 anos |
| Sinfim-coroa (capstan antigo) | SAE 80W-90 GL-4 (**GL-5 pode atacar bronze** — consultar manual) | 0,3–1 L | 1.000 h ou 2 anos |
| Capstan hidráulico | Óleo ISO VG 32 ou 46 HLP/HVLP | 0,5–2 L (reservatório) | 2.000 h (ver [[Óleos Hidráulicos Marine — Guia Completo]]) |

## Falhas mais comuns

1. **Queda de tensão sob carga** — cabo subdimensionado, banco fraco, conexões oxidadas.
2. **Contator fatigado** — relé com contato queimado; catraca não liga ou liga intermitente.
3. **Motor aquecendo ou perdendo torque** — sobrecarga, duty cycle violado, enrolamento danificado.
4. **Travamento mecânico** — objeto preso entre cabo e tambor, bronzina travada.
5. **Sobrecarga de linha** — cabo passando por stopper bloqueado com catraca ainda tracionando.
6. **Cabo trabalhando fora da geometria correta** — fleet angle errado, cabo se cruzando no tambor.
7. **Corrosão de terminais e chicote** — sal, umidade, falta de manutenção.
8. **Self-tailing jaws desgastadas** — escorrega, não prende.
9. **Motor queimado** por violação crônica de duty cycle.
10. **Óleo/graxa ressecada** — catraca manual gira duro; elétrica puxa mais corrente.

## Diagnóstico profissional

### Perguntas certas

1. A **carga aplicada** está dentro do envelope real do equipamento (consultar manual)?
2. A **tensão nos terminais** se mantém aceitável sob esforço (≥ 11,5 V em 12 V na partida)?
3. O problema é **elétrico, mecânico ou operacional**?
4. O sistema de **comando está íntegro** (sem water ingress, sem corrosão no botão)?
5. O **redutor está silencioso** ou apresenta ruído (clicks, battidas, rangido)?
6. As **mandíbulas self-tailing** estão com dentado íntegro ou polido?

### Ensaios úteis

- Medir tensão no motor durante manobra com carga típica (voltímetro ou logger).
- Observar aquecimento de cabo, contator e terminais (termografia).
- Inspecionar ruído mecânico, travas e redutor.
- Verificar histórico de operação em sobrecarga (log de uso, se houver).
- Inspeção visual das mandíbulas self-tailing (cabo comprime aço com o tempo, espera-se desgaste).
- Medir consumo em vazio e com carga — comparar com spec.

## Boas práticas

- **Separar conceitualmente catraca e guincho de âncora** — tratamento técnico, proteção, óleo e procedimento são distintos.
- **Projetar para carga dinâmica**, não apenas estática.
- **Manter circuito curto e robusto** — cabo grosso, ida-volta mínima.
- **Proteger o controle e a potência contra corrosão** — terminais estanhados, heat-shrink, IP67 em botões.
- **Inspecionar linha, tambor, fixação e contatores** periodicamente (anual em cruiser, semestral em charter ou comercial).
- **Respeitar duty cycle** — não forçar içamento contínuo de vela grande em catraca subdimensionada.
- **Usar linha de diâmetro correto** para as mandíbulas self-tailing (não improvisar).
- **Re-graxear anualmente** redutor e rolamentos (off-season é ideal).
- **Troca preventiva de contator** em catracas de uso intenso (charter, regata), 5 anos ou 500 ciclos.
- **Treinamento** — veleiro de charter deve treinar hóspede mínimo antes de usar catraca elétrica.

## Erros comuns

- Usar a catraca para função que deveria ser de guincho (fundeio com capstan queima motor ou quebra redutor).
- Dimensionar pelo "peso do objeto" e ignorar esforço real.
- Improvisar controle sem segurança de operação (sem dead-man, sem emergência).
- Negligenciar queda de tensão em circuito de convés.
- Insistir em uso com trava ou cabo mal alinhado.
- Misturar graxa de fornecedores diferentes sem limpeza entre aplicações.
- Usar graxa automotiva em catraca de vela.
- Usar GL-5 em redutor sinfim-coroa de bronze.
- Não trocar óleo do redutor por anos (catraca fica dura, motor puxa mais corrente, queima em cascata).
- Operar catraca com cabo de aço (a menos que o modelo seja projetado para isso — raro).
- Ignorar aquecimento no uso — catraca cheirando queimado é falha iminente.

## Normas aplicáveis

### Normas elétricas

- **ABYC E-11** — AC and DC Electrical Systems on Boats.
- **ISO 10133** — Small craft DC systems.
- **ISO 13297** — Small craft AC systems.
- **USCG 33 CFR 183 Subpart I** (EUA).
- **NBR 5410** — Instalações elétricas baixa tensão (Brasil).
- **IEC 60364** — Low-voltage installations.
- **EN 60204-32** — Electrical equipment for hoisting machines.

### Normas de içamento e segurança de máquinas

- **EN 14492-1** — Power driven winches.
- **CE 2006/42/EC** — Machinery Directive.
- **EN ISO 12100** — Safety of machinery — General principles.
- **EN ISO 13849-1** — Safety-related parts of control systems.
- **IEC 60529** — IP Code (grau de proteção).
- **NR-11** — Transporte e manuseio de materiais (Brasil).
- **NR-12** — Máquinas e equipamentos (Brasil).
- **NBR 8400** — Cálculo de equipamento de içamento.

### Normas de cabos têxteis e aço

- **ISO 4309** — Wire ropes — Inspection and discard.
- **ISO 2408** — Steel wire ropes general.
- **SAE J1614** — Wire Rope Marine Grade.
- **ISO 9554** — Fibre ropes — General specifications (cabos têxteis).
- **ISO 10556** — Fibre ropes — HMPE (Dyneema).

### Normas de óleo e graxa

- **ISO 6743-4, ISO 3448, ISO 11158, ISO 4406** — Óleo hidráulico.
- **SAE J306** — Gear oil viscosity.
- **API GL-4 / GL-5** — Gear oil service classification.
- **DIN 51524-2/-3** — HLP, HVLP.
- **DIN 51517-3** — CLP gear oil.
- **NLGI** — classes de graxa.

### Normas estruturais e convés

- **ABYC H-40** — Anchoring, Mooring and Strong Points (pontos de fixação).
- **ISO 12217** — Stability and buoyancy assessment.
- **ISO 12401** — Deck safety harness and safety line.

### Tabela comparativa por jurisdição

| Aspecto | EUA | Brasil | Internacional | Europa |
|---|---|---|---|---|
| Elétrica DC | ABYC E-11 | NORMAM + NBR 5410 | ISO 10133 | EN 60204-32 / IEC 60364 |
| Segurança máquina | OSHA 1910 | NR-12 | ISO 12100 | CE 2006/42/EC |
| Içamento | ASME B30 | NBR 8400 / NR-11 | ISO 4301 / EN 14492 | EN 14492-1 + FEM 1.001 |
| Óleo/graxa | SAE / API / NLGI | ANP + SAE | ISO 6743-4 / 11158 | DIN 51524 / DIN 51517 |
| Cabos têxteis | CI 2001 | NBR 13541 | ISO 9554 / 10556 | EN 14296 |
| Homologação | USCG 33 CFR | NORMAM-05 | ISO 8666 | RCD 2013/53/EU |

## Glossário rápido

- **Catraca** — termo BR para winch/capstan (dispositivo motorizado de tração de cabo).
- **Winch** — termo EN; dispositivo motorizado com tambor.
- **Self-tailing winch** — catraca com mordente automático para linha.
- **Capstan** — catraca vertical sem mordente, tambor simples.
- **Windlass** — guincho de âncora, trata corrente (ver [[Guincho]]).
- **Tambor (drum)** — parte rotativa onde enrola a linha.
- **Mordente / self-tailing jaws** — mandíbulas que "mordem" o cabo no topo da catraca.
- **Pawl** — dente de trava (catraca mecânica de direção única).
- **Embreagem multispeed** — mecanismo que seleciona velocidade por sentido de giro.
- **Relação de redução** — n° de voltas do motor por 1 volta do tambor (tipicamente 40:1 a 120:1).
- **Fleet angle** — ângulo entre cabo e plano do tambor; excesso causa desgaste e mau enrolamento.
- **Lead block** — bloco guia de cabo antes da catraca.
- **Stopper / clutch** — dispositivo de trava da linha após tração.
- **Halyard** — cabo que iza vela.
- **Escota (sheet)** — cabo que controla vela depois de izada.
- **Cunningham** — cabo que tensiona a borda de ataque da vela.
- **Dyneema / HMPE** — fibra de alta performance (poliet. UHMW).
- **Poliéster** — material tradicional de cabo têxtil marinho.
- **Duty cycle S2** — tempo máximo contínuo antes de resfriamento.
- **Duty cycle S3** — percentual de tempo ligado em um ciclo.
- **Dead-man control** — comando que só opera enquanto pressionado.
- **Botoeira pedal** — botão de pé, comum em catraca de vela elétrica.
- **Chicote (cable whip)** — movimento violento de cabo rompido sob tensão.
- **Graxa winch** — graxa específica com aditivos PTFE, NLGI 2.
- **NLGI** — escala de consistência de graxa (0 = fluida, 6 = cera).
- **HLP / HVLP** — classes DIN de óleo hidráulico.
- **ISO VG** — graduação de viscosidade ISO.
- **GL-4 / GL-5** — classes de gear oil.
- **Bronzina** — bucha de bronze; comum em coroas de sinfim e alguns rolamentos de catraca antiga.
- **Rolamento (bearing)** — esferas ou roletes entre tambor e eixo.
- **Eixo central** — eixo vertical fixo em torno do qual o tambor gira.
- **Redutor planetário (epicicloidal)** — conjunto de engrenagens com sol, planetas e coroa.
- **Redutor sinfim-coroa** — par de engrenagens autobloqueante.
- **Contator bipolar** — relé de potência que inverte sentido.
- **Class T / MRBF** — fusíveis DC de alta ruptura (aplicável em capstans grandes, não em winch de vela).
- **IP67 / IP68** — classe de proteção contra água em botoeira de convés.

## Integração com outras notas

- [[Óleos Hidráulicos Marine — Guia Completo]] — óleo e graxa aplicáveis.
- [[Guincho]] — distinção fundamental (windlass).
- [[Bancos de Bateria]]
- [[Dimensionamento de Cabos DC — Cálculo Prático]]
- [[Fusíveis DC — Proteção Contra Sobrecorrente]]
- [[Thruster]] — outro consumidor de alta corrente.
- [[Davit - Munk - Guindaste de Bote - Tender Lift]] — sistema análogo (cabo, contator, motor DC/hidráulico).
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]]

## Perguntas que esta nota responde

- O que diferencia catraca de guincho de âncora?
- Onde a catraca falha: elétrica, mecânica ou operacionalmente?
- Como alimentar e proteger corretamente esse atuador de convés?
- Que graxa/óleo usar em catraca self-tailing e em capstan?
- Posso usar a catraca do spinnaker para içar tender?
- Por que a catraca elétrica aquece rápido em vento forte?
- Quando substituir as mandíbulas self-tailing?
- Capstan hidráulico vale a pena em iate 25 m?
- Qual cabo usar: poliéster, Dyneema ou misto?
- O que a NR-12 e EN ISO 12100 exigem em comando de catraca?
