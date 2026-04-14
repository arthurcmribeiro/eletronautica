---
title: "Flap"
note_type: "technical-note"
domain: "70_Hidraulica_Climatizacao_e_Utilidades"
source_file: "FLAP 2de19734f7fb827a83150176909e81e1.md"
status: "technical-review-l1"
review_level: "engineering-curated"
aliases:
  - "FLAP"
  - "Trim tab"
  - "Interceptor"
seo_title: "Flap em embarcações: trim tabs, atuadores, controle e diagnóstico"
seo_description: "Guia técnico sobre flap/trim tab: correção de atitude, atuadores elétricos ou eletro-hidráulicos, sincronismo, corrosão, fim de curso e diagnóstico do sistema."
seo_keywords:
  - "flap barco"
  - "trim tab marine"
  - "atuador flap embarcação"
  - "diagnóstico trim tab"
geo_queries:
  - "Como diagnosticar flap lento, travado ou assimétrico na embarcação?"
  - "Qual a diferença entre flap, interceptor e trim do motor?"
related_notes:
  - "Motor de Trim - Tilt"
  - "Estabilizador"
  - "Atuador Linear"
  - "Relés e Relés de Estado Sólido"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
---

# Flap

> [!abstract] Resumo técnico
> O flap, ou `trim tab`, corrige atitude longitudinal e transversal da embarcação. Seu desempenho depende da superfície hidrodinâmica, do atuador, do comando e da simetria do sistema. Muitos problemas de flap são interpretados como defeito do casco ou do motor, quando a origem está no controle ou no atuador.

## O que é

Flap é a superfície ativa instalada normalmente na popa para influenciar a atitude da embarcação em navegação.

O sistema pode ser:

- elétrico;
- eletro-hidráulico;
- baseado em interceptores, em arquiteturas mais modernas.

## O que ele faz de fato

O flap ajuda a:

- corrigir adernamento;
- ajustar atitude longitudinal;
- melhorar transição para planeio em determinadas condições;
- otimizar conforto e, em alguns casos, eficiência operacional.

Ele não substitui:

- distribuição correta de carga;
- trim do propulsor;
- escolha adequada de hélice;
- projeto hidrodinâmico do casco.

## Flap, interceptor e trim do motor

Esses sistemas são relacionados, mas não iguais.

- `flap` atua pela superfície de popa;
- `interceptor` atua por lâmina/elemento rápido de pequena projeção;
- [[Motor de Trim - Tilt]] atua no ângulo do propulsor.

Misturar os conceitos atrapalha diagnóstico e projeto.

## Arquitetura do sistema

Os elementos principais costumam ser:

- superfície hidrodinâmica;
- atuador ou unidade hidráulica;
- comando no painel;
- alimentação e proteção;
- eventualmente indicação de posição ou controle automático.

## Atuador e controle

O atuador precisa:

- gerar curso suficiente;
- resistir ao ambiente de popa;
- manter simetria funcional entre bombordo e boreste;
- trabalhar dentro do duty cycle;
- ter proteção coerente.

Falha de um lado muda a leitura de pilotagem e pode ser confundida com problema de casco ou distribuição.

## Ambiente severo

Popa é região agressiva por:

- imersão e spray;
- vibração;
- corrosão;
- eletrólise;
- incrustação.

Logo, flap exige boa instalação e inspeção periódica.

## Falhas mais comuns

As falhas recorrentes são:

- um lado operando e o outro não;
- movimento lento;
- assimetria de curso;
- travamento mecânico;
- corrosão em chicote e conexões;
- perda de resposta por atuador degradado;
- confusão entre problema de flap e problema de trim do propulsor.

## Diagnóstico profissional

Perguntas certas:

1. O atuador recebe comando e alimentação corretos?
2. O curso é simétrico entre os lados?
3. O problema é elétrico, hidráulico ou mecânico?
4. O efeito na navegação corresponde ao movimento observado?

Ensaios úteis:

- observar curso real dos dois lados;
- medir tensão/corrente durante acionamento;
- inspecionar fixações, vedações e chicote;
- verificar se o comando está reversível e coerente;
- comparar resposta em navegação com resposta mecânica em repouso.

## Boas práticas

- inspecionar ambos os lados como sistema pareado;
- proteger chicote e conexões de popa;
- manter comando claro e sem ambiguidade;
- separar, no diagnóstico, flap de trim do motor e de estabilização ativa;
- revisar periodicamente fixações e sinais de corrosão.

## Erros comuns

- achar que qualquer adernamento é “só flap”;
- substituir atuador sem testar comando e alimentação;
- ignorar corrosão de popa;
- operar com um lado claramente fora de curso;
- tratar sistema automático e sistema manual como se fossem equivalentes.

## Integração com outras notas

- [[Motor de Trim - Tilt]]
- [[Estabilizador]]
- [[Atuador Linear]]
- [[Relés e Relés de Estado Sólido]]
- [[Fusíveis DC — Proteção Contra Sobrecorrente]]
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]]

## Perguntas que esta nota responde

- Como flap difere de trim do motor e de estabilizador?
- Onde nasce a assimetria de resposta do sistema?
- Como diagnosticar flap com rigor técnico?
