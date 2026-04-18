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

## 2026-04-15 — Lote 3 — Varredura visual ampla

- Ajustado o template visual para reduzir desalinhamento em títulos longos, resumo e cards de fluxo.
- Acrescentados tipos reutilizáveis ao renderer:
  - `flow_diagram`
  - `comparison_cards`
  - `cause_effect`
- Criadas specs adicionais para cobrir os principais temas visuais da base.
- Renderizados `21` visuais versionados em `svg`, `png` e `md` no total.
- Criado `scripts/visuals/integrate_visuals.py` para inserir blocos visuais em notas-alvo sem duplicação.
- Integrados `18` novos visuais diretamente em notas técnicas.
- Criado `Inventário Visual da Base` com cobertura atual, candidatos por domínio e fila recomendada.

## Próximo lote recomendado

- Criar pacote de medição e diagnóstico: multímetro, shunt, troubleshooting e inspeção.
- Criar pacote de distribuição DC: fusíveis, disjuntores, barramento, quadro e chaves.
- Criar pacote de navegação/comunicação: AIS, VHF, radar, piloto automático e chartplotter.

## 2026-04-15 — Lote 4 — Cartilha visual e segunda onda

- Registrado feedback editorial: os visuais anteriores estavam informativos, mas excessivamente parecidos e com pouca leitura humana aplicada.
- Redesenhado o renderer para linguagem de cartilha/infográfico técnico:
  - `flow_diagram` agora usa mapa de processo com eixo visual, estações numeradas, faixa de aplicação e erros comuns;
  - `comparison_cards` agora usa mapa comparativo radial, painéis de uso prático e leitura rápida;
  - `cause_effect` agora usa raciocínio diagnóstico em faixas progressivas.
- Otimizado o rasterizador local:
  - retângulos passaram a usar escrita por linha em vez de pixel a pixel;
  - PNG passou a ser gerado em resolução lógica 2x para melhorar leitura quando ajustado à tela.
- Criadas e renderizadas `24` novas specs, elevando a cobertura para `45` visuais em `svg`, `png` e `md`.
- Integrados `24` novos visuais em notas-alvo, mantendo idempotência do integrador.
- Atualizados `Inventário Visual da Base`, `Backlog de Evolução Editorial` e este log.

## Próximo lote recomendado

- Fazer revisão visual fina dos SVGs mais estratégicos para curso/apostila.
- Criar exemplos calculados específicos com números de campo e cautela explícita.
- Criar versões verticais/compactas dos melhores infográficos para slide, aula e publicação futura.

## 2026-04-18 — Lote 5 — Higiene final de versionamento

- Revisado o estado pós-rodada com validação estrutural completa: `147` notas, `0` erros, `0` avisos.
- Regenerado `manifest/content-manifest.json` para confirmar consistência do corpus atual.
- Reexecutado o pipeline visual: `45` specs confirmadas, `45` integrações já presentes e `0` notas alteradas pelo integrador.
- Identificado que `.obsidian/graph.json` seguia rastreado apesar de já constar no `.gitignore`.
- Ajustado o versionamento para retirar `graph.json` do Git e evitar ruído local recorrente de layout/zoom do Obsidian.
