---
title: "Acervo Local — README"
note_type: "index"
domain: "90_Revisao_Manual"
status: "active-curation"
reviewed_on: "2026-04-19"
review_jurisdiction: "Brasil"
aliases:
  - "README do Acervo Local"
  - "Raiz Física do Acervo"
related_notes:
  - "Portal do Acervo — Biblioteca de Referência"
  - "Acervo Local — Índice Gerado"
  - "Padrão da Biblioteca de Referência Técnica"
  - "Tabela-Mestre do Acervo — Biblioteca de Referência"
  - "Backlog Operacional — Coleta de Manuais"
---

# Acervo Local — README

> [!abstract] Resumo técnico
> Esta é a raiz física prevista para os `PDFs`, `parts lists`, `brochures` e demais documentos efetivamente baixados da biblioteca. A ideia é separar `mapa de links` de `acervo local real`.

## Função desta pasta

- receber somente material já `baixado`;
- refletir a organização da [[Tabela-Mestre do Acervo — Biblioteca de Referência]];
- facilitar consulta direta por oficina, ensino e curadoria.

## Estado atual

- a raiz do acervo local já está definida;
- nem todo item `manual localizado` já foi baixado para cá;
- o uso desta pasta deve crescer conforme o backlog sair de `manual localizado` para `baixado`.
- a subpasta `Acervo do humano/` funciona como `staging bruto` de triagem e promoção; ela não entra no índice gerado do acervo principal.
- para ver os primeiros arquivos que já entraram de fato, usar [[90_Revisao_Manual/90_Arquivo_Historico/Acervo Local — Índice Inicial|Acervo Local — Índice Inicial]].
- para ver o inventário automático atual do disco, usar [[90_Revisao_Manual/10_Indices_e_Paineis/Acervo Local — Índice Gerado|Acervo Local — Índice Gerado]].

## Camada Python operacional

- a fila estruturada de download fica em `90_Revisao_Manual/_Acervo_Local/acervo-download-queue.json`;
- o relatório automático da última rodada fica em `90_Revisao_Manual/_Acervo_Local/acervo-download-report.json`;
- o índice JSON do acervo local fica em `90_Revisao_Manual/_Acervo_Local/acervo-local-index.json`;
- a visão humana gerada automaticamente fica em [[90_Revisao_Manual/10_Indices_e_Paineis/Acervo Local — Índice Gerado|Acervo Local — Índice Gerado]].
- a promoção em lote de conteúdo técnico vindo do staging fica em `scripts/acervo/promote_all_human_pdfs_to_main.py` e, por padrão, já dispara a geração das notas companheiras;
- a renomeação para busca forte no acervo principal fica em `scripts/acervo/rename_acervo_files_for_search.py`;
- a camada companheira de notas Markdown dos PDFs fica em `90_Revisao_Manual/_Acervo_Notas/`, gerada por `scripts/acervo/build_pdf_companion_notes.py`;
- a camada companheira tambem gera o painel `90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado.md` e preserva o bloco de curadoria humana em reexecucoes futuras;
- a checagem sintática dos scripts Python do projeto fica em `scripts/check_python_scripts.py`.

```bash
python scripts/acervo/download_queue.py
python scripts/acervo/build_local_index.py
python scripts/acervo/build_pdf_companion_notes.py
python scripts/check_python_scripts.py
```

## Fluxo desta etapa

- o material bruto entra primeiro em `Acervo do humano/`;
- o que for técnico e validado sobe para o acervo principal por `scripts/acervo/promote_human_archive_to_main.py`;
- nessa mesma subida, a camada de rastreio textual já pode ser atualizada em `90_Revisao_Manual/_Acervo_Notas/`;
- depois os nomes são refinados por `scripts/acervo/rename_acervo_files_for_search.py`;
- em seguida o disco real é refletido por:
  - `python scripts/acervo/build_local_index.py`
  - `python scripts/acervo/build_pdf_companion_notes.py`
  - `python scripts/build_manifest.py`
  - `python scripts/validate_vault.py`
  - `python scripts/check_python_scripts.py`

## Estrutura-alvo

- `Geradores/`
- `Climatizacao/`
- `Shore-Power/`
- `Bombas/`
- `Navegacao/`
- `Iluminacao/`
- `Seguranca/`
- `Estabilizacao/`
- `Complementar-Brasil/`

## Convenção de subpastas

- usar padrão `Sistema/Marca/Familia-ou-Codigo`
- exemplos:
  - `Geradores/Cummins-Onan/MDKBH`
  - `Geradores/Rehlko-Kohler/6EKOD`
  - `Climatizacao/H-Tec/HFC-Acqua`
  - `Bombas/Xylem-Rule/Bilge-Float-DryBilge`

## Nome de arquivo

- usar padrão:
  - `marca__familia-modelo__tipo-documento__spec-rev-ano`

## Convenção adicional de nome

- o sufixo `legacy-espelho` indica documento técnico útil, porém sustentado por fonte legada ou espelho curado;
- evitar o uso solto de `mirror` no nome final do arquivo;
- sempre que houver ganho real de busca, preferir incluir:
  - família/código;
  - tipo documental;
  - contexto técnico relevante, como `12v-systems`, `eletrolise` ou `self-contained-air-conditioner`.

## Regra de entrada no acervo local

- não salvar arquivo aqui só porque o link existe;
- só mover para esta pasta quando o documento estiver:
  - localizado;
  - identificado corretamente;
  - com nome consistente;
  - apto a ser marcado como `baixado` na tabela.

## Regra de separação documental

- `manual técnico` deve ficar separado de `catálogo`, `brochure` e `guide`;
- quando uma família tiver muitos documentos, separar por tipo:
  - `installation`
  - `operation`
  - `service`
  - `parts`
  - `wiring`
  - `catalogo-guide`
