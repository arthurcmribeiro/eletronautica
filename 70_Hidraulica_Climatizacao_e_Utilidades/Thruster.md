---
title: "Thruster"
note_type: "technical-note"
domain: "70_Hidraulica_Climatizacao_e_Utilidades"
source_file: "THRUSTER 0f519734f7fb82dea40b017c2a10e5ae.md"
status: "technical-review-l1"
review_level: "engineering-curated"
aliases:
  - "THRUSTER"
  - "Bow thruster"
  - "Stern thruster"
seo_title: "Thruster em embarcações: banco dedicado, cabos, contatores e falhas"
seo_description: "Guia técnico sobre thrusters elétricos e hidráulicos: demanda de corrente, banco dedicado, queda de tensão, contatores, túnel, duty cycle e integração com baterias e BMS."
seo_keywords:
  - "thruster embarcação"
  - "bow thruster boat"
  - "bateria thruster"
  - "queda de tensão thruster"
geo_queries:
  - "Por que o thruster fica fraco ou faz o BMS cortar no barco?"
  - "Como especificar corretamente cabos e banco de baterias para thruster?"
related_notes:
  - "Bancos de Bateria"
  - "BMS — Battery Management System"
  - "Dimensionamento de Cabos DC — Cálculo Prático"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Monitor de Bateria - BMV - Shunt"
  - "Plataforma de Popa Elétrica - Hidráulica"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
---

# Thruster

> [!abstract] Resumo técnico
> O `thruster` é uma carga transitória de alta demanda, com forte sensibilidade a queda de tensão, qualidade do banco, contatores, tempo de uso e estado mecânico do conjunto. Muitos problemas atribuídos ao equipamento nascem, na verdade, da arquitetura elétrica que o alimenta.

## O que é

Thruster é o propulsor auxiliar destinado a gerar força lateral para manobras.

As arquiteturas mais comuns são:

- `bow thruster`;
- `stern thruster`;
- sistemas elétricos ou hidráulicos;
- versões em túnel, externas ou retráteis, conforme o projeto da embarcação.

## O que realmente define o desempenho

O desempenho final não depende só do motor do thruster. Ele depende de:

- compatibilidade entre empuxo e porte da embarcação;
- qualidade da instalação hidrodinâmica;
- capacidade do banco ou da fonte de energia;
- queda de tensão no circuito;
- condição dos contatores e comandos;
- respeito ao regime de uso.

É um erro comum discutir thruster apenas em termos de “kgf” ou potência.

## Arquitetura elétrica

Em versões elétricas, os pontos centrais são:

- corrente muito alta por períodos curtos;
- sensibilidade extrema à queda de tensão;
- necessidade frequente de banco dedicado ou alimentação muito bem planejada;
- coordenação entre proteção, contatores e cabos.

Ver também:

- [[Bancos de Bateria]]
- [[BMS — Battery Management System]]
- [[Dimensionamento de Cabos DC — Cálculo Prático]]

## Banco dedicado ou compartilhado

Muitas embarcações adotam banco dedicado próximo ao thruster por uma razão simples: reduzir percurso de corrente alta e proteger o restante da arquitetura.

Compartilhar banco pode funcionar, mas exige validar:

- corrente de pico admissível;
- comportamento do BMS, se houver lítio;
- queda de tensão no trajeto completo;
- impacto sobre outros consumidores sensíveis.

## Cabos, contatores e proteção

O thruster pune qualquer improviso em:

- seção de cabo;
- comprimento de percurso;
- qualidade de conexão;
- estado dos contatores;
- coordenação da proteção.

O fusível ou dispositivo equivalente deve proteger o circuito sem transformar a operação normal em disparo crônico.

Ver também:

- [[Fusíveis DC — Proteção Contra Sobrecorrente]]

## Duty cycle e limite térmico

Thruster não é propulsão contínua.

O uso prolongado acima do permitido gera:

- aquecimento;
- queda de desempenho;
- desgaste elétrico e mecânico;
- aumento de risco de falha.

O limite exato depende do fabricante, da potência e do ambiente de instalação.

## Interface mecânica e hidrodinâmica

Mesmo com circuito elétrico impecável, o desempenho cai se houver:

- incrustação;
- túnel mal dimensionado ou sujo;
- folga excessiva;
- hélice ou conjunto danificados;
- entrada de água inadequada em alguns tipos construtivos.

## Falhas mais comuns

As falhas recorrentes são:

- queda de tensão excessiva;
- banco incapaz de sustentar o pico;
- BMS limitando descarga;
- contator fatigado;
- degradação mecânica no conjunto propulsor;
- uso acima do duty cycle;
- falsa expectativa de desempenho para o porte do barco.

## Diagnóstico profissional

Perguntas essenciais:

1. A tensão no equipamento durante a manobra permanece aceitável?
2. O banco ou fonte de energia suporta o pico real?
3. Os contatores e conexões estão íntegros?
4. O problema é elétrico, mecânico ou de dimensionamento?

Ensaios úteis:

- medir tensão diretamente no thruster durante acionamento;
- medir corrente real, quando possível;
- inspecionar aquecimento anormal em cabos e contatores;
- verificar histórico de corte de BMS ou fusível;
- inspecionar túnel, hélice e incrustação.

## Boas práticas

- projetar o sistema completo, não apenas comprar o equipamento;
- encurtar ao máximo o percurso de alta corrente;
- validar banco e BMS com margem realista;
- respeitar o duty cycle;
- incluir o thruster no plano de manutenção e inspeção subaquática.

## Erros comuns

- escolher thruster sem validar arquitetura elétrica;
- confiar em cabo “aproximado” para corrente muito alta;
- compartilhar banco sem análise de pico;
- culpar o thruster por problema de contatores ou tensão;
- usar o equipamento como se fosse propulsão contínua.

## Integração com outras notas

- [[Bancos de Bateria]]
- [[BMS — Battery Management System]]
- [[Dimensionamento de Cabos DC — Cálculo Prático]]
- [[Fusíveis DC — Proteção Contra Sobrecorrente]]
- [[Monitor de Bateria - BMV - Shunt]]
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]]

## Perguntas que esta nota responde

- Por que o thruster perde força ou faz a eletrônica sofrer?
- Quando vale usar banco dedicado?
- Como diferenciar falha elétrica de falha mecânica em thruster?
