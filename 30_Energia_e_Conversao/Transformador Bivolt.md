---
title: "Transformador Bivolt"
note_type: "technical-note"
domain: "30_Energia_e_Conversao"
source_file: "editorial-addition-2026-04-13"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "39"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
  - "internacional"
normas_citadas:
  - "ABYC E-11 (2023) — AC & DC Electrical Systems on Boats (shore power + isolation + bond N-PE)"
  - "ABYC A-22 — Marinas and Boatyards"
  - "ABYC E-4 — Lightning Protection (cross-ref)"
  - "ISO 13297:2020 — Small craft — Electrical systems — AC and DC"
  - "ISO 8846:2020 — Small craft — Electrical devices — Protection against ignition"
  - "IEC 60076-1:2011 — Power transformers — General"
  - "IEC 60076-5:2006 — Ability to withstand short circuit"
  - "IEC 60076-11:2018 — Dry-type transformers"
  - "IEC 60076-18 — Measurement of frequency response"
  - "IEC 61558-1:2017 — Safety of transformers, reactors, power supply units"
  - "IEC 61558-2-1 — Particular requirements for isolating transformers"
  - "IEC 61558-2-4 — Isolating transformers for general applications"
  - "IEC 60092-201 — Electrical installations in ships — System design"
  - "IEC 60092-301 — Equipment — Generators, converters, transformers"
  - "IEC 60092-352 — Cables for shipboard installations"
  - "UL 1561 — Dry-Type General Purpose and Power Transformers"
  - "UL 506 — Specialty Transformers"
  - "NEC Art. 250 — Grounding and Bonding"
  - "NEC Art. 450 — Transformers and Transformer Vaults"
  - "NEC Art. 555 — Marinas, Boatyards, Boat Basins"
  - "NBR 5410:2004 + emendas — Instalações elétricas de baixa tensão"
  - "NBR 5356-1/-2/-3 — Transformadores de potência"
  - "NBR 10295 — Transformadores de potência secos"
  - "NBR IEC 61558-1/-2 — Segurança de transformadores"
  - "INMETRO Portaria 637/2014 — Regulamentação de transformadores"
  - "ANEEL PRODIST Módulo 8 — Qualidade da energia (cross-ref)"
  - "DNV-RU-SHIP Pt 4 Ch 8 — Electrical installations"
  - "Lloyd's Register Rules Pt 6 — Electrical"
  - "EN 61558-1 — Safety of transformers"
  - "EN 61558-2-4 — Isolating transformers"
  - "CE-RCD Directive 2013/53/EU — Recreational Craft Directive"
  - "NORMAM-211/DPC — Esporte e recreio"
  - "NORMAM-201/204/DPC — Comercial / SMM"
  - "NFPA 302 — Pleasure and Commercial Motor Craft (shore power integration)"
review_level: "engineering-curated"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "Transformador shore power bivolt"
  - "Transformador de adaptação de marina"
  - "Bivolt náutico"
seo_title: "Transformador bivolt náutico: adaptação de tensão e topologia para marinas brasileiras"
seo_description: "Transformador bivolt náutico é a solução de adaptação mais séria quando a embarcação precisa operar entre marinas com tensões e topologias diferentes. A nota distingue autotransformador, transformador de isolamento, sistema derivado, neutro de saída, dimensionamento, falhas e critérios para aplicação segura."
seo_keywords:
  - "transformador bivolt barco"
  - "transformador 220 fase fase para fase neutro"
  - "shore power brasil"
  - "transformador de isolamento náutico"
  - "autotransformador náutico"
  - "30 Energia e Conversao"
geo_queries:
  - "Quando preciso de transformador bivolt em embarcação?"
  - "Como adaptar barco 220 fase-neutro para marina 220 fase-fase?"
  - "Qual a diferença entre autotransformador e transformador de isolamento no barco?"
related_notes:
  - "Aterramento"
  - "CAIS (Pier) (AC)"
  - "Fase e Neutro"
  - "Isolador Galvânico / Transformador de Isolamento"
  - "Normas e Regulamentações — Abyc Iso e Brasil"
  - "Proteção Dr"
  - "Transformador Entrada"
---

# Transformador Bivolt

> [!abstract] Resumo técnico
> "Transformador bivolt" é a expressão de campo usada para o equipamento que permite à embarcação operar entre marinas com tensões e topologias diferentes. Em projeto sério, isso precisa ser refinado: às vezes o problema é só tensão; às vezes é tensão + topologia; às vezes é topologia + isolamento galvânico. Por isso, o termo pode esconder três soluções diferentes: autotransformador, transformador de isolamento com taps múltiplos e conversão eletrônica de entrada. Para a realidade brasileira, a solução mais robusta costuma ser o equipamento que, além de adaptar a tensão, permite definir de forma previsível o sistema derivado de bordo.

> [!tip] Regra de decisão em 30 segundos
> 1. **"Bivolt" esconde TRÊS soluções distintas** — autotransformador (só adapta V), transformador de isolamento com taps (V + topologia + isolamento galvânico), ou entrada AC universal em equipamento específico (carregador, inverter); NÃO são intercambiáveis.
> 2. **Autotransformador ≠ isolação galvânica** — sem enrolamento primário e secundário separados fisicamente, o loop galvânico com a marina PERMANECE; vender autotransformador como "isolação" é fraude técnica.
> 3. **Brasil exige adaptar TOPOLOGIA + TENSÃO** — `220 V fase-fase` (marina) → `220 V fase-neutro` (barco) só com transformador de isolamento + sistema derivado documentado; autotransformador cria "neutro artificial" perigoso.
> 4. **Transformador de isolamento com taps múltiplos é a arquitetura mais robusta para trocar marinas no Brasil** — tap primário 120/208/220/230/240 V, secundário fixo 220 V f-n; define fronteira técnica clara.
> 5. **Dimensionamento em kVA (VA), NÃO watt** — somar carga contínua + motor inrush (3–6× running); margem 25%; ar-condicionado e compressor de pressurização dominam o pico.
> 6. **Bond neutro-PE DEVE existir no secundário APENAS quando sistema derivado é criado** — ponto ÚNICO, documentado no unifilar; NEC 250.30 + ABYC E-11 + IEC 61558-2-4; duplicar = corrente em PE + corrosão + ESD.
> 7. **DR/ELCI/RCD precisa enxergar a topologia da SAÍDA do transformador, não da entrada** — o diferencial mede soma vetorial dos condutores ativos do sistema ativo; reposicionar após o secundário quando sistema é derivado.
> 8. **Referências primárias: ABYC E-11 + IEC 61558-2-4 + NEC 450/555 + NBR IEC 61558 + INMETRO Portaria 637/2014** — classificadora exige IEC 60092-301 para comercial.
> 9. **Integração com gerador + inversor via ATS (Automatic Transfer Switch)** — ATS deve comutar N + L (4-pole) quando há bond N-PE em cada fonte; ATS 2-pole só serve quando neutro é comum.

> [!danger] Quando chamar engenheiro elétrico / surveyor
> 1. **Autotransformador vendido/instalado como "isolação" — risco de corrente galvânica persistente + perícia rejeitada** — desconstruir instalação; especificar transformador de isolamento IEC 61558-2-4 com laudo de dielétrico 4 kV RMS.
> 2. **Sistema derivado mal construído = bond N-PE duplicado = choque fatal em água (ESD)** — desligar TUDO + medição com miliohmímetro N vs PE no secundário + inspeção física + reprojeto de barramento; emergência antes de nova operação.
> 3. **Dimensionamento por watt (nameplate load) ignorando FP + inrush de motor** — aquecimento, isolação classe B (130°C) excedida, risco incêndio; recalcular em VA com fator de partida + termografia anual.
> 4. **Transformador instalado em compartimento fechado sem ventilação conforme UL 1561 / IEC 60076-11** — elevação térmica > classe de isolação; redução drástica de vida útil; ventilação forçada ou reinstalação em zona ventilada.
> 5. **Retrofit de transformador sem revisar barramento PE da embarcação** — loop galvânico subsistente; medição de tensão PE-casco + continuidade bonding + ajuste de arquitetura.
> 6. **Transfer switch ATS manual/automático errado (2-pole onde deveria ser 4-pole)** — múltiplos bonds N-PE simultâneos entre shore + gerador + inversor; NEC 250.30(A)(1) + ABYC E-11 10.2; substituir ATS por 4-pole com switching de neutro.
> 7. **Charter, aluguel ou escola náutica com transformador sem certificação INMETRO (Portaria 637/2014) ou sem laudo de ensaio dielétrico** — não conformidade; responsabilidade civil + recusa de apólice; laudo + rastreabilidade antes da operação.
> 8. **Embarcação americana 120/240 split-phase em marina brasileira 220 V sem projeto completo** — perigo de subdimensionamento + topologia errada; projeto técnico com transformador de isolamento step-up ou 1:1 + redesenho de barramento.
> 9. **Perícia pós-incêndio, choque em água ou sinistro com suspeita de falha do transformador** — preservar evidência: transformador inteiro (não desconectar), conexões, etiqueta de plaqueta, laudo classe de isolação se disponível; IBAPE + Abracem + IEC 60076-1 análise térmica.

## O que é

Transformador bivolt, no vocabulário náutico brasileiro, é o equipamento instalado na interface de shore power para permitir que a embarcação receba energia de marinas diferentes sem depender de uma única combinação fixa de tensão e topologia.

Tecnicamente, ele pode assumir três formas:

1. **autotransformador**: adapta tensão, mas não isola galvanicamente;
2. **transformador de isolamento com taps ou primários configuráveis**: adapta tensão e cria separação elétrica;
3. **equipamento com entrada AC universal**: resolve parte da faixa de tensão, mas não substitui o tratamento da topologia da entrada.

## Por que ele ficou crítico no Brasil

A realidade brasileira é particularmente hostil para soluções simplistas porque:

- o mesmo barco pode sair de uma região acostumada a `220 V fase-neutro` e ir operar em marina com `220 V fase-fase`;
- muitos pedestais são mal documentados;
- parte do mercado replica filosofias estrangeiras sem revalidar a alimentação local;
- o problema não é apenas "quanto volts chegam", e sim **como esses volts chegam**.

Em outras palavras: o transformador bivolt passa a ser peça de arquitetura, não acessório.

## Quando ele é necessário

| Situação | Transformador bivolt faz sentido? | Observação |
| --- | --- | --- |
| Barco projetado para `220 V fase-neutro` operando em marina `220 V fase-fase` | sim, fortemente recomendado | sem sistema derivado correto, o risco de neutralização artificial é alto |
| Barco americano `120/240 split-phase` em marina brasileira `220 V` | sim, quase sempre | o problema envolve tensão e filosofia de distribuição |
| Barco brasileiro `220 V` visitando marina `120 V` | sim, se houver cargas que exijam 220 V real | avaliar também demanda e potência total |
| Embarcação com apenas carregadores/fonte universal na entrada | talvez não para todas as cargas | entrada universal não resolve ar-condicionado, tomadas e rede AC inteira |
| Marina de infraestrutura duvidosa, com alta incidência de corrosão e falhas de PE | sim, preferindo versão com isolamento | aqui o ganho é tensão + topologia + isolamento |

## O que ele resolve e o que ele não resolve

| Tema | Resolve? | Observação |
| --- | --- | --- |
| Adaptação de tensão | sim | desde que a potência nominal seja adequada |
| Adaptação de topologia | depende do tipo | autotransformador sozinho não cria sistema derivado isolado |
| Criação de neutro funcional previsível | depende do tipo e do projeto | só existe quando a solução realmente define esse ponto na saída |
| Isolamento galvânico da marina | só com transformador de isolamento | autotransformador não entrega esse benefício |
| Correção de frequência | não | frequência exige conversão eletrônica específica |
| Correção de fiação errada do barco | não | equipamento não substitui revisão de arquitetura |
| Cura de PE ruim ou pedestal perigoso | parcialmente | melhora a fronteira técnica, mas não autoriza uso cego de marina defeituosa |

## Tipos reais de "transformador bivolt"

### 1. Autotransformador bivolt

Usa enrolamento comum e taps para elevar ou reduzir tensão.

Vantagens:

- menor peso;
- custo menor;
- boa eficiência;
- útil quando o problema é predominantemente tensão.

Limitações:

- não há separação galvânica;
- não quebra o vínculo elétrico com a marina;
- não deve ser vendido como solução completa quando o problema também é neutralização e corrosão.

### 2. Transformador de isolamento bivolt

Tem primário e secundário separados eletricamente e pode oferecer taps ou combinação de primários para diferentes tensões de entrada.

Vantagens:

- cria barreira elétrica entre marina e bordo;
- permite sistema derivado previsível na saída;
- é a solução mais robusta para o cenário brasileiro de topologias variáveis.

Limitações:

- custo e peso maiores;
- volume relevante;
- exige ventilação, fixação e coordenação de proteção corretas.

### 3. Entrada AC universal em equipamento específico

Alguns inversores-carregadores e carregadores modernos aceitam faixa ampla de entrada AC.

Vantagens:

- simplificam alguns cenários de carga de bateria;
- podem dispensar transformador dedicado para determinadas cargas eletrônicas.

Limitações:

- não resolvem a rede AC inteira da embarcação;
- não corrigem, sozinhos, o problema de um barco concebido para `L + N + PE` conectado a `L1 + L2 + PE`.

## O ponto decisivo: saída previsível

O bom transformador bivolt não é o que "faz funcionar". É o que **entrega uma saída de bordo tecnicamente previsível**.

Isso significa definir:

- quais condutores ativos existirão na saída;
- se haverá neutro funcional ou não;
- onde ficará o bond neutro-PE, se aplicável;
- como o DR / ELCI / RCD será instalado;
- como essa fonte conversará com gerador e inversor.

## Matriz de topologias típicas

| Entrada da marina | Saída desejada no barco | Tipo mais adequado | Comentário |
| --- | --- | --- | --- |
| `220 V fase-fase + PE` | `220 V fase-neutro + PE` | transformador de isolamento/bivolt com sistema derivado documentado | cenário clássico de correção de topologia |
| `220 V fase-neutro + PE` | `220 V fase-neutro + PE` | 1:1 com ou sem isolamento, conforme objetivo | se o objetivo for só isolamento, usar transformador de isolamento 1:1 |
| `120/240 split-phase` | `220/230 V monofásico de bordo` | solução dedicada de adaptação com projeto claro | exige análise detalhada de cargas |
| `120 V` | `220 V` | step-up/autotransformador ou isolamento com taps | depende de necessidade de isolamento |
| `220 V` | `120 V` | step-down/autotransformador ou isolamento com taps | atenção à corrente na saída |

## Transformador bivolt versus transformador de entrada

| Critério | Transformador Entrada | Transformador Bivolt |
| --- | --- | --- |
| Foco principal | adaptar nível de tensão | adaptar tensão e, frequentemente, topologia operacional entre marinas |
| Pode ser portátil ou simples | sim | pode, mas a solução séria tende a ser fixa e documentada |
| Precisa tratar neutralização | às vezes não | quase sempre, no contexto brasileiro |
| É sinônimo de isolamento | não | não, mas na prática o tipo isolado costuma ser o mais robusto |

## Transformador bivolt versus transformador de isolamento

| Critério | Autotransformador bivolt | Transformador de isolamento bivolt |
| --- | --- | --- |
| Isolamento galvânico | não | sim |
| Sistema derivado a bordo | limitado | sim, quando projetado |
| Controle de corrosão/corrente vagante | limitado | muito melhor |
| Robustez para marinas ruins | média/baixa | alta |
| Peso e custo | menores | maiores |

## Dimensionamento

O transformador precisa ser dimensionado pela **potência aparente** e pela **natureza das cargas**, não pela soma ingênua dos watts de plaqueta.

### Critérios mínimos

- levantar a potência simultânea plausível das cargas AC;
- considerar partidas de compressor, bombas e outros motores;
- prever margem térmica e de expansão;
- checar corrente de entrada e de saída na pior condição;
- coordenar disjuntores e proteção diferencial dos dois lados.

### Regra prática conservadora

Para cargas mistas de bordo, trabalhar com margem acima da carga simultânea prevista é prudente. Em aplicações com ar-condicionado, bombas, aquecimento e tomadas, subdimensionar o transformador costuma gerar aquecimento, queda de tensão e falsa impressão de "problema na marina".

## Bond neutro-PE e sistema derivado

Esse é o coração da nota.

Se o transformador bivolt for também um transformador de isolamento, ele permite ao projetista definir um sistema derivado na saída. A partir daí:

- o neutro de saída, se existir, deve ser criado **no secundário**;
- o bond neutro-PE deve existir **no ponto único previsto** para essa saída;
- esse bond não pode ser confundido com ligação indiscriminada entre entrada do cais, negativo DC e bonding;
- o DR deve enxergar os condutores ativos corretos do sistema derivado.

Se o equipamento for apenas autotransformador, não existe essa fronteira limpa. Nesse caso, adaptação de tensão não deve ser vendida como neutralização resolvida.

## Integração com DR, PE, gerador e inversor

Um transformador bivolt bem aplicado só funciona quando conversa com o resto do sistema:

- **DR/RCD/ELCI**: precisa ser posicionado de acordo com a fonte ativa e a topologia efetiva monitorada;
- **PE**: precisa manter função de proteção, não retorno operacional;
- **gerador**: a transferência entre fontes não pode criar múltiplos bonds nem neutros paralelos;
- **inversor**: alguns equipamentos comutam neutro ou usam relé de ground; isso precisa ser compatibilizado.

## Diagnóstico prático

### Sinais de que a solução atual está errada

- barco funciona em uma marina e enlouquece em outra;
- DR dispara apenas em certos pedestais;
- aparece tensão anormal entre barramentos, chassis e PE;
- carregador, automação ou módulos eletrônicos falham após mudança de marina;
- barramento de neutro aparece interligado a negativo DC e bonding sem diagrama claro.

### Ensaios mínimos

1. medir tensão entre condutores de entrada;
2. medir relação de cada condutor de entrada com PE;
3. confirmar a topologia da saída do transformador;
4. identificar onde está o bond neutro-PE do sistema ativo;
5. verificar seletividade e posição do DR;
6. revisar a lógica de transferência entre shore, gerador e inversor.

## Marcas e referências

### Fabricantes internacionais conhecidos

- **Victron Energy**: autotransformer e isolation transformer, forte documentação técnica;
- **Mastervolt**: soluções premium integradas para shore power e power conversion;
- **Charles Industries**: tradição em transformadores marinhos e galvanic isolators;
- **ASEA Power Systems**: forte presença em iates maiores e shore conversion de alto padrão;
- **Toroid / fabricantes especializados equivalentes**: soluções compactas para casos específicos.

### Fabricantes sob encomenda e soluções locais

No Brasil há transformadores sob encomenda e montagens locais. Eles podem funcionar muito bem, desde que o fornecedor entregue:

- diagrama de ligação;
- classe de isolamento;
- elevação térmica;
- ensaio dielétrico;
- tensão nominal, taps e corrente nominal claros;
- instruções explícitas sobre neutralização e PE.

Sem isso, o equipamento vira caixa pesada sem rastreabilidade.

## Boas práticas profissionais

- definir no unifilar a topologia aceita na entrada da marina e a topologia entregue ao barco;
- preferir solução com isolamento quando a embarcação circular entre marinas de padrão incerto;
- etiquetar fisicamente entrada e saída como `L1`, `L2`, `N`, `PE` conforme a função real;
- documentar onde fica o bond neutro-PE do sistema ativo;
- impedir múltiplas referências simultâneas entre shore, gerador, inversor e secundário;
- revisar o projeto inteiro de entrada AC ao instalar o transformador, não apenas encaixar o equipamento.

## Erros comuns

**Comprar autotransformador e achar que ganhou isolamento:**

Não ganhou.

**Instalar transformador e manter a arquitetura errada do barramento:**

Se o barramento de neutro continuar artificialmente amarrado ao universo errado, o problema muda de forma, mas não desaparece.

**Dimensionar por carga "normal" e ignorar pico:**

É o caminho mais curto para aquecimento e queima prematura.

**Não documentar a saída:**

Sem diagrama, o próximo técnico não sabe se está diante de `L + N + PE`, `L1 + L2 + PE` ou sistema derivado.

**Usar o transformador para mascarar pedestal perigoso:**

Marina ruim continua exigindo cautela, medição e inspeção.

## Relação com outras notas

- [[CAIS (Pier) (AC)]]
- [[Fase e Neutro]]
- [[Transformador Entrada]]
- [[Isolador Galvânico / Transformador de Isolamento]]
- [[Aterramento]]
- [[Proteção Dr]]
- [[Normas e Regulamentações — Abyc Iso e Brasil]]

## Normas aplicáveis (organizadas por família)

Transformador bivolt cruza quatro áreas normativas: **shore power marinho** (ABYC E-11, NEC 555, ISO 13297), **transformador propriamente dito** (IEC 60076, 61558, UL 1561, NBR 5356), **embarcação comercial** (IEC 60092, classificadoras), **jurisdição brasileira** (NBR 5410, INMETRO, ANEEL).

### ABYC (recreio USA) — referência técnica dominante

- **ABYC E-11 (2023) — AC & DC Electrical Systems on Boats** — norma central; Seção 10 (shore power) + Seção 11 (isolation transformer) cobrem dimensionamento, bond N-PE no secundário, proteção ELCI, identificação.
- **ABYC A-22 — Marinas and Boatyards** — exigências do lado da marina; ELCI no pedestal, aterramento do cais.
- **ABYC E-4 — Lightning Protection** — proteção contra descarga atmosférica; DPS na entrada do transformador.

### ISO (pequena embarcação internacional)

- **ISO 13297:2020 — Small craft — Electrical systems — AC and DC** — obrigatório para certificação CE.
- **ISO 8846:2020 — Small craft — Electrical devices — Protection against ignition** — proteção de ignição em compartimento com vapor combustível.

### IEC (transformador propriamente dito — referência técnica universal)

- **IEC 60076-1:2011 — Power transformers — General** — norma guarda-chuva; terminologia, classificação, requisitos gerais.
- **IEC 60076-5:2006 — Ability to withstand short circuit** — capacidade de suportar curto; ensaio mecânico.
- **IEC 60076-11:2018 — Dry-type transformers** — transformador seco (sem óleo); maioria dos bivolt marinhos.
- **IEC 60076-18 — Measurement of frequency response** — diagnóstico por resposta em frequência (FRA).
- **IEC 61558-1:2017 — Safety of transformers, reactors, power supply units** — segurança; requisitos dielétricos, térmicos, construtivos.
- **IEC 61558-2-1 — Particular requirements for isolating transformers** — transformador de isolamento geral.
- **IEC 61558-2-4 — Isolating transformers for general applications** — específico para isolação; referência primária para "isolation transformer" marinho.

### IEC marítimo (comercial)

- **IEC 60092-201 — System design** — arquitetura elétrica em navio comercial.
- **IEC 60092-202 — System design — Protection** — proteção elétrica, incluindo transformadores.
- **IEC 60092-301 — Equipment — Generators, converters, transformers** — requisitos específicos para transformador em navio.
- **IEC 60092-352 — Cables for shipboard installations** — cabos de alimentação.
- **IEC 60092-502 — Tankers** — requisitos adicionais para navios petroleiros (cross-ref).

### UL (certificação USA)

- **UL 1561 — Dry-Type General Purpose and Power Transformers** — certificação USA padrão.
- **UL 1562 — Distribution Dry-Type Transformers — Over 600 V** — alta tensão.
- **UL 506 — Specialty Transformers** — transformadores especiais, incluindo pequenos.

### NEC (USA — instalação)

- **NEC Art. 250 — Grounding and Bonding** — Seção 250.30 específica para sistemas derivados separadamente.
- **NEC Art. 450 — Transformers and Transformer Vaults** — instalação de transformadores em edificação.
- **NEC Art. 555 — Marinas, Boatyards, Boat Basins** — instalação do pedestal; ELCI obrigatório 2017+.

### Brasil (normas técnicas)

- **NBR 5410:2004 + emendas — Instalações elétricas de baixa tensão** — norma guarda-chuva BT Brasil; aplica-se ao lado AC do barco.
- **NBR 5356-1/-2/-3 — Transformadores de potência** — especificação de transformador de potência BT.
- **NBR 10295 — Transformadores de potência secos** — transformador seco (sem óleo).
- **NBR IEC 61558-1/-2 — Segurança de transformadores** — adoção brasileira de IEC 61558.
- **INMETRO Portaria 637/2014 — Regulamentação de transformadores** — certificação compulsória no Brasil.
- **ANEEL PRODIST Módulo 8 — Qualidade da energia** — referência para qualidade (cross-ref para marinas com QualidadeEnergia ruim).

### Sociedades classificadoras (comercial)

- **DNV-RU-SHIP Pt 4 Ch 8 — Electrical installations** — regras DNV para instalação elétrica.
- **Lloyd's Register Rules Pt 6 — Electrical** — regras LR.
- **ABS Steel Vessel Rules Pt 4 Ch 8** — regras ABS.
- **Bureau Veritas NR 467 Pt C Ch 2** — regras BV para instalação elétrica.

### Europa (RCD)

- **EN 61558-1 — Safety of transformers** — adoção europeia de IEC 61558.
- **EN 61558-2-4 — Isolating transformers** — adoção europeia.
- **CE-RCD Directive 2013/53/EU — Recreational Craft Directive** — exige conformidade a ISO 13297 + EN 61558.

### Brasil (marítimo)

- **NORMAM-211/DPC — Esporte e recreio** — regulamento DPC recreio.
- **NORMAM-201/204/DPC — Comercial / SMM** — comercial classificada.

### Proteção contra incêndio (USA)

- **NFPA 302 — Pleasure and Commercial Motor Craft** — integração do transformador ao sistema de proteção.
- **NFPA 70 (NEC)** — código elétrico nacional.

### Como usar este conjunto normativo na prática

| Situação | Norma-chave |
|---|---|
| Projeto recreio USA | ABYC E-11 + NEC 555 + UL 1561 + NFPA 302 |
| Projeto recreio Brasil | ABYC E-11 + NBR IEC 61558 + INMETRO Portaria 637 |
| Projeto comercial classificado | IEC 60092-201/301 + classificadora |
| Certificação CE Europa | EN 61558 + RCD |
| Sistema derivado separadamente | NEC 250.30 + ABYC E-11 10.x + IEC 61558-2-4 |
| Fabricante sob encomenda Brasil | NBR 5356 + NBR 10295 + laudo INMETRO |
| Retrofit marina brasileira | NBR 5410 + ABYC E-11 + laudo técnico CREA |
| Perícia pós-incêndio | IEC 60076-18 (FRA) + IBAPE + NR-10 |
| Integração ATS shore+gerador+inverter | NEC 250.30 + ABYC E-11 + fabricante ATS |
| Ensaio dielétrico | IEC 61558-1 Seção 18 + NBR 5356-3 |

## Glossário rápido

### Tipos de transformador

- **Autotransformador (autotransformer)** — um único enrolamento com derivações (taps); sem isolação galvânica; mais leve e barato; NÃO cria sistema derivado.
- **Transformador de duplo enrolamento (dual-winding / two-winding)** — primário e secundário fisicamente separados; isolação galvânica; padrão IEC 61558-2-1/-2-4.
- **Transformador de isolamento (isolation transformer)** — transformador de duplo enrolamento 1:1 ou com taps; dedicado a criar barreira elétrica entre duas redes.
- **Transformador bivolt** — expressão de campo; pode ser auto ou isolação, com taps para tensões de entrada diferentes.
- **Toroidal transformer** — núcleo toroidal; baixa radiação eletromagnética + alta eficiência; comum em marinho premium.
- **E-I core (laminado)** — núcleo E-I tradicional; mais barato, mais ruidoso, maior fluxo de fuga.
- **Shell type / core type** — topologia construtiva do núcleo.
- **Dry-type transformer (seco)** — sem óleo refrigerante; padrão em marinho por segurança de fogo.
- **Oil-filled transformer** — com óleo mineral refrigerante; NÃO usado em marinho.
- **Cast resin transformer** — resina epóxi encapsulada; alta isolação; premium.

### Topologia e sistema derivado

- **Sistema derivado separadamente (separately derived system)** — NEC 250.30; sistema onde o secundário do transformador cria nova referência de terra/neutro.
- **Bond neutro-PE (N-PE bond)** — conexão ÚNICA entre neutro e proteção; no secundário do transformador quando sistema é derivado.
- **Ponto único de aterramento** — localização onde todos os referenciais convergem; crítico para evitar loops.
- **Service entrance** — ponto de entrada de energia; onde o transformador da concessionária entrega ao consumidor.
- **Sistema TN-S / TT / IT** — classificação IEC 60364 de sistemas de aterramento; determina onde o DR atua.
- **Ground fault circuit interrupter (GFCI)** — disjuntor diferencial 5 mA (tomadas).
- **Equipment Leakage Circuit Interrupter (ELCI)** — disjuntor diferencial 30 mA marinho; ABYC E-11.
- **RCD (Residual Current Device)** — nomenclatura europeia para diferencial.
- **ESD (Electric Shock Drowning)** — choque elétrico fatal em água; fuga AC > 30 mA.

### Parâmetros do transformador

- **kVA (potência aparente)** — produto V × I; dimensionamento correto em CA.
- **Watt (potência ativa)** — V × I × cos φ; NÃO usar para dimensionar transformador.
- **Fator de potência (power factor, cos φ)** — ângulo entre V e I; define relação kW/kVA.
- **Inrush current (corrente de partida)** — pico na energização; 3–10× nominal durante 50–200 ms.
- **Locked rotor current (corrente de rotor bloqueado)** — motor parado; 6–8× corrente nominal.
- **Rated voltage (tensão nominal)** — V nominal do enrolamento.
- **Tap (derivação)** — conexão intermediária do enrolamento; ± 2,5 %, ± 5 % típicos.
- **Voltage regulation (regulação)** — queda de V da vazio para plena carga; idealmente < 5 %.
- **Impedance (Z %)** — impedância percentual; típica 2–6 % para transformadores de distribuição.
- **Short-circuit impedance** — impedância vista do secundário com primário em curto; define corrente de curto.

### Parâmetros térmicos e de isolação

- **Class of insulation** — classe de isolação térmica; A (105 °C), B (130 °C), F (155 °C), H (180 °C), N (200 °C).
- **Temperature rise (elevação térmica)** — diferença entre temperatura do enrolamento e ambiente; classe B permite elevação 80–90 °C sobre ambiente 40 °C.
- **Hot spot temperature** — ponto mais quente do enrolamento; limite da classe.
- **Ambient temperature rating** — temperatura ambiente de projeto; tipicamente 40 °C IEC, 30 °C UL.
- **Altitude derating** — redução de capacidade em altitude > 1000 m (menos densidade de ar = menos convecção).
- **Cooling class** — natural AN (air natural), AF (air forced), ON (oil natural), OF (oil forced).
- **Magnetostriction (noise / ruído)** — vibração do núcleo em 100/120 Hz; causa hum audível.

### Ensaios e certificação

- **Dielectric test (ensaio dielétrico)** — aplicação de tensão > nominal para verificar isolação; típico 2,5× + 1 kV RMS durante 1 min.
- **Voltage withstand** — tensão que o equipamento suporta sem falha.
- **BIL (Basic Insulation Level)** — tensão de impulso 1,2/50 μs; capacidade de surto.
- **SWC (Surge Withstand Capability)** — capacidade a surto.
- **FRA (Frequency Response Analysis)** — diagnóstico por resposta em frequência (IEC 60076-18); detecta deformação mecânica.
- **No-load loss (perdas a vazio)** — perdas no núcleo (hysteresis + eddy current); constantes.
- **Load loss (perdas em carga)** — perdas em enrolamento (I²R); proporcional a carga².
- **Eficiência** — razão potência de saída / potência de entrada; tipicamente 95–99 %.
- **K-factor** — fator K para harmônicos; K-13, K-20 para cargas não-lineares (LEDs, inverters).

### Construção

- **Winding (enrolamento)** — espiras de cobre (ou alumínio) em torno do núcleo.
- **Primary winding (primário)** — enrolamento de entrada (alta tensão em step-down).
- **Secondary winding (secundário)** — enrolamento de saída.
- **Copper winding** — cobre; padrão premium; melhor condutividade.
- **Aluminum winding** — alumínio; mais barato, mais leve; exige seção maior.
- **Faraday shield (tela eletrostática)** — tela metálica entre primário e secundário; reduz acoplamento capacitivo; ausente em autotransformador.
- **Core (núcleo)** — aço-silício laminado; concentra fluxo magnético.
- **Saturation (saturação)** — ponto onde o núcleo não responde linearmente a H; limite superior.
- **B-H curve (curva de magnetização)** — relação densidade de fluxo vs campo magnético.

### Integração com a arquitetura

- **Automatic Transfer Switch (ATS)** — chave automática de transferência entre fontes (shore/gerador).
- **2-pole ATS** — chaveia apenas L; neutro é comum; simples, mas limita arquiteturas.
- **4-pole ATS** — chaveia L + N; necessário quando há bond N-PE em cada fonte.
- **Hardwired neutral** — neutro direto sem chaveamento.
- **Switched neutral** — neutro comutado no ATS.
- **Phase synchronization** — sincronização de fase antes de fechar ATS; evita contracorrente.
- **Zero-crossing switching** — comutação em zero crossing; reduz arc.

### Jurisdições e padrões citados

- **ABYC E-11** — padrão americano AC/DC marinho (Seção 11 = isolation transformer).
- **IEC 61558-2-4** — padrão internacional específico de isolation transformer.
- **NEC 250.30** — seção específica de sistema derivado separadamente.
- **UL 1561** — certificação USA padrão.
- **NBR 5356** — padrão brasileiro transformador de potência.
- **INMETRO Portaria 637/2014** — certificação compulsória Brasil.
- **DNV-RU-SHIP** — regras DNV para navio.
- **IEC 60092-301** — regras IEC para comercial.

## Perguntas que esta nota responde

- O que é um transformador bivolt náutico?
- Transformador bivolt e transformador de entrada são a mesma coisa?
- Em que cenário ele é indispensável no Brasil?
- Ele resolve tensão, topologia ou os dois?
- Autotransformador serve para esse problema?
- Autotransformador isola a embarcação da marina?
- Quando preciso de transformador de isolamento em vez de autotransformador?
- Como adaptar barco 220 fase-neutro para marina 220 fase-fase?
- Como adaptar barco americano ao padrão brasileiro?
- O transformador cria neutro automaticamente?
- Onde o bond neutro-PE deve ficar?
- Como o DR deve ser pensado com esse equipamento?
- O que acontece se eu mantiver barramento de neutro errado?
- Ele corrige frequência?
- Como dimensionar em kVA?
- Como considerar partida de ar-condicionado e motores?
- Quais marcas sérias existem nesse segmento?
- O que exigir de um fabricante sob encomenda?
- O que precisa estar no unifilar após a instalação?
- Como integrar shore power, gerador e inversor?
- Quais sintomas mostram que a solução atual está errada?
- Como diferenciar problema de pedestal ruim e problema do barco?
- Qual é a arquitetura mais robusta para uso entre regiões do Brasil?
