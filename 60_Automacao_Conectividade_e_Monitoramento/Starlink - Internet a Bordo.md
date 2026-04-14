---
title: "Starlink / Internet a Bordo"
note_type: "system"
domain: "60_Automacao_Conectividade_e_Monitoramento"
source_file: "STARLINK INTERNET A BORDO 33a19734f7fb81018482d2332b9c9d34.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://www.nmea.org/standards.html"
  - "https://www.nmea.org/nmea-0400.html"
  - "https://www.iso.org/standard/83643.html"
  - "https://www.starlink.com/business/maritime"
aliases:
  - "STARLINK INTERNET A BORDO"
  - "STARLINK / INTERNET A BORDO"
  - "Starlink Internet a Bordo"
seo_title: "Starlink / Internet a Bordo"
seo_description: "STARLINK / INTERNET A BORDO — Conectividade satelital de banda larga para uso maritimo e remoto. Hardware, cobertura e planos variam por regiao e devem ser verificados em fonte oficial."
seo_keywords:
  - "Starlink"
  - "Internet"
  - "60 Automacao Conectividade e Monitoramento"
geo_queries:
  - "O que e Starlink / Internet a Bordo em instalacoes eletricas nauticas?"
  - "Qual e a funcao de Starlink / Internet a Bordo na embarcacao?"
related_notes:
  - "Atuador Linear"
  - "Automação de Bordo — Sistemas Domoticos"
  - "Câmeras de Bordo / Sistema CFTV"
  - "Interfone / Intercomunicador de Bordo"
  - "Monitoramento Remoto — VRM / Telemetria"
  - "Sensor de Nível Diesel"
  - "Sistema de Alarme Geral / Painel de Alarmes"
  - "Som"
---

# Starlink / Internet a Bordo

> [!abstract] Resumo técnico
> STARLINK / INTERNET A BORDO — Solução de conectividade via satélite LEO para uso remoto, costeiro e marítimo, dependendo do hardware e do plano contratados. Cobertura, uso em movimento e acesso em águas costeiras ou oceânicas devem sempre ser confirmados na documentação oficial vigente.

## O que é

Starlink é um sistema de acesso à internet via constelação de satélites de órbita baixa. Em ambiente marítimo, ele se tornou uma alternativa prática ao VSAT tradicional e, em muitas situações, complementa ou substitui o 4G/5G costeiro.

Para uso a bordo, o ponto técnico mais importante é entender que "Starlink" não é uma solução única. Há diferenças relevantes entre:

- hardware portátil e de baixo consumo;
- kits de instalação permanente e maior robustez;
- uso costeiro/inland waters;
- uso em águas internacionais;
- operação fixa e em movimento.

## O que está confirmado em fonte oficial

Segundo as páginas oficiais da Starlink:

- os planos **Roam** podem ser usados em viagem e incluem uso em embarcações em águas territoriais e interiores, com opção de cobertura oceânica;
- para uso oceânico frequente ou prolongado, a própria Starlink direciona o usuário para a linha **Maritime**;
- o **Starlink Mini** é portátil, tem roteador Wi-Fi integrado, entrada DC e velocidades de download acima de 100 Mbps;
- o **Starlink Performance** é voltado a instalação permanente, foi projetado para ambientes severos, pode operar em AC e/ou DC e a Starlink informa capacidade atual de download de até 400+ Mbps no kit, além de melhorias de rede planejadas para 2026.

## Função na embarcação

- fornecer acesso externo à internet onde 4G/5G não atende;
- suportar monitoramento remoto, atualização de sistemas e comunicação de dados;
- permitir operações de bordo, trabalho remoto e entretenimento;
- atuar como WAN principal ou secundária dentro de uma arquitetura multi-WAN.

## Fundamentos mínimos

**Cobertura:** não tratar como global/universal sem conferir mapa e plano oficiais.

**Energia:** Starlink não é carga desprezível. Mesmo quando o hardware é eficiente, ele deve entrar no balanço energético da embarcação.

**Obstrução:** antenas LEO continuam exigindo bom campo de visão do céu. Mastro, radar, hardtop e superestrutura importam.

**Arquitetura de rede:** Starlink resolve a WAN; o Wi-Fi a bordo continua dependendo da rede local da embarcação.

## Critérios de decisão

| Cenário | Diretriz |
| --- | --- |
| uso predominantemente costeiro | comparar Starlink com 4G/5G e arquitetura híbrida |
| uso oceânico frequente | verificar linha e plano marítimo oficiais |
| baixo orçamento energético | avaliar consumo real e regime de uso |
| instalação permanente | tratar suporte, passagem de cabos e manutenção como parte do projeto |
| uso casual e portátil | avaliar kits compactos e limites operacionais |

## Problemas mais frequentes

| Problema | Causa provável |
| --- | --- |
| quedas de conexão | obstrução, movimento, cobertura/plano ou alimentação |
| consumo acima do esperado | regime de uso contínuo e subdimensionamento energético |
| expectativa errada sobre cobertura oceânica | leitura incompleta do plano contratado |
| Wi-Fi interno ruim | confusão entre Starlink e arquitetura LAN local |
| reinício em transientes | alimentação DC mal tratada |

## Diagnóstico prático

1. Separar problema de `WAN Starlink` de `rede local Wi-Fi`.
2. Confirmar o plano e o cenário de uso contratados.
3. Verificar campo de visão e posicionamento da antena.
4. Avaliar qualidade da alimentação e comportamento em partidas/transientes.
5. Conferir se a topologia local não está mascarando o problema.

## Boas práticas

- verificar cobertura, plano e limitações em fonte oficial antes da compra;
- tratar Starlink como parte do projeto de energia, não apenas de telecom;
- prever integração com roteador/gateway adequado;
- separar WAN satelital de rede local interna;
- instalar suporte e passagem de cabo com padrão mecânico adequado ao ambiente marítimo.

## Erros comuns

- comprar pelo marketing sem confirmar plano e área real de uso;
- assumir que qualquer kit serve igualmente para mar aberto;
- ignorar impacto energético no banco de baterias;
- montar o sistema sem pensar na rede local e na redundância com 4G/5G;
- fixar antena em ponto com obstrução relevante.

## Relação com outros sistemas

- **Wi-Fi a Bordo** — Starlink normalmente alimenta a WAN do roteador local.
- **Monitoramento remoto** — depende de conectividade externa.
- **Câmeras de bordo** — acesso remoto e upload de eventos.
- **Sistema de alarme** — envio de alertas quando houver internet disponível.

## Normas e referências

- **Starlink Roam**: [starlink.com/roam](https://www.starlink.com/us/roam)
- **Starlink Maritime**: [starlink.com/maritime](https://www.starlink.com/maritime)
- **Regulação nacional aplicável** — homologação e uso conforme a jurisdição.

## FAQ

**Starlink substitui totalmente o 4G/5G?**

Nem sempre. Em muitos projetos, a arquitetura híbrida faz mais sentido.

**Todo Starlink serve para oceano?**

Não é seguro assumir isso. O critério correto é conferir hardware, plano e cobertura oficiais.

**O principal risco técnico é a antena?**

A antena é crítica, mas alimentação, cobertura/plano e integração com a rede local pesam quase tanto quanto.

## Integração com outras notas

- [[Atuador Linear]]
- [[Automação de Bordo — Sistemas Domoticos]]
- [[Câmeras de Bordo / Sistema CFTV]]
- [[Interfone / Intercomunicador de Bordo]]
- [[Monitoramento Remoto — VRM / Telemetria]]
- [[Sensor de Nível Diesel]]
- [[Sistema de Alarme Geral / Painel de Alarmes]]
- [[Som]]

## Perguntas que esta nota responde

- O que é Starlink / Internet a Bordo em instalações elétricas náuticas?
- Qual é a função de Starlink / Internet a Bordo na embarcação?
