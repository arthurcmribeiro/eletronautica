# Eletro Nautica

Vault curada de eletrica nautica com foco em Obsidian, governanca editorial e revisao Brasil-primeiro.

## O que este repositorio contem

- base tecnica em Markdown organizada por dominios;
- MOCs para navegacao no Obsidian;
- frontmatter editorial para SEO e GEO;
- scripts para validar links internos, metadados e referencias sensiveis;
- geracao de manifesto JSON para integracoes futuras;
- camada versionavel de visuais didaticos em SVG, PNG e Markdown de apoio.
- instrucoes persistentes para agentes em `AGENTS.md` e `CLAUDE.md`.

## Estrutura

- `00_Mapas/` mapas e MOCs da base
- `10_Fundamentos_e_Projeto/` fundamentos, projeto e normas
- `20_Baterias_e_Armazenamento/` bancos, BMS e litio
- `30_Energia_e_Conversao/` shore power, alternador, inversor e geracao
- `40_Distribuicao_Protecao_e_Aterramento/` distribuicao, DR, bonding e aterramento
- `50_` a `80_` dominios aplicados
- `_Editorial/` auditoria, lacunas e governanca editorial
- `_visuals/specs/` especificacoes declarativas dos visuais
- `_visuals/generated/` assets gerados e markdowns de apoio
- `90_Revisao_Manual/` acervo de revisao manual, com entrada/controle, indices gerados, matrizes, notas tecnicas e arquivo historico
- `scripts/` automacao local e validacoes
- `scripts/visuals/` pipeline local de geracao visual
- `manifest/` saidas geradas para integracoes

## Validacao local

```powershell
python scripts/check_python_scripts.py
python scripts/validate_vault.py
python scripts/build_manifest.py
python scripts/visuals/render_visuals.py
python scripts/visuals/integrate_visuals.py
```

## Acervo local e PDFs

PDFs do acervo principal devem ficar em `90_Revisao_Manual/_Acervo_Local/` usando o padrao `Sistema/Marca/Familia/arquivo.pdf`.

Para atualizar indices, auditoria, OCR auxiliar, notas companheiras e validacao:

```powershell
python scripts/acervo/run_pdf_pipeline.py
```

O validador bloqueia PDF solto na raiz do acervo principal e exige nota companheira para cada PDF curado.
O orquestrador gera `manifest/pdf-pipeline-last-run.json` e `_Editorial/Pipeline PDF - Ultima Execucao.md`, com status de cada etapa.
O auditor operacional gera `manifest/acervo-pdf-toolchain-audit.json` e `_Editorial/Auditoria Operacional PDF - Toolchain.md`, com paginas, metadados, status `qpdf`, texto pesquisavel e fila de OCR.
O OCR controlado gera texto auxiliar em `90_Revisao_Manual/_Dados_Acervo/ocr_texts/`, notas OCR em `90_Revisao_Manual/_Dados_Acervo/ocr_notes/` e manifesto em `90_Revisao_Manual/_Dados_Acervo/ocr-results.json`, sem sobrescrever os PDFs originais.
O painel de curadoria gera `manifest/acervo-curation-dashboard.json` e `90_Revisao_Manual/10_Indices_e_Paineis/Painel de Curadoria do Acervo.md`, com separacao humano/tecnico, OCR pendente e fila de notas prioritarias.

## Agentes

- `AGENTS.md` concentra as regras gerais para Codex, Claude e agentes futuros.
- `CLAUDE.md` traz a rotina curta para o Claude operar sem depender do historico do chat.

## O que a validacao verifica

- links `[[wikilinks]]` sem destino;
- ausencia de `title` e `note_type`;
- padroes normativos marcados como obsoletos ou divergentes;
- avisos para notas tecnicas sem data de revisao, jurisdicao ou fontes.

## Camada visual

Os visuais sao definidos em `_visuals/specs/*.json` e gerados localmente por `python scripts/visuals/render_visuals.py`.

Cada spec gera:

- `arquivo.svg` para embedding em notas, GitHub e futura publicacao web;
- `arquivo.png` para reaproveitamento rapido em apostila, slide ou mensageria;
- `arquivo.md` com objetivo didatico, cautelas e notas recomendadas para embedding.

O script `scripts/visuals/integrate_visuals.py` insere blocos de "Visual didatico" nas notas-alvo sem duplicar visuais ja integrados.

## GitHub Actions

O workflow em `.github/workflows/vault-check.yml` roda a validacao em `push`, `pull_request` e `workflow_dispatch`, gera `manifest/content-manifest.json`, renderiza `_visuals/generated/` e publica ambos como artefatos.

## Diretriz editorial atual

- Brasil primeiro para enquadramento regulatorio;
- ABYC e ISO como referencia de engenharia;
- fonte primaria obrigatoria em notas normativas e sensiveis;
- datas de revisao explicitas nas notas criticas.
