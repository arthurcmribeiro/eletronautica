---
title: "Eletrólise"
note_type: "technical-note"
domain: "80_Seguranca_e_Corrosao"
source_file: "ELETRÓLISE bb819734f7fb8373bf6e01246ab6177a.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "34"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
  - "internacional"
normas_citadas:
  - "ABYC E-2 (2020) — Cathodic Protection (bonding + ânodos sacrificiais)"
  - "ABYC E-11 (2023) — AC & DC Electrical Systems (shore power + ELCI + isolador galvânico)"
  - "ABYC A-22 — Marinas and Boatyards"
  - "ABYC TE-13 — Technical note corrosion control"
  - "ISO 13297:2020 — Small craft — Electrical systems AC & DC"
  - "ISO 10133:2012 — retirada, sucedida por 13297"
  - "ISO 17339:2009 — Sacrificial anode materials and testing methods"
  - "NACE SP0176:2007 — Corrosion Control Offshore"
  - "NACE TM0497:2018 — Measurement Techniques for Cathodic Protection"
  - "NACE SP0169:2013 — Control of External Corrosion on Underground or Submerged Metallic Piping Systems"
  - "NACE Basic Corrosion Course (CP1/CP2/CP3/CP4)"
  - "ASTM G1 — Preparing, Cleaning, and Evaluating Corrosion Test Specimens"
  - "ASTM G15 — Standard Terminology Relating to Corrosion (terminologia padrão)"
  - "ASTM G46 — Examination and Evaluation of Pitting Corrosion"
  - "ASTM G71 — Galvanic Corrosion (teste galvânico)"
  - "ASTM G82 — Development and Use of a Galvanic Series"
  - "IEC 60092-350 — Electrical installations in ships — General construction"
  - "IEC 60092-401 — Installation and test of completed installation"
  - "IEEE 45 — IEEE Recommended Practice for Electrical Installations on Shipboard"
  - "IEEE 80 — Guide for Safety in AC Substation Grounding (referência para ELCI)"
  - "NFPA 303 — Fire Protection Standard for Marinas and Boatyards"
  - "NEC Art. 555 — Marinas, Boatyards, Boat Basins (USA)"
  - "USCG 33 CFR Part 183 — Boats and Associated Equipment"
  - "NORMAM-211/DPC — Esporte e recreio"
  - "NORMAM-201/204/DPC — Comercial / SMM"
  - "NBR 5410:2004 + emendas — Instalações elétricas de baixa tensão"
  - "CE-RCD Directive 2013/53/EU — Recreational Craft Directive"
review_level: "engineering-curated"
aliases:
  - "ELETRÓLISE"
  - "Corrosão eletrolítica"
  - "Corrosão eletroquímica"
seo_title: "Eletrólise em embarcações: termo correto, mecanismos e diagnóstico"
seo_description: "Nota técnica para separar eletrólise, corrosão galvânica e correntes parasitas no contexto náutico, com foco em terminologia correta, mecanismos e decisão de diagnóstico."
seo_keywords:
  - "eletrólise embarcação"
  - "corrosão eletrolítica náutica"
  - "galvânica versus corrente parasita"
  - "diagnóstico corrosão barco"
geo_queries:
  - "O que é chamado de eletrólise em embarcações e o que o termo realmente significa?"
  - "Como diferenciar corrosão galvânica de corrosão por corrente parasita?"
related_notes:
  - "Anôdo"
  - "Bonding — Sistema de Interligação de Massas"
  - "Correntes Parasitas — Stray Currents"
  - "Isolador Galvânico - Transformador de Isolamento"
  - "CAIS (Pier) (AC)"
  - "Aterramento"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
---

# Eletrólise

> [!abstract] Resumo técnico
> Em linguagem de oficina, "eletrólise" costuma virar sinônimo de qualquer corrosão elétrica em embarcação. Tecnicamente isso é fraco. Esta nota existe para organizar o vocabulário e evitar diagnóstico errado: uma coisa é corrosão galvânica, outra é corrosão por corrente parasita, e outra ainda é risco de fuga AC em ambiente aquático.

> [!tip] Regra de decisão em 30 segundos
> 1. **"Eletrólise" é termo guarda-chuva impreciso** — separar em três famílias: corrosão galvânica (natural, entre metais diferentes), corrosão por corrente parasita (stray current, por fuga), ESD/ELCI fault (risco humano, não só material).
> 2. **Corrosão galvânica: lenta, distribuída, previsível** — metais diferentes + eletrólito + contato elétrico = par galvânico (série de Nernst / ASTM G82); ânodos controlam. Taxa < 1 mm/ano típico.
> 3. **Corrosão por corrente parasita: rápida, localizada, sinal de falha elétrica** — fuga DC em bonding + shore power + vizinho de marina; consumo acelerado de ânodo em semanas; sinal de ATIVA INVESTIGAÇÃO, não de troca de ânodo.
> 4. **ESD / ELCI fault: risco à vida, não ao material** — fuga AC > 30 mA em água = choque fatal em nadador próximo; detectada por ELCI/RCD (ABYC E-11); nunca chamar "eletrólise".
> 5. **Eletrólito = água do mar** — condutividade ~5 S/m (salgada), 0,5 S/m (salobra), 0,05 S/m (doce); salgada é o eletrólito mais agressivo.
> 6. **Pitting rápido e localizado = corrente parasita** — corrosão uniforme e lenta = galvânica; distinguir pelo padrão de ataque (ASTM G46).
> 7. **Eletrodo de referência Ag/AgCl é o voltímetro da corrosão** — potencial absoluto em solução aquosa; sem ele, palpite (NACE TM0497).
> 8. **Isolador galvânico (diodo anti-paralelo) resolve galvânica via shore** — mas NÃO resolve fuga DC interna nem fuga AC; diagnóstico primeiro.
> 9. **Transformador de isolação elimina todas as três vias de shore power** — isola galvanicamente AC do cais; investimento maior mas mitigação completa (ABYC E-11 recomenda > 50 A shore).

> [!danger] Quando chamar um especialista (engenheiro corrosionista NACE / surveyor elétrico)
> 1. **Consumo de ânodo em < 1 mês** — corrente parasita severa, falha AC/DC ou marina com problema coletivo; medição com eletrodo de referência + current survey; NÃO zarpar até diagnosticar (risco de perda de hélice/eixo).
> 2. **Pitting acelerado em alumínio, aço ou bronze submerso** — sinal de corrente parasita ativa; engenharia NACE com mapeamento setorial + isolamento de loops.
> 3. **Choque em água próximo à embarcação (ESD — Electric Shock Drowning)** — emergência: desligar shore power + gerador + inverter; sem acesso à água até diagnóstico; ABYC E-11 + NFPA 303 + NEC 555; laudo obrigatório + ELCI retrofit.
> 4. **Embarcação vizinha com problema conhecido** — marina pode ser exposição coletiva; medir com eletrodo de referência próprio; considerar mudança ou pressão legal.
> 5. **Corrosão em bronze manganês (hélice, válvulas) — dezincification** — perda seletiva de zinco do bronze; substituir por Nibral (bronze-níquel-alumínio) ou Cu-Ni 70/30; projeto de substituição.
> 6. **Arqueologia elétrica em embarcação usada — histórico não conhecido** — levantamento completo: bonding, shore, AC leakage, DC leakage, bilge, motor; surveyor com instrumento calibrado emite relatório baseline.
> 7. **Corrosão por correntes telúricas ou geotermicamente induzidas** — raro mas existe em marinas próximas a subestações/linhas de transmissão; mitigação por aterramento perimetral.
> 8. **Dano a infraestrutura do cais (estacas, trilhos, dutos)** — corrente parasita da embarcação pode atacar estrutura do cais; responsabilidade civil; NACE SP0169 + inspeção cooperativa marina+proprietário.
> 9. **Perícia pós-sinistro com causa elétrica-corrosiva** — preservar evidências (ânodos, hélice, eixo, cabos); laudo IBAPE/Abracem + NACE-certified; base para seguradora + responsabilização.

## Por que esta nota é necessária

Quando o termo é usado de forma solta, o resultado costuma ser ruim:

- troca-se anodo sem resolver a causa;
- culpa-se o metal errado;
- aplica-se solução de galvanic isolator onde o problema é interno;
- ignora-se um defeito de segurança porque "é só eletrólise".

Esta nota funciona como nota de síntese conceitual. O diagnóstico operacional detalhado está em [[Correntes Parasitas — Stray Currents]].

## O que o mercado costuma chamar de eletrólise

Na prática brasileira, o termo costuma englobar:

- corrosão galvânica;
- corrosão por corrente parasita;
- dano associado a shore power;
- às vezes até choque elétrico em água.

Isso é útil para conversa informal, mas ruim para engenharia.

## Distinção técnica mínima

### Corrosão galvânica

É o ataque eletroquímico natural entre metais com potenciais diferentes, eletricamente conectados em um eletrólito. Não precisa de fonte elétrica externa.

Mitigações típicas:

- [[Anôdo]];
- seleção de materiais;
- isolamento entre metais;
- arquitetura correta de [[Bonding — Sistema de Interligação de Massas]].

### Corrosão por corrente parasita

É o ataque por corrente elétrica indevida saindo de um metal para a água ou estrutura. É muito mais agressiva e quase sempre aponta problema elétrico real.

Mitigações típicas:

- localizar e eliminar a fuga;
- revisar aterramento, bonding e negativo DC;
- revisar shore power;
- usar [[Isolador Galvânico - Transformador de Isolamento]] quando aplicável;
- corrigir a instalação, não apenas trocar anodo.

### Vazamento AC para água

É um tema de segurança humana crítica. Pode coexistir com corrosão e com defeitos de instalação, mas não deve ser resumido apenas como "eletrólise". O risco principal imediato é choque elétrico em ambiente aquático.

## Como o termo deve ser usado nesta base

Para manter rigor técnico, esta vault adota a seguinte lógica:

- [[Eletrólise]] = nota conceitual e organizadora;
- [[Correntes Parasitas — Stray Currents]] = mecanismo destrutivo por fuga/corrente indevida;
- [[Anôdo]] = proteção catódica e leitura de consumo;
- [[Bonding — Sistema de Interligação de Massas]] = arquitetura de equipotencialização;
- [[Isolador Galvânico - Transformador de Isolamento]] = mitigação associada ao shore power.

## Sinais que exigem separação de hipóteses

Sempre diferenciar:

- dano lento e coerente com par galvânico;
- consumo anormal de anodos;
- pitting rápido e localizado;
- mudança de comportamento conforme marina ou conexão AC;
- coincidência entre corrosão e defeitos elétricos aparentes.

Se tudo é tratado como uma só doença, o reparo costuma ser superficial.

## Fluxo mental de diagnóstico

Perguntas úteis:

1. Existe fonte externa de energia conectada?
2. O dano acelera em determinadas marinas ou períodos?
3. O padrão de ataque é lento e distribuído ou rápido e localizado?
4. O anodo está consumindo compativelmente, pouco demais ou rápido demais?
5. Há mudança ao isolar shore power e circuitos internos?

Isso ajuda a separar fenômeno eletroquímico natural de defeito elétrico ativo.

## Boas práticas editoriais e técnicas

Ao escrever ou ensinar o tema, evitar frases como:

- "foi eletrólise" sem explicar o mecanismo;
- "o zinco resolve";
- "a marina corrói o barco" sem medir;
- "é normal o anodo acabar rápido".

A formulação melhor é sempre:

- qual foi o mecanismo provável;
- qual evidência aponta para ele;
- qual teste faltou;
- qual solução realmente atua naquela causa.

## Integração com outras notas

- [[Anôdo]]
- [[Bonding — Sistema de Interligação de Massas]]
- [[Correntes Parasitas — Stray Currents]]
- [[Isolador Galvânico - Transformador de Isolamento]]
- [[CAIS (Pier) (AC)]]
- [[Aterramento]]

## Normas aplicáveis (organizadas por família)

O tratamento correto de "eletrólise" cruza três áreas normativas: **sistema elétrico da embarcação** (ABYC, ISO, IEC), **engenharia de corrosão** (NACE, ASTM, DNV) e **segurança de shore power / marinas** (NFPA, NEC, NORMAM). Falhar em qualquer uma delas produz diagnóstico incompleto.

### ABYC (American Boat & Yacht Council) — referência técnica primária em recreio

- **ABYC E-2 (2020) — Cathodic Protection** — dimensionamento de ânodos, bonding de proteção, potenciais de referência. Base para qualquer projeto de proteção catódica em pequena embarcação.
- **ABYC E-11 (2023) — AC & DC Electrical Systems** — cobre ELCI (Equipment Leakage Circuit Interrupter), isolador galvânico, transformador de isolação, grounding de shore power. Conecta diretamente a segurança AC (ESD) à prevenção de correntes parasitas.
- **ABYC A-22 — Marinas and Boatyards** — exposição coletiva: o barco ancorado em marina está sujeito a problemas de outros barcos e da rede do cais.
- **ABYC TE-13 — Technical note on corrosion control** — nota técnica com estudo de casos e diagnóstico diferencial.

### ISO (embarcações de pequeno porte — interoperabilidade internacional)

- **ISO 13297:2020 — Small craft — Electrical systems — AC & DC** — norma consolidada (unifica 13297-1/2 antigas).
- **ISO 10133:2012** — norma histórica de DC em pequena embarcação; **retirada e sucedida por ISO 13297:2020**. Citar apenas se o projeto é anterior à atualização.
- **ISO 17339:2009 — Sacrificial anode materials and testing methods** — especificação de ligas de zinco, alumínio e magnésio para proteção catódica marinha.

### NACE / AMPP (engenharia de corrosão — aplicação aplicada)

- **NACE SP0176:2007 — Corrosion Control of Steel Fixed Offshore Structures** — referência para proteção catódica em estruturas submersas; aplicável quando o barco fica em fundeio permanente ou na análise da estrutura do cais.
- **NACE TM0497:2018 — Measurement Techniques Related to Criteria for Cathodic Protection** — protocolo de medição com eletrodo de referência (Ag/AgCl, Cu/CuSO₄, Zn). Sem isso, diagnóstico de corrosão é chute.
- **NACE SP0169:2013 — External Corrosion on Underground or Submerged Metallic Piping** — aplicável quando a embarcação causa dano a tubulações ou estacas metálicas do cais.
- **NACE Basic Corrosion Course + CP1/CP2/CP3/CP4** — cadeia de certificação de engenheiros corrosionistas; CP3+ exigido para laudo formal.

### ASTM (testes laboratoriais e terminologia)

- **ASTM G1 — Preparing, Cleaning, and Evaluating Corrosion Test Specimens** — protocolo padrão para análise de ânodos consumidos ou peças corroídas.
- **ASTM G15 — Standard Terminology Relating to Corrosion** — vocabulário oficial (pitting, crevice, galvanic, erosion-corrosion, etc.). Evita o termo "eletrólise" solto.
- **ASTM G46 — Standard Guide for Examination and Evaluation of Pitting Corrosion** — classifica o pitting em 6 morfologias (narrow-deep, elliptical, wide-shallow, subsurface, undercutting, horizontal/vertical).
- **ASTM G71 — Conducting and Evaluating Galvanic Corrosion Tests in Electrolytes** — teste laboratorial para confirmar par galvânico.
- **ASTM G82 — Development and Use of a Galvanic Series for Predicting Galvanic Corrosion Performance** — a tabela de série galvânica em água do mar é a primeira ferramenta de decisão de material.

### IEC (embarcação comercial e navios)

- **IEC 60092-350 — Electrical installations in ships — General construction and test methods of power, control and instrumentation cables for shipboard and offshore applications** — referência para cabos em embarcação classificada.
- **IEC 60092-401 — Installation and test of completed installation** — comissionamento elétrico de navio/embarcação classificada, incluindo isolação e continuidade de bonding.

### IEEE (referência técnica, especialmente para análise de falha AC)

- **IEEE 45 — Recommended Practice for Electrical Installations on Shipboard** — padrão americano para instalação elétrica em embarcação comercial; conecta-se a IEC 60092.
- **IEEE 80 — Guide for Safety in AC Substation Grounding** — não é norma naval, mas é a referência técnica para dimensionar ELCI e tensões de passo/toque — útil para entender por que 30 mA é o limiar de ESD.

### Infraestrutura de marina e segurança de shore power (USA)

- **NFPA 303 — Fire Protection Standard for Marinas and Boatyards** — exigências gerais de marina (distâncias, aterramento, sinalização, ELCI).
- **NEC Art. 555 — Marinas, Boatyards, Boat Basins, Commercial Docks, Boat Hoists** — código elétrico USA para instalação do cais; define ELCI obrigatório em receptáculos de shore power (2017+).
- **USCG 33 CFR Part 183 — Boats and Associated Equipment** — regulamento federal USA; complementa ABYC.

### Brasil

- **NORMAM-211/DPC — Esporte e recreio** — regulamento da Diretoria de Portos e Costas para embarcações de esporte e recreio. Não entra em detalhe de corrosão, mas exige manutenção geral e inspeção.
- **NORMAM-201/204/DPC — Comercial / SMM** — embarcações classificadas via Sociedade Classificadora (DNV, BV, LR, RINA, ABS); exige documentação de proteção catódica formal.
- **NBR 5410:2004 + emendas — Instalações elétricas de baixa tensão** — referência para lado AC (shore power interno); não cobre corrosão, mas define segurança elétrica.

### Europa

- **CE-RCD Directive 2013/53/EU — Recreational Craft Directive** — para embarcação com certificação CE, exige conformidade a ISO 13297 + ISO 10240 (manuais) + proteção AC conforme. Vendedores brasileiros que exportam / compradores que importam caem aqui.

### Como usar este conjunto normativo na prática

| Situação | Norma-chave |
|---|---|
| Dimensionar ânodos em projeto novo | ABYC E-2, ISO 17339, NACE SP0176 |
| Medir potencial de proteção | NACE TM0497 + eletrodo Ag/AgCl |
| Diagnóstico de pitting em casco | ASTM G46 + G82 |
| Certificado de proteção catódica (comercial) | DNV-RP-B401 + classificadora |
| Retrofit de shore power com ELCI | ABYC E-11 + NEC 555 + NFPA 303 |
| Perícia de ESD em marina | NFPA 303 + ABYC A-22 + ELCI mandatory |
| Relatório de corrosão formal | NACE CP3+ + ASTM G1/G15 |

## Glossário rápido

### Terminologia de corrosão (ASTM G15 + NACE)

- **Corrosão galvânica** — ataque eletroquímico natural entre dois metais com potenciais diferentes, eletricamente conectados, imersos em eletrólito. Não requer fonte elétrica externa. Lenta, distribuída, previsível pela série galvânica.
- **Corrosão por corrente parasita (stray current corrosion)** — ataque acelerado causado por corrente elétrica indevida saindo de um metal via eletrólito. Requer diagnóstico ativo: fuga DC no bonding, shore power mal aterrado, vizinho de marina.
- **Pitting corrosion** — corrosão localizada que produz cavidades profundas; sinal típico de corrente parasita ou passivação rompida. Classificada em 6 morfologias por ASTM G46.
- **Crevice corrosion** — corrosão em fresta (sob junta, sob flange, sob porca); oxigênio restrito aprisiona eletrólito e gera ataque local; tratada por design (evitar fresta).
- **Dezincification** — perda seletiva de zinco em ligas de bronze-manganês (latão), deixando esponja porosa de cobre. Típico em hélices de barco antigas; solução = substituir por Nibral.
- **Erosion-corrosion** — combinação de ataque químico + desgaste mecânico por fluxo; comum em hélices, bombas, tubulações de refrigeração de motor.
- **Passivação** — formação de filme de óxido estável que protege o metal; base do comportamento de inox 316; se rompida sem re-passivar, dá pitting.
- **Potencial de corrosão** — tensão do metal vs eletrodo de referência (Ag/AgCl em água do mar); base do diagnóstico.
- **Potencial de proteção** — tensão mais negativa que -800 mV vs Ag/AgCl (aço) indica proteção catódica adequada.
- **Série galvânica (ASTM G82)** — ordenação empírica de metais em água do mar por potencial; prevê qual metal corrói em par.
- **Série de Nernst** — derivação termodinâmica da série galvânica; base teórica.
- **Eletrólito** — meio condutor iônico (água do mar ~5 S/m, água salobra ~0,5 S/m, água doce ~0,05 S/m). Condutividade define taxa.
- **Eletrodo de referência** — elemento que fornece tensão conhecida para medir potencial do metal; Ag/AgCl é o padrão marinho; Cu/CuSO₄ é de solo; Zn puro é o popular "fisherman's" (menos preciso).

### Proteção catódica e ânodos (ABYC E-2 + ISO 17339)

- **Ânodo sacrificial** — metal mais ativo (Zn, Al, Mg) que corrói no lugar do casco/hélice; consumido em semanas a meses.
- **Zn (zinco) — MIL-A-18001 H** — liga padrão para água salgada; não funciona em água doce (passivação).
- **Al-In (alumínio-índio, tipo "Navalloy", "MG Duff Alloy")** — liga de alumínio ativada por índio; opção moderna; ASTM B418 Tipo I; serve tanto em salgada quanto salobra.
- **Mg (magnésio)** — para água doce; nunca em salgada (corrosão explosiva).
- **Corrente de proteção** — densidade de corrente necessária para polarizar o metal ao potencial de proteção; tipicamente 20–50 mA/m² para casco aço pintado em água do mar.
- **ICCP (Impressed Current Cathodic Protection)** — proteção catódica por corrente impressa via fonte externa + ânodos de MMO (mixed metal oxide); navios grandes e plataformas; não é padrão em recreio.
- **MMO (mixed metal oxide)** — ânodo de titânio revestido com óxido misto (Pt, Ru, Ir); usado em ICCP; não é consumível como Zn/Al/Mg.
- **Bonding** — sistema de conexão equipotencial entre massas metálicas; base para proteção catódica funcionar (sem bonding, ânodo não "vê" o metal a proteger).
- **Bonding continuity test** — medição de resistência entre pontos do sistema de bonding com miliohmímetro; < 1 Ω aceitável, ideal < 100 mΩ.

### Shore power, ELCI e ESD (ABYC E-11 + NEC 555 + NFPA 303)

- **Shore power** — alimentação AC do cais para o barco; via cabo 30A/50A/100A.
- **Shore power ground** — terra do cais que entra na embarcação; principal via de corrente galvânica entre dois barcos da marina.
- **Isolador galvânico (galvanic isolator)** — diodos anti-paralelos no fio terra shore; bloqueia tensão DC < 1,4 V (par galvânico típico), mas passa fuga AC; mitigação parcial.
- **Transformador de isolação (isolation transformer)** — transformador 1:1 que isola galvanicamente AC do cais; elimina par galvânico e fuga; mitigação completa; ABYC E-11 recomenda > 50 A shore.
- **ELCI (Equipment Leakage Circuit Interrupter)** — disjuntor diferencial marinho; dispara com fuga > 30 mA AC; protege nadador de ESD; obrigatório NEC 2017+ em cais.
- **GFCI (Ground Fault Circuit Interrupter)** — disjuntor diferencial 5 mA para tomadas; proteção de usuário em tomadas molhadas; não é o mesmo que ELCI.
- **RCD (Residual Current Device)** — nomenclatura europeia (ISO/IEC) para disjuntor diferencial; equivalente a GFCI/ELCI dependendo do limiar.
- **ESD (Electric Shock Drowning)** — choque elétrico em água próximo a embarcação ou cais; causa morte por paralisia muscular + afogamento; fuga AC > 30 mA é suficiente em água doce.

### Materiais e geometria submersa

- **Hélice Nibral (nickel-aluminum-bronze)** — liga moderna para hélice; resistente a dezincification; substitui o bronze-manganês.
- **Cu-Ni 70/30** — liga de cobre-níquel para tubulação de refrigeração de motor; resistente a biofouling e corrosão; caro.
- **SS 316** — inox austenítico; resistente à corrosão marinha se passivado e exposto a oxigênio; falha em crevice.
- **SS 17-4 PH** — inox precipitation-hardened; alta resistência mecânica; usado em eixos.
- **Monel (400/K-500)** — liga Ni-Cu; excelente em água do mar; caro; usado em parafusos submersos críticos.
- **Zinc collar (colar de zinco de eixo)** — ânodo cilíndrico instalado no eixo propulsor entre redutor e hélice; protege eixo + hélice.
- **Trim tab anode** — ânodo pequeno instalado nas trim tabs (popa); protege alumínio das trim tabs + estrutura próxima.

### Instrumentação de diagnóstico

- **Eletrodo Ag/AgCl de prata-cloreto de prata** — padrão de medição em água do mar; voltímetro lê potencial vs Ag/AgCl.
- **Impedance survey** — técnica de medir tensão/corrente em múltiplos pontos do casco; mapeia fugas.
- **Current survey / corrosion survey** — inspeção completa com eletrodo de referência em múltiplas posições ao redor do casco; emite relatório com mapa de potencial.
- **Reference cell** — mesmo que eletrodo de referência.
- **Polarization curve** — gráfico tensão × corrente para diagnosticar comportamento eletroquímico; usado por laboratório NACE.

### Ambientes especiais

- **Marina galvânica (galvanic marina)** — marina onde o shore power ground comum entre barcos cria par galvânico entre embarcações de materiais diferentes; isolador galvânico / transformador isolação mitiga.
- **Correntes telúricas** — correntes DC induzidas geofisicamente (sistemas de transmissão HVDC, subestações, trilhos ferroviários); raras mas reais em marinas próximas.
- **Ground loop** — laço de aterramento entre dois pontos com potenciais diferentes; caminho para corrente parasita.
- **Equipotencial bonding** — objetivo de manter todas as massas no mesmo potencial; evita correntes de dispersão.

### Padrões e classificações

- **DNV-RP-B401 — Cathodic Protection Design** — norma DNV para projeto formal de proteção catódica (embarcações comerciais, estruturas offshore).
- **CE-RCD** — Recreational Craft Directive (EU 2013/53); requisito para vender em mercado europeu.
- **NORMAM-211** — regulamento brasileiro de esporte e recreio (DPC/Marinha).
- **NORMAM-201/204** — regulamento brasileiro de embarcação comercial classificada.
- **ABYC E-2** — padrão técnico americano de proteção catódica em recreio.
- **IEEE 45** — padrão americano para instalação elétrica em embarcação comercial.
- **IEC 60092-350** — padrão internacional para cabos em embarcação comercial.

## Perguntas que esta nota responde

- O que a maioria das pessoas chama de eletrólise em embarcações?
- Como esta base diferencia corrosão galvânica, corrente parasita e risco AC?
- Por que usar o termo certo melhora o diagnóstico e evita reparo errado?
