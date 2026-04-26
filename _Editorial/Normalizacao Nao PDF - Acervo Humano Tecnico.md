---
title: "Normalizacao Nao PDF - Acervo Humano Tecnico"
note_type: "audit"
domain: "90_Revisao_Manual"
status: "active-curation"
reviewed_on: "2026-04-26"
review_jurisdiction: "Brasil"
related_notes:
  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Nao PDF - Indice Gerado"
  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Indice Gerado"
---

# Normalizacao Nao PDF - Acervo Humano Tecnico

> [!abstract] Resumo tecnico
> Esta auditoria registra a normalizacao dos arquivos tecnicos do staging humano que ainda nao sao PDFs.
> O objetivo e busca e triagem: preservar os originais, extrair texto e deixar uma fila clara para conversao ou curadoria.

## Resultado

- arquivos nao-PDF processados: `67`
- arquivos com texto extraivel: `24`
- arquivos sem texto util: `43`
- notas com bloco integral de busca: `66`
- imagens com OCR via Tesseract: `7`

## Distribuicao por extensao

- `.html`: `60`
- `.jpeg`: `1`
- `.jpg`: `5`
- `.png`: `1`

## Decisao operacional

- HTML tecnico passa a ter texto extraido dentro da propria nota companheira e sidecar `.txt` em `_Dados_Acervo/non_pdf_texts`.
- Imagens tentam OCR via Tesseract quando a ferramenta esta disponivel; quando o OCR nao gera texto util, ficam como evidencias visuais a revisar.
- Estes arquivos continuam fora do acervo principal PDF-first ate haver conversao limpa para PDF, nota tecnica autoral ou descarte fundamentado.

## Proxima fila sugerida

- converter HTML de maior valor em notas tecnicas autorais ou PDFs arquivaveis
- revisar imagens de campo para remover conteudo pessoal/sensivel antes de qualquer reaproveitamento
- priorizar HTML de `03_Baterias_e_DC`, `04_Shore_Power_e_AC` e `06_Bombas_Hidraulica_e_Utilidades` para material didatico
