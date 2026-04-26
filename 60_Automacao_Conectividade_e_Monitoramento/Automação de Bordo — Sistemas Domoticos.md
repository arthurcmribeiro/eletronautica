---
title: "Automação de Bordo — Sistemas Domoticos"
note_type: "system"
domain: "60_Automacao_Conectividade_e_Monitoramento"
source_file: "AUTOMAÇÃO DE BORDO — SISTEMAS DOMOTICOS 33a19734f7fb81b99e7fcd10258cd8f3.md"
status: "premium-l3"
fase_6_reescrita: 92
reviewed_on: "2026-04-26"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://www.nmea.org/standards.html"
  - "https://webstore.iec.ch/publication/2697"
  - "https://www.czone.net/"
  - "https://www.empirbus.com/"
review_level: "engineering-curated"
aliases:
  - "AUTOMAÇÃO DE BORDO — SISTEMAS DOMOTICOS"
  - "Marine automation"
  - "Boat automation"
  - "Digital switching marine"
  - "Sistema integrado de bordo"
  - "Boat control system"
  - "Yacht automation"
  - "Smart boat"
seo_title: "Automação de bordo náutica: digital switching CZone/EmpirBus/Garmin OneHelm, NMEA 2000, IEC 61162, fail-safe"
seo_description: "Guia técnico premium da automação de bordo (sistema domótico náutico): arquiteturas (digital switching CZone, EmpirBus NG2, Garmin OneHelm, Lumitec POCO), integração NMEA 2000 (IEC 61162-3) + Ethernet OneNet (IEC 61162-450), princípios fail-safe, override manual, segurança ISO 13849-1, ABYC E-11/TE-30, scenes, monitoring (BMS/tank/temp), fabricantes, riscos."
seo_keywords:
  - "automação náutica"
  - "marine automation"
  - "digital switching"
  - "CZone Touch 5"
  - "EmpirBus NG2"
  - "Garmin OneHelm"
  - "Lumitec POCO"
  - "Domotics marine"
  - "NMEA 2000 backbone"
  - "fail-safe override"
  - "scene control yacht"
  - "smart boat system"
geo_queries:
  - "Vale a pena instalar digital switching no barco?"
  - "CZone vs EmpirBus vs Garmin OneHelm — qual escolher?"
  - "Como funciona scene em automação náutica?"
  - "Override manual é obrigatório em automação?"
  - "Como integrar iluminação + bombas + climatização?"
  - "Smart home Alexa funciona em barco?"
  - "Falha de software no digital switching: como recuperar?"
  - "Quanto custa automação completa em yacht 50 ft?"
  - "Cabos NMEA 2000 vs Ethernet OneNet — qual escolher?"
  - "Touchscreen ou app — qual interface preferir?"
normas_citadas:
  - "ABYC E-11 (AC and DC Electrical Systems on Boats)"
  - "ABYC TE-30 (Electronic Equipment Installation Standards)"
  - "ABYC TE-04 (Lightning Protection)"
  - "ABYC A-30 (Cabin Illumination)"
  - "ABYC E-30 (Electric Reset System) — referência"
  - "IEC 60945 (Maritime navigation equipment)"
  - "IEC 61162-1 (NMEA 0183)"
  - "IEC 61162-3 (NMEA 2000)"
  - "IEC 61162-450 (NMEA OneNet — Ethernet)"
  - "IEC 60204-1 (Safety of machinery — Electrical)"
  - "IEC 60529 (IP)"
  - "IEC 61000-6-1/-3 (EMC)"
  - "IEC 62471 (Photobiological)"
  - "IEC 62443 (Industrial cybersecurity)"
  - "ISO 12100 (Safety of machinery)"
  - "ISO 13849-1 (Safety-related parts of control systems)"
  - "ISO 26262 (Automotive functional safety — referência)"
  - "ISO 14971 (Risk management — princípio aplicável)"
  - "USCG NVIC 7-04 (referência cruzada)"
  - "EU Directive 2014/30/EU (EMC)"
  - "EU Directive 2014/35/EU (LVD)"
  - "EU Directive 2014/90/EU (Marine Equipment Directive)"
  - "EU 2013/53/EU (Recreational Craft Directive)"
  - "EU 2006/42/EC (Machinery Directive)"
  - "EU GDPR 2016/679 (data privacy — telemetria/cloud)"
  - "ABNT NBR 14728"
  - "ABNT NBR 5410"
  - "ABNT NBR ISO 13849-1"
  - "DPC NORMAM-211/DPC"
  - "DPC NORMAM-201/DPC"
  - "DPC NORMAM-05/DPC"
  - "ANATEL Resolução 715/2019 (RF + Bluetooth + Wi-Fi)"
  - "Manual técnico CZone (Power Products): Touch 5, Touch 7, Touch 10, COI, MIPS modules"
  - "Manual técnico EmpirBus NG / NG2 — system design guide"
  - "Manual técnico Garmin OneHelm + OneCan modules"
  - "Manual técnico Lumitec POCO Lighting Control"
  - "Manual técnico Maretron N2KView + DCM100/DSM monitoring"
  - "Manual técnico Yacht Devices (YDxxx series)"
  - "Manual técnico Mastervolt CZone integration"
  - "Manual técnico Victron VRM / Cerbo GX (referência cruzada)"
  - "Manual técnico Home Assistant + N2K bridge (open-source)"
related_notes:
  - "Atuador Linear"
  - "Sensor de Nível Diesel"
  - "Sistema de Alarme Geral - Painel de Alarmes"
  - "Câmeras de Bordo - Sistema CFTV"
  - "Interfone - Intercomunicador de Bordo"
  - "Monitoramento Remoto — VRM - Telemetria"
  - "Wi-Fi a Bordo — Roteador Marine e Conectividade"
  - "NMEA 2000 - NMEA 0183 — Rede de Instrumentos"
  - "Chartplotter - GPS - MFD"
  - "Dimmer — Controle de Intensidade Luminosa"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
  - "BMS — Battery Management System"
  - "Bonding — Sistema de Interligação de Massas"
  - "Cabeamento Náutico"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Disjuntores (DC) e (AC)"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
---

# Automação de Bordo — Sistemas Domoticos

> [!abstract] Resumo técnico
> A **automação de bordo (marine automation / digital switching / boat domotics)** é a integração de **sensores + lógica de controle + atuação + interface humana** para operar sistemas elétricos da embarcação de forma centralizada, programável e contextualizada. **Não é "smart home transposto para barco"** — em ambiente marine, princípios distintos prevalecem: **fail-safe (falha leva a estado seguro), override manual obrigatório (chave/botão físico para cada função crítica), redundância em sistemas de segurança (luzes de navegação, bombas de porão, alarmes), EMC robusta (IEC 61547 + IEC 60945), arquitetura distribuída (sem ponto único de falha)**. Padrões de transporte: **NMEA 2000 (IEC 61162-3)** como backbone consolidado + **Ethernet OneNet (IEC 61162-450)** como evolução. Padrões de segurança: **ISO 13849-1** (PL "c" mínimo em risco a pessoa), **IEC 60204-1** (safety of machinery). Quatro arquiteturas dominantes: **digital switching dedicado** (CZone, EmpirBus NG2, Garmin OneHelm — ABYC E-11 compatible), **lighting-first** (Lumitec POCO, Lumishore Lumix), **monitoring + alerts** (Maretron N2KView, Victron VRM/Cerbo GX), **DIY open-source** (Home Assistant + N2K bridge — yacht-specific). **Cybersecurity** emerge como tópico crítico (IEC 62443) — sistemas conectados a internet via Wi-Fi/cellular precisam de proteção. Escopo apropriado: **iluminação + climatização + bombas + tank monitoring + scenes + alarmes**; escopo proibido sem redundância: **luzes de navegação obrigatórias, bombas de porão de emergência, comandos de propulsão**.

> [!tldr] TL;DR — 10 regras inegociáveis
> 1. **Override manual obrigatório em todas as funções críticas.** Botão físico / chave que ignore o sistema digital. Falha de software / firmware → tripulação precisa controlar localmente. ISO 13849-1.
> 2. **Fail-safe é princípio nuclear:** falha do sistema deve levar a estado seguro (luz acesa, bomba ligada se for emergência, alarme ativo) — não a estado desligado em sistema crítico.
> 3. **Redundância em sistemas de segurança:** luzes de navegação (vide [[NAVEGAÇÃO (BB, BE e Alcançado)]]) NÃO devem depender exclusivamente de digital switching; bomba de porão (vide [[Bomba de Porão]]) idem; alarme de água idem.
> 4. **NMEA 2000 backbone com terminadores 120 Ω** em ambos extremos (IEC 61162-3) — sem isso, rede falha intermitentemente. Padrões: Mid-C ou Micro-C, drop ≤ 6 m, backbone ≤ 200 m, ≤ 50 nós.
> 5. **EMC certificada** (IEC 61547 + IEC 60945 + EU 2014/30/EU) em TODOS os módulos — equipamento sem certificação pode poluir VHF/GPS/AIS.
> 6. **Cybersecurity** (IEC 62443) — sistema conectado a Wi-Fi/cellular precisa de senha forte + atualização regular + rede separada de tripulação/convidados.
> 7. **Backup de configuração** + **firmware update planejado** — antes de viagem longa, atualizar TODOS os módulos + exportar config para cartão SD/cloud.
> 8. **Documentação operacional A BORDO** (impressa + digital): mapas de rede, módulos, endereços, scenes, override manual de cada função. Tripulação treinada antes de viagem.
> 9. **Surge protection** em entrada AC/cabos longos NMEA 2000 (ABYC TE-04). Relâmpago no mastro queima toda a rede simultaneamente sem proteção.
> 10. **Dimensionar margens generosas** em cargas (módulos de saída) — corrente nominal × 1,3-1,5 evitando overload em pico (motor partida, lâmpada incandescente residual).

> [!danger] Cenários de risco
> - **Falha total do sistema digital em offshore noturno:** firmware corrompido + sem override manual → todas as luzes apagam + bomba de porão off + alarme silencioso → emergência sem detecção → grounding ou alagamento. **Caso histórico:** múltiplos casos USCG documentados de yachts com automação proprietária de geração 1. **Prevenção:** override manual obrigatório por função crítica; redundância de circuitos de segurança; teste mensal de override.
> - **Surto atmosférico via NMEA 2000 destrói rede inteira:** raio próximo + cabo longo do MFD ao salão sem surge protection → todos módulos queimam simultaneamente → barco "desliga" totalmente em mar agitado. **Prevenção:** ABYC TE-04 surge protectors em pontos chave; bonding mastro-quilha; backup desconectável (chave de bypass).
> - **Cybersecurity breach via Wi-Fi marine** (yacht charter / luxury): atacante remoto desliga sistemas de bordo durante operação → ransomware → custo elevado de recuperação + perda de dados. **Prevenção:** rede de tripulação separada de convidados; senha forte; firmware atualizado; sistema crítico OFFLINE (não-internet).
> - **EMC severo de módulos de baixa qualidade:** instalação misturando CZone certificado + módulo chinês EMC pobre → harmonics inutilizam VHF/GPS/AIS. **Prevenção:** exclusivamente módulos certificados (CZone, EmpirBus, Lumitec, Maretron, Yacht Devices, Victron).
> - **Falha de scene em manobra crítica:** scene "manobra" com dimmer cockpit + bomba ar-condicionado off + luzes de cortesia high → falha de execução → cockpit escuro em ancoragem. **Prevenção:** override manual; teste de cada scene mensalmente; backup de config.
> - **Endereçamento NMEA 2000 conflitante** após adicionar módulos novos: dois módulos com mesmo address → bus errático → todos os instrumentos pulsam. **Prevenção:** documentar endereços; usar tools (Maretron N2KMeter, Actisense NMEA Reader); re-comissionar bus após adição.
> - **Module de saída queima por sobrecarga:** dimensionou módulo CZone Touch para iluminação 10A; motorista substituiu lâmpadas por incandescente alta potência → 15A → módulo abre fusível interno. **Prevenção:** dimensionar com margem; treinar instalador para checar antes de mudanças.
> - **Override manual desligado por engano** (chave em "auto" sem fallback): tripulante novo aciona override pensando que é desliga → função crítica fica em modo digital sem manual → emergência sem ação local. **Prevenção:** sinalização clara; treinamento; chave de override com posição de bloqueio.
> - **Confiança excessiva em monitoring remoto** (charter — owner monitora a distância): notificação não chega por falha de Wi-Fi/cellular → emergência sem resposta. **Prevenção:** monitoring é complemento, não substituto; capitão local sempre.
> - **Scene "harbor mode" desligando bomba de porão por engano** durante chuva torrencial: lógica errada na config → barco alaga. **Prevenção:** bomba de porão SEMPRE em circuito separado, NUNCA controlada por digital switching exclusivamente; ABYC H-22.

## O que é (definição rigorosa)

A **automação de bordo** integra:

```
[Sensores]──┬──[Tank levels (vide [[Sensor de Nível Diesel]])]
            ├──[Battery (vide [[BMS — Battery Management System]])]
            ├──[Temperature / RH (cabines, motor, baterias)]
            ├──[Flood / bilge water (alarme alagamento)]
            ├──[Door / hatch open]
            ├──[Engine RPM / fuel flow]
            └──[GPS / heading / wind]
                        │
                ┌───────┴───────────────────────────────────────────┐
                │   LÓGICA DE CONTROLE (Digital Switching CPU)        │
                │   - Scenes (cruising, harbor, sleep, emergency)     │
                │   - Conditional rules (if-then-else)                │
                │   - Time-based (sunset, sunrise)                    │
                │   - Geofence (chegou na marina → cena harbor)       │
                └───────┬───────────────────────────────────────────┘
                        │
[Atuação]───┬──[Lighting (dimmable + scene)]
            ├──[Climate (AC ON/OFF + setpoint)]
            ├──[Bombas (FW pressurizada, banheiro)]
            ├──[Atuadores lineares (escotilha, capota)]
            ├──[Comutação AC/DC (chave seletora)]
            └──[Alertas (display + buzzer + SMS / push)]
                        │
                [Interface humana]
                        │
                ┌───────┴───────┐
                │               │
        [Touchscreen]   [App / smartphone / tablet]
        [MFD chartplotter]  [Voice (Alexa, Google, Siri)]
        [Botões físicos]    [Telemetria remota]
```

### Quatro arquiteturas dominantes

#### 1. Digital switching dedicado

- **CZone (Power Products / Mastervolt):** referência marine; touchscreens (Touch 5/7/10) + módulos COI (Combination Output Input) + MIPS (Multi-Input Power Switching) + integração com MFD (Garmin/Simrad/Raymarine).
- **EmpirBus NG / NG2:** concorrente premium europeu; design modular.
- **Garmin OneHelm / OneCan:** integração Garmin GPSMAP.

#### 2. Lighting-first

- **Lumitec POCO:** controle proprietário Bluetooth para iluminação Lumitec.
- **Lumishore Lumix:** equivalente para iluminação Lumishore.

#### 3. Monitoring + alerts (não substitui digital switching)

- **Maretron N2KView + DCM100/DSM:** monitoring NMEA 2000 + alertas.
- **Victron VRM / Cerbo GX:** monitoring de bateria/solar/inversor + integração simples (não digital switching completo).

#### 4. DIY open-source

- **Home Assistant + N2K bridge** (Yacht Devices YDNB-07, Actisense NGT-1) — flexibilidade total + cybersecurity própria; menos integração nativa.
- **OpenPlotter** / **SignalK** + Raspberry Pi.

## Comparação técnica entre arquiteturas

| Parâmetro | CZone | EmpirBus NG2 | Garmin OneHelm | Lumitec POCO | Home Assistant DIY |
|-----------|-------|---------------|-----------------|---------------|----------------------|
| **Maturidade** | Alta | Alta | Média (recente) | Limitada (lighting) | Alta (geral) |
| **Integração MFD** | Sim (multi-marca) | Sim (multi-marca) | Garmin only | NMEA 2000 | Variável |
| **Override manual** | Sim (módulos) | Sim | Sim | Sim | Customizável |
| **Cabling** | NMEA 2000 + Ethernet | NMEA 2000 + Ethernet | NMEA 2000 + OneNet | NMEA 2000 / Bluetooth | NMEA 2000 + Ethernet + Wi-Fi |
| **Custo install yacht 50 ft** | R$ 35.000-80.000 | R$ 50.000-120.000 | R$ 25.000-60.000 | R$ 5.000-15.000 (lighting only) | R$ 8.000-25.000 (DIY) |
| **Cybersecurity** | Boa (LAN local) | Boa | Boa | N/A | Variável |
| **Suporte BR** | Distribuidor | Limitado (importação) | Garmin BR | Limitado | Comunidade |
| **Scenes** | Sim (avançado) | Sim (avançado) | Sim | Sim (lighting) | Customizável |
| **App + cloud** | Yes (Mastervolt CZone Connect) | Yes | Garmin ActiveCaptain | Lumitec POCO app | Customizável |

## Onde se encaixa na arquitetura elétrica

```
[Bateria (banco serviço)] → [Disjuntor principal] → [DC Bus]
                                                          │
                            ┌─────────────────────────────┴─┐
                            │                               │
                  [Quadro tradicional]              [Digital switching CPU]
                  (chaves físicas)                        │
                                                  ┌───────┴───────────┐
                                                  │                   │
                                          [Output modules]    [Input modules]
                                          (cargas)              (sensores)
                                                  │
                                          [Override manual local]
                                                  │
                                          [Cargas com fail-safe]
```

## Fabricantes e modelos dominantes

### CZone (Power Products / BEP)

- **Touch 5 / Touch 7 / Touch 10** — interfaces touchscreen 5"/7"/10".
- **COI module** — Combination Output Input.
- **MIPS** — Multi-Input Power Switching (até 16 saídas + 12 inputs).
- **Mastervolt CZone Connect** — app + cloud.

### EmpirBus

- **NG2 NXT** — sistema modular escalável.
- Design especialmente para mega-iates (Sunseeker, Princess, Azimut OEM).

### Garmin

- **OneHelm + OneCan modules** — integração nativa GPSMAP.
- **OneCan I/O modules** — controle de cargas.

### Lumitec

- **POCO 2 / POCO 3** — controle proprietário Bluetooth.
- Foco em iluminação Lumitec mas extensível.

### Maretron

- **N2KView** — visualização + alertas.
- **DCM100** — monitor DC.
- **DSM150 / DSM250 / DSM410** — multi-display.

### Victron

- **Cerbo GX + Touch 50/70** — monitoring + integração.
- **VRM cloud** — telemetria remota.

### Yacht Devices

- **YDNB-07 / YDEN / YDxxx** — interfaces NMEA 2000 ↔ NMEA 0183 / Ethernet / WiFi.

### Home Assistant + N2K bridge

- DIY open-source.

## Princípios de design (fail-safe + override)

### Princípio 1 — Override manual

**Toda função crítica deve ter botão/chave físico que ignora o sistema digital.**

Exemplos:
- Luzes de navegação: chave física dedicada que conecta diretamente bateria → luzes (bypass do digital switching).
- Bomba de porão automática: separada do digital switching, ligação direta à bateria com float switch.
- Alarme de alta água: separado, com bateria interna.

### Princípio 2 — Fail-safe

**Falha do sistema → estado seguro:**
- Luz: ON em emergência.
- Bomba de porão: ON em alta água.
- Climatização: OFF (não risco).
- Bomba água pressurizada: OFF (não risco).

### Princípio 3 — Redundância

Funções de segurança duplicadas:
- Luzes de tope: bombas instaladas + circuito alternativo manual.
- Bomba de porão: principal + backup + alarme.

### Princípio 4 — Confidencialidade / Cybersecurity

- Senha forte + atualização firmware regular.
- Rede de tripulação separada de convidados.
- Sistema crítico OFFLINE (não conectado à internet).

## Falhas comuns

| Falha | Causa | Solução |
|-------|-------|---------|
| Sistema todo "trava" | Firmware corrompido | Restart + restaurar config backup |
| EMC no VHF | Módulo não-certificado | Substituir certificado |
| Module de saída queima | Sobrecarga | Dimensionar com margem |
| NMEA 2000 errático | Terminador faltando | 60 Ω entre CAN-H e CAN-L |
| Cybersecurity breach | Wi-Fi sem senha forte | Atualizar; rede segregada |
| Override não funciona | Chave queimada / config errada | Trocar chave; verificar config |
| Notificação não chega | Wi-Fi/cellular off | Local primary + remote secondary |
| Scene errada | Lógica de programação ruim | Re-programar com testes |
| Surto queima módulos | Sem surge protection | ABYC TE-04 |

## Boas práticas

- **Override manual** mandatório em função crítica.
- **Documentação A BORDO** (papel + digital).
- **Treinamento** de tripulação.
- **Backup de config** + cartão SD.
- **Atualização de firmware** antes de viagem longa.
- **Teste mensal de scenes + override**.
- **Cybersecurity** atualizada.
- **Surge protection** em pontos chave.
- **Dimensionar com margem** (1,3-1,5×).
- **Rede separada** tripulação/convidados.

## Erros comuns

- "Smart home funciona em barco." → Falso. Ambiente marine + critical safety + EMC ≠ residencial.
- "Wi-Fi cobre tudo." → Falso. Wi-Fi marine não cobre offshore; sistema deve ser independente de internet em crítico.
- "Override é luxo." → Falso. ISO 13849-1 + ABYC requirement.
- "Mais sensores = melhor." → Falso. Sensores ruins inutilizam dados; melhor poucos confiáveis.
- "Atualização de firmware é arriscada." → Falso. Manter atualizado é segurança.

## Glossário

- **Domotics:** automação residencial / yacht.
- **Digital switching:** controle digital de cargas via NMEA 2000.
- **Scene:** cena pré-definida (cruising, harbor, sleep, emergency).
- **Override manual:** controle local que ignora digital.
- **Fail-safe:** estado seguro em falha.
- **Redundância:** duplicação de função crítica.
- **Cybersecurity:** segurança digital.
- **NMEA 2000:** padrão CAN-bus marine (IEC 61162-3).
- **NMEA OneNet:** Ethernet evolução (IEC 61162-450).
- **CZone / EmpirBus / Garmin OneHelm:** marcas digital switching.
- **Lumitec POCO:** controle Bluetooth lighting.
- **Maretron N2KView:** monitoring.
- **Victron VRM / Cerbo GX:** Victron ecosystem.
- **Yacht Devices:** interfaces.
- **Home Assistant:** open-source automation.
- **SignalK:** padrão open-source.
- **OpenPlotter:** distribuição RPi marine.
- **PL "c":** Performance Level ISO 13849-1.
- **EMC / EMI:** electromagnetic compatibility / interference.
- **Surge protection:** proteção surto (ABYC TE-04).
- **Bonding:** ABYC E-11.16.
- **GDPR:** privacidade dados (telemetria cloud).
- **IEC 62443:** cybersecurity industrial.
- **PGN:** Parameter Group Number (NMEA 2000).
- **MAC address:** identificador Ethernet.
- **DHCP / IP estático:** configuração rede.

## Integração com outras notas

- [[Atuador Linear]] — atuação mecânica.
- [[Sensor de Nível Diesel]] — input de tank.
- [[Sistema de Alarme Geral - Painel de Alarmes]] — output de alertas.
- [[Câmeras de Bordo - Sistema CFTV]] — monitoring video.
- [[Interfone - Intercomunicador de Bordo]] — comunicação interna.
- [[Monitoramento Remoto — VRM - Telemetria]] — telemetria remota.
- [[Wi-Fi a Bordo — Roteador Marine e Conectividade]] — backbone IP.
- [[NMEA 2000 - NMEA 0183 — Rede de Instrumentos]] — backbone CAN.
- [[Chartplotter - GPS - MFD]] — interface integrada.
- [[Dimmer — Controle de Intensidade Luminosa]] — controle de luz.
- [[Quadro Elétrico e Painel de Distribuição AC-DC]] — distribuição.
- [[BMS — Battery Management System]] — monitoring bateria.
- [[Bonding — Sistema de Interligação de Massas]] — aterramento.
- [[Cabeamento Náutico]] — cabos.
- [[Fusíveis DC — Proteção Contra Sobrecorrente]] / [[Disjuntores (DC) e (AC)]] — proteção.
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]] — diagnóstico.

## Perguntas que esta nota responde

- Vale a pena instalar digital switching no barco?
- CZone vs EmpirBus vs Garmin OneHelm — qual escolher?
- Como funciona scene em automação náutica?
- Override manual é obrigatório em automação?
- Como integrar iluminação + bombas + climatização?
- Smart home Alexa funciona em barco?
- Falha de software no digital switching: como recuperar?
- Quanto custa automação completa em yacht 50 ft?
- Cabos NMEA 2000 vs Ethernet OneNet — qual escolher?
- Touchscreen ou app — qual interface preferir?
