---
title: "Dimmer — Controle de Intensidade Luminosa"
note_type: "technical-note"
domain: "55_Iluminacao_e_Sinalizacao"
source_file: "DIMMER — CONTROLE DE INTENSIDADE LUMINOSA 33a19734f7fb810197b3d469666bb573.md"
status: "premium-l3"
fase_6_reescrita: 88
reviewed_on: "2026-04-25"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://webstore.iec.ch/publication/2697"
  - "https://www.lutron.com/en-US/Pages/default.aspx"
  - "https://www.lumitec.com/poco/"
review_level: "engineering-curated"
aliases:
  - "DIMMER — CONTROLE DE INTENSIDADE LUMINOSA"
  - "Dimmer marine"
  - "PWM dimmer"
  - "TRIAC dimmer"
  - "0-10V dimmer"
  - "DALI dimmer"
  - "DMX dimmer"
  - "Variador de luminosidade"
seo_title: "Dimmer marine: PWM × TRIAC × 0-10V × DALI × DMX, IEC 60669-2-1, ABYC E-11, compatibilidade LED, EMI"
seo_description: "Guia técnico premium do dimmer (controle de intensidade luminosa) em embarcações: tecnologias (PWM × TRIAC × 0-10V × DALI × DMX × Bluetooth Mesh), IEC 60669-2-1 / IEC 61347-2-13, compatibilidade LED dimável, frequência PWM × flicker, EMI / IEC 61547, fabricantes (Lutron Caseta, Lumitec POCO, Lumishore Lumix, Aqualuma), modes (continuous × scene × group), instalação ABYC E-11."
seo_keywords:
  - "dimmer náutico"
  - "PWM dimmer marine"
  - "LED dimmer"
  - "TRIAC dimmer LED"
  - "0-10V dimmer"
  - "DALI marine"
  - "DMX512"
  - "Lutron Caseta"
  - "Lumitec POCO"
  - "Bluetooth Mesh lighting"
  - "compatibilidade LED dimável"
  - "flicker LED"
  - "EMI dimmer"
geo_queries:
  - "Por que LED pisca com dimmer existente?"
  - "PWM ou TRIAC dimmer para LED em barco?"
  - "Como integrar dimmer ao sistema de automação?"
  - "Dimmer wireless Bluetooth funciona em ambiente marine?"
  - "Como evitar zumbido do dimmer com fita LED?"
  - "Frequência PWM ideal para evitar flicker?"
  - "Dimmer DALI vs DMX: qual usar em yacht?"
  - "Dimmer compatível com fita LED 12V — qual escolher?"
  - "Dimmer rotativo versus toque versus app: qual melhor?"
  - "Como dimensionar carga máxima do dimmer?"
normas_citadas:
  - "ABYC E-11 (AC and DC Electrical Systems on Boats)"
  - "ABYC A-30 (Cabin and Weather Deck Illumination)"
  - "IEC 60669-1 (Switches for household and similar fixed electrical installations)"
  - "IEC 60669-2-1 (Electronic switches — dimmer)"
  - "IEC 61347-2-13 (LED driver — DC/AC)"
  - "IEC 62386 (DALI — Digital Addressable Lighting Interface)"
  - "IEC 60598-1 (Luminaires — General)"
  - "IEC 60529 (IP)"
  - "IEC 61547 (EMC for lighting)"
  - "IEC 61000-3-2 (Harmonics)"
  - "IEC 61000-6-1/-3 (EMC)"
  - "ISO 11898 (CAN bus — referência cruzada para sistemas digitais)"
  - "USITT DMX512-A (DMX protocol)"
  - "ANSI E1.20 (RDM — Remote Device Management)"
  - "ANSI E1.11 / E1.20 (DMX/RDM USA)"
  - "UL 1472 (Solid-State Dimming Controls)"
  - "UL 8750 (LED equipment)"
  - "EU Directive 2014/35/EU (LVD)"
  - "EU Directive 2014/30/EU (EMC)"
  - "EU Regulation 2019/2020 (EcoDesign)"
  - "ABNT NBR 5410"
  - "ABNT NBR 14728"
  - "INMETRO Portaria 144/2015"
  - "ANATEL Resolução 715/2019"
  - "DPC NORMAM-211/DPC"
  - "DPC NORMAM-05/DPC"
  - "Manual técnico Lutron Caseta / Vive / RA2 Select"
  - "Manual técnico Lumitec POCO / Lighting Control System"
  - "Manual técnico Lumishore Lumix Sense / Eclipse"
  - "Manual técnico Aqualuma EZ-Connect"
  - "Manual técnico CZone (Power Products) — digital switching"
  - "Manual técnico EmpirBus NG / NG2 — digital switching"
  - "Manual técnico Garmin OneHelm / Empirbus integration"
  - "Manual técnico DMX512 controllers (Pathway Connectivity, ENTTEC)"
related_notes:
  - "Tipos de Lâmpadas e LEDs Náuticos"
  - "Fitas Led - Iluminação Led"
  - "Luz de Cortesia"
  - "Luzes Internas Teto"
  - "Iluminação de Emergência a Bordo"
  - "Automação de Bordo — Sistemas Domoticos"
  - "Bonding — Sistema de Interligação de Massas"
  - "Cabeamento Náutico"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
---

# Dimmer — Controle de Intensidade Luminosa

> [!abstract] Resumo técnico
> O **dimmer (controle de intensidade luminosa)** regula o **fluxo luminoso (lumens)** entregue à luminária, modulando a **potência elétrica** entregue ao emissor. Em iluminação náutica moderna **predomina LED**, e o dimmer LED não é trivial: **diferentes tecnologias de dimmer não são intercambiáveis** com diferentes tecnologias de driver LED. Cinco famílias dominantes: **PWM (Pulse Width Modulation — DC native, padrão em fitas LED 12V/24V)**, **TRIAC (corte de fase AC — padrão residencial 220V; em LED requer driver dimável TRIAC-compatible)**, **0-10V (sinal analógico de controle, padrão industrial)**, **DALI (IEC 62386 — digital addressable, scene/group/zone)**, **DMX512 (USITT — controle profissional iluminação cênica/RGB)** + **Bluetooth Mesh / Wi-Fi / proprietário** (Lutron Caseta, Lumitec POCO, CZone, EmpirBus). Falha #1 em barco: **LED não-dimável + dimmer existente = piscar / zumbido / queima**. Padrões: **IEC 60669-2-1** (dimmer eletrônico), **IEC 61347-2-13** (LED driver), **IEC 61547** (EMC), **ABYC E-11** (wiring), **ABYC A-30** (cabin illumination). Sistemas modernos integram dimmer ao **digital switching** (CZone, EmpirBus, Garmin OneHelm) — múltiplas zonas, scenes, integração NMEA 2000. Vide [[Tipos de Lâmpadas e LEDs Náuticos]] para fundamentos LED + [[Fitas Led - Iluminação Led]] para aplicação típica de PWM.

> [!tldr] TL;DR — 9 regras inegociáveis
> 1. **Compatibilidade dimmer-LED é a falha #1.** Etiqueta "dimmable" no LED + tipo de dimmer (TRIAC, 0-10V, PWM, DALI). Mismatch = pisca / zumbe / queima driver. Verificar TODAS as combinações antes de instalar.
> 2. **PWM em DC nativo é a solução mais simples e robusta** para fita LED 12V/24V em barco. Frequência ≥1 kHz para evitar flicker visível; ≥10 kHz para eliminar flicker em câmera.
> 3. **TRIAC dimmer + LED genérico NÃO-dimável = não funciona.** TRIAC corta a onda AC; LED sem driver compatível interpreta como tensão errada → piscar / queima. Trocar para LED dimmable + TRIAC compatível OU dimmer 0-10V.
> 4. **0-10V é padrão industrial** — separação de potência (12/24V para luminária) e sinal (0-10V em par dedicado). Driver LED com entrada 0-10V responde linear de 1-100%. Padrão em luminárias profissionais marine.
> 5. **DALI (IEC 62386)** permite endereçamento individual + scenes + grupos + dimming logarítmico (mais natural para o olho). **Cabo de 2 fios bidirecional** — instalação relativamente simples para sistemas grandes.
> 6. **DMX512** é overkill em residencial mas padrão em iluminação cênica + RGB + barcos com show lighting. Cada canal = 1 byte (0-255 níveis); até 512 canais por universo.
> 7. **EMI / flicker é problema comum** em PWM mal projetado — drivers chineses geram harmônicas que poluem VHF/GPS adjacente (vide [[Tipos de Lâmpadas e LEDs Náuticos]]). IEC 61547 + EU 2014/30/EU EMC + IEC 61000-6-3.
> 8. **Sistema digital switching** (CZone, EmpirBus, Garmin OneHelm, Lumitec POCO) — controle de iluminação + outras cargas via NMEA 2000 + app. Padrão emergente em yachts >40 ft.
> 9. **Dimensionamento da carga:** dimmer rated para corrente total. Fita 14,4 W/m × 5 m × 12V = 6 A → dimmer com rated ≥10A com 30% margem. Subdimensionado = queima.

> [!danger] Cenários de risco
> - **LED queima imediatamente ao ligar dimmer:** TRIAC dimmer existente em circuito que recebeu LED não-dimável → spike de tensão na partida → driver explode + faísca + risco de fogo. **Prevenção:** verificar etiqueta dimmable; testar com 1 LED antes de instalar todos.
> - **EMI severo do dimmer poluído mata VHF/GPS:** dimmer chinês PWM sem EMC + cabo paralelo a antena → GPS perde fix em manobra. **Prevenção:** dimmer certificado IEC 61547 + ferrite cores + cabo separado; Lutron / Lumitec / Lumishore / CZone / EmpirBus são EMC OK.
> - **Flicker visível em movimento da câmera** (charter, vídeo, vlog): PWM frequência <200 Hz → faixas pretas em vídeo. **Prevenção:** PWM ≥10 kHz para imagem profissional; LED com driver "flicker-free".
> - **Zumbido audível do dimmer/LED** em camarote noturno: TRIAC com LED genérico → ressonância 100/120 Hz audível. **Prevenção:** trocar para PWM ou 0-10V; substituir LED por dimmable verdadeiro.
> - **Falha de scene em emergência:** sistema digital switching com falha de software / firmware → todas as luzes apagam ou ficam fixas em modo errado. **Prevenção:** redundância — dimmer manual local + override mecânico; testes mensais; backup firmware.
> - **Curto em wireless dimmer com bateria descarregada:** Bluetooth dimmer com bateria CR2032 morta + módulo recebe gradualmente menos potência → comportamento errático → danifica driver LED. **Prevenção:** verificar bateria semestralmente; modelo com alimentação cabo + bateria backup.
> - **Instalação dimmer AC sem aterramento + ambiente molhado:** banheiro / cockpit + AC 220V sem ELCI → choque ao tocar painel. **Prevenção:** ELCI 30 mA; bonding; preferir dimmer DC quando possível.
> - **Sistema DALI com endereço duplicado:** dois dispositivos com mesmo endereço → conflito → comportamento aleatório. **Prevenção:** usar comissionamento DALI com software (DALI Commissioner); documentar endereços.
> - **Surto atmosférico via cabo de controle DMX/DALI** queima eletrônica de bordo: cabo longo (10+ m) sem proteção captura energia de relâmpago próximo. **Prevenção:** ABYC TE-04 surge protection em cada extremo; cabo blindado; bonding.
> - **Substituição de luminária dimável por não-dimável** sem trocar dimmer: nova luminária gerando harmônicas que dimmer não suporta → comportamento errático. **Prevenção:** documentar tipo de luminária; substituir conjunto.

## O que é (definição rigorosa)

O **dimmer** é o componente que regula a **potência elétrica** entregue à carga (luminária), permitindo controle do **fluxo luminoso emitido**. Em LED, a relação entre potência elétrica e fluxo é aproximadamente linear (com pequena curva logarítmica para conforto visual).

Cinco tecnologias dominam o mercado marine:

### 1. PWM (Pulse Width Modulation) — DC native

```
100%:  ████████████████████████████████
 75%:  ██████████░░░░██████████░░░░████
 50%:  ████░░░░████░░░░████░░░░████░░░░
 25%:  ██░░░░░░██░░░░░░██░░░░░░██░░░░░░
       Frequência típica 200 Hz a 20 kHz
```

- **Aplicação:** fita LED 12V/24V; LED com driver PWM-compatible.
- **Vantagens:** simples, eficiente, sem perda térmica em corte.
- **Desvantagens:** EMI se mal projetado; flicker se frequência <200 Hz.
- **Frequência ideal:** ≥1 kHz olho humano; ≥10 kHz câmera de vídeo.

### 2. TRIAC (Corte de Fase AC)

```
Onda senoidal AC: ──────╱╲────╱╲────╱╲──
Corte 50%:        ──────_╲────_╲────_╲──   (corte na parte negativa)
Corte 25%:        ──────___╲────___╲─────  (corte mais cedo)
```

- **Aplicação:** dimmer residencial 110/220V AC; LED dimmable TRIAC-compatible.
- **Vantagens:** tradicional, infraestrutura ampla.
- **Desvantagens:** EMI; harmônicas; LED genérico NÃO funciona (precisa driver compatível).

### 3. 0-10V (analógico industrial)

```
[Driver com entrada de controle 0-10V]
       │
       ├─ 0V: 0% intensidade (off)
       ├─ 1V: 1% intensidade (mínimo)
       ├─ 5V: 50% intensidade
       └─ 10V: 100% intensidade
```

- **Aplicação:** luminárias profissionais marine; estações industriais.
- **Vantagens:** padrão consolidado; baixa EMI; cabo dedicado.
- **Desvantagens:** mais cabos (potência + sinal).

### 4. DALI (Digital Addressable Lighting Interface — IEC 62386)

```
[Master controller] ── [Bus DALI 2 fios] ── [Drivers DALI individuais (até 64 endereços por bus)]
                                                  │
                                            [Cada driver = endereço único]
                                            [Scenes / grupos / dimming log.]
```

- **Aplicação:** sistemas grandes com múltiplas zonas.
- **Vantagens:** endereçamento individual; scenes; bidirecional.
- **Desvantagens:** complexidade; comissionamento.

### 5. DMX512 (USITT — controle cênico)

```
[DMX controller] ── [Cabo DMX 5-pin XLR] ── [Driver 1 → 4 → 64 → 512 canais]
                                                  │
                                            [Cada canal = 1 byte (0-255)]
                                            [RGB usa 3 canais; RGBW usa 4]
                                            [Universo = 512 canais]
```

- **Aplicação:** RGB/RGBW + show lighting + iluminação subaquática profissional.
- **Vantagens:** controle profissional; compatibilidade ampla.
- **Desvantagens:** overkill em sistemas pequenos; cabo blindado dedicado.

### 6. Wireless / proprietário (mercado moderno)

- **Lutron Caseta / Vive / RA2:** Bluetooth Mesh + Wi-Fi.
- **Lumitec POCO:** controle proprietário Bluetooth.
- **CZone (Power Products):** digital switching + NMEA 2000.
- **EmpirBus NG / NG2:** digital switching mais novo.
- **Garmin OneHelm:** integração via MFD.

## Comparação técnica entre tecnologias

| Tecnologia | Cabos | Resolução | EMI | Compatibilidade LED | Custo |
|------------|-------|-----------|-----|---------------------|-------|
| **PWM** | 2 (alimentação) | Análoga (∞) | Variável | Alta (driver PWM) | Baixo |
| **TRIAC** | 2 (alimentação) | Análoga | Alta sem filtro | Baixa (precisa LED dim TRIAC) | Baixo |
| **0-10V** | 4 (potência + sinal) | Análoga (1024) | Baixa | Alta (driver 0-10V) | Médio |
| **DALI** | 2 (bidirecional) | 254 níveis | Baixa | Alta (driver DALI) | Médio-alto |
| **DMX512** | 3 (1 par + GND) | 256 níveis × 512 canais | Baixa | Alta (driver DMX) | Médio-alto |
| **Wireless RF** | Bateria/cabo | Variável | Variável | Alta (proprietário) | Médio-alto |

## Onde se encaixa

```
[Bateria 12V/24V] → [Disjuntor] → [Dimmer] → [Driver LED] → [Luminária]
                                       │
                                       └─ [Controle: rotativo / toque / app / scene]
```

## Fabricantes e modelos dominantes

### Marine-specific

- **Lumitec POCO** — controle wireless multi-luminária.
- **Lumishore Lumix Sense** — touch + scene.
- **Aqualuma EZ-Connect** — controle fácil.
- **Hella Marine** — dimmer integrado.

### Generalista premium

- **Lutron Caseta / Vive / RA2 Select** — referência residencial premium adaptável.

### Digital switching marine

- **CZone (Power Products)** — referência marine digital switching.
- **EmpirBus NG / NG2** — concorrente premium.
- **Garmin OneHelm** — integração via MFD.

### DMX professional

- **Pathway Connectivity** — interfaces DMX.
- **ENTTEC** — controllers DMX USB / network.

> [!example] Comparação Brasil 2024-2026
> | Equipamento | Tipo | Preço (R$) |
> |-------------|------|------------|
> | PWM dimmer 12V genérico 10A | Manual rotativo | 150-500 |
> | Lutron Caseta starter kit | Bluetooth + Wi-Fi | 1.500-3.500 |
> | Lumitec POCO 2-zone | Wireless marine | 2.500-5.000 |
> | CZone Touch 5 + módulos | Digital switching | 8.000-25.000 |
> | EmpirBus NG2 sistema completo | Digital switching | 15.000-50.000 |
> | DMX512 controller 4-universe | Profissional | 3.000-12.000 |

## Falhas comuns

| # | Falha | Causa | Solução |
|---|-------|-------|---------|
| 1 | LED pisca | Não-dimável + dimmer | LED dimável compatible |
| 2 | LED queima | Mismatch dimmer-driver | Trocar conjunto |
| 3 | Zumbido audível | TRIAC harmônico | PWM ou 0-10V |
| 4 | EMI no VHF | Driver sem EMC | Certificado + ferrite |
| 5 | Dimmer queima | Sobrecarga | Calcular corrente + 30% |
| 6 | Wireless intermitente | Bateria / interferência | Cabo backup |
| 7 | Scene não responde | Comissionamento errado | Re-comissionar |
| 8 | DALI duplo endereço | Address conflict | DALI Commissioner |

## Boas práticas

- **Verificar compatibilidade** antes de comprar.
- **Testar com 1 LED** antes de instalar conjunto.
- **EMC certificada** preferida.
- **Documentar** tipo + modelo + zonas.
- **Backup manual** se sistema digital.
- **Teste mensal** de scenes + override.
- **Bonding** da carcaça AC.
- **Surge protection** em cabos longos.

## Erros comuns

- "Qualquer dimmer funciona com LED." → Falso.
- "Mais barato é igual." → EMC variável.
- "Frequência PWM não importa." → <200 Hz = flicker.
- "Posso usar dimmer AC em LED 12V." → Falso. Sistemas separados.

## Glossário

- **Dimmer:** controlador de intensidade.
- **PWM:** Pulse Width Modulation.
- **TRIAC:** Triode for Alternating Current (corte de fase).
- **0-10V:** sinal analógico de controle.
- **DALI:** Digital Addressable Lighting Interface (IEC 62386).
- **DMX512:** padrão USITT.
- **Bluetooth Mesh:** rede BLE.
- **Digital switching:** controle digital de cargas (CZone, EmpirBus).
- **Scene:** cena pré-definida.
- **Group:** grupo de luminárias.
- **Universe (DMX):** 512 canais.
- **Frequência PWM:** Hz.
- **Flicker:** oscilação visível.
- **Driver dimável:** compatível com sinal de controle.
- **TRIAC-compatible:** LED com driver TRIAC.
- **Compatibilidade leading-edge / trailing-edge:** TRIAC modos.
- **Logarithmic dimming:** curva natural ao olho.
- **Comissionamento DALI:** atribuição de endereços.
- **EmpirBus / CZone:** digital switching marine.
- **Lutron Caseta:** Bluetooth Mesh + Wi-Fi.
- **Lumitec POCO:** wireless marine.
- **Vide [[Tipos de Lâmpadas e LEDs Náuticos]]** + [[Fitas Led - Iluminação Led]] — fundamentos.

## Integração com outras notas

- [[Tipos de Lâmpadas e LEDs Náuticos]] — fundamentos.
- [[Fitas Led - Iluminação Led]] — aplicação típica PWM.
- [[Luz de Cortesia]] / [[Luzes Internas Teto]] — controle de cena.
- [[Iluminação de Emergência a Bordo]] — backup independente.
- [[Automação de Bordo — Sistemas Domoticos]] — integração total.
- [[Bonding — Sistema de Interligação de Massas]] — aterramento AC.
- [[Cabeamento Náutico]] — cabos.
- [[Quadro Elétrico e Painel de Distribuição AC-DC]] — disjuntor.
- [[Fusíveis DC — Proteção Contra Sobrecorrente]] — proteção.
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]] — diagnóstico.

## Perguntas que esta nota responde

- Por que LED pisca com dimmer existente?
- PWM ou TRIAC dimmer para LED em barco?
- Como integrar dimmer ao sistema de automação?
- Dimmer wireless Bluetooth funciona em ambiente marine?
- Como evitar zumbido do dimmer com fita LED?
- Frequência PWM ideal para evitar flicker?
- Dimmer DALI vs DMX: qual usar em yacht?
- Dimmer compatível com fita LED 12V — qual escolher?
- Dimmer rotativo versus toque versus app: qual melhor?
- Como dimensionar carga máxima do dimmer?
