---
title: "Matriz de Modelos e Versões — Geradores"
note_type: "inventory"
domain: "90_Revisao_Manual"
status: "active-curation"
reviewed_on: "2026-04-19"
review_jurisdiction: "Brasil"
aliases:
  - "Matriz de Geradores"
  - "Geradores — Modelos e Versões"
related_notes:
  - "Padrão da Biblioteca de Referência Técnica"
  - "Checklist Operacional — Abertura de Nova Família do Acervo"
  - "MOC — Revisao Manual"
  - "Tabela-Mestre do Acervo — Biblioteca de Referência"
  - "Matriz de Fontes — Fabricantes e Repositórios"
  - "Backlog Operacional — Coleta de Manuais"
  - "Acervo de Manuais — Marcas e Modelos Prioritários"
  - "Gerador (AC)"
---

# Matriz de Modelos e Versões — Geradores

> [!abstract] Resumo técnico
> Esta nota organiza a primeira camada de normalização para geradores marítimos com muitas variantes. O objetivo não é esgotar o mercado inteiro numa passada, e sim reduzir o atrito de busca em `Onan/Cummins` e `Kohler/Rehlko`, onde `modelo`, `spec`, `Hz`, `fase` e `rebranding` costumam atrapalhar muito a pesquisa de manuais.

Para execução consolidada da biblioteca, usar [[Tabela-Mestre do Acervo — Biblioteca de Referência]].

Para abertura padronizada de novas famÃ­lias, usar [[_Editorial/Padrão da Biblioteca de Referência Técnica|Padrão da Biblioteca de Referência Técnica]] e [[Checklist Operacional — Abertura de Nova Família do Acervo]].

## Regra de pesquisa para geradores

- manter o escopo em `mercado náutico`; não misturar nesta matriz linhas `RV`, `residenciais`, `standby` ou `industriais terrestres`, salvo quando servirem apenas como apoio de nomenclatura;
- nunca buscar só pela marca;
- combinar sempre `marca + família + código + 50/60 Hz + fase`, quando disponível;
- quando o fabricante usa `spec`, manter esse campo como coluna obrigatória da coleta;
- considerar sempre como entrega mínima o pacote triplo `manual de serviço + manual operacional + parts manual`;
- quando a marca mudou, pesquisar por `nome atual` e `nome legado`.

## Estratégia de avanço em blocos

- não faz sentido avançar `um modelo solto por vez` quando a marca publica famílias marinhas consolidadas;
- o melhor ganho vem de blocos que compartilham:
  - plataforma;
  - faixa de potência;
  - controlador;
  - lógica de documentação;
- o bloco só deve ser quebrado em modelos exatos quando a separação melhora de verdade a coleta do pacote triplo.

## Pacote mínimo obrigatório por gerador

| Documento | Obrigatório | Função no acervo |
| --- | --- | --- |
| manual de serviço | sim | diagnóstico, desmontagem, ajustes, torque, troubleshooting e procedimentos de oficina |
| manual operacional | sim | operação, alarmes, painel, rotina de uso, manutenção de usuário e checklist |
| parts manual | sim | explosão, códigos, kits, peças, compatibilidade e reposição |
| installation manual | complementar forte | montagem, ventilação, exaustão, água, elétrica e integração do conjunto |
| spec sheet / ratings sheet | complementar forte | conferir potência, Hz, fase, tensão, consumo e envelope físico |
| brochure / pocket guide / catalog | complementar | visão de linha, comparação entre famílias e pré-seleção |

## Cummins / Onan — espectro marinho `MDK` e `MDDC`

> [!note] Chave de indexacao
> Para `Onan`, o rotulo `QD` ajuda a reconhecer a familia comercial, mas a indexacao de biblioteca deve ser feita primeiro por `codigo de conjunto`. Nas familias pequenas e medias, isso costuma cair em `MDK`; no bloco grande, a literatura marinha tambem usa `MDDC`. E esse codigo que aparece em etiqueta, manual, parts list, oficina e pesquisa de campo.

| Bloco marinho | Codigos / familias | Faixa | Motor-base | Cilindros | Observacao operacional | Fonte base |
| --- | --- | --- | --- | --- | --- | --- |
| pequeno | `MDKBH` | 4 a 5 kW | Kubota diesel | 2 | familia pequena, ignicao protegida; boa para lanchas e barcos compactos | [Produto](https://www.cummins.com/generators/onan-marine-qd-45-kw-generator) / [ManualsLib MDKBH](https://www.manualslib.com/products/Onan-Mdkbh-Series-11780253.html) |
| pequeno | `MDKBJ`, `MDKBW` | 6 a 8 kW | Kubota diesel | 3 | `MDKBJ` cobre 6/7.5; `MDKBW` aparece na faixa 8 kW | [Produto](https://www.cummins.com/generators/products/onan-marine-qd-6758-kw-generator) / [Aksa Onan Marine](https://aksaeurope.com/en-us/marin-onan) |
| pequeno | `MDKDL` | 7 a 9 kW | Kubota diesel | 3 | familia regular, chassi convencional | [Produto](https://www.cummins.com/pt-br/generators/products/onan-marine-qd-79-kw-marine-generator) / [Citimarine MDKDL](https://citimarinestore.com/en/cummins-onan-marine-generators/5131-mdkbl-9-kw.html) |
| pequeno | `MDKDK` | 7 a 9 kW | Kubota diesel | 3 | versao compacta `Space Saver`, util quando o barco tem casa de maquinas apertada | [Produto](https://www.cummins.com/en-na/generators/products/onan-marine-qd-79-kw-space-saver-generator) |
| pequeno-medio | `MDKDM`, `MDKDN` | 9.5 a 13.5 kW | Kubota diesel | 4 | primeira faixa onde o codigo do conjunto muda dentro da propria familia | [Produto](https://www.cummins.com/generators/products/onan-marine-qd-9511115135-kw-generator) / [Citimarine MDKDM](https://citimarinestore.com/en/cummins-onan-marine-generators/5132-mdkbm-11-kw.html) |
| medio | `MDKDP`, `MDKDR`, `MDKDV` | 13.5 a 21.5 kW | Kubota diesel | 4 | aqui a coleta tem que considerar `Lloyd's`, CAN, fase e a variante `MDKDV` que aparece em catalogos marinhos secundarios | [Produto](https://www.cummins.com/generators/onan-marine-qd-1351717519215-kw-generator) / [Aksa Onan Marine](https://aksaeurope.com/en-us/marin-onan) |
| medio-alto | `MDKDS`, `MDKDT`, `MDKDU` | 22.5 a 29 kW | Kubota diesel | 4 | bloco marinho mais pesado; nao limitar ao nome `QD 22.5/29` | [Produto](https://www.cummins.com/generators/products/onan-marine-qd-2252729-kw-generator) / [NauticExpo pump trace](https://www.nauticexpo.com/prod/jmp-corporation/product-26603-573223.html) |
| grande 4 cil. | `MDDCW`, `MDDCU`, `MDDCY`, `MDDCS`, `MDDCT` | 40 a 55 kW | plataforma grande 4 cil.; portal atual simplifica em `Cummins B4.5` | 4 | bloco grande de entrada; vale abrir por `Hz`, `shield` e geracao da literatura | [Produto 40-110](https://www.cummins.com/en-na/generators/products/onan-marine-qd-40-110-kw-generator) / [Sheet 40-65](https://mart.cummins.com/imagelibrary/data/assetfiles/0058498.pdf) / [Brochure full line](https://pdf.directindustry.com/pdf/cummins-inc/cummins-onan-marine-generators-full-line-brochure/28678-586609.html) |
| grande 6 cil. | `MDDCH`, `MDDCJ`, `MDDCN`, `MDDCP`, `MDDCR` | 65 a 99 kW | plataforma grande `6.8 L` em literatura marinha | 6 | nao misturar com o bloco anterior; a literatura de oficina muda bastante | [Produto 40-110](https://www.cummins.com/en-na/generators/products/onan-marine-qd-40-110-kw-generator) / [MDDCH/J 65/80](https://pdf.nauticexpo.com/pdf/cummins-marine/mddch-j-65-80-kw/21504-102136.html) / [MDDCP/R 80/99](https://pdf.nauticexpo.com/pdf/cummins-marine/mddcp-r-80-99-kw/21504-102135.html) |
| grande aberto | faixa `73/85/98/99/110` e `MDDC*` a refinar por ano/spec | 73 a 110 kW | bloco grande a refinar por `codigo`, `ano` e `spec` | 4-6 | o portal atual simplifica demais; a biblioteca tem que conviver com literatura de epocas diferentes | [Produto 40-110](https://www.cummins.com/en-na/generators/products/onan-marine-qd-40-110-kw-generator) / [Brochure full line](https://pdf.directindustry.com/pdf/cummins-inc/cummins-onan-marine-generators-full-line-brochure/28678-586609.html) |

## Onan — legado `MDK` de alto valor nautico

| Bloco legado | Codigos | Motor-base / cilindros | Como usar | Fonte |
| --- | --- | --- | --- | --- |
| legado digital pequeno-medio | `MDKBK`, `MDKBL`, `MDKBM`, `MDKBN` | `D1105`, `D1105`, `V1305`, `V1505` / `3-4 cil` | excelente bloco para barcos dos anos 2000; agrega muito valor de oficina | [ManualMachine owner manual](https://manualmachine.com/onan/mdkbm/22534801-owners-manual/) / [MDKBK service manual](https://www.manualslib.com/manual/3112362/Onan-Mdkbk.html) |
| legado digital medio-alto | `MDKBP`, `MDKBR`, `MDKBS` | `V1903B`, `V2203B`, `V2803B` / `4-5 cil` | importante porque muda bastante o motor-base mesmo dentro do mesmo pacote de documentacao | [ManualsLib page 85](https://www.manualslib.com/manual/3112362/Onan-Mdkbk.html?page=85) |
| legado digital alto | `MDKBT`, `MDKBU`, `MDKBV` | `V3300-E2B`, `V3300-E2B`, `V2403` / `4 cil` | muito util para embarcacoes maiores, retrofit e manutencao pesada | [Operator manual mirror](https://www.skilledcrafting.com/onanfiles/981-0175C%20Onan%20MDKBK%20thru%20MDKBU%20Operator%27s%20Manual%20%281-2007%29.pdf) / [ManualsLib MDKBU](https://www.manualslib.com/products/Onan-Mdkbu-3661057.html) |

## Onan — apoio legado nao-`MDK`

| Linha | Valor pratico | Fonte |
| --- | --- | --- |
| `MDJA`, `MDJB`, `MDJC`, `MDJE`, `MDJF` | sao diesel marinhos mais antigos; entram como camada de apoio, nao como frente principal desta passada | [MDJA](https://www.manualslib.com/products/Onan-Mdja-12413893.html) / [MDJB](https://www.manualslib.com/products/Onan-Mdjb-12413894.html) / [MDJC](https://www.manualslib.com/products/Onan-Mdjc-12413895.html) / [MDJE](https://www.manualslib.com/products/Onan-Mdje-12413896.html) / [MDJF](https://www.manualslib.com/products/Onan-Mdjf-Series-10588906.html) |
| `MCCK` | importante para barcos mais antigos e retrofits | [ManualsLib MCCK](https://www.manualslib.com/products/Onan-Mcck-Series-8942489.html) |

## Cobertura-alvo `Onan` nesta fase

- atuais e recentes de pequeno/medio porte: `MDKBH`, `MDKBJ`, `MDKBW`, `MDKDL`, `MDKDK`, `MDKDM`, `MDKDN`, `MDKDP`, `MDKDR`, `MDKDV`, `MDKDS`, `MDKDT`, `MDKDU`;
- bloco grande marinho: `MDDCW`, `MDDCU`, `MDDCY`, `MDDCS`, `MDDCT`, `MDDCH`, `MDDCJ`, `MDDCN`, `MDDCP`, `MDDCR` e demais `MDDC*` que aparecerem por `spec`, `Hz` e ano de brochure;
- legado digital de alto valor: `MDKBK` ate `MDKBV`;
- apoio legado nao-`MDK`: `MDJA`, `MDJB`, `MDJC`, `MDJE`, `MDJF` e `MCCK`.

> [!important] Leitura pratica de oficina
> No `Onan` atual, varias fontes oficiais expõem com clareza `tipo de motor + cilindros`, mas nem sempre abrem o codigo exato do motor-base Kubota. Nesses casos, a biblioteca deve registrar o que a fonte realmente mostra e deixar o refinamento do modelo exato para `service manual`, `parts` e `spec sheet`, sem inventar codigo.

## Rehlko / Kohler Marine — normalização inicial

| Faixa / série | Modelos ou famílias visíveis nesta passada | Estrutura de variação | Observação operacional | Fonte base |
| --- | --- | --- | --- | --- |
| Série pequena | `5EFKOD`, `6EKOD`, `7EFKOZD` | muda por `50/60 Hz` e código base | famílias compactas com `ADC IId` | [5EFKOD](https://www.marine.rehlko.com/product/5efkod) / [6EKOD](https://www.marine.rehlko.com/product/6ekod) / [7EFKOZD](https://www.marine.rehlko.com/product/7efkozd) |
| Série média | `9EKOZD`, `9EFKOZD`, `11EKOZD`, `11EFKOZD`, `12EFKOZD`, `13.5EFKOZD` | 1 fase / 3 fases em vários casos | a mesma potência pode abrir páginas diferentes por fase | [Catálogo atual](https://www.marine.rehlko.com/products/Pleasure%2BCraft%2BGenerators) / [13.5EFKOZD 1-phase](https://www.marine.rehlko.com/product/13.5efkozd_1phase) / [13.5EFKOZD 3-phase](https://www.marine.rehlko.com/product/13.5efkozd_3phase) |
| Série média-alta | `17EFKOZD`, `20.5EFKOZD`, `28EFKOZD`, `35EFKOZD` | fortemente orientada a fase e a docs por SKU | convém manter tabela por modelo exato, não por família genérica | [17EFKOZD](https://www.marine.rehlko.com/product/17efkozd_3phase) / [20.5EFKOZD](https://www.marine.rehlko.com/product/20.5efkozd_3phase) / [28EFKOZD](https://www.marine.rehlko.com/product/28efkozd_3phase) / [35EFKOZD](https://www.marine.rehlko.com/product/35efkozd_3phase) |
| Série grande John Deere | `45EFOZDJ`, `55EFOZDJ`, `70EFOZDJ`, `80EFOZDJ`, `99EOZDJ`, `100EFOZDJ`, `125EFOZDJ`, `175EFOZDJ` | páginas independentes por potência | geração maior, comum em iates importados e uso mais pesado | [45EFOZDJ](https://www.marine.rehlko.com/product/45efozdj) / [55EFOZDJ](https://www.marine.rehlko.com/product/55efozdj) / [80EFOZDJ](https://www.marine.rehlko.com/product/80efozdj) / [125EFOZDJ](https://www.marine.rehlko.com/product/125efozdj) / [175EFOZDJ](https://www.marine.rehlko.com/product/175efozdj) |

## Kohler legado e espelho externo

| Modelo legado / linha | Valor prático | Espelho útil |
| --- | --- | --- |
| `6EKOD` | ajuda a cruzar `service`, `operation` e `installation` | [ManualsLib 6EKOD](https://www.manualslib.com/products/Kohler-6ekod-3799386.html) |
| `7.5R` | útil em barcos mais antigos | [ManualsLib 7.5R](https://www.manualslib.com/products/Kohler-7-5r-3981797.html) |
| `33-125EFOZDJ` | bom exemplo de instalação por faixa maior | [ManualsLib 33-125EFOZDJ](https://www.manualslib.com/products/Kohler-33-125efozdj-4003196.html) |

## 6EKOD — trilha documental já clara

| Tipo | Estado atual | Fonte |
| --- | --- | --- |
| produto oficial | confirmado | [Rehlko 6EKOD](https://www.marine.rehlko.com/product/6ekod) |
| service manual | espelho confirmado | [ManualsLib — Service](https://www.manualslib.com/manual/1196255/Kohler-6ekod.html) |
| operation manual | espelho confirmado | [ManualsLib — Operation](https://www.manualslib.com/manual/1071277/Kohler-6ekod.html) |
| installation manual | espelho confirmado | [ManualsLib — Installation](https://www.manualslib.com/manual/928158/Kohler-6ekod.html) |
| partes / kits / consumíveis | trilha oficial confirmada, sem `parts manual` exportável nesta passada | [Rehlko Parts](https://www.marine.rehlko.com/parts) |
| guia oficial de linha | confirmado | [Pocket Guide](https://resources.rehlko.com/marine/PDF/PocketGuide.pdf) |

- leitura prática:
  - o `6EKOD` já saiu da fase de marcação genérica e entrou em fase real de coleta;
  - o maior ganho agora é procurar `parts manual`, `parts list` ou PDF equivalente por distribuidor/autorizado;
  - vale registrar sempre junto `ADC IId`, porque isso melhora a busca por documentos complementares.

## Blocos nauticos recomendados de coleta

| Bloco | Faixa | Núcleo de busca | Estratégia |
| --- | --- | --- | --- |
| `Cummins / Onan MDK pequeno` | 4 a 13.5 kW | `MDKBH`, `MDKBJ`, `MDKBW`, `MDKDL`, `MDKDK`, `MDKDM`, `MDKDN` | fechar operação, service, parts e installation por famílias pequenas antes de abrir blocos grandes |
| `Cummins / Onan MDK médio` | 13.5 a 29 kW | `MDKDP`, `MDKDR`, `MDKDV`, `MDKDT`, `MDKDU`, `MDKDS` | trabalhar por faixa e depois quebrar por fase quando necessário |
| `Cummins / Onan grande (MDDC)` | 40 a 110 kW | `MDDCW`, `MDDCU`, `MDDCY`, `MDDCS`, `MDDCT`, `MDDCH`, `MDDCJ`, `MDDCN`, `MDDCP`, `MDDCR` e demais `MDDC*` | entrar por sheets e literatura, depois refinar por `codigo`, `spec` e ano |
| `Cummins / Onan MDK legado` | 5 a 29+ kW | `MDKBK` até `MDKBV` | frente de alto valor para biblioteca técnica de oficina |
| `Rehlko / Kohler pequeno` | 5 a 7 kW | `5EFKOD`, `6EKOD`, `7EFKOZD`, `ADC IId` | bloco mais eficiente para ganho rápido no mercado náutico |
| `Rehlko / Kohler médio` | 9 a 13.5 kW | `EKOZD`, `EFKOZD` | separar depois por 1 fase / 3 fases |
| `Rehlko / Kohler médio-alto` | 17 a 35 kW | `EFKOZD` | entrar por família e fase |
| `Rehlko / Kohler grande` | 45 a 175 kW | `EFOZDJ`, `EOZDJ` | usar literature, technical documents e parts como mapa inicial |

## Campos mínimos da tabela operacional de geradores

| Campo | Motivo |
| --- | --- |
| marca canônica | separar `Kohler` de `Rehlko`, `Onan` de `Cummins` |
| alias legado | melhora busca em texto antigo, placa e anúncio de barco |
| família oficial | reduz confusão entre linha e SKU |
| modelo / código | é o identificador real da busca |
| motor-base / modelo do motor | aproxima a pesquisa do mundo de oficina e de peças |
| cilindros | atalho técnico fortíssimo para identificar família e manutenção |
| `spec` / revisão | muitas vezes é a chave verdadeira do manual |
| frequência | evita misturar `50 Hz` e `60 Hz` |
| fase / tensão | evita erro em wiring e ratings |
| controlador | ajuda muito em diagnóstico e painel remoto |
| pacote triplo conferido | garante que `service + operacional + parts` já foram de fato localizados |
| tipo de documento | `operation`, `installation`, `service`, `parts`, `wiring` |
| portal oficial | trilha de rastreabilidade |
| espelho externo | camada de contingência |

## Consultas prontas para acelerar busca

- `MDKBH operator manual 60 Hz`
- `MDKDK installation manual space saver`
- `MDKDN spec sheet 13.5 kW`
- `13.5EFKOZD 1-phase installation manual`
- `45EFOZDJ technical documents`
- `Kohler 6EKOD service manual`
- `Onan MCCK operator manual`

## Próxima passada recomendada

1. Fechar primeiro `Cummins / Onan MDK pequeno` e `Cummins / Onan MDK legado`, porque entregam mais valor nautico com menos ambiguidade.
2. Tratar `MAN-B31` como universo `MDK + MDDC`, usando `QD` somente como alias comercial.
3. Consolidar `motor-base / modelo do motor` e `cilindros` como campo obrigatorio em toda familia de gerador aberta na biblioteca.
4. Dentro do universo `Rehlko / Kohler pequeno`, fechar `GEN-013` e depois abrir a tabela auxiliar de `controladores de gerador`.
