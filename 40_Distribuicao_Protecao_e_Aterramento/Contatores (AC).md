---
title: "Contatores (AC)"
note_type: "technical-note"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "CONTATORES (AC) f0f19734f7fb820895d40138dc40c1ac.md"
status: "technical-review-l1"
review_level: "engineering-curated"
aliases:
  - "CONTATORES (AC)"
  - "Contator AC"
seo_title: "Contatores (AC) em embarcações: seleção, falhas e diagnóstico"
seo_description: "Critérios profissionais para aplicação de contatores AC em embarcações: categoria de emprego, bobina, intertravamento, falhas típicas e integração com ar-condicionado, boilers e cargas pesadas."
seo_keywords:
  - "contatores AC embarcações"
  - "contator compressor ar condicionado náutico"
  - "contator carga indutiva"
  - "comando de potência embarcação"
geo_queries:
  - "Como selecionar um contator AC para ar-condicionado náutico?"
  - "Quais falhas são mais comuns em contatores AC de embarcações?"
related_notes:
  - "Ar-Condicionado Marine — Sistema Completo"
  - "Chaves Seletoras (AC)"
  - "Disjuntores (DC) e (AC)"
  - "Gerador (AC)"
  - "Inversora (DC To AC)"
  - "Linha Pesada (AC)"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
  - "Relés e Relés de Estado Sólido"
---

# Contatores (AC)

> [!abstract] Resumo técnico
> Contator AC é um dispositivo de manobra para comutar cargas de potência com alta frequência operacional e com capacidade de suportar arco, inrush e regime de serviço muito superiores aos de um relé comum. Em embarcações, aparece principalmente em ar-condicionado, resistências, bombas AC e sequências automáticas de partida/parada.

## O que é

Contator é um equipamento de comando, não de proteção. Sua função é abrir e fechar circuitos de potência mediante o acionamento de uma bobina de controle, normalmente por termostato, controlador, PLC, pressostato, relé intermediário ou sistema de automação.

A diferença prática entre um relé e um contator não é apenas "tamanho". O contator é construído para:

- suportar manobra repetitiva sob carga;
- lidar melhor com correntes de partida e com arco elétrico;
- aceitar acessórios de intertravamento, contatos auxiliares e sinalização;
- operar em categorias de emprego específicas para motores, resistências e cargas mistas.

## Onde se aplica a bordo

As aplicações mais típicas são:

- compressores e bombas de água do mar de [[Ar-Condicionado Marine — Sistema Completo]];
- resistências de [[Boiler]] e aquecedores;
- cargas de [[Linha Pesada (AC)]] comandadas remotamente;
- sequências de partida, permissivos e intertravamentos em quadros AC;
- comutação de cargas em sistemas com [[Gerador (AC)]], [[Inversora (DC To AC)]] e automação.

## Princípio de funcionamento

Quando a bobina é energizada, o núcleo magnético atrai o conjunto móvel e fecha os contatos principais. Ao retirar o comando, a mola de retorno abre os contatos. O arco que aparece na abertura é controlado por geometria de contato e câmara de extinção apropriadas ao equipamento.

Isso importa porque:

- cargas resistivas puras são relativamente fáceis de manobrar;
- motores, compressores e transformadores impõem inrush e fator de potência menores;
- selecionar apenas pela corrente nominal quase sempre leva a erro.

## Critérios corretos de seleção

### 1. Categoria de emprego

A escolha deve seguir a categoria de utilização do fabricante e da família do contator. Em termos práticos:

- cargas resistivas e aquecimento costumam cair em categorias equivalentes a serviço resistivo;
- motores e compressores exigem categoria de manobra própria para motor;
- partidas severas, reversão e inching exigem categoria mais dura.

Contator "de mesma corrente" pode ser adequado para uma resistência e inadequado para um compressor.

### 2. Corrente e regime real da carga

Avaliar:

- corrente nominal em regime;
- corrente de partida;
- número de manobras por hora;
- temperatura interna do painel;
- altitude, ventilação e grau de proteção exigido.

Compressores de ar-condicionado, bombas e motores exigem margem real de projeto. O dado crítico não é só a corrente estabilizada, mas o comportamento na partida e na abertura sob carga.

### 3. Tensão e natureza da bobina

A bobina pode ser:

- AC;
- DC;
- universal, em linhas específicas.

Em embarcações, é comum usar bobina DC quando o comando vem de eletrônica de bordo ou automação em 12 V ou 24 V. Nesses casos:

- a tensão precisa bater com o circuito de comando;
- deve-se prever supressão de surtos compatível com a eletrônica de acionamento.

Bobinas DC normalmente pedem diodo, TVS ou módulo supressor especificado pelo fabricante. Bobinas AC usam RC snubber, varistor ou supressor equivalente, nunca um diodo simples.

### 4. Contatos auxiliares e intertravamento

Em arquitetura profissional, o contator raramente trabalha sozinho. São comuns:

- contatos auxiliares para realimentação e alarme;
- intertravamento mecânico e elétrico;
- permissivo de pressostato, fluxo, temperatura e nível;
- bloqueio de partidas simultâneas para gerenciamento de carga.

## O que ele não substitui

Contator não substitui:

- disjuntor;
- fusível;
- DR;
- relé de proteção térmica ou eletrônico de motor;
- chave seccionadora de manutenção.

Quem protege é o sistema de proteção a montante e, quando aplicável, o relé de sobrecarga ou o próprio controlador do equipamento.

## Modos de falha mais comuns

Os defeitos mais recorrentes em campo são:

- bobina aberta ou degradada;
- tensão de comando insuficiente para fechamento confiável;
- contatos principais erodidos, soldados ou com resistência elevada;
- vibração mecânica por subtensão, sujeira ou armadura desgastada;
- aquecimento por aperto ruim nos terminais;
- contator subdimensionado para o regime da carga;
- uso de contator AC em aplicação DC, o que é tecnicamente inadequado.

Em ambiente marinho, oxidação, condensação e salinidade aceleram falhas de contato e de bornes.

## Diagnóstico profissional

### Verificação do circuito de comando

Confirmar:

- presença da tensão correta na bobina;
- compatibilidade entre tensão de comando e bobina instalada;
- integridade de termostatos, pressostatos, sensores de fluxo e permissivos;
- presença de supressão de surtos quando exigida.

Se há comando, mas o contator não fecha, suspeitar de bobina defeituosa, travamento mecânico ou subtensão.

### Verificação do circuito de potência

Com carga em operação, medir:

- tensão a montante e a jusante;
- queda de tensão nos contatos;
- corrente por fase ou por polo;
- aquecimento localizado em bornes e contatos.

Queda de tensão anormal em contator fechado aponta contato degradado. Corrente acima do esperado pode indicar problema na carga, não no contator.

### Diagnóstico em compressores e motores

Se o contator opera, mas o equipamento não parte corretamente, verificar antes de condená-lo:

- subtensão da fonte;
- capacitor, protetor térmico ou soft-start do compressor;
- bloqueio mecânico;
- proteção de motor atuando;
- seletividade inadequada do disjuntor a montante.

## Boas práticas de projeto e montagem

- selecionar contator pela categoria de emprego, não só pela corrente;
- prever proteção adequada a montante e, quando necessário, relé de sobrecarga;
- instalar em quadro ventilado, seco e com acesso para inspeção;
- usar terminais corretos, torque controlado e reaperto em manutenção;
- separar circuito de comando do circuito de potência;
- documentar claramente bobina, contatos principais, auxiliares e lógica de intertravamento;
- manter peça de reposição quando o equipamento comandado for crítico à operação.

## Erros de projeto e de campo

Os mais danosos são:

- usar relé comum onde deveria haver contator;
- usar contator AC em carga DC;
- ignorar corrente de partida do compressor;
- acionar bobina DC sem supressão adequada;
- proteger o circuito apenas "porque o disjuntor geral existe";
- deixar o contator como único ponto de seccionamento de manutenção.

## Normas e referências úteis

- IEC 60947-4-1 para contatores e partidas de motores;
- documentação do fabricante para categoria de emprego, durabilidade elétrica e acessórios;
- [[Disjuntores (DC) e (AC)]], [[Linha Pesada (AC)]] e [[Quadro Elétrico e Painel de Distribuição AC-DC]] para coordenação com o restante do sistema.

## Integração com outras notas

- [[Ar-Condicionado Marine — Sistema Completo]]
- [[Chaves Seletoras (AC)]]
- [[Disjuntores (DC) e (AC)]]
- [[Gerador (AC)]]
- [[Inversora (DC To AC)]]
- [[Linha Pesada (AC)]]
- [[Quadro Elétrico e Painel de Distribuição AC-DC]]
- [[Relés e Relés de Estado Sólido]]

## Perguntas que esta nota responde

- Como escolher corretamente um contator AC para uso náutico?
- Quando um relé não é suficiente e o circuito pede contator?
- Quais defeitos fazem um contator fechar, vibrar ou queimar em serviço?
