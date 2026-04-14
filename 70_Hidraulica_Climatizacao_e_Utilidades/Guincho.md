---
title: "Guincho"
note_type: "technical-note"
domain: "70_Hidraulica_Climatizacao_e_Utilidades"
source_file: "GUINCHO 50f19734f7fb8338bcfd819cb7823229.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
review_level: "engineering-curated"
aliases:
  - "GUINCHO"
  - "Windlass"
seo_title: "Guincho de âncora em embarcações: windlass, cabos, banco e falhas"
seo_description: "Guia técnico sobre windlass de âncora: gypsy, corrente, cabo, queda de tensão, banco dedicado de proa, contatores, duty cycle e diagnóstico de falhas."
seo_keywords:
  - "guincho âncora barco"
  - "windlass marine"
  - "queda de tensão guincho proa"
  - "bateria guincho âncora"
geo_queries:
  - "Por que o guincho de âncora perde força ou não recolhe a corrente?"
  - "Como dimensionar cabos e alimentação do windlass da embarcação?"
related_notes:
  - "Catraca"
  - "Bancos de Bateria"
  - "Dimensionamento de Cabos DC — Cálculo Prático"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Relés e Relés de Estado Sólido"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
---

# Guincho

> [!abstract] Resumo técnico
> O guincho de âncora, ou `windlass`, é um atuador de alta demanda instalado longe do centro elétrico da embarcação. Seu comportamento é dominado por queda de tensão, qualidade do banco, contatores, regime de uso, estado da corrente/gypsy e procedimento de ancoragem. Muito “guincho ruim” é, na prática, instalação ruim.

## O que é

O `windlass` é o equipamento usado para arriar e recolher âncora, corrente e, em alguns arranjos, cabo combinado.

Ele normalmente envolve:

- motor elétrico ou arquitetura hidráulica;
- redutor;
- `gypsy` compatível com a corrente;
- eventual tambor adicional;
- comando local e/ou remoto;
- circuito de potência dedicado.

## O que ele não deve fazer

Um erro clássico é usar o guincho para “puxar o barco” como se fosse equipamento de reboque ou içamento contínuo.

O procedimento de ancoragem e recuperação normalmente exige cooperação do barco:

- aliviar carga com propulsão quando necessário;
- evitar choques desnecessários;
- não insistir em arrancar âncora presa só no motor elétrico.

## Distância elétrica: problema estrutural

Como o guincho costuma ficar na proa, o circuito pode sofrer com:

- grande comprimento;
- alta corrente;
- queda de tensão severa;
- aquecimento de conexão;
- baixa performance exatamente sob maior carga.

É por isso que a arquitetura do circuito importa tanto.

Ver também:

- [[Bancos de Bateria]]
- [[Dimensionamento de Cabos DC — Cálculo Prático]]
- [[Fusíveis DC — Proteção Contra Sobrecorrente]]

## Banco dedicado na proa

Em muitos casos, banco dedicado ou ponto de energia robusto próximo à proa melhora drasticamente:

- desempenho;
- queda de tensão;
- confiabilidade;
- desgaste do sistema.

Nem todo barco precisa disso, mas muitos se beneficiam.

## Gypsy, corrente e compatibilidade

O guincho depende da compatibilidade entre:

- tipo e bitola da corrente;
- geometria do `gypsy`;
- estado de desgaste do conjunto;
- alinhamento e condição do paiol de corrente.

Corrente errada ou desgastada pode simular falha elétrica.

## Contatores e comando

Além do motor, são críticos:

- contatores/solenoides de potência;
- botão ou comando de convés;
- retorno de massa;
- proteção coordenada.

Falhas de comando podem produzir sintomas como:

- sobe mas não desce;
- apenas “clica”;
- opera de forma intermitente;
- derruba proteção sob carga.

## Regime de uso

O `windlass` é equipamento de serviço intermitente.

Uso prolongado acima do previsto gera:

- aquecimento do motor;
- queda de desempenho;
- aumento de corrente;
- degradação de contatores e isolamento.

## Falhas mais comuns

As falhas recorrentes são:

- queda de tensão excessiva;
- contator fatigado;
- proteção mal coordenada;
- `gypsy` incompatível ou desgastado;
- corrente mal assentada;
- uso inadequado para arrancar âncora presa;
- corrosão em conexões de proa.

## Diagnóstico profissional

Perguntas obrigatórias:

1. A tensão no motor está aceitável durante recolhimento real?
2. O banco ou fonte de energia sustenta a demanda?
3. Existe problema de comando, contator ou proteção?
4. A corrente e o `gypsy` estão compatíveis?
5. O equipamento está sendo usado dentro do regime correto?

Ensaios úteis:

- medir tensão no motor sob carga;
- inspecionar aquecimento em terminais e contatores;
- observar comportamento com âncora aliviada pelo barco;
- revisar `gypsy`, corrente e paiol.

## Boas práticas

- dimensionar o circuito pelo cenário real de carga e distância;
- considerar solução dedicada na proa quando fizer sentido;
- manter contatores e conexões em estado excelente;
- usar o barco para aliviar esforço ao recuperar âncora;
- revisar compatibilidade entre corrente e `gypsy`.

## Erros comuns

- tratar o windlass como equipamento de tração contínua;
- subdimensionar cabos por economia;
- ignorar a distância até a proa;
- culpar o motor por problema de instalação;
- operar com corrente incompatível ou paiol mal resolvido.

## Integração com outras notas

- [[Catraca]]
- [[Bancos de Bateria]]
- [[Dimensionamento de Cabos DC — Cálculo Prático]]
- [[Fusíveis DC — Proteção Contra Sobrecorrente]]
- [[Relés e Relés de Estado Sólido]]
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]]

## Perguntas que esta nota responde

- Como o windlass deve ser alimentado e protegido?
- Por que o guincho perde força na proa?
- Onde separar falha elétrica, falha mecânica e erro de operação?
