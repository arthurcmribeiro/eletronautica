---
title: "Linha Leve (AC)"
note_type: "system"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "LINHA LEVE (AC) f9e19734f7fb82ebb08a01bde9cf45c6.md"
status: "technical-review-l1"
review_level: "engineering-curated"
aliases:
  - "LINHA LEVE (AC)"
  - "Circuitos AC de uso geral"
seo_title: "Linha leve AC em embarcações: tomadas, circuitos de uso geral e proteção"
seo_description: "Arquitetura técnica da linha leve AC em embarcações: circuitos de uso geral, proteção diferencial, setorização, quedas de tensão e integração com shore power, gerador e inversor."
seo_keywords:
  - "linha leve AC embarcação"
  - "tomadas AC barco"
  - "circuitos de uso geral náutico"
  - "proteção diferencial AC embarcações"
geo_queries:
  - "Como organizar a linha leve AC de uma embarcação?"
  - "Quais proteções usar em circuitos AC de uso geral no barco?"
related_notes:
  - "CAIS (Pier) (AC)"
  - "Chaves Seletoras (AC)"
  - "Disjuntores (DC) e (AC)"
  - "Fase e Neutro"
  - "Inversora (DC To AC)"
  - "Linha Pesada (AC)"
  - "Proteção Dr"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
---

# Linha Leve (AC)

> [!abstract] Resumo técnico
> Linha leve AC é a parte da distribuição em corrente alternada dedicada a tomadas e cargas de uso geral, normalmente com potência moderada e menor severidade de partida do que a [[Linha Pesada (AC)]]. O critério correto não é um número mágico de watts, mas a natureza da carga, a setorização e a coordenação das proteções.

## O que é

Na prática de projeto, a linha leve reúne os circuitos AC destinados a:

- tomadas de uso geral;
- pequenos eletrodomésticos;
- entretenimento e eletrônica de cabine;
- alguns auxiliares de conforto de baixa ou média potência;
- circuitos que não exigem ramal dedicado por alto inrush ou potência sustentada.

Ela convive com a linha pesada, mas não deve ser tratada como "resto do quadro". Continua exigindo projeto, proteção e documentação.

## O que diferencia da linha pesada

A diferença mais útil não é apenas a potência.

Linha leve costuma ter:

- cargas mais dispersas;
- maior quantidade de pontos de consumo;
- maior importância de setorização;
- mais interação com usuários finais;
- mais risco de improviso com extensões, adaptadores e plugues.

Linha pesada, por sua vez, tende a ter circuitos dedicados para cargas específicas, como compressores, boilers e carregadores de maior porte.

## Arquitetura recomendada

A distribuição madura de linha leve AC costuma incluir:

- alimentação a partir do quadro AC principal;
- divisão por áreas ou funções;
- proteção por circuito;
- proteção diferencial em pontos apropriados;
- identificação clara no quadro;
- compatibilidade com a fonte ativa: shore, gerador ou inversor.

Em vez de "um único disjuntor para todas as tomadas", o correto é pensar por zonas:

- salão;
- camarotes;
- banheiro;
- galley;
- cockpit ou áreas externas, se aplicável.

## Cargas típicas

São exemplos usuais:

- TVs, monitores e som;
- carregadores portáteis;
- notebook e equipamentos de escritório;
- pequenos eletrodomésticos de bancada;
- tomadas de apoio em áreas internas;
- alguns circuitos de conveniência alimentados por [[Inversora (DC To AC)]], quando essa for a arquitetura.

Mesmo nessa faixa, um conjunto de pequenas cargas pode saturar um circuito mal setorizado.

## Critérios corretos de projeto

### 1. Setorização

Setorizar melhora:

- diagnóstico;
- seletividade;
- continuidade operacional;
- manutenção.

Uma falha em um banheiro, por exemplo, não deveria apagar todas as tomadas do barco.

### 2. Proteção diferencial

Circuitos de uso geral e áreas úmidas pedem proteção diferencial bem pensada. A aplicação pode ser:

- DR geral;
- RCBO por circuito;
- combinação de proteção geral e proteção adicional localizada.

A solução depende da topologia do quadro, da seletividade desejada e da presença de fontes eletrônicas que possam exigir dispositivos adequados ao tipo de corrente residual esperado.

### 3. Queda de tensão e comprimento

Mesmo na linha leve, cabos longos, conexões ruins e adaptadores improvisados degradam tensão em carga. Isso afeta desempenho, aquece conexões e aumenta falhas intermitentes.

### 4. Ambiente de instalação

Em embarcação, tomada, borne e caixa sofrem com:

- vibração;
- condensação;
- spray salino;
- ciclos térmicos;
- mau uso por adaptação de plugues.

Tomada "residencial comum" pode funcionar, mas isso não a torna boa solução técnica para ambiente marinho.

## Integração com as fontes AC

Linha leve pode ser alimentada por:

- [[CAIS (Pier) (AC)]];
- [[Gerador (AC)]];
- [[Inversora (DC To AC)]];
- sistemas híbridos com transferência automática.

O projeto precisa garantir coerência entre:

- seletora ou transferência de fontes;
- presença ou não de neutro referenciado conforme a topologia;
- atuação correta de [[Proteção Dr]];
- limites de potência do inversor quando a linha leve for alimentada em navegação ou fundeio.

## Falhas típicas em campo

As falhas mais comuns são:

- tomada aquecendo por borne frouxo;
- circuito caindo por excesso de carga agregada;
- disparo diferencial intermitente com equipamento específico;
- ponto de tomada "morto" por emenda ou borne solto;
- tensão baixa por conector, adaptador ou cabo inadequado;
- circuito de uso geral misturado com carga que deveria estar em linha pesada.

## Diagnóstico profissional

O diagnóstico deve seguir o caminho da energia:

1. fonte AC;
2. entrada do quadro;
3. dispositivo de proteção;
4. circuito derivado;
5. ponto de consumo;
6. carga conectada.

Medições úteis:

- tensão sem carga e com carga;
- corrente do circuito;
- continuidade e integridade de bornes;
- temperatura de tomadas, conectores e disjuntores;
- comportamento do DR/RCBO com diferentes cargas.

## Boas práticas

- dividir a linha leve por setores ou funções;
- usar componentes adequados ao ambiente marinho ou, no mínimo, a áreas úmidas e vibrantes;
- evitar adaptadores permanentes como solução estrutural;
- manter diagrama e identificação de circuitos atualizados;
- prever circuitos externos com cuidado adicional de vedação e proteção;
- coordenar o uso da linha leve com a potência disponível no cais, no gerador ou no inversor.

## Erros comuns

Os mais recorrentes são:

- colocar todas as tomadas em um único circuito;
- usar cabo e tomada sem considerar ambiente e vibração;
- esquecer que um circuito de uso geral também precisa de seletividade;
- alimentar linha leve por inversor sem controlar a potência total;
- tratar a linha leve como algo "simples" demais para exigir projeto.

## Integração com outras notas

- [[CAIS (Pier) (AC)]]
- [[Chaves Seletoras (AC)]]
- [[Disjuntores (DC) e (AC)]]
- [[Fase e Neutro]]
- [[Inversora (DC To AC)]]
- [[Linha Pesada (AC)]]
- [[Proteção Dr]]
- [[Quadro Elétrico e Painel de Distribuição AC-DC]]

## Perguntas que esta nota responde

- Como separar corretamente a linha leve da linha pesada em uma embarcação?
- Quais critérios tornam um circuito AC de uso geral realmente bem projetado?
- Como evitar que tomadas e circuitos de conveniência virem ponto de falha recorrente?
