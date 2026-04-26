---
title: "Auditoria de Conteúdo — Ferramentas do Sistema"
note_type: "audit-report"
domain: "_Editorial"
status: "working-draft"
reviewed_on: "2026-04-25"
review_jurisdiction: "Brasil"
---

# Auditoria de Conteúdo — Ferramentas do Sistema

## Escopo desta rodada

- Auditoria executada em `2026-04-25` com base nos validadores locais e em consultas programáticas sobre `manifest/content-manifest.json` e a malha de links do vault.
- Ferramentas usadas nesta passada:
  - `python scripts/check_python_scripts.py`
  - `python scripts/validate_vault.py`
  - `python scripts/build_manifest.py`
  - consultas adicionais para backlinks, metadados faltantes e qualidade da camada `acervo-companion`

## Snapshot objetivo do vault

- notas analisadas pelo sistema: `559`
- scripts Python compilando: `20`
- erros bloqueantes de validação: `0`
- avisos do validador principal: `0`
- notas do núcleo principal fora de `_Editorial/` e `90_Revisao_Manual/`: `140`
- notas em `90_Revisao_Manual/`: `410`
- notas `acervo-companion`: `371`

## Leitura executiva

- A camada principal de conhecimento está estruturalmente forte.
- O núcleo técnico segue sem notas órfãs reais e sem falhas de frontmatter nos tipos que o validador trata como críticos.
- O maior risco atual não está no conteúdo técnico principal, e sim na observabilidade da camada de acervo: ela está grande, rastreável para humanos, mas parcialmente invisível para auditorias que leem apenas links wiki do Obsidian.

## Achados principais

### 1. Núcleo técnico saudável e pronto para continuar crescendo

- `112` notas dos tipos `technical-note`, `system`, `procedure` e `reference` estão completas para os campos cobrados hoje pelo validador:
  - `reviewed_on`
  - `review_jurisdiction`
  - `source_urls`
- Fora de `_Editorial/` e `90_Revisao_Manual/`, o vault tem `140` notas e `0` órfãs reais.
- As únicas notas com backlink muito baixo no núcleo principal continuam sendo:
  - `00_Mapas/MOC — Mapas.md`
  - `60_Automacao_Conectividade_e_Monitoramento/USB 12V (Power).md`
  - `70_Hidraulica_Climatizacao_e_Utilidades/Limpador de Parabrisas.md`

### 2. O problema mais importante desta rodada é de ferramenta, não de texto

- A camada de acervo parece ter `375` órfãs quando a análise conta apenas links wiki do Obsidian.
- Na prática, boa parte dessa camada está indexada por links Markdown locais absolutos gerados automaticamente, como ocorre em `90_Revisao_Manual/Acervo Humano Tecnico - Indice Gerado.md`.
- Consequência:
  - a navegação humana funciona;
  - mas relatórios programáticos de backlinks e orfandade ficam cegos para essa parte da base;
  - isso pode induzir decisões editoriais erradas sobre cobertura, descoberta e prioridade.

### 3. Entry points de `00_Mapas/` ainda têm dívida simples de frontmatter

- `9` MOCs de `00_Mapas/` ainda estão sem `status`.
- `10` entry points de `00_Mapas/` ainda estão sem `reviewed_on` e `review_jurisdiction`.
- Isso não quebra a validação atual, mas enfraquece governança editorial justamente na camada que deveria funcionar como porta de entrada.

### 4. A camada `acervo-companion` está robusta, mas pede triagem dirigida

- distribuição principal de extração:
  - `286` via `pdftotext`
  - `60` via `html-title-body`
  - `10` via `pdf-stream-strings`
- casos com texto fraco ou inexistente, já corretamente marcados como `text_extractable: nao`: `15`
- esses `15` casos estão concentrados em:
  - PDFs/imagens de baixa legibilidade
  - recortes visuais
  - alguns itens residuais ou legados
- leitura prática:
  - o pipeline está se comportando bem, porque não está vendendo texto ruim como se fosse extração confiável;
  - mas esses itens não devem ser usados para resumo técnico ou SEO sem OCR, inspeção humana ou descarte editorial.

### 5. Há uma convenção de procedência ainda incompleta no acervo principal

- `46` notas `acervo-companion` estão sem `acervo_origin`.
- O padrão observado sugere que elas pertencem ao acervo principal já promovido, e não ao staging humano.
- Isso não quebra a operação atual, mas deixa a trilha de procedência menos clara do que o restante da pipeline.

## O que não é problema real nesta rodada

- O número bruto de notas sem `source_urls` (`431`) parece alto, mas está concentrado em:
  - `acervo-companion`
  - `moc`
  - `index`
  - relatórios editoriais
- Na camada técnica principal cobrada pelo validador, a cobertura está íntegra.
- Portanto, o próximo esforço não deve ser “preencher `source_urls` em tudo”, e sim atacar os pontos onde a ausência realmente enfraquece curadoria ou publicação.

## Recomendações priorizadas

### Prioridade 1

- Ajustar a auditoria programática para reconhecer links Markdown locais para `.md`, ou normalizar os índices gerados do acervo para links wiki do Obsidian.
- Esta é a melhor alavanca da rodada, porque melhora a leitura do sistema inteiro sem retrabalho manual em centenas de notas.

### Prioridade 2

- Padronizar `status`, `reviewed_on` e `review_jurisdiction` nos principais MOCs de `00_Mapas/`.
- É uma correção pequena, barata e com retorno alto em governança.

### Prioridade 3

- Abrir uma fila curta para os `15` `acervo-companion` com extração fraca ou nula.
- Critério recomendado:
  - promover para OCR quando houver alto valor técnico;
  - manter como referência visual quando a imagem em si for útil;
  - arquivar ou rebaixar quando o item não trouxer valor real para oficina, ensino ou SEO.

### Prioridade 4

- Definir convenção explícita para `acervo_origin` das notas já promovidas ao acervo principal.
- Exemplo de caminho editorial viável:
  - `humano-staging`
  - `acervo-principal`
  - `captura-oficial`

## Conclusão prática

- A base está tecnicamente estável.
- O núcleo didático está melhor do que o agregado bruto sugere.
- O próximo ganho não vem de reescrever conteúdo principal, e sim de:
  - enxergar melhor a camada de acervo;
  - fechar metadados dos mapas;
  - tratar poucos casos de exceção com baixa extração.
