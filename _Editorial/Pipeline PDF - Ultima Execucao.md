---
title: "Pipeline PDF - Ultima Execucao"
note_type: "audit"
domain: "90_Revisao_Manual"
status: "auto-generated"
reviewed_on: "2026-04-26"
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
- iniciado em: `2026-04-26T09:05:00.497697+00:00`
- finalizado em: `2026-04-26T09:06:18.581833+00:00`
- duracao total: `78.084` s
- dry-run: `False`
- manifesto: `manifest/pdf-pipeline-last-run.json`

## Contagem por status

- `ok`: `7`
- `skipped`: `2`

## Passos

### Empacotar/atualizar staging humano tecnico

- status: `ok`
- retorno: `0`
- duracao: `34.558` s
- comando: `C:\Python314\python.exe scripts/acervo/package_human_technical_archive.py`

### Reconstruir indice local do acervo principal

- status: `ok`
- retorno: `0`
- duracao: `7.25` s
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
- duracao: `30.894` s
- comando: `C:\Python314\python.exe scripts/acervo/build_pdf_companion_notes.py`

### Construir painel de curadoria do acervo

- status: `ok`
- retorno: `0`
- duracao: `0.955` s
- comando: `C:\Python314\python.exe scripts/acervo/build_curation_dashboard.py`

### Validar scripts Python

- status: `ok`
- retorno: `0`
- duracao: `0.721` s
- comando: `C:\Python314\python.exe scripts/check_python_scripts.py`

### Validar vault Markdown

- status: `ok`
- retorno: `0`
- duracao: `1.877` s
- comando: `C:\Python314\python.exe scripts/validate_vault.py`

### Reconstruir manifesto geral

- status: `ok`
- retorno: `0`
- duracao: `1.828` s
- comando: `C:\Python314\python.exe scripts/build_manifest.py`

## Uso recomendado

- Para rotina completa: `python scripts/acervo/run_pdf_pipeline.py`.
- Para teste rapido: `python scripts/acervo/run_pdf_pipeline.py --dry-run`.
- Para nao gastar OCR pesado: `python scripts/acervo/run_pdf_pipeline.py --skip-ocr`.
- Para janela curta: `python scripts/acervo/run_pdf_pipeline.py --fast-audit --skip-ocr`.
