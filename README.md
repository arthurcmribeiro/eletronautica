# Eletro Nautica

Vault curada de elétrica náutica com foco em Obsidian, governança editorial e revisão Brasil-primeiro.

## Status atual da base

- **Fase 6 (Caminho B) 100% fechada** — 137/137 notas técnicas processadas com template DEC-11 premium.
- **Norma mestre estrutural** em `10_Fundamentos_e_Projeto/Normas e Regulamentações — Abyc Iso e Brasil.md` consolida 340+ documentos normativos canonicalizados em 10 famílias (IMO, IHO, ITU, ISO, IEC, ABYC/USCG/NFPA/UL, EU MED/RCD/LVD/EMC, ABNT/DPC NORMAM/ANATEL/INMETRO, classification societies).
- **12 DECs documentados** durante a auditoria (DEC-30 a DEC-41) — cobrem cadência auto-contínua, two-tier template, notas-filhas, taxonomia separadores, backfeed bomba porão, convenção de chaveamento, ISO 17479 macerador, retrofit DEC-26 refrigerantes, GL-4 vs GL-5.

## O que este repositorio contem

- base técnica em Markdown organizada por domínios;
- MOCs para navegação no Obsidian;
- frontmatter editorial com SEO/GEO + normas_citadas + status por tier;
- scripts para validar wikilinks, frontmatter, YAMLs de auditoria, source_urls e referências sensíveis;
- geração de manifesto JSON para integrações futuras;
- camada versionável de visuais didáticos em SVG, PNG e Markdown de apoio;
- pipeline completo de PDFs do acervo (curadoria, OCR, dashboards, companion notes);
- instruções persistentes para agentes em `AGENTS.md` e `CLAUDE.md`.

## Estrutura

- `00_Mapas/` — mapas e MOCs da base
- `10_Fundamentos_e_Projeto/` — fundamentos, projeto e **norma mestre estrutural**
- `20_Baterias_e_Armazenamento/` — bancos, BMS, lítio LiFePO4
- `30_Energia_e_Conversao/` — shore power, alternador, inversor, geração (solar, eólica)
- `40_Distribuicao_Protecao_e_Aterramento/` — distribuição AC/DC, DR/ELCI/GFCI, bonding e aterramento
- `50_Navegacao_Instrumentacao_e_Comunicacao/` — heading sensor, chartplotter, NMEA, anemômetro, autopilot, sonda
- `55_Iluminacao_e_Sinalizacao/` — luzes navegação, cabine, fitas LED, subaquática, strobo
- `60_Automacao_Conectividade_e_Monitoramento/` — automação, telemetria, sensores, alarmes
- `70_Hidraulica_Climatizacao_e_Utilidades/` — sanitário, galley, climatização, hidráulica, atuadores
- `80_Seguranca_e_Corrosao/` — ânodo, eletrólise, correntes parasitas, detectores, extintor
- `90_Revisao_Manual/` — acervo curado de PDFs, índices, matrizes, fila de OCR, painel de curadoria
- `_Editorial/` — auditoria, lacunas, governança editorial, YAMLs de fase, log de evolução
- `_visuals/specs/` — especificações declarativas dos visuais
- `_visuals/generated/` — assets SVG/PNG/MD gerados
- `scripts/` — automação local + validações
- `scripts/visuals/` — pipeline de geração visual
- `scripts/acervo/` — pipeline de PDFs (Codex/OpenAI)
- `manifest/` — saídas geradas (content-manifest, dashboards, OCR results)

## Sistema de tiers (Fase 6 Caminho B)

A base usa 4 níveis hierárquicos para escopo proporcional ao risco/regulação:

| Tier | Quantidade | Template | Critério |
|------|------------|----------|----------|
| **Tier S** (premium full) | 45 notas | TL;DR 9 regras + Danger 5-9 cenários + Glossário 15-25 + normas canonicalizadas (titulo/ano/cláusula) | Risco vida/fogo/explosão/corrosão estrutural OU topologia AC OU sistema regulado por norma explícita |
| **Tier A** (premium recalibrado) | 51 notas | TL;DR 9-10 + Danger 9-10 + Glossário 50-90 + normas 30-65 | Componente operacional médio-risco, nota técnica padrão 180-300 linhas |
| **Tier B** (DEC-11 light) | 12 notas | TL;DR 4 regras + Glossário 4-8 + frontmatter completo | Nota-conceito curta, componente conveniência/acessório |
| **Tier C** (frontmatter) | 16 MOCs | status + normas vazio + manter conteúdo | MOCs, índices, guias, README |

## Convenções editoriais

### Wikilinks (importante!)

- **Usar em-dash (—) em títulos compostos**, não hífen (-).
- Exemplos corretos:
  - `[[Fusíveis DC — Proteção Contra Sobrecorrente]]`
  - `[[Detector de CO — Monóxido de Carbono]]`
  - `[[Automação de Bordo — Sistemas Domoticos]]`
  - `[[Óleos Hidráulicos Marine — Guia Completo]]`
- Validação `validate_vault.py` falha com `Erros: N` se houver wikilink quebrado.

### Citação normativa

- Sempre incluir **edição/ano + cláusula + contexto**.
- Exemplo: `ABYC E-11.4.4.1.b (2023) — queda de tensão ≤3% sob carga`.
- A nota mestre **`10_Fundamentos_e_Projeto/Normas e Regulamentações — Abyc Iso e Brasil.md`** é a source-of-truth normativa: 340+ docs em 10 famílias, com hierarquia, comparação ABYC × ISO × Brasil, convenções de cor, vademecum por assunto e quando chamar especialista.

### Frontmatter premium-l3

```yaml
---
title: "Nome da Nota"
note_type: "technical-note" # ou system, component, comparison, reference, procedure, moc
domain: "70_Hidraulica_Climatizacao_e_Utilidades"
status: "premium-l3" # ou tier-b-curated, moc-curated, technical-review-l1
fase_6_reescrita: NN
reviewed_on: "YYYY-MM-DD"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
review_level: "engineering-curated"
source_urls: [...]
aliases: [...]
seo_title: "..."
seo_description: "..."
seo_keywords: [...]
geo_queries: [...]
normas_citadas: [...] # lista plana com docs canonicalizados
related_notes: [...]
---
```

## Validação local

```powershell
python scripts/check_python_scripts.py    # syntax dos scripts Python
python scripts/validate_vault.py          # 760 notas, ~37 avisos esperados, 0 erros
python scripts/validate_audit_yaml.py     # YAMLs de fase em _Editorial
python scripts/check_source_urls.py       # source_urls válidos
python scripts/build_manifest.py          # manifest/content-manifest.json
python scripts/visuals/render_visuals.py  # _visuals/generated/*.svg|png|md
python scripts/visuals/integrate_visuals.py
```

`validate_vault.py` retorna **exit 1** em caso de erros de wikilink/frontmatter — bloqueia o CI no GitHub Actions.

## Acervo local e PDFs

PDFs do acervo principal devem ficar em `90_Revisao_Manual/_Acervo_Local/` usando o padrão `Sistema/Marca/Familia/arquivo.pdf`.

Para atualizar índices, auditoria, OCR auxiliar, notas companheiras e validação:

```powershell
python scripts/acervo/run_pdf_pipeline.py
```

O validador bloqueia PDF solto na raiz do acervo principal e exige nota companheira para cada PDF curado.
O orquestrador gera `manifest/pdf-pipeline-last-run.json` e `_Editorial/Pipeline PDF - Ultima Execucao.md`, com status de cada etapa.
O auditor operacional gera `manifest/acervo-pdf-toolchain-audit.json` e `_Editorial/Auditoria Operacional PDF - Toolchain.md`, com páginas, metadados, status `qpdf`, texto pesquisável e fila de OCR.
O OCR controlado gera texto auxiliar em `90_Revisao_Manual/_Dados_Acervo/ocr_texts/`, notas OCR em `90_Revisao_Manual/_Dados_Acervo/ocr_notes/` e manifesto em `90_Revisao_Manual/_Dados_Acervo/ocr-results.json`, sem sobrescrever os PDFs originais.
O painel de curadoria gera `manifest/acervo-curation-dashboard.json` e `90_Revisao_Manual/10_Indices_e_Paineis/Painel de Curadoria do Acervo.md`, com separação humano/técnico, OCR pendente e fila de notas prioritárias.

## Agentes

- `AGENTS.md` concentra as regras gerais para Codex, Claude e agentes futuros (incluindo template DEC-11 premium-l3, convenções de wikilink e citação normativa).
- `CLAUDE.md` traz a rotina curta para o Claude operar sem depender do histórico do chat.

## O que a validacao verifica

- links `[[wikilinks]]` sem destino (erro bloqueante);
- ausência de `title` e `note_type` no frontmatter (erro bloqueante);
- referências normativas obsoletas/divergentes (aviso — `NORMAM-02` antigo, `ABYC TE-13` errado, etc.);
- frontmatter sem `source_urls` em notas técnicas (aviso);
- frontmatter sem `reviewed_on` ou `review_jurisdiction` em notas críticas (aviso);
- códigos ABNT marcados como inválidos no registro central (aviso).

## Camada visual

Os visuais são definidos em `_visuals/specs/*.json` e gerados localmente por `python scripts/visuals/render_visuals.py`.

Cada spec gera:

- `arquivo.svg` para embedding em notas, GitHub e futura publicação web;
- `arquivo.png` para reaproveitamento rápido em apostila, slide ou mensageria;
- `arquivo.md` com objetivo didático, cautelas e notas recomendadas para embedding.

O script `scripts/visuals/integrate_visuals.py` insere blocos de "Visual didático" nas notas-alvo sem duplicar visuais já integrados.

## GitHub Actions

O workflow em `.github/workflows/vault-check.yml` roda a validação em `push`, `pull_request` e `workflow_dispatch`, gera `manifest/content-manifest.json`, renderiza `_visuals/generated/` e publica ambos como artefatos.

## Stack de ferramentas locais

**Core:**

- `python 3.12+` (validação, manifest, render visual, pipeline PDF)
- `git` + `gh` (versionamento + Actions/PRs)
- `rg` / `ripgrep` (busca em texto)
- `fd` (file finder)
- `jq` (JSON query)
- `fzf` (fuzzy finder)
- `uv` (Python package manager)

**PDF/OCR (acervo):**

- `pdftotext` (Poppler)
- `pdfinfo`
- `qpdf`
- `exiftool`
- `tesseract` (OCR)
- `mutool`
- `magick` (ImageMagick)
- `gswin64c` (Ghostscript)
- `7z`

**Web/Site (camada de publicação):**

- `node` + `npm` (para `lei-de-ohm-calculos-basicos-web/` e futuros)

## Diretriz editorial atual

- **Brasil primeiro** para enquadramento regulatório (DPC NORMAM, ABNT NBR, Lei 9.605, ANATEL, INMETRO);
- **ABYC + ISO** como referência de engenharia (com edição/ano/cláusula explícita);
- **Multi-jurisdição** (USA + Internacional + Europa + Brasil) em notas premium para cobertura completa;
- **Fonte primária obrigatória** em notas normativas e sensíveis (sempre `source_urls` no frontmatter);
- **Datas de revisão explícitas** nas notas críticas (`reviewed_on` no frontmatter);
- **Em-dash (—) em títulos compostos**, não hífen, para consistência com convenções do vault;
- **Tier proporcional ao escopo** — não inflar Tier B/C com Danger callouts ou normas excessivas.

## Próximos passos (pós-Fase 6)

- **Fase 7** (a definir): manutenção contínua + Visual Layer ampliada + integração com automações (n8n) + camada de publicação web.
- **Curadoria humana** dos conteúdos premium-l3 dentro do Obsidian (ajuste de tom, foco, priorização).
- **Investigação** de eventual CI failure (autenticar `gh` para diagnóstico direto via `gh run view --log-failed`).
- **Setup de `pre-commit`** para rodar `validate_vault.py` antes de cada commit.
