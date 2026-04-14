---
title: "Transformador Bivolt"
note_type: "technical-note"
domain: "30_Energia_e_Conversao"
source_file: "editorial-addition-2026-04-13"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
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
