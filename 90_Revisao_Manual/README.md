---
title: "README do 90_Revisao_Manual"
note_type: "moc"
domain: "90_Revisao_Manual"
status: "active-curation"
reviewed_on: "2026-04-26"
review_jurisdiction: "Brasil"
aliases:
  - "Mapa do 90_Revisao_Manual"
  - "Entrada do Acervo de Revisao Manual"
related_notes:
  - "90_Revisao_Manual/00_Entrada_e_Controle/Portal do Acervo - Biblioteca de Referencia"
  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Local - Indice Gerado"
  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado"
---

# README do 90_Revisao_Manual

> [!abstract] Resumo tecnico
> Esta pasta concentra a biblioteca de referencia, os PDFs locais, as notas companheiras e a governanca operacional da revisao manual.

## Estrutura atual

- `00_Entrada_e_Controle/`: portal, tabela-mestre, backlog e checklist de operacao.
- `10_Indices_e_Paineis/`: indices e paineis gerados por script.
- `20_Matrizes_Fontes_e_Links/`: matrizes, fontes oficiais, links confirmados e notas source-first.
- `30_Notas_Tecnicas/`: notas tecnicas pontuais que ainda pertencem a esta frente.
- `90_Arquivo_Historico/`: notas substituidas ou historicas mantidas para rastreabilidade.
- `_Acervo_Local/`: PDFs e documentos fisicos.
- `_Acervo_Notas/`: notas companheiras geradas para busca e curadoria.
- `_Dados_Acervo/`: manifestos, OCR, sidecars e filas estruturadas.

## Rotina curta

1. Consultar [[90_Revisao_Manual/00_Entrada_e_Controle/Portal do Acervo — Biblioteca de Referência|Portal do Acervo]].
2. Ver PDFs principais em [[90_Revisao_Manual/10_Indices_e_Paineis/Acervo Local — Índice Gerado|Acervo Local - Indice Gerado]].
3. Ver notas companheiras em [[90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado|Acervo Notas - Indice Gerado]].
4. Ver staging humano em [[90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Indice Gerado|Acervo Humano Tecnico - Indice Gerado]].

## Regra de limpeza

- Nao apagar PDFs, HTML, imagens ou notas de acervo sem arquivar primeiro.
- Arquivos gerados devem permanecer em `10_Indices_e_Paineis/`.
- Itens antigos substituidos por indice gerado entram em `90_Arquivo_Historico/`.
- Se um novo PDF entrar, rodar `python scripts/acervo/run_pdf_pipeline.py`.
