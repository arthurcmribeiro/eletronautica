---
title: "Pipeline PDF - Ultima Execucao"
note_type: "audit"
domain: "90_Revisao_Manual"
status: "auto-generated"
reviewed_on: "2026-04-27"
review_jurisdiction: "Brasil"
related_notes:
  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Local - Indice Gerado"
  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado"
  - "Auditoria Operacional PDF - Toolchain"
  - "OCR Controlado - Acervo Principal"
---

# Pipeline PDF - Ultima Execucao

> [!abstract] Resumo tecnico
> Orquestrador operacional para atualizar indice local, auditoria PDF, OCR auxiliar, notas companheiras, validacao e manifestos.

## Resultado

- status geral: `ok`
- iniciado em: `2026-04-27T06:34:52.642018+00:00`
- finalizado em: `2026-04-27T06:35:23.163085+00:00`
- duracao total: `30.521` s
- dry-run: `False`
- manifesto: `manifest/pdf-pipeline-last-run.json`

## Contagem por status

- `ok`: `5`
- `skipped`: `4`

## Passos

### Empacotar/atualizar staging humano tecnico

- status: `skipped`
- retorno: `0`
- duracao: `0.0` s
- comando: `C:\Python314\python.exe scripts/acervo/package_human_technical_archive.py`

### Reconstruir indice local do acervo principal

- status: `skipped`
- retorno: `0`
- duracao: `0.0` s
- comando: `C:\Python314\python.exe scripts/acervo/build_local_index.py`

### Auditar PDFs com toolchain externo

- status: `skipped`
- retorno: `0`
- duracao: `0.0` s
- comando: `C:\Python314\python.exe scripts/acervo/audit_pdf_toolchain.py --scope all --ocr-sample-limit 2`

### Gerar OCR auxiliar prioritario

- status: `skipped`
- retorno: `0`
- duracao: `0.0` s
- comando: `C:\Python314\python.exe scripts/acervo/ocr_priority_pdfs.py --priority alta`

### Regenerar notas companheiras dos PDFs

- status: `ok`
- retorno: `0`
- duracao: `26.056` s
- comando: `C:\Python314\python.exe scripts/acervo/build_pdf_companion_notes.py`

### Construir painel de curadoria do acervo

- status: `ok`
- retorno: `0`
- duracao: `0.955` s
- comando: `C:\Python314\python.exe scripts/acervo/build_curation_dashboard.py`

### Validar scripts Python

- status: `ok`
- retorno: `0`
- duracao: `0.549` s
- comando: `C:\Python314\python.exe scripts/check_python_scripts.py`

### Validar vault Markdown

- status: `ok`
- retorno: `0`
- duracao: `1.468` s
- comando: `C:\Python314\python.exe scripts/validate_vault.py`

### Reconstruir manifesto geral

- status: `ok`
- retorno: `0`
- duracao: `1.493` s
- comando: `C:\Python314\python.exe scripts/build_manifest.py`

## Uso recomendado

- Para rotina completa: `python scripts/acervo/run_pdf_pipeline.py`.
- Para teste rapido: `python scripts/acervo/run_pdf_pipeline.py --dry-run`.
- Para nao gastar OCR pesado: `python scripts/acervo/run_pdf_pipeline.py --skip-ocr`.
- Para janela curta: `python scripts/acervo/run_pdf_pipeline.py --fast-audit --skip-ocr`.
