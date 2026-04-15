---
title: "Backlog de Evolução Editorial"
note_type: "audit-report"
domain: "_Editorial"
status: "working-draft"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
---

# Backlog de Evolução Editorial

## Revisão editorial

- `[x]` Auditar a estrutura real do vault e separar o corpus principal do espelho operacional em `.claude/worktrees`.
- `[x]` Reforçar frontmatter e consistência editorial dos entrypoints de `00_Mapas`.
- `[ ]` Revisar `USB 12V (Power)` e `Limpador de Parabrisas` para ampliar integração interna.
- `[x]` Consolidar uma segunda camada de hubs transversais para energia, diagnóstico e segurança.

## Reforço didático

- `[x]` Criar `MOC — Diagnóstico e Manutenção`.
- `[x]` Criar `MOC — Segurança Integrada`.
- `[x]` Criar `Referência Rápida — Valores de Campo` como nota de apoio de consulta.
- `[x]` Inserir recursos visuais diretamente nas notas-alvo com explicação curta e link para asset de apoio.

## Melhoria estrutural

- `[x]` Corrigir `scripts/vault_tools.py` para excluir `.claude` e `_visuals`.
- `[x]` Documentar a arquitetura da camada visual no `README.md`.
- `[ ]` Avaliar inclusão de auditoria programática adicional para métricas editoriais.
- `[ ]` Estudar expansão do workflow para validar a camada visual em CI.

## Criação de visual

- `[x]` Implantar `_visuals/specs/`, `_visuals/generated/` e `scripts/visuals/`.
- `[x]` Gerar `onda-pura-vs-onda-quadrada`.
- `[x]` Gerar `50hz-vs-60hz`.
- `[x]` Gerar `bateria-zona-util-vs-recarga`.
- `[x]` Ajustar template visual para melhor alinhamento de título, resumo e cards.
- `[x]` Corrigir linguagem visual para padrão de cartilha/infográfico técnico, reduzindo o padrão repetitivo de caixas sequenciais.
- `[x]` Criar inventário visual completo por domínio.
- `[x]` Gerar lote amplo com visuais de projeto, cálculo, baterias, energia, proteção, rede, automação, utilidades e corrosão.
- `[x]` Criar integrador automático de visuais em notas-alvo.
- `[x]` Executar segunda onda com 24 novos visuais integrados nas notas-alvo.
- `[x]` Regenerar os `45` visuais com o novo template de cartilha/infográfico.
- `[x]` Gerar PNG em resolução lógica 2x para melhorar leitura em visualização ajustada à tela, mantendo SVG como master editável.
- `[ ]` Planejar terceira onda:
  - pacote de medição e diagnóstico;
  - pacote de distribuição DC;
  - pacote de navegação/comunicação;
  - pacote de segurança e alarmes;
  - pacote de utilidades eletromecânicas.
  - pacote de exemplos calculados e versões para slide/apostila.

## Criação de analogia

- `[x]` Explicitar a analogia de faixa de tensão em repouso para baterias de chumbo-ácido.
- `[ ]` Criar analogia visual controlada para diferenças entre AC e DC.
- `[ ]` Criar analogia visual para papel de PE, negativo DC, neutro e bonding sem misturar funções.

## Criação de exemplo calculado

- `[x]` Exemplo visual de queda de tensão em cabo DC.
- `[x]` Exemplo visual de autonomia do banco em função da carga.
- `[x]` Exemplo visual de RPM x frequência em gerador AC.
- `[ ]` Exemplo visual de corrente DC exigida por inversor em 12V versus 24V com cautela de pico/surto.
- `[ ]` Exemplo visual de leitura de shunt, SoC e corrente líquida.

## Reforço de fontes

- `[ ]` Fortalecer `source_urls` e observações de cautela em notas de síntese recém-criadas.
- `[ ]` Revisar notas de comparação com números práticos e garantir que todos sejam claramente apresentados como referência de campo quando não forem valores normativos rígidos.
- `[ ]` Criar convenção editorial para diferenciar “referência prática”, “valor típico” e “valor normativo”.

## Melhoria de frontmatter

- `[ ]` Padronizar `domain`, `status`, `reviewed_on` e `review_jurisdiction` nos principais MOCs e entrypoints.
- `[ ]` Revisar se `00_Mapas/Atlas Técnico.md`, `00_Mapas/Guia da Vault Curada.md` e `00_Mapas/MOC — Mapas.md` devem receber camada completa `seo_*`, `geo_queries` e `related_notes`.
- `[ ]` Definir convenção para metadados de notas editoriais e relatórios.

## Melhoria de links internos

- `[x]` Aumentar backlinks de `Atlas Técnico`, `Fundamentos da Elétrica Náutica` e `MOC — Mapas`.
- `[ ]` Incluir links transversais entre notas de diagnóstico, inspeção e manutenção.
- `[x]` Reforçar ligações entre `Tipos de Bateria`, `Monitor de Bateria`, `Bancos de Bateria` e futuros visuais.
- `[x]` Reforçar ligações entre `DC vs AC`, `Inversora`, `CAIS`, `Gerador (AC)` e visuais de forma de onda/frequência.
- `[x]` Integrar visualmente notas antes pouco conectadas como `USB 12V (Power)`.
