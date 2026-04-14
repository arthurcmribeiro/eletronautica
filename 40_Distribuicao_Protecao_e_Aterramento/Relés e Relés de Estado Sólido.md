---
title: "Relés e Relés de Estado Sólido"
note_type: "technical-note"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "RELÉS E RELÉS DE ESTADO SÓLIDO 33a19734f7fb81488f55fb058be47993.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "RELÉS E RELÉS DE ESTADO SÓLIDO"
seo_title: "Relés e Relés de Estado Sólido"
seo_description: "RELES E RELES DE ESTADO SOLIDO — Dispositivos de comando e comutacao cuja escolha depende do tipo de carga, frequencia de acionamento, tensao, corrente, dissipacao e ambiente de instalacao."
seo_keywords:
  - "Rele"
  - "Rele de estado solido"
  - "Comutacao"
  - "40 Distribuicao Protecao e Aterramento"
geo_queries:
  - "Como escolher rele e SSR em embarcacoes?"
  - "Qual a diferenca entre rele eletromecanico e rele de estado solido?"
related_notes:
  - "Contatores (AC)"
  - "Chaves Gerais (DC)"
  - "Atuador Linear"
  - "Sistema de Alarme Geral / Painel de Alarmes"
  - "Automação de Bordo — Sistemas Domoticos"
  - "Disjuntores (DC) e (AC)"
---

# Relés e Relés de Estado Sólido

> [!abstract] Resumo técnico
> Relé é um dispositivo de comando que permite a um circuito de baixa potência controlar outro circuito. Em embarcações, a escolha correta depende do tipo de carga, corrente de partida, frequência de acionamento, ambiente, estratégia de falha e compatibilidade entre tecnologia eletromecânica ou estado sólido.

## O que é

Relés e dispositivos correlatos são elementos de interface entre lógica de comando e potência. Eles podem:

- acionar cargas;
- isolar circuitos de comando;
- implementar intertravamentos;
- permitir automação e supervisão.

Nem todo dispositivo de comutação é "só um relé". Em certos patamares de corrente, frequência ou criticidade, o componente adequado passa a ser um contator, um MOSFET switch dedicado ou outra arquitetura.

## Função na embarcação

- comandar bombas, ventiladores, atuadores e alarmes;
- isolar lógica de controle da carga principal;
- reduzir corrente circulando em botoeiras e controles;
- viabilizar automação e acionamentos remotos.

## Fundamentos mínimos

### Tipo de carga importa

Carga resistiva, indutiva, capacitiva ou eletrônica impõe estresses diferentes aos contatos ou semicondutores. Escolher relé apenas pela corrente nominal "em amperes" é uma das causas mais comuns de falha.

### Corrente de partida pode ser muito maior que a de regime

Motor, solenóide, bomba e certos atuadores podem exigir picos de corrente bem acima da corrente nominal contínua.

### SSR não é uma categoria homogênea

Há SSRs específicos para AC, SSRs específicos para DC e soluções MOSFET que o mercado chama genericamente de SSR. Tratar todos como equivalentes é erro técnico.

### Dissipação térmica faz parte da seleção

Dispositivo de estado sólido pode comutar rápido e sem contatos móveis, mas dissipa calor em condução e precisa de projeto térmico coerente.

## Tecnologias principais

### Relé eletromecânico

- usa bobina e contatos móveis;
- oferece isolamento e simplicidade;
- é adequado a muitas cargas quando bem especificado;
- sofre desgaste mecânico e elétrico ao longo do tempo.

### Relé de estado sólido

- não possui contato mecânico clássico;
- pode ser interessante em acionamento frequente ou silencioso;
- exige atenção a queda interna, dissipação, vazamento e compatibilidade AC/DC.

### Dispositivos especializados

- VSR/ACR para certas arquiteturas de bancos;
- contatores para correntes e esforços mais altos;
- módulos eletrônicos dedicados para automação embarcada.

## Projeto e instalação

### O que precisa ser definido

1. tensão do comando e da carga;
2. tipo de carga e corrente de partida;
3. frequência de acionamento;
4. ambiente de instalação;
5. estratégia de proteção da carga e do comando;
6. comportamento esperado em falha.

### Diretrizes práticas

- não especificar relé apenas por corrente nominal contínua;
- prever supressão adequada para cargas indutivas quando necessário;
- escolher tecnologia compatível com o tipo de corrente comutada;
- proteger e identificar os circuitos de comando e potência;
- prever acesso para substituição e diagnóstico.

## Onde costuma dar problema

| Problema | Causa provável |
| --- | --- |
| relé não aciona | falha na bobina, ausência de comando ou queda de tensão |
| contato cola ou degrada | carga acima do especificado ou carga inadequada |
| SSR aquece demais | subdimensionamento térmico ou aplicação inadequada |
| acionamento errático | comando ruidoso, tensão instável ou lógica ruim |
| vida útil baixa | escolha errada para frequência e ambiente de operação |

## Diagnóstico prático

1. Confirmar se o comando chega corretamente ao dispositivo.
2. Medir tensão no comando e na carga em operação.
3. Verificar aquecimento e integridade dos terminais.
4. Isolar se a falha está no relé, na lógica de comando ou na carga.
5. Conferir se o dispositivo escolhido é apropriado para AC ou DC e para o tipo de carga real.

## Boas práticas profissionais

- selecionar componente com base na aplicação real e não em equivalência genérica;
- documentar tensão de bobina, tipo de contato e função do circuito;
- considerar supressão de transientes quando a carga exigir;
- usar soluções de estado sólido só quando fizerem sentido térmico e funcional;
- preferir contatores quando corrente, duty ou criticidade saírem da zona de conforto do relé comum.

## Erros comuns

- chamar qualquer módulo eletrônico de SSR e achar que serve para qualquer carga;
- usar relé pequeno em motor ou bomba com partida pesada;
- esquecer dissipação térmica de comutação sólida;
- ignorar polaridade e especificação DC em circuito contínuo;
- usar relé como substituto improvisado de arquitetura de proteção.

## Relação com outros sistemas

- **[[Contatores (AC)]]** — quando a aplicação exige categoria superior de manobra.
- **[[Atuador Linear]]** — exemplo prático de comando de movimento.
- **[[Sistema de Alarme Geral / Painel de Alarmes]]** — saídas de sirene, sinalização e intertravamento.
- **[[Automação de Bordo — Sistemas Domoticos]]** — lógica de controle e supervisão.
- **[[Disjuntores (DC) e (AC)]]** — proteção do circuito comutado.

## Normas e referências

- documentação do fabricante do relé ou módulo eletrônico;
- especificação de categoria de carga, tensão e ambiente;
- critérios de instalação e proteção aplicáveis ao circuito comandado.

## FAQ

**SSR é sempre melhor que relé eletromecânico?**

Não. Depende do tipo de carga, corrente, frequência de acionamento, dissipação e estratégia de falha.

**Posso usar SSR AC em circuito DC?**

Não é uma premissa segura. Muitos SSRs para AC não funcionam corretamente em DC.

**Relé comum serve para qualquer motor pequeno?**

Não necessariamente. Corrente de partida, tensão e número de ciclos precisam entrar na análise.

## Integração com outras notas

- [[Contatores (AC)]]
- [[Chaves Gerais (DC)]]
- [[Atuador Linear]]
- [[Sistema de Alarme Geral / Painel de Alarmes]]
- [[Automação de Bordo — Sistemas Domoticos]]
- [[Disjuntores (DC) e (AC)]]

## Perguntas que esta nota responde

- Quando usar relé eletromecânico ou estado sólido em embarcações?
- Quais erros técnicos são mais comuns na seleção de relés?
- Como diagnosticar falhas de comando e comutação em bordo?
