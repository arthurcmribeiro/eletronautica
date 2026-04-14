---
title: "Alarme de Alagamento / Sensor de Porão"
note_type: "technical-note"
domain: "80_Seguranca_e_Corrosao"
source_file: "ALARME DE ALAGAMENTO SENSOR DE PORÃO 33a19734f7fb81d2ba97e64f015d6859.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "ALARME DE ALAGAMENTO SENSOR DE PORÃO"
  - "ALARME DE ALAGAMENTO / SENSOR DE PORÃO"
seo_title: "Alarme de Alagamento / Sensor de Porão"
seo_description: "ALARME DE ALAGAMENTO — Sistema de alto nivel de agua no porao que complementa a bomba de bilge, exige sensor independente, alimentacao nao seccionada e aviso perceptivel ao operador."
seo_keywords:
  - "Alarme de alagamento"
  - "High water alarm"
  - "Sensor de porao"
  - "Bilge alarm"
  - "80 Seguranca e Corrosao"
geo_queries:
  - "Como instalar alarme de alagamento em embarcacao?"
  - "Qual a diferenca entre bomba de porao e alarme de alto nivel?"
related_notes:
  - "Bomba de Porão"
  - "Sistema de Alarme Geral / Painel de Alarmes"
  - "Monitoramento Remoto — VRM / Telemetria"
  - "Sensor de Nível de Água"
  - "Hotline (DC)"
---

# Alarme de Alagamento / Sensor de Porão

> [!abstract] Resumo técnico
> Alarme de alagamento, ou high water alarm, é o sistema que avisa quando o nível de água no porão ultrapassa a condição normal de bombeamento. Ele não substitui a bomba de porão: atua como camada de alerta e diagnóstico para inundação progressiva, falha da bomba ou entrada anormal de água.

## O que é

É um sistema composto por:

- sensor ou chave de alto nível;
- lógica de alarme;
- aviso sonoro e/ou visual;
- eventualmente integração com monitoramento remoto.

Seu papel é detectar condição anormal de água, não apenas ligar a bomba.

## Função na embarcação

- alertar subida anormal do nível de água;
- indicar que a bomba não está vencendo a entrada de água ou falhou;
- permitir ação rápida da tripulação;
- complementar a bomba automática e o monitoramento do barco.

## Fundamentos mínimos

### Bomba de porão e alarme são funções diferentes

- bomba: remove água;
- alarme: informa condição anormal.

Se ambos dependem do mesmo sensor ou da mesma lógica, perde-se independência funcional.

### Alarme de alto nível pede sensor independente

A arquitetura mais robusta usa sensor dedicado de alarme acima do nível normal de acionamento da bomba automática, para indicar anomalia e não operação rotineira.

### Alimentação precisa continuar disponível

Alarme de alto nível perde grande parte do valor se fica morto quando a chave principal é desligada. A estratégia de alimentação deve refletir a função de segurança do sistema.

### Um único compartimento pode não bastar

Embarcações com múltiplos espaços sujeitos a inundação podem precisar de mais de um sensor, conforme a compartimentação e os pontos de risco.

## Projeto e instalação

### O que precisa ser definido

1. quais espaços estão sujeitos a alagamento;
2. qual o nível normal de partida da bomba;
3. qual o nível de alarme desejado;
4. onde o operador verá e ouvirá o aviso;
5. se haverá notificação remota;
6. como o circuito será alimentado e protegido.

### Diretrizes práticas

- instalar sensor de alarme independente e acima do nível de trabalho normal da bomba;
- posicionar o aviso em ponto perceptível ao operador;
- manter a fiação fora da água e protegida mecanicamente;
- prever teste periódico simples e claro;
- documentar a lógica do sistema e as zonas atendidas.

## Onde costuma dar problema

| Problema | Causa provável |
| --- | --- |
| alarme não dispara | sensor travado, circuito sem alimentação adequada ou instalação errada |
| alarme falso recorrente | sensor mal posicionado, detritos, turbulência ou contaminação |
| alarme soa mas ninguém percebe | buzzer fraco, ausência de indicação no ponto de operação |
| bomba atua e ninguém sabe | ausência de alarme ou de indicador de bomba em operação |
| compartimento crítico sem cobertura | projeto incompleto da compartimentação |

## Diagnóstico prático

1. Confirmar que o sistema permanece energizado conforme a arquitetura definida.
2. Testar o sensor de alarme de forma controlada.
3. Verificar diferença de nível entre acionamento da bomba e acionamento do alarme.
4. Inspecionar estado do sensor, do chicote e do módulo de alarme.
5. Confirmar que o aviso chega ao posto de comando ou área ocupada relevante.

## Boas práticas profissionais

- usar sensor independente para o alarme de alto nível;
- alimentar por circuito não seccionado quando a função exigir vigilância contínua;
- prever alarme visual e sonoro perceptíveis;
- adicionar monitoramento remoto apenas como complemento, não substituto do alarme local;
- testar periodicamente bomba, sensor de bomba e sensor de alto nível separadamente.

## Erros comuns

- chamar bomba automática de "alarme";
- usar o mesmo sensor da bomba como único elemento de detecção;
- alimentar o sistema de modo que ele fique morto com o barco parado;
- instalar aviso quase inaudível ou escondido;
- ignorar compartimentos secundários propensos a entrada de água.

## Relação com outros sistemas

- **[[Bomba de Porão]]** — sistema complementar, com função diferente.
- **[[Sistema de Alarme Geral / Painel de Alarmes]]** — centralização do aviso.
- **[[Monitoramento Remoto — VRM / Telemetria]]** — camada remota complementar.
- **[[Sensor de Nível de Água]]** — comparação entre medição de tanque e detecção de inundação.
- **[[Hotline (DC)]]** — lógica de circuito permanentemente disponível, quando aplicável.

## Normas e referências

- requisitos aplicáveis da embarcação para bilge systems e high water alarm;
- documentação do sensor e do módulo de alarme;
- boas práticas de alimentação, proteção e teste periódico do sistema.

## FAQ

**Alarme de alagamento substitui a bomba de porão?**

Não. Ele complementa a bomba com função de alerta.

**Posso usar o mesmo float da bomba para acionar o alarme?**

É possível em arquiteturas simples, mas reduz independência funcional e tende a piorar a qualidade do alerta. Sensor dedicado é abordagem melhor.

**Notificação remota resolve o problema sozinha?**

Não. Ela ajuda quando o barco está desacompanhado, mas não substitui alarme local robusto.

## Integração com outras notas

- [[Bomba de Porão]]
- [[Sistema de Alarme Geral / Painel de Alarmes]]
- [[Monitoramento Remoto — VRM / Telemetria]]
- [[Sensor de Nível de Água]]
- [[Hotline (DC)]]

## Perguntas que esta nota responde

- Qual a função real do alarme de alagamento em uma embarcação?
- Como ele deve se relacionar com a bomba de porão?
- Quais erros tornam um high water alarm praticamente inútil?
