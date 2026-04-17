---
title: "Fase e Neutro"
note_type: "technical-note"
domain: "10_Fundamentos_e_Projeto"
source_file: "FASE E NEUTRO 3fc19734f7fb8307932d81f9a93b33b1.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "FASE E NEUTRO"
  - "L e N em embarcações"
seo_title: "Fase e neutro em embarcações: topologias reais, erro do 220 V e riscos em marinas brasileiras"
seo_description: "Fase e neutro não podem ser entendidos fora da topologia da fonte. Em marinas brasileiras, 220 V pode significar fase-neutro ou fase-fase, e tratar qualquer 220 V como se houvesse neutro é um erro que compromete DR, PE, bonding e módulos eletrônicos."
seo_keywords:
  - "fase e neutro embarcação"
  - "220 fase fase marina"
  - "220 fase neutro barco"
  - "neutralização embarcação"
  - "shore power Brasil"
  - "10 Fundamentos e Projeto"
geo_queries:
  - "Como identificar se o 220 V da marina é fase neutro ou fase fase?"
  - "Posso criar neutro no barco ligando uma fase ao terra?"
  - "Qual o risco de ligar barco 220 fase-neutro em marina 220 fase-fase?"
related_notes:
  - "Aterramento"
  - "Bonding — Sistema de Interligação de Massas"
  - "CAIS (Pier) (AC)"
  - "Diagrama Unifilar — Documentação do Sistema Elétrico"
  - "Isolador Galvânico / Transformador de Isolamento"
  - "Neutro, Negativo, Terra, PE, Bonding e DR — Diferenças Críticas"
  - "Normas e Regulamentações — Abyc Iso e Brasil"
  - "Proteção Dr"
  - "Transformador Bivolt"
  - "Transformador Entrada"
---

# Fase e Neutro

> [!abstract] Resumo técnico
> Fase e neutro são funções elétricas, não apelidos de fio. Em embarcações, a interpretação correta depende da topologia da fonte ativa: cais, gerador, inversor ou secundário derivado. No Brasil, o erro mais grave é assumir que todo 220 V já traz neutro; em muitas marinas o barco recebe 220 V entre dois condutores ativos, e transformar um deles em "neutro" por ligação ao PE, ao negativo DC ou ao bonding é um defeito de projeto com potencial para disparos erráticos, circulação indevida de corrente, dano eletrônico e incêndio.

## O que é

**Fase** é qualquer condutor ativo que participa da alimentação AC e pode apresentar diferença de potencial em relação a outro condutor ativo, ao neutro funcional da fonte ou ao ponto de referência definido pela arquitetura.

**Neutro** é o condutor funcional de retorno somente em topologias que realmente o possuem. Ele não nasce do nome do fio, da cor azul nem da vontade do instalador; ele existe quando a fonte ou o sistema derivado define esse condutor como referência funcional.

**PE / terra de proteção** é o condutor de segurança destinado às massas expostas e ao controle das tensões de toque. PE não é retorno operacional de carga e não deve ser tratado como neutro improvisado.

## A premissa que mais derruba projetos no Brasil

O mesmo valor de **220 V** pode aparecer em arquiteturas diferentes:

- `220 V fase-neutro-PE`
- `220 V fase-fase-PE`
- `120/240 V split-phase`
- `220 V derivado a bordo por transformador de isolamento`

Isso significa que **medir 220 V entre dois bornes não prova a existência de neutro**. O valor da tensão sozinho não identifica a topologia. Em termos práticos, é aqui que muito projeto bonito pega fogo no mundo real.

## Topologias que realmente aparecem na náutica brasileira

| Cenário | Condutores entregues ao barco | O que existe de fato | Observação crítica |
| --- | --- | --- | --- |
| Marina/região com `220 V fase-neutro` | `L + N + PE` | neutro funcional fornecido pela origem | o barramento de neutro existe por topologia, não por convenção |
| Marina/região com `220 V fase-fase` | `L1 + L2 + PE` | dois condutores ativos, sem neutro entregue | nenhum dos dois condutores pode ser rebatizado como neutro |
| Embarcação americana `120/240 split-phase` | `L1 + L2 + N + PE` | neutro central da fonte e 240 V entre L1 e L2 | arquitetura diferente do 220 V brasileiro clássico |
| Secundário de transformador de isolamento ou fonte derivada | depende do projeto | a embarcação passa a definir a própria referência | neutro e bond N-PE só existem se o projeto os criar explicitamente |

## O cenário crítico de campo: barco construído para 220 V fase-neutro vai para marina 220 V fase-fase

Esse é um dos cenários mais perigosos da náutica brasileira:

1. o barco sai de um estaleiro ou concessionária acostumados a `220 V fase-neutro`;
2. o painel AC, o barramento de neutro e parte da documentação assumem `L + N + PE`;
3. esse barramento de neutro é interligado ao negativo DC e ao bonding em um raciocínio importado ou mal adaptado;
4. a embarcação vai para uma marina do Sudeste onde o pedestal entrega `220 V entre dois ativos`;
5. um dos ativos passa a ser usado a bordo como se fosse neutro;
6. cria-se uma malha indevida entre condutor ativo, PE, negativo DC e bonding.

O resultado pode incluir:

- corrente de retorno circulando por caminhos que deveriam ser apenas de proteção;
- disparos erráticos ou não seletivos de DR/RCD;
- tensões de toque anormais em carcaças, estruturas e água próxima;
- aquecimento de cabos de proteção e conexões de barramento;
- estresse elétrico em carregadores, automação, eletrônica embarcada e módulos de motores;
- falhas intermitentes de comunicação, sensores e módulos sensíveis;
- risco real de arco, carbonização e incêndio.

## Onde a prática costuma errar

O erro não é "usar ABYC". O erro é **copiar uma filosofia de instalação sem validar a topologia da alimentação disponível no país e na marina**.

ABYC e o ambiente norte-americano foram desenvolvidos em um contexto em que a arquitetura da fonte e a forma de distribuição são mais previsíveis para o universo de aplicação. No Brasil, a realidade de campo é muito menos homogênea. Portanto:

- usar ABYC como referência de segurança é válido;
- transplantar cegamente barramentos, cores e bonds de neutro sem revisar a fonte é errado;
- tratar `220 V` como se significasse sempre `L + N` é tecnicamente indefensável.

## O que nunca deve acontecer

Não é aceitável:

- pegar um sistema `L1 + L2 + PE` e escolher um dos ativos para virar "neutro";
- interligar esse falso neutro ao `PE`;
- interligar esse falso neutro ao negativo do banco de baterias;
- interligar esse falso neutro ao barramento de bonding;
- documentar a entrada como `L + N + PE` quando o barco na verdade recebe `L1 + L2 + PE`.

Se o barco precisa de um neutro funcional a bordo, ele deve nascer de uma **fonte derivada corretamente projetada**, como:

- secundário de transformador de isolamento/bivolt projetado para isso;
- gerador com topologia definida pelo fabricante;
- inversor com estratégia de neutro e bond documentada.

## Como medir sem se enganar

Na entrada AC de uma embarcação, o diagnóstico inicial precisa responder a quatro perguntas:

1. qual é a tensão entre os condutores ativos;
2. existe condutor neutro entregue pela fonte ou só dois ativos;
3. qual é a relação desses condutores com o PE;
4. qual fonte está energizando o sistema naquele momento.

### Sequência de medição recomendada

| Ensaio | O que mostra | Interpretação correta |
| --- | --- | --- |
| `entre os dois condutores de alimentação` | tensão efetiva de entrada | confirma o valor nominal disponível para o barco |
| `condutor A para PE` | relação desse condutor com a referência da fonte | não basta, sozinho, para chamar o condutor de neutro |
| `condutor B para PE` | relação do segundo condutor com a referência da fonte | em sistemas fase-fase pode haver leitura semelhante em ambos, leitura assimétrica ou leitura instável conforme a topologia |
| `N para PE`, quando o projeto declara neutro | integridade do vínculo funcional da fonte | só faz sentido se o sistema realmente tiver neutro |
| `continuidade do PE até o barramento de proteção` | integridade do caminho de falha | indispensável para segurança e para interpretação das medições |

**Regra prática:** medir um condutor em relação ao PE e ver valor "baixo" não autoriza classificá-lo como neutro. A identificação funcional precisa vir da topologia confirmada da fonte e do diagrama do sistema.

## Bond neutro-PE: onde ele pode existir e onde ele não pode

| Fonte ativa | O sistema tem neutro? | Onde o bond neutro-PE pertence | O que não fazer |
| --- | --- | --- | --- |
| Shore power `L + N + PE` vindo da marina | sim, se a marina realmente entregar neutro | na origem ou na posição prevista pela arquitetura daquela fonte, não aleatoriamente dentro do barco | duplicar bond em vários pontos |
| Shore power `L1 + L2 + PE` sem neutro entregue | não, na interface recebida | não existe neutro para ser bondado na entrada | criar neutro falso com um dos ativos |
| Gerador a bordo | depende do fabricante e do modo de transferência | conforme a documentação do gerador e do esquema de transferência | assumir que todo gerador sai com neutro tratado igual |
| Inversor / inversor-carregador | depende da plataforma e do modo ilha/shore | conforme a estratégia documentada do fabricante | copiar bond fixo sem entender o chaveamento interno |
| Secundário de transformador de isolamento/bivolt | depende de como o secundário foi configurado | no ponto único previsto do sistema derivado, quando a arquitetura pedir neutro | misturar bond do secundário com a entrada do primário |

## Consequências práticas do erro de neutralização

Quando um ativo é tratado como neutro sem topologia que o sustente, vários sintomas aparecem:

- carregador trabalha, mas opera fora da referência esperada;
- automação e módulos eletrônicos apresentam falhas intermitentes;
- DR dispara em uma marina e não dispara em outra;
- carcaças e barramentos assumem tensões inesperadas;
- PE passa a conduzir corrente operacional;
- corrosão e corrente vagante pioram;
- o diagrama deixa de representar o que existe fisicamente.

Em motores e módulos eletrônicos modernos, isso é particularmente grave porque a instalação de potência passa a contaminar a referência elétrica dos equipamentos de controle.

## Boas práticas de projeto no Brasil

- especificar no diagrama de entrada quais topologias o barco aceita: `L + N + PE`, `L1 + L2 + PE`, `120/240 split-phase`, ou sistema derivado;
- marcar barramentos e borne de entrada como `L1`, `L2`, `N` e `PE` de acordo com a função real, não pela cor disponível;
- usar transformador bivolt/de isolamento quando a embarcação precisa operar entre marinas com topologias distintas;
- manter separado o barramento de neutro do barramento de PE sempre que a topologia não autorizar o bond naquele ponto;
- documentar de forma explícita a relação entre `PE`, `negativo DC` e `bonding`;
- revisar o projeto inteiro quando a embarcação mudar de região, pedestal ou filosofia de shore power;
- ensaiar a entrada do cais antes da primeira conexão, não depois da primeira queima.

## Erros comuns

**Assumir que 220 V significa automaticamente fase-neutro:**

Esse erro é a raiz de grande parte das neutralizações indevidas em embarcações nacionais.

**Usar a cor azul para "criar" neutro:**

Cor ajuda identificação. Cor não cria função elétrica.

**Interligar barramento de neutro ao negativo da bateria sem validar a topologia:**

Mistura retorno funcional AC com referência DC e ainda aproxima falhas do sistema de automação e do motor.

**Usar o bonding como caminho de retorno invisível:**

Quando o falso neutro encosta no universo `PE/DC/bonding`, a embarcação perde a fronteira entre proteção, referência e equipotencialização.

## Relação com outros sistemas

- **[[CAIS (Pier) (AC)]]** define a topologia efetivamente entregue ao barco.
- **[[Aterramento]]** trata o papel do PE e do ponto único de referência.
- **[[Bonding — Sistema de Interligação de Massas]]** trata a malha anticorrosão, que não pode ser usada como neutro.
- **[[Proteção Dr]]** depende da leitura correta dos condutores ativos monitorados.
- **[[Transformador Entrada]]** trata adaptação de tensão.
- **[[Transformador Bivolt]]** trata adaptação de topologia e tensão para a realidade das marinas brasileiras.
- **[[Isolador Galvânico / Transformador de Isolamento]]** diferencia isolamento real de simples mitigação no PE.

## Normas e referências de engenharia

- **ABYC E-11 (2023)**: referência forte para arquitetura AC/DC, mas deve ser aplicada com adaptação à topologia brasileira de alimentação.
- **ISO 13297:2020**: trata sistemas elétricos AC monofásicos em pequenas embarcações e reforça a importância de definir a arquitetura da fonte.
- **ABNT NBR 5410 (2004 + emendas)**: referência complementar de baixa tensão para identificação de condutores e princípios de proteção, sem substituir norma náutica.
- **NORMAM-211 (2022 rev. aplicável via DPC)**: referência regulatória brasileira para o ambiente de embarcações de esporte e recreio; não substitui a engenharia de projeto.

## FAQ

**Se a marina mede 220 V, posso assumir que existe neutro?**

Não. Você só sabe que existe 220 V entre dois pontos. A existência de neutro depende da topologia da fonte e da forma como ela foi entregue ao barco.

**Posso transformar uma fase em neutro ligando-a ao terra?**

Não. Isso cria uma neutralização artificial e perigosa. Se o barco precisa de neutro funcional, ele deve nascer de uma fonte derivada corretamente projetada.

**Quando um transformador resolve o problema?**

Quando o transformador foi escolhido para o problema certo. Autotransformador resolve adaptação de tensão. Transformador de isolamento/bivolt corretamente configurado pode também criar um sistema derivado previsível a bordo.

**O DR protege mesmo se a topologia estiver errada?**

Nem sempre do jeito esperado. DR mal aplicado em topologia mal entendida pode disparar sem lógica aparente ou, pior, deixar o instalador com falsa sensação de segurança.

**ABYC está errada para o Brasil?**

Não. Errado é importar a solução sem refazer a leitura da alimentação local, do esquema de aterramento e do objetivo real do projeto.

## Integração com outras notas

- [[Aterramento]]
- [[Bonding — Sistema de Interligação de Massas]]
- [[CAIS (Pier) (AC)]]
- [[Normas e Regulamentações — Abyc Iso e Brasil]]
- [[Proteção Dr]]
- [[Transformador Bivolt]]
- [[Transformador Entrada]]
- [[Isolador Galvânico / Transformador de Isolamento]]

## Perguntas que esta nota responde

- O que é fase em uma embarcação?
- O que é neutro em uma embarcação?
- Todo 220 V traz neutro?
- Como diferenciar `L + N + PE` de `L1 + L2 + PE`?
- Posso criar neutro a bordo a partir de uma fase?
- Onde o bond neutro-PE pode existir?
- O que acontece quando o barco chega a uma marina com topologia diferente?
- Por que o erro aparece muito no Brasil?
- Como medir a entrada do cais sem se enganar?
- Que relação isso tem com DR, PE, negativo DC e bonding?
