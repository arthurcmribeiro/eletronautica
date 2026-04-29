---
title: "Anôdo"
note_type: "technical-note"
domain: "80_Seguranca_e_Corrosao"
source_file: "ANÔDO 8e019734f7fb829abd3e01f8fcef8de0.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "33"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
  - "internacional"
normas_citadas:
  - "ABYC E-2 (2020) — Cathodic Protection (bonding + ânodos sacrificiais + eletrodo de referência)"
  - "ABYC E-11 (2023) — AC & DC Electrical Systems (interface bonding + shore power)"
  - "ABYC A-22 — Marinas and Boatyards (referência cruzada ambiente)"
  - "ISO 13297:2020 — Small craft — Electrical systems AC & DC"
  - "ISO 10133:2012 — retirada, sucedida por 13297"
  - "ISO 17339:2009 — Sacrificial anode materials and testing methods"
  - "ISO 15589-1:2015 — Cathodic protection of pipeline transportation systems — On-land pipelines"
  - "ISO 15589-2:2012 — Cathodic protection — Offshore pipelines"
  - "IEC 60092-350 — Electrical installations in ships — General construction"
  - "IEC 60092-301 — Equipment — Generators and motors (corrosão em motores)"
  - "NACE SP0176:2007 — Corrosion Control of Submerged Areas of Permanently Installed Steel Offshore Structures"
  - "NACE TM0497:2018 — Measurement Techniques Related to Criteria for Cathodic Protection"
  - "NACE SP0387:2012 — Metallurgical and Inspection Requirements for Offshore Steel Structures"
  - "ASTM B418-16 — Standard Specification for Cast and Wrought Galvanic Zinc Anodes"
  - "ASTM G97-97(2018) — Laboratory Evaluation of Magnesium Sacrificial Anode Test Specimens"
  - "ASTM F1182-07 — Standard Specification for Anodes, Sacrificial Zinc Alloy (US Navy)"
  - "MIL-A-18001K — Zinc anodes (US military — padrão histórico)"
  - "DNV-RP-B401 — Cathodic Protection Design (offshore classificadora)"
  - "Lloyd's Register Rules Pt 5 Ch 21 — Cathodic Protection"
  - "NORMAM-211/DPC — Esporte e recreio"
  - "NORMAM-201/204/DPC — Comercial / SMM"
  - "NBR 5410:2004 + emendas — Instalações elétricas de baixa tensão"
  - "NBR ISO 12696:2016 — Proteção catódica de aço em concreto (referência cruzada)"
  - "CE-RCD Directive 2013/53/EU — Recreational Craft Directive"
source_urls:
  - "https://webstore.ansi.org/standards/abyc/abyc2025"
  - "https://www.ampp.org/technical-research/what-is-corrosion/cathodic-protection-for-corrosion-control"
  - "https://store.astm.org/standards/b418"
  - "https://store.astm.org/Standards/G82.htm"
review_level: "engineering-curated"
aliases:
  - "ANÔDO"
  - "Ânodo"
  - "Ânodo sacrificial"
  - "Anodo de proteção catódica"
seo_title: "Ânodo sacrificial em embarcações: material, instalação e diagnóstico"
seo_description: "Guia técnico sobre ânodos sacrificiais em embarcações: escolha por eletrólito, contato elétrico, inspeção, leitura de consumo e relação com corrosão galvânica e correntes parasitas."
seo_keywords:
  - "ânodo sacrificial embarcação"
  - "zinco alumínio magnésio barco"
  - "proteção catódica náutica"
  - "consumo de anodo diagnóstico"
geo_queries:
  - "Como escolher o ânodo certo para água salgada, salobra ou doce?"
  - "Como saber se o ânodo está realmente protegendo a embarcação?"
related_notes:
  - "Bonding — Sistema de Interligação de Massas"
  - "Boiler"
  - "Correntes Parasitas — Stray Currents"
  - "Eletrólise"
  - "Tipos de Embarcação"
  - "Aterramento"
  - "Isolador Galvânico - Transformador de Isolamento"
---

# Anôdo

> [!abstract] Resumo técnico
> Ânodo sacrificial é o elemento de proteção catódica que se consome para preservar metais mais nobres ou estruturalmente importantes da embarcação. Ele só funciona bem quando a liga é correta para o eletrólito, o contato elétrico é efetivo e a arquitetura de bonding e shore power não está levando corrente indevida ao sistema.

> [!tip] Regra de decisão em 30 segundos
> 1. **Liga por eletrólito, não "zinco universal"** — Zn (salgada), Al (salobra, eficiência mais alta que zinco em salinidade variável), Mg (doce apenas; Mg em salgada consome em dias e superprotege causando descolagem de tinta).
> 2. **Contato elétrico limpo = condição necessária** — superfície desnuda + fixação metal-metal + torque correto; pintar o ânodo ou montar sobre primer = ânodo decorativo sem função (ABYC E-2).
> 3. **Ânodo é sensor + atuador** — consumo é dado diagnóstico; substituir sem entender padrão = perder o diagnóstico (consumo baixo = desprotegido, alto = corrente parasita, irregular = bonding descontínuo).
> 4. **Potencial de proteção com eletrodo de referência** — Ag/AgCl em salgada: -0,80 a -1,05 V vs Ag/AgCl (mV-scale readings); Zn reference: +0,25 V vs Zn; sem medição = palpite.
> 5. **Bonding primeiro, ânodo depois** — ABYC E-2 exige todas as massas metálicas submersas interligadas; ânodo em elemento isolado = só protege aquele elemento; nunca protege o conjunto.
> 6. **Ânodos internos tão críticos quanto externos** — trocador de calor, bloco motor, aquecedor, tanque aço; manutenção frequentemente ignora; rotineiramente inspecionados no serviço anual do motor.
> 7. **Substituir em 50% consumo, nunca 0%** — ânodo com > 50% consumido perde área eficaz e superfície de contato interna; manutenção ABYC recomenda troca preventiva.
> 8. **Isolador galvânico ou transformador de isolação em shore power** — sem eles, a marina toda "empresta" ânodo para sua embarcação; consumo 3-5× acelerado (ABYC E-11).
> 9. **Registro de data + histórico por marina** — consumo varia com salinidade, temperatura, corrente parasita local; log traz padrão rastreável para diagnóstico.

> [!danger] Quando chamar um especialista (engenheiro corrosionista / surveyor / NACE-certified)
> 1. **Ânodo consumindo em < 3 meses ou ausente após 1 mês** — corrente parasita severa do shore power, falha de isolação AC, vizinho de marina com problema; investigação com eletrodo de referência + corrente externa + isolador galvânico; antes disso, NÃO zarpe (risco iminente de perda de hélice/eixo/rabeta).
> 2. **Corrosão severa em metal protegido mesmo com ânodo consumindo** — sinal de bonding descontínuo ou corrente parasita localizada; engenharia dedicada de corrosão com medição setorizada por eletrodo de referência (NACE TM0497).
> 3. **Embarcação metálica (aço, alumínio, liga cobre-níquel) > 12 m** — projeto de proteção catódica dedicado (NACE SP0176 + DNV-RP-B401); cálculo de corrente por área + ânodos galvânicos ou ICCP (Impressed Current Cathodic Protection).
> 4. **ICCP (sistema de proteção catódica por corrente impressa)** — comum em embarcações comerciais grandes; exige projeto + comissionamento + monitoramento contínuo; engenharia dedicada + CP technician homologado (NACE CP1-4).
> 5. **Corrosão em ambiente contaminado (esgoto marina, vazamento combustível)** — acelera consumo ânodo e ataca metais não protegidos; mudança de marina ou ação legal + laudo.
> 6. **Pintura/revestimento em casco metálico falhando ao redor do ânodo** — indica superproteção (potencial < -1,15 V vs Ag/AgCl) causando descolagem alcalina; reduzir ânodos ou usar Al-In (menos ativo que Zn).
> 7. **Perícia pós-perda de hélice/eixo/rabeta por corrosão** — preservar peça afetada + ânodos existentes + histórico; laudo IBAPE/Abracem + NACE-certified; base para acionamento de seguradora ou marina.
> 8. **Casco alumínio com zinco instalado erroneamente** — zinco é mais nobre que alumínio em alguns regimes = proteção INVERTIDA (casco vira ânodo, se consome); corrigir com ânodos de magnésio ou Al-In especial; erro comum em retrofit.
> 9. **Embarcação comercial classificada (NORMAM-201/204, BV, Lloyd's, RINA, DNV)** — plano de proteção catódica auditável + medições periódicas + log; inspeção a cada docagem.

## O que é

Ânodo sacrificial é uma peça de liga metálica mais ativa instalada para se corroer preferencialmente e proteger outros metais ligados eletricamente ao mesmo sistema.

Não é acessório estético nem "peça de troca por hábito". É parte do sistema de proteção catódica.

## O que ele protege

Dependendo da embarcação e da arquitetura, o anodo pode proteger:

- hélice e eixo;
- rabeta, pé de motor e trim tabs;
- ferragens submersas ligadas ao bonding;
- casco metálico ou partes metálicas específicas;
- trocadores de calor, motores e [[Boiler]]s com anodos internos.

## Materiais mais usados

Os três grupos mais comuns são:

- zinco;
- alumínio em liga apropriada para uso sacrificial;
- magnésio.

A escolha depende da condutividade da água, da liga do anodo e da aplicação. De forma geral:

- água salgada costuma aceitar bem zinco ou alumínio adequado;
- água salobra normalmente favorece alumínio sacrificial;
- água doce pede magnésio em muitas aplicações.

Isso não substitui recomendação do fabricante do equipamento nem levantamento de potencial quando a aplicação é crítica.

## O erro mais comum de seleção

O maior erro de campo é tratar o material do anodo como item universal. Não é.

Também é erro supor que "mais anodo sempre é melhor". Excesso de proteção pode ser indesejável em alguns conjuntos, especialmente quando há revestimentos, alumínio e geometrias sensíveis. Projeto sério busca proteção suficiente, não superproteção cega.

## Instalação correta

O ponto central é simples: sem continuidade elétrica adequada, o anodo não protege.

Isso exige:

- superfície de contato limpa e metálica;
- fixação firme;
- ausência de tinta, primer ou isolamento no ponto de contato;
- integração coerente com o sistema que se pretende proteger.

Pintar o anodo ou montá-lo sobre superfície isolada anula sua função prática.

## Como interpretar o consumo

O consumo do anodo é informação diagnóstica, não só critério de troca.

### Consumo compatível

Indica que há atividade de proteção, mas não garante sozinho que o sistema está perfeito.

### Consumo muito baixo ou inexistente

Pode significar:

- falta de contato elétrico;
- anodo inadequado para o eletrólito;
- área protegida pequena demais ou mal conectada;
- leitura visual enganosa por incrustação superficial.

### Consumo excessivamente rápido

Pode indicar:

- ambiente agressivo;
- anodo subdimensionado;
- problema sério de [[Correntes Parasitas — Stray Currents]];
- falha de isolamento ou problema vindo do shore power.

Trocar o anodo sem investigar a causa, nesse caso, é só mascarar o problema.

## Dimensionamento

O dimensionamento depende de:

- área metálica exposta;
- material protegido;
- qualidade do revestimento;
- ambiente de operação;
- tempo esperado entre inspeções;
- corrente de proteção requerida.

Regras simplificadas de "x kg por y metros quadrados" podem servir como aproximação preliminar, mas não substituem recomendação do fabricante nem medição de potencial em aplicações relevantes.

## Anodos internos

Muita instalação falha por focar só nos anodos externos. Também existem anodos internos em:

- trocadores de calor;
- blocos e circuitos de refrigeração de motores;
- [[Boiler]]s e reservatórios específicos.

Eles são críticos e frequentemente esquecidos em manutenção.

## Diagnóstico profissional

Verificar:

- integridade física;
- continuidade elétrica com o conjunto protegido;
- padrão de consumo ao longo do tempo;
- histórico por marina ou ambiente;
- potencial do sistema com eletrodo de referência, quando a aplicação justificar.

O método mais confiável para avaliar a qualidade da proteção não é só olhar o anodo, mas correlacionar:

- consumo;
- condição do metal protegido;
- medição de potencial;
- presença de correntes parasitas.

## Boas práticas

- usar anodo de liga correta e procedência confiável;
- registrar data de instalação e histórico de consumo;
- inspecionar sempre que a embarcação sair do seco ou em intervalos programados;
- trocar antes de perder área útil demais, conforme a criticidade da aplicação;
- revisar ponto de contato, não apenas trocar a peça;
- incluir anodos internos no plano de manutenção.

## Erros comuns

Os mais frequentes são:

- instalar sobre tinta;
- comprar anodo genérico sem liga confiável;
- usar o mesmo material em qualquer ambiente;
- tratar consumo alto como sinal de "anodo bom";
- ignorar anodos internos;
- esquecer que o anodo responde à qualidade do sistema elétrico ao redor.

## Relação com outras notas

[[Eletrólise]] e [[Correntes Parasitas — Stray Currents]] explicam por que um anodo pode acabar rápido demais. [[Bonding — Sistema de Interligação de Massas]] define como os metais estão eletricamente conectados. [[Isolador Galvânico - Transformador de Isolamento]] entra quando o shore power participa do problema.

## Normas aplicáveis

**ABYC — proteção catódica em embarcações (náutica):**

- **ABYC E-2 (2020)** — *Cathodic Protection*: bonding + ânodos sacrificiais + eletrodo de referência + critério de potencial; documento mestre. Exige continuidade < 1 Ω entre massas metálicas submersas.
- **ABYC E-11 (2023)** — *AC & DC Electrical Systems*: interface bonding + shore power + isolador galvânico + transformador de isolação.
- **ABYC A-22** — Marinas and Boatyards: ambiente de marina (corrente parasita coletiva).
**ISO — padrões internacionais:**

- **ISO 13297:2020** — Small craft — Electrical systems AC & DC: requisitos de bonding e proteção em recreio.
- **ISO 17339:2009** — Sacrificial anode materials and testing methods.
- **ISO 15589-1/-2** — Cathodic protection of pipeline / offshore pipelines (aplicação cruzada).

**NACE (Associação de engenheiros corrosionistas — referência técnica primária):**

- **NACE SP0176:2007** — Corrosion Control of Submerged Areas of Permanently Installed Steel Offshore Structures: projeto de proteção catódica offshore.
- **NACE TM0497:2018** — Measurement Techniques Related to Criteria for Cathodic Protection: métodos de medição de potencial com eletrodo de referência.
- **NACE SP0387:2012** — Metallurgical and Inspection Requirements for Offshore Steel Structures.
- **NACE CP1 / CP2 / CP3 / CP4** — níveis de certificação profissional em proteção catódica (Tester, Technician, Technologist, Specialist).

**ASTM — materiais de ânodo:**

- **ASTM B418-16** — Standard Specification for Cast and Wrought Galvanic Zinc Anodes: Tipo I (MIL spec) e Tipo II (comercial).
- **ASTM G97-97(2018)** — Laboratory Evaluation of Magnesium Sacrificial Anode Test Specimens.
- **ASTM F1182-07** — Standard Specification for Anodes, Sacrificial Zinc Alloy (padrão US Navy).

**Militar/histórico:**

- **MIL-A-18001K** — Zinc anodes (US military): composição e teste de ânodos de zinco; base técnica histórica.

**IEC — embarcações comerciais (SOLAS):**

- **IEC 60092-350** — Electrical installations in ships — General construction.
- **IEC 60092-301** — Equipment — Generators and motors.

**Sociedades classificadoras:**

- **DNV-RP-B401** — Cathodic Protection Design: projeto de CP em offshore (referência técnica de classificadora).
- **Lloyd's Register Rules Pt 5 Ch 21** — Cathodic Protection: requisitos para embarcações classificadas.
- **ABS / BV / RINA** — regras equivalentes; todas exigem plano de proteção catódica auditável.

**Brasil:**

- **NORMAM-211/DPC** — Esporte e recreio.
- **NORMAM-201/204/DPC** — Comercial / SMM.
- **NBR 5410:2004 + emendas** — princípios de baixa tensão (interface bonding).
- **NBR ISO 12696:2016** — Proteção catódica de aço em concreto (referência cruzada).

**Diretiva europeia:**

- **CE-RCD Directive 2013/53/EU** — Recreational Craft Directive.

## Glossário rápido

- **Alumínio Al-In (Aluminum-Indium alloy)** — liga de alumínio sacrificial com índio; padrão náutico atual para salgada/salobra, maior eficiência que zinco (2.400-2.700 Ah/kg vs zinco 780 Ah/kg).
- **Ânodo galvânico (sacrificial)** — metal mais ativo que cede elétrons preferencialmente; Zn, Al, Mg.
- **Ânodo ICCP (Impressed Current)** — ânodo não-sacrificial (platina, MMO, silício-ferro) alimentado por corrente externa (retificador); comum em embarcações comerciais grandes.
- **Área eficaz** — superfície efetivamente em contato com eletrólito; ânodo coberto por incrustação perde área útil.
- **ASTM B418 Tipo I** — zinco militar (U-3): 99,99% Zn + traços Al/Cd; padrão para salgada pura.
- **ASTM B418 Tipo II** — zinco comercial (ZHC): alta performance em águas quentes/contaminadas.
- **Bonding submerso** — interligação de TODAS as massas metálicas abaixo da linha d'água (ABYC E-2).
- **Consumo específico (Ah/kg)** — capacidade do ânodo: Zn puro = 820 Ah/kg, Zn comercial = 780 Ah/kg, Al-In = 2.500 Ah/kg, Mg = 1.230 Ah/kg.
- **Corrente de proteção** — densidade de corrente para manter potencial abaixo do crítico: aço em salgada ≈ 30-100 mA/m²; alumínio ≈ 10-50 mA/m².
- **Corrente parasita (stray current)** — corrente externa (shore power, vizinho de marina) que acelera consumo do ânodo.
- **DNV-RP-B401** — recommended practice de DNV para projeto de proteção catódica.
- **Eficiência do ânodo** — razão entre capacidade teórica e real: Zn ≈ 95%, Al-In ≈ 85%, Mg ≈ 50-60%.
- **Eletrodo de referência Ag/AgCl (saturated)** — padrão em medição de proteção catódica em salgada; potencial conhecido 0 mV (convenção).
- **Eletrodo de referência Zinco (Zn-RE)** — alternativa de campo: mais simples, mais barato, menos preciso; 0,25 V vs Ag/AgCl.
- **Eletrodo de referência Cobre-sulfato (Cu/CuSO₄)** — padrão em solo/concreto, NÃO em água salgada.
- **Embarcação metálica** — casco aço ou alumínio; exige projeto de proteção catódica dedicado (NACE SP0176).
- **Encaixe cônico (cone seat anode)** — geometria de instalação em eixo/hélice; garante contato metal-metal.
- **EPDM / Viton (gasket)** — vedação do suporte de ânodo; não deve isolar o ânodo do metal protegido.
- **Eprom (ânodo "eprom")** — gíria para ânodo em formato disco rígido-parafuso; popular em trim tab e rabeta.
- **Fathom gauge** — critério histórico de espessura: ânodo em 25% da espessura original = substituir.
- **Galvanic isolator (isolador galvânico)** — dispositivo no terra shore que bloqueia DC < 1,2 V (diodos em oposição); permite passagem AC de falta.
- **Gpm wear rate** — taxa de consumo em gramas por mês; acompanhado mensalmente é bom indicador.
- **Hull potential (potencial do casco)** — tensão medida entre casco e eletrodo de referência; indica estado da proteção.
- **Hype ("hype corrosion")** — corrosão por superproteção em alumínio; gera alcalinidade local que dissolve o alumínio.
- **ICCP (Impressed Current Cathodic Protection)** — sistema ativo com retificador, controlador, ânodos inertes; padrão em navios grandes.
- **In-service measurement (medição em serviço)** — medição de potencial com embarcação na água; exige acesso submerso ao ponto.
- **Ionic Current** — corrente que flui por ions no eletrólito (água); diferente da corrente eletrônica no metal.
- **Ligação elétrica entre ânodo e protegido** — condição obrigatória; sem ela, ânodo é decorativo.
- **Linha de marca (waterline)** — limite da proteção submersa; ânodos acima da linha d'água não funcionam (secos).
- **Magnésio AZ-63 / AZ-31** — ligas comuns de magnésio sacrificial; alto potencial, consumo rápido em salgada.
- **Mass (massa do ânodo)** — peso inicial (kg); determina vida útil em função da corrente de proteção.
- **Mill finish (acabamento de fabricação)** — ânodo novo vem sem pintura, sem primer, sem proteção superficial; qualquer tratamento é erro.
- **MMO (Mixed Metal Oxide)** — ânodo inerte para ICCP (substrato titânio + óxidos); alta durabilidade, baixo consumo.
- **NACE TM0497** — método de medição de potencial com instrument off/on para eliminar queda IR do eletrólito.
- **Over-protection (superproteção)** — potencial < -1,15 V vs Ag/AgCl; em alumínio causa "hype corrosion" alcalina; em aço pode causar desprendimento de hidrogênio (embrittlement em alta resistência).
- **Pear-shaped anode (gota)** — formato para trim tab e sailing.
- **Pencil anode (lápis)** — ânodo cilíndrico de motor interno (trocador de calor, resfriamento).
- **Potencial de proteção — critério ABYC/NACE:**
  - Aço em salgada: -0,85 V a -1,10 V vs Ag/AgCl
  - Alumínio em salgada: -0,85 V a -1,00 V (cuidado com superproteção)
  - Cobre/latão: -0,60 V a -0,80 V
- **Radiograph (teste ultrassom)** — verifica integridade interna do ânodo contra porosidade.
- **Reference electrode (eletrodo de referência)** — sensor para medição de potencial absoluto.
- **Sacrificial mass consumed** — massa consumida em um período; base do cálculo de vida útil.
- **Salinity-specific alloy** — ligas específicas por salinidade: Zn para salgada, Al-In para salobra, Mg para doce.
- **Secondary anode (ânodo secundário)** — ânodo de backup instalado em ponto difícil de inspecionar.
- **Shaft anode (ânodo de eixo)** — cinta ou collar instalado no eixo da hélice.
- **Shore power ground** — aterramento do cabo de marina; rota de corrente galvânica para vizinhos.
- **Single reference cell method** — medição simples com um único eletrodo de referência; menos precisa que multi-cell.
- **Specific consumption rate (kg/ano)** — taxa anual de consumo; típico 0,5-2 kg/ano em embarcação de recreio 30 pés.
- **Stern gear anode (conjunto popa)** — conjunto completo: eixo, hélice, rabeta, trim, leme.
- **Teardrop anode** — formato aerodinâmico para hélice.
- **Through-hull anode** — ânodo que passa pelo casco (rosca de vantagem para acesso externo).
- **Trim tab anode (placa)** — ânodo plano instalado na popa, frequentemente esquecido.
- **Zinc grade M** — zinco militar grau M (99,99% puro); padrão ABYC.
- **Zinc reference electrode (Zn-RE)** — eletrodo de referência simples: zinco imerso indica 0,25 V vs Ag/AgCl.

## Visual didático

![Anodo, eletrolise e protecao contra corrosao](../_visuals/generated/anodo-eletrolise-protecao.svg)

Evitar que anodo seja tratado como solucao universal para qualquer corrosao submersa.

**Cautela:** Diagnostico de corrosao exige inspecao, historico, medicao e avaliacao do ambiente de marina.

Material de apoio: [Anodo, eletrolise e protecao contra corrosao](../_visuals/generated/anodo-eletrolise-protecao.md)

## Integração com outras notas

- [[Bonding — Sistema de Interligação de Massas]]
- [[Boiler]]
- [[Correntes Parasitas — Stray Currents]]
- [[Eletrólise]]
- [[Isolador Galvânico - Transformador de Isolamento]]

## Perguntas que esta nota responde

- Como escolher o anodo certo para o ambiente da embarcação?
- Como diferenciar anodo sem contato de anodo consumindo por problema elétrico?
- Quando trocar o anodo e quando investigar a arquitetura elétrica antes disso?
