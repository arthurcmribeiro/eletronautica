---
title: "Eletrólise"
note_type: "technical-note"
domain: "80_Seguranca_e_Corrosao"
source_file: "ELETRÓLISE bb819734f7fb8373bf6e01246ab6177a.md"
status: "technical-review-l1"
review_level: "engineering-curated"
aliases:
  - "ELETRÓLISE"
  - "Corrosão eletrolítica"
  - "Corrosão eletroquímica"
seo_title: "Eletrólise em embarcações: termo correto, mecanismos e diagnóstico"
seo_description: "Nota técnica para separar eletrólise, corrosão galvânica e correntes parasitas no contexto náutico, com foco em terminologia correta, mecanismos e decisão de diagnóstico."
seo_keywords:
  - "eletrólise embarcação"
  - "corrosão eletrolítica náutica"
  - "galvânica versus corrente parasita"
  - "diagnóstico corrosão barco"
geo_queries:
  - "O que é chamado de eletrólise em embarcações e o que o termo realmente significa?"
  - "Como diferenciar corrosão galvânica de corrosão por corrente parasita?"
related_notes:
  - "Anôdo"
  - "Bonding — Sistema de Interligação de Massas"
  - "Correntes Parasitas — Stray Currents"
  - "Isolador Galvânico - Transformador de Isolamento"
  - "CAIS (Pier) (AC)"
  - "Aterramento"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
---

# Eletrólise

> [!abstract] Resumo técnico
> Em linguagem de oficina, "eletrólise" costuma virar sinônimo de qualquer corrosão elétrica em embarcação. Tecnicamente isso é fraco. Esta nota existe para organizar o vocabulário e evitar diagnóstico errado: uma coisa é corrosão galvânica, outra é corrosão por corrente parasita, e outra ainda é risco de fuga AC em ambiente aquático.

## Por que esta nota é necessária

Quando o termo é usado de forma solta, o resultado costuma ser ruim:

- troca-se anodo sem resolver a causa;
- culpa-se o metal errado;
- aplica-se solução de galvanic isolator onde o problema é interno;
- ignora-se um defeito de segurança porque "é só eletrólise".

Esta nota funciona como nota de síntese conceitual. O diagnóstico operacional detalhado está em [[Correntes Parasitas — Stray Currents]].

## O que o mercado costuma chamar de eletrólise

Na prática brasileira, o termo costuma englobar:

- corrosão galvânica;
- corrosão por corrente parasita;
- dano associado a shore power;
- às vezes até choque elétrico em água.

Isso é útil para conversa informal, mas ruim para engenharia.

## Distinção técnica mínima

### Corrosão galvânica

É o ataque eletroquímico natural entre metais com potenciais diferentes, eletricamente conectados em um eletrólito. Não precisa de fonte elétrica externa.

Mitigações típicas:

- [[Anôdo]];
- seleção de materiais;
- isolamento entre metais;
- arquitetura correta de [[Bonding — Sistema de Interligação de Massas]].

### Corrosão por corrente parasita

É o ataque por corrente elétrica indevida saindo de um metal para a água ou estrutura. É muito mais agressiva e quase sempre aponta problema elétrico real.

Mitigações típicas:

- localizar e eliminar a fuga;
- revisar aterramento, bonding e negativo DC;
- revisar shore power;
- usar [[Isolador Galvânico - Transformador de Isolamento]] quando aplicável;
- corrigir a instalação, não apenas trocar anodo.

### Vazamento AC para água

É um tema de segurança humana crítica. Pode coexistir com corrosão e com defeitos de instalação, mas não deve ser resumido apenas como "eletrólise". O risco principal imediato é choque elétrico em ambiente aquático.

## Como o termo deve ser usado nesta base

Para manter rigor técnico, esta vault adota a seguinte lógica:

- [[Eletrólise]] = nota conceitual e organizadora;
- [[Correntes Parasitas — Stray Currents]] = mecanismo destrutivo por fuga/corrente indevida;
- [[Anôdo]] = proteção catódica e leitura de consumo;
- [[Bonding — Sistema de Interligação de Massas]] = arquitetura de equipotencialização;
- [[Isolador Galvânico - Transformador de Isolamento]] = mitigação associada ao shore power.

## Sinais que exigem separação de hipóteses

Sempre diferenciar:

- dano lento e coerente com par galvânico;
- consumo anormal de anodos;
- pitting rápido e localizado;
- mudança de comportamento conforme marina ou conexão AC;
- coincidência entre corrosão e defeitos elétricos aparentes.

Se tudo é tratado como uma só doença, o reparo costuma ser superficial.

## Fluxo mental de diagnóstico

Perguntas úteis:

1. Existe fonte externa de energia conectada?
2. O dano acelera em determinadas marinas ou períodos?
3. O padrão de ataque é lento e distribuído ou rápido e localizado?
4. O anodo está consumindo compativelmente, pouco demais ou rápido demais?
5. Há mudança ao isolar shore power e circuitos internos?

Isso ajuda a separar fenômeno eletroquímico natural de defeito elétrico ativo.

## Boas práticas editoriais e técnicas

Ao escrever ou ensinar o tema, evitar frases como:

- "foi eletrólise" sem explicar o mecanismo;
- "o zinco resolve";
- "a marina corrói o barco" sem medir;
- "é normal o anodo acabar rápido".

A formulação melhor é sempre:

- qual foi o mecanismo provável;
- qual evidência aponta para ele;
- qual teste faltou;
- qual solução realmente atua naquela causa.

## Integração com outras notas

- [[Anôdo]]
- [[Bonding — Sistema de Interligação de Massas]]
- [[Correntes Parasitas — Stray Currents]]
- [[Isolador Galvânico - Transformador de Isolamento]]
- [[CAIS (Pier) (AC)]]
- [[Aterramento]]

## Perguntas que esta nota responde

- O que a maioria das pessoas chama de eletrólise em embarcações?
- Como esta base diferencia corrosão galvânica, corrente parasita e risco AC?
- Por que usar o termo certo melhora o diagnóstico e evita reparo errado?
