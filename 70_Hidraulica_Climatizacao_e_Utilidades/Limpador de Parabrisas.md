---
title: "Limpador de Parabrisas"
note_type: "technical-note"
domain: "70_Hidraulica_Climatizacao_e_Utilidades"
source_file: "LIMPADOR DE PARABRISAS 9f419734f7fb83199e2301a78b4b5d06.md"
status: "tier-b-curated"
fase_6_reescrita: 131
reviewed_on: "2026-04-26"
review_jurisdiction: "Brasil + Internacional"
review_level: "tier-b-curated"
normas_citadas:
  - "ABYC E-11"
  - "IEC 60945"
  - "IEC 60529 (IP)"
  - "ISO 8846 (Ignition protection)"
  - "ISO 11591 (Field of vision from helm) — referência cruzada"
  - "ABNT NBR 14728"
  - "Manual técnico AFI Marine / Doga / Speich Marine / Roca / Wynn"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
review_level: "engineering-curated"
aliases:
  - "LIMPADOR DE PARABRISAS"
  - "Wiper"
seo_title: "Limpador de parabrisas náutico: motor, park position, vedação e falhas"
seo_description: "Guia técnico sobre limpador de parabrisas náutico: motor DC, retorno à posição de descanso, pantográfico, vedação, corrosão, palheta e diagnóstico de falhas."
seo_keywords:
  - "limpador parabrisas barco"
  - "marine wiper"
  - "wiper park position boat"
  - "falha limpador náutico"
geo_queries:
  - "Por que o limpador de parabrisas do barco para no meio ou perde força?"
  - "Como diagnosticar motor e mecanismo do limpador náutico?"
related_notes:
  - "Casa de Máquinas e Paiol"
  - "Iluminação de Emergência a Bordo"
  - "Relés e Relés de Estado Sólido"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
---

# Limpador de Parabrisas

> [!abstract] Resumo técnico
> O limpador de parabrisas náutico é um sistema simples na aparência, mas crítico para visibilidade e segurança. O conjunto depende de motor vedado, mecanismo de transmissão, posição de repouso, palheta adequada, alimentação correta e resistência ao ambiente salino.

> [!tldr] TL;DR — 4 regras
> 1. **Motor marine-grade vedado** (AFI, Doga, Speich, Roca, Wynn) com IPX5+ — wiper automotivo falha em 6-12 meses.
> 2. **Park position (retorno automático ao repouso)** — sem isso, lâmina fica em vista atrapalhando visão.
> 3. **Palheta adequada (silicone marine)** — borracha automotiva degrada com UV + sal em meses.
> 4. **Alimentação ABYC E-11** com fusível dedicado + bonding; cabo dimensionado para corrente de pico (5-15A típico).

> [!info] Glossário rápido
> - **Wiper:** limpador de parabrisas.
> - **Park position:** posição de repouso (motor retorna).
> - **Pantográfico:** mecanismo de paralelogramo (limpa área retangular).
> - **Tandem:** dois braços paralelos.
> - **Palheta silicone:** resistente a UV/sal.
> - **Washer pump:** bomba de água do limpador.
> - **AFI Marine / Doga / Speich:** referências marine.

## O que é

É o sistema responsável por manter a área varrida do parabrisas visível sob chuva, spray, névoa e sujeira operacional.

O conjunto normalmente inclui:

- motor DC;
- mecanismo de transmissão;
- eixo passante e vedação;
- braço e palheta;
- chave/comando;
- função de `park` ou posição de repouso.

## Diferença para aplicação automotiva

Em ambiente náutico, o sistema precisa lidar com:

- névoa salina;
- vibração;
- umidade contínua;
- incidência UV;
- operação em acrílico, policarbonato ou vidro, conforme a embarcação.

Logo, adaptação automotiva sem critério costuma falhar cedo.

## Posição de repouso

O circuito de `park` é parte essencial da arquitetura.

Ele garante que, ao desligar o limpador:

- a palheta não pare no meio do campo de visão;
- o sistema finalize o curso e volte à posição definida.

Quando isso falha, o problema não é apenas estético; atrapalha navegação e indica defeito no circuito de comando interno.

## Braço, palheta e geometria

O desempenho final depende de:

- tipo de braço;
- pressão correta da palheta;
- compatibilidade com o material do parabrisas;
- amplitude de varredura;
- geometria da instalação.

Mesmo com motor bom, ajuste ruim de braço/palheta compromete o resultado.

## Ambiente e vedação

Pontos críticos:

- vedação do eixo passante;
- corrosão em conectores;
- penetração de água no motor ou no chicote;
- degradação da borracha da palheta.

## Falhas mais comuns

As falhas recorrentes são:

- motor sem força;
- sistema que não estaciona corretamente;
- braço solto ou fora de sincronismo;
- palheta inadequada ao material do parabrisas;
- corrosão em comando ou alimentação;
- entrada de água no conjunto.

## Diagnóstico profissional

Perguntas certas:

1. O motor recebe alimentação correta?
2. A função de `park` está íntegra?
3. O problema é elétrico, mecânico ou de palheta/ajuste?
4. Há vedação suficiente no conjunto?

Ensaios úteis:

- medir tensão no motor durante acionamento;
- observar comportamento ao desligar;
- inspecionar braço, fixação e varredura;
- verificar aquecimento, ruído e sinais de corrosão;
- inspecionar palheta e compatibilidade com o parabrisas.

## Boas práticas

- usar conjunto apropriado ao ambiente náutico;
- revisar palheta e vedação periodicamente;
- proteger conexões e chicote;
- considerar material do parabrisas ao escolher a palheta;
- não negligenciar esse sistema por parecer secundário.

## Erros comuns

- adaptar componente automotivo sem critério;
- focar só no motor e ignorar geometria da varredura;
- operar com palheta endurecida;
- deixar infiltração degradar o conjunto;
- tratar falha de `park` como defeito menor.

## Integração com outras notas

- [[Relés e Relés de Estado Sólido]]
- [[Fusíveis DC — Proteção Contra Sobrecorrente]]
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]]
- [[Casa de Máquinas e Paiol]]

## Perguntas que esta nota responde

- Como o sistema de limpador náutico funciona de verdade?
- Por que ele para no meio, perde força ou deixa de vedar?
- Onde separar falha de motor, de comando e de geometria da palheta?
