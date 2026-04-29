---
title: "MOC — Automacao Conectividade e Monitoramento"
note_type: "moc"
domain: "60_Automacao_Conectividade_e_Monitoramento"
status: "moc-curated-plus"
fase_6_reescrita: 140
reviewed_on: "2026-04-29"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
review_level: "moc-curated-plus"
aliases:
  - "MOC Automacao"
  - "Hub automacao conectividade monitoramento"
seo_title: "MOC Automação Náutica: domótica, sensores, alarmes, VRM, Starlink, Wi-Fi, câmeras e USB 12V"
seo_description: "Hub do domínio 60 para automação, conectividade e monitoramento em embarcações: atuadores, domótica, sensores de nível, alarme geral, telemetria VRM, Starlink, Wi-Fi, CFTV, entretenimento e alimentação USB."
seo_keywords:
  - "automação náutica"
  - "monitoramento remoto VRM"
  - "Starlink barco"
  - "Wi-Fi a bordo"
  - "alarme geral embarcação"
geo_queries:
  - "Como monitorar uma embarcação remotamente?"
  - "Starlink substitui roteador Wi-Fi a bordo?"
  - "Como integrar sensores e alarmes no barco?"
  - "Como alimentar USB 12V sem ruído?"
  - "Quando automação de bordo vale a pena?"
normas_citadas: []
related_notes:
  - "Atlas Técnico"
  - "MOC — Energia e Conversao"
  - "MOC — Distribuicao Protecao e Aterramento"
  - "MOC — Segurança Integrada"
---

# MOC — Automacao Conectividade e Monitoramento

> [!abstract] Sobre este domínio
> Este domínio cobre a camada digital e de supervisão da embarcação: automação de cargas, sensores, alarmes, conectividade WAN/LAN, telemetria, CFTV, áudio/vídeo e pontos de alimentação USB. **Venha aqui** quando a pergunta envolver monitorar, comandar, registrar evento ou manter comunicação a bordo. Não use este MOC para dimensionar potência principal: isso pertence a energia, distribuição e baterias.

> [!tip] Trilhas de leitura
> - **Barco conectado básico:** [[Wi-Fi a Bordo — Roteador Marine e Conectividade]] → [[Starlink - Internet a Bordo]] → [[USB 12V (Power)]]
> - **Monitoramento remoto:** [[Monitoramento Remoto — VRM - Telemetria]] → [[Sensor de Nível Diesel]] → [[Sistema de Alarme Geral - Painel de Alarmes]]
> - **Automação física:** [[Automação de Bordo — Sistemas Domoticos]] → [[Atuador Linear]] → [[Câmeras de Bordo - Sistema CFTV]]
> - **Conforto e comunicação interna:** [[Som]] → [[TV a Bordo - Entretenimento]] → [[Interfone - Intercomunicador de Bordo]]

## Notas por categoria

### Controle e automação

- [[Automação de Bordo — Sistemas Domoticos]] — arquitetura de comandos, integração de cargas, cenas e supervisão.
- [[Atuador Linear]] — movimento elétrico controlado para escotilhas, mobiliário, tampas e mecanismos auxiliares.

### Alarmes e sensores

- [[Sistema de Alarme Geral - Painel de Alarmes]] — centralização de eventos críticos, sinalização local e lógica de resposta.
- [[Sensor de Nível Diesel]] — medição de combustível, calibração, ruído e integração com painel/telemetria.

### Telemetria e conectividade

- [[Monitoramento Remoto — VRM - Telemetria]] — leitura remota de energia, baterias, inversores e histórico operacional.
- [[Starlink - Internet a Bordo]] — WAN por satélite, consumo elétrico, instalação e limites de uso marítimo.
- [[Wi-Fi a Bordo — Roteador Marine e Conectividade]] — LAN interna, roteamento, cobertura e separação entre internet e rede local.

### Segurança eletrônica e comunicação interna

- [[Câmeras de Bordo - Sistema CFTV]] — visibilidade de áreas técnicas, convés, porão e monitoramento remoto.
- [[Interfone - Intercomunicador de Bordo]] — comunicação interna entre comando, praça de máquinas e cabines.

### Entretenimento e alimentação leve

- [[Som]] — áudio a bordo, amplificadores, ruído, consumo e proteção.
- [[TV a Bordo - Entretenimento]] — displays, antenas, fontes e integração com rede.
- [[USB 12V (Power)]] — pontos de carga, conversores DC-DC, ruído e queda de tensão.

## Cross-domain links

| Necessidade | Vá para |
|---|---|
| Energia para roteador, Starlink, câmeras e telas | [[MOC — Energia e Conversao]] |
| Fusível, barramento, chave e cabo dos circuitos auxiliares | [[MOC — Distribuicao Protecao e Aterramento]] |
| Banco e autonomia de cargas always-on | [[MOC — Baterias e Armazenamento]] |
| Alarmes de porão, gás, CO e incêndio | [[MOC — Segurança Integrada]] |
| Instrumentos NMEA, MFD, AIS e VHF | [[MOC — Navegacao Instrumentacao e Comunicacao]] |

## Quick-reference — top 6 dúvidas

1. **Starlink substitui rede Wi-Fi?** Não. Starlink é WAN; o barco ainda precisa de LAN/roteador.
2. **VRM resolve automação?** Não. VRM monitora e registra; automação exige lógica de comando e proteção local.
3. **USB 12V pode sair direto do barramento?** Deve passar por conversor/proteção adequada e considerar queda e ruído.
4. **Câmera sempre ligada descarrega banco?** Sim, se não houver cálculo de consumo e estratégia de standby.
5. **Sensor de nível diesel é plug-and-play?** Raramente. Geometria do tanque e calibração mandam no resultado.
6. **Automação deve comandar carga crítica?** Só com fallback manual e lógica fail-safe.

## Glossário rápido

- **WAN:** conexão externa com a internet.
- **LAN:** rede interna do barco.
- **VRM:** plataforma de monitoramento remoto, comum em ecossistema Victron.
- **CFTV:** circuito fechado de TV.
- **Gateway:** ponte entre protocolos ou redes.
- **Fail-safe:** estado seguro em caso de falha.
- **Always-on:** carga energizada mesmo com chave geral desligada.
- **DC-DC:** conversor de tensão contínua.

## Quando NÃO entrar aqui

- Dimensionamento de inversor, gerador, solar ou shore-power → [[MOC — Energia e Conversao]]
- Barramento, fusível, disjuntor ou queda de tensão → [[MOC — Distribuicao Protecao e Aterramento]]
- AIS, VHF, NMEA e piloto automático → [[MOC — Navegacao Instrumentacao e Comunicacao]]
- Detector de CO, GLP, alagamento e incêndio → [[MOC — Segurança Integrada]]

## Perguntas que esta página responde

- Como organizar automação sem virar gambiarra digital?
- Como separar internet, rede local, telemetria e entretenimento?
- Quais cargas devem ser monitoradas remotamente?
- Que notas ler antes de instalar Starlink ou VRM?
- Como evitar que eletrônica auxiliar drene o banco?
