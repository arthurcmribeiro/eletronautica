---
title: "Bonding — Sistema de Interligação de Massas"
note_type: "system"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "BONDING — SISTEMA DE INTERLIGAÇÃO DE MASSAS 33a19734f7fb81549c39cdaf6dffb20e.md"
status: "technical-review-l1"
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
| Bitola do cabo de bonding | Definida pela norma aplicável, comprimento, robustez mecânica e ambiente |
| Continuidade do sistema | Deve ser estável e verificável em todos os pontos previstos |
| Cor do cabo de bonding | Verde (ABYC) — não confundir com terra AC |
| Potencial de proteção catódica | Interpretado por material, tipo de água e norma de referência |
| Eletrodo de referência para medição | Prata/Cloreto de Prata (Ag/AgCl) |

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
| Obrigatoriedade de bonding | Não fiscalizada | ABYC E-2 define padrões |
| Conhecimento entre instaladores | Baixo | Treinamento específico disponível |
| Diagrama de bonding documentado | Raro | Recomendado (embarcações certificadas) |
| Medição de potencial catódico | Quase inexistente | Padrão em frotas profissionais |
| Bitola usada em campo | AWG 10–14 (subdimensionado) | AWG 8 mínimo (ABYC) |
| Proteção de terminais | Raramente feita | Padrão com auto-fusível ou selante |

**Realidade brasileira:** A maioria das embarcações de recreio no Brasil não tem sistema de bonding completo ou documentado. A proteção catódica é feita de forma intuitiva (colocar zinco no eixo) sem entender o sistema como um todo. Há grande oportunidade de diferenciação técnica.

## Normas aplicáveis

- **ABYC E-2** — Prevention of Galvanic Corrosion (mais detalhada sobre bonding)
- **ABYC E-11** — AC and DC Electrical Systems (SPOG e interação com terra AC)
- **ABYC A-31** — Lightning Protection (bonding integrado ao pararaios)
- **NBR 13885** — Instalações elétricas em embarcações (Brasil — referências básicas)
- **ISO 10133** — Electrical systems — Extra-low voltage DC installations

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
