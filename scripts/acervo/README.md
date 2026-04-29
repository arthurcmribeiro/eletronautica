---
title: "Scripts do acervo"
note_type: "process"
domain: "90_Revisao_Manual"
status: "active"
reviewed_on: "2026-04-26"
review_jurisdiction: "Brasil"
---

# Scripts do acervo

Este diretorio concentra a automacao da frente `90_Revisao_Manual`. Nao limpar por data de modificacao: alguns scripts antigos ainda sao dependencia de pacote, rerun ou auditoria reversivel.

## Pipeline ativa

- `run_pdf_pipeline.py`: orquestra auditoria, OCR controlado, indices, notas companheiras, manifesto e validacao operacional.
- `audit_pdf_toolchain.py`: audita PDFs, paginas, metadados, integridade `qpdf`, texto pesquisavel e fila de OCR.
- `ocr_priority_pdfs.py`: gera OCR auxiliar em sidecars sem alterar PDFs originais.
- `build_pdf_companion_notes.py`: cria/atualiza notas `.md` para PDFs curados do acervo principal, extraindo titulos, codigos documentais, modelos, topicos, secoes e linhas tecnicas curtas para busca e curadoria.
- `build_curation_dashboard.py`: separa acervo humano/tecnico em manifesto, prioriza fila de curadoria e enriquece notas prioritarias sem sobrescrever curadoria humana.
- `build_local_index.py`: gera o indice humano e JSON do acervo principal.
- `package_human_technical_archive.py`: empacota o staging humano e preserva curadoria humana ja feita.
- `promote_all_human_pdfs_to_main.py`: promove PDFs tecnicos do staging humano para o acervo principal.
- `pdf_text_tools.py`: utilitarios compartilhados de leitura e resumo de PDF.

## Fonte, links e coleta

- `build_brand_norm_bank.py`: gera banco de marcas, normas e citacoes do corpus.
- `build_manual_resolution_queue.py`: gera fila source-first de links oficiais a resolver.
- `resolve_manual_links.py`: resolve links oficiais quando a fila esta pronta.
- `download_queue.py`: baixa itens da fila estruturada quando aplicavel.

## Migracao, triagem e manutencao

- `organize_human_archive.py`: organiza staging humano bruto.
- `organize_technical_triage_bulk.py`: organiza lotes tecnicos de triagem.
- `consolidate_human_triage_buckets.py`: consolida buckets humanos quando a triagem muda.
- `archive_human_duplicate_groups.py`: arquiva duplicatas/excedentes de forma reversivel.
- `promote_human_archive_to_main.py`: base legada de promocoes pontuais; ainda e importada por outros scripts.
- `rename_acervo_files_for_search.py`: renomeia arquivos do acervo para busca forte.
- `rename_promoted_pdf_files_readably.py`: migra PDFs promovidos em massa de nomes tecnicos com hash para nomes legiveis baseados no arquivo original.
- `rename_pdf_companion_names_from_content.py`: limpa nomes remanescentes com `__`, hash ou `legacy-espelho`, mantendo PDFs, notas companheiras e sidecars OCR sincronizados.

## Regra de limpeza

- Preferir arquivamento reversivel a exclusao.
- Antes de mover um `.py`, rodar `rg "nome_do_script|import_do_modulo" scripts`.
- Depois de qualquer mudanca, rodar:

```powershell
python scripts/check_python_scripts.py
python scripts/acervo/run_pdf_pipeline.py
python scripts/validate_vault.py
python scripts/build_manifest.py
```
