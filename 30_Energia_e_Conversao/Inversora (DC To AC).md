---
title: "Inversora (DC To AC)"
note_type: "technical-note"
domain: "30_Energia_e_Conversao"
source_file: "INVERSORA (DC to AC) 8ed19734f7fb836b85828192050b797a.md"
status: "technical-review-l1"
aliases:
  - "INVERSORA (DC to AC)"
seo_title: "Inversora (DC To AC)"
seo_description: "Inversor converte energia DC do banco em AC para cargas de bordo. A escolha correta depende de potência contínua e de pico, tensão do banco, qualidade da forma de onda, estratégia de comutação com shore power/gerador e coordenação com a proteção AC/DC."
seo_keywords:
  - "Inversora"
  - "30 Energia e Conversao"
geo_queries:
  - "O que é Inversora (DC To AC) em instalações elétricas náuticas?"
  - "Qual é a função de Inversora (DC To AC) na embarcação?"
related_notes:
  - "Alternador (DC)"
  - "Arranque"
  - "Bancos de Bateria"
  - "BMS — Battery Management System"
  - "CAIS (Pier) (AC)"
  - "Carregador Elétrico para Tender e Jet Ski"
  - "Eólico (DC)"
  - "Gerador (AC)"
  - "Gerador (DC)"
  - "Lítio LiFePO4 — Instalação e Cuidados Específicos"
  - "Placa Solar (DC)"
---

# Inversora (DC To AC)

> [!abstract] Resumo técnico
> INVERSORA (DC → AC) — Converte energia DC do banco de baterias em AC 220V para equipamentos a bordo sem shore power ou gerador. Permite operar ar-condicionado, micro-ondas, carregadores e tomadas com energia armazenada. A diferença entre on.

## O que é

O inversor elétrico (inversora) é um conversor eletrônico que transforma energia DC (corrente contínua do banco de baterias — 12V, 24V ou 48V) em energia AC (corrente alternada — 220V/60Hz) para alimentar equipamentos que normalmente funcionariam na tomada doméstica.

É o componente que permite suprir cargas AC a partir do banco DC quando a arquitetura da embarcação, o banco e as fontes de recarga suportam isso. O grau de independência real depende da energia disponível, não apenas da potência nominal do inversor.

**Inversor vs Inversor/Carregador:**

- **Inversor simples:** apenas converte DC → AC. Sem função de carregamento.
- **Inversor/Carregador (Inverter/Charger):** converte DC → AC E carrega o banco quando há shore power ou gerador. Faz a transferência automática entre shore power e inversão. Exemplo: Victron MultiPlus, Mastervolt Mass Combi.

## Função

| Função | Detalhe |
| --- | --- |
| Conversão DC → AC | Banco de baterias → 220V/60Hz para cargas AC |
| Independência de marina | Operar equipamentos AC em fundeio, navegação, ancoragem |
| Transferência automática | Comuta entre shore power e inversão automaticamente (inversor/carregador) |
| Carregamento (inv./carregador) | Carrega o banco quando conectado ao shore power ou gerador |

## Como aparece na prática

**Muito comum no Brasil:**

- Inversor de onda senoidal modificada de 1.000–2.000W para alimentar TV, notebook e carregadores simples
- Victron Phoenix ou Xantrex instalado em embarcações que ficam em fundeio prolongado
- Inversor/carregador Victron MultiPlus como centro do sistema elétrico de veleiros e trawlers

**Comum em barcos importados:**

- Inversor/carregador de 2.500–5.000W com banco de LiFePO4 e painel solar — sistema autossuficiente
- Gerenciamento pelo Victron Cerbo GX + VRM com monitoramento remoto
- Transferência automática entre shore power, gerador e inversão

**Mais presente em embarcações maiores/premium:**

- Inversor/carregador de 8–15kW para alimentar ar-condicionado, fogão, aquecedor de água
- Banco de 48V com LiFePO4 de 400–800Ah para máxima eficiência e menor corrente DC
- Sistema híbrido: solar + eólico + alternador de alta potência + gerador de backup

## Fundamentos mínimos

**Onda senoidal pura vs onda modificada — a diferença mais crítica:**

| Tipo de onda | Custo | Equipamentos compatíveis | Equipamentos problemáticos |
| --- | --- | --- | --- |
| Senoidal pura | Maior | Todos os equipamentos AC | Nenhum |
| Senoidal modificada | Menor | TV, iluminação resistiva, carregadores simples | Motores AC, ar-condicionado, compressores, equipamentos com transformador, impressoras, aparelhos médicos |

**Por que a forma de onda importa:**

Motores, transformadores, fontes e eletrônica sensível podem apresentar aquecimento, ruído, menor eficiência ou mau funcionamento com formas de onda pobres. Para cargas críticas e sistemas permanentes de bordo, a forma senoidal pura é a referência preferencial.

**Eficiência e perdas:**

Um inversor de 12V com 2.000W de carga no output extrai do banco:

- Potência DC = Potência AC / eficiência = 2.000 / 0,92 = 2.174W
- Corrente DC = 2.174W / 12V = **181A** — corrente altíssima que exige banco e cabos dimensionados para isso

**Tensão mínima de operação (low battery cutoff):**

O inversor desliga automaticamente quando a tensão do banco cai abaixo do limite configurado ou suportado. Esse valor precisa ser compatível com a química do banco e com a estratégia de proteção adotada; não deve ser tratado como número universal.

## Características

| Parâmetro | Valor típico |
| --- | --- |
| Tensão de entrada | 12V DC ou 24V DC ou 48V DC |
| Tensão de saída | 220V AC / 60Hz |
| Potência contínua | 300W a 15.000W |
| Potência de pico | 2× a 3× a potência contínua (por 5–30s) |
| Eficiência | 88–96% (inversores de qualidade) |
| Distorção harmônica (THD) | < 3% (senoidal pura) |
| Frequência de saída | 60,0Hz ± 0,1Hz |
| Proteções integradas | Sobrecorrente, sobrecarga, alta temperatura, baixa tensão, curto-circuito |

## Configurações comuns

**Inversor simples (embarcações com uso ocasional de AC):**

- Victron Phoenix, Xantrex Freedom — instalado próximo ao banco
- Alimenta tomadas selecionadas (TV, notebook, carregadores)
- Não interfere com o shore power — sistemas separados

**Inversor/Carregador (sistema integrado — mais eficiente):**

- Victron MultiPlus, Mastervolt Mass Combi, Schneider XW+
- Um único equipamento: inverte, carrega e faz transferência automática
- Shore power presente: passa direto para as cargas + carrega o banco
- Shore power ausente: inverte o banco para as cargas
- Transferência em < 20ms — imperceptível para a maioria dos equipamentos

**Sistema com banco 48V (máxima eficiência):**

- Banco de 48V reduz a corrente DC a ¼ comparado com 12V — cabos mais finos, menos perdas
- Inversor/carregador de 48V/220V com LiFePO4
- Menor perda nos cabos DC, maior eficiência total do sistema

## Marcas e referências

- **Victron Energy** — referência mundial, linha completa (Phoenix inversor, MultiPlus inversor/carregador, Quattro para fontes duplas), melhor integração com o ecossistema GX/VRM
- **Mastervolt** — qualidade premium europeia, linha Mass Combi, excelente integração com outros produtos Mastervolt
- **Xantrex (Schneider Electric)** — americana, linha Freedom e XW+, robustos, muito presentes em embarcações americanas
- **Outback Power** — focado em sistemas off-grid maiores, qualidade reconhecida, menos comum no Brasil
- **Growatt / Epever** — marcas chinesas de qualidade crescente, custo menor, menos suporte pós-venda no Brasil
- **Cotek / Must Power** — intermediários, presentes no mercado nacional, qualidade variável

## Componentes relacionados

- Banco de baterias (fonte DC — deve ser dimensionado para a corrente de pico do inversor)
- Cabo DC de alimentação do inversor (alta corrente — 50–300A+, bitola mínima 35–95mm²)
- Fusível DC de alta corrente próximo ao banco (MRBF ou fusível NH — dimensionado para 125% da corrente máxima)
- Barramento DC (conexão do inversor ao banco)
- Painel AC secundário (alimentado pelo inversor — separado do circuito de shore power)
- Cerbo GX / Venus GX (Victron) — controle e monitoramento do inversor
- Banco de solar/eólico/alternador — fontes de recarga do banco usado pelo inversor

## Problemas mais frequentes

| Problema | Sintoma | Causa provável |
| --- | --- | --- |
| Inversor desliga sozinho | Corte silencioso durante uso | Banco com baixa tensão (cutoff), sobrecarga, sobretemperatura |
| Equipamento não funciona no inversor | Motor não parte, comportamento errático | Onda modificada × equipamento que exige senoidal pura |
| Banco descarrega muito rápido | Autonomia menor que o esperado | Carga superior à estimada, eficiência do inversor não considerada, banco subdimensionado |
| Inversor em standby consome muito | Banco descarrega mesmo sem cargas | Consumo no-load do inversor (0,5–3W em standby — somar ao balanço de energia) |
| Ruído nos equipamentos de áudio | Interferência sonora | Onda modificada, aterramento ruim, filtro de linha ausente |
| Inversor não liga | Silêncio total | Tensão do banco abaixo do mínimo, fusível queimado, cabo solto |

## Causas raiz

**Banco subdimensionado para o inversor:**

Cada 100W de carga AC extrai ~10A DC em sistema de 12V. Um inversor de 2.000W pode extrair 180–200A do banco. Banco de 100Ah esgota em menos de 30 minutos com esse consumo. Equação simples frequentemente ignorada no dimensionamento.

**Onda modificada usada com equipamento incompatível:**

Instalador compra o inversor mais barato (onda modificada) sem avisar o proprietário. Compressor da geladeira começa a falhar em 6 meses. Aquecimento anormal, consumo maior, vida útil reduzida.

**Cabo DC subdimensionado:**

A corrente DC de um inversor de alta potência em 12V chega a 200–300A. Cabo AWG 4 (25mm²) em um sistema de 3kW é cabo insuficiente — queda de tensão e aquecimento. O cabo do inversor precisa ser o mais curto e o mais grosso da embarcação.

**Fusível ausente ou distante da bateria:**

O inversor tem sua proteção interna — mas o cabo entre a bateria e o inversor é o trecho desprotegido. Curto nesse trecho + fusível distante = arco/incêndio.

## Diagnóstico prático

**Inversor desligando por baixa tensão:**

```
Multímetro → modo DCV
Medir tensão do banco com carga ligada no inversor
Se cai para 10,5V (sistema 12V) → banco descarregado ou com célula fraca
Testar banco sem carga: se tensão em repouso < 12,0V → banco com problema
Se tensão OK em repouso mas cai rápido sob carga → alta resistência interna (banco velho)
```

**Inversor desligando por sobrecarga:**

```
Somar potência de todas as cargas conectadas ao inversor
Comparar com potência nominal contínua do inversor
Se soma > 80% do nominal: risco de sobrecarga com partida de motores (corrente de pico)
Solução: inversor maior ou reduzir cargas simultâneas
```

**Verificar corrente DC do inversor em operação:**

```
Amperímetro de alicate → no cabo positivo de alimentação do inversor
Ligar carga AC conhecida (ex: chuveiro de 1.500W)
Corrente DC esperada: 1.500W / (12V × 0,92 eficiência) ≈ 136A
Se corrente muito maior → eficiência baixa (inversor com problema) ou carga maior que o declarado
```

## Boas práticas profissionais

- Preferir inversores de onda senoidal pura em instalações permanentes e cargas críticas
- Instalar o inversor o mais próximo possível do banco — minimizar comprimento do cabo DC
- Dimensionar o banco para a energia diária total, não apenas para a potência de pico
- Calcular o balanço de energia: Ah consumidos por dia vs Ah gerados por dia (solar + alternador + shore)
- Instalar fusível DC de alta corrente (MRBF, ANL ou NH) próximo ao banco, no cabo de alimentação do inversor
- Escolher entre inversor simples e inversor/carregador conforme a arquitetura da embarcação, o perfil de uso e a necessidade de transferência automática

## Cuidados de instalação

- Cabo DC de alimentação: dimensionado para a corrente máxima do inversor (ver tabela do fabricante)
- Comprimento máximo do cabo DC: reduzir ao mínimo possível (queda de tensão e perda de eficiência)
- Fixação mecânica: inversor em posição ventilada, nunca em espaço fechado sem circulação de ar
- Terminal de saída AC: circuito separado ou comutado corretamente em relação ao shore power, com proteção dedicada
- Aterramento/PE e bond neutro-PE: seguir rigorosamente a topologia prevista pelo fabricante e pelo projeto do sistema

## Cuidados de uso

- Não ligar cargas que somem mais de 80% da potência nominal — deixar margem para picos de partida
- Monitorar a tensão do banco durante uso prolongado do inversor
- Em parada longa: desligar o inversor fisicamente — o consumo em standby drena o banco ao longo do tempo
- Não cobrir o inversor durante operação — o calor danifica os componentes eletrônicos internos

## Erros comuns

**Comprar inversor de onda modificada para economizar:**

O preço inicial menor gera custo de reparo ou substituição de compressor de geladeira, micro-ondas ou equipamento de áudio. A economia inicial se paga negativamente em poucos meses.

**Subdimensionar o cabo DC:**

O cabo mais crítico da embarcação é o menos cuidado. Cabo fino para 200A = queda de tensão, aquecimento, risco de fogo.

**Calcular a autonomia pelo consumo AC sem considerar eficiência e perdas:**

"O inversor é de 2.000W e o banco tem 200Ah." Sem considerar a eficiência (≈92%) e a corrente extraída real, a autonomia calculada é 30–40% maior que a real.

**Inversor/carregador com shore power e banco simultaneamente:**

"O inversor está carregando o banco e alimentando o AC ao mesmo tempo pelo banco." O inversor/carregador faz isso corretamente — mas é importante entender o fluxo de energia para não criar expectativas incorretas de carregamento.

**Instalar sem fusível de alta corrente no cabo DC:**

O inversor tem proteção interna — mas o cabo entre o banco e o inversor não. Curto nesse trecho = arco garantido. O fusível vai no cabo, próximo ao banco.

## Relação com outros sistemas

- **Banco de baterias:** a fonte primária do inversor — capacidade e estado interno determinam a autonomia
- **BMS (em lítio):** pode limitar descarga, informar limites ao inversor ou provocar desligamento se o sistema estiver mal coordenado
- **Painel solar / Eólico:** recarregam o banco usado pelo inversor — necessários para uso autônomo prolongado
- **Alternador:** recarga o banco durante a navegação, compensando o consumo do inversor
- **Shore power:** com inversor/carregador, shore power recarrega o banco e alimenta cargas diretamente
- **Gerador AC:** com inversor/carregador, gerador recarrega o banco e alimenta cargas
- **Carregador de bateria:** em sistemas sem inversor/carregador, o carregador separa a função de recarga

## Brasil x Internacional

| Aspecto | Brasil | Internacional |
| --- | --- | --- |
| Tipo de onda mais vendida | Modificada (custo) | Senoidal pura (qualidade) |
| Inversor/carregador integrado | Crescendo, ainda pouco | Padrão em veleiros e trawlers |
| Banco 48V | Raro | Crescente em novos projetos |
| LiFePO4 + inversor | Muito raro | Padrão em sistemas modernos |
| Marca dominante | Victron | Victron (global) |

**Realidade brasileira:** O mercado nacional ainda vende muito inversor de onda modificada por questão de preço. O proprietário liga um aparelho de TV ou notebook e funciona. O problema aparece quando liga o compressor da geladeira, o ar-condicionado ou qualquer motor AC — que funcionam por meses com problemas crescentes antes de falhar definitivamente.

## Normas aplicáveis

- **ABYC E-11** — AC Electrical Systems (instalação, proteção, aterramento)
- **UL 458** — Power Converters/Inverters and Power Converter/Inverter Systems for Land Vehicles and Marine Crafts
- **NBR 13885** — Instalações elétricas em embarcações (Brasil)

## Como ensinar este tópico

**Sequência recomendada:**

1. Mostrar a diferença entre onda senoidal pura e modificada em osciloscópio (ou imagem) — impacto visual imediato
2. Calcular ao vivo: dado um inversor de 2.000W em 12V, qual a corrente DC? (~180A) — para que o aluno entenda a dimensão dos cabos
3. Demonstrar o inversor/carregador: ligar o shore power e mostrar a transferência automática
4. Exercício de dimensionamento: lista de cargas AC → potência total → banco necessário → autonomia
5. Mostrar o cálculo de balanço energético: Ah consumidos vs Ah gerados

**Conceito-chave para fixar:**

"Forma de onda ruim cobra a conta depois. Para sistema permanente e cargas reais de bordo, a senoidal pura é a referência prudente."

## Ideias de vídeos

- **"Onda senoidal pura vs modificada: o que você está destruindo sem saber"** — demonstração ao vivo
- **"Como dimensionar o inversor e o banco para o seu barco"** — cálculo prático passo a passo
- **"Inversor/carregador Victron MultiPlus: instalação e configuração"** — prático, muito procurado
- **"Por que seu banco descarrega tão rápido com o inversor ligado"** — cálculo de corrente DC vs potência AC
- **"Balanço de energia: quantos painéis solares preciso para usar o inversor?"** — conexão com solar

## Diagramas sugeridos

- Diagrama de fluxo de energia: banco DC → inversor → cargas AC (com setas de potência e corrente)
- Comparativo gráfico: onda senoidal pura vs onda modificada (forma visual da diferença)
- Esquema de inversor/carregador: shore power → primário → cargas AC + carregamento do banco
- Diagrama de dimensionamento: cargas AC → potência total → corrente DC → banco necessário → autonomia
- Esquema de instalação: banco → fusível DC → cabo DC grosso → inversor → disjuntor AC → painel AC

## FAQ

**Qual o inversor mínimo para operar um ar-condicionado de 12.000 BTU?**

Um AC de 12.000 BTU consome aproximadamente 1.200–1.500W. O pico de partida do compressor pode ser 2,5–3× isso (3.000–4.500W por 1–2 segundos). O inversor precisa de pelo menos 2.500W contínuos e pico de 4.500–5.000W para operar com margem segura.

**Inversor de 2.000W em 24V vs 12V — qual a diferença?**

Em 24V: corrente DC para 2.000W = ≈91A. Em 12V: ≈181A. Cabos de 24V têm metade da corrente e podem ser significativamente menores. Sistema de 24V é mais eficiente para potências acima de 1.000W.

**O inversor estraga a bateria?**

Não diretamente — mas usa a bateria. O que estraga é descarregar o banco abaixo do limite de DOD recomendado regularmente. O inversor tem cutoff de proteção, mas se o banco estiver subdimensionado, o cutoff ativa com frequência — estressando as baterias.

**Posso ligar o inversor direto na tomada 12V do barco (isqueiro)?**

Não para inversores acima de 150–200W. A tomada de 12V suporta geralmente 10–20A (120–240W). Para inversores maiores, é obrigatório conectar diretamente ao banco com cabo dimensionado.

**Inversor/carregador substitui o carregador de bateria separado?**

Sim — é exatamente o que faz. O inversor/carregador é um único equipamento que inverte quando não tem shore power e carrega quando tem. Elimina a necessidade de um carregador separado, mas dimensionar a função de carregamento é importante (corrente máxima de carga configurada no equipamento).

## Integração com outras notas

- [[Alternador (DC)]]
- [[Arranque]]
- [[Bancos de Bateria]]
- [[BMS — Battery Management System]]
- [[CAIS (Pier) (AC)]]
- [[Carregador Elétrico para Tender e Jet Ski]]
- [[Eólico (DC)]]
- [[Gerador (AC)]]
- [[Gerador (DC)]]
- [[Lítio LiFePO4 — Instalação e Cuidados Específicos]]
- [[Placa Solar (DC)]]

## Perguntas que esta nota responde

- O que é Inversora (DC To AC) em instalações elétricas náuticas?
- Qual é a função de Inversora (DC To AC) na embarcação?
