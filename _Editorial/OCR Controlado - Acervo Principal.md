---
title: "OCR Controlado - Acervo Principal"
note_type: "audit"
domain: "90_Revisao_Manual"
status: "auto-generated"
reviewed_on: "2026-04-25"
review_jurisdiction: "Brasil"
related_notes:
  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado"
  - "Auditoria Operacional PDF - Toolchain"
---

# OCR Controlado - Acervo Principal

> [!abstract] Resumo tecnico
> OCR pesado executado somente nos PDFs prioritarios do acervo principal, sem regravar os PDFs originais.

## Execucao

- gerado em: `2026-04-26T02:13:19.648173+00:00`
- resultados no manifesto: `90_Revisao_Manual/_Dados_Acervo/ocr-results.json`
- pasta TXT: `90_Revisao_Manual/_Dados_Acervo/ocr_texts`
- pasta MD: `90_Revisao_Manual/_Dados_Acervo/ocr_notes`

## Ferramentas

- `pdftoppm`: `pdftoppm version 25.07.0` - `C:\Users\User\AppData\Local\Microsoft\WinGet\Packages\oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe\poppler-25.07.0\Library\bin\pdftoppm.EXE`
- `tesseract`: `tesseract v5.5.0.20241111` - `C:\Program Files\Tesseract-OCR\tesseract.exe`

## Status

- `completed`: `1`
- `partial`: `1`

## PDFs processados

- `partial` - [dometic__marine-air-conditioners__price-list__2024.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Climatizacao/Dometic/Self-Contained/dometic__marine-air-conditioners__price-list__2024.pdf>) - `95/98` paginas uteis - `213175` chars - [MD](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Dados_Acervo/ocr_notes/Climatizacao/Dometic/Self-Contained/dometic__marine-air-conditioners__price-list__2024.ocr.md>) - [TXT](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Dados_Acervo/ocr_texts/Climatizacao/Dometic/Self-Contained/dometic__marine-air-conditioners__price-list__2024.ocr.txt>)
- `completed` - [raymarine__seatalk__cabling-and-connections__legacy-espelho.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Navegacao/Raymarine/SeaTalk/raymarine__seatalk__cabling-and-connections__legacy-espelho.pdf>) - `3/3` paginas uteis - `3767` chars - [MD](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Dados_Acervo/ocr_notes/Navegacao/Raymarine/SeaTalk/raymarine__seatalk__cabling-and-connections__legacy-espelho.ocr.md>) - [TXT](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Dados_Acervo/ocr_texts/Navegacao/Raymarine/SeaTalk/raymarine__seatalk__cabling-and-connections__legacy-espelho.ocr.txt>)

## Proximos passos

- Rodar `python scripts/acervo/build_pdf_companion_notes.py` para as notas companheiras herdarem os links OCR.
- Rodar `python scripts/acervo/audit_pdf_toolchain.py --scope all` quando houver janela longa para atualizar a fila global de OCR.
- Manter OCR pesado limitado a `alta` e `media`; nao gastar processamento em duplicata ou fora de escopo.
