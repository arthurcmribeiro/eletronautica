---
title: "Divisores de Carga (DC)"
note_type: "technical-note"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "DIVISORES DE CARGA (DC) 2f419734f7fb831cad5d81f3bc9880ae.md"
status: "technical-review-l1"
review_level: "engineering-curated"
aliases:
  - "DIVISORES DE CARGA (DC)"
  - "Isolação de bancos"
  - "Battery isolator"
seo_title: "Divisores de carga DC: ACR, isoladores, seletores e DC-DC em embarcações"
seo_description: "Guia técnico para separar e carregar bancos DC em embarcações sem confundir ACR, isolador por diodo/FET, chave seletora e carregador DC-DC."
seo_keywords:
  - "divisor de carga DC embarcação"
  - "ACR VSR náutico"
  - "isolador de baterias"
  - "carregador DC-DC banco de baterias"
geo_queries:
  - "Qual a diferença entre ACR, isolador de baterias e carregador DC-DC?"
  - "Como separar banco de partida e banco de serviço em uma embarcação?"
related_notes:
  - "Alternador (DC)"
  - "Bancos de Bateria"
  - "BMS — Battery Management System"
  - "Carregador de Bateria (AC To DC)"
  - "Chaves Gerais (DC)"
  - "Lítio LiFePO4 — Instalação e Cuidados Específicos"
  - "Monitor de Bateria - BMV - Shunt"
  - "Tipos de Bateria"
---

# Divisores de Carga (DC)

> [!abstract] Resumo técnico
> "Divisor de carga" é um nome guarda-chuva para estratégias de separação e compartilhamento de carga entre bancos DC. Em engenharia, é essencial separar os conceitos: chave seletora manual, ACR/VSR, isolador por diodo/FET e carregador DC-DC não fazem a mesma coisa e não devem ser tratados como equivalentes.

## O que esta nota realmente cobre

Na prática náutica, o termo costuma ser usado de forma imprecisa. Aqui, ele será tratado como arquitetura de gerenciamento entre bancos DC, especialmente entre:

- banco de partida;
- banco de serviço;
- bancos auxiliares ou dedicados;
- fontes como [[Alternador (DC)]], [[Carregador de Bateria (AC To DC)]] e solar.

## Problema técnico que precisa ser resolvido

Quando a embarcação tem mais de um banco, a arquitetura precisa responder a quatro perguntas:

1. Como garantir reserva para partida?
2. Como carregar múltiplos bancos sem criar desequilíbrios?
3. Como compatibilizar químicas diferentes?
4. Como manter operação de emergência simples e previsível?

Se a solução não responde a essas quatro perguntas, ela não está madura o suficiente.

## Tipos de solução e suas diferenças

### 1. Chave seletora manual

É a solução mais simples. O operador seleciona banco 1, banco 2, ambos ou off, conforme a arquitetura.

Vantagens:

- simplicidade;
- baixo custo;
- fácil entendimento em sistemas pequenos.

Limitações:

- depende de disciplina operacional;
- não compensa perfil de carga;
- aumenta risco de erro humano;
- não resolve adequadamente sistemas com lítio, alta corrente ou carga complexa.

### 2. ACR / VSR / combinador automático

É um dispositivo que conecta bancos quando detecta tensão de carga e os separa quando essa condição desaparece. É muito útil em sistemas chumbo-chumbo bem comportados e com alternador convencional.

Vantagens:

- operação automática;
- queda de tensão muito baixa quando fechado;
- boa relação custo-benefício em sistemas simples.

Limitações:

- não controla perfil de carga;
- não substitui regulador inteligente;
- pode ser inadequado em arquiteturas com lítio, BMS ou alternadores sensíveis;
- pode combinar bancos em momentos que a estratégia do projeto não deseja.

### 3. Isolador por diodo ou FET

Recebe uma fonte e a distribui a bancos separados sem conectá-los diretamente entre si. Os modelos antigos por diodo introduzem queda de tensão relevante; os baseados em FET reduzem esse problema, mas continuam exigindo análise cuidadosa de regulagem.

Vantagens:

- separação elétrica clara entre saídas;
- topologia previsível;
- útil em alguns sistemas com múltiplas saídas a partir de uma única fonte.

Limitações:

- pode afetar a tensão efetiva de carga;
- exige compatibilidade com regulador e estratégia do alternador;
- não corrige sozinho incompatibilidades entre químicas.

### 4. Carregador DC-DC

É a solução mais robusta quando se quer controlar de forma explícita o perfil de carga entre bancos diferentes ou quando a fonte primária não deve ser conectada diretamente ao banco de destino.

Vantagens:

- perfil de carga definido;
- melhor compatibilidade entre chumbo e lítio;
- desacoplamento elétrico e operacional mais limpo;
- proteção do alternador em muitas arquiteturas modernas.

Limitações:

- custo maior;
- potência limitada pelo modelo escolhido;
- exige projeto mais consciente de ventilação, proteção e cabos.

## O erro mais comum

O erro mais recorrente é usar "divisor de carga" como se qualquer solução servisse para qualquer sistema. Isso é falso.

Exemplos:

- ACR não é sinônimo de carregador DC-DC;
- chave manual não substitui gerenciamento automático em sistemas complexos;
- isolador FET não resolve, por si só, um banco de lítio com BMS agressivo;
- paralelar bancos de químicas diferentes sem estratégia costuma gerar comportamento ruim e, em alguns casos, perigoso.

## Critérios corretos de escolha

### Separar por função

Antes de escolher o equipamento, definir:

- qual banco é de partida;
- qual banco é de serviço;
- se existe banco dedicado a thruster, eletrônica ou emergência;
- quais fontes carregam cada banco;
- se haverá possibilidade de auxílio de partida entre bancos.

### Verificar a química

Arquiteturas chumbo-chumbo são mais tolerantes. Arquiteturas com [[Lítio LiFePO4 — Instalação e Cuidados Específicos]] exigem muito mais cuidado, especialmente quando há:

- BMS que pode abrir o circuito;
- alternador sem proteção contra load dump;
- grande diferença de capacidade entre bancos;
- necessidade de perfil de carga específico.

### Verificar a fonte de energia

A escolha muda conforme a fonte principal:

- [[Alternador (DC)]] pede atenção a corrente, temperatura e resposta do regulador;
- [[Carregador de Bateria (AC To DC)]] já pode ter saídas independentes;
- solar pode exigir prioridade ou caminho próprio de carga;
- inversores/carregadores podem introduzir lógica adicional.

### Verificar operação de emergência

Toda arquitetura com mais de um banco deve prever:

- isolamento normal;
- meio claro de paralelo de emergência;
- documentação visível para operação e manutenção.

## Falhas típicas em campo

As mais comuns são:

- banco de partida sendo drenado pelo banco de serviço;
- alternador trabalhando fora de sua zona segura por conexão inadequada com lítio;
- ACR oscilando por causa de tensão instável;
- queda excessiva de tensão em isoladores mal aplicados;
- cabos entre bancos sem proteção adequada;
- monitoramento ruim porque o [[Monitor de Bateria - BMV - Shunt]] está no lugar errado.

## Diagnóstico profissional

O diagnóstico deve responder:

1. Os bancos estão realmente separados quando deveriam?
2. A fonte está chegando com tensão e corrente compatíveis ao banco de destino?
3. O sistema está carregando como a química exige?
4. Existe caminho de emergência funcional e documentado?

Medições úteis:

- tensão de cada banco em repouso;
- tensão de cada banco durante carga;
- corrente entre bancos;
- resposta do sistema com motor ligado e desligado;
- atuação do BMS, quando houver;
- temperatura de cabos e conexões sob carga.

## Boas práticas de arquitetura

- manter banco de partida e banco de serviço com funções bem definidas;
- evitar paralelos permanentes sem justificativa de projeto;
- proteger cabos interbancos o mais próximo possível das fontes;
- preferir solução controlada por perfil quando houver lítio ou bancos muito diferentes;
- documentar a topologia com diagrama simples e legível;
- prever modo de emergência sem comprometer a operação normal;
- alinhar a solução de separação com a estratégia do alternador.

## O que geralmente merece reedição no conteúdo de campo

Há quatro simplificações que precisam ser combatidas:

- "ACR serve para qualquer sistema";
- "divisor por diodo e combinador automático fazem a mesma coisa";
- "se carrega, está certo";
- "lítio aceita qualquer arquitetura desde que tenha BMS".

Nenhuma dessas frases é tecnicamente robusta.

## Integração com outras notas

- [[Alternador (DC)]]
- [[Bancos de Bateria]]
- [[BMS — Battery Management System]]
- [[Carregador de Bateria (AC To DC)]]
- [[Chaves Gerais (DC)]]
- [[Lítio LiFePO4 — Instalação e Cuidados Específicos]]
- [[Monitor de Bateria - BMV - Shunt]]
- [[Tipos de Bateria]]

## Perguntas que esta nota responde

- Qual a diferença entre ACR, isolador por diodo/FET, chave seletora e carregador DC-DC?
- Como separar banco de partida e banco de serviço sem comprometer a carga?
- Em que situações ACR deixa de ser a melhor solução?
