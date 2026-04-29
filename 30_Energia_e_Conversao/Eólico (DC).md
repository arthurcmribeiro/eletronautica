---
title: "Eólico (DC)"
note_type: "technical-note"
domain: "30_Energia_e_Conversao"
status: "premium-l3"
fase_6_reescrita: 103
reviewed_on: "2026-04-26"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://webstore.iec.ch/publication/2697"
  - "https://www.silentwindgenerator.com/"
  - "https://www.ampair.com/"
review_level: "engineering-curated"
aliases:
  - "Eólico DC"
  - "Aerogerador marine"
  - "Wind generator marine"
  - "Wind turbine náutico"
  - "Marine wind charger"
seo_title: "Aerogerador marine (eólico DC): IEC 61400, ABYC E-11, Silentwind, Air Breeze, Ampair, dimensionamento, instalação"
seo_description: "Guia técnico premium do aerogerador (wind turbine / wind generator) DC em embarcação: IEC 61400-2 (small wind turbines), ABYC E-11, IEC 60092, classe de vento, curva de potência (cut-in × rated × cut-out), brake, regulador de carga MPPT, fabricantes (Silentwind, Air Breeze, Air X, Ampair, Eclectic D400), instalação no mastro / dedicated post."
seo_keywords:
  - "aerogerador marine"
  - "wind turbine náutico"
  - "Silentwind"
  - "Air Breeze Air X"
  - "Ampair 100 300"
  - "Eclectic D400"
  - "IEC 61400-2"
  - "MPPT wind"
  - "regulador eólico"
  - "cut-in cut-out wind"
geo_queries:
  - "Aerogerador vale a pena no veleiro?"
  - "Quanto produz um wind generator marine?"
  - "Silentwind ou Air Breeze?"
  - "Como instalar wind turbine no mastro?"
  - "Aerogerador faz barulho à noite?"
  - "Wind charger queima em rajada forte?"
  - "Conexão eólico ao banco — regulador necessário?"
  - "MPPT funciona com eólico?"
  - "Manutenção do aerogerador?"
  - "Eólico vs solar: qual produzir mais em barco?"
normas_citadas:
  - "ABYC E-11 (AC and DC Electrical Systems on Boats)"
  - "ABYC E-11.5 (Overcurrent protection)"
  - "ABYC E-11.16 (Bonding)"
  - "ABYC TE-04 (Lightning protection)"
  - "IEC 61400-1 (Wind turbines — Design requirements)"
  - "IEC 61400-2 (Small wind turbines — design)"
  - "IEC 61400-12 (Power performance measurements)"
  - "IEC 61400-21 (Power quality)"
  - "IEC 61400-24 (Lightning protection)"
  - "IEC 60092-507 (Pleasure craft)"
  - "IEC 60364-7-712 (Photovoltaic — referência cruzada)"
  - "IEC 60529 (IP)"
  - "ISO 28848 (DC installations)"
  - "ISO 13297 (AC installations)"
  - "IEEE 1547 (Interconnection — referência)"
  - "ABNT NBR 14728"
  - "ABNT NBR 5410"
  - "ABNT NBR IEC 61400-2"
  - "INMETRO Portaria 4/2010 (eólico residencial — referência)"
  - "DPC NORMAM-211/DPC"
  - "DPC NORMAM-201/DPC"
  - "Manual técnico Silentwind 400W / Pro"
  - "Manual técnico Air Breeze / Air X / Air 40 (Primus Wind Power)"
  - "Manual técnico Ampair 100 / 300 / 600"
  - "Manual técnico Eclectic D400 / DUOGEN"
  - "Manual técnico Rutland 504 / 914i / 1200"
  - "Manual técnico Aerogen 4F / 6"
related_notes:
  - "Tipos de Bateria"
  - "Bancos de Bateria"
  - "Placa Solar (DC)"
  - "Carregador de Bateria (AC To DC)"
  - "Inversora (DC To AC)"
  - "Cabeamento Náutico"
  - "Dimensionamento de Cabos DC — Cálculo Prático"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Bonding — Sistema de Interligação de Massas"
  - "Lei de Ohm e Cálculos Básicos"
  - "Estação de Vento - Anemômetro"
---

# Eólico (DC)

> [!abstract] Resumo técnico
> O **aerogerador marine (wind generator / wind turbine DC)** é o **gerador de carga DC alimentado pelo vento** — fonte de energia auxiliar em **veleiros offshore, mega-iates e embarcações em fundeio prolongado**. Modelos típicos produzem **100-600W em vento 12-15 nós** (cruzeiro), com **cut-in 4-6 nós, rated 25-30 nós, cut-out 35-40 nós** (proteção contra sobrevelocidade). Tecnologia: **gerador permanent magnet DC** + **3-5 pás** + **rabicho ou tail vane** para auto-orientação ao vento + **regulador de carga MPPT (preferível) ou shunt regulator**. Instalação típica: **mastro dedicado de proa ou popa (não principal de vela — turbulência)** ou **mastro principal em yacht motor**. Fabricantes dominantes: **Silentwind 400W (Portugal — referência), Air Breeze / Air X (Primus Wind Power USA), Ampair (UK legacy), Eclectic D400 / DUOGEN (UK), Rutland 504 / 914i / 1200, Aerogen 4F**. Padrões: **IEC 61400-2** (small wind turbines), **ABYC E-11** (wiring), **IEC 60092-507** (pleasure craft), **ABYC TE-04** (lightning protection — torre + brake elétrico em tempestade). Vide [[Placa Solar (DC)]] para fonte alternativa complementar.

> [!tldr] TL;DR — 9 regras inegociáveis
> 1. **Eólico complementa solar, não substitui.** Em barco fundeado: **solar produz 30-150 Ah/dia** (depende lat/sol), **eólico 30-100 Ah/dia** (depende vento médio). Combinar é prática.
> 2. **Fabricantes premium (Silentwind, Air Breeze) >> chineses genéricos.** Diferença: brake elétrico, qualidade de mancal, geração em vento fraco, ruído, vida útil 8-15 anos vs 1-3 anos.
> 3. **Cut-out automático** em vento >35-40 nós — protege contra sobrevelocidade. **Brake elétrico manual** acessível em emergência (tempestade).
> 4. **Regulador de carga obrigatório** — eólico em direct-drive sem regulação mata banco. **MPPT é melhor** (extrai mais energia em vento variável); shunt é mais simples.
> 5. **Localização longe de tripulação** (ruído + ferimento por pás): mastro dedicado de proa/popa, altura 3-5 m acima do deck. NÃO em mastro de vela (turbulência).
> 6. **Lightning protection** (ABYC TE-04 + IEC 61400-24): torre aterrada à quilha; protetor de surto na entrada DC.
> 7. **Bitola de cabo** dimensionada para corrente máxima (rated × 125%). Silentwind 400W em 12V = 33A → AWG 8 mínimo até 5m.
> 8. **Manutenção:** lubrificação anual de mancal; inspeção visual de pás (rachadura → falha catastrófica); aperto de parafusos; verificação de regulador.
> 9. **Aplicação ideal:** veleiros offshore em latitudes com vento (Caribe, Mediterrâneo, Atlântico Norte, Pacífico); pouco efetivo em água doce ou ancoradouro protegido.

> [!danger] Cenários de risco
> - **Pá quebra em rajada >50 nós** sem cut-out: pedaço de pá voa 50-100 m em alta velocidade → ferimento grave em tripulação ou outro barco. **Caso histórico:** múltiplos casos documentados. **Prevenção:** cut-out automático <35 nós; brake elétrico manual; modelo certificado IEC 61400-2.
> - **Eólico sem regulador conectado a banco lítio:** sobretensão > 14,8V queima BMS → célula litio em risco de thermal runaway. **Prevenção:** regulador certificado para o tipo de bateria; nunca direct-drive em LFP.
> - **Surto atmosférico via torre eólica** queima banco + carregador + chartplotter: torre alta + cabo direto = antena para raio. **Prevenção:** ABYC TE-04 + IEC 61400-24; bonding torre-quilha; surge protector DC na entrada.
> - **Falha de bonding** + cabo DC → corrente parasita no casco → corrosão acelerada de hélice/eixos. **Prevenção:** ABYC E-11.16; cabo dedicado; isolador.
> - **Cabo subdimensionado em mastro alto** (cabo 10-15 m de comprimento): queda de tensão excessiva → eficiência cai 20-30% → "eólico não rende". **Prevenção:** AWG dimensionado para queda <3%.
> - **Vibração afrouxa parafusos do mounting:** torre / pás soltas → falha catastrófica em alta velocidade. **Prevenção:** Loctite 242 em todos os parafusos; inspeção semestral; substituir parafusos a cada 5 anos.
> - **Ruído noturno em fundeio** atrapalha tripulação + barcos vizinhos: modelos antigos (Air X first gen) eram rudes; modernos (Silentwind, Air Breeze) são mais silenciosos. **Prevenção:** modelo silent-design; localização longe de cabines; brake quando não usado.
> - **Pas com bird strike** ou impacto causa desbalanceamento → vibração violenta → falha de mancal. **Prevenção:** inspeção visual após cada tempestade ou impacto suspeito; substituir pá danificada.
> - **Curto interno do gerador** queima regulador → tensão DC oscila → eletrônica de bordo afetada. **Prevenção:** fusível dedicado entre eólico e regulador; regulador robusto.
> - **Oxidação de escovas em motor com escovas (modelos antigos):** após 3-5 anos contato degradado → tensão cai → carga insuficiente. **Prevenção:** modelo brushless preferido; manutenção das escovas se aplicável.

## O que é (definição rigorosa)

O **aerogerador marine** é o sistema de **conversão de energia eólica em DC** para carga de banco de bateria, composto por:

1. **Rotor (3-5 pás)** — captura energia do vento (eficiência típica 30-45% Betz limit ~59%).
2. **Gerador permanent magnet DC** (PMDC ou PMSG — Permanent Magnet Synchronous Generator) — converte rotação em energia elétrica.
3. **Tail vane / rabicho** — auto-orienta o rotor ao vento.
4. **Mounting (mastro / poste)** — estrutura mecânica.
5. **Regulador de carga** — MPPT ou shunt regulator (limita tensão de carga ao banco).
6. **Cabeamento DC** — bitola dimensionada para corrente máxima.
7. **Brake elétrico** — desligamento de emergência (curto-circuito do gerador via resistor).
8. **Surge protection + bonding** — proteção contra raio.

### Curva de potência típica (referência Silentwind 400W em 12V)

| Vento (nós) | Vento (m/s) | Potência (W) | Corrente (A) |
|-------------|-------------|---------------|---------------|
| 4-5 (cut-in) | 2-2,5 | 0-10 | 0-1 |
| 8 | 4 | 50 | 4 |
| 12 (cruzeiro) | 6 | 150 | 12 |
| 15 | 7,5 | 250 | 20 |
| 20 | 10 | 350 | 28 |
| 25 (rated) | 12,5 | 400 | 33 |
| 30 | 15 | 400 (regulado) | 33 |
| 35-40 (cut-out) | 17,5-20 | 0 (brake) | 0 |

> **Energia diária típica em fundeio com vento médio 12 nós:**
> - 150W × 18h efetivas (não-zero) ≈ 2.700 Wh = **225 Ah em 12V**.
> - Em uso real (vento variável + ineficiências): 80-150 Ah/dia.

## Tecnologias

### Permanent Magnet DC (PMDC) — modelo direto

- Saída direta DC (12V/24V).
- Simples, robusto.
- Eficiência média.

### Permanent Magnet Synchronous Generator (PMSG) — moderno

- Saída AC trifásica → retificada para DC.
- Maior eficiência em vento variável.
- Padrão em modelos modernos (Silentwind, Air Breeze).

## Reguladores de carga

### Shunt regulator (passivo — barato)

- Curto-circuita o gerador quando banco atinge V_max.
- Desperdiça energia em resistor.
- Simples + robusto.

### MPPT (Maximum Power Point Tracking — eficiente)

- Otimiza corrente × tensão para máximo rendimento em vento variável.
- 15-30% mais energia anual que shunt.
- Preferido em modernos.

### Linear regulator (legacy)

- Em desuso.

## Fabricantes e modelos dominantes

### Silentwind (Portugal — referência premium)

- **Silentwind 400W** — clássico, 12V/24V, PMSG + MPPT.
- **Silentwind Pro** — versão high-end.
- Diferenciais: silencioso, brake elétrico, ótima qualidade construtiva.

### Primus Wind Power (USA)

- **Air Breeze** — sucessor do Air X.
- **Air X / Air X Marine** — clássico (mas barulhento).
- **Air 40** — entry-level.

### Ampair (UK — legacy)

- **Ampair 100 / 300 / 600** — UK premium tradicional.

### Eclectic Energy (UK)

- **D400** — premium silencioso.
- **DUOGEN** — eólico + hídrico (water generator).

### Rutland (UK)

- **Rutland 504 / 914i / 1200** — mid-range.

### Aerogen (UK)

- **Aerogen 4F / 6** — entry-level.

> [!example] Comparação de preço Brasil 2024-2026 (importado)
> | Modelo | Potência | Preço (R$) |
> |--------|----------|------------|
> | Aerogen 4F | 80W | 4.500-7.500 |
> | Air Breeze | 200W | 5.500-9.000 |
> | Rutland 914i | 250W | 8.000-13.000 |
> | Silentwind 400W | 400W | 12.000-22.000 |
> | Ampair 300 | 300W | 9.000-16.000 |
> | Eclectic D400 | 400W | 14.000-25.000 |

## Instalação correta

### Localização

- **Mastro dedicado de proa ou popa** (não principal de vela).
- **Altura 3-5 m acima do deck** — vento mais limpo.
- **Distância ≥3 m de tripulação** — ruído + segurança.
- **Distância de antena VHF / GPS** ≥1 m — EMI.

### Cabeamento

- **AWG dimensionado** para corrente máxima + queda <3%.
- **Cabo blindado** em ambiente com EMI sensível.
- **Roteamento** longe de antenas RF.

### Aterramento e proteção

- **Bonding** torre-quilha (ABYC E-11.16 + IEC 61400-24).
- **Surge protector DC** entrada do regulador.
- **Fusível dedicado** entre eólico e regulador (ABYC E-11.5).
- **Brake elétrico acessível** em painel.

## Falhas e diagnóstico

| Falha | Causa | Solução |
|-------|-------|---------|
| Não gera | Brake travado / regulador falhou | Verificar brake; multímetro |
| Gera pouco | Cabo subdimensionado / orientação errada | Recalcular; verificar tail vane |
| Ruído excessivo | Mancal seco / desbalanceamento | Lubrificação; rebalanceamento |
| Pas trincadas | Impacto / UV | Substituir |
| Sobretensão no banco | Regulador defeituoso | Substituir regulador |
| Vibração violenta | Pas desbalanceadas | Inspecionar; substituir |

## Boas práticas

- **Modelo certificado** IEC 61400-2.
- **Localização correta** + altura.
- **Brake quando não em uso** (poupa mancal).
- **Inspeção semestral** + lubrificação anual.
- **Surge protection** mandatório.
- **Bonding** ao casco.
- **Combinar com solar** para redundância.
- **Documentar** modelo + curva de potência.
- **Backup** se geração crítica.

## Erros comuns

- "Eólico substitui solar." → Falso. Complementam.
- "Mais barato é igual." → Vida útil, ruído, performance variam dramaticamente.
- "Sem regulador funciona." → Banco queima.
- "Mastro principal serve." → Turbulência da vela mata performance.

## Glossário

- **Wind generator / aerogerador:** gerador eólico.
- **Wind turbine:** turbina eólica.
- **Cut-in:** vento mínimo para começar geração.
- **Rated:** potência nominal (em vento rated).
- **Cut-out:** vento máximo (proteção).
- **Brake:** freio elétrico.
- **PMSG:** Permanent Magnet Synchronous Generator.
- **PMDC:** Permanent Magnet DC.
- **MPPT:** Maximum Power Point Tracking.
- **Shunt regulator:** regulador por curto.
- **Tail vane / rabicho:** aleta de orientação.
- **Pa / blade:** pa do rotor.
- **Tower / torre / mastro:** estrutura mecânica.
- **Yaw:** rotação horizontal.
- **Pitch:** ângulo das pás.
- **Surge protector:** protetor de surto.
- **IEC 61400-2:** small wind turbines.
- **Vide [[Placa Solar (DC)]]** + [[Bancos de Bateria]] + [[Lei de Ohm e Cálculos Básicos]].

## Integração com outras notas

- [[Tipos de Bateria]] / [[Bancos de Bateria]] — banco a carregar.
- [[Placa Solar (DC)]] — fonte complementar.
- [[Carregador de Bateria (AC To DC)]] — alternativa AC.
- [[Inversora (DC To AC)]] — uso da energia.
- [[Cabeamento Náutico]] / [[Dimensionamento de Cabos DC — Cálculo Prático]].
- [[Fusíveis DC — Proteção Contra Sobrecorrente]] — proteção.
- [[Bonding — Sistema de Interligação de Massas]] — torre.
- [[Lei de Ohm e Cálculos Básicos]] — fundamentos.
- [[Estação de Vento - Anemômetro]] — medir vento.

## Perguntas que esta nota responde

- Aerogerador vale a pena no veleiro?
- Quanto produz um wind generator marine?
- Silentwind ou Air Breeze?
- Como instalar wind turbine no mastro?
- Aerogerador faz barulho à noite?
- Wind charger queima em rajada forte?
- Conexão eólico ao banco — regulador necessário?
- MPPT funciona com eólico?
- Manutenção do aerogerador?
- Eólico vs solar: qual produzir mais em barco?
- Cut-in / cut-out / rated: o que significa?
- IEC 61400-2 vale para barco?
