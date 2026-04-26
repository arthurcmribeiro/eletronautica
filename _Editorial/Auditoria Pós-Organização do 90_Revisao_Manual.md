---
title: "Auditoria Pós-Organização do 90_Revisao_Manual"
note_type: "audit-report"
domain: "_Editorial"
status: "working-draft"
reviewed_on: "2026-04-25"
review_jurisdiction: "Brasil"
---

# Auditoria Pós-Organização do 90_Revisao_Manual

## Escopo desta rodada

- Auditoria executada após a organização dos PDFs do `90_Revisao_Manual`.
- Ferramentas usadas:
  - `python scripts/check_python_scripts.py`
  - `python scripts/validate_vault.py`
  - `python scripts/build_manifest.py`
  - `python scripts/acervo/package_human_technical_archive.py --dry-run`
  - `python scripts/acervo/archive_human_duplicate_groups.py --dry-run --priority alta --priority media --priority baixa`
  - consultas programáticas sobre manifesto, backlinks, acervo local e notas companheiras.

## Resultado executivo

- A base está estável.
- O acervo principal voltou ao padrão esperado depois da remoção do PDF pessoal solto na raiz.
- Não há erro bloqueante, aviso do validador ou duplicata operacional pendente no staging técnico.
- O próximo ganho relevante não é reorganizar arquivos de novo; é melhorar metadado e automação de observabilidade.

## Snapshot atual

- notas analisadas: `560`
- scripts Python compilando: `20`
- erros de validação: `0`
- avisos de validação: `0`
- notas em `90_Revisao_Manual`: `410`
- notas `acervo-companion`: `371`
- notas do núcleo principal fora de `_Editorial/` e `90_Revisao_Manual/`: `140`
- órfãs reais no núcleo principal: `0`

## Estado do acervo físico

- arquivos em `_Acervo_Local`: `605`
- arquivos no staging `Acervo do humano`: `553`
- documentos no acervo principal curado:
  - `Climatizacao`: `6`
  - `Complementar-Brasil`: `3`
  - `Geradores`: `27`
  - `Navegacao`: `10`
- arquivos soltos na raiz de `_Acervo_Local`:
  - `README.md`
  - `acervo-download-queue-onan-lote01.json`
  - `acervo-download-queue.json`
  - `acervo-download-report-onan-lote01.json`
  - `acervo-download-report.json`
  - `acervo-local-index.json`
- PDFs soltos na raiz de `_Acervo_Local`: `0`

## Estado do staging humano

- itens técnicos ativos no staging humano: `325`
- renomeações planejadas: `0`
- ações previstas de arquivamento de duplicatas: `0`
- leitura prática:
  - a etapa de empacotamento está estabilizada;
  - a próxima etapa deve ser curadoria seletiva, não nova reorganização em massa.

## Estado da camada companheira

- notas companheiras totais: `371`
- origem:
  - `humano-staging`: `325`
  - sem `acervo_origin`: `46`
- extração:
  - `pdftotext`: `288`
  - `html-title-body`: `60`
  - `pdf-stream-strings`: `8`
  - `pdf-stream-strings-low-confidence`: `7`
  - `binary-no-text`: `7`
  - `no-text-detected`: `1`
- estágio de curadoria:
  - `triagem-automatica`: `357`
  - `curadoria-humana-parcial`: `14`

## Achados

### 1. Organização física corrigida

- O desvio anterior de PDF pessoal solto na raiz do acervo principal foi corrigido.
- O acervo principal voltou a ter apenas documentos técnicos organizados por sistema/marca/família e artefatos operacionais na raiz.
- A camada principal `_Acervo_Notas` voltou a `46` notas, que é o padrão esperado para o acervo principal curado.

### 2. O núcleo técnico segue saudável

- O corpus principal, fora de `_Editorial/` e `90_Revisao_Manual/`, tem `140` notas.
- Não há órfãs reais nesse núcleo.
- As notas com baixo backlink continuam concentradas em:
  - `00_Mapas/MOC — Mapas.md`
  - `60_Automacao_Conectividade_e_Monitoramento/USB 12V (Power).md`
  - `70_Hidraulica_Climatizacao_e_Utilidades/Limpador de Parabrisas.md`

### 3. Dívida de metadado continua nos MOCs e no acervo principal

- Há `10` notas sem `status`.
- Há `11` notas sem `reviewed_on` ou `review_jurisdiction`.
- A maior parte está em MOCs de `00_Mapas`.
- As `46` notas companheiras do acervo principal ainda não têm `acervo_origin`.
- Recomendação: preencher `acervo_origin: "acervo-principal"` nessas notas e ajustar o gerador para manter essa convenção.

### 4. Extração fraca está corretamente sinalizada

- Existem `54` notas companheiras com `text_extractable: nao`.
- Isso não é erro automático: o pipeline está sinalizando quando o material é imagem, HTML pobre, PDF sem texto útil ou extração fraca.
- O risco é editorial:
  - não usar essas notas como base de resumo técnico;
  - só promover para ensino, SEO ou material de oficina após OCR ou leitura humana.

## Recomendações priorizadas

### Prioridade 1

- Endurecer `scripts/acervo/build_pdf_companion_notes.py` para:
  - ignorar PDFs soltos na raiz de `_Acervo_Local`;
  - gerar `acervo_origin: "acervo-principal"` nas notas do acervo principal.

### Prioridade 2

- Padronizar frontmatter dos MOCs de `00_Mapas`, principalmente:
  - `status`
  - `reviewed_on`
  - `review_jurisdiction`

### Prioridade 3

- Criar fila editorial curta para os `54` itens com `text_extractable: nao`.
- Separar em três decisões:
  - OCR;
  - manter como referência visual;
  - arquivar/rebaixar por baixo valor técnico.

### Prioridade 4

- Continuar curadoria humana por valor de oficina, não por volume.
- Ordem recomendada:
  - `Geradores/Cummins-Onan`
  - `Geradores/Rehlko-Kohler`
  - `Climatizacao/Dometic`
  - `Navegacao/Raymarine` e `Navegacao/Garmin`

## Conclusão

- A organização física do `90_Revisao_Manual` está saudável.
- A automação está estável.
- O acervo principal voltou ao padrão esperado.
- O próximo lote deve ser pequeno e cirúrgico: blindar o gerador de notas companheiras e fechar metadados, em vez de reorganizar o acervo de novo.
