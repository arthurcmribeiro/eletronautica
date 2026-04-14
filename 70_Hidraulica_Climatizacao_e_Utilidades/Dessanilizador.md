---
title: "Dessalinizador"
note_type: "system"
domain: "70_Hidraulica_Climatizacao_e_Utilidades"
source_file: "DESSANILIZADOR 2d619734f7fb83b290ce8195a3c4da0c.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
review_level: "engineering-curated"
aliases:
  - "DESSANILIZADOR"
  - "Dessanilizador"
  - "Dessalinizador"
  - "Watermaker"
seo_title: "Dessalinizador em embarcações: osmose reversa, energia, membrana e operação"
seo_description: "Guia técnico sobre dessalinizador marinho: osmose reversa, pré-filtração, bomba de alta pressão, membrana, preservação, TDS, consumo elétrico e critérios de operação."
seo_keywords:
  - "dessalinizador barco"
  - "watermaker marine"
  - "osmose reversa embarcação"
  - "membrana watermaker barco"
geo_queries:
  - "Quando vale a pena instalar dessalinizador na embarcação?"
  - "Por que o watermaker perde produção ou estraga a membrana?"
related_notes:
  - "Bomba de Água Pressurizada"
  - "Sensor de Nível de Água"
  - "Boiler"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
  - "Carregador de Bateria (AC To DC)"
  - "Gerador (AC)"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
---

# Dessalinizador

> [!abstract] Resumo técnico
> O dessalinizador, ou `watermaker`, converte água do mar em água doce por osmose reversa. É um sistema de alta exigência operacional: depende de pré-tratamento, pressão, qualidade da água de entrada, energia disponível, preservação correta da membrana e disciplina de manutenção.

## O que é

O dessalinizador é um sistema de produção de água doce a bordo a partir de água do mar, normalmente baseado em osmose reversa.

Ele não é apenas “uma bomba com filtro”. Envolve:

- captação de água;
- pré-filtração;
- bombeamento de baixa e alta pressão, conforme o projeto;
- membrana;
- controle de descarte do concentrado;
- monitoramento da qualidade da água produzida;
- integração com o sistema de água doce.

## Quando ele faz sentido

Faz mais sentido quando:

- a embarcação busca autonomia elevada;
- o perfil de navegação inclui longos períodos longe de marina;
- o consumo de água é alto;
- a logística de abastecimento é limitada ou cara.

Em barcos de uso esporádico e dependentes de marina, pode ser luxo complexo demais para o benefício entregue.

## Princípio de funcionamento

Na osmose reversa, a água de alimentação é pressurizada contra uma membrana semipermeável.

O resultado é dividido em:

- **permeado**: a água de melhor qualidade que segue para uso ou reservação;
- **concentrado**: a salmoura rejeitada.

A eficiência e a produção dependem de:

- pressão efetiva;
- salinidade da água de entrada;
- temperatura;
- estado da membrana;
- condição dos pré-filtros.

## Elementos críticos do sistema

Os elementos principais são:

- tomada de mar dedicada ou equivalente bem definido;
- pré-filtros;
- bomba de alimentação, quando o projeto exigir;
- bomba de alta pressão ou sistema de recuperação de energia;
- membrana;
- válvulas e restritores;
- monitoramento de qualidade e descarte inicial;
- integração com tanque de água doce.

## Energia e arquitetura elétrica

O dessalinizador precisa ser compatibilizado com a arquitetura energética real do barco.

Pontos críticos:

- corrente de partida e de regime;
- duração típica de operação;
- impacto no banco de baterias;
- convivência com gerador, alternador, solar ou `shore power`;
- estratégia de comando e proteção.

Há sistemas muito eficientes energeticamente, mas não existe regra universal de consumo “por litro” que sirva para toda tecnologia.

Ver também:

- [[Carregador de Bateria (AC To DC)]]
- [[Gerador (AC)]]
- [[Quadro Elétrico e Painel de Distribuição AC-DC]]

## Membrana: coração e principal fragilidade

A membrana é o elemento mais sensível do sistema.

Ela pode perder desempenho por:

- fouling biológico;
- incrustação mineral;
- operação em água inadequada;
- ataque químico incompatível;
- preservação mal feita;
- longos períodos parada sem procedimento adequado.

Grande parte dos problemas caros nasce aqui.

## Água de entrada e limite operacional

O sistema não deve ser tratado como máquina universal de produzir água em qualquer lugar.

Água muito turva, poluída, estuarina ou com carga orgânica elevada pode:

- saturar pré-filtros rapidamente;
- agredir a membrana;
- derrubar produção;
- piorar a qualidade final;
- aumentar a necessidade de limpeza química.

## Operação e descarte inicial

A água produzida no início do ciclo nem sempre deve seguir diretamente ao tanque. Em muitos sistemas, existe fase inicial de estabilização e descarte.

O operador precisa conhecer:

- sequência de partida;
- descarte inicial;
- leitura de TDS ou critério equivalente;
- rotina de flush/preservação;
- condições em que não vale a pena operar.

## Onde costuma falhar

As falhas mais comuns são:

- queda de produção;
- TDS alto;
- pré-filtros saturando rápido;
- cavitação ou alimentação ruim na bomba;
- consumo elétrico incompatível com a expectativa;
- membrana degradada por parada inadequada.

## Diagnóstico profissional

O diagnóstico deve responder:

1. A água de entrada é adequada?
2. O pré-tratamento está funcionando?
3. A pressão efetiva está na faixa correta para o sistema?
4. A membrana está preservada e íntegra?
5. A qualidade da água produzida está estável e aceitável?

Ensaios úteis:

- acompanhar TDS ou indicador equivalente;
- medir produção real ao longo do tempo;
- verificar estado dos pré-filtros;
- revisar pressão e comportamento das bombas;
- avaliar histórico de paradas e preservação.

## Boas práticas

- operar o sistema em água adequada;
- registrar horas, TDS e intervenções;
- respeitar rotina de flush e preservação;
- dimensionar energia antes de instalar;
- prever acesso real para troca de filtros e serviço na membrana;
- tratar a água produzida com o critério definido pelo fabricante e pelo projeto sanitário do barco.

## Erros comuns

- instalar pelo marketing da autonomia sem pensar em operação;
- usar em água ruim e culpar a membrana;
- negligenciar preservação;
- achar que qualquer leitura isolada resolve o diagnóstico;
- ligar o sistema a um arranjo elétrico que não suporta o uso real.

## Integração com outras notas

- [[Bomba de Água Pressurizada]]
- [[Sensor de Nível de Água]]
- [[Boiler]]
- [[Carregador de Bateria (AC To DC)]]
- [[Gerador (AC)]]
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]]

## Perguntas que esta nota responde

- Quando um dessalinizador faz sentido técnico e operacional?
- Quais fatores realmente destroem produção e membrana?
- Como integrar o watermaker ao sistema elétrico e hidráulico da embarcação?
