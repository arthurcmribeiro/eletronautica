---
title: "Detector de Gás GLP / GN"
note_type: "technical-note"
domain: "80_Seguranca_e_Corrosao"
source_file: "DETECTOR DE GÁS GLP GN 33a19734f7fb81b6bb99f3cffadae2fe.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "36"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
  - "internacional"
normas_citadas:
  - "ABYC A-1 (2022) — Marine Liquefied Petroleum Gas (LPG) Systems"
  - "ABYC A-26 — LPG and CNG Fueled Appliances"
  - "ABYC A-27 — Marine Galley Stoves and Ovens"
  - "ABYC E-11 (2023) — AC & DC Electrical Systems on Boats (alimentação do detector)"
  - "ABYC H-2 — Ventilation of Boats Using Gasoline (referência cruzada de ventilação)"
  - "ISO 10239:2017 — Small craft — Liquefied petroleum gas (LPG) systems"
  - "ISO 16147 — Small craft — Inboard diesel engines (referência cruzada)"
  - "ISO 12133:2011 — Small craft — CO detection (comparação)"
  - "UL 1484 — Residential Gas Detectors"
  - "UL 1524 — Marine Alarm Systems"
  - "UL 61010-1 — Safety requirements for electrical equipment for measurement"
  - "EN 50194-1 — Electrical apparatus for the detection of combustible gases in domestic premises"
  - "EN 50244 — Selection, installation, use and maintenance of residential gas detectors"
  - "IEC 60079-0 — Explosive atmospheres — General requirements"
  - "IEC 60079-29-1 — Gas detectors — Performance requirements"
  - "NBR 13787 — Central predial de GLP"
  - "NBR 13523 — Central predial de GLP — armazenagem"
  - "NBR 14024 — Instalações internas de GLP"
  - "NR-20/MTE — Segurança e saúde no trabalho com inflamáveis e combustíveis"
  - "INMETRO Portaria 27/2004 + Portaria 195/2011 — equipamentos GLP"
  - "NFPA 302 — Fire Protection Standard for Pleasure and Commercial Motor Craft"
  - "NFPA 58 — Liquefied Petroleum Gas Code"
  - "NFPA 54 — National Fuel Gas Code"
  - "USCG 33 CFR Part 183 — Boats and Associated Equipment"
  - "NORMAM-211/DPC — Esporte e recreio"
  - "NORMAM-201/204/DPC — Comercial / SMM"
  - "CE-RCD Directive 2013/53/EU — Recreational Craft Directive"
review_level: "engineering-curated"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "DETECTOR DE GÁS GLP GN"
  - "DETECTOR DE GÁS GLP / GN"
  - "Detector de Gás GLP GN"
seo_title: "Detector de Gás GLP / GN"
seo_description: "DETECTOR DE GAS GLP GN — Sistema de deteccao de vazamento de gas combustivel, com enfase na diferenca entre GLP e gas natural, posicionamento do sensor e integracao com valvula de corte."
seo_keywords:
  - "Detector de gas"
  - "GLP"
  - "Gas natural"
  - "Valvula de corte"
  - "80 Seguranca e Corrosao"
geo_queries:
  - "Como instalar detector de GLP no barco?"
  - "Qual a diferenca entre detector de GLP e de GN em embarcacoes?"
related_notes:
  - "Detector de CO — Monóxido de Carbono"
  - "Sistema de Alarme Geral / Painel de Alarmes"
  - "Extintor Automático — Combate a Incêndio na Casa de Máquinas"
  - "Fogão - Cooktop Elétrico - Galley"
  - "Blower"
---

# Detector de Gás GLP / GN

> [!abstract] Resumo técnico
> Detector de gás combustivel é o sistema de alarme que identifica vazamento de GLP ou gás natural antes que a concentração se aproxime de faixa perigosa. O ponto crítico é que GLP e GN não se comportam igual no ambiente: a posição do sensor, a estratégia do sistema e a integração com válvula de corte dependem do gás realmente usado a bordo.

> [!tip] Regra de decisão em 30 segundos
> 1. **GLP é pesado (densidade 1,5–2,0 × ar) e desce; GN é leve (0,55 × ar) e sobe** — sensor em posições OPOSTAS. Errar isso é projeto cego.
> 2. **GLP → sensor BAIXO (próximo ao piso, em zona de acúmulo)** — bilge, sob fogão, compartimento baixo adjacente à tubulação; **GN → sensor ALTO (próximo ao teto)**.
> 3. **Detector = alerta precoce a 10–25% LEL, NÃO confirmador de explosão** — ABYC A-1 recomenda disparo a 25% LEL; trabalhar na faixa > 50% LEL já é falha de projeto.
> 4. **Sistema completo = detector + válvula solenóide NC (normally closed / fail-safe) + compartimento estanque ventilado + regulador certificado** — detector sozinho sem corte automático é mitigação parcial.
> 5. **ABYC A-1 + ISO 10239 + NFPA 58/302 + EN ISO 10239** são as referências primárias para sistema de GLP em embarcação; residencial (NBR 13787, EN 50194) é adaptação, não padrão nativo.
> 6. **Olfato (mercaptana) é backup, NÃO primário** — vazamento rápido satura o olfato antes de o cheiro ser percebido; depender do nariz é negligência.
> 7. **Teste com gás padrão (bomba/ampola de calibração), NÃO com isqueiro/chama/cheiro solto** — improvisação com chama é risco direto de explosão; ABYC A-1 exige protocolo documentado.
> 8. **Cilindro em compartimento estanque com DRENO OVERBOARD (para fora) na parte BAIXA** — GLP vaza, cai, sai pelo dreno; dreno para bilge = acúmulo = explosão. Ventilação alta serve para GN, não para GLP.
> 9. **Substituição do sensor: 5 anos típico (pellistor), 10 anos (IR dual-channel), 2–3 anos (portátil)** — sensor vencido é cego; checagem de data obrigatória.

> [!danger] Quando chamar emergência / especialista
> 1. **Cheiro de gás + alarme disparou** — EMERGÊNCIA: NÃO operar nenhum interruptor elétrico (faísca pode iniciar explosão), fechar válvula manual do cilindro, evacuar todos, abrir portas/escotilhas, ventilar naturalmente; só retornar quando detector zerar e inspeção técnica confirmar.
> 2. **Compartimento de GLP sem dreno para fora do casco** — retrofit obrigatório antes de próxima operação; vazamento acumula em bilge e qualquer ignição (motor, fiação, bateria) causa deflagração; ABYC A-1 + ISO 10239.
> 3. **Fogão com botão frouxo, vazamento lento contínuo em embarcação fechada** — encontrado em > 40% das embarcações de > 10 anos não manutenidas; levantamento com gas sniffer portátil + bubble test em todas as conexões.
> 4. **Detector de GLP usado para detectar GN (ou inverso)** — projeto cego: sensor pode nem responder ao gás presente; troca de detector + reposicionamento obrigatórios antes de usar.
> 5. **Churrasqueira ou grill a GLP retrofitada em embarcação fechada** — projeto precisa revisão completa: compartimento estanque, ventilação, dreno, mangote certificado ABYC A-1, válvula solenóide; instalador certificado + teste pressão.
> 6. **Charter, aluguel ou escola náutica com sistema GLP não certificado ou sem manutenção documentada** — responsabilidade civil e penal em caso de incidente; INMETRO Portaria 27/2004 + NORMAM-201.
> 7. **Perícia pós-explosão / incêndio com suspeita de gás** — preservar como evidência: cilindro (mesmo vazio), regulador, mangote, tubulação, válvulas, detector; laudo IBAPE + corpo de bombeiros + Abracem.
> 8. **Retrofit de GLP para GN (marina com GN) ou inverso sem projeto completo** — não são intercambiáveis: pressão de trabalho, volume de consumo, posição do sensor, dimensão do compartimento, regulador — tudo muda.
> 9. **Sistema "caseiro" com mangote de borracha de cozinha doméstica, conexão de rosca errada ou tubulação de cobre recozido sem suporte** — condição de risco iminente; sistema deve ser reconstruído do zero por profissional ABYC A-1 / ISO 10239.

## O que é

É um sistema de detecção de gás combustível composto, em geral, por:

- sensor;
- módulo de alarme/controle;
- sinalização sonora e visual;
- eventualmente válvula solenóide de corte.

Em embarcações de recreio, o caso mais comum é o uso de GLP. Se houver gás natural ou outra mistura, a seleção e a posição do sensor precisam ser revistas conforme o comportamento do gás.

## Função na embarcação

- detectar vazamento antes de formação de atmosfera perigosa;
- acionar aviso local claro;
- comandar corte automático do gás quando a arquitetura permitir;
- complementar compartimento adequado, ventilação e disciplina operacional.

## Fundamentos mínimos

### GLP e GN não usam a mesma lógica de instalação

- **GLP/propano/butano** tende a se acumular em regiões baixas.
- **GN/metano** tende a se acumular em regiões altas.

Misturar esses comportamentos em uma mesma recomendação genérica é erro grave de projeto.

### Detector não substitui sistema de gás bem construído

Compartimento do cilindro, ventilação, regulador, tubulação, conexões e válvula de corte continuam sendo a base da segurança.

### Alarme deve antecipar risco, não "confirmar explosão"

Sistemas sérios operam como alerta precoce em fração do limite inferior de inflamabilidade, conforme o fabricante e a certificação do equipamento.

### Teste precisa seguir o método do fabricante

Improvisar teste com chama, vazamento deliberado ou método não previsto pode ser inseguro e induzir interpretação errada do sistema.

## Projeto e instalação

### O que precisa ser definido

1. qual gás existe realmente a bordo;
2. onde o gás pode acumular em caso de vazamento;
3. se haverá válvula solenóide de corte;
4. onde ficará o painel de alarme;
5. como será a alimentação elétrica do sistema;
6. quais testes e substituições periódicas serão adotados.

### Diretrizes práticas

- para GLP, instalar sensor em zona baixa compatível com o risco;
- para GN, instalar sensor em zona alta compatível com o risco;
- manter o painel e o alarme em local perceptível ao operador;
- integrar corte automático quando a arquitetura de gás utilizar válvula dedicada;
- alimentar o sistema de forma coerente com a função de segurança;
- seguir o manual do detector e da válvula de corte, sem improviso.

## Onde costuma dar problema

| Problema | Causa provável |
| --- | --- |
| sensor na posição errada | desconhecimento do comportamento do gás |
| alarme frequente sem diagnóstico | contaminação, produto inadequado ou instalação ruim |
| detector existe, mas válvula não corta | integração elétrica incompleta |
| sistema desligado quando mais precisava | alimentação inadequada ou falta de governança |
| falsa sensação de segurança | detector sem manutenção ou fora do prazo |

## Diagnóstico prático

1. Confirmar qual gás está sendo usado.
2. Verificar se o sensor está no ponto compatível com esse gás.
3. Testar funções conforme instrução do fabricante.
4. Confirmar atuação do alarme e, se existir, da válvula de corte.
5. Inspecionar compartimento, regulador, tubulação e conexões do sistema de gás.

## Boas práticas profissionais

- diferenciar explicitamente projeto para GLP e para GN;
- usar detector e controle compatíveis com o gás escolhido;
- prever válvula solenóide de corte quando aplicável;
- manter disciplina de inspeção do sistema de gás como um todo;
- treinar tripulação para resposta imediata ao alarme;
- nunca confiar só no olfato como estratégia de segurança.

## Erros comuns

- instalar detector alto para GLP ou baixo para GN;
- tratar qualquer detector de gás como universal;
- deixar cilindro e detector sem arquitetura coerente de ventilação e corte;
- improvisar teste com método inseguro;
- usar detector de CO como se servisse para vazamento de GLP.

## Relação com outros sistemas

- **[[Detector de CO — Monóxido de Carbono]]** — risco distinto; não substitui detector de gás combustível.
- **[[Sistema de Alarme Geral / Painel de Alarmes]]** — possível integração de alarme.
- **[[Blower]]** — ventilação pode ser parte da mitigação, conforme a arquitetura.
- **[[Extintor Automático — Combate a Incêndio na Casa de Máquinas]]** — incêndio é consequência possível, mas não substitui prevenção do vazamento.

## Normas e referências

- documentação do detector e da válvula solenóide empregados;
- critérios aplicáveis ao sistema de GLP/GN da embarcação;
- manuais do fabricante para posição, teste e substituição dos sensores.

## Normas aplicáveis (organizadas por família)

Sistema de gás combustível em embarcação cruza quatro áreas normativas: **instalação marinha de GLP/CNG** (ABYC, ISO, NFPA 302), **combustível doméstico base** (NFPA 58/54, NBR 13787), **detector propriamente dito** (UL, EN, IEC 60079), **trabalho com inflamáveis** (NR-20).

### ABYC (American Boat & Yacht Council) — referência marítima primária

- **ABYC A-1 (2022) — Marine Liquefied Petroleum Gas (LPG) Systems** — norma central: compartimento estanque, dreno overboard, mangotes certificados, regulador, válvula solenóide, teste pressão, detector 25% LEL.
- **ABYC A-26 — LPG and CNG Fueled Appliances** — aparelhos que consomem GLP/CNG: fogão, aquecedor, grill, churrasqueira; exigências de certificação e instalação.
- **ABYC A-27 — Marine Galley Stoves and Ovens** — fogões marinhos: gimbaled, selagem, ignição, válvula termocupla.
- **ABYC E-11 (2023) — AC & DC Electrical Systems on Boats** — alimentação do detector: circuito dedicado, fusível, sempre energizado.
- **ABYC H-2 — Ventilation of Boats Using Gasoline** — referência cruzada para ventilação (blower antes de partida); aplica-se por extensão a casa de máquinas onde pode haver gás.

### ISO (internacional)

- **ISO 10239:2017 — Small craft — Liquefied petroleum gas (LPG) systems** — equivalente internacional de ABYC A-1; obrigatório para certificação CE.
- **ISO 16147 — Small craft — Inboard diesel engines** — referência cruzada para sistema de combustível em embarcação recreativa.
- **ISO 12133:2011 — Small craft — CO detection** — detector de CO paralelo; não substitui detector de gás combustível.

### UL (certificação USA)

- **UL 1484 — Residential Gas Detectors** — certificação residencial; referência para sensor; não resiste a ambiente marinho sem adaptação.
- **UL 1524 — Marine Alarm Systems** — certificação específica para sistema de alarme marinho (pode integrar CO + gás + bilge + incêndio).
- **UL 61010-1** — requisitos de segurança para equipamento elétrico de medição.

### EN / IEC (Europa e internacional)

- **EN 50194-1 — Electrical apparatus for the detection of combustible gases in domestic premises** — referência residencial europeia; 50194-1 Tipo 1 (sensor catalítico), Tipo 2 (semicondutor).
- **EN 50244 — Selection, installation, use and maintenance of residential gas detectors** — guia de aplicação complementar a 50194.
- **IEC 60079-0 — Explosive atmospheres — Part 0: Equipment — General requirements** — base para classificação de equipamento em área Ex.
- **IEC 60079-29-1 — Gas detectors — Performance requirements of detectors for flammable gases** — requisitos de desempenho para detector em área classificada.

### NFPA (segurança contra incêndio)

- **NFPA 302 — Fire Protection Standard for Pleasure and Commercial Motor Craft** — referência marinha; cobre detecção e combate a incêndio + prevenção de vazamento.
- **NFPA 58 — Liquefied Petroleum Gas Code** — código LP americano; referência técnica de reguladores, cilindros, tubulação.
- **NFPA 54 — National Fuel Gas Code** — código de gás natural americano.

### Brasil (infraestrutura)

- **NBR 13787 — Central predial de GLP** — referência residencial/predial; conceitos aplicáveis a projeto de compartimento de cilindro.
- **NBR 13523 — Central predial de GLP — armazenagem** — armazenagem do cilindro; distâncias mínimas, ventilação.
- **NBR 14024 — Instalações internas de GLP** — tubulação interna; dimensionamento, materiais, pressão de teste.
- **NR-20/MTE — Segurança e saúde no trabalho com inflamáveis e combustíveis** — aplicável a charter, escola náutica, profissional do gás; treinamento obrigatório.
- **INMETRO Portaria 27/2004 + Portaria 195/2011** — regulamentação técnica de equipamentos GLP vendidos no Brasil; etiqueta compulsória.

### USCG (USA)

- **USCG 33 CFR Part 183 — Boats and Associated Equipment** — regulamento federal; define equipamento obrigatório em embarcação recreativa USA.

### Brasil (marítimo)

- **NORMAM-211/DPC — Esporte e recreio** — regulamento da DPC para recreio.
- **NORMAM-201/204/DPC — Comercial / SMM** — regulamento para comercial classificada.

### Europa (RCD)

- **CE-RCD Directive 2013/53/EU — Recreational Craft Directive** — embarcação CE com sistema de GLP deve atender ISO 10239 + EN 50194 + auditoria de notified body.

### Limiares inflamabilidade (referência técnica)

- **Propano (C₃H₈):** LEL 2,1 % (21.000 ppm), UEL 9,5 %.
- **Butano (C₄H₁₀):** LEL 1,8 % (18.000 ppm), UEL 8,4 %.
- **GLP (mistura propano/butano):** LEL ~1,9 %, UEL ~9,0 %.
- **Metano / GN:** LEL 5 % (50.000 ppm), UEL 15 %.
- **ABYC A-1 — alarme de detector a 25 % LEL** (equivale a ~5.000 ppm GLP ou ~12.500 ppm GN).

### Como usar este conjunto normativo na prática

| Situação | Norma-chave |
|---|---|
| Projeto de sistema GLP novo em recreio | ABYC A-1 + ISO 10239 |
| Projeto comercial classificado | ISO 10239 + sociedade classificadora |
| Seleção do detector | EN 50194-1 / UL 1484 / UL 1524 |
| Área classificada (comercial petróleo) | IEC 60079-0 + IEC 60079-29-1 |
| Embarcação CE (Europa) | ISO 10239 + RCD |
| Charter / aluguel Brasil | NORMAM + NR-20 + INMETRO Portaria 27/2004 |
| Ventilação de casa de máquinas | ABYC H-2 |
| Retrofit de churrasqueira | ABYC A-26 + A-1 + teste pressão |
| Fogão gimbaled | ABYC A-27 |
| Perícia pós-incidente | IBAPE + NR-20 + preservação de evidência |

## Glossário rápido

### Gases e propriedades

- **GLP (Gás Liquefeito de Petróleo)** — mistura de propano (C₃H₈) e butano (C₄H₁₀) em proporções variáveis; líquido sob pressão no cilindro, gás à pressão atmosférica.
- **Propano (C₃H₈)** — componente mais volátil do GLP; densidade 1,52 × ar; LEL 2,1 %; vaporiza a −42 °C.
- **Butano (C₄H₁₀)** — componente menos volátil; densidade 2,00 × ar; LEL 1,8 %; vaporiza a −0,5 °C (para de funcionar no frio).
- **GN (Gás Natural) / Metano (CH₄)** — gás leve; densidade 0,55 × ar; LEL 5 %; distribuído por tubulação (em marinas especiais) ou CNG comprimido.
- **CNG (Compressed Natural Gas)** — GN comprimido a 200–250 bar em cilindro; raro em recreio, comum em embarcação comercial USA.
- **Densidade relativa ao ar** — GLP 1,5–2,0 (pesado, desce); GN 0,55 (leve, sobe); CO 0,97 (neutro, mistura).
- **LEL (Lower Explosive Limit / Limite Inferior de Inflamabilidade)** — concentração mínima para ignição; abaixo do LEL não queima.
- **UEL (Upper Explosive Limit / Limite Superior)** — concentração máxima para ignição; acima do UEL não queima (rico demais).
- **Faixa de inflamabilidade** — intervalo [LEL, UEL]; mais estreito = mais seguro; GN 5–15 % é mais tolerante que propano 2,1–9,5 %.
- **Flash point** — temperatura mínima onde o vapor inflama com fonte de ignição; GLP é gás, não tem flash point convencional.
- **Mercaptana (etil-mercaptana, t-butil-mercaptana)** — odorante adicionado ao GLP/GN (~10–20 ppm); cheiro característico de "ovo podre" ou "repolho"; backup olfativo.

### Infraestrutura do sistema GLP

- **Cilindro (botijão)** — recipiente de aço/alumínio para GLP líquido; 13 kg P13 doméstico, P2/P5 pequeno para embarcação.
- **Válvula manual do cilindro** — corte primário; fechar sempre que não em uso.
- **Regulador de 1º estágio** — reduz pressão do cilindro (~1–7 bar) para pressão intermediária (~0,5 bar); em sistemas grandes.
- **Regulador de 2º estágio / final** — pressão final para aparelho (~28 mbar / 11" WC); padrão residencial/marinho.
- **Regulador OPD (Overfill Protection Device)** — proteção contra sobre-enchimento; obrigatório em alguns cilindros.
- **Mangote flexível ABYC A-1** — mangote com cobertura resistente a hidrocarboneto + reforço têxtil; certificado especificamente para GLP marinho.
- **Tubulação rígida de cobre recozido** — usado em trechos fixos; diâmetro 3/8" ou 1/2"; conexões flare SAE 45°.
- **Conexão flare SAE 45°** — cone metálico, sem fita, sem solda; padrão GLP.
- **Compartimento estanque do cilindro** — compartimento vedado que contém vazamento, com dreno overboard e ventilação controlada.
- **Dreno overboard (dreno para fora do casco)** — saída do compartimento do cilindro direto para o costado, acima da linha d'água; leva gás vazado para fora; obrigatório para GLP (pesado).

### Detector e válvula

- **Detector marinho ABYC A-1** — detector certificado para ambiente marinho; resistente a vibração, umidade, choque.
- **Válvula solenóide de corte NC (normally closed)** — válvula elétrica; fail-safe: quando sem energia, fecha; aciona com detector.
- **Válvula solenóide de corte no cilindro (propane tank shutoff)** — ligada ao detector; corta na fonte ao detectar vazamento.
- **Circuito dedicado de segurança** — alimentação do detector + válvula com fusível próprio, sempre energizado (não passa por chave geral).
- **Painel de status** — display no posto de pilotagem / galley com status verde/amarelo/vermelho do sistema.

### Tipos de sensor

- **Sensor catalítico / pellistor** — bolinha catalítica aquecida que oxida o gás; sinal proporcional; vida 3–5 anos; envenena por silicone/enxofre.
- **Sensor semicondutor MOS (metal-oxide semiconductor)** — SnO₂ aquecido muda resistência com gás; barato, mas falso-positivo em álcool, solventes.
- **Sensor IR (Infrared) dual-channel** — absorção de infravermelho por hidrocarboneto; caro, preciso, vida 10 anos; imune a envenenamento.
- **Sensor ultrassônico de vazamento** — detecta som de vazamento de pressão; raro em recreio.
- **Cross-sensitivity** — resposta errônea a gases não-alvo; cozinhar, álcool, aerosol pode disparar MOS.

### Calibração e teste

- **Calibração com gás padrão** — bomba ou ampola com concentração conhecida de propano/metano (ex: 50 % LEL); exige protocolo.
- **Zero calibration** — ajuste de ponto zero com ar limpo.
- **Span calibration** — ajuste de ganho com gás padrão.
- **Bump test** — teste de resposta (rápido) com gás padrão; não é calibração completa.
- **Bubble test (água + sabão)** — teste de vazamento em conexões com solução; vê bolhas formando.
- **Leak detection spray** — spray comercial equivalente ao sabão; mais prático.
- **Teste de pressão (pressure decay)** — fechar sistema, pressurizar, esperar 15 min; queda = vazamento.
- **Gas sniffer portátil** — detector portátil para varrer conexões e compartimentos; complementa o fixo.

### Aparelhos consumidores

- **Fogão marinho gimbaled** — fogão com suspensão cardan; mantém panela nivelada com balanço; ABYC A-27.
- **Forno marinho** — integrado ao fogão ou separado; válvula termocupla (se apaga a chama piloto, fecha o gás).
- **Churrasqueira / grill a GLP** — Magma, Dickinson, Kuuma; instalação na popa, lado; exige suporte estanque.
- **Aquecedor de água a gás (instant water heater)** — Paloma, Bosch marinho; exige exaustão dedicada e detector CO adjacente.
- **Cabin heater GLP (catalytic)** — aquecedor catalítico portátil; alta produção de CO se mal ventilado; desencorajado em cabine fechada.

### Alternativa elétrica

- **Fogão elétrico marinho (cooktop vitro-cerâmico / indução)** — alternativa sem risco de vazamento; exige shore power ou gerador + inverter.
- **Aquecedor de água elétrico** — calefator AC; alternativa ao gás; exige shore power.
- **Cabin heater elétrico (PTC / infrared)** — exige shore power ou gerador.

### Padrões e áreas classificadas

- **Área classificada Ex (zona 0/1/2)** — áreas com atmosfera potencialmente explosiva; equipamento precisa ser certificado Ex (IEC 60079).
- **Ignition protection** — construção de equipamento para não iniciar ignição (encapsulamento, pressurização, selagem); ABYC E-11 exige em compartimento de bateria e motor gasolina.
- **Intrinsically safe (i)** — equipamento intrinsecamente seguro; corrente/energia limitada a não iniciar ignição.
- **Explosion proof (d)** — invólucro robusto que contém explosão interna.
- **Pressurized (p)** — invólucro pressurizado com ar limpo.

### Padrões de referência citados

- **ABYC A-1** — padrão marinho americano LPG.
- **ISO 10239** — padrão internacional small craft LPG.
- **NFPA 58** — código LP USA.
- **EN 50194-1** — padrão europeu detector residencial.
- **IEC 60079-29-1** — padrão internacional detector gases inflamáveis.
- **NBR 13787** — padrão brasileiro central predial GLP.
- **NR-20** — regulamento trabalhista brasileiro.
- **INMETRO Portaria 27/2004** — regulamentação de equipamentos GLP no Brasil.

## FAQ

**Detector de GLP serve para gás natural?**

Não deve ser presumido. O gás, a sensibilidade e a posição de instalação podem ser diferentes.

**Posso instalar o sensor perto do fogão para ficar mais fácil?**

Nem sempre é a melhor posição. O sensor deve ser instalado onde o gás tende a se acumular em caso de vazamento, conforme o tipo de gás e o manual do sistema.

**Se tenho cheiro de gás, posso esperar o detector confirmar?**

Não. Cheiro de gás exige resposta imediata de segurança, independentemente do estado do alarme.

## Integração com outras notas

- [[Detector de CO — Monóxido de Carbono]]
- [[Sistema de Alarme Geral / Painel de Alarmes]]
- [[Extintor Automático — Combate a Incêndio na Casa de Máquinas]]
- [[Fogão - Cooktop Elétrico - Galley]]
- [[Blower]]

## Perguntas que esta nota responde

- Qual a diferença entre detector de GLP e detector de GN em embarcações?
- Onde o sensor deve ficar conforme o gás usado?
- Como integrar detector de gás com alarme e válvula de corte?
