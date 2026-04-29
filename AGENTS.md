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
- Citar normas com **edição/ano + cláusula + contexto** sempre que possível.

## Estado da base (pós-Fase 6)

- **Caminho B 100% fechado** — 137 notas técnicas processadas com template DEC-11 premium-l3.
- **Norma mestre estrutural** em `10_Fundamentos_e_Projeto/Normas e Regulamentações — Abyc Iso e Brasil.md` é a **source-of-truth normativa** (340+ docs canonicalizados em 10 famílias).
- **12 DECs** ativos (DEC-30 a DEC-41) — documentados em `_Editorial/plano_execucao_auditoria.md`.

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

- `_Editorial/`: auditoria, backlog, logs, governança e pontos de retomada + YAMLs de fase.
- `_visuals/`: specs e saídas versionáveis de visuais.
- `scripts/`: validações + manifest + checks Python.
- `scripts/visuals/`: automações visuais (renderer + integrate).
- `scripts/acervo/`: pipeline de PDFs (Codex/OpenAI).
- `manifest/`: artefatos gerados para integração e auditoria.
- `90_Revisao_Manual/_Acervo_Local/`: PDFs e documentos físicos do acervo.
- `90_Revisao_Manual/_Acervo_Notas/`: notas companheiras em Markdown para busca, rastreio e curadoria.
- `90_Revisao_Manual/_Dados_Acervo/`: artefatos operacionais, filas e dados estruturados.
- `90_Revisao_Manual/00_Entrada_e_Controle/`: portal, tabela-mestre, backlog e checklist operacional.
- `90_Revisao_Manual/10_Indices_e_Paineis/`: índices e painéis gerados por script.
- `90_Revisao_Manual/20_Matrizes_Fontes_e_Links/`: matrizes, links confirmados e notas source-first.
- `90_Revisao_Manual/30_Notas_Tecnicas/`: notas técnicas pontuais da frente de revisão.
- `90_Revisao_Manual/90_Arquivo_Historico/`: notas substituídas ou históricas, preservadas sem poluir a operação.

## Sistema de tiers (Fase 6 Caminho B)

| Tier | Quantidade | Template | Critério de uso |
|------|------------|----------|-----------------|
| **Tier S** (premium full DEC-11) | 45 notas | TL;DR 9 regras (tip callout) + Danger 5-9 cenários + Glossário 15-25 termos + normas canonicalizadas (titulo+ano+cláusula) | Risco vida/fogo/explosão/corrosão estrutural OU topologia AC OU sistema regulado por norma explícita |
| **Tier A** (premium recalibrado) | 51 notas | TL;DR 9-10 regras + Danger 9-10 cenários + Glossário 50-90 termos + normas 30-65 itens | Componente operacional médio-risco, nota técnica padrão 180-300 linhas, regulação multi-jurisdição |
| **Tier B** (DEC-11 light) | 12 notas | TL;DR 4 regras + Glossário 4-8 termos + frontmatter normalizado + sem danger callout | Nota-conceito curta, componente conveniência/acessório, escopo proporcional |
| **Tier C / MOC Plus** | mapas e MOCs | frontmatter normalizado + resumo de escopo + trilhas de leitura + agrupamento funcional + cross-links + quick-reference + fronteiras de escopo | MOCs, índices, guias e entrypoints |

## Padrão atual para MOCs

MOC não deve ser lista plana nem mini-apostila. O papel dele é reduzir tempo de decisão: orientar onde entrar, em que ordem ler, quando trocar de domínio e qual nota técnica resolve a pergunta.

Estrutura recomendada:

- frontmatter completo com `status: "moc-curated-plus"`;
- abstract curto explicando o domínio e quando usar;
- trilhas de leitura por intenção;
- notas por categoria funcional;
- links cruzados para domínios adjacentes;
- quick-reference com dúvidas recorrentes;
- "Quando NÃO entrar aqui" para evitar navegação errada;
- perguntas que a página responde.

Para MOCs, `normas_citadas: []` pode permanecer vazio quando a página apenas aponta para notas técnicas. Se o MOC trouxer prescrição normativa própria, preencher `normas_citadas` ou mover a prescrição para a nota técnica fonte.

## Template DEC-11 premium-l3 (referência)

Estrutura canônica para Tier S/A:

```yaml
---
title: "Nome da Nota"
note_type: "technical-note" # system, component, comparison, reference, procedure, moc
domain: "70_Hidraulica_Climatizacao_e_Utilidades"
status: "premium-l3"
fase_6_reescrita: NN
reviewed_on: "YYYY-MM-DD"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
review_level: "engineering-curated"
source_urls: [...]
aliases: [...]
seo_title: "..."
seo_description: "..."
seo_keywords: [...]
geo_queries: [...]  # 8-12 perguntas que o leitor faz
normas_citadas: [...]  # lista plana com docs canonicalizados
related_notes: [...]
---

# Título

> [!abstract] Resumo técnico
> Definição rigorosa em 1-2 parágrafos, cobrindo escopo + diferenciação + padrões aplicáveis + fabricantes dominantes.

> [!tldr] TL;DR — N regras inegociáveis
> 1. Regra 1...
> ...

> [!danger] Cenários de risco
> - Cenário com causa raiz + prevenção...
> ...

## O que é (definição rigorosa)
## Comparação técnica
## Onde se encaixa na arquitetura
## Fabricantes e modelos dominantes
## Instalação correta
## Falhas mais comuns (com causa raiz e diagnóstico)
## Diagnóstico profissional
## Boas práticas operacionais
## Erros comuns
## Glossário (termos técnicos)
## Integração com outras notas
## Perguntas que esta nota responde
```

## Convenções editoriais críticas

### Wikilinks — em-dash (—), não hífen (-)

Validação `validate_vault.py` retorna **exit 1** com wikilink quebrado. **Causa documentada do CI failure histórico.**

✅ Correto:
- `[[Fusíveis DC — Proteção Contra Sobrecorrente]]`
- `[[Detector de CO — Monóxido de Carbono]]`
- `[[Automação de Bordo — Sistemas Domoticos]]`
- `[[Óleos Hidráulicos Marine — Guia Completo]]`
- `[[Proteção Dr]]` (não `[[DR (Dispositivo Diferencial Residual)]]`)
- `[[Inversora (DC To AC)]]` (não `[[Inversor (DC To AC)]]`)

❌ Errado:
- `[[Fusíveis DC - Proteção Contra Sobrecorrente]]` (hífen)
- `[[DR (Dispositivo Diferencial Residual)]]` (alias, não título)
- `[[Bateria Náutica]]` (não existe)

**Antes de criar wikilink novo, validar contra `ls 70_Hidraulica_Climatizacao_e_Utilidades/` ou similar.**

### Citação normativa

Sempre incluir:

- **Documento + edição/ano + cláusula + contexto + limitação assumida**

Exemplo correto:

> "Projeto de entrada AC analisado à luz da filosofia de proteção da **ABYC E-11 (2023) cláusulas 11.4 + 11.5 + 11.16**, complementado por **ISO 13297:2020** para harmonização internacional e **ABNT NBR 14728** para princípios de BT no Brasil, com enquadramento regulatório segundo **DPC NORMAM-211/DPC** vigente."

Exemplo errado:

> "Sistema conforme ABYC."

Para qualquer dúvida normativa, consultar a nota mestre **`10_Fundamentos_e_Projeto/Normas e Regulamentações — Abyc Iso e Brasil.md`** que canonicaliza 340+ documentos em 10 famílias (IMO, IHO, ITU, ISO, IEC, ABYC/USCG/NFPA/UL, EU MED/RCD/LVD/EMC, ABNT/DPC NORMAM/ANATEL/INMETRO, classification societies, setoriais).

### Normas a evitar (sensitive references)

O validador alerta para:

- `NORMAM-02` (antiga) → usar **NORMAM-211/DPC** (esporte e recreio) ou **NORMAM-201/DPC** (comerciais).
- `ABYC TE-13` (errado) → usar **ABYC E-13** (Lithium Ion Batteries).
- `ISO 10133` (aposentada) → usar **ISO 28848** (DC) e **ISO 13297** (AC).
- `NBR 13885` / `ABNT NBR 16033` (validação pendente) → manter `<!-- TODO-CITAÇÃO -->`.

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
- A saúde operacional dos PDFs e a fila de OCR são tratadas por `audit_pdf_toolchain.py`.
- OCR pesado deve ser feito por `ocr_priority_pdfs.py`, gerando sidecars `.txt` e `.md` em `_Dados_Acervo` sem alterar o PDF original.
- A separação humano/técnico, fila de curadoria e enriquecimento assistido das notas prioritárias são tratados por `build_curation_dashboard.py`.
- A rotina completa e propagável para PDF novo deve ser feita por `run_pdf_pipeline.py`.

## Comandos de validação

Rodar antes de concluir qualquer lote:

```powershell
python scripts/check_python_scripts.py    # syntax dos scripts Python
python scripts/validate_vault.py          # 0 erros bloqueantes (exit 1 se falhar)
python scripts/validate_audit_yaml.py     # YAMLs de fase 1-6 em _Editorial
python scripts/check_source_urls.py       # source_urls válidos no frontmatter
python scripts/build_manifest.py          # manifest/content-manifest.json
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
- Documentar decisões estruturais como **DEC-NN** em `_Editorial/plano_execucao_auditoria.md` (atualmente DEC-01 a DEC-41).
- YAMLs de auditoria em `_Editorial/fase_*.yaml` — gerados por onda, validados por `validate_audit_yaml.py`.
- Não editar manualmente artefatos gerados sem entender qual script os recria.
- Não apagar arquivos do acervo para "limpar"; preferir arquivamento reversível ou staging fora de escopo.

## Ferramentas esperadas

**Core:**

- `python 3.12+`
- `git`
- `gh` (quando autenticado — para Actions/PRs)
- `rg` / `ripgrep`
- `fd` (file finder)
- `jq` (JSON query)
- `fzf` (fuzzy finder)
- `uv` (Python package manager)

**PDF/OCR (acervo):**

- `pdftotext` (Poppler)
- `pdfinfo`
- `qpdf`
- `exiftool`
- `tesseract`
- `mutool`
- `magick`
- `gswin64c` (Ghostscript)
- `7z`

**Web/Publicação:**

- `node` + `npm`

## Não fazer

- Não inventar norma, código ABNT, exigência da Marinha, ABYC ou ISO.
- Não citar `NORMAM-02` antigo, `ISO 10133` aposentada, ou `ABYC TE-13` (errado).
- Não usar hífen (-) em wikilinks de títulos compostos — usar em-dash (—).
- Não criar wikilink para nota inexistente sem confirmar primeiro com `ls dominio/`.
- Não misturar acervo principal curado com staging bruto.
- Não promover PDF pessoal ou fora de escopo para o acervo principal.
- Não tratar nota automática como curadoria humana final.
- Não transformar MOC em nota técnica com Danger callouts e normas excessivas — escopo proporcional.
- Não reescrever tudo sem motivo.
- Não remover mudanças existentes que não foram feitas por você.
- Não pushar com erros bloqueantes do `validate_vault.py` — CI vai falhar.
