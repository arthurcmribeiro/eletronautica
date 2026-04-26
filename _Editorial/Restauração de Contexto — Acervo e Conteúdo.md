---
title: "Restauração de Contexto — Acervo e Conteúdo"
note_type: "editorial"
domain: "_Editorial"
status: "active"
reviewed_on: "2026-04-22"
review_jurisdiction: "Brasil"
aliases:
  - "Ponto de Retomada do Acervo"
  - "Memória Operacional do Acervo"
related_notes:
  - "MOC — Revisao Manual"
  - "Portal do Acervo — Biblioteca de Referência"
  - "Log de Evolução"
  - "_Editorial/Recuperação de Threads do Codex — Eletro Nautica"
  - "_Editorial/Ponto de Retomada — Acervo Notas e Curadoria"
  - "Acervo Notas - Indice Gerado"
  - "Acervo Local — Índice Gerado"
---

# Restauração de Contexto — Acervo e Conteúdo

> [!abstract] Resumo técnico
> Esta nota recompõe o estado operacional da frente de `acervo + conteúdo` para retomada no Codex mesmo quando o histórico do chat não aparece mais.

## Onde o trabalho está

- frente editorial e governança: [[_Editorial/Log de Evolução|Log de Evolução]]
- recuperação de histórico do Codex: [[_Editorial/Recuperação de Threads do Codex — Eletro Nautica|Recuperação de Threads do Codex — Eletro Nautica]]
- ponto exato de continuação editorial: [[_Editorial/Ponto de Retomada — Acervo Notas e Curadoria|Ponto de Retomada — Acervo Notas e Curadoria]]
- mapa principal da frente: [[00_Mapas/MOC — Revisao Manual|MOC — Revisao Manual]]
- entrada simples da biblioteca: [[90_Revisao_Manual/00_Entrada_e_Controle/Portal do Acervo — Biblioteca de Referência|Portal do Acervo — Biblioteca de Referência]]
- acervo físico de PDFs: [[90_Revisao_Manual/_Acervo_Local/README|Acervo Local — README]]
- camada textual companheira dos PDFs: [[90_Revisao_Manual/_Acervo_Notas/README|Acervo Notas - README]]
- scripts operacionais: `scripts/acervo/`

## Estado consolidado em 2026-04-22

- a trilha editorial já está registrada até o `Lote 39` no [[_Editorial/Log de Evolução|Log de Evolução]];
- a frente de manuais saiu da fase só de pesquisa e já tem:
  - `links confirmados`;
  - `tabela-mestre`;
  - `backlog operacional`;
  - `fila source-first`;
  - `acervo local` com PDFs;
  - `camada companheira` em Markdown;
- o `90_Revisao_Manual/_Acervo_Local/` tem `651` arquivos no disco;
- o painel [[90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado|Acervo Notas - Indice Gerado]] mostra `46` notas companheiras distribuídas em:
  - `Climatizacao`: `6`;
  - `Complementar-Brasil`: `3`;
  - `Geradores`: `27`;
  - `Navegacao`: `10`;
- a camada de dados operacionais já existe em `90_Revisao_Manual/_Dados_Acervo/`, com banco de marcas/normas e fila de resolução;
- a automação central da etapa está concentrada em:
  - `scripts/acervo/promote_human_archive_to_main.py`;
  - `scripts/acervo/rename_acervo_files_for_search.py`;
  - `scripts/acervo/build_local_index.py`;
  - `scripts/acervo/build_pdf_companion_notes.py`;
  - `scripts/acervo/resolve_manual_links.py`.

## Último ponto real de avanço

- `Lote 38`: criação da camada `_Acervo_Notas/`, extração textual mais robusta e organização do staging técnico por tema;
- `Lote 39`: evolução das notas companheiras para formato preservável, com:
  - frontmatter útil para curadoria;
  - bloco `CURADORIA-HUMANA:START/END`;
  - painel geral [[90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado|Acervo Notas - Indice Gerado]];
- o `MOC — Revisao Manual` já foi expandido para apontar para a maior parte dessas notas e painéis.

## Arquivos-chave para retomar rápido

- [[90_Revisao_Manual/00_Entrada_e_Controle/Tabela-Mestre do Acervo — Biblioteca de Referência|Tabela-Mestre do Acervo — Biblioteca de Referência]]
- [[90_Revisao_Manual/00_Entrada_e_Controle/Backlog Operacional — Coleta de Manuais|Backlog Operacional — Coleta de Manuais]]
- [[90_Revisao_Manual/20_Matrizes_Fontes_e_Links/Preparação Source-First — Resolver de Links Oficiais|Preparação Source-First — Resolver de Links Oficiais]]
- [[90_Revisao_Manual/20_Matrizes_Fontes_e_Links/Aplicação Piloto — Onan (Resolver Source-First)|Aplicação Piloto — Onan (Resolver Source-First)]]
- [[90_Revisao_Manual/10_Indices_e_Paineis/Acervo Local — Índice Gerado|Acervo Local — Índice Gerado]]
- [[90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado|Acervo Notas - Indice Gerado]]
- [[_Editorial/Padrão da Biblioteca de Referência Técnica|Padrão da Biblioteca de Referência Técnica]]

## Comandos de manutenção já usados nesta frente

```bash
python scripts/acervo/build_local_index.py
python scripts/acervo/build_pdf_companion_notes.py
python scripts/build_manifest.py
python scripts/validate_vault.py
python scripts/check_python_scripts.py
```

## Próxima retomada recomendada

- usar [[90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado|Acervo Notas - Indice Gerado]] como fila curta de curadoria humana;
- priorizar os itens de `curation_priority: alta` antes de abrir novas famílias do staging;
- promover novos PDFs do `Acervo do humano/` apenas quando a família já estiver clara na governança;
- ao perder contexto no Codex, reabrir nesta ordem:
  - esta nota;
  - [[_Editorial/Log de Evolução|Log de Evolução]];
  - [[00_Mapas/MOC — Revisao Manual|MOC — Revisao Manual]];
  - [[90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado|Acervo Notas - Indice Gerado]].

## Observação importante

- o histórico conversacional do Codex pode ter sumido da interface;
- o conteúdo operacional não sumiu do vault;
- as threads antigas também seguem presentes em `C:\Users\User\.codex\`, conforme documentado em [[_Editorial/Recuperação de Threads do Codex — Eletro Nautica|Recuperação de Threads do Codex — Eletro Nautica]];
- esta nota existe para substituir essa memória de chat por memória persistente dentro da própria base.
