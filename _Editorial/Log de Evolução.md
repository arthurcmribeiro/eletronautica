---
title: "Log de Evolução"
note_type: "audit-report"
domain: "_Editorial"
status: "active-log"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
---

# Log de Evolução

## 2026-04-14 — Lote 0 — Higiene estrutural da automação

- Confirmado que `scripts/vault_tools.py` estava varrendo o espelho `.claude/worktrees/agitated-hugle`.
- Corrigido o escopo dos scanners para excluir `.claude` e `_visuals`.
- Revalidado o vault real: `140` notas, `0` erros, `0` avisos.
- Regenerado `manifest/content-manifest.json` com o corpus correto.

## 2026-04-14 — Lote 1 — Auditoria editorial da base

- Mapeada a estrutura por domínio, tipo de nota e entrypoints.
- Confirmado que o vault principal não possui notas órfãs reais.
- Identificadas notas pouco integradas:
  - `USB 12V (Power)`
  - `Limpador de Parabrisas`
- Identificados problemas críticos:
  - escopo incorreto dos scripts;
  - ausência de sistema visual versionável;
  - rascunhos úteis presos fora do vault principal.
- Criados:
  - `Auditoria Geral da Base`
  - `Backlog de Evolução Editorial`
  - `Log de Evolução`

## Próximo lote planejado

- Implantar a camada `_visuals/` com specs, gerador e outputs.
- Gerar os três primeiros visuais obrigatórios.
- Reforçar a camada de mapas com hubs transversais e nota de referência rápida.

## 2026-04-14 — Lote 2 — Camada visual inicial e reforço de navegação

- Implantada a estrutura `_visuals/specs/`, `_visuals/generated/` e `scripts/visuals/`.
- Gerados os três primeiros visuais obrigatórios:
  - `onda-pura-vs-onda-quadrada`
  - `50hz-vs-60hz`
  - `bateria-zona-util-vs-recarga`
- Integrados os visuais nas notas:
  - `DC vs AC — Corrente Contínua e Alternada`
  - `Inversora (DC To AC)`
  - `Tipos de Bateria`
- Reforçado `Fundamentos da Elétrica Náutica` com hubs transversais para diagnóstico, segurança e referência rápida.
- Documentada a camada visual no `README.md`.
- Ajustado `.gitignore` para manter `.claude/` e `.obsidian/graph.json` fora do versionamento.

## Próximo lote recomendado

- Revisar `USB 12V (Power)` e `Limpador de Parabrisas` para aumentar integração interna.
- Criar a segunda onda de visuais focada em `shore power`, `bonding`, `DR` e `NMEA`.
- Estender CI para validar geração mínima dos specs visuais.
