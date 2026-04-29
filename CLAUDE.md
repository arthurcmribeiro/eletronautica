# CLAUDE.md

Leia primeiro `AGENTS.md`. Este arquivo é um resumo operacional para trabalhar com esta vault sem depender do histórico do chat.

## Papel do Claude nesta base

- Atuar como agente técnico/editorial da base de elétrica náutica.
- Manter português do Brasil, clareza técnica e rastreabilidade.
- Tratar o repositório como Obsidian vault, acervo técnico e futura base para ensino, SEO/GEO, site, apostila e automações.

## Estado atual (Caminho B 100% fechado)

- **137 notas técnicas processadas** com template DEC-11 premium em 11 ondas (Fase 6).
- **Norma mestre estrutural:** `10_Fundamentos_e_Projeto/Normas e Regulamentações — Abyc Iso e Brasil.md` — source-of-truth com 340+ docs canonicalizados.
- **12 DECs ativos** (DEC-30 a DEC-41) — ver `_Editorial/plano_execucao_auditoria.md`.
- **Próximo passo:** Fase 7 (a definir) + curadoria humana do conteúdo técnico.

## Rotina curta

Antes de editar:

```powershell
git status --short
rg --files
```

Depois de editar:

```powershell
python scripts/check_python_scripts.py
python scripts/validate_vault.py          # exit 1 se houver erro
python scripts/validate_audit_yaml.py
python scripts/build_manifest.py
```

Se mexer no acervo:

```powershell
python scripts/acervo/run_pdf_pipeline.py
```

## Sistema de tiers (uso prático)

- **Tier S:** vida/fogo/explosão/corrosão estrutural OU AC topology OU norma explícita → template full DEC-11 (TL;DR 9 + Danger 5-9 + Glossário 15-25 + normas canonicalizadas).
- **Tier A:** componente operacional médio-risco, 180-300 linhas → premium recalibrado (TL;DR 9-10 + Danger 9-10 + Glossário 50-90 + normas 30-65).
- **Tier B:** componente conveniência, escopo proporcional → DEC-11 light (TL;DR 4 + Glossário 4-8 + sem danger).
- **Tier C:** MOC, índice, guia → frontmatter only (status + normas vazio + manter conteúdo).

## Convenções críticas (não esquecer!)

### Wikilinks com em-dash (—), nunca hífen (-)

CI failure histórico foi causado por wikilinks errados. Antes de criar link, confira o título exato via `ls`:

✅ `[[Fusíveis DC — Proteção Contra Sobrecorrente]]`
✅ `[[Detector de CO — Monóxido de Carbono]]`
✅ `[[Automação de Bordo — Sistemas Domoticos]]`
✅ `[[Proteção Dr]]` (não DR)
✅ `[[Inversora (DC To AC)]]` (não Inversor)
✅ `[[Bancos de Bateria]]` (não Bateria Náutica)

### Citação normativa = doc + edição/ano + cláusula

Sempre. Para qualquer norma, consultar a nota mestre:

`10_Fundamentos_e_Projeto/Normas e Regulamentações — Abyc Iso e Brasil.md`

### Normas a evitar

- `NORMAM-02` antigo → **NORMAM-211** ou **201**
- `ABYC TE-13` errado → **ABYC E-13**
- `ISO 10133` aposentada → **ISO 28848** (DC) e **ISO 13297** (AC)

## Regra crítica do acervo

- `_Acervo_Local` é o acervo físico.
- `_Acervo_Notas` é a camada Markdown companheira.
- `Acervo do humano/` é staging, não acervo principal curado.
- O acervo principal deve seguir `Sistema/Marca/Familia/arquivo.pdf`.
- Não deixar PDF solto na raiz de `_Acervo_Local`.
- Cada PDF do acervo principal deve ter uma nota `.md` companheira.
- Preservar sempre `CURADORIA-HUMANA:START/END`.
- Rodar `audit_pdf_toolchain.py` para manter páginas, metadados, `qpdf` e fila de OCR atualizados.
- Rodar `ocr_priority_pdfs.py --priority alta` para gerar OCR auxiliar sem sobrescrever PDFs originais.
- Rodar `build_curation_dashboard.py` para manter painel de curadoria, separação humano/técnico e enriquecimento assistido das notas prioritárias.
- Preferir `run_pdf_pipeline.py` quando a tarefa for atualizar o acervo após entrada de PDF novo.

## Onde recuperar contexto

**Estado da vault e auditoria:**

- `_Editorial/Log de Evolução.md`
- `_Editorial/plano_execucao_auditoria.md` (DECs + ondas Fase 6)
- `_Editorial/Padrão da Biblioteca de Referência Técnica.md`
- `_Editorial/Restauração de Contexto — Acervo e Conteúdo.md`
- `_Editorial/Ponto de Retomada — Acervo Notas e Curadoria.md`

**Norma mestre estrutural:**

- `10_Fundamentos_e_Projeto/Normas e Regulamentações — Abyc Iso e Brasil.md`

**Acervo:**

- `90_Revisao_Manual/README.md`
- `90_Revisao_Manual/00_Entrada_e_Controle/Portal do Acervo — Biblioteca de Referência.md`
- `90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado.md`
- `90_Revisao_Manual/10_Indices_e_Paineis/Acervo Local — Índice Gerado.md`
- `90_Revisao_Manual/10_Indices_e_Paineis/Painel de Curadoria do Acervo.md`

## Quando criar conteúdo técnico

- **Tier S/A:** template DEC-11 premium-l3 (ver `AGENTS.md` ou nota Fase 6 já feita como referência).
- Reforçar resumo técnico (abstract callout) + TL;DR (tip callout) + Danger callout + Glossário + normas canonicalizadas.
- Aplicar `normas_citadas` no frontmatter como lista plana.
- Sempre incluir `source_urls` no frontmatter para notas técnicas.
- Sempre incluir `reviewed_on` + `review_jurisdiction`.
- Para **Tier B**: TL;DR 4 regras + Glossário 4-8 + frontmatter completo (sem danger callout).
- Para **Tier C**: apenas normalizar frontmatter (status + normas vazio).
- Não transformar rascunho automático em material de ensino sem revisão humana.
- Separar valor típico, referência prática e valor normativo.

## Quando criar visual

- Preferir specs versionáveis em `_visuals/specs/*.json` e geração por Python.
- Saída esperada: SVG, PNG e Markdown de apoio em `_visuals/generated/`.
- Visual deve ensinar claramente algo técnico, não decorar.
- Após criar spec, rodar `python scripts/visuals/render_visuals.py` + `integrate_visuals.py`.

## Fechamento de lote

Um lote só está pronto quando:

- scripts compilam (`check_python_scripts.py` OK);
- vault valida sem erro (`validate_vault.py` exit 0 = 0 erros);
- YAMLs de auditoria validam (`validate_audit_yaml.py`);
- manifesto regenerado (`build_manifest.py`);
- mudanças relevantes registradas no `_Editorial/Log de Evolução.md`;
- DECs novos documentados em `_Editorial/plano_execucao_auditoria.md`;
- commit com mensagem descritiva (formato dos commits da Fase 6 como referência);
- estado final explicável em poucas linhas.

## Antes de pushar para GitHub

- `validate_vault.py` retorna **exit 1** com erros — CI vai falhar.
- Wikilinks quebrados são a causa #1 de erro bloqueante.
- Confirmar com `python scripts/validate_vault.py` antes de cada commit/push.
