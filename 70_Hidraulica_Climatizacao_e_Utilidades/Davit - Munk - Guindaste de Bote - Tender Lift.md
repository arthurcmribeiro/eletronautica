---
title: "Davit - Munk - Guindaste de Bote - Tender Lift"
note_type: "technical-note"
domain: "70_Hidraulica_Climatizacao_e_Utilidades"
source_file: "DAVIT MUNK GUINDASTE DE BOTE TENDER LIFT 33a19734f7fb8192a27ff7744a3de000.md"
status: "technical-review-l1"
review_level: "engineering-curated"
aliases:
  - "DAVIT MUNK GUINDASTE DE BOTE TENDER LIFT"
  - "Davit"
  - "Tender lift"
seo_title: "Davit e tender lift em embarcações: carga, comando, intertravamentos e falhas"
seo_description: "Guia técnico sobre davit, guindaste de bote e tender lift: carga útil, fator dinâmico, atuadores elétricos ou hidráulicos, fim de curso, comando e segurança operacional."
seo_keywords:
  - "davit barco"
  - "tender lift embarcação"
  - "guindaste de bote"
  - "carga útil davit marine"
geo_queries:
  - "Como dimensionar ou diagnosticar davit e tender lift da embarcação?"
  - "Quais são os riscos de operação do guindaste de bote no barco?"
related_notes:
  - "Plataforma de Popa Elétrica - Hidráulica"
  - "Bancos de Bateria"
  - "Relés e Relés de Estado Sólido"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Casa de Máquinas e Paiol"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
---

# Davit - Munk - Guindaste de Bote - Tender Lift

> [!abstract] Resumo técnico
> Sistemas de içamento de tender e bote combinam estrutura, atuador, controle e segurança operacional. O erro mais grave é tratar o conjunto como simples “acessório de conforto”, ignorando carga dinâmica, fator de segurança, fim de curso, visibilidade de operação e integridade estrutural da instalação.

## O que é

Esta nota cobre sistemas de içamento e movimentação de bote ou tender, como:

- `davit`;
- guindaste de bote;
- `munk` em contexto brasileiro;
- `tender lift`.

As soluções podem ser:

- elétricas;
- eletro-hidráulicas;
- hidráulicas.

## O que realmente importa

Mais do que a potência do motor, o sistema depende de:

- carga útil real;
- fator dinâmico da operação;
- geometria do braço e do ponto de içamento;
- sincronismo entre lados, quando existir;
- visibilidade do operador;
- intertravamentos e limites de curso;
- estrutura onde o conjunto está fixado.

## Carga estática versus carga dinâmica

Essa diferença é crítica.

O peso do tender parado não é a única referência. A estrutura pode ver esforço maior por:

- embarcação em movimento;
- tender molhado;
- ocupação residual;
- balanço na hora do içamento;
- impacto em fim de curso;
- desalinhamento.

Especificar apenas pelo “peso seco do bote” é tecnicamente insuficiente.

## Arquitetura de acionamento

Os arranjos mais comuns envolvem:

- motor elétrico com redutor;
- cilindro hidráulico ou bomba eletro-hidráulica;
- relés/contatores de potência;
- chaves de fim de curso;
- comandos locais ou remotos;
- travas mecânicas ou retenção hidráulica.

## Segurança operacional

Como esse sistema movimenta massa suspensa, ele precisa de:

- comando claro;
- visibilidade ou observação adequada;
- parada segura;
- controle de curso;
- respeito à carga admissível;
- rotina de inspeção mecânica.

O melhor sistema elétrico do mundo não compensa operação sem disciplina.

## Integração elétrica

Em versões elétricas e eletro-hidráulicas, avaliar:

- corrente de partida;
- corrente sob carga;
- queda de tensão;
- proteção coordenada;
- qualidade de terminais e contatores;
- compatibilidade do banco com a manobra.

Ver também:

- [[Bancos de Bateria]]
- [[Fusíveis DC — Proteção Contra Sobrecorrente]]
- [[Relés e Relés de Estado Sólido]]

## Falhas mais comuns

As falhas recorrentes são:

- movimento lento por baixa tensão;
- assimetria entre lados;
- contator fatigado;
- fim de curso defeituoso;
- retenção hidráulica ruim;
- desgaste estrutural ou de cabo/cinta;
- operação acima da carga real admissível.

## Diagnóstico profissional

Perguntas essenciais:

1. A estrutura está íntegra e a carga é compatível?
2. O sistema recebe tensão/pressão adequadas sob carga?
3. Há sincronismo correto, quando aplicável?
4. Os intertravamentos e fins de curso funcionam?
5. O problema é estrutural, elétrico, hidráulico ou operacional?

## Boas práticas

- tratar o conjunto como sistema de içamento, não como acessório;
- validar carga real e fator dinâmico;
- prever inspeção fácil de cabos, fixações e articulações;
- manter fins de curso e travas em estado confiável;
- integrar o sistema ao procedimento operacional da tripulação.

## Erros comuns

- dimensionar pelo peso idealizado do tender;
- ignorar assimetria e alinhamento;
- instalar fim de curso sem robustez;
- subestimar queda de tensão;
- usar o sistema sem linha de visada ou sem observador.

## Integração com outras notas

- [[Plataforma de Popa Elétrica - Hidráulica]]
- [[Bancos de Bateria]]
- [[Relés e Relés de Estado Sólido]]
- [[Fusíveis DC — Proteção Contra Sobrecorrente]]
- [[Casa de Máquinas e Paiol]]
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]]

## Perguntas que esta nota responde

- Como analisar de forma séria um sistema de tender lift ou davit?
- Quais são os riscos mais comuns em içamento de bote?
- Onde separar falha elétrica/hidráulica de erro estrutural e operacional?
