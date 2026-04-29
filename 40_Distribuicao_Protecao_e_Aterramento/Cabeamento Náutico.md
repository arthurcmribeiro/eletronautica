---
title: "Cabeamento Náutico"
note_type: "technical-note"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "CABEAMENTO NÁUTICO 33a19734f7fb81a3b4a1c4138078865d.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "57"
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
  - "https://www.ul.com/services/ul-1426"
  - "https://webstore.iec.ch/publication/4"
normas_citadas:
  - "ABYC E-11 (AC and DC Electrical Systems on Boats) — capítulo 15 (condutores), 16 (métodos de instalação), 17 (proteção mecânica)"
  - "ABYC E-30 (Electric Propulsion Systems) — cabos de tração e alta corrente"
  - "ABYC TE-4 (Lightning Protection) — requisitos para condutores de descida"
  - "ABYC S-32 (Electrical Installations on Vessels Under 20 m) — síntese prática"
  - "ISO 10133:2012 (Small craft — Electrical systems — Extra-low-voltage DC)"
  - "ISO 13297:2020 (Small craft — Electrical systems — AC installations)"
  - "ISO 6722-1 (Road vehicles — 60 V and 600 V single-core cables) — referência para cabo primário"
  - "ISO 8820 (Road vehicles — Fuse-links) — coordenação fusível/cabo"
  - "ISO 19642 (Road vehicles — Automotive cables) — espec. moderna substituindo parte do 6722"
  - "IEC 60228 (Conductors of insulated cables — classes 1 a 6 de flexibilidade)"
  - "IEC 60332-1 (Tests on electric cables under fire conditions — single cable)"
  - "IEC 60332-3 (Bunched wires — Category A/B/C flame-retardant)"
  - "IEC 60754-1/-2 (Halogen-free / low-smoke test on gases evolved during combustion)"
  - "IEC 61034-1/-2 (Measurement of smoke density — LS0H low-smoke zero-halogen)"
  - "IEC 60287 (Electric cables — Calculation of current rating)"
  - "IEC 60364-5-52 (Selection and erection — Wiring systems)"
  - "IEC 60092-350 a 60092-376 (Electrical installations in ships — shipboard cables)"
  - "IEC 60092-353 (Power cables for rated voltages 0,6/1 kV) — padrão internacional de cabo naval"
  - "IEC 60092-376 (Cables for control and instrumentation circuits)"
  - "UL 1426 (Electrical Cables for Boats) — padrão americano BC5W2"
  - "UL 1309 (Marine Shipboard Cable)"
  - "UL 83 (Thermoplastic-Insulated Wires and Cables)"
  - "UL 44 (Thermoset-Insulated Wires and Cables)"
  - "SAE J378 (Marine Propulsion Wiring Systems)"
  - "SAE J1127 (Battery cable)"
  - "SAE J1128 (Low-voltage primary cable)"
  - "NFPA 70 (NEC) — art. 310 (condutores), art. 555 (marinas e boatyards)"
  - "ABNT NBR 5410 (Instalações elétricas de baixa tensão) — Tab. 36 a 41 ampacidade"
  - "ABNT NBR NM 247-1/-3 (Cabos isolados com PVC — 450/750 V)"
  - "ABNT NBR 7286/7287/7288 (Cabos EPR/XLPE/PVC para baixa tensão)"
  - "ABNT NBR 14039 (Instalações elétricas de média tensão)"
  - "NORMAM-05/DPC (Embarcações de esporte e recreio)"
  - "NORMAM-01/DPC (Embarcações na navegação marítima)"
  - "USCG 33 CFR 183.425 a 183.460 (Conductors — sizing and protection)"
  - "DNV-RU-SHIP Pt.4 Ch.8 (Electrical installations) — classificadora europeia"
  - "Lloyd's Register / BV / RINA — regras para cabos navais classificados"
  - "NMEA 2000 / SAE J1939 — cabeamento de rede (backbone/dropper, terminação 120 Ω)"
family_clusters:
  - "ABYC-USCG (EUA)"
  - "ISO-IEC-UL (internacional)"
  - "ABNT-NORMAM (Brasil)"
  - "IEC 60092-class (navios classificados)"
aliases:
  - "CABEAMENTO NÁUTICO"
  - "Cabo marinho"
  - "Marine cable"
  - "Fio náutico"
seo_title: "Cabeamento Náutico"
seo_description: "CABEAMENTO NAUTICO — Conjunto de condutores e criterios de instalacao para ambiente marinho, com foco em material, ampacidade, queda de tensao, roteamento, protecao mecanica e identificacao."
seo_keywords:
  - "Cabeamento nautico"
  - "Cabo marinho"
  - "Ampacidade"
  - "Queda de tensao"
  - "40 Distribuicao Protecao e Aterramento"
geo_queries:
  - "Como especificar cabeamento nautico?"
  - "Qual a diferenca entre cabo marinho e cabo comum?"
  - "Quando usar cabo BC5W2 ou IEC 60092?"
related_notes:
  - "Barramento DC / Bus Bar / Distribuição DC"
  - "Terminais Conectores e Emendas"
  - "Dimensionamento de Cabos DC — Cálculo Prático"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Disjuntores (DC) e (AC)"
  - "NMEA 2000 / NMEA 0183 — Rede de Instrumentos"
---

# Cabeamento Náutico

> [!abstract] Resumo técnico
> Cabeamento náutico é o conjunto de condutores e critérios de instalação elétrica aplicados ao ambiente marinho. O desempenho do sistema não depende só da bitola: material do condutor, isolamento, classe térmica, flexibilidade, roteamento, proteção mecânica, terminação e identificação pesam tanto quanto o cálculo elétrico. A principal diferença para instalação automotiva ou predial é a combinação de três agressões simultâneas: névoa salina + vibração cíclica + ciclo térmico — que favorece condutor de cobre estanhado classe 5 flexível, isolamento XLPE/EPR termofixo e classe IEC 60092 ou UL 1426 BC5W2 conforme jurisdição.

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **Cobre estanhado, sempre** — em DC > 24 V ou AC 120/240 V, cobre nu vira verdete e perde ampacidade em 2-3 anos; custo extra do estanho (~10%) paga-se no primeiro refit evitado.
> 2. **Classe 5 flexível mínimo** (IEC 60228) — rigidez classes 1/2 quebra por fadiga em zonas de vibração (motor, casaria); em motor e thruster use classe 6 extra-flexível.
> 3. **Dimensione por ampacidade E por queda de tensão** — circuitos DC críticos (bomba de porão, VHF, ignição, eletrônica) exigem ΔV ≤ 3% ida-e-volta; iluminação/carga não-crítica ≤ 10%.
> 4. **Coordene cabo ⇄ proteção** — o fusível/disjuntor protege o cabo, não a carga; seção mínima conforme ABYC E-11 Tab. XVII (10 AWG → 35 A, 6 AWG → 60 A, etc.).
> 5. **Método de instalação muda ampacidade** — em conduíte fechado sem ventilação, derate ~30%; em feixe de 6+ condutores, derate 40-50% (IEC 60364-5-52 Anexo B).
> 6. **Raio de curvatura ≥ 6× diâmetro externo** — dobra menor fratura filamentos internos ao longo do tempo (efeito do rizzo).
> 7. **Suporte a cada 450 mm (18") em horizontal, 600 mm (24") em vertical** — ABYC E-11.15.6; vibração sem suporte fadiga terminação.
> 8. **Nunca passe potência DC > 50 A paralelo ao NMEA 2000/cabo de eletrônica** — separação ≥ 150 mm (6") ou cruzamento 90° reduz acoplamento capacitivo e indutivo.
> 9. **Etiquete nas duas pontas + no meio** em cabos > 3 m — padrão com heat-shrink impresso + diagrama unifilar sincronizado; cor é pista, etiqueta é prova.

> [!danger] Quando chamar um especialista
> Estes 9 cenários exigem engenheiro elétrico náutico ou certificador, não eletricista generalista:
> 1. **Cabo de propulsão elétrica (Tração > 5 kW, Li-Fe > 48 V)** — ABYC E-30 exige dimensionamento específico com análise de ondulação térmica, curto presumido e classe de isolação; erro resulta em incêndio em alta corrente DC.
> 2. **Retrofit que atravessa compartimento com risco de gás** (sala de baterias chumbo-ácido ventilada, paiol de combustível) — exige cabo ignition-protected ou passagem em conduíte selado conforme ISO 8846 / 33 CFR 183.410.
> 3. **Embarcação comercial sob classificadora (DNV, Lloyd's, BV, RINA, ABS)** — cabo naval classificado IEC 60092-353 com certificado de origem, ensaios IEC 60332-3-22 (flame-retardant Categoria A), IEC 60754 (halogen-free) e IEC 61034 (low-smoke).
> 4. **Sistema híbrido/elétrico com inversor > 3 kW e cabos DC > 100 mm² (4/0 AWG)** — estudo de curto-circuito, força eletrodinâmica (Lorentz) e coordenação com barramento classe T é obrigatório.
> 5. **Passagem em zona de alta temperatura** (coletor de escape, motor interno, turbina) — requer cabo silicone ou fluoropolímero (FEP/PTFE/ETFE) com classificação ≥ 150 °C; PVC/polietileno funde.
> 6. **Cabeamento de rede NMEA 2000/N2K em barco com inversor de alta frequência** — análise de EMC, terminação 120 Ω, segregação de backbone e impedância de malha exigem conhecimento específico de redes CAN.
> 7. **Sistema CA de terra (shore power) 240 V split-phase ou trifásico** — ABYC E-11 anexo sobre inversores, isoladores galvânicos, IT-system × TN-S e proteção diferencial (GFCI/RCD) exige análise jurisdição-por-jurisdição.
> 8. **Cabeamento em fibra de vidro laminada molhada** (aramação de cabo detectada com trincas, osmose próxima, delaminação) — risco de corrente de fuga pela estrutura; investigação estrutural + elétrica combinada.
> 9. **Certificação CE/RCD, NMMA Certified ou USCG inspection** — requer dossiê técnico com memorial de cálculo, coordenação cabo-proteção, teste de isolamento pós-instalação (500 V DC / 1 MΩ mínimo).

## O que é

Cabeamento náutico não é apenas "fio que aguenta água". É a combinação de:

- condutor adequado ao ambiente (cobre estanhado classe 5/6 em regra);
- isolação compatível com temperatura, óleo, vibração, UV e umidade;
- instalação coerente com movimento, abrasão e manutenção;
- documentação e identificação capazes de sustentar diagnóstico futuro.

Em embarcações, boa parte das falhas elétricas nasce na interface entre cabo, terminal e ambiente, não apenas no valor de corrente do circuito.

## Função na embarcação

- transportar energia com queda de tensão aceitável;
- manter integridade dielétrica em ambiente agressivo (salinidade, UV, ozônio);
- resistir a vibração, flexão e manutenção repetida;
- permitir inspeção, expansão e reparo com rastreabilidade;
- integrar com rede de dados (NMEA, N2K, CAN, Ethernet marítima) sem interferência mútua.

## Fundamentos mínimos

### Cabo correto não se escolhe só por bitola

É preciso considerar:

- **ampacidade** (corrente contínua máxima sem exceder T° do isolante);
- **queda de tensão** admissível (3% crítico / 10% não-crítico);
- **classe térmica** do isolamento (60/75/90/105/125/150/200 °C);
- **ambiente químico** (óleo, combustível, solvente, névoa salina);
- **flexibilidade** (classe IEC 60228: 1 rígido / 2 flexível / 5 muito flexível / 6 extra-flexível);
- **método de instalação** (bandeja, conduíte, feixe, exposto) e agrupamento.

### Ambiente marinho pune atalho

Um cabo que funciona em automóvel ou em instalação predial pode falhar cedo em presença de névoa salina, umidade persistente, vibração e aquecimento local. Os padrões diferenciados para náutica são:

- **UL 1426 BC5W2 (EUA)** — cobre estanhado, resistente a água, óleo, solvente, abrasão;
- **IEC 60092-353 (internacional/navios classificados)** — cabo naval com bainha XLPE/EPR, flame-retardant categoria A;
- **ISO 6722/19642 (UE automotivo, aplicável em recreio)** — temperatura e vibração especificadas.

### Cor ajuda, mas não substitui identificação

Padrões de cores existem, porém variam com norma, época da instalação e histórico da embarcação:

- **ABYC (EUA)** — Tabela XVI do E-11 define código: vermelho = +DC, preto/amarelo = -DC, verde = bonding, branco = neutro AC, preto = fase AC, verde/amarelo = PE AC.
- **ISO 10133/IEC 60092** — preto = neutro AC, marrom = fase AC, azul claro = neutro, verde/amarelo = PE, vermelho = +DC, azul escuro = -DC.
- **NBR 5410** — azul claro = neutro, verde ou verde/amarelo = PE, preto/vermelho/marrom/cinza = fase AC.

Em retrofit sério, etiqueta e documentação são tão importantes quanto a cor do isolante.

### Roteamento importa tanto quanto o cabo

Mesmo um excelente cabo vira fonte de falha se passar em borda cortante, ponto quente, região alagável ou zona de movimento sem proteção. Regras ABYC E-11.15:

- suporte a cada 450 mm (18") horizontal, 600 mm (24") vertical;
- proteção mecânica em passagem de anteparo (bucha ou grommet);
- afastamento de tubulações de combustível > 50 mm (2");
- cabo de bateria nunca abaixo do nível de sentina esperado.

## Seleção técnica do cabo

### Critérios principais

1. corrente contínua plausível (não soma dos disjuntores);
2. queda de tensão admissível para a função do circuito (3% crítico / 10% não-crítico);
3. comprimento elétrico real (ida + volta em DC);
4. classe de isolamento e temperatura (ambiente + aquecimento por condução);
5. flexibilidade necessária (classe 5 mínima em zonas de vibração);
6. ambiente de instalação (exposição a óleo, combustível, UV, salinidade).

### Tabela de referência — AWG × mm² × ampacidade (cabo único, 30 °C, ventilado)

| AWG | mm² (nominal) | Ampacidade 60 °C | Ampacidade 75 °C | Ampacidade 90 °C | Uso típico |
| --- | --- | --- | --- | --- | --- |
| 18 | 0,82 | 10 A | 15 A | 18 A | sinal, iluminação LED pequena |
| 16 | 1,3 | 15 A | 20 A | 25 A | iluminação, circuitos leves |
| 14 | 2,1 | 20 A | 25 A | 30 A | cargas médias |
| 12 | 3,3 | 25 A | 35 A | 40 A | bombas, cargas médias |
| 10 | 5,3 | 35 A | 50 A | 55 A | geladeira, eletrônica pesada |
| 8 | 8,4 | 50 A | 65 A | 75 A | inversor pequeno, winch |
| 6 | 13,3 | 65 A | 85 A | 95 A | thruster, bow/stern small |
| 4 | 21,2 | 85 A | 115 A | 130 A | inversor médio, partida diesel pequeno |
| 2 | 33,6 | 115 A | 150 A | 170 A | partida diesel médio |
| 1/0 | 53,5 | 150 A | 200 A | 225 A | inversor grande, thruster grande |
| 2/0 | 67,4 | 175 A | 230 A | 260 A | tração pequena |
| 4/0 | 107,2 | 230 A | 310 A | 360 A | tração média, banco 200 Ah |

*Valores aproximados baseados em ABYC E-11 Tab. XVII (classe 75 °C) e NFPA 70 Tab. 310.16; em feixe ≥ 4 condutores aplicar fator de redução 0,65.*

### Sobre bitolas e tabelas

Tabelas rápidas ajudam, mas não substituem o cálculo e as tabelas normativas completas. Ampacidade e queda de tensão variam com:

- temperatura ambiente (cada +10 °C reduz ~10% da ampacidade);
- agrupamento (feixe reduz ampacidade — IEC 60364-5-52 Anexo B);
- ventilação (conduíte fechado sem ventilação: derate 30%);
- número de condutores carregados;
- tipo de isolamento (XLPE/EPR > EPDM > PVC em T°);
- comprimento ida e volta (em DC, sempre calcular ida+volta; em AC monofásico, fase + neutro).

### Cálculo de queda de tensão em DC

Fórmula prática: **ΔV (V) = 2 × L × I × ρ / S**

- L = comprimento de um sentido (m);
- I = corrente (A);
- ρ = resistividade do cobre ~0,0175 Ω·mm²/m;
- S = seção (mm²).

ΔV% = (ΔV / V_nominal) × 100.

## Projeto e instalação

### Boas diretrizes de roteamento

- separar potência, sinal e RF sempre que a arquitetura pedir (150 mm / 6" mínimo);
- evitar pontos de abrasão e zonas de temperatura elevada;
- suportar o chicote adequadamente, sem deixar vão excessivo (450 mm horizontal / 600 mm vertical);
- usar proteção mecânica onde houver passagem por anteparas, bordas ou partes móveis (grommet, conduíte espiral, malha de aramida);
- manter o cabo fora de áreas sujeitas a água acumulada sempre que possível;
- raio de curvatura ≥ 6× diâmetro externo (≥ 8× em classe XLPE/EPR rígido);
- drip loop antes de conectores para evitar migração de água por capilaridade.

### Identificação

- identificar circuitos relevantes nas duas extremidades e, em cabos longos (> 3 m), também no meio;
- manter correspondência com diagrama unifilar e painel;
- evitar instalação "misteriosa" que só funciona para quem montou;
- preferir heat-shrink impresso (impressão a quente) a etiqueta adesiva que descola.

### Terminação

O cabo só é tão bom quanto sua terminação. Crimpagem inadequada, terminal incompatível ou selagem ruim destroem o benefício de um condutor bem escolhido:

- usar alicate de crimpagem certificado (ratchet-type com die correspondente ao terminal);
- terminal de cobre estanhado com heat-shrink adesivo (tipo "marine grade");
- torque conforme especificação do fabricante em bolt-on (ver nota [[Terminais Conectores e Emendas]]);
- teste de puxão (pull test) após crimpagem — 60 lbs para AWG 6 e maiores.

### Conduíte e proteção mecânica

- **Conduíte espiral** (split-loom) em trajetos internos sem agressão química — não é estanque;
- **Conduíte rígido PVC/PP** em casaria/convés com travessa de anteparo selada;
- **Malha expansível de aramida/nylon** em chicote de motor (resistente a abrasão e temperatura média);
- **Conduíte selado (liquid-tight)** em compartimento com risco de alagamento ou gás.

## Onde costuma dar problema

| Problema | Causa provável | Correção |
| --- | --- | --- |
| queda de tensão alta | bitola insuficiente, cabo longo demais ou conexão degradada | recalcular ΔV com fórmula; aumentar seção ou encurtar cabo |
| aquecimento do chicote | sobrecorrente, agrupamento ruim ou terminal deficiente | separar feixe, verificar corrente real, trocar terminais |
| falha intermitente | vibração, flexão cíclica ou terminal mal crimpado | reforçar suporte, usar classe 6 em zona de vibração, refazer crimpagem com alicate certificado |
| corrosão sob isolamento | ambiente agressivo e vedação ruim (wicking) | trocar por cobre estanhado + heat-shrink adesivo; verificar ponto de entrada de água |
| ruído em eletrônica | roteamento inadequado entre potência e sinal | separar ≥ 150 mm; trançar par diferencial; blindagem conectada em uma ponta só |
| rigidez e fratura filamentar | classe de flexibilidade inadequada | trocar para classe 5/6 em zona de movimento |
| isolamento trincado por UV | cabo inadequado exposto a sol direto | usar cabo com bainha UV-resistente (TPU, XLPE-UV) ou reinstalar em trajeto protegido |

## Diagnóstico prático

1. **Medir queda de tensão** com a carga operando — comparar com cálculo teórico.
2. **Comparar corrente real** (alicate amperímetro) com a capacidade do conjunto cabo-instalação.
3. **Inspecionar terminais**, suportação, abrasão e zonas de aquecimento (visual + termografia se disponível).
4. **Verificar consistência** entre cor, etiqueta, diagrama e função real — só a medição confirma.
5. **Isolar se o defeito está no cabo, no terminal ou na carga** conectada (desconectar e medir cada trecho).
6. **Teste de isolação** (megôhmetro 500 V DC) entre condutor e massa — deve ser > 1 MΩ.
7. **Pull test** em terminações suspeitas (60 lbs para AWG 6).

## Boas práticas profissionais

- especificar cabo pelo conjunto elétrico e ambiental, não por hábito;
- usar material e isolamento compatíveis com o serviço real (cobre estanhado, XLPE/EPR, classe 5+);
- documentar bitola, origem, destino e proteção do circuito em diagrama unifilar;
- deixar manutenção possível sem desmontagem destrutiva do barco (service loop de 150 mm em pontos de manutenção);
- revisar periodicamente pontos de fixação, abrasão e terminação (anual ou 500 h);
- evitar emendas desnecessárias e improvisadas em trechos críticos;
- em refits, substituir trecho inteiro ao invés de remendar quando houver sinais de envelhecimento generalizado;
- manter registro de trocas e inspeções em arquivo de manutenção da embarcação.

## Erros comuns

- escolher cabo só pelo "parece grosso o bastante";
- assumir padrão de cores como verdade absoluta em barco usado;
- misturar circuitos de potência e sinal no mesmo caminho sem critério;
- deixar cabo tensionado, sem folga de serviço e sem proteção mecânica;
- resolver problema de queda de tensão aumentando fusível em vez de rever o circuito (perigoso — fusível não protege mais o cabo);
- usar cabo automotivo (GPT, TXL, SGT) em circuito de bateria de embarcação marítima;
- crimpar terminal com alicate genérico (terminal fica frouxo ou condutor fica fraturado);
- estanhar condutor antes de crimpar (estanho flui sob pressão e afrouxa a conexão ao longo do tempo);
- emendar por torção + fita isolante (wicking de água + corrosão garantidos);
- passar cabo de potência em paralelo com cabo de dados sem segregação.

## Relação com outros sistemas

- **[[Dimensionamento de Cabos DC — Cálculo Prático]]** — cálculo de bitola e queda de tensão.
- **[[Terminais Conectores e Emendas]]** — qualidade da terminação.
- **[[Barramento DC / Bus Bar / Distribuição DC]]** — origem e organização dos ramais.
- **[[Fusíveis DC — Proteção Contra Sobrecorrente]]** e **[[Disjuntores (DC) e (AC)]]** — proteção coordenada com o cabo.
- **[[NMEA 2000 / NMEA 0183 — Rede de Instrumentos]]** — diferenças entre cabeamento de potência e dados.
- **[[Chaves Gerais (DC)]]** e **[[Chaves Seletoras (AC)]]** — interface entre cabeamento e comando.

## Normas e referências

### Por família e jurisdição

| Família | Norma | Escopo |
| --- | --- | --- |
| **ABYC (EUA)** | E-11 §15, §16, §17 | condutores, instalação, proteção mecânica |
| ABYC | E-30 | sistemas de propulsão elétrica |
| ABYC | TE-4 | condutores de descida de para-raios |
| ABYC | S-32 | síntese para embarcações < 20 m |
| **USCG (EUA)** | 33 CFR 183.425–460 | dimensionamento e proteção |
| **UL (EUA)** | UL 1426 BC5W2 | cabo para embarcações (boat cable) |
| UL | UL 1309 | cabo para navios (marine shipboard) |
| UL | UL 83 / UL 44 | isolantes termoplásticos / termofixos |
| **SAE (EUA)** | SAE J378 | cabeamento de propulsão marítima |
| SAE | SAE J1127/J1128 | cabo de bateria / cabo primário |
| **NFPA (EUA)** | NFPA 70 art. 310/555 | ampacidade / marinas |
| **ISO (internacional)** | ISO 10133:2012 | sistemas DC em pequenas embarcações |
| ISO | ISO 13297:2020 | sistemas AC em pequenas embarcações |
| ISO | ISO 6722-1 / 19642 | cabo automotivo 60V/600V |
| ISO | ISO 8820 | coordenação fusível/cabo |
| **IEC (internacional)** | IEC 60228 | classes 1-6 de condutores |
| IEC | IEC 60287 | cálculo de ampacidade |
| IEC | IEC 60332-1/-3 | flame retardant |
| IEC | IEC 60754 / 61034 | halogen-free / low-smoke |
| IEC | IEC 60364-5-52 | instalação de sistemas de fiação |
| IEC | IEC 60092-350 a -376 | cabos para instalações elétricas em navios |
| **Classificadoras** | DNV-RU-SHIP Pt.4 Ch.8 | regras europeias para navios |
| Classificadoras | Lloyd's/BV/RINA/ABS | regras internacionais navais |
| **ABNT (Brasil)** | NBR 5410 | instalações de baixa tensão |
| ABNT | NBR NM 247-1/-3 | cabos isolados PVC 450/750 V |
| ABNT | NBR 7286/7287/7288 | cabos EPR/XLPE/PVC |
| ABNT | NBR 14039 | média tensão |
| **NORMAM (Brasil)** | NORMAM-05/DPC | embarcações de esporte e recreio |
| NORMAM | NORMAM-01/DPC | navegação marítima |

### Comparação prática entre jurisdições

- **EUA (ABYC + UL 1426 BC5W2)**: padrão "boat cable" — cobre estanhado + PVC náutico, tabelas prescritivas de ampacidade por AWG.
- **Internacional (ISO + IEC 60092)**: cabo classificado com ensaios de fogo (IEC 60332-3-22 categoria A), halogen-free (IEC 60754), low-smoke (IEC 61034); exigência em navios classificados.
- **Brasil (ABNT + NORMAM)**: NBR 5410 predial não cobre náutica; NORMAM-05 remete a ABYC/ISO para recreio e a SOLAS/IEC 60092 para comercial; falta norma ABNT específica náutica → uso de referência internacional é regra.
- **Classificadoras navais** (DNV, Lloyd's, BV, RINA, ABS): todas remetem a IEC 60092-series para cabo naval — classificação obrigatória em navio sob regra de classe.

## Glossário rápido

1. **Ampacidade** — corrente máxima contínua que um condutor suporta sem exceder o limite térmico do isolante.
2. **AWG (American Wire Gauge)** — sistema americano de bitolas; quanto menor o número, maior a seção.
3. **Bainha externa (sheath/jacket)** — camada externa de proteção mecânica do cabo.
4. **BC5W2** — classificação UL 1426 — Boat Cable, 5 A/mm² (aprox.), 2 camadas.
5. **Blindagem (shield)** — camada metálica para proteção contra EMI (malha trançada ou fita alumínio).
6. **Cabo de bateria (battery cable)** — cabo muito flexível e grosso entre banco e cargas críticas (partida, inversor).
7. **Cabo primário (primary cable)** — cabo de circuito de 12/24 V de baixa a média corrente.
8. **CAN bus** — rede de comunicação serial (NMEA 2000, SAE J1939); cabo blindado com terminação 120 Ω.
9. **Classe 1 a 6 (IEC 60228)** — classificação de flexibilidade: 1 rígido / 2 flexível / 5 muito flexível / 6 extra-flexível.
10. **Cobre estanhado (tinned copper)** — cobre com revestimento de estanho, padrão náutico.
11. **Comprimento elétrico** — soma do trajeto de ida + volta em DC; em AC monofásico, fase + neutro.
12. **Condutor** — o cobre (ou alumínio) que conduz corrente.
13. **Conduíte** — tubo/calha de proteção mecânica do cabo.
14. **Corrente contínua (continuous current)** — corrente mantida indefinidamente; base para dimensionamento.
15. **Crimpagem** — deformação controlada do terminal sobre o condutor por pressão mecânica.
16. **Derating** — redução de ampacidade por temperatura, agrupamento ou instalação.
17. **Diagrama unifilar (single-line diagram)** — representação simplificada com cada polo/fase em linha única.
18. **Drip loop** — alça no cabo antes do conector para escorrer água por gravidade.
19. **EMI (Electromagnetic Interference)** — interferência eletromagnética entre potência e sinal.
20. **EPR (Ethylene Propylene Rubber)** — borracha termofixa, excelente em ambiente marinho.
21. **ETFE / FEP / PTFE** — fluoropolímeros para alta temperatura (150-260 °C).
22. **Feixe (bundle)** — agrupamento de cabos correndo juntos — reduz ampacidade individual.
23. **Flame retardant (FR)** — cabo com aditivo que retarda propagação de chama (IEC 60332).
24. **Halogen-free (HF / LS0H)** — sem flúor/cloro/bromo — baixa toxicidade em incêndio (IEC 60754).
25. **Heat-shrink** — tubo termorretrátil para selar/proteger terminação.
26. **IEC 60092-series** — normas internacionais para instalações elétricas em navios.
27. **Isolação** — camada dielétrica ao redor do condutor (PVC, EPR, XLPE, silicone, fluoropolímero).
28. **Loom (split-loom)** — conduíte espiral flexível.
29. **Low-smoke (LS)** — baixa densidade de fumaça em incêndio (IEC 61034).
30. **mm² (secção nominal)** — área do condutor em milímetros quadrados.
31. **NMEA 2000 / N2K** — rede náutica baseada em CAN, backbone micro/mini, terminação 120 Ω.
32. **PE (Protective Earth)** — condutor de proteção em AC (verde/amarelo).
33. **PVC** — cloreto de polivinila — isolante barato mas gera gás halogênico em incêndio.
34. **Pull test** — teste de tração em terminação após crimpagem.
35. **Queda de tensão (voltage drop)** — diferença de tensão entre origem e carga sob corrente.
36. **Raio de curvatura** — menor raio que o cabo pode dobrar sem danificar.
37. **Resistividade (ρ)** — resistência elétrica por comprimento unitário; cobre ~0,0175 Ω·mm²/m.
38. **Service loop** — folga de cabo reservada para manutenção/reposicionamento.
39. **Shore power** — alimentação de terra (cais) — 120 V ou 240 V, 50 ou 60 Hz.
40. **Simultaneidade (diversity factor)** — fração das cargas que operam ao mesmo tempo.
41. **Suporte (support spacing)** — distância entre fixações do cabo.
42. **Terminal (lug)** — peça de conexão crimpada na ponta do cabo.
43. **TPE/TPU** — elastômeros termoplásticos, bainhas flexíveis modernas.
44. **Trefilação** — processo de fabricação do fio por estiragem.
45. **UL 1426** — norma americana para boat cable.
46. **UV-resistant** — aditivo na bainha que resiste à radiação ultravioleta.
47. **Voltage drop (ΔV)** — ver queda de tensão.
48. **Wicking** — capilaridade que leva água pelo condutor ao longo do cabo.
49. **XLPE** — polietileno reticulado — isolante termofixo de alta performance.
50. **Zona de flexão** — trecho de cabo sujeito a movimento cíclico — exige classe 5/6.

## FAQ

**Cabo automotivo e cabo náutico são a mesma coisa?**

Não. Podem até se parecer visualmente, mas ambiente, materiais, isolamento e expectativa de durabilidade são diferentes. Cabo automotivo (GPT, TXL, SGT) usa cobre nu + PVC básico; cabo náutico (BC5W2, IEC 60092) usa cobre estanhado + bainha reforçada para névoa salina, óleo e UV.

**A cor do cabo sempre identifica a função?**

Ajuda, mas não garante. Em retrofit ou barco sem histórico claro, valide com medição e documentação. Os padrões ABYC, ISO e NBR divergem em alguns pontos.

**Se a corrente está baixa, qualquer cabo serve?**

Não. Queda de tensão, ambiente, flexibilidade e método de instalação continuam importando. Um circuito de 2 A em 12 V com 20 m de ida e volta em AWG 18 já cai > 5% da tensão.

**Posso usar cabo BC5W2 em navio SOLAS classificado?**

Em geral não. Navio classificado exige cabo IEC 60092-353 ou equivalente com certificação de classe (DNV, Lloyd's, BV). BC5W2 é padrão americano para embarcação de recreio e pequeno comercial.

**Posso estanhar o condutor antes de crimpar?**

Não. O estanho é maleável e flui sob a pressão da crimpagem ao longo do tempo, afrouxando a conexão. Crimpe em condutor nu (mas já estanhado de fábrica, se for cabo marinho) com alicate certificado.

**Qual a diferença entre classe 5 e classe 6 de flexibilidade?**

Classe 5 (IEC 60228) tem filamentos de 0,4-0,6 mm; classe 6 tem filamentos ≤ 0,3 mm — muito mais flexível, indicado para zonas de flexão cíclica (motor, thruster, cabos de partida).

## Visual didático

**Cautela:** Ampacidade, queda de tensão e classe de cabo dependem de projeto, ambiente e fabricante. Confirme com datasheet e normas aplicáveis à embarcação.

## Integração com outras notas

- [[Barramento DC / Bus Bar / Distribuição DC]]
- [[Terminais Conectores e Emendas]]
- [[Dimensionamento de Cabos DC — Cálculo Prático]]
- [[Fusíveis DC — Proteção Contra Sobrecorrente]]
- [[Disjuntores (DC) e (AC)]]
- [[NMEA 2000 / NMEA 0183 — Rede de Instrumentos]]
- [[Chaves Gerais (DC)]]
- [[Chaves Seletoras (AC)]]

## Perguntas que esta nota responde

- O que caracteriza um cabeamento náutico profissional?
- Como escolher e instalar cabos em embarcações com critério técnico?
- Quais são os erros mais comuns de cabeamento em ambiente marinho?
- Qual a diferença entre UL 1426 BC5W2, IEC 60092 e cabo automotivo?
- Quando usar cabo classe 5 ou classe 6 de flexibilidade?
