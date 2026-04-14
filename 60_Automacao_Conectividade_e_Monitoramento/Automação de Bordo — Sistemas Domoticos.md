---
title: "Automação de Bordo — Sistemas Domoticos"
note_type: "system"
domain: "60_Automacao_Conectividade_e_Monitoramento"
source_file: "AUTOMAÇÃO DE BORDO — SISTEMAS DOMOTICOS 33a19734f7fb81b99e7fcd10258cd8f3.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://www.nmea.org/standards.html"
  - "https://www.nmea.org/nmea-0400.html"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "AUTOMAÇÃO DE BORDO — SISTEMAS DOMOTICOS"
seo_title: "Automação de Bordo — Sistemas Domoticos"
seo_description: "AUTOMACAO DE BORDO — Integracao de sensores, logica e atuacao para operar sistemas de forma assistida ou automatica. O criterio central e fail-safe, override manual e limites claros de escopo."
seo_keywords:
  - "Automação"
  - "Domoticos"
  - "60 Automacao Conectividade e Monitoramento"
geo_queries:
  - "O que e Automacao de Bordo — Sistemas Domoticos em instalacoes eletricas nauticas?"
  - "Qual e a funcao de Automacao de Bordo — Sistemas Domoticos na embarcacao?"
related_notes:
  - "Atuador Linear"
  - "Câmeras de Bordo / Sistema CFTV"
  - "Interfone / Intercomunicador de Bordo"
  - "Monitoramento Remoto — VRM / Telemetria"
  - "Sensor de Nível Diesel"
  - "Sistema de Alarme Geral / Painel de Alarmes"
  - "Som"
  - "Starlink / Internet a Bordo"
---

# Automação de Bordo — Sistemas Domoticos

> [!abstract] Resumo técnico
> AUTOMAÇÃO DE BORDO — Integração de sensores, lógica e atuação para operar sistemas de forma assistida ou automática. O critério central não é “fazer sozinho”, e sim falhar de forma segura, permitir override manual e não transformar conveniência em ponto único de falha.

## O que é

Automação de bordo é o uso coordenado de sensores, controladores, relés, interfaces e lógicas de decisão para supervisionar ou acionar sistemas da embarcação. Ela pode ser simples, como o acionamento automático de uma bomba, ou mais sofisticada, como gestão de energia com telemetria e comandos remotos.

O erro comum é tratar tudo como se fosse “domótica residencial no barco”. Em embarcação, automação convive com:

- limitação energética;
- ambiente severo;
- riscos à vida e ao patrimônio;
- necessidade de fallback manual.

## Função

- automatizar funções repetitivas e previsíveis;
- reduzir erro operacional em tarefas bem definidas;
- melhorar supervisão e rastreabilidade;
- apoiar manutenção e diagnóstico;
- integrar dados de sistemas distintos sem substituir o julgamento do operador.

## Níveis de automação

**Nível 1 — automação funcional**

- bombas automáticas;
- carregadores inteligentes;
- monitoramento básico;
- relés de transferência ou lógica simples de habilitação.

**Nível 2 — automação supervisória**

- gestão energética;
- telemetria e alarmes;
- históricos;
- integração entre subsistemas.

**Nível 3 — automação integrada**

- comandos remotos;
- sequências coordenadas;
- múltiplas fontes de dados;
- interfaces centralizadas.

Quanto maior o nível, maior a exigência de documentação, teste, governança e contingência.

## Fundamentos mínimos

**Fail-safe:** ao falhar, o sistema deve ir para um estado previsível e seguro.

**Override manual:** funções críticas precisam de forma clara de operação manual.

**Supervisão não é atuação:** nem todo dado precisa gerar comando automático.

**Barramento de dados não é PLC:** NMEA 2000, por exemplo, é excelente para compartilhamento de dados, mas não deve ser tratado automaticamente como backbone de automação de segurança.

**Tempo de resposta e criticidade:** lógica para conforto e lógica para segurança não devem ser projetadas com o mesmo nível de tolerância.

## Onde a automação faz sentido

- monitoramento energético;
- alarmes e eventos;
- rotinas de conveniência não críticas;
- sequências bem compreendidas de gestão de fontes;
- telemetria e manutenção preditiva.

## Onde a automação exige mais cautela

- qualquer função cuja falha possa gerar perda de propulsão, inundação, incêndio ou risco à vida;
- comandos remotos sem confirmação local;
- automações que escondem o estado real do sistema do operador;
- soluções customizadas sem documentação e sem fallback.

## Arquitetura recomendada

```text
Sensores -> lógica/controlador -> atuação
                 ↓
           alarmes e registro
                 ↓
        interface local + remoto
```

Separar essas camadas ajuda a evitar que um único erro derrube tudo ao mesmo tempo.

## Problemas mais frequentes

| Problema | Causa provável |
| --- | --- |
| automação “misteriosa” | lógica não documentada |
| desligamentos inesperados | limites mal parametrizados ou dependência excessiva de proteção |
| excesso de alarmes | lógica sem histerese e sem priorização |
| operador perdido em falha | ausência de override manual |
| projeto frágil | mistura de dados, potência e segurança sem separação clara |

## Diagnóstico prático

1. Identificar a função automática real e a condição de disparo.
2. Confirmar quem decide, quem atua e quem pode sobrescrever manualmente.
3. Verificar alimentação, sensores, saídas e lógica de intertravamento.
4. Reproduzir o cenário com teste controlado.
5. Validar documentação e comportamento de falha.

## Boas práticas

- automatizar só o que está entendido manualmente;
- documentar condição de atuação, condição de falha e condição de retorno;
- manter override manual acessível;
- registrar eventos e mudanças de parâmetro;
- separar conveniência, supervisão e segurança em níveis claros;
- testar periodicamente as automações críticas.

## Erros comuns

- automatizar antes de entender a operação manual;
- usar barramento de dados como se fosse malha de segurança;
- tratar app remoto como interface principal de funções críticas;
- criar dependência de internet para funções locais essenciais;
- construir automação custom sem documentação, nomenclatura e estratégia de manutenção.

## Relação com outros sistemas

- **Monitoramento remoto** — camada supervisória e histórica.
- **Sistema de alarme** — detecção e notificação de eventos.
- **Nível diesel / sensores** — entrada de dados.
- **Atuadores e relés** — camada de atuação.
- **Conectividade** — suporte ao acesso remoto, nunca substituto da operação local crítica.

## Brasil x referências internacionais

### Leitura equilibrada

No mercado local, muita “automação” ainda é só soma de módulos desconectados. Em projetos maduros, automação é arquitetura, não coleção de gadgets.

## Normas e referências

- **Documentação do fabricante** — lógica, limites e wiring dos controladores.
- **Boas práticas de instalação elétrica e de segurança funcional** — conforme a criticidade do sistema envolvido.

## FAQ

**Automação sempre melhora a segurança?**

Não. Automação mal pensada pode criar novas falhas e mascarar o estado real do sistema.

**NMEA 2000 é sistema de automação?**

É principalmente um barramento de compartilhamento de dados. Pode participar da arquitetura, mas não deve ser confundido com malha de segurança por si só.

**Vale a pena automatizar tudo?**

Não. O critério correto é custo técnico, criticidade, mantenabilidade e risco de falha.

## Integração com outras notas

- [[Atuador Linear]]
- [[Câmeras de Bordo / Sistema CFTV]]
- [[Interfone / Intercomunicador de Bordo]]
- [[Monitoramento Remoto — VRM / Telemetria]]
- [[Sensor de Nível Diesel]]
- [[Sistema de Alarme Geral / Painel de Alarmes]]
- [[Som]]
- [[Starlink / Internet a Bordo]]

## Perguntas que esta nota responde

- O que é Automação de Bordo — Sistemas Domoticos em instalações elétricas náuticas?
- Qual é a função da automação de bordo na embarcação?
