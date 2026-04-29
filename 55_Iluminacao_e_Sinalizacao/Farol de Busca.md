---
title: "Farol de Busca"
note_type: "technical-note"
domain: "55_Iluminacao_e_Sinalizacao"
source_file: "FAROL DE BUSCA bfe19734f7fb83b9becc01589acd8157.md"
status: "premium-l3"
fase_6_reescrita: 87
reviewed_on: "2026-04-25"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://webstore.iec.ch/publication/2697"
  - "https://www.acrartex.com/"
  - "https://www.hellamarine.com/"
  - "https://www.lumitec.com/"
review_level: "engineering-curated"
aliases:
  - "FAROL DE BUSCA"
  - "Searchlight"
  - "Marine spotlight"
  - "Holofote náutico"
  - "Farol manobra"
  - "Farol direcional"
  - "Spotlight controlável"
seo_title: "Farol de busca náutico (searchlight): ABYC A-30/E-11, IEC 60945, fixo × giratório, COLREGS Rule 36"
seo_description: "Guia técnico premium do farol de busca (searchlight / spotlight) em embarcações: tipos (fixo manual × giratório motorizado × LED bar × multifeixe), potência 35-300W, ABYC A-30/E-11/TE-30, IEC 60945, COLREGS Rule 36 (sinal de chamar atenção), fabricantes (ACR, Golight, Hella Marine Mega Beam, Lumitec, Vetus), instalação, dimensionamento elétrico, EMC."
seo_keywords:
  - "farol de busca barco"
  - "marine searchlight"
  - "Golight Stryker"
  - "ACR RCL-100/100D"
  - "Hella Mega Beam"
  - "Lumitec searchlight"
  - "LED bar marine"
  - "spotlight wireless"
  - "COLREGS Rule 36"
  - "ABYC A-30"
geo_queries:
  - "Diferença entre farol fixo e giratório no barco?"
  - "Quantos watts para farol de busca em yacht 40 ft?"
  - "Posso usar farol de busca para sinalizar outra embarcação?"
  - "LED bar 240W tem mesma performance que farol HID 100W?"
  - "Como integrar farol giratório ao MFD via NMEA 2000?"
  - "Farol de busca pode confundir com luz de navegação (COLREGS)?"
  - "Por que farol queima em horas de uso contínuo?"
  - "Wireless ou cabeado: qual escolher?"
  - "Farol de busca atrapalha visão noturna da tripulação?"
  - "Como dimensionar fusível para farol 100W em 12V?"
normas_citadas:
  - "ABYC E-11 (AC and DC Electrical Systems on Boats)"
  - "ABYC A-30 (Cabin and Weather Deck Illumination)"
  - "ABYC TE-30 (Electronic Equipment Installation Standards)"
  - "ABYC TE-04 (Lightning Protection)"
  - "IEC 60598-1 (Luminaires — General)"
  - "IEC 60598-2-3 (Luminaires for road/street — princípio analógico)"
  - "IEC 60945 (Maritime navigation equipment)"
  - "IEC 61347 (Lamp control gear)"
  - "IEC 62471 (Photobiological safety — Risk Group para alta potência)"
  - "IEC 60529 (IP code)"
  - "IEC 61547 (EMC for lighting)"
  - "IEC 61000-6-1/-3 (EMC)"
  - "ISO 19009 (Internal lighting on small craft)"
  - "ISO 8846 (Ignition protection)"
  - "UL 1598 (Luminaires)"
  - "UL 8750 (LED equipment)"
  - "COLREGS Rule 36 (Signals to attract attention — uso de farol controlado)"
  - "COLREGS Rule 22 (Visibility of lights — não confundir com nav lights)"
  - "COLREGS Annex IV (Distress signals — uso de farol em emergência)"
  - "USCG NVIC 7-04 (referência cruzada)"
  - "EU Directive 2014/35/EU (LVD)"
  - "EU Directive 2014/30/EU (EMC)"
  - "EU 2013/53/EU (RCD)"
  - "ABNT NBR 5410 (Instalações elétricas BT)"
  - "ABNT NBR 14728 (Embarcações de recreio)"
  - "INMETRO Portaria 144/2015 (LED)"
  - "ANATEL Resolução 715/2019 (homologação eletrônica + RF wireless)"
  - "DPC NORMAM-211/DPC (esporte e recreio)"
  - "DPC NORMAM-201/DPC (comerciais)"
  - "Manual técnico ACR RCL-100 / 100D / 75 / 50 / 95"
  - "Manual técnico Golight Stryker / GXL / RadioRay"
  - "Manual técnico Hella Marine Mega Beam / Sea Hawk Pro"
  - "Manual técnico Lumitec Caprera2 / Mirage / Lighting Control"
  - "Manual técnico Vetus Searchlight / Carlisle"
  - "Manual técnico Imtra ILSL / Pacific Floodlight"
  - "Manual técnico Quick Italy / Nemo Light Bar"
  - "Manual técnico Rigid Industries / Baja Designs (LED bars marine-grade)"
related_notes:
  - "Tipos de Lâmpadas e LEDs Náuticos"
  - "Dimmer — Controle de Intensidade Luminosa"
  - "Fitas Led - Iluminação Led"
  - "Strobo"
  - "Luz de Cortesia"
  - "NAVEGAÇÃO (BB, BE e Alcançado)"
  - "Bonding — Sistema de Interligação de Massas"
  - "Cabeamento Náutico"
  - "Dimensionamento de Cabos DC — Cálculo Prático"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Disjuntores (DC) e (AC)"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
---

# Farol de Busca

> [!abstract] Resumo técnico
> O **farol de busca (searchlight / marine spotlight)** é a luminária de **alta intensidade direcional** instalada na embarcação para **iluminação a distância** em manobra noturna, busca de objeto/pessoa, navegação em águas rasas com balizamento limitado, identificação de outras embarcações e sinalização de atenção (**COLREGS Rule 36** — "signals to attract attention" — permitido se não puder ser confundido com sinal de socorro). **Não é luz de navegação** (vide [[NAVEGAÇÃO (BB, BE e Alcançado)]]); pelo contrário, **COLREGS Rule 22 alerta para que farol de busca não seja confundido com luzes de navegação**. Quatro arquiteturas dominantes: **fixo manual** (apontamento mecânico em popa/cabine — entry-level), **giratório motorizado com controle remoto/cabeado/wireless** (ACR RCL-100/100D, Golight Stryker — referência), **LED bar com múltiplos feixes** (Rigid Industries, Baja Designs, Quick Italy Nemo — manobra de marina e visualização ampla), **multifeixe combinado** (Lumitec Caprera2 — fixo + giratório). Tecnologia migrou de **HID/halogênio (50-100W consumo + calor extremo + vida 200-1000 h)** para **LED (35-300W com mesmo brilho + 25.000+ h vida)**. Padrões: **ABYC A-30** (cabin and weather deck illumination) + **ABYC E-11** (wiring) + **IEC 60598/60945/62471** + **EU 2014/30/EU EMC**. Vide [[Tipos de Lâmpadas e LEDs Náuticos]] para fundamentos compartilhados.

> [!tldr] TL;DR — 9 regras inegociáveis
> 1. **Farol de busca NÃO é luz de navegação.** COLREGS Rule 22 + Rule 36: uso esporádico para chamar atenção/identificar — NÃO substitui luzes obrigatórias (Tope, BB, BE, Alcançado, Âncora). Uso contínuo em movimento = infração + risco de colisão.
> 2. **Dimensionamento elétrico crítico:** farol 200W em 12V = 17A nominal + pico 25A (LED) ou 35A (HID). Fusível ANL/MIDI a 125% do pico, ≤7" da bateria (ABYC E-11.5.4); cabo AWG 8-10 para 5 m com queda <3% (ABYC E-11.4.4.1.b); circuito dedicado.
> 3. **LED substituiu HID/halogênio em 95% das aplicações.** LED 100W bar > halógena 100W spot em alcance + vida útil 25× maior. Manter halogênio só em luminárias certificadas existentes ou aplicações específicas.
> 4. **Fixo manual em yacht <30 ft** geralmente suficiente (manobra ocasional); **giratório motorizado** padrão >35 ft (ACR RCL-100/Golight Stryker — controle joystick + 360° rotação + 90° elevação).
> 5. **Wireless tem latência (50-300 ms) e bateria a manter** — em manobra crítica, cabeado ainda é mais confiável. Modelos modernos (ACR RCL-100D) operam ambos modos (wireless + cabeado backup).
> 6. **Tempo de uso contínuo limitado** — LED de alta potência precisa de dissipação. Maioria dos faróis premium tem proteção térmica que reduz potência ou desliga após 30-60 min uso contínuo. Verificar duty cycle no manual.
> 7. **Anti-flicker EMC importante** — driver de 200W com EMC ruim mata VHF/GPS adjacente. **IEC 61547 + EU 2014/30/EU EMC + IEC 60945** se usado em equipamento de bordo.
> 8. **Iluminação direta em outra embarcação tem etiqueta:** "blinking" / piscar para chamar atenção (Rule 36) é aceitável; manter farol direto na ponte de outra embarcação por longos períodos é falta de boas práticas + risco de cegueira temporária do timoneiro adjacente.
> 9. **Visão noturna da tripulação:** acender farol forte na ponte → tripulação perde adaptação à escuridão (15-30 min de recuperação). Usar com critério; acender só quando necessário; backup com LED vermelho na sala de carta.

> [!danger] Cenários de risco
> - **Confusão com luz de navegação por outra embarcação:** farol de busca branco fixo em rota → outra embarcação interpreta como luz de tope errada → manobra de evasão errada → colisão. **Caso histórico:** documentado em vários relatórios de USCG/IIMS. **Prevenção:** uso esporádico apenas; piscar (Rule 36); desligar quando não em uso ativo.
> - **Cegueira temporária do timoneiro adjacente** (próprio ou de outro barco): farol 200W direto nos olhos → 15-30 min de visão noturna perdida + lacrimejamento → manobra errada possível. **Prevenção:** evitar apontar para outra cabine; desligar antes de outro barco se aproximar.
> - **Surto / curto durante uso prolongado:** cabos subdimensionados aquecem → derretimento de isolação → curto entre +12V e GND ou casco → fogo elétrico. **Caso típico:** farol 100W com cabo AWG 14 em 5 m (deveria ser AWG 8) → Δt rises rapidly. **Prevenção:** dimensionamento correto; fusível protege.
> - **EMI severo do driver mata VHF/GPS:** farol LED 200W com driver chinês sem EMC → VHF "scratchy" / GPS perde fix em manobra crítica. **Prevenção:** modelos certificados EMC (ACR/Golight/Hella/Lumitec); ferrite cores; cabo separado.
> - **Falha mecânica do giratório motorizado** em uso intenso: motor de pan/tilt queima em manobra prolongada → farol fica "preso" em direção fixa em momento crítico. **Prevenção:** modelos com motor robusto (ACR RCL-100D, Golight Stryker GXL); inspeção / lubrificação anual.
> - **Choque por farol AC em ambiente molhado:** instalação 220V em farol externo + casco molhado + ELCI defeituoso → choque ao tocar carcaça. **Prevenção:** SEMPRE 12V/24V DC em farol externo; ELCI 30 mA; bonding.
> - **Falha de bateria em uso prolongado** (charter, busca SAR): farol 200W consome 17A → banco 100Ah dura 3-5h apenas com farol; pode "matar" a bateria principal. **Prevenção:** circuito separado ligado em banco de serviço (não banco de motor); monitor de bateria.
> - **Wireless dropout em manobra crítica:** controle wireless perde sinal (interferência, bateria do remoto, distância) → farol fica fixo + tripulante volta para console. **Prevenção:** modelos com fail-over para cabeado (ACR RCL-100D); remoto com bateria carregada; backup manual.
> - **Lente quebrada por pedra / impacto** + chuva: water ingress no driver → curto + corrente reversa via cabo → eletrônica de bordo afetada. **Prevenção:** lente policarbonato (não vidro); montagem em zona protegida; surge protection.
> - **Uso ilegal em zona regulada:** Iluminar para pesca em ARIE/parque marinho → multa Lei 9.605 + IBAMA + Marinha. **Prevenção:** consultar regulação local; respeitar áreas protegidas; pesca esportiva em zonas legais.

## O que é (definição rigorosa)

O **farol de busca** é a luminária de **alta intensidade luminosa direcional** com:

1. **Refletor parabólico ou óptica focada** que concentra o feixe em ângulo estreito (típico 6-15° para spotlight; 30-60° para floodlight; 8-30° para LED bar).
2. **Fonte de luz de alta potência** (35-300W LED moderno; ou 50-100W halógeno; ou 50-150W HID legacy).
3. **Carcaça resistente** ao ambiente marine (alumínio anodizado, polímero composto, ou aço inox 316).
4. **Lente** policarbonato (resistente a impacto) ou vidro temperado.
5. **Mecanismo de apontamento** (manual em fixo; pan/tilt motorizado em giratório).
6. **Driver eletrônico** com EMC certificada.

### Comparação com outras luminárias

| Tipo | Função | Intensidade | Spread | Continuidade |
|------|--------|-------------|--------|--------------|
| **Luz de tope (nav)** | Sinalização posição | Baixa-média | 360° (Tope/Alcançado) ou 112,5° (BB/BE) | Contínua em movimento |
| **Luz de âncora** | Sinalização posição em fundeio | Baixa | 360° | Contínua em fundeio |
| **Luz de cabine** | Iluminação interna | Média | 360° amplo | Contínua quando precisar |
| **Luz de cortesia** | Circulação noturna | Baixa | Difusa | Contínua noturna |
| **Farol de busca** | Iluminação distante esporádica | **Muito alta** | Direcional estreito | Esporádica (uso ocasional) |
| **LED bar** | Iluminação ampla manobra | Alta | Direcional amplo | Esporádica (manobra) |

## Comparação técnica entre tecnologias

### Quatro arquiteturas

#### 1. Farol fixo manual

```
[Carcaça parafusada na popa / cabine] ── [Apontamento manual via punho]
        │
        └── [Driver interno + cabo de alimentação]
```

- **Aplicação:** yacht 25-35 ft; uso ocasional.
- **Custo:** R$ 800-3.500.
- **Modelos:** Hella Marine Mega Beam (LED), Vetus Searchlight Manual.

#### 2. Farol giratório motorizado

```
[Carcaça com motor pan/tilt] ── [Cabo de controle + alimentação]
        │
        └── [Joystick console / remoto cabeado / wireless RF / NMEA 2000]
```

- **Aplicação:** yacht 35+ ft; charter; comercial; busca SAR.
- **Custo:** R$ 8.000-50.000.
- **Modelos:** **ACR RCL-100 / 100D / 75 / 50 / 95** (referência), **Golight Stryker / GXL / RadioRay**, Carlisle Searchlight.
- **Diferencial RCL-100D:** wireless + cabeado backup + interface NMEA 2000.

#### 3. LED bar / light bar

```
[Barra com múltiplos LEDs (4 a 60+)] ── [Cabo de alimentação]
        │
        └── [Driver integrado]
```

- **Aplicação:** manobra de aproximação a píer, visualização ampla, complemento.
- **Custo:** R$ 1.500-15.000.
- **Modelos:** Rigid Industries (RDS / SR / D-Series — marine-grade), Baja Designs Squadron, Quick Italy Nemo.

#### 4. Multifeixe combinado

```
[Carcaça] ── [Spot focado + flood spread + RGB ambient]
        │
        └── [Controle integrado via app / NMEA 2000]
```

- **Aplicação:** premium yachts.
- **Modelos:** Lumitec Caprera2 / Mirage / Lighting Control system.

### Potência × alcance

| Potência LED | Alcance típico | Aplicação |
|--------------|----------------|-----------|
| 35-50W | 100-200 m | Yacht <30 ft, fixed |
| 80-120W | 200-400 m | Yacht 30-45 ft, search occasional |
| 150-200W | 400-700 m | Yacht 45-65 ft, charter, SAR backup |
| 250-300W+ | 700-1500+ m | Comercial, SAR profissional, mega-iates |

### Tipos de feixe

| Tipo | Ângulo | Aplicação |
|------|--------|-----------|
| **Spot (focado)** | 6-15° | Identificação a distância |
| **Combo (intermediate)** | 15-30° | Misto |
| **Flood (amplo)** | 30-60° | Manobra próxima |
| **Driving (longo+médio)** | Variável | LED bar — combinação |

## Onde se encaixa na arquitetura

```
[Bateria de serviço] ── [Disjuntor / Fusível] ── [Chave dedicada / Console]
                                                            │
                                            ┌──────────────┴──────────────┐
                                            │                              │
                                  [Farol fixo / giratório]         [Console controle]
                                                                          │
                                                                   [Joystick / app / NMEA]
```

## Fabricantes e modelos dominantes (mercado 2024-2026)

### ACR Electronics (USA — referência giratórios)

- **RCL-100 / RCL-100D** — flagship LED 350.000 cd, NMEA 2000 + wireless, 12/24V.
- **RCL-95** — versão sem wireless.
- **RCL-75 / RCL-50** — entry/mid.

### Golight (USA)

- **Stryker / Stryker ST** — pan/tilt LED, wireless, premium.
- **GXL** — LED bar / spot integrado.
- **RadioRay** — economic LED com wireless.

### Hella Marine (referência fixos LED)

- **Mega Beam LED** — fixo, alta potência.
- **Sea Hawk Pro** — flood/spot mid-range.

### Lumitec (USA)

- **Caprera2 / Mirage** — multifeixe + RGB.
- **Lighting Control System** — integração completa.

### Vetus (NL)

- **Searchlight Halogen / LED** — entry-level fixo.
- **Carlisle** — premium giratório.

### Imtra (USA)

- **ILSL Series Searchlight** — premium.
- **Pacific Floodlight** — LED bar.

### Quick Italy

- **Nemo Light Bar** — LED bar marine.

### LED Bars (multiuso, instalação marine-grade)

- **Rigid Industries RDS / SR / D-Series** — marine-grade tested.
- **Baja Designs Squadron / S8 / OnX6** — marine-grade.
- **Auxbeam / Nilight** — entry-level chinês (cuidado com EMC).

> [!example] Comparação Brasil 2024-2026 (importado)
> | Equipamento | Potência | Preço (R$) |
> |-------------|----------|------------|
> | Hella Mega Beam LED Fixed | 50W | 1.800-3.500 |
> | Vetus LED Searchlight Manual | 30W | 1.500-2.800 |
> | Lumitec Caprera2 Mirage Multibeam | 100W | 12.000-20.000 |
> | ACR RCL-50 LED | 50W giratório wireless | 8.000-13.000 |
> | ACR RCL-100D LED | 350.000 cd giratório | 22.000-38.000 |
> | Golight Stryker ST | 215.000 cd giratório | 18.000-30.000 |
> | Quick Italy Nemo LED Bar 30" | 240W | 3.500-6.500 |
> | Rigid Industries RDS Marine 30" | 240W | 5.500-9.000 |

## Instalação correta (ABYC E-11 + A-30 + TE-30)

### Localização

1. **Linha de visão limpa** sem obstrução por mastro/antena.
2. **Sem ofuscamento da ponte** (não direcionar para console).
3. **Acesso para manutenção** (limpeza de lente).
4. **Estrutura mecânica reforçada** para o peso + vibração.
5. **Mínimo 1 m de antena VHF/GPS** (EMI).

### Cabeamento

1. **Cabo dedicado** com fusível ANL/MIDI/ATC.
2. **Bitola** dimensionada para corrente + queda <3%.
3. **Cabo blindado** se driver com EMC marginal.
4. **Roteamento** longe de antenas RF.

### Fusível e proteção

- Farol 100W em 12V → 8,3A nominal + pico 12A (LED) → fusível 15-20A ANL.
- Farol 200W em 12V → 17A nominal + pico 25A → fusível 25-30A ANL.
- Cabo AWG 8 para 5 m em 100W; AWG 6 para 200W.

### Bonding e proteção

- **Bonding** da carcaça (ABYC E-11.16) — surge + corrosão.
- **Surge protector** (ABYC TE-04) — relâmpago.

## Falhas mais comuns

| # | Falha | Causa raiz | Diagnóstico |
|---|-------|------------|-------------|
| 1 | Farol fica fixo (giratório) | Motor pan/tilt queimado | Substituir motor; revisar mecânica |
| 2 | Wireless intermitente | Bateria do remoto / interferência | Trocar bateria; aproximar; cabeado backup |
| 3 | LED queima | Calor + driver ruim | Modelo com dissipação adequada |
| 4 | Tira de baixa intensidade | Driver de baixa qualidade | Trocar |
| 5 | EMI no VHF | Driver sem EMC | Ferrite cores; trocar |
| 6 | Curto após chuva | IP inadequado | Modelo IP67+ |
| 7 | Lente fosca | UV degradation | Substituir |
| 8 | Fusível abre em uso prolongado | Subdimensionamento | Calcular nominal + pico |

## Boas práticas operacionais

- **Uso esporádico** — não como iluminação permanente.
- **Pisca para chamar atenção** (COLREGS Rule 36) — não fixo.
- **Desligar antes de aproximação a outra embarcação** (cegueira).
- **Verificar fusível e bitola** anualmente.
- **Inspeção do giratório** (lubrificação, motor) anualmente.
- **Backup do remoto wireless** (bateria carregada).
- **Bonding** da carcaça.
- **EMC certificada** (ACR/Golight/Hella/Lumitec) preferida.
- **Documentar** modelo, fusível, bitola.
- **Treinamento** da tripulação no controle.

## Erros comuns

- "Farol de busca substitui luz de navegação." → Falso e perigoso. Rule 22 + Rule 36.
- "Mais watts = melhor." → Em LED, ~100W bem feito > 200W mal feito.
- "Wireless é sempre superior." → Latência + bateria; cabeado backup é prática.
- "Posso apontar farol fixo em rota." → Falso. Confusão com luz de navegação.
- "LED bar de carro funciona em barco." → Pode funcionar mas IP/EMC/material variável; preferir marine-grade.
- "Fusível de 30A funciona para 100W em 12V." → Excessivo; queima motor antes do fusível.

## Glossário

- **Searchlight / spotlight:** farol direcional alta intensidade.
- **Floodlight:** feixe amplo.
- **LED bar:** barra com múltiplos LEDs.
- **Pan/tilt:** rotação horizontal/vertical.
- **Joystick:** controle direcional.
- **Wireless RF:** controle por rádio.
- **NMEA 2000 control:** integração à rede.
- **Beam angle:** ângulo do feixe.
- **Candela (cd):** intensidade luminosa direcional.
- **Lumens (lm):** fluxo total.
- **Candle power (cp):** unidade legacy = candela.
- **Throw / range:** alcance efetivo.
- **HID:** High-Intensity Discharge (xenon, metal halide).
- **Halogênio:** lâmpada de filamento + halogênio.
- **LED:** semicondutor.
- **Driver constante (CC ou CV):** alimentação do LED.
- **Duty cycle:** tempo ON/OFF permitido.
- **Thermal protection:** redução de potência por aquecimento.
- **IP code:** Ingress Protection.
- **EMC:** compatibilidade eletromagnética.
- **EMI:** interferência eletromagnética.
- **COLREGS Rule 36:** sinais para chamar atenção.
- **COLREGS Rule 22:** visibilidade de luzes.
- **ABYC A-30:** cabin and weather deck illumination.
- **Ferrite core:** supressor EMI.
- **Surge protector:** protetor de surto.
- **Pan / Tilt:** horizontal / vertical rotation.
- **Vide [[Tipos de Lâmpadas e LEDs Náuticos]]** — fundamentos.

## Integração com outras notas

- [[Tipos de Lâmpadas e LEDs Náuticos]] — fundamentos LED.
- [[Dimmer — Controle de Intensidade Luminosa]] — não usado em farol (controle on/off).
- [[Fitas Led - Iluminação Led]] — complemento ambient.
- [[Strobo]] — sinal de emergência (Rule 36 também).
- [[Luz de Cortesia]] — diferenciação.
- [[NAVEGAÇÃO (BB, BE e Alcançado)]] — distinção crítica.
- [[Bonding — Sistema de Interligação de Massas]] — aterramento.
- [[Cabeamento Náutico]] / [[Dimensionamento de Cabos DC — Cálculo Prático]] — bitola.
- [[Fusíveis DC — Proteção Contra Sobrecorrente]] / [[Disjuntores (DC) e (AC)]] — proteção.
- [[Quadro Elétrico e Painel de Distribuição AC-DC]] — disjuntor dedicado.
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]] — diagnóstico.

## Perguntas que esta nota responde

- Diferença entre farol fixo e giratório no barco?
- Quantos watts para farol de busca em yacht 40 ft?
- Posso usar farol de busca para sinalizar outra embarcação?
- LED bar 240W tem mesma performance que farol HID 100W?
- Como integrar farol giratório ao MFD via NMEA 2000?
- Farol de busca pode confundir com luz de navegação (COLREGS)?
- Por que farol queima em horas de uso contínuo?
- Wireless ou cabeado: qual escolher?
- Farol de busca atrapalha visão noturna da tripulação?
- Como dimensionar fusível para farol 100W em 12V?
