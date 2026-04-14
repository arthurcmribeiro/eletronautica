---
title: "Sensor de Nível de Água"
note_type: "concept-note"
domain: "70_Hidraulica_Climatizacao_e_Utilidades"
source_file: "SENSOR DE NIVEL ÁGUA fbf19734f7fb83aeb875017afe071612.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
review_level: "engineering-curated"
aliases:
  - "SENSOR DE NIVEL ÁGUA"
  - "Sensor de nível de água"
seo_title: "Sensor de nível de água em embarcações: tanque, porão e desambiguação técnica"
seo_description: "Nota de desambiguação para separar corretamente sensor de nível de tanque de água doce, sensor de alta água e sensor de porão em embarcações."
seo_keywords:
  - "sensor nível água embarcação"
  - "sensor tanque água doce barco"
  - "sensor porão barco"
  - "alta água embarcação"
geo_queries:
  - "Qual a diferença entre sensor de tanque de água e sensor de porão em embarcação?"
  - "Quando sensor de nível de água é conforto e quando é segurança?"
related_notes:
  - "Alarme de Alagamento - Sensor de Porão"
  - "Bomba de Água Pressurizada"
  - "Bomba de Porão"
  - "Caixa de Água Cinza"
  - "Sensor de Nível Diesel"
  - "Sistema de Alarme Geral - Painel de Alarmes"
---

# Sensor de Nível de Água

> [!abstract] Resumo técnico
> Esta nota não trata de um único componente. Ela existe para separar três assuntos que o mercado costuma misturar com o mesmo nome: medição de nível de tanque de água doce, detecção de alta água/porão e sensores de nível de outros reservatórios. Sem essa separação, a taxonomia da base fica errada e o diagnóstico também.

## Por que esta nota existe

No uso prático, "sensor de nível de água" pode significar coisas muito diferentes:

- medição contínua do tanque de água doce;
- sensor de alta água;
- sensor que aciona bomba de porão;
- sensor de reservatórios técnicos específicos.

Esses itens não têm a mesma função, nem a mesma criticidade, nem a mesma lógica elétrica.

## 1. Sensor de nível de tanque de água doce

É uma nota de conforto e operação. Sua função é informar reserva disponível no sistema de água doce.

Os métodos mais comuns são:

- boia/resistivo;
- capacitivo;
- leitura por múltiplos pontos;
- sensor externo sem contato com a água, em alguns tanques.

Essa família de sensores se integra mais a:

- [[Bomba de Água Pressurizada]];
- autonomia de consumo;
- reabastecimento;
- dessalinização, quando houver.

## 2. Sensor de porão ou alta água

Aqui a criticidade muda completamente. O foco deixa de ser conforto e passa a ser segurança da embarcação.

Esse grupo inclui:

- sensor de acionamento da [[Bomba de Porão]];
- sensor de alta água independente para alarme;
- lógica de supervisão em [[Sistema de Alarme Geral - Painel de Alarmes]].

Essa família deve ser lida em conjunto com [[Alarme de Alagamento - Sensor de Porão]], não como simples "medidor de nível".

## 3. Sensor de nível em outros reservatórios

Alguns princípios são semelhantes ao tanque de água doce, mas o contexto muda. Exemplo:

- [[Sensor de Nível Diesel]];
- reservatórios de água cinza;
- outros tanques de serviço.

Usar o mesmo nome para todos sem recorte editorial enfraquece a arquitetura do conhecimento.

## O que muda de um caso para o outro

### Criticidade

- tanque de água doce: gestão operacional;
- porão/alta água: segurança;
- outros tanques: depende da função.

### Tipo de sinal

- medição contínua;
- contato seco;
- chave boia;
- sensor eletrônico por ponto;
- saída para gauge, controlador ou alarme.

### Estratégia de alimentação

- tanque de água doce pode estar em circuito comum de instrumentação;
- sensor de porão e bomba automática exigem lógica de circuito permanente e tratamento de segurança.

## Problema estrutural da base antiga

Antes da revisão, esta nota tentava juntar medição de tanque e segurança de porão como se fossem o mesmo assunto. Isso gerava duplicação com [[Alarme de Alagamento - Sensor de Porão]] e enfraquecia a taxonomia.

Nesta vault, o papel correto desta nota é de desambiguação e navegação conceitual.

## Como usar esta nota no Obsidian

Use esta nota como ponto de entrada quando a dúvida for terminológica:

- quer saber do tanque de água doce: siga para o sistema de água doce;
- quer saber de segurança de porão: siga para [[Alarme de Alagamento - Sensor de Porão]] e [[Bomba de Porão]];
- quer comparar com combustível: siga para [[Sensor de Nível Diesel]].

## Integração com outras notas

- [[Alarme de Alagamento - Sensor de Porão]]
- [[Bomba de Água Pressurizada]]
- [[Bomba de Porão]]
- [[Caixa de Água Cinza]]
- [[Sensor de Nível Diesel]]
- [[Sistema de Alarme Geral - Painel de Alarmes]]

## Perguntas que esta nota responde

- Quando "sensor de nível de água" significa conforto e quando significa segurança?
- Por que tanque de água doce e porão não devem ficar escondidos na mesma lógica editorial?
- Qual nota desta vault deve ser usada para cada tipo de sensor?
