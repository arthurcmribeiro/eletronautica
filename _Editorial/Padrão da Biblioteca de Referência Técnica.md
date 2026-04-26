---
title: "Padrão da Biblioteca de Referência Técnica"
note_type: "governance"
domain: "_Editorial"
status: "active-governance"
reviewed_on: "2026-04-19"
review_jurisdiction: "Brasil"
aliases:
  - "Padrão da Biblioteca"
  - "Padrão do Acervo Técnico"
  - "Regra-Mãe da Biblioteca"
related_notes:
  - "MOC — Revisao Manual"
  - "Checklist Operacional — Abertura de Nova Família do Acervo"
  - "Tabela-Mestre do Acervo — Biblioteca de Referência"
  - "Backlog Operacional — Coleta de Manuais"
  - "Matriz de Fontes — Fabricantes e Repositórios"
  - "Matriz de Modelos e Versões — Geradores"
  - "Log de Evolução"
---

# Padrão da Biblioteca de Referência Técnica

> [!abstract] Resumo técnico
> Esta nota congela o padrão de construção da biblioteca técnica da base. Toda expansão futura do acervo deve seguir este modelo para manter a biblioteca completa, funcional, rastreável, pesquisável e pronta para uso de oficina, ensino e automação.

## Objetivo do padrão

- transformar a biblioteca em ferramenta de trabalho, e não em depósito solto de PDFs;
- manter foco em `mercado náutico`, com utilidade real para diagnóstico, instalação, manutenção, retrofit e ensino;
- garantir que cada nova frente de coleta siga a mesma lógica de fontes, campos, nomeação, status e curadoria;
- deixar a estrutura pronta para exportação futura para `Notion`, `Base44`, automações e busca estruturada.

## Escopo e limites

- o núcleo da biblioteca é `náutico`; linhas `RV`, `residenciais`, `standby` e `industriais terrestres` só entram como apoio de nomenclatura ou contingência;
- a unidade principal de avanço é `bloco náutico de família/plataforma`, e não um PDF isolado;
- um `modelo exato` só vira unidade principal quando a documentação realmente se rompe por `SKU`, `spec`, `Hz`, `fase`, `controlador` ou arquitetura;
- `catálogos`, `guides`, `brochures` e `pocket guides` entram como camada complementar, nunca como substitutos do manual técnico.

## Hierarquia obrigatória de fontes

1. `fonte oficial primária`
   fabricante, portal técnico, área de suporte, document library, parts portal.
2. `fonte oficial secundária`
   distribuidor oficial, dealer autorizado, portal corporativo regional, literatura técnica do fabricante.
3. `espelho externo`
   repositórios como `ManualsLib`, `ManualMachine` e equivalentes.

Regras:

- sempre priorizar a fonte oficial;
- usar espelho externo quando o oficial não entrega o PDF diretamente ou quando o equipamento é legado;
- registrar explicitamente quando um documento está sustentado só por espelho;
- não marcar família como `fechada` só porque o espelho existe.

## Camadas obrigatórias da biblioteca

- `Matriz de Fontes`
  fonte-first, com fabricantes, subgrupos e repositórios.
- `Banco de marcas e normas`
  camada analítica do corpus para marcas, submarcas, famílias e normativas citadas.
- `Portal do Acervo`
  camada simples de acesso humano, com atalhos para consulta por marca, sistema, links e status.
- `Matriz de Modelos e Versões`
  usada quando a linha tem muitas variantes, aliases ou famílias confusas.
- `Backlog Operacional`
  fila prática de coleta, download e curadoria.
- `Tabela-Mestre do Acervo`
  camada central da biblioteca, com status e estrutura do acervo.
- `Acervo local`
  pasta física nomeada e organizada para consulta e reuso, com `README` na raiz.
- `Camada Python operacional`
  fila JSON, relatório de captura e índice gerado do acervo local.
- `Fila de resolução oficial`
  camada pronta para visitar hubs oficiais e ligar `nome -> página -> manual`, sem download automático.

## Campos mínimos obrigatórios

| Campo | Obrigatoriedade | Função |
| --- | --- | --- |
| `grupo_matriz` | obrigatório | fabricante ou ecossistema principal |
| `marca` | obrigatório | marca operacional de busca |
| `alias` | obrigatório quando existir | legado, rebranding, nome comercial ou submarca |
| `subgrupo` | obrigatório | categoria técnica principal |
| `familia_codigos` | obrigatório | família, código-base ou conjunto principal |
| `spec_rev` | obrigatório quando aplicável | spec, revisão, série, variante ou observação crítica |
| `motor_base` | obrigatório em geradores e motorizados | motor-base, fabricante do motor ou modelo do motor |
| `cilindros` | obrigatório em geradores e motorizados | número de cilindros ou faixa quando a família mistura motores |
| `Hz` | obrigatório quando aplicável | evitar mistura de `50 Hz` e `60 Hz` |
| `fase_tensao` | obrigatório quando aplicável | evitar erro de aplicação e wiring |
| `controlador` | desejável forte | painel, display, ECU, ADC, CAN, controle remoto ou similar |
| `service`, `operacao`, `parts`, `installation` | obrigatório por status | rastreio documental por tipo |
| `catalogo_guide` | obrigatório por status | camada complementar de catálogo e literatura |
| `fonte_oficial`, `fonte_espelho` | obrigatório | rastreabilidade e auditoria |
| `pacote_triplo` | obrigatório em geradores | confirmação mínima de fechamento |
| `pasta_sugerida` | obrigatório | estrutura-alvo do acervo local |

## Pacote documental mínimo por tipo

### Regra geral

- equipamento técnico comum:
  `instalação + operação` como base;
- quando existir:
  acrescentar `service`, `parts`, `wiring`, `troubleshooting`, `spec sheet` e `product guide`.

### Regra forte para geradores

- mínimo obrigatório:
  `manual de serviço + manual operacional + parts manual`;
- camada complementar forte:
  `installation manual`, `spec sheet`, `ratings`, `brochure`, `technical documents`, `parts portal`.

### Regra para catálogos

- catálogo não substitui manual;
- catálogo serve para:
  abrir famílias, listar subgrupos, identificar aliases, comparar faixas, localizar controladores e acelerar busca.

## Regra de indexação e pesquisa

- nunca pesquisar só pela marca;
- sempre combinar, quando possível:
  `marca + família/código + spec + Hz + fase + controlador`;
- quando o fabricante usa `código de conjunto`, indexar por esse código antes do nome comercial;
- em `Onan`, priorizar `MDK` e `MDDC`; `QD` vira alias comercial;
- quando houver mudança de marca, pesquisar pelo nome atual e pelo legado.

## Extração mínima de inteligência do documento

Cada família aberta na biblioteca deve puxar, sempre que possível:

- aplicação principal;
- modelo, código ou família;
- aliases e rebrandings;
- motor-base ou plataforma;
- cilindros;
- combustível, quando aplicável;
- frequência, fase e tensão;
- controlador, painel ou display;
- tipo de documento;
- revisão, ano ou spec;
- fonte oficial;
- fonte espelho;
- observação operacional útil de oficina.

## Critério de “pronto”

Uma família só deve ser considerada realmente útil quando:

- a fonte principal está mapeada;
- o bloco está corretamente posicionado na matriz e na tabela-mestre;
- os documentos-chave foram localizados;
- os arquivos foram nomeados com padrão consistente;
- a pasta local está definida;
- a curadoria técnica foi feita sem ambiguidade grave de modelo ou versão.

Para `geradores`, o bloco só sobe como `fechado` quando o `pacote triplo` estiver conferido.

## Estrutura e nomeação do acervo local

### Estrutura de pasta

- usar padrão `Sistema/Marca/Familia-ou-Codigo`;
- exemplos:
  - `Geradores/Cummins-Onan/MDKBH`
  - `Geradores/Rehlko-Kohler/6EKOD`
  - `Climatizacao/Dometic/ECD-DCU`

### Nome de arquivo

- usar padrão:
  `marca__familia-modelo__tipo-documento__spec-rev-ano`

Exemplos:

- `cummins-onan__mdkbh__operator-manual__60hz-revC`
- `rehlko-kohler__6ekod__service-manual__tp-6774`
- `dometic__ecd16k__installation-manual__revB`

## Fluxo operacional padrão

1. abrir a marca ou família na `Matriz de Fontes`;
2. regenerar o `Banco de Marcas e Normas` quando houver nova rodada de análise integral;
3. decidir se precisa `Matriz de Modelos e Versões`;
4. criar ou atualizar a linha correspondente no `Backlog Operacional`;
5. abrir ou atualizar a linha da `Tabela-Mestre do Acervo`;
6. localizar documentos oficiais e, se necessário, espelhos;
7. preencher campos mínimos obrigatórios;
8. rodar `python scripts/acervo/build_manual_resolution_queue.py` para preparar a fila `source-first`;
9. rodar `python scripts/acervo/download_queue.py` quando a fila de download estiver pronta;
10. rodar `python scripts/acervo/build_local_index.py` para refletir o disco real;
11. baixar, nomear, organizar e curar;
12. registrar o avanço no `Log de Evolução`;
13. rodar `scripts/validate_vault.py`;
14. regenerar `manifest/content-manifest.json`.

## Regras de qualidade e consistência

- não misturar famílias diferentes num mesmo bloco sem justificativa técnica;
- não inventar `spec`, motor-base, cilindros ou compatibilidade;
- quando a fonte atual simplificar demais, registrar a simplificação e manter a incerteza explícita;
- preservar a diferença entre `oficial localizado` e `espelho localizado`;
- separar claramente `manual técnico` de `catálogo`, `brochure` e `guide`;
- sempre preferir consistência operacional à pressa de “fechar” uma linha.

## Pronto para automação

Este padrão deve permitir exportação futura para `Notion`, `Base44` e automações, então:

- manter IDs estáveis;
- usar vocabulário consistente de status;
- evitar campos livres quando houver campo estruturado;
- registrar links oficiais e espelhos separadamente;
- manter o `Banco de Marcas e Normas` auditável e regenerável;
- manter `fila`, `relatório` e `índice` como artefatos previsíveis do acervo;
- manter campos técnicos que facilitem filtro e busca.

## Aplicação futura

- qualquer nova rodada do acervo deve começar por esta nota;
- na abertura prática de uma nova família, usar [[90_Revisao_Manual/00_Entrada_e_Controle/Checklist Operacional — Abertura de Nova Família do Acervo|Checklist Operacional — Abertura de Nova Família do Acervo]];
- toda nova nota operacional da biblioteca deve apontar para este padrão;
- quando o padrão evoluir, a mudança deve ser registrada no `Log de Evolução` antes de ser replicada no acervo.
