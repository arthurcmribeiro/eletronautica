---
title: "Aterramento"
note_type: "technical-note"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "ATERRAMENTO 62019734f7fb83ed822d818740bfe4cb.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "ATERRAMENTO"
seo_title: "Aterramento"
seo_description: "Aterramento em embarcações é o arranjo de referência e proteção que conecta condutores de proteção, massas expostas e pontos de referência do sistema AC/DC conforme a topologia da instalação. O maior erro é tratar negativo DC, PE e bonding como se fossem o mesmo circuito."
seo_keywords:
  - "Aterramento"
  - "40 Distribuicao Protecao e Aterramento"
geo_queries:
  - "O que é Aterramento em instalações elétricas náuticas?"
  - "Qual é a função de Aterramento na embarcação?"
related_notes:
  - "CAIS (Pier) (AC)"
  - "Barramento DC / Bus Bar / Distribuição DC"
  - "Bonding — Sistema de Interligação de Massas"
  - "Cabeamento Náutico"
  - "Chaves Gerais (DC)"
  - "Chaves Seletoras (AC)"
  - "Contatores (AC)"
  - "Disjuntores (DC) e (AC)"
  - "Divisores de Carga (DC)"
  - "Isolador Galvânico / Transformador de Isolamento"
  - "Neutro, Negativo, Terra, PE, Bonding e DR — Diferenças Críticas"
  - "Transformador Bivolt"
  - "Proteção Dr"
---

# Aterramento

> [!abstract] Resumo técnico
> Aterramento, em contexto náutico, é o arranjo de condutores de proteção, pontos de referência e equipotencialização que controla tensões de toque e permite a atuação correta das proteções. Negativo DC, PE do sistema AC e bonding podem se relacionar, mas não são sinônimos e não devem ser interligados de forma arbitrária.

## O que é

Aterramento é o conjunto de conexões que estabelece a referência de potencial zero do sistema elétrico e protege contra choque elétrico. Em embarcações, o conceito se divide em três sistemas distintos que coexistem mas **não devem ser interligados indiscriminadamente**:

- **Negativo DC** — referência do sistema de corrente contínua (baterias, painéis, cargas 12/24V)
- **Terra AC (Safety Ground)** — fio verde ou verde/amarelo do sistema de corrente alternada (proteção contra choque)
- **Bonding** — interligação de massas metálicas para proteção contra corrosão galvânica

A separação correta entre esses três sistemas é fundamental para segurança e proteção da embarcação.

## Função

| Sistema | Função principal |
| --- | --- |
| Negativo DC | Referência de tensão para todo o sistema 12/24V |
| Terra AC | Derivar corrente de falha ao corpo, protegendo o operador |
| Bonding | Equalizar potencial entre massas metálicas submersas |

O aterramento AC é especialmente crítico: sem ele, uma falha de isolação em qualquer equipamento 220V coloca tensão na carcaça — risco de choque fatal.

## Como aparece na prática

- Cabo preto (negativo DC) indo do banco de baterias ao barramento negativo
- Cabo verde/amarelo conectando carcaças de equipamentos AC ao ponto de terra
- Barra de aterramento (ground bus) no painel elétrico
- Ponto único de aterramento (SPOG — Single Point of Grounding)
- Cabo de bonding interligando motor, tanque de combustível, quilha e acessórios metálicos

## Fundamentos mínimos

**Separar função, referência e equipotencialização:**

- **Negativo DC** é o retorno funcional dos circuitos em corrente contínua.
- **PE / terra AC** é o condutor de proteção das massas expostas do sistema AC.
- **Bonding** é a malha de equipotencialização e proteção contra corrosão galvânica entre partes metálicas selecionadas.

Esses sistemas podem convergir em um ponto de referência definido pela arquitetura elétrica da embarcação, mas a localização e a forma dessa convergência dependem da fonte ativa: shore power, gerador, inversor ou transformador de isolamento.

**Bond de neutro e terra não é livre:**

Em AC, a ligação entre neutro e condutor de proteção só pode existir no ponto previsto pela topologia do sistema e pela norma aplicável. Em sistemas alimentados do cais, esse vínculo normalmente já existe no lado da origem ou em arranjo derivado corretamente projetado. Em sistemas derivados a bordo, como gerador, inversor com neutro comutado ou secundário de transformador de isolamento, esse vínculo precisa ser tratado de forma explícita e única. Fazer esse bond em múltiplos pontos cria circulação indevida de corrente no PE e no bonding.

Aplicação direta para a realidade brasileira: se a embarcação recebe `220 V` entre dois condutores ativos e `PE`, não existe neutro funcional entregue na entrada. Portanto, não é admissível amarrar um desses ativos ao `PE`, ao negativo DC ou ao barramento de bonding para "fabricar" neutro. Se o projeto precisa de neutro a bordo, isso deve nascer de um sistema derivado corretamente definido, como o secundário de um [[Transformador Bivolt]]/transformador de isolamento.

**Objetivo do condutor de proteção:**

Quando uma falha energiza a carcaça de um equipamento, o PE oferece um caminho de baixa impedância para a corrente de falha e reduz a tensão de toque, permitindo a atuação de disjuntores, fusíveis e dispositivos diferenciais/leakage. Sem continuidade adequada do PE, a carcaça pode permanecer energizada mesmo com a instalação "funcionando".

**Baixa impedância é mais importante que um número isolado:**

Em inspeção de campo, o foco deve ser continuidade confiável, conexões íntegras, baixa impedância do caminho de falha e coerência com a norma da embarcação. Um único valor de resistência não substitui a verificação da arquitetura completa, das conexões e da capacidade de atuação das proteções.

## Características

| Parâmetro | Valor típico |
| --- | --- |
| Bitola mínima terra AC | Igual ao condutor de fase |
| Resistência máxima (ABYC) | ≤ 1 Ω |
| Cor terra AC | Verde ou verde/amarelo |
| Cor negativo DC | Preto (12V) ou amarelo (negativo de retorno) |
| Ponto de conexão | SPOG — único ponto de interligação |

## Configurações comuns

**Embarcações somente DC (muito comum no Brasil):**

- Sistema mais simples: apenas negativo DC e bonding
- Risco menor de choque, mas corrosão galvânica ainda presente
- Sem shore power: ausência de terra AC não é problema imediato

**Embarcações com shore power (comum em barcos importados):**

- PE obrigatório e protegido desde a entrada AC
- Verificação de polaridade, continuidade do PE e dispositivo diferencial/leakage deixam de ser opcionais
- O arranjo ideal inclui proteção diferencial/leakage e, quando aplicável, isolador galvânico ou transformador de isolamento

**Embarcações com gerador (mais presente em embarcações maiores/premium):**

- O gerador pode constituir uma fonte derivada a bordo, exigindo tratamento correto do vínculo neutro-PE
- Chave de transferência ou intertravamento é obrigatório para impedir paralelismo indevido com o shore power
- O ponto de referência do gerador deve ser documentado no diagrama do barco

## Marcas e referências

- **Blue Sea Systems** — barras de aterramento, conectores, SPOG kits
- **Victron Energy** — barras de distribuição com terra integrado
- **Marinco / Hubbell** — conectores shore power com terra certificado
- **Paneltronics** — painéis com barra de terra dedicada
- **Ancor** — cabos e terminais para sistemas de terra marítimos

## Componentes relacionados

- Barra de aterramento (ground bus bar)
- Transformador de isolamento
- GFCI / disjuntor diferencial
- Sistema de bonding
- Pedestal de marina com terra
- Cabo shore power (3 condutores: fase, neutro, terra)

## Problemas mais frequentes

| Problema | Sintoma | Gravidade |
| --- | --- | --- |
| Terra AC ausente | Choque ao tocar equipamentos | Crítico |
| Terra interligado ao negativo DC em múltiplos pontos | Loop de corrente, corrosão acelerada | Alto |
| Marina sem terra no pedestal | Terra AC flutuante | Alto |
| Resistência alta no terra | Proteção ineficaz | Alto |
| Carcaça de equipamento sem terra | Choque silencioso | Crítico |
| Confusão entre negativo DC e terra AC | Curtos, queima de equipamentos | Alto |

## Causas raiz

**Terra AC ausente:**

Instalações improvisadas sem conhecimento de elétrica náutica. Técnicos de terra transferindo práticas de instalações prediais sem adaptação.

**Loop de terra:**

Múltiplos pontos de interligação entre negativo DC e terra AC criam loops onde circulam correntes parasitas, acelerando corrosão galvânica e gerando interferência.

**Marina sem terra:**

Infraestrutura precária. Pedestais antigos no Brasil frequentemente têm apenas fase e neutro — terra é fio sem conexão no pedestal.

**Alta resistência:**

Terminais oxidados, conexões frouxas ou cabo subdimensionado. A resistência aumenta com o tempo sem manutenção.

## Diagnóstico prático

**Verificar presença e coerência do circuito de proteção AC:**

```jsx
Multímetro → modo VAC
Medir fase-neutro → tensão nominal do sistema
Medir fase-PE → deve ser compatível com fase-neutro
Medir neutro-PE → pequeno desvio pode existir sob carga
Desvios elevados ou instáveis exigem investigação da topologia e do pedestal
```

**Verificar continuidade do PE com a instalação desenergizada:**

```jsx
Desligar e bloquear as fontes AC
Confirmar ausência de tensão
Medir continuidade entre o barramento de proteção e as carcaças metálicas relevantes
Qualquer ponto sem continuidade consistente exige correção imediata
```

**Verificar ligação indevida entre neutro e PE:**

```jsx
Com todas as fontes AC isoladas
Conferir em diagrama onde o bond neutro-PE deveria existir
Medir se há continuidade neutro-PE fora do ponto previsto
Múltiplos pontos de continuidade indicam bond indevido ou equipamento ligado de forma errada
```

**Verificar corrente de fuga/corrente indevida no PE:**

```jsx
Alicate miliamperímetro no PE do shore power
Medir com cargas normais e depois circuito a circuito
Corrente persistente no PE deve ser interpretada junto com a topologia e com a proteção diferencial
Valores anormais pedem investigação de fuga, bond neutro-PE indevido ou falha em equipamento
```

## Boas práticas profissionais

- Sempre instalar barra de aterramento dedicada (ground bus) separada do barramento negativo DC
- Definir em projeto onde existe o vínculo funcional entre neutro, PE, negativo DC e bonding, quando aplicável
- Nunca criar múltiplos pontos de ligação entre neutro/PE/negativo DC por conveniência de instalação
- Usar cabo de bitola igual ou superior ao condutor de fase para o terra AC
- Verificar o terra da marina antes de qualquer trabalho elétrico a bordo
- Documentar no diagrama a topologia de cada fonte AC: shore, gerador, inversor e transformador
- Empregar transformador de isolamento quando a embarcação permanece conectada por longos períodos ou opera em marinas de infraestrutura incerta
- Testar continuidade, polaridade, atuação do diferencial e condição das conexões em inspeções periódicas

## Cuidados de instalação

- Nunca usar o chassi/estrutura metálica como único condutor de terra — usar cabo dedicado
- Terminais de compressão (não parafuso solto) em todas as conexões de terra
- Identificar claramente todos os cabos de terra com cor padrão (verde/amarelo) ou marcação
- Não conectar PE, neutro e negativo DC fora do arranjo previsto pelo diagrama e pela fonte ativa
- Apertar conexões de barra de aterramento com torque especificado
- Usar terminais bimetálicos em conexões bronze/aço inox para evitar corrosão de contato

## Cuidados de uso

- Verificar o terra do pedestal antes de conectar shore power em marina desconhecida
- Usar GFCI portátil se houver dúvida sobre terra da marina
- Nunca ignorar choque ao tocar equipamentos — investigar imediatamente
- Inspecionar conexões de terra anualmente
- Não usar o barco como aterramento para ferramentas elétricas externas

## Erros comuns

**Interligar negativo DC e terra AC em múltiplos pontos:**

Cria caminhos paralelos para corrente de retorno e fuga. O ponto de referência deve ser único e coerente com a topologia da fonte.

**Usar o casco metálico como terra:**

Em embarcações de fibra, o casco não conduz. Em alumínio/aço, o casco pode funcionar, mas aumenta área de corrosão galvânica.

**Confiar no terra da marina sem verificar:**

O pedestal pode aparentar normalidade e ainda assim estar com PE ausente, invertido ou com alta impedância. Medição e inspeção são obrigatórias.

**Subdimensionar o cabo de terra:**

O terra AC precisa conduzir a corrente de falha até o disjuntor abrir — cabo fino queima antes de proteger.

**Aterrar o negativo do gerador separado do negativo do banco de baterias:**

Cria diferença de potencial entre sistemas — risco de arco e danos a equipamentos.

## Relação com outros sistemas

- **Bonding:** compartilha o SPOG, mas é sistema independente
- **Shore power:** introduz um PE vindo de fora; exige verificação de polaridade, continuidade e estratégia contra corrosão
- **Gerador:** pode ser fonte derivada e exigir bond neutro-PE próprio, controlado por chaveamento
- **Inversor:** alguns modelos comutam neutro e bond automaticamente; isso precisa ser compatível com o restante do sistema
- **Isolador galvânico / transformador de isolamento:** definem como a embarcação se relaciona com o PE do cais
- **Proteção Dr:** depende de arquitetura correta para responder de forma confiável a fugas e tensões de toque
- **Eletrólise:** loops de terra e terra ausente são causas diretas de corrosão acelerada
- **Equipamentos de navegação:** interferência por loops de terra é causa comum de ruído em NMEA

## Brasil x Internacional

| Aspecto | Brasil | Internacional (ABYC/IEC) |
| --- | --- | --- |
| Cor do terra AC | Verde/amarelo (NBR) | Verde (ABYC) / Verde/amarelo (IEC) |
| Tensão AC | 220V monofásico | 120V (EUA) / 230V (Europa) |
| Terra em pedestais de marina | Frequentemente ausente | Obrigatório e fiscalizado |
| Fiscalização de instalação | Praticamente inexistente | Inspeção por seguradora |
| GFCI obrigatório | Não regulamentado em náutica | ABYC E-11 (2023) exige em shore power |

**Realidade brasileira:** A maioria das embarcações de recreio no Brasil tem instalações AC sem terra adequado. O risco de choque é real e subestimado. A solução mais segura é o transformador de isolamento, que elimina a dependência do terra da marina.

## Normas aplicáveis

- **ABYC E-11 (2023)** — AC and DC Electrical Systems on Boats (referência primária)
- **ABNT NBR 5410 (2004 + emendas)** e família **ABNT/IEC** aplicável — referência complementar para princípios de baixa tensão, identificação e proteção
- **IEC 60092 (edição a verificar)** — Electrical installations in ships
- **ABNT NBR 5410 (2004 + emendas)** — Instalações elétricas de baixa tensão (base comparativa)
- **NORMAM-211 (2022 rev. aplicável via DPC)** — referencial regulatório brasileiro a ser confirmado primeiro para amadores, embarcações de esporte e recreio e universo correlato

## Como ensinar este tópico

**Sequência recomendada:**

1. Analogia: terra elétrico = escoamento de emergência — só funciona quando há vazamento
2. Explicar os 3 sistemas (negativo DC / terra AC / bonding) com diagrama de separação
3. Mostrar o SPOG fisicamente em uma embarcação real
4. Demonstrar medição de terra na marina com multímetro
5. Simular falha de isolação com amperímetro de alicate no terra
6. Discutir soluções para marina sem terra

**Conceito-chave para fixar:**

"Três sistemas, um único ponto de encontro."

## Ideias de vídeos

- **"Por que seu barco pode te matar na marina"** — terra AC ausente, risco real
- **"Os 3 sistemas de terra em embarcações"** — negativo DC vs terra AC vs bonding (animação)
- **"Como testar o terra da marina"** — multímetro na tomada do pedestal, passo a passo
- **"SPOG: o ponto mais importante da elétrica náutica"** — o que é, onde fica, como instalar
- **"Terra da marina com problema: o que fazer?"** — GFCI portátil, transformador de isolamento

## Diagramas sugeridos

- Diagrama de separação: negativo DC / terra AC / bonding / SPOG (cores diferentes para cada sistema)
- Esquema de conexão shore power com terra: pedestal → cabo → entrada barco → GFCI → painel → SPOG
- Diagrama de loop de terra (o que não fazer) vs SPOG correto (comparação lado a lado)
- Fluxo de corrente de falha: falha no equipamento → carcaça → terra → neutro → disjuntor
- Diagrama de instalação com transformador de isolamento (marina sem terra)

## FAQ

**O terra AC pode ser conectado ao negativo DC?**

Depende da topologia do sistema e da fonte em operação. Quando houver esse vínculo, ele deve existir apenas no ponto definido em projeto e nunca surgir por conexões dispersas.

**Embarcações de fibra precisam de terra?**

Sim. Mesmo sem casco metálico, todos os equipamentos AC com carcaça metálica precisam de terra AC.

**O que fazer em marina sem terra?**

Não energizar a embarcação até verificar a origem do problema. Em uso recorrente, o transformador de isolamento é a solução mais robusta para reduzir dependência da infraestrutura do cais.

**Posso usar o motor como ponto de terra?**

O bloco do motor pode participar do sistema de referência e do bonding, mas não deve substituir sozinho uma barra de proteção e um esquema de aterramento documentado.

**Como saber se meu barco tem terra AC correto?**

É preciso validar quatro pontos: continuidade do PE, posição correta do bond neutro-PE, coerência das tensões medidas na entrada e atuação das proteções diferenciais/leakage. Uma única medição isolada não fecha o diagnóstico.

## Integração com outras notas

- [[Barramento DC / Bus Bar / Distribuição DC]]
- [[Bonding — Sistema de Interligação de Massas]]
- [[CAIS (Pier) (AC)]]
- [[Cabeamento Náutico]]
- [[Chaves Gerais (DC)]]
- [[Chaves Seletoras (AC)]]
- [[Contatores (AC)]]
- [[Disjuntores (DC) e (AC)]]
- [[Divisores de Carga (DC)]]
- [[Isolador Galvânico / Transformador de Isolamento]]
- [[Proteção Dr]]

## Perguntas que esta nota responde

- O que é Aterramento em instalações elétricas náuticas?
- Qual é a função de Aterramento na embarcação?
