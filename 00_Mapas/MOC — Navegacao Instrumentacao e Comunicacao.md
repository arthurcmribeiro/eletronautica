---
title: "MOC — Navegacao Instrumentacao e Comunicacao"
note_type: "moc"
domain: "50_Navegacao_Instrumentacao_e_Comunicacao"
status: "moc-curated-plus"
fase_6_reescrita: 141
reviewed_on: "2026-04-29"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
review_level: "moc-curated-plus"
aliases:
  - "MOC Navegacao"
  - "Hub navegacao instrumentacao comunicacao"
seo_title: "MOC Navegação Náutica: MFD, NMEA, AIS, VHF, radar, piloto automático, sonda e sensores"
seo_description: "Hub do domínio 50 para eletrônica de navegação, instrumentação e comunicação: chartplotter, NMEA 2000/0183, radar, AIS, VHF/DSC, EPIRB, MOB, piloto automático, bússola eletrônica, sonda, vento e buzina."
seo_keywords:
  - "NMEA 2000"
  - "chartplotter MFD"
  - "AIS VHF DSC"
  - "piloto automático náutico"
  - "radar e sonda"
geo_queries:
  - "Como montar rede NMEA 2000 no barco?"
  - "AIS precisa conversar com VHF e chartplotter?"
  - "Radar, sonda e GPS entram em qual arquitetura?"
  - "Como diagnosticar piloto automático caçando?"
  - "Que eletrônica é crítica para navegação segura?"
normas_citadas: []
related_notes:
  - "Atlas Técnico"
  - "MOC — Automacao Conectividade e Monitoramento"
  - "MOC — Energia e Conversao"
  - "MOC — Segurança Integrada"
---

# MOC — Navegacao Instrumentacao e Comunicacao

> [!abstract] Sobre este domínio
> Este domínio organiza a eletrônica que permite navegar, comunicar, localizar, medir e reagir em emergência. Ele cobre sensores, displays, redes de dados, rádio, balizas e sistemas de auxílio à decisão. **Venha aqui** para mapear arquitetura de navegação, resolver integração NMEA, priorizar equipamentos de segurança ou diagnosticar ruído/intermitência em instrumentos.

> [!tip] Trilhas de leitura
> - **Arquitetura base:** [[NMEA 2000 - NMEA 0183 — Rede de Instrumentos]] → [[Chartplotter - GPS - MFD]] → [[Bússola Eletrônica (Compass - HDG Sensor)]]
> - **Comunicação e emergência:** [[VHF]] → [[Dsc — Chamada Seletiva Digital]] → [[AIS (Automatic Identification System)]] → [[EPIRB - Beacon de Emergência]]
> - **Sensores de navegação:** [[Radar]] → [[Sonda - Profundímetro - Sonar]] → [[Estação de Vento - Anemômetro]]
> - **Controle e resposta:** [[Piloto Automático]] → [[Mob — Man Overboard — Sistema de Detecção]] → [[Buzina]]

## Notas por categoria

### Rede, display e referência de navegação

- [[NMEA 2000 - NMEA 0183 — Rede de Instrumentos]] — backbone, drops, gateways e falhas de comunicação.
- [[Chartplotter - GPS - MFD]] — display multifunção, cartas, sensores integrados e alarmes.
- [[Bússola Eletrônica (Compass - HDG Sensor)]] — heading, calibração, interferência magnética e referência do piloto.
- [[NAVEGAÇÃO (BB, BE e Alcançado)]] — linguagem operacional de bordo e orientação espacial.

### Comunicação e socorro

- [[VHF]] — rádio marítimo, instalação, alimentação, antena e alcance real.
- [[Dsc — Chamada Seletiva Digital]] — chamada seletiva, MMSI e integração com GNSS.
- [[AIS (Automatic Identification System)]] — transponder/receptor, integração com MFD e consciência situacional.
- [[EPIRB - Beacon de Emergência]] — baliza de emergência, registro e uso correto.
- [[Mob — Man Overboard — Sistema de Detecção]] — homem ao mar, alarme e integração com navegação.

### Sensores e percepção externa

- [[Radar]] — detecção, consumo, instalação, zonas de sombra e interpretação.
- [[Sonda - Profundímetro - Sonar]] — profundidade, transdutor, interferência e leitura de fundo.
- [[Estação de Vento - Anemômetro]] — vento aparente/real, masthead, calibração e rede.

### Controle e sinalização

- [[Piloto Automático]] — unidade de controle, sensor de heading, atuador e falhas típicas.
- [[Buzina]] — sinalização sonora, alimentação e acionamento confiável.

## Cross-domain links

| Necessidade | Vá para |
|---|---|
| Alimentação estável para MFD, radar e VHF | [[MOC — Distribuicao Protecao e Aterramento]] |
| Banco, autonomia e cargas críticas | [[MOC — Baterias e Armazenamento]] |
| Starlink, Wi-Fi, câmeras e VRM | [[MOC — Automacao Conectividade e Monitoramento]] |
| Luzes de navegação e sinalização noturna | [[MOC — Iluminacao e Sinalizacao]] |
| Segurança integrada e resposta a emergência | [[MOC — Segurança Integrada]] |

## Quick-reference — top 6 dúvidas

1. **NMEA 2000 é só cabo?** Não. Topologia, terminação, alimentação e LEN definem a confiabilidade.
2. **AIS precisa de GPS?** Sim, e a integração com MFD/VHF precisa ser verificada.
3. **Piloto automático caçando é sempre atuador?** Não. Heading, alimentação, calibração e interferência costumam vir antes.
4. **Radar pode compartilhar circuito com eletrônica leve?** Deve ser analisado por pico de consumo e ruído.
5. **DSC sem MMSI resolve emergência?** Fica muito limitado. Registro e programação importam.
6. **Sonda ruim é sempre transdutor?** Não. Instalação, bolhas, cabo, ruído e configuração podem dominar.

## Glossário rápido

- **MFD:** display multifunção.
- **GNSS:** sistema global de navegação por satélite.
- **MMSI:** identificação marítima usada por DSC/AIS.
- **LEN:** carga elétrica declarada em rede NMEA 2000.
- **Backbone/drop:** tronco e derivações da rede NMEA 2000.
- **Heading:** rumo da proa, diferente de curso sobre o fundo.
- **MOB:** man overboard, homem ao mar.

## Quando NÃO entrar aqui

- Internet, roteador, Starlink, VRM e CFTV → [[MOC — Automacao Conectividade e Monitoramento]]
- Luz de tope, âncora, cortesia e emergência → [[MOC — Iluminacao e Sinalizacao]]
- Dimensionamento de cabo/fusível/disjuntor da eletrônica → [[MOC — Distribuicao Protecao e Aterramento]]
- Procedimento geral de troubleshooting → [[MOC — Trilha do Diagnosticador]]

## Perguntas que esta página responde

- Em que ordem estruturar a eletrônica de navegação?
- O que entra em NMEA 2000 e o que pode ficar isolado?
- Como separar comunicação, emergência e instrumentação?
- Que notas ler antes de diagnosticar piloto automático, radar ou sonda?
- Como conectar navegação com segurança integrada?
