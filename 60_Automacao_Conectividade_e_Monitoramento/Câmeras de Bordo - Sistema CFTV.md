---
title: "Câmeras de Bordo / Sistema CFTV"
note_type: "system"
domain: "60_Automacao_Conectividade_e_Monitoramento"
source_file: "CÂMERAS DE BORDO SISTEMA CFTV 33a19734f7fb813ebf9ece9616f73405.md"
status: "tier-b-curated"
fase_6_reescrita: 123
reviewed_on: "2026-04-26"
review_jurisdiction: "Brasil + Internacional"
review_level: "tier-b-curated"
normas_citadas:
  - "ABYC E-11 (AC and DC Electrical Systems on Boats)"
  - "ABYC TE-30 (Electronic Equipment Installation)"
  - "IEC 60945 (Maritime navigation equipment)"
  - "IEC 60529 (IP)"
  - "IEC 61010-1 (Safety of measurement equipment)"
  - "IEC 62676-1/-2 (Video surveillance systems)"
  - "ONVIF (Open Network Video Interface Forum)"
  - "ABNT NBR 14728"
  - "LGPD Lei 13.709/2018 (Brasil — privacidade gravação)"
  - "GDPR (UE — privacidade)"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://www.nmea.org/standards.html"
  - "https://www.nmea.org/nmea-0400.html"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "CÂMERAS DE BORDO SISTEMA CFTV"
  - "CÂMERAS DE BORDO / SISTEMA CFTV"
seo_title: "Câmeras de Bordo / Sistema CFTV"
seo_description: "CAMERAS DE BORDO — Sistema de monitoramento visual para manobra, seguranca e vigilancia. A escolha correta depende da funcao: camera de re, camera IP, gravacao e acesso remoto nao sao a mesma coisa."
seo_keywords:
  - "Câmeras"
  - "CFTV"
  - "60 Automacao Conectividade e Monitoramento"
geo_queries:
  - "O que e Câmeras de Bordo / Sistema CFTV em instalacoes eletricas nauticas?"
  - "Qual e a funcao de Câmeras de Bordo / Sistema CFTV na embarcacao?"
related_notes:
  - "Atuador Linear"
  - "Automação de Bordo — Sistemas Domoticos"
  - "Interfone / Intercomunicador de Bordo"
  - "Monitoramento Remoto — VRM / Telemetria"
  - "Sensor de Nível Diesel"
  - "Sistema de Alarme Geral / Painel de Alarmes"
  - "Som"
  - "Starlink / Internet a Bordo"
---

# Câmeras de Bordo / Sistema CFTV

> [!abstract] Resumo técnico
> CÂMERAS DE BORDO — Sistema de monitoramento visual para manobra, segurança e vigilância. A escolha correta depende da função: câmera de ré, câmera IP, gravação contínua e acesso remoto não são a mesma coisa e não devem ser projetados como se fossem.

> [!tldr] TL;DR — 4 regras
> 1. **Diferenciar função:** câmera de ré (ManobrAuto, baixa latência, tela do MFD) ≠ câmera IP de vigilância (gravação NVR/cloud, ONVIF, alta resolução) ≠ térmica/FLIR (M-Series).
> 2. **IP67+ obrigatório** em câmera externa — IEC 60529. Câmera residencial IP44 falha em 6-12 meses.
> 3. **Privacidade regulada** — LGPD Lei 13.709/2018 (BR) + GDPR (UE) em embarcação charter / comercial: aviso visível + retenção limitada + acesso restrito.
> 4. **Integração com MFD** (Garmin OneHelm, Raymarine LightHouse, Furuno NavNet) ou NVR dedicado (Hikvision, Dahua, Axis marine-grade).

> [!info] Glossário rápido
> - **CFTV:** Circuito Fechado de TV.
> - **NVR:** Network Video Recorder.
> - **DVR:** Digital Video Recorder.
> - **IP camera:** câmera de rede.
> - **ONVIF:** padrão de interoperabilidade.
> - **PoE:** Power over Ethernet (até 30W per IEEE 802.3at).
> - **FLIR:** câmera térmica infravermelha.
> - **MFD:** Multifunction Display.

## O que é

Sistema de monitoramento visual embarcado para diferentes objetivos:

- manobra;
- vigilância patrimonial;
- monitoramento de áreas técnicas;
- acesso remoto;
- registro de eventos.

O erro clássico é usar uma única solução para tudo. Em termos práticos, câmera para manobra e câmera para vigilância costumam ter requisitos bem diferentes.

## Função

- auxiliar manobras em espaços restritos;
- monitorar áreas críticas a bordo;
- registrar eventos de segurança;
- permitir consulta local ou remota quando houver infraestrutura de rede compatível.

## Fundamentos mínimos

**Câmera de manobra:** precisa de baixa latência e previsibilidade.

**Câmera IP / vigilância:** prioriza resolução, gravação, integração em rede e acesso remoto.

**Ambiente marinho:** IP, resistência UV, névoa salina, vibração, conectores e encaminhamento de cabo são parte do sistema, não detalhe.

**Rede local:** câmeras IP dependem da qualidade da LAN de bordo, não só da câmera.

## Arquiteturas comuns

**Manobra**

- câmera dedicada
- monitor ou integração ao MFD
- prioridade para latência baixa

**Vigilância**

- múltiplas câmeras
- NVR/DVR ou gravação local
- rede cabeada sempre que possível

**Acesso remoto**

- depende de rede local robusta
- depende de conectividade externa
- exige política mínima de segurança digital

## Onde costuma dar problema

| Problema | Causa provável |
| --- | --- |
| latência ruim em manobra | solução IP inadequada para uso crítico |
| imagem com ruído ou queda | conectores/cabos ruins, corrosão, alimentação instável |
| câmera externa morre cedo | IP irreal, instalação ruim, produto não marinizado |
| acesso remoto falha | problema de rede local ou WAN, não necessariamente da câmera |
| gravação não serve quando precisa | retenção, armazenamento ou posicionamento mal definidos |

## Diagnóstico prático

1. Confirmar a função da câmera antes de diagnosticar o sistema.
2. Verificar alimentação no ponto de consumo.
3. Conferir integridade de cabos, conectores e passagens.
4. Separar problema óptico, de transporte de vídeo, de rede e de gravação.
5. Validar latência real quando a função for manobra.

## Boas práticas

- separar projeto de câmera de manobra do projeto de vigilância;
- preferir cabeamento robusto e documentado;
- proteger conectores e passagens contra umidade;
- prever manutenção de lente, posição e armazenamento;
- tratar credenciais e acesso remoto como tema de segurança, não só de conveniência.

## Erros comuns

- usar câmera com latência perceptível para manobra crítica;
- instalar produto indoor em ambiente externo marítimo;
- depender só de Wi-Fi onde cabear seria muito melhor;
- esquecer retenção e gestão de gravação;
- deixar câmeras expostas em rede sem política mínima de acesso.

## Relação com outros sistemas

- **Wi-Fi a Bordo** — suporte de LAN quando houver câmeras IP.
- **Starlink / Internet** — acesso remoto e upload de eventos.
- **Sistema de alarme** — integração por eventos e gatilhos.
- **Monitoramento remoto** — supervisão combinada com telemetria.

## Normas e referências

- **IEC 60529** — proteção IP.
- **Boas práticas de cabeamento e instalação elétrica** — proteção, alimentação e encaminhamento.
- **Requisitos legais de gravação e privacidade** — conforme a jurisdição e o uso.

## FAQ

**Câmera IP serve para ré?**

Pode até funcionar em alguns cenários, mas para manobra crítica a latência precisa ser avaliada com muito cuidado.

**Wi-Fi resolve tudo?**

Não. Em muitos barcos, rede cabeada continua sendo a solução mais confiável.

**Toda embarcação precisa de CFTV?**

Não como regra universal. A necessidade depende do perfil de uso, risco patrimonial, manobra e operação.

## Integração com outras notas

- [[Atuador Linear]]
- [[Automação de Bordo — Sistemas Domoticos]]
- [[Interfone / Intercomunicador de Bordo]]
- [[Monitoramento Remoto — VRM / Telemetria]]
- [[Sensor de Nível Diesel]]
- [[Sistema de Alarme Geral / Painel de Alarmes]]
- [[Som]]
- [[Starlink / Internet a Bordo]]

## Perguntas que esta nota responde

- O que é Câmeras de Bordo / Sistema CFTV em instalações elétricas náuticas?
- Qual é a função de Câmeras de Bordo / Sistema CFTV na embarcação?
