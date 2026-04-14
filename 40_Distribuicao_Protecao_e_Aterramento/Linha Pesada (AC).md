---
title: "Linha Pesada (AC)"
note_type: "system"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "LINHA PESADA (AC) 6bd19734f7fb836e818f01ed1f949d26.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
review_level: "engineering-curated"
aliases:
  - "LINHA PESADA (AC)"
  - "Circuitos AC dedicados"
seo_title: "Linha pesada AC em embarcações: cargas dedicadas, seletividade e gestão de potência"
seo_description: "Critérios profissionais para projetar linha pesada AC em embarcações: cargas dedicadas, correntes de partida, seletividade, shore power, gerador, inversor e proteção."
seo_keywords:
  - "linha pesada AC embarcação"
  - "cargas dedicadas barco"
  - "ar condicionado shore power"
  - "gestão de potência embarcação"
geo_queries:
  - "Como projetar linha pesada AC para ar-condicionado e boiler em embarcação?"
  - "Quando uma carga deve ter circuito AC dedicado no barco?"
related_notes:
  - "Ar-Condicionado Marine — Sistema Completo"
  - "CAIS (Pier) (AC)"
  - "Chaves Seletoras (AC)"
  - "Contatores (AC)"
  - "Gerador (AC)"
  - "Inversora (DC To AC)"
  - "Linha Leve (AC)"
  - "Proteção Dr"
---

# Linha Pesada (AC)

> [!abstract] Resumo técnico
> Linha pesada AC é a camada da distribuição dedicada a cargas de alta potência, alta corrente de partida ou alta criticidade operacional. Em embarcações, ela define boa parte do dimensionamento do shore power, do gerador, do inversor e do próprio quadro AC.

## O que é

Não existe um único valor de corrente que transforme um circuito em "linha pesada". O critério profissional é mais amplo:

- carga com alta potência sustentada;
- carga com alto inrush;
- carga que exige circuito dedicado;
- carga que afeta diretamente a gestão global de potência;
- carga cuja falha não pode derrubar circuitos de uso geral.

Embarcações de recreio costumam enquadrar aqui:

- [[Ar-Condicionado Marine — Sistema Completo]];
- [[Boiler]];
- dessalinizador;
- cooktop, forno ou resistências relevantes;
- carregadores/inversores de maior porte;
- bombas ou máquinas com partida severa.

## Por que isso é central no projeto

É na linha pesada que aparecem, com mais frequência:

- sobrecarga do shore power;
- partida difícil de compressores;
- queda de tensão sob carga;
- aquecimento de conectores e cabos;
- coordenação ruim entre disjuntor, contator e fonte;
- conflito entre conforto e capacidade real da embarcação.

Projeto ruim de linha pesada normalmente cobra a conta cedo: disjuntor caindo, gerador sofrendo, compressor falhando e conectores aquecendo.

## Relação com as fontes de energia

A linha pesada precisa ser pensada a partir da fonte disponível:

- [[CAIS (Pier) (AC)]];
- [[Gerador (AC)]];
- [[Inversora (DC To AC)]], quando a arquitetura permitir;
- sistemas híbridos com gerenciamento de potência.

A pergunta correta não é "qual o disjuntor do equipamento", mas:

- qual fonte vai alimentá-lo;
- que outras cargas podem operar junto;
- qual corrente de partida aparece;
- como a transferência entre fontes será feita;
- o que deve ter prioridade quando a potência for insuficiente.

## Cargas típicas e exigências

### Compressores e ar-condicionado

São os casos mais clássicos de carga pesada. Exigem atenção a:

- corrente nominal;
- corrente de partida;
- quedas de tensão;
- contatores e proteção adequados;
- interação com shore power e gerador.

### Resistências e aquecimento

Boilers e aquecedores são mais previsíveis eletricamente, mas puxam corrente elevada por tempo prolongado. Isso afeta:

- dimensionamento do circuito;
- aquecimento em conectores;
- simultaneidade com outras cargas.

### Carregadores e inversores/carregadores

Não devem ser tratados como "eletrônica leve". Em correntes altas de carga, tornam-se grandes consumidores AC e interferem fortemente na gestão de energia do barco.

## Critérios corretos de projeto

### 1. Circuito dedicado

Toda carga relevante deve ter ramal próprio quando:

- a corrente é alta;
- a partida é severa;
- a criticidade operacional justifica segregação;
- a seletividade se perde se o circuito for compartilhado.

Compartilhar ar-condicionado, boiler e carregador no mesmo circuito raramente é decisão profissional.

### 2. Seletividade e coordenação

O circuito precisa coordenar:

- dispositivo de proteção;
- condutor;
- meio de manobra;
- características da carga;
- capacidade da fonte.

Disjuntor "maior para não cair" não corrige projeto ruim. Só desloca o problema para cabo, conector, contator ou equipamento.

### 3. Corrente de partida

Motores e compressores exigem análise de partida. Em alguns casos, vale considerar:

- soft starter;
- delay e lógica de prioridade;
- dimensionamento mais robusto do gerador;
- limitação ou programação do inversor/carregador;
- intertravamento entre cargas que não devem partir juntas.

### 4. Queda de tensão

Em linha pesada, a queda de tensão passa de detalhe a variável crítica. Partidas sob subtensão aumentam aquecimento, reduzem torque e elevam falhas.

### 5. Gestão de potência

Embarcações com múltiplas cargas pesadas pedem estratégia:

- prioridade manual;
- shedding automático;
- limitação de corrente do shore;
- controle pelo inversor/carregador;
- intertravamentos de partida.

## Falhas típicas em campo

As mais frequentes são:

- disjuntor do cais atuando quando uma carga pesada entra;
- gerador incapaz de sustentar a partida do compressor;
- conector de shore power aquecendo;
- cabo ou borne aquecendo em operação contínua;
- DR disparando por arquitetura incompatível ou fuga real;
- mistura de linha leve e linha pesada no mesmo circuito;
- circuito dedicado mal dimensionado por ignorar inrush e simultaneidade.

## Diagnóstico profissional

O diagnóstico deve medir:

- tensão na origem, no quadro e na carga;
- corrente em regime e no momento de partida, quando possível;
- temperatura de conectores, cabos e terminais;
- resposta da proteção;
- comportamento da fonte sob carga.

Perguntas importantes:

1. A fonte suporta a carga sozinha?
2. O circuito derivado foi pensado para essa carga ou só "adaptado"?
3. O problema é proteção, cabo, contato, carga ou falta de gestão de potência?

## Boas práticas

- usar circuito dedicado para cada carga pesada relevante;
- alinhar proteção, cabo e regime real da carga;
- prever lógica de prioridade quando a soma de cargas puder exceder a fonte;
- tratar conectores e cabos de entrada como itens críticos de manutenção;
- documentar quais cargas podem operar simultaneamente em cada fonte;
- separar claramente linha leve e linha pesada no quadro e no diagrama.

## Erros comuns

Os erros mais danosos são:

- projetar pela corrente nominal e ignorar a partida;
- usar um único circuito para várias cargas severas;
- resolver queda de tensão com disjuntor maior;
- tratar carregador de grande porte como carga "secundária";
- esquecer que a linha pesada redefine a arquitetura inteira do AC do barco.

## Integração com outras notas

- [[Ar-Condicionado Marine — Sistema Completo]]
- [[CAIS (Pier) (AC)]]
- [[Chaves Seletoras (AC)]]
- [[Contatores (AC)]]
- [[Gerador (AC)]]
- [[Inversora (DC To AC)]]
- [[Linha Leve (AC)]]
- [[Proteção Dr]]

## Perguntas que esta nota responde

- Quando uma carga deve receber circuito dedicado na embarcação?
- Como a linha pesada influencia shore power, gerador e inversor?
- Por que falhas em ar-condicionado, boiler e carregador quase sempre revelam problema maior de arquitetura AC?
