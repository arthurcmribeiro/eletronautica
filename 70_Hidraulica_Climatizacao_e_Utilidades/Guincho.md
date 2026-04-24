---
title: "Guincho"
note_type: "technical-note"
domain: "70_Hidraulica_Climatizacao_e_Utilidades"
source_file: "GUINCHO 50f19734f7fb8338bcfd819cb7823229.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "52"
tier_fase_6: "A"
reviewed_on: "2026-04-21"
review_jurisdiction:
  - "Brasil"
  - "internacional"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
  - "https://www.lewmar.com/"
  - "https://www.lofrans.com/"
  - "https://www.quickitaly.com/"
  - "https://www.maxwellmarine.com/"
review_level: "engineering-curated"
normas_citadas:
  - "ABYC A-16 - Electrical Safety"
  - "ABYC E-11 - AC and DC Electrical Systems on Boats"
  - "ABYC H-40 - Anchoring, Mooring, Towing, and Tie Down of Boats"
  - "ABYC H-3 - Boat Hull Maintenance (bonding of metal appendages)"
  - "ABYC P-24 - Electric Propulsion Systems"
  - "ISO 10133:2017 - Small craft - Extra-low-voltage DC installations"
  - "ISO 13297:2020 - Small craft - AC installations"
  - "ISO 15084:2003 - Small craft - Anchoring, mooring and towing - Strong points"
  - "ISO 7840:2013 - Small craft - Fire-resistant fuel hoses (reference for rope/hawser classes)"
  - "ISO 12215 - Small craft - Hull construction and scantlings"
  - "ISO 8846:1990 - Small craft - Electrical devices - Protection against ignition of flammable gases"
  - "IEC 60529:2013 - Degrees of protection provided by enclosures (IP Code)"
  - "IEC 60068-2-11 - Salt mist testing"
  - "UL 1500 - Ignition-Protected Marine Products"
  - "SAE J1171 - Marine Ignition Protection"
  - "DIN 766 - Chain for chainwheels (short link)"
  - "ISO 4565 - Short link chain for chain conveyors and elevators"
  - "ISO 3448:1992 - Industrial liquid lubricants - ISO viscosity classification"
  - "ISO 11158:2023 - Hydraulic fluids Family H"
  - "SAE J306 - Automotive Gear Lubricant Viscosity Classification (gearbox of windlass)"
  - "API GL-4 / GL-5 - Gear Oil Service Classifications"
  - "DIN 51517 Part 3 - Gear oils CLP"
  - "ABS Guide for Certification of Lifting Appliances (for commercial vessels)"
  - "DNV-GL Rules for Classification: Ships Part 4 Chapter 6 - Piping systems and lifting appliances"
  - "IMO MSC.1/Circ.1331 - Guidelines for construction, installation, maintenance and inspection/survey of means of embarkation and disembarkation"
  - "CE Machinery Directive 2006/42/EC (for EU-flagged vessels)"
  - "EN 13157:2004 + A1:2009 - Cranes - Safety - Hand powered cranes"
  - "EN 14492-1:2006 + A1:2009 - Cranes - Power driven winches and hoists"
  - "ISO 4309:2017 - Cranes - Wire ropes - Care and maintenance, inspection and discard"
  - "NR-12 - Segurança no Trabalho em Máquinas e Equipamentos (comercial)"
  - "NBR 11213:2020 - Óleos hidráulicos"
  - "NBR 14134:2015 - Óleos lubrificantes - Terminologia"
  - "NORMAM-01/DPC - Embarcações empregadas na navegação em mar aberto"
  - "NORMAM-03/DPC - Embarcações empregadas na navegação interior"
  - "NORMAM-05/DPC - Homologação de material de salvatagem"
aliases:
  - "GUINCHO"
  - "Windlass"
  - "Âncora elétrica"
  - "Molinete"
seo_title: "Guincho de âncora (windlass) em embarcações: cabos, banco, óleo e falhas"
seo_description: "Guia técnico sobre windlass de âncora: gypsy, corrente, cabo, queda de tensão, banco dedicado de proa, contatores, óleo de redução, duty cycle e diagnóstico de falhas."
seo_keywords:
  - "guincho âncora barco"
  - "windlass marine"
  - "queda de tensão guincho proa"
  - "bateria guincho âncora"
  - "óleo redução windlass"
  - "Lewmar Lofrans Maxwell Quick"
geo_queries:
  - "Por que o guincho de âncora perde força ou não recolhe a corrente?"
  - "Como dimensionar cabos e alimentação do windlass da embarcação?"
  - "Qual óleo usar na redução do guincho Lewmar/Lofrans/Maxwell?"
related_notes:
  - "Óleos Hidráulicos Marine — Guia Completo"
  - "Catraca"
  - "Bancos de Bateria"
  - "Dimensionamento de Cabos DC — Cálculo Prático"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Relés e Relés de Estado Sólido"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
---

# Guincho

> [!abstract] Resumo técnico
> O guincho de âncora, ou `windlass`, é um atuador de alta demanda instalado longe do centro elétrico da embarcação. Seu comportamento é dominado por queda de tensão, qualidade do banco, contatores, regime de uso, estado da corrente/gypsy, óleo da redução e procedimento de ancoragem. Muito "guincho ruim" é, na prática, instalação ruim. Em uso comercial, aplica-se NR-12 e regulamentos de classificação.

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **Windlass é equipamento intermitente** — duty cycle típico 5-10 min ligado em 1 h; uso contínuo queima motor ou contator.
> 2. **Queda de tensão na proa é problema estrutural** — cabo 10-15 m do banco até proa com 80-300 A pede bitola generosa (1/0 AWG a 4/0 AWG / 50-120 mm²).
> 3. **Banco dedicado na proa resolve 80% dos "windlass fraco"** — banco de 100-200 Ah próximo ao guincho + carregador DC-DC ou bomba de equalização.
> 4. **Gypsy precisa ser compatível com a corrente** — DIN 766 (padrão europeu), ISO 4565 ou padrão americano (BBB, proof coil); errado gera pulos e falhas.
> 5. **Redutor usa óleo de engrenagem** — SAE 80W-90 GL-5, SAE 90 GL-5 ou óleo sintético específico; verificar anualmente em windlass de uso médio/alto.
> 6. **Contator é ponto de falha crítico** — deve ser marine-grade, ignition-protected se próximo de gases; dimensionado para stall current (400-600 A comum).
> 7. **Não puxar barco com windlass** — âncora presa deve ser aliviada com motor; insistir queima conjunto em minutos.
> 8. **Circuit breaker ou fusível dedicado** — tipicamente 150-250 A em barcos médios; proteção por corrente nominal + tempo.
> 9. **Chain counter / controle remoto é parte do sistema** — sensores Hall contam metros de corrente; falhas silenciosas são comuns se não inspecionados.

> [!danger] Quando chamar um especialista (9 cenários)
> 1. **Windlass "trabalhando" mas corrente não avança** — gypsy gasto/incompatível ou corrente fora de alinhamento; risco de disparo violento se soltar sob tensão.
> 2. **Fumaça ou cheiro de queimado** — motor em stall prolongado ou contator soldando; parar operação antes que propagar.
> 3. **Contator soldado ("travado ligado")** — windlass não para; único jeito de desligar é breaker principal; pode puxar corrente até o fim do stopper e arrancar estrutura.
> 4. **Botão de convés operando sozinho** — chicote em curto; pode ativar em navegação ou com pessoa sobre a corrente; desligar alimentação imediatamente.
> 5. **Corrente travada em boca do paiol** — forçar com motor pode romper gypsy ou boca de lobo; liberar manualmente.
> 6. **Âncora presa no fundo** — não usar windlass para arrancar; manobrar barco; insistir destrói conjunto em segundos.
> 7. **Queda da âncora durante navegação** — freio de desengate falhou ou trava de segurança solta; risco catastrófico (pode romper casco se arremessar).
> 8. **Corrosão galvânica severa no conjunto** — aço galvanizado em contato com inox pode acelerar; inspeção estrutural antes de próxima ancoragem.
> 9. **Perícia pós-acidente (desancoragem em mar, colisão com fundeio)** — preservar evidência; chain counter, logs e posição do gypsy.

## O que é

O `windlass` é o equipamento usado para arriar e recolher âncora, corrente e, em alguns arranjos, cabo combinado.

Ele normalmente envolve:

- motor elétrico (vertical ou horizontal, 12V ou 24V DC; raramente AC em yachts grandes);
- arquitetura hidráulica em yachts ou comerciais maiores;
- redutor (coroa sem-fim ou engrenagem planetária);
- `gypsy` (coroa) compatível com a corrente específica;
- eventual tambor adicional para cabo (warping drum);
- comando local (pedal ou botão no convés) e/ou remoto (breaker);
- circuito de potência dedicado.

**Fabricantes dominantes:**

- **Lewmar** — linha ampla Pro-Series, V-Series, Horizon;
- **Lofrans** — italiano, linha Tigres, Kobra, Falkon;
- **Maxwell** — RC, HWC, VWC;
- **Quick** — linha Genius, DP, Aleph;
- **Muir** — Austrália, uso em yachts maiores;
- **Steelhead** — pesca profissional, Alaska;
- **Ideal** — yachts clássicos.

## O que ele não deve fazer

Um erro clássico é usar o guincho para "puxar o barco" como se fosse equipamento de reboque ou içamento contínuo.

O procedimento de ancoragem e recuperação normalmente exige cooperação do barco:

- aliviar carga com propulsão quando necessário (manobrar para posição da âncora);
- evitar choques desnecessários (corrente em tensão súbita);
- não insistir em arrancar âncora presa só no motor elétrico.

Windlass é **pull-to-break** = corrente + âncora + paiol devem falhar antes do motor; mas o motor não é projetado para operação contínua nem para tração contra obstáculo fixo.

## Distância elétrica: problema estrutural

Como o guincho costuma ficar na proa, o circuito pode sofrer com:

- grande comprimento (10-20 m em barcos 40-60 pés);
- alta corrente (80-300 A em regime, 400-600 A em stall);
- queda de tensão severa (pode superar 1.5-2V em chicote subdimensionado);
- aquecimento de conexão (pontos de junção são vulneráveis);
- baixa performance exatamente sob maior carga.

É por isso que a arquitetura do circuito importa tanto.

**Cálculo prático de cabo (12V, 100 A em 15 m ida e volta):**

- queda 3% = 0.36V → resistência máxima admissível 0.0036 Ω;
- para 30 m total: Ω/m = 0.12 mΩ → exige 2/0 AWG (≈ 70 mm²);
- em 24V, mesma corrente, cabo 4 AWG é suficiente (corrente proporcional, queda proporcional).

Ver também:

- [[Dimensionamento de Cabos DC — Cálculo Prático]]
- [[Fusíveis DC — Proteção Contra Sobrecorrente]]

## Banco dedicado na proa

Em muitos casos, banco dedicado ou ponto de energia robusto próximo à proa melhora drasticamente:

- desempenho;
- queda de tensão;
- confiabilidade;
- desgaste do sistema.

Arquitetura comum:

- **banco pequeno dedicado** (80-200 Ah AGM ou LiFePO4) próximo ao windlass;
- **carregador DC-DC** ou **bomba de equalização** do banco principal para manter o banco de proa carregado;
- **breaker ou solenoide** que isola o banco de proa quando não em uso (evita corrente parasita e corrosão galvânica).

Nem todo barco precisa disso, mas muitos se beneficiam.

Ver também:

- [[Bancos de Bateria]]

## Gypsy, corrente e compatibilidade

O guincho depende da compatibilidade entre:

- tipo e bitola da corrente (DIN 766, ISO 4565, BBB, Proof Coil, HT);
- geometria do `gypsy` (coroa com pinos ou bolsos para elos);
- estado de desgaste do conjunto (gypsy gasto não agarra);
- alinhamento e condição do paiol de corrente (embaraço, nó, incrustação).

**Padrões de corrente comuns:**

| Padrão | Origem | Aplicação típica |
|---|---|---|
| DIN 766 | Alemanha/Europa | Padrão em windlass europeus (Lewmar, Lofrans, Quick) |
| ISO 4565 | Internacional | Equivalente DIN |
| BBB (Triple-B) | EUA | Comum em yachts americanos antigos |
| Proof Coil | EUA | Corrente leve, uso limitado marine |
| G4 / High Test (HT) | EUA | Corrente alta resistência, yachts modernos |
| G7 | EUA/Internacional | Uso pesado |
| Inox 316 | Premium | Não-magnética, resistência à corrosão |

Corrente errada ou desgastada pode simular falha elétrica.

## Contatores e comando

Além do motor, são críticos:

- **contatores/solenoides de potência** — marine-grade, tipicamente 150-500 A contínuo, 600-1000 A pico;
- **botão ou comando de convés** — estanque (IP67/68), com guarda física para evitar acionamento acidental;
- **retorno de massa** — conexão robusta ao negativo do banco de proa;
- **proteção coordenada** — breaker ou fusível por stall, não por nominal.

Falhas de comando podem produzir sintomas como:

- sobe mas não desce;
- apenas "clica";
- opera de forma intermitente;
- derruba proteção sob carga.

Ver também:

- [[Relés e Relés de Estado Sólido]]

## Regime de uso

O `windlass` é equipamento de serviço intermitente.

Tipicamente:

- **S2 10 min** — classificação IEC para operação intermitente 10 min;
- **S3 25%** — 25% de duty cycle (15 min em 1 h);
- **fabricantes marine** — 5-10 min de operação seguida por 30-60 min de descanso.

Uso prolongado acima do previsto gera:

- aquecimento do motor (escovas e coletor atingem > 100°C);
- queda de desempenho;
- aumento de corrente (por aumento de resistência do enrolamento);
- degradação de contatores e isolamento.

## Óleo da redução

Windlasses com redutor requerem óleo de engrenagem:

- **Lewmar Pro-Series / V-Series** — SAE 80W-90 GL-5 ou SAE 90 GL-5;
- **Lofrans** — óleo de engrenagem EP (extreme pressure) GL-4/GL-5;
- **Maxwell** — conforme manual; tipicamente SAE 80W-140 em aplicações pesadas;
- **Quick** — GL-5 SAE 80W-90;
- **Windlasses hidráulicos (yachts)** — ISO VG 46 HLP/HVLP no circuito principal + GL-5 na redução mecânica final.

**Inspeção típica:**

- nível: anual;
- troca: a cada 500 h ou 3-5 anos, o que vier primeiro;
- aspecto: óleo escuro/emulsionado indica contaminação (água do convés entrou via selo);
- vazamento: em selo de eixo é falha comum; reparo antes que água destrua rolamentos.

Ver também:

- [[Óleos Hidráulicos Marine — Guia Completo]]

## Falhas mais comuns

As falhas recorrentes são:

- queda de tensão excessiva (cabo subdimensionado, conexão oxidada);
- contator fatigado (contatos oxidados ou soldados);
- proteção mal coordenada (breaker desarmando prematuramente);
- `gypsy` incompatível ou desgastado (corrente pula ou não agarra);
- corrente mal assentada (embaraço no paiol);
- uso inadequado para arrancar âncora presa;
- corrosão em conexões de proa (chicote exposto sem vedação);
- escovas gastas (motor DC comum após 500-1000 ciclos);
- óleo da redução contaminado ou baixo;
- selo de eixo vazando (água no redutor).

## Diagnóstico profissional

Perguntas obrigatórias:

1. A tensão no motor está aceitável durante recolhimento real (medir na proa, não na popa)?
2. O banco ou fonte de energia sustenta a demanda (tensão no banco sob carga)?
3. Existe problema de comando, contator ou proteção (ouvir click, medir com multímetro)?
4. A corrente e o `gypsy` estão compatíveis (medir elo de corrente e comparar com spec do gypsy)?
5. O equipamento está sendo usado dentro do regime correto (intermitente vs contínuo)?
6. O óleo da redução está em nível e limpo?

Ensaios úteis:

- medir tensão no motor sob carga (recolhendo corrente pesada);
- inspecionar aquecimento em terminais e contatores (termografia se disponível);
- observar comportamento com âncora aliviada pelo barco;
- revisar `gypsy`, corrente e paiol;
- testar com chain counter se houver (contagem deve ser coerente);
- inspecionar escovas do motor (se acessíveis).

## Boas práticas

- dimensionar o circuito pelo cenário real de carga e distância;
- considerar solução dedicada na proa quando fizer sentido;
- manter contatores e conexões em estado excelente (semestral mínimo);
- usar o barco para aliviar esforço ao recuperar âncora;
- revisar compatibilidade entre corrente e `gypsy`;
- incluir óleo da redução no plano de manutenção anual;
- testar freio e desengate (clutch) regularmente;
- documentar marca/lote da corrente e tamanho do gypsy.

## Erros comuns

- tratar o windlass como equipamento de tração contínua;
- subdimensionar cabos por economia;
- ignorar a distância até a proa;
- culpar o motor por problema de instalação;
- operar com corrente incompatível ou paiol mal resolvido;
- não trocar óleo da redução porque "está lubrificado";
- instalar windlass de potência inferior à exigida pela corrente/âncora.

## Normas aplicáveis

### 1. Padrão elétrico de recreio (ABYC/ISO)

- **ABYC A-16** — Electrical Safety;
- **ABYC E-11** — AC and DC Electrical Systems on Boats (dimensionamento, proteção);
- **ABYC H-40** — Anchoring, Mooring, Towing (aplicação direta);
- **ABYC H-3** — Bonding;
- **ABYC P-24** — Electric Propulsion Systems (quando integra com propulsão);
- **ISO 10133:2017** — Extra-low-voltage DC installations;
- **ISO 13297:2020** — AC installations (windlass AC em yachts grandes).

### 2. Ancoragem e fixação

- **ABYC H-40** — Anchoring standard completo;
- **ISO 15084:2003** — Strong points (ancoragem);
- **ISO 12215** — Hull construction (reforço estrutural da proa).

### 3. Correntes e gypsies

- **DIN 766** — Chain for chainwheels (short link);
- **ISO 4565** — Short link chain equivalente;
- **ISO 4309:2017** — Wire ropes care and maintenance.

### 4. Lubrificantes e fluidos

- **ISO 3448:1992** — Viscosity classification;
- **ISO 11158:2023** — Hydraulic fluids (em windlass hidráulico);
- **SAE J306** — Gear lubricant viscosity (redução);
- **API GL-4 / GL-5** — Gear oil service;
- **DIN 51517 Part 3** — Gear oils CLP;
- **NBR 11213:2020** — Óleos hidráulicos (Brasil);
- **NBR 14134:2015** — Lubrificantes — Terminologia.

### 5. Segurança de máquinas (comercial)

- **CE Machinery Directive 2006/42/EC** (embarcações UE);
- **EN 14492-1:2006 + A1:2009** — Power driven winches and hoists;
- **EN 13157:2004 + A1:2009** — Hand powered cranes (referência);
- **NR-12** — Segurança em Máquinas (Brasil, uso comercial);
- **ISO 4309:2017** — Wire ropes — Care and maintenance.

### 6. Certificação para comerciais

- **ABS Guide for Certification of Lifting Appliances**;
- **DNV-GL Rules for Classification: Ships Part 4 Chapter 6**;
- **IMO MSC.1/Circ.1331** — Means of embarkation/disembarkation.

### 7. Proteção e ignição

- **IEC 60529:2013** — IP Code;
- **IEC 60068-2-11** — Salt mist;
- **ISO 8846:1990** — Protection against ignition;
- **UL 1500** — Ignition-Protected Marine Products;
- **SAE J1171** — Marine Ignition Protection.

### 8. Brasil (Marinha/ABNT)

- **NORMAM-01/DPC** — Mar aberto;
- **NORMAM-03/DPC** — Navegação interior;
- **NORMAM-05/DPC** — Homologação de material de salvatagem (referência);
- **NR-12** — Segurança em máquinas.

### Tabela comparativa por jurisdição

| Aspecto | EUA (ABYC) | Internacional (ISO/IEC) | Europa (EN/CE) | Brasil (Marinha/ABNT/MTE) |
|---|---|---|---|---|
| Instalação elétrica | ABYC E-11, A-16 | ISO 10133, ISO 13297 | CE 2006/42/EC | NORMAM (referencia) |
| Ancoragem | ABYC H-40 | ISO 15084 | CE | NORMAM |
| Corrente | — (OEM) | DIN 766, ISO 4565 | EN (referencia) | NBR adota ISO |
| Óleo redução | SAE/API GL | ISO 3448, API GL | DIN 51517 | NBR 14134 |
| Segurança máquinas | — | — | EN 14492-1, CE 2006/42 | NR-12 |
| Certificação comercial | ABS | IMO | DNV-GL, LR | NORMAM |

## Glossário rápido

- **Windlass** — guincho de âncora; equipamento elétrico ou hidráulico para arriar/recolher.
- **Molinete** — termo em português para windlass (menos usado).
- **Âncora** — dispositivo de fundeio (Bruce, CQR, Danforth, Rocna, Ultra, Mantus, Spade).
- **Corrente** — elo a elo; transmite tração da âncora ao barco.
- **Cabo (rode)** — cordame que conecta a corrente ao barco em configuração parcial.
- **Gypsy (chainwheel)** — coroa com pinos/bolsos para engate da corrente.
- **Tambor de cabo (warping drum)** — tambor adicional para cabo; girador sem gypsy.
- **Paiol de corrente (chain locker)** — compartimento onde a corrente fica armazenada.
- **Boca de lobo / hawsepipe** — orifício por onde a corrente sai do paiol para o gypsy.
- **Freio (clutch)** — mecanismo para soltar a âncora em queda livre controlada.
- **Chain counter** — contador de metros da corrente; sensor Hall típico.
- **Stopper / chain stopper** — trava mecânica que retém corrente quando fundeado.
- **DIN 766** — padrão europeu de corrente curta.
- **BBB / Proof Coil** — padrões americanos de corrente.
- **G4 / G7 / HT (High Test)** — corrente alta resistência.
- **Inox 316** — corrente premium não-magnética.
- **Short link / long link** — comprimento relativo do elo; compatibilidade com gypsy.
- **Stall current** — corrente máxima do motor bloqueado (400-600 A comum).
- **Stall torque** — torque máximo ao bloqueio; não deve ser excedido em uso contínuo.
- **Duty cycle S2/S3** — classificação IEC de operação intermitente.
- **Motor DC escovado** — motor padrão em windlass; escovas gastam com ciclos.
- **Motor DC sem escovas (BLDC)** — linha moderna; vida útil maior.
- **Redução coroa sem-fim** — redutor típico; razão 50:1 a 200:1.
- **Planetário** — alternativa em windlasses maiores/profissionais.
- **Contator / solenoide de potência** — chave eletromagnética de alta corrente.
- **Relé auxiliar** — comando que aciona o contator.
- **Breaker DC** — disjuntor rearmável; substituto preferido em circuitos de alta corrente.
- **Fusível Class T / MRBF / ANL** — fusíveis DC de alta capacidade.
- **Banco de proa** — banco dedicado próximo ao windlass; resolve queda de tensão.
- **DC-DC charger** — carregador que mantém banco de proa a partir do principal.
- **Queda de tensão** — ABYC recomenda ≤ 10% em pico, ≤ 3% em regime crítico.
- **Bus bar** — barra condutora para distribuição.
- **Ponto de massa** — conexão ao negativo; crítico em DC de alta corrente.
- **Ignition-protected** — componente certificado para não inflamar gases.
- **IP67 / IP68** — grau de proteção para comando de convés.
- **Inox 316L** — aço inoxidável padrão marine.
- **Bronze naval** — liga resistente à corrosão.
- **Galvanizado a fogo (hot-dip galvanized)** — revestimento de zinco em corrente de aço.
- **Anodo sacrificial** — zinco que corrói protegendo windlass.
- **Corrosão galvânica** — processo entre metais dissimilares.
- **Chuveiro** — instalação para lavar corrente ao recolher (evita sujeira no paiol).
- **Snubber** — cabo amortecedor que isola corrente de proa durante fundeio.
- **Kellet** — peso adicional na corrente para melhorar ângulo.
- **Catenária** — curva que a corrente forma entre barco e âncora.
- **Scope** — razão entre comprimento de corrente e profundidade (5:1 típico, 7:1 em mar pesado).
- **Pull-to-break** — filosofia: outros componentes devem falhar antes do motor.
- **NR-12** — segurança em máquinas (Brasil, uso comercial).
- **CE Machinery Directive 2006/42/EC** — diretiva UE.
- **EN 14492-1** — norma europeia de winches e hoists.

## Integração com outras notas

- [[Óleos Hidráulicos Marine — Guia Completo]]
- [[Catraca]]
- [[Bancos de Bateria]]
- [[Dimensionamento de Cabos DC — Cálculo Prático]]
- [[Fusíveis DC — Proteção Contra Sobrecorrente]]
- [[Relés e Relés de Estado Sólido]]
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]]

## Perguntas que esta nota responde

- Como o windlass deve ser alimentado e protegido?
- Por que o guincho perde força na proa?
- Onde separar falha elétrica, falha mecânica e erro de operação?
- Qual óleo de engrenagem usar na redução do Lewmar, Lofrans, Maxwell, Quick?
- Quando instalar banco dedicado na proa?
- Quais normas aplicam-se a windlass em embarcação comercial?
