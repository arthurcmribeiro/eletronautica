# AGENTS.md

## Objetivo desta base

Esta é uma base técnica em Markdown sobre elétrica náutica, pensada para Obsidian, governança editorial, consulta técnica, ensino, SEO/GEO e futura publicação em site, apostila, slides e produtos digitais.

## Princípios de trabalho

- Escrever em português do Brasil, com tom técnico, claro e profissional.
- Priorizar Brasil-primeiro para contexto regulatório e operacional.
- Usar ABYC/ISO como referência de engenharia quando aplicável, sem inventar norma.
- Preservar conteúdo bom e melhorar estrutura, clareza, rastreabilidade e navegabilidade.
- Evitar reescrita indiscriminada, texto inchado e figuras ornamentais.
- Separar analogia didática de descrição física literal, explicitando limites quando necessário.

## Contexto operacional do usuário

- O usuário é engenheiro eletricista com atuação em elétrica náutica e oficina focada em soluções práticas.
- Frentes principais:
  - Instituto Porta do Mar: cursos e formação técnica.
  - Imobiliária Porta do Mar: gestão de imóveis.
  - Apps no Base44: CRM, automação e sistemas.
- Stack preferida:
  - Base44
  - n8n
  - Notion
  - Google Drive
  - WhatsApp
- Priorizar soluções simples, baratas, rastreáveis e automatizáveis.
- Evitar automação que pareça atendimento robótico barato.

## Estrutura esperada

- `_Editorial/`: auditoria, backlog, logs, governança e pontos de retomada.
- `_visuals/`: specs e saídas versionáveis de visuais.
- `scripts/visuals/`: automações visuais.
- `90_Revisao_Manual/_Acervo_Local/`: PDFs e documentos físicos do acervo.
- `90_Revisao_Manual/_Acervo_Notas/`: notas companheiras em Markdown para busca, rastreio e curadoria.
- `90_Revisao_Manual/_Dados_Acervo/`: artefatos operacionais, filas e dados estruturados.
- `90_Revisao_Manual/00_Entrada_e_Controle/`: portal, tabela-mestre, backlog e checklist operacional.
- `90_Revisao_Manual/10_Indices_e_Paineis/`: indices e paineis gerados por script.
- `90_Revisao_Manual/20_Matrizes_Fontes_e_Links/`: matrizes, links confirmados e notas source-first.
- `90_Revisao_Manual/30_Notas_Tecnicas/`: notas tecnicas pontuais da frente de revisao.
- `90_Revisao_Manual/90_Arquivo_Historico/`: notas substituidas ou historicas, preservadas sem poluir a operacao.
- `manifest/`: artefatos gerados para integração e auditoria.

## Fluxo obrigatório para PDFs novos

1. Se o PDF ainda não foi curado, colocar em `90_Revisao_Manual/_Acervo_Local/Acervo do humano/` ou em uma subpasta adequada do staging.
2. Se o PDF já pertence ao acervo principal, colocar somente dentro do padrão `Sistema/Marca/Familia/arquivo.pdf`.
3. Nunca deixar PDF solto na raiz de `_Acervo_Local`.
4. Usar nomes pesquisáveis no padrão `marca__familia-modelo__tipo-documento__spec-rev-ano.pdf`.
5. Rodar a pipeline apropriada:

```powershell
python scripts/acervo/run_pdf_pipeline.py
```

## Contrato da camada companheira

- Cada PDF do acervo principal curado deve ter uma nota `.md` espelhada em `_Acervo_Notas/`.
- A nota companheira deve preservar o bloco `CURADORIA-HUMANA:START/END`.
- A nota companheira serve para busca, indexação, rastreio e preparo de curadoria.
- Ela não substitui leitura técnica humana quando o PDF for escaneado, gráfico demais ou tiver `text_extractable: nao`.
- PDFs do staging humano são tratados por `package_human_technical_archive.py`.
- PDFs do acervo principal são tratados por `build_pdf_companion_notes.py`.
- A saude operacional dos PDFs e a fila de OCR sao tratadas por `audit_pdf_toolchain.py`.
- OCR pesado deve ser feito por `ocr_priority_pdfs.py`, gerando sidecars `.txt` e `.md` em `_Dados_Acervo` sem alterar o PDF original.
- A rotina completa e propagavel para PDF novo deve ser feita por `run_pdf_pipeline.py`.

## Comandos de validação

Rodar antes de concluir qualquer lote:

```powershell
python scripts/check_python_scripts.py
python scripts/validate_vault.py
python scripts/build_manifest.py
```

Quando houver mudança em visuais:

```powershell
python scripts/visuals/render_visuals.py
python scripts/visuals/integrate_visuals.py
```

Quando houver mudança no acervo:

```powershell
python scripts/acervo/run_pdf_pipeline.py
```

## Governança editorial

- Registrar mudanças relevantes em `_Editorial/Log de Evolução.md`.
- Criar relatórios em `_Editorial/` quando a rodada alterar arquitetura, acervo, validação ou política editorial.
- Não editar manualmente artefatos gerados sem entender qual script os recria.
- Não apagar arquivos do acervo para “limpar”; preferir arquivamento reversível ou staging fora de escopo.

## Ferramentas esperadas

- `git`
- `python`
- `rg`
- `pdftotext`
- `pdfinfo`
- `qpdf`
- `exiftool`
- `tesseract`
- `mutool`
- `magick`
- `gswin64c`
- `7z`
- `node` e `npm`
- `gh`, quando autenticado

Ferramentas desejáveis para OCR/PDF pesado:

- `ImageMagick`
- `Ghostscript`

## Não fazer

- Não inventar norma, código ABNT, exigência da Marinha, ABYC ou ISO.
- Não misturar acervo principal curado com staging bruto.
- Não promover PDF pessoal ou fora de escopo para o acervo principal.
- Não tratar nota automática como curadoria humana final.
- Não reescrever tudo sem motivo.
- Não remover mudanças existentes que não foram feitas por você.
