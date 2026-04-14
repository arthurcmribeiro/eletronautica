---
title: "Ar-Condicionado Marine — Sistema Completo"
note_type: "system"
domain: "70_Hidraulica_Climatizacao_e_Utilidades"
source_file: "AR-CONDICIONADO MARINE — SISTEMA COMPLETO 33a19734f7fb81b6b5b9e1055d981535.md"
status: "technical-review-l1"
review_level: "engineering-curated"
aliases:
  - "AR-CONDICIONADO MARINE — SISTEMA COMPLETO"
  - "HVAC marinho"
seo_title: "Ar-condicionado marine: arquitetura do sistema, água do mar, elétrica e diagnóstico"
seo_description: "Guia técnico do ar-condicionado marinho: circuito frigorífico, circuito de água do mar, ar, elétrica, automação, dimensionamento e falhas típicas."
seo_keywords:
  - "ar condicionado marine"
  - "HVAC náutico"
  - "bomba água do mar ar condicionado"
  - "diagnóstico ar condicionado embarcação"
geo_queries:
  - "Como funciona o ar-condicionado marine em embarcações?"
  - "Quais são as falhas mais comuns em ar-condicionado marinho?"
related_notes:
  - "Bomba Ar Condicionado"
  - "CAIS (Pier) (AC)"
  - "Contatores (AC)"
  - "Gerador (AC)"
  - "Linha Pesada (AC)"
  - "Proteção Dr"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
---

# Ar-Condicionado Marine — Sistema Completo

> [!abstract] Resumo técnico
> Ar-condicionado marine é um sistema HVAC adaptado ao ambiente náutico, normalmente com condensação a água do mar e exigências fortes de integração hidráulica, elétrica e de automação. O sistema não se resume ao compressor: desempenho e confiabilidade dependem tanto da bomba de água do mar, da circulação de ar e da alimentação AC quanto do circuito frigorífico em si.

## O que é

É o sistema responsável por climatizar e desumidificar ambientes da embarcação. Em barcos de recreio, aparecem principalmente duas arquiteturas:

- unidades self-contained ou direct expansion;
- sistemas centrais com água gelada e fan-coils.

Ambas podem usar água do mar como rejeição de calor, o que diferencia fortemente o sistema náutico do residencial comum.

## Os quatro subsistemas que precisam funcionar juntos

### 1. Circuito frigorífico

Inclui compressor, condensador, evaporador, dispositivo de expansão e controles de proteção.

### 2. Circuito de água do mar

Inclui tomada de mar, registro, filtro, [[Bomba Ar Condicionado]] e tubulação de condensação/rejeição.

### 3. Circuito de ar

Inclui retorno, filtro, ventilador, dutos e distribuição no ambiente.

### 4. Circuito elétrico e de comando

Inclui alimentação AC, proteção, [[Contatores (AC)]], termostatos, controladores, permissivos e alarmes.

Quando o diagnóstico não enxerga os quatro subsistemas, a chance de troca errada de peça sobe muito.

## Tipos de arquitetura

### Self-contained

É a solução mais comum em lanchas e barcos médios. A unidade concentra refrigeração e ventilação localmente. Tem instalação mais simples, mas multiplica equipamentos quando há muitos ambientes.

### Chilled water

Mais comum em embarcações maiores. Centraliza a refrigeração e distribui água gelada para unidades terminais. É mais sofisticado, exige projeto melhor e facilita setorização, manutenção e acústica quando bem executado.

## O que mais derruba desempenho no mundo real

Os fatores de campo mais críticos são:

- vazão insuficiente de água do mar;
- filtro/coador sujo;
- incrustação em condensador;
- fluxo de ar deficiente;
- alimentação elétrica ruim;
- subdimensionamento;
- ambiente com grande carga térmica e desumidificação insuficiente.

Em muitas embarcações, o defeito parece "falta de gás", mas a causa raiz está em água do mar, ar ou alimentação.

## Dimensionamento correto

Dimensionamento sério não deve ser feito só por área do ambiente. Entram:

- insolação;
- área envidraçada;
- isolamento térmico;
- volume do ambiente;
- ocupação;
- renovação de ar;
- temperatura da água do mar;
- perfil operacional da embarcação.

BTU por metro quadrado funciona como aproximação grosseira, não como critério final.

## Integração elétrica

Ar-condicionado costuma entrar em [[Linha Pesada (AC)]]. O projeto precisa considerar:

- capacidade real do [[CAIS (Pier) (AC)]];
- capacidade do [[Gerador (AC)]];
- corrente de partida do compressor;
- seletividade do circuito;
- uso ou não de soft start;
- coordenação com [[Contatores (AC)]] e proteções.

É frequente o sistema de climatização revelar que o problema verdadeiro é a arquitetura elétrica do barco.

## Integração hidráulica

No trecho de água do mar, importam muito:

- posição da tomada de mar;
- acesso ao filtro/coador;
- escorva e posicionamento da bomba;
- diâmetro das mangueiras;
- altura manométrica;
- descarte visível ou verificável da água.

Sem vazão adequada, o sistema perde capacidade, pode entrar em proteção e pode sofrer danos.

## Falhas típicas

As mais recorrentes são:

- liga e desliga por alta pressão;
- funciona, mas resfria pouco;
- compressor não parte;
- água do mar não circula adequadamente;
- retorno de ar obstruído;
- ruído, vibração ou vazamento de condensado;
- corrosão ou incrustação em componentes da água do mar.

## Diagnóstico profissional

O diagnóstico precisa separar:

1. falha de alimentação ou comando;
2. falha de circulação de água do mar;
3. falha de circulação de ar;
4. falha real do circuito frigorífico.

Perguntas úteis:

- há vazão de água suficiente?
- há troca de calor adequada?
- o evaporador está com fluxo de ar correto?
- a alimentação AC está dentro do esperado?
- o sistema foi dimensionado para essa carga térmica?

## Boas práticas

- tratar água do mar, elétrica e refrigeração como partes do mesmo sistema;
- garantir acesso fácil a filtro, bomba e pontos de manutenção;
- documentar circuito elétrico e hidráulico;
- controlar vibração e drenagem de condensado;
- revisar vazão e limpeza do circuito antes de condenar compressor ou carga de refrigerante.

## Erros comuns

Os mais frequentes são:

- adaptar split residencial sem discutir consequências de ambiente marinho, corrosão e integração;
- culpar refrigerante antes de verificar água do mar e fluxo de ar;
- esquecer corrente de partida e seletividade do circuito;
- esconder componentes críticos em locais sem acesso;
- subdimensionar o sistema porque o critério foi apenas "metragem".

## Integração com outras notas

- [[Bomba Ar Condicionado]]
- [[CAIS (Pier) (AC)]]
- [[Contatores (AC)]]
- [[Gerador (AC)]]
- [[Linha Pesada (AC)]]
- [[Proteção Dr]]
- [[Quadro Elétrico e Painel de Distribuição AC-DC]]
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]]

## Perguntas que esta nota responde

- Quais subsistemas definem o funcionamento do ar-condicionado marine?
- Por que tanta falha de AC começa fora do circuito frigorífico?
- Como o sistema de climatização se encaixa na arquitetura elétrica e hidráulica do barco?
