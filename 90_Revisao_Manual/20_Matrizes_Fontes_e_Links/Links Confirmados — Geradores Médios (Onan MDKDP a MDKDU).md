---
title: "Links Confirmados — Geradores Médios (Onan MDKDP a MDKDU)"
note_type: "inventory"
domain: "90_Revisao_Manual"
status: "active-curation"
reviewed_on: "2026-04-19"
review_jurisdiction: "Brasil"
aliases:
  - "Links Confirmados Geradores Médios Onan"
  - "Fontes Confirmadas MDKDP a MDKDU"
related_notes:
  - "MOC — Revisao Manual"
  - "Tabela-Mestre do Acervo — Biblioteca de Referência"
  - "Backlog Operacional — Coleta de Manuais"
  - "Matriz de Modelos e Versões — Geradores"
  - "Padrão da Biblioteca de Referência Técnica"
  - "Links Confirmados — Geradores Pequenos (Onan e Rehlko)"
---

# Links Confirmados — Geradores Médios (Onan MDKDP a MDKDU)

> [!abstract] Resumo tecnico
> Esta nota consolida a segunda leva real de captacao para geradores maritimos `Cummins / Onan`, agora no bloco medio `MDKDP` ate `MDKDU`. O foco desta passada foi fechar a trilha documental pratica por familia, com `manual operacional`, `service manual`, `parts manual`, `installation manual` e leitura de `motor-base / cilindros`.

## Criterio desta rodada

- manter o escopo estritamente `nautico`;
- usar `produto oficial Cummins` e `manual oficial do operador` como ancora principal;
- aceitar `dealer oficial / fonte oficial secundaria` para `service` e `parts`, quando isso for a melhor rota disponivel;
- usar `espelho externo` para `installation manual` quando ele realmente adiantar o trabalho;
- registrar explicitamente quando a familia mistura `motor-base` por `rating`, `Hz` ou `spec`.

## 1. Bloco medio `GEN-006` — `MDKDP`, `MDKDR`, `MDKDV`

- produto oficial da familia: [Onan Marine QD 13.5/17/17.5/19/21.5](https://selfscreening.cummins.com/en-in/generators/onan-marine-qd-1351717519215-kw-generator)
- operador oficial em portugues do Brasil: [Operator Manual PT-BR — A050G574](https://www.cummins.fr/wp-content/uploads/2020/10/A050G574-Issue-1-Portuguese-Brazil.pdf)
- service manual em fonte oficial secundaria: [Service Manual — A046J602](https://www.seapowermarine.com/seapowerwp/wp-content/uploads/2018/05/MDKDP-DR-DS-DT-DU-DV-Service-Manual.pdf)
- installation manual em espelho: [Installation Manual — A046J598](https://bazakonkurencyjnosci.funduszeeuropejskie.gov.pl/api/files/760932)
- parts manual `MDKDP / MDKDR / MDKDV`: [Parts Manual — A046L892](https://www.seapowermarine.com/seapowerwp/wp-content/uploads/2018/05/MDKDP-DR-DV-Parts-Manual.pdf)
- leitura operacional:
  - `service = espelho localizado`
  - `operacao = oficial localizado`
  - `parts = espelho localizado`
  - `installation = espelho localizado`
  - `pacote_triplo = sim`

### Motor-base e cilindros do `GEN-006`

- todos os modelos desta frente usam `4 cilindros`;
- `13.5 MDKDP` aponta para `Kubota V2003`;
- `17 MDKDP` e `21.5 MDKDR` apontam para `Kubota V2403` na trilha `E4BG`;
- `17.5 MDKDR` e `19 MDKDV` tambem caem no universo `Kubota V2403`, mas por literatura de motor e emissao de geracao anterior;
- conclusao pratica:
  - a familia `GEN-006` nao deve ser indexada com um unico `motor_base`;
  - a biblioteca deve registrar `Kubota V2003 / V2403` e detalhar isso por rating quando o download local comecar.

## 2. Bloco medio-alto `GEN-007` — `MDKDS`, `MDKDT`, `MDKDU`

- produto oficial da familia: [Onan Marine QD 22.5/27/29](https://selfscreening.cummins.com/generators/onan-marine-qd-2252729-kw-generator)
- operador oficial em portugues do Brasil: [Operator Manual PT-BR — A050G574](https://www.cummins.fr/wp-content/uploads/2020/10/A050G574-Issue-1-Portuguese-Brazil.pdf)
- service manual em fonte oficial secundaria: [Service Manual — A046J602](https://www.seapowermarine.com/seapowerwp/wp-content/uploads/2018/05/MDKDP-DR-DS-DT-DU-DV-Service-Manual.pdf)
- installation manual em espelho: [Installation Manual — A046J598](https://bazakonkurencyjnosci.funduszeeuropejskie.gov.pl/api/files/760932)
- parts manual `MDKDS / MDKDT / MDKDU`: [Parts Manual — A046J604](https://www.seapowermarine.com/seapowerwp/wp-content/uploads/2018/05/MDKDS-DT-DU-Parts-Manual.pdf)
- leitura operacional:
  - `service = espelho localizado`
  - `operacao = oficial localizado`
  - `parts = espelho localizado`
  - `installation = espelho localizado`
  - `pacote_triplo = sim`

### Motor-base e cilindros do `GEN-007`

- todos os modelos desta frente usam `4 cilindros`;
- `22.5 MDKDT` e `27 MDKDU` apontam para `Kubota V3300-E3BG`;
- `29 MDKDS` aponta para `Kubota V3300-E4BG`;
- conclusao pratica:
  - a familia `GEN-007` ja pode entrar na biblioteca com `motor_base = Kubota V3300-E3BG / V3300-E4BG`;
  - ao baixar os arquivos, vale separar `MDKDT-MDKDU` de `MDKDS` para evitar mistura de geracoes do motor.

## 3. Observacoes praticas de captura

- o `manual operacional` desta familia ja tem ancora oficial forte no portal `Cummins France`, inclusive em `pt-BR`;
- `service` e `parts` continuam mais faceis de trabalhar por `fonte oficial secundaria / dealer`;
- o `installation manual` desta frente aparece em espelho tecnico util e suficiente para destravar a organizacao do acervo;
- a combinacao `A046J602 + A046L892 / A046J604 + A046J598 + A050G574` ja deixa `GEN-006` e `GEN-007` em nivel operacional real.

## Proximo ganho direto

- separar, no acervo local, a trilha `GEN-006` por `V2003` versus `V2403`;
- abrir a proxima passada para `legado digital MDKBK ate MDKBV`, porque a literatura ja aponta motores-base especificos por subfamilia;
- se o objetivo virar biblioteca de oficina, a etapa seguinte nao e mais `achar portal`, e sim `baixar, nomear e curar`.
