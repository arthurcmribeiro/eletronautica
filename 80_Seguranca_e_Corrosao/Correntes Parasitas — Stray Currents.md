---
title: "Correntes Parasitas — Stray Currents"
note_type: "technical-note"
domain: "80_Seguranca_e_Corrosao"
source_file: "CORRENTES PARASITAS — STRAY CURRENTS 33a19734f7fb8174be22f7de6a4170ba.md"
status: "technical-review-l1"
review_level: "engineering-curated"
aliases:
  - "CORRENTES PARASITAS — STRAY CURRENTS"
  - "Correntes Parasitárias — Stray Currents"
  - "Stray current corrosion"
  - "Corrente de fuga corrosiva"
seo_title: "Correntes parasitas em embarcações: corrosão acelerada, diagnóstico e mitigação"
seo_description: "Entenda a diferença entre correntes parasitas, corrosão galvânica e vazamentos AC perigosos. Guia técnico para diagnóstico, inspeção e mitigação em embarcações."
seo_keywords:
  - "correntes parasitas embarcação"
  - "stray current corrosion"
  - "corrosão acelerada barco"
  - "diagnóstico de corrosão elétrica náutica"
geo_queries:
  - "Como identificar correntes parasitas em uma embarcação?"
  - "Qual a diferença entre corrosão galvânica e correntes parasitas?"
related_notes:
  - "Anôdo"
  - "Aterramento"
  - "Bonding — Sistema de Interligação de Massas"
  - "CAIS (Pier) (AC)"
  - "Eletrólise"
  - "Isolador Galvânico - Transformador de Isolamento"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
---

# Correntes Parasitas — Stray Currents

> [!abstract] Resumo técnico
> Corrente parasita é corrente elétrica que percorre caminhos não previstos e produz perda de metal em pontos de saída de corrente para a água ou para estruturas condutivas. Em linguagem de oficina, muita gente chama tudo de "eletrólise"; tecnicamente, isso é impreciso. Corrente parasita é uma forma específica e muito mais agressiva de corrosão eletroquímica.

## O que são correntes parasitas

Em termos práticos, há corrente parasita quando parte da corrente elétrica de um sistema DC ou de uma falha AC encontra um caminho indevido por:

- água;
- eixo;
- ferragens submersas;
- casco metálico;
- sistema de bonding;
- terra de shore power.

Quando a corrente sai do metal para o eletrólito, esse ponto sofre perda acelerada de material.

## O que esta nota não deve confundir

É fundamental separar três fenômenos:

### 1. Corrosão galvânica

Ocorre sem alimentação elétrica externa, por diferença natural de potencial entre metais em um eletrólito.

### 2. Corrente parasita DC

É o caso mais destrutivo para perda de metal. Normalmente decorre de fuga, aterramento incorreto, cabo danificado, equipamento defeituoso ou arquitetura ruim.

### 3. Vazamento AC para a água

É gravíssimo do ponto de vista de segurança de pessoas e pode coexistir com problemas de corrosão, mas seu principal risco imediato é choque elétrico em ambiente aquático. Não deve ser tratado como se fosse idêntico ao mecanismo clássico de corrosão por corrente parasita DC.

## Fontes típicas

As origens mais comuns são:

- cabo DC com isolamento danificado;
- retorno indevido por estrutura metálica;
- ligação incorreta entre negativo DC, PE e bonding;
- equipamento com falha interna;
- shore power com problema de aterramento, polaridade ou isolamento;
- barco vizinho injetando corrente na água da marina.

Em marinas, uma embarcação pode sofrer o problema gerado por outra.

## Onde o dano costuma aparecer

Os pontos mais vulneráveis são:

- hélices;
- eixos;
- trim tabs;
- rabetas e pés de motor;
- cascos de alumínio;
- passa-cascos metálicos;
- trocadores de calor e ferragens submersas conectadas ao bonding.

Consumo anormalmente rápido de [[Anôdo]] é sinal de alerta, mas não basta para fechar diagnóstico sozinho.

## Sinais de campo que merecem investigação

Desconfie fortemente quando houver:

- pitting severo em pouco tempo;
- corrosão localizada e agressiva em componente específico;
- anodos acabando cedo demais em marina ou período específico;
- dano muito maior após conexão prolongada ao [[CAIS (Pier) (AC)]];
- comportamento diferente ao mudar de marina;
- aquecimento, odores ou anomalias elétricas junto com corrosão.

## Diagnóstico correto

### 1. Não usar medições improvisadas como verdade final

Enfiar um fio qualquer na água e ler milivolts com multímetro pode até dar indício, mas não produz diagnóstico confiável. Para análise séria de potencial de proteção e de corrosão, o correto é usar eletrodo de referência apropriado, tipicamente prata/cloreto de prata.

### 2. Separar problema interno de problema externo

O raciocínio base é:

1. medir o comportamento atual;
2. desconectar shore power;
3. observar o que muda;
4. isolar cargas e fontes internas uma a uma;
5. localizar o circuito ou a condição que altera o potencial ou a corrente.

Se o sintoma muda fortemente ao retirar o shore, a origem pode estar:

- na própria embarcação via entrada AC;
- na marina;
- em outra embarcação conectada à mesma infraestrutura.

### 3. Medir corrente e não só tensão

Dependendo da arquitetura, vale medir:

- corrente em condutores de PE;
- corrente em bonding;
- correntes residuais em derivações específicas;
- diferença de potencial entre metais submersos e eletrodo de referência.

Valores absolutos variam com material, liga, anodo, salinidade e arquitetura. Tendência, desvio abrupto e comparação com baseline do próprio barco são mais úteis do que números soltos sem contexto.

### 4. Ensaios de isolamento

Ensaios com megôhmetro podem ser úteis, mas só depois de:

- desconectar eletrônicos sensíveis;
- respeitar limites do fabricante;
- definir claramente o que está sendo testado.

Megger mal aplicado pode danificar equipamento e ainda assim não explicar toda a corrosão observada.

## Relação com shore power

Corrente parasita e shore power se cruzam em três pontos:

- terra/PE;
- neutro referenciado em topologia inadequada;
- acoplamento com sistema de bonding e metais submersos.

[[Isolador Galvânico - Transformador de Isolamento]] pode ajudar, mas não são soluções equivalentes:

- isolador galvânico atua em cenário específico e não corrige toda falha de instalação;
- transformador de isolamento é a solução mais robusta para desacoplar a embarcação da rede da marina.

## Papel do bonding

[[Bonding — Sistema de Interligação de Massas]] não é vilão nem solução mágica. Ele:

- ajuda a equalizar potenciais;
- facilita proteção catódica;
- também pode distribuir um problema quando a arquitetura está errada.

Bonding mal entendido leva a dois erros opostos:

- não interligar o que precisava estar no mesmo potencial;
- interligar indiscriminadamente e criar caminho para corrente indevida.

## Boas práticas de prevenção

- manter cabos, conectores e passagens mecânicas em ótimo estado;
- revisar periodicamente a relação entre negativo DC, PE e bonding;
- usar [[Anôdo]] correto para o ambiente e monitorar sua taxa de consumo;
- registrar medições de referência do próprio barco em condição saudável;
- investigar mudanças de marina, berço ou comportamento do shore power;
- considerar transformador de isolamento em instalações mais críticas ou sensíveis.

## Erros comuns

Os mais perigosos são:

- chamar toda corrosão de "eletrólise" e parar por aí;
- trocar anodo sem investigar a causa;
- usar leitura improvisada de multímetro como diagnóstico definitivo;
- confundir corrente parasita DC com risco de choque por AC na água;
- condenar o metal da peça quando o problema é a arquitetura elétrica.

## Integração com outras notas

- [[Anôdo]]
- [[Aterramento]]
- [[Bonding — Sistema de Interligação de Massas]]
- [[CAIS (Pier) (AC)]]
- [[Eletrólise]]
- [[Isolador Galvânico - Transformador de Isolamento]]
- [[Quadro Elétrico e Painel de Distribuição AC-DC]]

## Perguntas que esta nota responde

- O que diferencia corrente parasita de corrosão galvânica?
- Como separar defeito interno, problema de shore power e problema da marina?
- Por que medir "qualquer milivolt na água" não basta para um diagnóstico profissional?
