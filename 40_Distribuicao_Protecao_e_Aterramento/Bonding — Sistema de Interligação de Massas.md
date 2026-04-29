---
title: "Bonding — Sistema de Interligação de Massas"
note_type: "system"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "BONDING — SISTEMA DE INTERLIGAÇÃO DE MASSAS 33a19734f7fb81549c39cdaf6dffb20e.md"
status: "fase-5-reescrita-premium"
reviewed_on: "2026-04-17"
fase_5_reescrita: "05"
prioridade_fase_5: 6.3
review_jurisdiction:
  - "Brasil"
  - "internacional"
normas_citadas:
  - "ABYC E-2 (2020)"
  - "ABYC E-11 (2023)"
  - "ABYC A-28 (2020)"
  - "ABYC A-31 (2024)"
  - "ABNT NBR 5410 (2004 + emendas)"
  - "ISO 13297:2020"
  - "ISO 28679:2017"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "BONDING — SISTEMA DE INTERLIGAÇÃO DE MASSAS"
seo_title: "Bonding — Sistema de Interligação de Massas"
seo_description: "Bonding é a rede de equipotencialização de partes metálicas selecionadas da embarcação para controle de corrosão, integração com a proteção catódica e redução de diferenças de potencial. Não é sinônimo de terra AC."
seo_keywords:
  - "Bonding"
  - "Interligação"
  - "Massas"
  - "40 Distribuicao Protecao e Aterramento"
geo_queries:
  - "O que é Bonding — Sistema de Interligação de Massas em instalações elétricas náuticas?"
  - "Qual é a função de Bonding — Sistema de Interligação de Massas na embarcação?"
related_notes:
  - "Aterramento"
  - "Ânodo"
  - "Barramento DC / Bus Bar / Distribuição DC"
  - "Cabeamento Náutico"
  - "Chaves Gerais (DC)"
  - "Chaves Seletoras (AC)"
  - "Contatores (AC)"
  - "Correntes Parasitárias — Stray Currents"
  - "Disjuntores (DC) e (AC)"
  - "Divisores de Carga (DC)"
  - "Eletrólise"
---

# Bonding — Sistema de Interligação de Massas

> [!abstract] Resumo técnico
> Bonding é a malha de equipotencialização de partes metálicas selecionadas da embarcação, normalmente integrada à estratégia de proteção catódica e separada funcionalmente do PE do sistema AC. Quando mal projetado, vira caminho de corrosão acelerada e de correntes indevidas.

> [!tip] Regra de decisão em 30 segundos
> 1. **Bonding ≠ PE ≠ Negativo DC.** Três sistemas com funções distintas que convergem apenas no SPOG (ponto único de referência).
> 2. **Verde com função de equalização ≠ verde-amarelo de PE.** Ambos são verdes; confundir é erro estrutural.
> 3. **Cabo mínimo: AWG 8 (8 mm²)** para barramento principal em casco não-metálico (ABYC E-11). AWG 10-14 é subdimensionado.
> 4. **Continuidade alvo: < 1 Ω** entre barramento e cada componente. > 3 Ω = conexão ruim.
> 5. **Ânodo correto por material:** zinco para aço em salgada; alumínio (AlZnIn) para casco de alumínio; magnésio para doce. Trocar sem respeitar material é erro técnico.
> 6. **Corrente persistente no cabo de bonding** (alicate) = loop indevido com PE/negativo/neutro. Investigar antes que corroa algo caro.
> 7. **Eixo é o componente mais esquecido.** Sem escova/clamp de eixo, a hélice fica desprotegida mesmo com todo o resto OK.

## O que é

Bonding é a interligação elétrica intencional de partes metálicas selecionadas da embarcação para manter potenciais próximos, distribuir a ação dos ânodos sacrificiais quando aplicável e reduzir diferenças de potencial que aceleram corrosão. Em embarcações de recreio, o bonding costuma abranger eixo, ferragens submersas, motor, alguns passe-cascos e outros elementos metálicos definidos pelo projeto.

O sistema de bonding é **distinto** do terra AC (segurança elétrica) e do negativo DC (referência de circuito), embora a arquitetura possa prever um ponto de referência comum ou controlado entre esses sistemas.

## Função

| Função | Mecanismo |
| --- | --- |
| Equalizador de potencial | Mantém todos os metais no mesmo potencial → sem fluxo de corrente galvânica entre eles |
| Proteção catódica | Conecta todos os metais ao ânodo sacrificial → zinc protege todos simultaneamente |
| Prevenção de faíscas | Tanques de combustível em potencial igual → sem faísca por descarga estática |

Observação importante: proteção contra descargas atmosféricas é um subsistema próprio. Em alguns projetos ele compartilha elementos metálicos com a embarcação, mas não deve ser tratado como consequência automática de "ter bonding".

## Como aparece na prática

- Cabo verde (bonding) correndo ao longo da quilha, conectando motor → eixo → passe-cascos → tanque → quilha
- Barramento de bonding (bonding bus) na parte mais baixa da bilge, próximo ao SPOG
- Eletrodo de zinco externo conectado ao barramento de bonding por cabo dedicado
- Clamps de bonding em cada componente metálico submerso ou próximo à água
- Em embarcações de alumínio: o casco próprio faz o bonding (estrutura condutora)

## Fundamentos mínimos

**Diferença de potencial como motor da corrosão:**

Dois metais dissimilares submersos criam uma célula galvânica — o menos nobre corrói. O bonding conecta todos os metais ao ânodo (zinc/alumínio), fazendo com que o ânodo seja o único metal a corroer.

**Não existe uma faixa única para todos os metais e todas as águas:**

Critérios de potencial de proteção catódica dependem do material protegido, do tipo de ânodo, da salinidade, da temperatura e do método de medição. Leituras com eletrodo Ag/AgCl são extremamente úteis, mas devem ser interpretadas por material e condição de serviço, não por uma única faixa universal aplicada a toda embarcação.

**Baixa impedância e continuidade são essenciais:**

O bonding só funciona se os caminhos metálicos e os condutores tiverem continuidade confiável, conexões limpas e baixa impedância relativa. O objetivo de campo não é perseguir um único número mágico, e sim garantir que o ânodo e a malha de bonding efetivamente "enxerguem" os componentes previstos pelo projeto.

## Características

| Parâmetro | Valor típico |
| --- | --- |
| Bitola do cabo de bonding (partida) | AWG 8 (≈ 8 mm²) mínimo para barramento principal em cascos não-metálicos. Ramais, saltos e corrente de falta esperada conforme projeto. Fonte: ABYC E-11 (2023), consultar cláusula vigente. |
| Continuidade do sistema | Meta de campo: `< 1 Ω` entre o barramento e qualquer ponto metálico previsto. Medir com ohmímetro de baixa resistência. |
| Cor do cabo de bonding | Verde (convenção ABYC). **Não confundir** com o PE verde-amarelo do AC — mesmo verde, sistemas distintos. |
| Potencial de proteção catódica | Depende do material, do ânodo e do meio. Ver tabela Ag/AgCl abaixo. |
| Eletrodo de referência para medição | Prata/Cloreto de Prata (Ag/AgCl) em água salgada; Cu/CuSO₄ em água doce. |

### Potenciais de proteção catódica (referência Ag/AgCl, água salgada)

| Material protegido | Faixa protetora | Observação |
| --- | --- | --- |
| Aço carbono / aço inox | `-0,80 V` a `-1,05 V` | Abaixo de `-1,10 V` risco de over-protection (descolamento de tinta, fragilização por hidrogênio em inox). |
| Alumínio | `-0,90 V` a `-1,10 V` | Faixa estreita; over-protection ataca alumínio. Medir com cuidado e escolher ânodo adequado (AlZnIn, não Zn puro em água salgada fria). |
| Bronze / latão naval | `-0,60 V` a `-0,80 V` | Risco maior: dealloying (perda de zinco) se potencial cair demais. |
| Cobre | `-0,50 V` a `-0,60 V` | Protege-se facilmente; atenção à contaminação do meio. |

> Tabela para triagem. Consultar ABYC E-2 (2020) e datasheet do fabricante do ânodo para valores definitivos por aplicação, temperatura e salinidade.

### Comissionamento e teste de continuidade

Após instalação ou revisão do bonding:

1. **Visual:** inspeção de clamps, conexões e cabos verdes — oxidação, soltura, contato com água salgada, terminais corroídos.
2. **Continuidade:** medir resistência entre o barramento de bonding e cada ponto da malha (eixo, passe-cascos, motor, tanque metálico, âncora). Meta `< 1 Ω`. Valores `> 3 Ω` indicam conexão ruim — investigar.
3. **Potencial:** medir potencial de cada componente submerso com eletrodo Ag/AgCl. Valores fora da faixa da tabela → revisar ânodo, conexão ou isolação do componente.
4. **Documentar:** registrar leituras em planilha de comissionamento para comparação em revisões futuras (ver [[MOC — Diagnóstico e Manutenção]]).

## Configurações comuns

**Embarcações de fibra (muito comum no Brasil):**

- Bonding costuma ser necessário para ferragens submersas e outros elementos definidos pelo projeto
- Motor, eixo e ferragens molhadas tendem a ser os primeiros candidatos à malha
- A inclusão de cada item deve obedecer ao fabricante, ao material e à estratégia de proteção catódica
- Ânodo externo fixado ao casco ou no eixo

**Embarcações de alumínio (comum em barcos importados — trawlers, lanchas de pesca offshore):**

- O casco de alumínio é o próprio barramento de bonding
- ATENÇÃO: alumínio corrói rapidamente sem ânodos adequados
- A escolha do ânodo depende do material do casco e da qualidade da água; aplicar regra simplista aqui é erro comum

**Embarcações com pararaios (mais presente em embarcações maiores/premium):**

- O projeto de proteção atmosférica deve ser tratado como subsistema específico
- Qualquer compartilhamento com a malha metálica principal precisa ser explicitamente previsto em projeto
- Não assumir que o bonding existente já satisfaz requisitos de proteção contra descargas

## Marcas e referências

- **Blue Sea Systems** — barramentos de bonding, terminais
- **Ancor** — cabos e terminais para bonding marítimo
- **Martyr Anodes / MG Duff** — ânodos e kits de proteção catódica
- **Perko** — passe-cascos com terminal de bonding integrado
- **Shurlock** — clamps de bonding para tubulações e eixos

## Componentes relacionados

- Barramento de bonding (bonding bus bar)
- Ânodos sacrificiais externos (zinc/alumínio)
- Cabo de bonding AWG 8 verde
- Clamps de bonding (para eixo, passe-cascos)
- Eletrodo de referência Ag/AgCl (para medição)
- Placa de terra (ground plate) para sistema de pararaios

## Problemas mais frequentes

| Problema | Sintoma | Causa |
| --- | --- | --- |
| Bonding interrompido | Ânodo não protege componente remoto | Cabo cortado, terminal solto |
| Alta resistência | Proteção catódica ineficaz | Oxidação nos terminais, cabo subdimensionado |
| Bonding conduzindo corrente indevida | Corrosão acelerada | Loop de terra, falha de isolamento, ligação indevida com PE/neutro/negativo |
| Bonding ausente | Corrosão galvânica severa | Instalação incompleta |
| Ânodo mal conectado | Zero proteção | Tinta entre ânodo e casco (sem contato) |
| Proteção catódica mal ajustada | Consumo anormal de ânodos ou ataque localizado | Seleção errada de ânodo, leitura mal interpretada, ambiente agressivo |

## Causas raiz

**Bonding interrompido por oxidação:**

Conexões de bonding em ambiente salino oxidam progressivamente. Conexões sem proteção (terminais a crimpar descobertos, sem selante) perdem contato elétrico em 2–3 anos.

**Sistema de bonding conduzindo corrente parasita:**

Quando o bonding está conectado ao negativo DC e ao terra AC em múltiplos pontos, qualquer falha de isolação injeta corrente parasita no sistema de bonding — que distribui para todos os metais submersos. Paradoxo: o sistema de proteção vira fonte de destruição.

**Instalação incompleta:**

Instaladores terrestres que migram para náutica frequentemente não conhecem bonding. Motor aterrado, eixo sem bonding, passe-cascos sem conexão — proteção fragmentada.

**Ânodo sem contato elétrico:**

Pintura aplicada entre o ânodo e o casco por descuido ou desconhecimento. O zinco está fisicamente fixado mas eletricamente isolado — zero proteção.

## Diagnóstico prático

**Verificar continuidade do sistema de bonding:**

```jsx
Multímetro → modo Ω
Medir entre barramento de bonding e cada componente
Motor: deve ser < 1 Ω
Eixo: deve ser < 1 Ω
Passe-cascos: deve ser < 1 Ω
Tanque de combustível: deve ser < 1 Ω
Resultado > 1 Ω → conexão com problema
```

**Verificar potencial de proteção catódica:**

```jsx
Eletrodo de referência Ag/AgCl na água próximo ao casco
Multímetro → modo DCV (preto no eletrodo, vermelho no barramento de bonding)
Comparar o valor obtido com o material protegido, o tipo de água e o critério de referência adotado
Leitura isolada não fecha diagnóstico sem conhecer casco, ferragens e ânodos instalados
```

**Verificar corrente indevida na malha:**

```jsx
Amperímetro de alicate → no cabo principal de bonding
Com shore power conectado
Corrente persistente ou variável na malha merece investigação
Verificar especialmente vínculo indevido com PE, neutro ou negativo DC
```

## Boas práticas profissionais

- Mapear quais componentes devem participar do bonding e justificar cada inclusão no diagrama
- Usar terminais de compressão bimetálicos e cobrir com auto-fusível ou fita de butila
- Documentar o sistema de bonding no diagrama da embarcação, com pontos de inspeção e posição dos ânodos
- Medir resistência do bonding anualmente e após qualquer trabalho de manutenção
- Verificar potencial catódico em inspeções programadas quando a embarcação permanecer muito tempo na água
- Não confundir cabo de bonding verde com terra AC verde — identificar com etiqueta

## Cuidados de instalação

- Dimensionar o condutor de bonding pela norma aplicável, pelo percurso e pela robustez mecânica necessária
- Nunca passar o cabo de bonding por dentro de conduítes com cabos de potência — interferência
- Conexões em locais protegidos da bilge — evitar imersão constante
- Verificar que cada ânodo tem contato metálico direto com a estrutura (raspar tinta)
- Não conectar bonding ao negativo DC exceto no SPOG — ponto único
- Instalar terminal de bonding em cada passe-casco durante a instalação (difícil retrofitar depois)

## Cuidados de uso

- Verificar visualmente o bonding quando o barco sobe na carena (risco de cabo cortado em obra)
- Lavar conexões de bonding com água doce após longos períodos em água salgada
- Não trocar um passe-casco sem reconectar o cabo de bonding — erro frequente em manutenção
- Inspecionar conexão do ânodo externo anualmente

## Quando chamar especialista

> [!danger] Situações que exigem análise qualificada
> - Casco metálico com pitting profundo ou perda de material em zona específica — dano estrutural iminente; reparar sem diagnóstico completo significa corroer de novo em meses.
> - Corrente persistente medida no cabo principal de bonding (alicate amperímetro) — indica loop indevido com PE, neutro ou negativo DC; origem pode ser interna ou na marina.
> - Ânodos consumidos em **semanas** em vez de temporada — corrente parasita grave, não desgaste normal.
> - Integração de bonding com sistema de pararaios (ABYC A-31 2024) — compartilhamento de malha é projeto específico, não retrofit intuitivo.
> - Transformador de isolamento ou isolador galvânico recém-instalado e bonding começou a comportar-se diferente — topologia AC afeta SPOG.
> - Casco de alumínio com faixa de potencial catódico fora do intervalo seguro (`-0,90 V` a `-1,10 V` vs Ag/AgCl) — over-protection ataca alumínio tão rápido quanto under-protection.
> - Instalação nova em embarcação com propulsão elétrica (lítio, motor elétrico) — malha de bonding interage com BMS e proteção do banco; erro pode desarmar BMS ou destruir célula.
>
> O bonding é um subsistema onde "quase certo" tem custo. Inspeção profissional anual custa muito menos que uma hélice, eixo ou trocador de calor substituído por corrosão evitável.

## Erros comuns

**Interligar bonding ao negativo DC em múltiplos pontos:**

Cria loop de corrente parasita. O SPOG deve ser o único ponto de interligação.

**Confundir bonding com terra AC:**

Ambos são verdes (ABYC). Ambos vão ao SPOG. Mas têm funções distintas — bonding é para corrosão, terra AC é para choque elétrico.

**Não incluir o eixo no bonding:**

O eixo é o componente mais difícil de conectar e o mais esquecido. Sem bonding no eixo, a hélice fica desprotegida.

**Instalar ânodo de zinco em embarcação de alumínio:**

A seleção do ânodo deve respeitar material, água doce/salobra/salgada e recomendação do fabricante. Tratar zinco, alumínio ou magnésio como solução universal é erro técnico.

**Substituir passe-cascos sem reconectar bonding:**

O profissional troca o fitting, pinta tudo — e esquece de reconectar o cabo verde. Resultado: corrosão galvânica no novo fitting em poucos meses.

**Superproteger com excesso de zincos:**

Mais ânodo não é sinônimo de melhor proteção. O potencial precisa ser avaliado com medição adequada e interpretação por material e ambiente.

## Relação com outros sistemas

- **Aterramento:** compartilha o SPOG, mas é sistema independente com função diferente
- **Correntes parasitas:** bonding mal executado pode se tornar caminho de propagação de corrente indevida
- **Ânodos sacrificiais:** bonding é o sistema que distribui a proteção dos ânodos para os metais previstos
- **Shore power:** sem transformador de isolamento, o PE vindo do cais chega ao arranjo de proteção da embarcação; com sistema derivado por transformador de isolamento/bivolt, a lógica muda e o bonding não pode ser usado como extensão informal de neutro
- **Pararaios:** pode compartilhar partes metálicas apenas quando houver projeto específico de proteção atmosférica
- **Motor:** o bloco do motor deve fazer parte do sistema de bonding

## Brasil x Internacional

| Aspecto | Brasil | Internacional (ABYC) |
| --- | --- | --- |
| Obrigatoriedade de bonding | Não fiscalizada | ABYC E-2 (2020) define padrões |
| Conhecimento entre instaladores | Baixo | Treinamento específico disponível |
| Diagrama de bonding documentado | Raro | Recomendado (embarcações certificadas) |
| Medição de potencial catódico | Quase inexistente | Padrão em frotas profissionais |
| Bitola usada em campo | AWG 10–14 (subdimensionado) | AWG 8 mínimo (ABYC) |
| Proteção de terminais | Raramente feita | Padrão com auto-fusível ou selante |

**Realidade brasileira:** A maioria das embarcações de recreio no Brasil não tem sistema de bonding completo ou documentado. A proteção catódica é feita de forma intuitiva (colocar zinco no eixo) sem entender o sistema como um todo. Há grande oportunidade de diferenciação técnica.

## Normas aplicáveis

- **ABYC E-2 (2020)** — Prevention of Galvanic Corrosion (mais detalhada sobre bonding)
- **ABYC E-11 (2023)** — AC and DC Electrical Systems (SPOG e interação com terra AC)
- **ABYC A-28 (2020)** — Galvanic Isolators (protecao catódica e interação com PE de shore power)
- **ABYC A-31 (2024)** — Lightning Protection (bonding integrado ao pararaios; edição canonicalizada na Fase 1 — vault mantém A-31 como referência única)
- **ISO 28679:2017** — Small craft — Cathodic protection (referência internacional para proteção catódica em embarcações)
- **ABNT NBR 5410 (2004 + emendas)** e família **ABNT/IEC** aplicável — referência complementar para princípios de baixa tensão, identificação e proteção
- **ISO 13297:2020** — Small craft — Electrical systems — Alternating and direct current installations (referência viva para DC em pequenas embarcações; sucedeu a ISO 10133, retirada)
- **ISO 10133** — *retirada*; manter apenas como contexto histórico conforme nota mestre [[Normas e Regulamentações — Abyc Iso e Brasil]]

## Como ensinar este tópico

**Sequência recomendada:**

1. Analogia: bonding = sistema de vasos comunicantes — pressão igual em todos os pontos, sem fluxo entre eles
2. Mostrar série galvânica: zinc → alumínio → aço inox → bronze — diferença de potencial entre eles
3. Demonstrar como o bonding une todos os metais ao zinc → zinc corrói sozinho
4. Medição ao vivo com eletrodo de referência — potencial antes e depois de conectar zinco
5. Mostrar o SPOG e como bonding, negativo DC e terra AC se encontram
6. Discutir erros comuns com fotos de dano real

**Conceito-chave para fixar:**

"Sem bonding, cada metal corrói por conta própria. Com bonding correto, só o zinc corrói — e é isso que você quer."

## Ideias de vídeos

- **"Bonding: o sistema invisível que protege seu barco"** — explicação do zero com animação de série galvânica
- **"Por que seu passe-casco corroeu em 2 anos"** — bonding ausente, diagnóstico e solução
- **"Como medir se o bonding está funcionando"** — eletrodo de referência, multímetro, interpretação
- **"SPOG: onde tudo se conecta"** — bonding + negativo DC + terra AC no único ponto correto
- **"Zinco no barco de alumínio: por que é um erro?"** — ânodo correto por tipo de metal e água

## Diagramas sugeridos

- Diagrama do sistema de bonding completo: motor → eixo → passe-cascos → tanque → quilha → barramento → ânodo externo
- Esquema do SPOG: como negativo DC, terra AC e bonding se encontram em um único ponto
- Série galvânica com potenciais em mV vs Ag/AgCl — visual e prático
- Diagrama de medição de potencial catódico: posição do eletrodo, multímetro, interpretação dos valores
- Comparação: bonding correto vs bonding como veículo de corrente parasita (antes e depois)

## Visuais editoriais associados

Specs editoriais disponíveis (em renderização — sprint 1 pós-Fase 4):

- [`_visuals/specs/ac-dc-pe-bonding-analogia.json`](../_visuals/specs/ac-dc-pe-bonding-analogia.json) — Analogia visual controlada que separa PE, Neutro AC, Negativo DC e Bonding em quatro painéis coloridos, com três erros comuns catalogados. Ajuda a quebrar a confusão sistemática tratada na Regra de 30 segundos desta nota.
- [`_visuals/specs/iso-10133-vs-13297-sucessao.json`](../_visuals/specs/iso-10133-vs-13297-sucessao.json) — Quadro histórico da sucessão normativa: ISO 10133 (APOSENTADA) vs ISO 13297:2020 (VIVA). Elimina a confusão documental comum em projetos antigos e manuais de fabricantes pré-2020.

Ambos os specs têm `target_notes` incluindo esta (`Bonding — Sistema de Interligação de Massas.md`) e serão renderizados em SVG/PNG via `scripts/render_visuals.py`.

## FAQ

**Todo barco precisa de bonding?**

Nem toda embarcação exige a mesma extensão de bonding. O critério depende dos metais presentes, do tipo de casco, do arranjo de ferragens e da estratégia de proteção catódica.

**Bonding e terra AC são a mesma coisa?**

Não. Ambos são verdes e vão ao SPOG, mas têm funções distintas: terra AC protege contra choque elétrico, bonding protege contra corrosão galvânica.

**O zinco no eixo substitui o sistema de bonding?**

Não. O zinco no eixo protege apenas o eixo e a hélice. Sem bonding, os passe-cascos e outros metais submersos ficam desprotegidos.

**Quanto tempo leva para o bonding oxidar?**

Não existe prazo universal. O que importa é ambiente, qualidade do terminal, proteção mecânica e rotina de inspeção.

**Como saber se o bonding está funcionando?**

Verificar continuidade entre barramento e componentes previstos, medir potenciais com eletrodo de referência e analisar o consumo dos ânodos à luz do material e do ambiente de operação.

## Integração com outras notas

- [[Aterramento]]
- [[Ânodo]]
- [[Barramento DC / Bus Bar / Distribuição DC]]
- [[Cabeamento Náutico]]
- [[Chaves Gerais (DC)]]
- [[Chaves Seletoras (AC)]]
- [[Contatores (AC)]]
- [[Correntes Parasitárias — Stray Currents]]
- [[Disjuntores (DC) e (AC)]]
- [[Divisores de Carga (DC)]]
- [[Eletrólise]]

## Perguntas que esta nota responde

- O que é Bonding — Sistema de Interligação de Massas em instalações elétricas náuticas?
- Qual é a função de Bonding — Sistema de Interligação de Massas na embarcação?
