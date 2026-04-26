# CLAUDE.md

Leia primeiro `AGENTS.md`. Este arquivo é um resumo operacional para trabalhar com esta vault sem depender do histórico do chat.

## Papel do Claude nesta base

- Atuar como agente técnico/editorial da base de elétrica náutica.
- Manter português do Brasil, clareza técnica e rastreabilidade.
- Tratar o repositório como Obsidian vault, acervo técnico e futura base para ensino, SEO/GEO, site, apostila e automações.

## Rotina curta

Antes de editar:

```powershell
git status --short
rg --files
```

Depois de editar:

```powershell
python scripts/check_python_scripts.py
python scripts/validate_vault.py
python scripts/build_manifest.py
```

Se mexer no acervo:

```powershell
python scripts/acervo/run_pdf_pipeline.py
```

## Regra crítica do acervo

- `_Acervo_Local` é o acervo físico.
- `_Acervo_Notas` é a camada Markdown companheira.
- `Acervo do humano/` é staging, não acervo principal curado.
- O acervo principal deve seguir `Sistema/Marca/Familia/arquivo.pdf`.
- Não deixar PDF solto na raiz de `_Acervo_Local`.
- Cada PDF do acervo principal deve ter uma nota `.md` companheira.
- Preservar sempre `CURADORIA-HUMANA:START/END`.
- Rodar `audit_pdf_toolchain.py` para manter paginas, metadados, `qpdf` e fila de OCR atualizados.
- Rodar `ocr_priority_pdfs.py --priority alta` para gerar OCR auxiliar sem sobrescrever PDFs originais.
- Rodar `build_curation_dashboard.py` para manter painel de curadoria, separacao humano/tecnico e enriquecimento assistido das notas prioritarias.
- Preferir `run_pdf_pipeline.py` quando a tarefa for atualizar o acervo apos entrada de PDF novo.

## Onde recuperar contexto

- `_Editorial/Log de Evolução.md`
- `_Editorial/Padrão da Biblioteca de Referência Técnica.md`
- `_Editorial/Restauração de Contexto — Acervo e Conteúdo.md`
- `_Editorial/Ponto de Retomada — Acervo Notas e Curadoria.md`
- `90_Revisao_Manual/README.md`
- `90_Revisao_Manual/00_Entrada_e_Controle/Portal do Acervo — Biblioteca de Referência.md`
- `90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado.md`
- `90_Revisao_Manual/10_Indices_e_Paineis/Acervo Local — Índice Gerado.md`
- `90_Revisao_Manual/10_Indices_e_Paineis/Painel de Curadoria do Acervo.md`

## Quando criar conteúdo

- Melhorar estrutura e utilidade sem inflar texto.
- Reforçar resumo técnico, aplicação prática, FAQ e links internos quando fizer sentido.
- Separar valor típico, referência prática e valor normativo.
- Não transformar rascunho automático em material de ensino sem revisão humana.

## Quando criar visual

- Preferir specs versionáveis e geração por Python.
- Saída esperada: SVG, PNG e Markdown de apoio.
- Visual deve ensinar claramente algo técnico, não decorar.

## Fechamento de lote

Um lote só está pronto quando:

- scripts compilam;
- vault valida sem erro;
- manifesto foi regenerado;
- mudanças relevantes foram registradas no log editorial;
- o estado final é explicável em poucas linhas.
