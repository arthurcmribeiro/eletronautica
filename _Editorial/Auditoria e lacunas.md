---
title: "Auditoria Editorial e Lacunas"
note_type: "audit-report"
---

# Auditoria Editorial e Lacunas

## Escopo desta geração

- Conteúdo bruto preservado e migrado para notas curadas com frontmatter, títulos canônicos, wikilinks, MOCs e camada SEO/GEO.
- Esta camada ainda não substitui validação normativa linha a linha com fonte primária vigente de ABYC, ISO e regulação brasileira aplicável.

## Lote 1 revisado manualmente

- Aterramento, bonding, fusíveis, disjuntores, DR, shore power, isolação galvânica e a nota de fase/neutro receberam revisão de arquitetura AC/DC, proteção, equipotencialização e topologia.

## Lote 2 revisado manualmente

- Bancos de bateria, BMS, carregadores, LiFePO4, monitor de bateria, tipos de bateria, alternador, inversora, gerador AC e transformador de entrada foram revisados com foco em integração, limites reais e coordenação de fontes.

## Lote 3 revisado manualmente

- Todo o núcleo de fundamentos e projeto foi endurecido: DC/AC, lei de Ohm, dimensionamentos, diagrama unifilar, leitura de esquemas, normas, troubleshooting, manutenção, instrumentação básica e metodologia de projeto.

## Lote 4 revisado manualmente

- Toda a camada de navegação, instrumentação e comunicação foi revisada: NMEA, chartplotter, radar, VHF, AIS, DSC, EPIRB, MOB, piloto automático, heading sensor, sonda, estação de vento e navegação/luzes relacionadas.

## Lote 5 revisado manualmente

- O domínio de iluminação e sinalização foi revisado integralmente, separando luzes regulamentares, iluminação funcional, emergência e aplicações decorativas.

## Lote 6 revisado manualmente

- Automação, conectividade e monitoramento foram revisados com foco em rede, telemetria, IoT de bordo, alarmística, sensores, USB power e equipamentos de entretenimento.

## Lote 7 revisado manualmente

- Barramento DC, cabeamento, painel AC/DC, relés, terminais e chaves gerais foram revisados para consolidar a arquitetura de distribuição e montagem.

## Lote 8 revisado manualmente

- Detector de CO, detector de gás e alarme de alagamento/sensor de porão foram revisados como sistemas de segurança com critérios mais rigorosos de instalação e resposta operacional.

## Lote 9 revisado manualmente

- Chaves seletoras AC, contatores AC, divisores de carga DC, hotline, linha leve/pesada AC, ânodo, correntes parasitas, eletrólise e extintor automático receberam revisão forte de arquitetura, corrosão e proteção.

## Lote 10 revisado manualmente

- Arranque, carregador para tender/jet ski, geração eólica DC, gerador DC e placa solar DC foram revisados com foco em alta corrente, integração com banco e papel correto de cada fonte.

## Lote 11 revisado manualmente

- Ar-condicionado marine, blower, boiler, bomba de porão e sensor de nível de água foram reestruturados para separar HVAC, segurança de vapores, aquecimento de água, drenagem e desambiguação editorial entre sensores de tanque e de porão.

## Lote 12 revisado manualmente

- O cluster sanitário foi refeito: bomba de água pressurizada, bomba de águas negras, macerador, holding tank/Y-valve e bomba de banheiro agora têm escopos separados, coerência de sistema e linking forte.

## Lote 13 revisado manualmente

- Aquecedor de bordo, bomba do ar-condicionado, caixa de água cinza, dessalinizador, casa de máquinas e paiol, fogão/cooktop, geladeira/freezer e icemaker foram reescritos como notas técnicas de sistema, e não mais como textos genéricos de catálogo.

## Lote 14 revisado manualmente

- Thruster, catraca, guincho, davit/tender lift, flap, limpador de parabrisas, plataforma de popa, trim/tilt e estabilizador foram revisados como atuadores e sistemas de movimento, com correção explícita da nota `Estabilizador`, que passou a tratar estabilização de movimento e não regulagem de tensão.

## Lote 15 revisado manualmente

- `Fundamentos da Elétrica Náutica` foi reescrito como MOC central da vault, deixando de ser lista longa herdada e passando a funcionar como mapa de estudo, projeto e diagnóstico.

## Status atual da camada curada

- Não restam notas em `curated-v1` dentro de `obsidian_vault_curated`.
- Toda a camada curada está em `technical-review-l1`.
- A revisão feita nesta rodada atuou em três níveis ao mesmo tempo:
  - mérito técnico;
  - fronteira editorial entre notas;
  - malha de linking e função de cada nota dentro do Obsidian.

## Correções conceituais mais importantes

- `Estabilizador` deixou de tratar estabilizador de tensão e passou a tratar estabilização de movimento da embarcação.
- `Casa de Máquinas e Paiol` deixou de ser nota de iluminação e passou a ser nota de ambiente técnico/compartimento.
- `Dessanilizador` foi corrigido editorialmente para `Dessalinizador` como sistema de osmose reversa.
- `Sensor de Nível de Água` foi reescrito como nota de desambiguação editorial.
- `Bomba de Águas Negras` e `Macerador - Bomba de Águas Negras` passaram a ter fronteiras de escopo mais defensáveis.
- `Fundamentos da Elétrica Náutica` passou a ser um hub real.

## Sobreposição de escopo que ainda merece vigilância

- `Starlink` x `Wi-Fi a Bordo`: a separação WAN/LAN já existe, mas deve continuar disciplinada para evitar repetição futura.
- `Bomba de Águas Negras` x `Macerador - Bomba de Águas Negras`: a fronteira foi fortalecida, mas ainda merece observação editorial em futuras extrações didáticas.

## Notas que ainda podem ser enxugadas futuramente

- `Bancos de Bateria`
- `Tipos de Bateria`
- `Sensor de Nível Diesel`
- `Sensor de Nível de Água`

## Lacuna real remanescente

- A lacuna principal deixou de ser estrutural/editorial e passou a ser normativa: validar, nota por nota, os trechos sensíveis contra documentação primária vigente antes de transformar a base em material formal final de ensino, apostila ou consultoria.
