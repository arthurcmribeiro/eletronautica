---
title: "Hotline (DC)"
note_type: "technical-note"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "HOTLINE (DC) 77f19734f7fb83e99276817165e87b28.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
review_level: "engineering-curated"
aliases:
  - "HOTLINE (DC)"
  - "Circuito sempre energizado"
  - "Unswitched DC"
seo_title: "Hotline DC em embarcações: circuitos sempre energizados, proteção e projeto"
seo_description: "Guia técnico sobre circuitos DC sempre energizados em embarcações: quando usar, como proteger, como documentar e quais erros tornam a hotline perigosa."
seo_keywords:
  - "hotline DC embarcação"
  - "circuito sempre energizado náutico"
  - "bomba de porão sempre ativa"
  - "proteção circuito essencial DC"
geo_queries:
  - "Quais circuitos devem ficar sempre energizados em uma embarcação?"
  - "Como projetar corretamente a hotline DC de um barco?"
related_notes:
  - "Alarme de Alagamento - Sensor de Porão"
  - "Bomba de Porão"
  - "Chaves Gerais (DC)"
  - "Detector de CO — Monóxido de Carbono"
  - "Detector de Gás GLP - GN"
  - "Monitor de Bateria - BMV - Shunt"
  - "Sistema de Alarme Geral - Painel de Alarmes"
  - "VRM / Monitoramento Remoto"
---

# Hotline (DC)

> [!abstract] Resumo técnico
> Hotline DC é o conjunto de circuitos que permanecem alimentados mesmo com a chave geral de serviços desligada. Em projeto profissional, não é um "fio direto na bateria", mas uma camada controlada de cargas essenciais, protegidas, documentadas e intencionalmente mantidas ativas.

## O que é

Chama-se hotline, neste contexto, a alimentação DC não comutada pela chave geral de serviços. São circuitos pensados para continuar operando quando o restante do barco é desenergizado pelo usuário.

Isso existe para manter funções críticas mesmo com a embarcação parada, fechada ou desacompanhada.

## O que deve entrar na hotline

A decisão deve ser feita por criticidade funcional, não por conveniência. Tipicamente entram:

- alimentação automática da [[Bomba de Porão]];
- [[Alarme de Alagamento - Sensor de Porão]];
- detectores de segurança que exijam alimentação contínua, como [[Detector de CO — Monóxido de Carbono]] e [[Detector de Gás GLP - GN]], quando essa for a estratégia do equipamento e do projeto;
- [[Monitor de Bateria - BMV - Shunt]] e sistemas de telemetria;
- [[VRM / Monitoramento Remoto]] ou rastreamento;
- memória, relógio ou controle de equipamentos que explicitamente precisem de alimentação permanente.

## O que normalmente não deve entrar

Em regra, não devem ficar permanentes:

- cargas de conforto;
- iluminação comum;
- eletrônica de uso casual;
- cargas de alto consumo sem justificativa clara;
- qualquer circuito deixado permanente apenas para "evitar passar pela chave".

Hotline mal definida vira consumo parasita, risco de manutenção e descontrole da arquitetura DC.

## Arquitetura correta

O arranjo maduro é:

- barramento ou distribuição dedicada para cargas permanentes;
- proteção individual por circuito;
- identificação visível;
- documentação no diagrama;
- possibilidade de isolamento total para manutenção e emergência.

Em instalações simples, parte dessa função pode sair diretamente da bateria ou do barramento principal. Em instalações melhores, existe um pequeno subquadro ou barramento específico para essenciais.

## Proteção e seccionamento

O erro clássico é tratar hotline como exceção à proteção. Não é.

Circuitos permanentes continuam precisando de:

- proteção contra sobrecorrente no condutor não aterrado/positivo, conforme a arquitetura adotada;
- derivação protegida o mais próximo possível da fonte de energia, conforme norma e projeto;
- bitola coerente com corrente, regime e queda de tensão admissível;
- meio de corte total para manutenção e emergência.

Uma chave geral "de uso normal" pode não cortar a hotline, mas o sistema precisa ter um modo de desenergização total do banco quando a intervenção exigir segurança completa.

## Exemplos corretos de aplicação

### Bomba de porão automática

É o caso didático mais importante. O automático deve continuar ativo com a chave geral desligada. Em muitos projetos, o comando manual da bomba passa pelo painel, enquanto o automático fica na hotline.

### Monitoramento e telemetria

Sistemas como [[VRM / Monitoramento Remoto]] só fazem sentido se permanecerem energizados. Isso exige orçamento energético de standby e proteção específica.

### Alarmes e detecção

Alarmes de água, gás ou CO não devem depender de o operador "lembrar de deixar a chave ligada", desde que o projeto, o equipamento e a rotina operacional justifiquem a permanência.

## Critérios de projeto

### 1. Corrente de repouso

Toda carga permanente deve entrar no balanço energético do barco. Pequenos consumos contínuos, somados por dias ou semanas, descarregam o banco.

### 2. Criticidade real

Se o circuito não gera ganho concreto de segurança, proteção do ativo ou monitoramento relevante, provavelmente não deveria estar na hotline.

### 3. Manutenção segura

O técnico precisa saber, de forma inequívoca, quais pontos permanecem vivos com a chave desligada. Sem isso, a hotline vira armadilha.

### 4. Queda de tensão

Cargas como bomba automática, eletrônica de segurança e telemetria costumam ser sensíveis a subtensão. A linha permanente precisa ser curta, bem protegida e dimensionada para o pior caso plausível.

## Falhas mais comuns em campo

As mais recorrentes são:

- bomba automática ligada depois da chave geral, anulando sua função;
- vários circuitos permanentes pendurados no mesmo fusível sem seletividade;
- hotline não documentada, confundindo manutenção;
- consumos fantasma drenando o banco em períodos de inatividade;
- sensores e monitores ligados em derivação improvisada, sem proteção adequada;
- ausência de meio de desligamento total para serviço.

## Diagnóstico profissional

O diagnóstico deve responder:

1. Quais circuitos ficam energizados com a chave desligada?
2. Isso foi intencional ou improvisado?
3. Cada derivação está protegida?
4. O consumo total de repouso está dentro do previsto?

Ensaios úteis:

- medição de corrente de repouso total do banco;
- conferência de tensão nas saídas permanentes com chave desligada;
- verificação funcional da bomba automática e alarmes;
- inspeção do diagrama versus instalação real;
- teste de desligamento total para manutenção.

## Boas práticas

- manter barramento dedicado para cargas permanentes quando a instalação justificar;
- proteger cada circuito individualmente;
- rotular fisicamente os condutores e pontos sempre energizados;
- medir e registrar consumo de repouso após qualquer alteração;
- revisar periodicamente o que está na hotline e remover cargas "de conveniência";
- prever corte total do banco para emergência e serviço.

## Erros que fragilizam a base técnica

Estas frases precisam ser evitadas:

- "hotline é só um fio direto na bateria";
- "se é importante, deixa direto";
- "chave desligada significa barco desenergizado";
- "se o fusível está no painel, já protege".

Todas elas simplificam demais e induzem instalação ruim.

## Integração com outras notas

- [[Alarme de Alagamento - Sensor de Porão]]
- [[Bomba de Porão]]
- [[Chaves Gerais (DC)]]
- [[Detector de CO — Monóxido de Carbono]]
- [[Detector de Gás GLP - GN]]
- [[Monitor de Bateria - BMV - Shunt]]
- [[Sistema de Alarme Geral - Painel de Alarmes]]
- [[VRM / Monitoramento Remoto]]

## Perguntas que esta nota responde

- Quais circuitos fazem sentido na hotline de uma embarcação?
- Como manter cargas essenciais ativas sem transformar o barco em um emaranhado de fios diretos?
- Como proteger, documentar e manter circuitos permanentes com segurança?
