---
title: "Catraca"
note_type: "technical-note"
domain: "70_Hidraulica_Climatizacao_e_Utilidades"
source_file: "CATRACA 93e19734f7fb835188a50199d626ca56.md"
status: "technical-review-l1"
review_level: "engineering-curated"
aliases:
  - "CATRACA"
  - "Capstan"
  - "Winch elétrico"
seo_title: "Catraca elétrica em embarcações: capstan, carga, cabos e falhas"
seo_description: "Guia técnico sobre catraca elétrica/capstan: tração de cabos, diferença para guincho de âncora, demanda de corrente, contatores, ergonomia e falhas em convés."
seo_keywords:
  - "catraca elétrica barco"
  - "capstan marine"
  - "winch elétrico embarcação"
  - "diferença catraca e guincho"
geo_queries:
  - "Qual a diferença entre catraca elétrica e guincho de âncora?"
  - "Por que a catraca fica fraca ou para sob carga no barco?"
related_notes:
  - "Guincho"
  - "Bancos de Bateria"
  - "Dimensionamento de Cabos DC — Cálculo Prático"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Thruster"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
---

# Catraca

> [!abstract] Resumo técnico
> A catraca elétrica, ou `capstan/winch` conforme o contexto, é um atuador de tração de cabos e linhas. Ela não deve ser confundida com o guincho de âncora. O desempenho depende de motor, redutor, contatores, alimentação elétrica, ergonomia de operação e compatibilidade entre carga real e sistema instalado.

## O que é

Nesta base, `Catraca` refere-se ao equipamento motorizado usado para tracionar cabo, corda ou manobra de convés, e não ao `windlass` de âncora.

Ela aparece em funções como:

- manobra de vela;
- movimentação de linhas;
- auxílio de içamento leve;
- apoio a operações de convés em embarcações específicas.

## Diferença para o guincho de âncora

Essa distinção precisa ser clara:

- [[Guincho]] trata de âncora e corrente;
- `Catraca` trata de tração de cabo/linha dentro de outra lógica mecânica e operacional.

Misturar os dois assuntos confunde seleção, proteção e manutenção.

## Arquitetura do sistema

Os elementos principais costumam ser:

- motor elétrico;
- redutor;
- tambor ou mecanismo de tração;
- contatores ou relés de potência;
- controle local por botão, pedal ou comando remoto;
- circuito de proteção;
- estrutura mecânica de convés.

## Carga real e regime de uso

A carga não é apenas o “peso” teórico do que se move.

É preciso considerar:

- atrito;
- enrolamento no tambor;
- ângulo de entrada da linha;
- choques de carga;
- operação intermitente;
- sobrecarga por manobra inadequada.

Em convés, a carga dinâmica costuma ser mais severa do que o operador imagina.

## Integração elétrica

Como em outros atuadores de convés, os pontos críticos são:

- corrente de pico;
- queda de tensão em percursos longos;
- qualidade das conexões expostas ao ambiente;
- coordenação de fusível/disjuntor e contatores;
- retorno elétrico confiável.

Ver também:

- [[Bancos de Bateria]]
- [[Dimensionamento de Cabos DC — Cálculo Prático]]
- [[Fusíveis DC — Proteção Contra Sobrecorrente]]

## Controles e segurança operacional

O sistema precisa permitir:

- operação com boa visibilidade da manobra;
- parada imediata;
- controle compatível com o risco de aprisionamento e chicote de cabo;
- entendimento claro de sentido e resposta do equipamento.

Em equipamentos de convés, ergonomia ruim vira risco real.

## Falhas mais comuns

As falhas recorrentes são:

- queda de tensão sob carga;
- contator fatigado;
- motor aquecendo ou perdendo torque;
- travamento mecânico ou sobrecarga de linha;
- cabo ou linha trabalhando fora da geometria correta;
- corrosão de terminais e chicote.

## Diagnóstico profissional

Perguntas certas:

1. A carga aplicada está dentro do envelope real do equipamento?
2. A tensão nos terminais se mantém aceitável sob esforço?
3. O problema é elétrico, mecânico ou operacional?
4. O sistema de comando está íntegro?

Ensaios úteis:

- medir tensão no motor durante manobra;
- observar aquecimento de cabo, contator e terminais;
- inspecionar ruído mecânico, travas e redutor;
- verificar histórico de operação em sobrecarga.

## Boas práticas

- separar conceitualmente catraca e guincho de âncora;
- projetar para carga dinâmica e não apenas estática;
- manter circuito curto e robusto;
- proteger o controle e a potência contra corrosão;
- inspecionar linha, tambor, fixação e contatores.

## Erros comuns

- usar a catraca para função que deveria ser de guincho;
- dimensionar pelo “peso do objeto” e ignorar esforço real;
- improvisar controle sem segurança de operação;
- negligenciar queda de tensão em circuito de convés;
- insistir em uso com trava ou cabo mal alinhado.

## Integração com outras notas

- [[Guincho]]
- [[Bancos de Bateria]]
- [[Dimensionamento de Cabos DC — Cálculo Prático]]
- [[Fusíveis DC — Proteção Contra Sobrecorrente]]
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]]

## Perguntas que esta nota responde

- O que diferencia catraca de guincho de âncora?
- Onde a catraca falha: elétrica, mecânica ou operacionalmente?
- Como alimentar e proteger corretamente esse atuador de convés?
