---
title: "Auditoria Geral da Base"
note_type: "audit-report"
domain: "_Editorial"
status: "working-draft"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
---

# Auditoria Geral da Base

## 1. Visão geral da estrutura do repositório

### Snapshot da abertura desta rodada

- Escopo real do vault curado: `140` arquivos Markdown.
- Conteúdo técnico/editorial útil: `139` notas fora de `_Editorial/`.
- Camada de mapas e navegação: `14` notas em `00_Mapas/`.
- Núcleo técnico principal: `125` notas fora de `00_Mapas/` e `_Editorial/`.

### Estrutura atual

- `00_Mapas/`: mapas de navegação, hubs e MOCs.
- `10_Fundamentos_e_Projeto/`: base conceitual, projeto, normas e cálculo.
- `20_Baterias_e_Armazenamento/`: baterias, BMS, monitoramento e química.
- `30_Energia_e_Conversao/`: shore power, gerador, inversor e conversão.
- `40_Distribuicao_Protecao_e_Aterramento/`: distribuição, proteção, aterramento e bonding.
- `50_Navegacao_Instrumentacao_e_Comunicacao/`: eletrônica de navegação e comunicação.
- `55_Iluminacao_e_Sinalizacao/`: iluminação funcional, regulamentar e de emergência.
- `60_Automacao_Conectividade_e_Monitoramento/`: telemetria, conectividade e automação.
- `70_Hidraulica_Climatizacao_e_Utilidades/`: utilidades eletromecânicas e sistemas auxiliares.
- `80_Seguranca_e_Corrosao/`: segurança integrada, alarmes, corrosão e mitigação.
- `90_Revisao_Manual/`: tópicos de revisão manual e sistemas específicos.
- `_Editorial/`: auditoria, backlog, manifestos editoriais e governança.
- `scripts/`: validação, manifesto e automação local.
- `manifest/`: artefatos gerados.

### Distribuição por tipo de nota

- `technical-note`: `80`
- `system`: `22`
- `moc`: `13`
- `component`: `9`
- `procedure`: `7`
- `comparison`: `4`
- `reference`: `2`
- `guide`: `1`
- `concept-note`: `1`

### Distribuição por domínio de conteúdo

- `70_Hidraulica_Climatizacao_e_Utilidades`: `26`
- `10_Fundamentos_e_Projeto`: `20`
- `40_Distribuicao_Protecao_e_Aterramento`: `19`
- `50_Navegacao_Instrumentacao_e_Comunicacao`: `15`
- `60_Automacao_Conectividade_e_Monitoramento`: `13`
- `30_Energia_e_Conversao`: `12`
- `55_Iluminacao_e_Sinalizacao`: `12`
- `80_Seguranca_e_Corrosao`: `8`
- `20_Baterias_e_Armazenamento`: `7`
- `90_Revisao_Manual`: `3`

## 2. Padrões editoriais detectados

### Frontmatter

Os campos mais frequentes hoje são:

- `title`
- `note_type`
- `domain`
- `source_file`
- `status`
- `aliases`
- `seo_title`
- `seo_description`
- `seo_keywords`
- `geo_queries`
- `related_notes`
- `reviewed_on`
- `review_jurisdiction`
- `source_urls`
- `review_level`

### Padrão de escrita

- Base `Markdown-first`, com headings claros e seções recorrentes.
- Notas maduras usam `Resumo técnico`, `O que é`, `Função`, `Problemas mais frequentes`, `Boas práticas`, `Erros comuns`, `FAQ` e `Integração com outras notas`.
- A linguagem dominante é técnica, pragmática, Brasil-primeiro e com boa utilidade de campo.
- A base já favorece SEO/GEO com `seo_*`, `geo_queries` e malha de `related_notes`.

### Padrão de navegação

- Há um MOC central forte em [Fundamentos da Elétrica Náutica](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/00_Mapas/Fundamentos da Elétrica Náutica.md:1>).
- Existem MOCs por domínio, mas alguns entrypoints ainda estão magros em metadados e reforço de backlinks.
- Não há notas órfãs reais no vault principal depois de excluir o espelho operacional em `.claude/worktrees`.

## 3. Lista de problemas críticos

### Crítico 1: scripts varriam o espelho operacional em `.claude/worktrees`

Na abertura desta rodada, `scripts/vault_tools.py` incluía `.claude/worktrees/agitated-hugle`, o que:

- duplicava o corpus;
- fazia a validação saltar de `140` para `284` notas;
- trazia rascunhos quebrados, wikilinks inválidos e `README.md` indevido para dentro do validador;
- contaminava o manifesto e qualquer métrica de knowledge base.

Status desta rodada:

- corrigido no lote estrutural inicial;
- `_visuals/` também entrou como diretório excluído dos scanners, evitando futura poluição de manifesto/validação.

### Crítico 2: inexistência de sistema versionável de conteúdo visual

Até esta rodada, a base não tinha:

- pasta padrão para specs de visuais;
- pipeline reusável local;
- ativos gerados versionáveis;
- camada de integração entre visuais e notas técnicas.

Isso limita:

- uso em aula e slide;
- reaproveitamento em PDF e site;
- clareza em tópicos que dependem fortemente de forma, fluxo e comparação.

Status desta rodada:

- resolvido com a implantação de `_visuals/specs/`, `_visuals/generated/` e `scripts/visuals/`;
- três visuais prioritários já foram gerados em `svg`, `png` e `md`;
- a integração inicial com notas-alvo já foi aplicada.

### Crítico 3: ativos e rascunhos valiosos presos fora da base principal

O espelho em `.claude/worktrees/agitated-hugle` contém rascunhos com potencial editorial, como:

- `MOC — Diagnóstico e Manutenção`
- `MOC — Segurança Integrada`
- `Referência Rápida — Valores de Campo`

Hoje eles não fazem parte do vault principal e, por isso, não ajudam navegação nem publicação.

Status desta rodada:

- resolvido para os três itens mais valiosos, agora promovidos ao vault principal;
- a camada de mapas passou a contar com hubs transversais de diagnóstico, segurança e referência rápida.

## 4. Lista de problemas médios

- `00_Mapas/Atlas Técnico.md` e `00_Mapas/Guia da Vault Curada.md` ainda estão mais leves em frontmatter do que o restante da base.
- `00_Mapas/MOC — Mapas.md` está funcional, mas ainda raso como hub.
- Os mapas principais têm baixa entrada por backlinks:
  - `Atlas Técnico`: `in=1`
  - `Fundamentos da Elétrica Náutica`: `in=1`
  - `MOC — Mapas`: `in=1`
- Há duas notas com integração fraca na malha principal:
  - `60_Automacao_Conectividade_e_Monitoramento/USB 12V (Power).md`
  - `70_Hidraulica_Climatizacao_e_Utilidades/Limpador de Parabrisas.md`
- O workflow atual valida Markdown e manifesto, mas ainda não contempla geração/verificação da futura camada visual.
- O workflow atual já contempla validação do vault, manifesto e geração da camada visual, mas ainda não verifica deriva entre spec e arquivos gerados.
- Ainda não existe camada explícita para exportação site/PDF/slides, apenas preparação estrutural.

## 5. Oportunidades de enriquecimento didático

- Criar hubs transversais por problema real de campo, não só por domínio:
  - diagnóstico e manutenção;
  - segurança integrada;
  - referência rápida de valores;
  - energia/autonomia.
- Adicionar exemplos calculados recorrentes:
  - queda de tensão em cabos DC;
  - autonomia real de banco;
  - corrente DC exigida por inversor;
  - efeito prático de frequência errada em gerador e shore power.
- Inserir analogias explícitas onde ajudam sem infantilizar:
  - bateria em repouso como “faixa de conforto/atenção/recarga”;
  - AC vs DC como transmissão vs armazenamento;
  - neutro/PE/bonding como papéis diferentes, não “todos os terras”.
- Criar blocos de “erro comum de campo” com visual próprio em notas de alto risco.

## 6. Oportunidades de conteúdo visual

### Matriz inicial de candidatos a visual

| Nota | Tipo de visual | Objetivo didático | Formato ideal | Prioridade |
| --- | --- | --- | --- | --- |
| `30_Energia_e_Conversao/Inversora (DC To AC)` | comparação de forma de onda | mostrar que mesma tensão nominal não implica mesma qualidade de energia | gráfico comparativo | alta |
| `10_Fundamentos_e_Projeto/DC vs AC — Corrente Contínua e Alternada` | comparação de frequência | separar frequência de tensão e mostrar impacto prático | gráfico comparativo | alta |
| `20_Baterias_e_Armazenamento/Tipos de Bateria` | faixa operacional com analogia | explicar zona útil de tensão em repouso | faixa/zona operacional | alta |
| `30_Energia_e_Conversao/CAIS (Pier) (AC)` | topologia de alimentação | comparar fase-neutro, fase-fase e split-phase | diagrama/topologia | alta |
| `40_Distribuicao_Protecao_e_Aterramento/Aterramento` | arquitetura de referência | diferenciar PE, negativo DC, bonding e neutro | diagrama de arquitetura | alta |
| `40_Distribuicao_Protecao_e_Aterramento/Proteção Dr` | causa e efeito | explicar desequilíbrio de corrente e disparo | fluxo/diagrama causal | alta |
| `40_Distribuicao_Protecao_e_Aterramento/Isolador Galvânico - Transformador de Isolamento` | quadro comparativo | comparar proteção parcial x barreira total | comparativo | alta |
| `20_Baterias_e_Armazenamento/Monitor de Bateria - BMV - Shunt` | fluxo de medição | explicar shunt, corrente e cálculo de SoC | diagrama de fluxo | média |
| `50_Navegacao_Instrumentacao_e_Comunicacao/NMEA 2000 - NMEA 0183 — Rede de Instrumentos` | arquitetura de rede | mostrar backbone, drops e integrações | diagrama de rede | média |
| `30_Energia_e_Conversao/Gerador (AC)` | relação causa/efeito | mostrar RPM x frequência x comportamento das cargas | curva/fluxo | média |
| `10_Fundamentos_e_Projeto/Dimensionamento de Banco de Baterias — Cálculo de Autonomia` | exemplo calculado | tornar autonomia visual e auditável | quadro calculado | média |
| `10_Fundamentos_e_Projeto/Dimensionamento de Cabos DC — Cálculo Prático` | exemplo calculado | mostrar bitola x corrente x queda de tensão | quadro comparativo | média |

## 7. Notas órfãs ou pouco integradas

### Estado real do vault principal

- Notas órfãs reais: `0`
- Notas pouco integradas (`<= 1` backlink): `2`

### Notas pouco integradas

- `60_Automacao_Conectividade_e_Monitoramento/USB 12V (Power).md`
- `70_Hidraulica_Climatizacao_e_Utilidades/Limpador de Parabrisas.md`

### Observação importante

As órfãs detectadas no início da rodada estavam concentradas no espelho `.claude/worktrees`, não no vault principal. Isso era sintoma de escopo incorreto dos scripts, e não de navegação deficiente do repositório principal.

## 8. Sugestões de MOCs ou reforço de links internos

### MOCs prioritários a reforçar

- `Atlas Técnico`
- `Fundamentos da Elétrica Náutica`
- `MOC — Mapas`

### MOCs transversais recomendados

- `MOC — Diagnóstico e Manutenção`
- `MOC — Segurança Integrada`

### Reforços de linking sugeridos

- Referenciar `USB 12V (Power)` a partir de notas de painel, tomadas, automação e energia DC.
- Referenciar `Limpador de Parabrisas` a partir de segurança, navegação em mau tempo e utilidades.
- Reforçar links para `Atlas Técnico` e `Fundamentos da Elétrica Náutica` nos entrypoints e materiais editoriais.

## 9. Oportunidades SEO/GEO

- Criar biblioteca visual reutilizável com nomes de arquivo estáveis e explicações Markdown indexáveis.
- Incluir visuais em notas com `alt text` forte e objetivo didático explícito.
- Reforçar notas-hub que respondem perguntas amplas:
  - por onde começar;
  - como diagnosticar;
  - o que revisar antes de navegar;
  - como comparar padrões elétricos.
- Aproveitar os futuros visuais como ativos reaproveitáveis em:
  - site;
  - PDF;
  - slides;
  - social snippets;
  - páginas de captura para materiais premium.

## 10. Recomendação de ordem de trabalho

### Ordem recomendada

1. Corrigir escopo dos scripts e blindar a automação contra diretórios operacionais.
2. Criar auditoria, backlog e log editorial para governança progressiva.
3. Implantar sistema versionável de visuais (`spec -> svg/png/md`).
4. Gerar os três primeiros visuais obrigatórios e integrá-los em notas-alvo.
5. Fortalecer a camada de mapas com hubs transversais e referência rápida.
6. Reforçar frontmatter e backlinks dos entrypoints de `00_Mapas`.
7. Planejar uma segunda onda de visuais para topologias AC, aterramento, DR e NMEA.

### Situação ao fim da fase de auditoria

- A base está estruturalmente forte para Obsidian.
- A governança editorial mínima já existe.
- A próxima alavanca de valor não é “reescrever tudo”, e sim:
  - corrigir pontos de arquitetura da knowledge base;
  - criar ativos visuais reutilizáveis;
  - fortalecer hubs e materiais de síntese.

## 11. Status ao fim da primeira rodada

- Auditoria editorial criada e versionada em `_Editorial/`.
- Backlog e log incremental criados para evolução por lotes.
- Camada visual inicial implementada com pipeline local e integração ao GitHub Actions.
- Três visuais prioritários já disponíveis para Obsidian, GitHub, site futuro, PDF e slides.
- Novos hubs transversais e uma nota de referência rápida já incorporados ao vault principal.
