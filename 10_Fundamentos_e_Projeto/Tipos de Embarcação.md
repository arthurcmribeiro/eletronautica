---
title: "Tipos de Embarcação"
note_type: "comparison"
domain: "10_Fundamentos_e_Projeto"
source_file: "TIPOS DE EMBARCAÇÃO d8b19734f7fb83f0a5280108ea7c19cc.md"
status: "premium-l3"
fase_6_reescrita: 97
reviewed_on: "2026-04-26"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://abycinc.org/standards/"
  - "https://www.imo.org/"
  - "https://www.iso.org/"
review_level: "engineering-curated"
aliases:
  - "TIPOS DE EMBARCAÇÃO"
  - "Vessel types"
  - "Boat types"
  - "Yacht categories"
  - "Classificação de embarcações"
seo_title: "Tipos de embarcação: lancha × veleiro × catamarã × mega-iate × charter × comercial — implicações elétricas, NORMAM-201/211, ISO 6185"
seo_description: "Guia técnico premium dos tipos de embarcação: classificação por uso (recreio × comercial × SOLAS), tamanho, casco (mono × catamarã × trimarã × planning × deslocamento), propulsão (motor × vela × híbrido × elétrico), implicações elétricas (tensão 12V/24V/48V/110V/220V/380V, banco bateria, gerador, inversor), DPC NORMAM-201/211, ABNT NBR 14728, RCD, SOLAS, ISO 6185, classification societies."
seo_keywords:
  - "tipos de embarcação"
  - "yacht categorias"
  - "lancha catamarã trimarã"
  - "mono casco vs catamarã"
  - "vela motor híbrido elétrico"
  - "NORMAM-211 NORMAM-201"
  - "RCD categorias A B C D"
  - "SOLAS GT"
  - "mega-iate LY3 PYC"
  - "ISO 6185 inflatable"
geo_queries:
  - "Quais são os tipos de embarcação no Brasil?"
  - "Diferença elétrica entre lancha e veleiro?"
  - "Catamarã ou monocasco para morar a bordo?"
  - "RCD categorias A/B/C/D — qual aplicar?"
  - "Mega-iate vs yacht: definição?"
  - "Tipos de propulsão: motor, vela, híbrido, elétrico?"
  - "Embarcação inflável é regulamentada?"
  - "Charter vs recreio: diferença regulatória?"
  - "Hovercraft, hidrofoil — categoria especial?"
  - "Embarcação tradicional × moderna — implicações elétricas?"
normas_citadas:
  - "ABYC (toda família — referência por categoria)"
  - "ISO 8666 (Small craft — Principal data)"
  - "ISO 6185-1/-2/-3/-4 (Inflatable boats)"
  - "ISO 12217-1/-2/-3 (Stability)"
  - "ISO 11591 (Field of vision from helm)"
  - "ISO 8849 (DC bilge pumps)"
  - "ISO 13297 (AC installations)"
  - "ISO 28848 (DC installations)"
  - "ISO 21487 (Fuel tanks)"
  - "ISO 19009 (Internal lighting)"
  - "ISO 8728 (Magnetic compass)"
  - "ISO 8729 (Radar reflectors)"
  - "IEC 60092 series (Electrical installations in ships)"
  - "IEC 60092-507 (Pleasure craft)"
  - "SOLAS Convention (≥500 GT international)"
  - "MARPOL Annex I-VI"
  - "COLREGS 1972"
  - "STCW Convention"
  - "MLC 2006"
  - "HSC Code (High-Speed Craft)"
  - "Polar Code"
  - "EU Directive 2013/53/EU (Recreational Craft Directive — RCD) — categorias A/B/C/D"
  - "EU Directive 2014/90/EU (MED)"
  - "ABYC E-11/H-2/H-22/H-29/A-7/A-30 (varies by category)"
  - "ABNT NBR 14728 (Embarcações de recreio)"
  - "ABNT NBR 5410"
  - "Lei 9.537/1997 (LESTA)"
  - "Lei 9.605/1998"
  - "Decreto 4.136/2002"
  - "DPC NORMAM-01/DPC (mar aberto)"
  - "DPC NORMAM-201/DPC e NORMAM-211/DPC (conforme enquadramento)"
  - "DPC NORMAM-08/DPC (tráfego e permanência)"
  - "DPC NORMAM-201/DPC (comerciais)"
  - "DPC NORMAM-211/DPC (esporte e recreio)"
  - "DPC NORMAM-04/DPC (Hidrografia)"
  - "DPC NORMAM-204/DPC (cartas eletrônicas)"
  - "DPC NORMAM-05/DPC (homologação)"
  - "USCG 33 CFR 183 (Pleasure craft)"
  - "USCG 46 CFR (Shipping commercial)"
  - "Classification: ABS, DNV, Lloyd's Register, RINA, Bureau Veritas, KR, ClassNK"
  - "LY3 (Large Yacht Code 3rd Edition)"
  - "PYC (Passenger Yacht Code)"
related_notes:
  - "Princípios Náuticos"
  - "Lei de Ohm e Cálculos Básicos"
  - "Projeto Elétrico de Embarcação — Passo a Passo"
  - "DC vs AC — Corrente Contínua e Alternada"
  - "Diagrama Unifilar — Documentação do Sistema Elétrico"
  - "Dimensionamento de Banco de Baterias — Cálculo de Autonomia"
  - "Dimensionamento de Cabos DC — Cálculo Prático"
  - "Bancos de Bateria"
  - "Inversora (DC To AC)"
  - "Gerador (DC)"
  - "Placa Solar (DC)"
  - "Eólico (DC)"
  - "CAIS (Pier) (AC)"
  - "Normas e Regulamentações — Abyc Iso e Brasil"
---

# Tipos de Embarcação

> [!abstract] Resumo técnico
> Esta nota classifica **embarcações** por **uso (recreio × comercial × SOLAS × militar)**, **tamanho (LOA / GT)**, **casco (monocasco × multicasco × planning × deslocamento)**, **propulsão (motor × vela × híbrido × full electric)**, **material do casco (fibra × alumínio × aço × madeira × inox)** e **arquitetura elétrica resultante (12V/24V/48V/110V/220V/380V × banco × gerador × shore-power)**. **A taxonomia define o quadro normativo aplicável** (vide [[Princípios Náuticos]] e [[Normas e Regulamentações — Abyc Iso e Brasil]]) e as **decisões técnicas elétricas críticas**: tensão DC predominante, capacidade de banco, presença de inversor, gerador, shore-power, isolador galvânico, complexidade do sistema. **No Brasil**: NORMAM-211 (recreio amador <12m), NORMAM-201 (comercial / charter), NORMAM-08 (tráfego/permanência), classification society opcional acima de certas faixas. **Na UE**: RCD 2013/53/EU define **categorias A (offshore — vento até 8 Bft, ondas até 4 m), B (high seas — vento até 8 Bft, ondas até 4 m), C (inshore — vento até 6 Bft, ondas até 2 m), D (sheltered — vento até 4 Bft, ondas até 0,3 m)**. **SOLAS** aplica-se a **navios ≥500 GT em viagem internacional**. Mega-iates (>24 m) frequentemente seguem **LY3 (Large Yacht Code)** e/ou **PYC (Passenger Yacht Code)**.

> [!tldr] TL;DR — 9 regras inegociáveis
> 1. **Identificar o tipo da embarcação é o primeiro passo de qualquer projeto elétrico.** Determina: tensão DC predominante, capacidade do banco, presença de inversor/gerador/shore-power, normas aplicáveis, redundância exigida, complexidade do diagrama unifilar.
> 2. **Recreio amador BR <12m:** ABNT NBR 14728 + NORMAM-211 + ABYC + ISO recomendado. **Mais de 12m:** classification society opcional mas recomendada (ABS/DNV/RINA/BV).
> 3. **Charter / pesca esportiva BR (com fins lucrativos):** automaticamente comercial → NORMAM-201 + LESTA Lei 9.537/1997 + classification society.
> 4. **SOLAS ≥500 GT viagem internacional:** Convention SOLAS + IMO MSC + classification society + STCW + MLC obrigatórios.
> 5. **Mega-iate (>24 m):** RCD em UE + LY3/PYC voluntário + classification society quase sempre.
> 6. **RCD categorias A/B/C/D:** define limites operacionais (vento + onda) e exigências de equipamento. Categoria afeta diretamente: equipamento de salvamento, comunicação, navegação obrigatórios.
> 7. **Catamarã ≠ monocasco em arquitetura elétrica:** dois cascos = dois compartimentos elétricos com bonding cruzado + cabling pela ponte; redundância natural mas complexidade dupla.
> 8. **Veleiro (vela + motor auxiliar) ≠ lancha (motor predominante):** veleiro tem mastro (raio, anemômetro, luz tope, antena VHF), banco menor mas autonomia maior; lancha tem alta corrente de partida + mais cargas DC.
> 9. **Embarcação elétrica (full electric / híbrida)** é categoria emergente: banco LiFePO4 alto voltage (48V/96V/144V/400V+), inversor multi-string, charging via shore + solar + regen, BMS sofisticado. Padrões em evolução (ABYC E-13 hybrid/electric propulsion).

> [!danger] Cenários de risco
> - **Aplicar norma errada por classificar mal o uso:** charter operando como "amador" → fiscal apreende + multa + embarcação parada. **Prevenção:** consultar regulação local (Marinha BR) antes de qualquer operação comercial.
> - **Operar fora da categoria RCD:** barco categoria C (inshore) navegando offshore em vento 8 Bft → afundamento por design não preparado. **Prevenção:** respeitar limites RCD; consultar manual.
> - **Subdimensionar elétrica em mega-iate** (visto como yacht recreativo grande): consumo real 80-200% maior que projetado → banco insuficiente → motor para → SAR offshore. **Prevenção:** consultoria com naval architect; classification society survey.
> - **Mistura de tecnologia em catamarã:** banco de bateria diferente em cada casco + sem balanceamento → desbalanceamento crônico → vida útil curta. **Prevenção:** banco coordenado com BMS unificado.
> - **Veleiro sem proteção contra raio em mastro alto:** raio incide → eletrônica destruída + tripulação em risco. **Prevenção:** ABYC TE-04 + ABYC A-31 lightning protection; bonding mastro-quilha.
> - **Hovercraft / hidrofoil tratado como lancha** convencional: arquitetura elétrica + dinâmica diferente; aplicação errada de norma. **Prevenção:** consultoria com fabricante; HSC Code se aplicável.
> - **Embarcação elétrica com BMS inadequado:** banco LiFePO4 sem proteção térmica → thermal runaway → fogo em mar aberto. **Prevenção:** BMS certificado + ABYC E-13 emergente; isolação adequada.
> - **Migração de regulação por mudança de uso:** yacht amador convertido em charter sem atualizar normas → multa + apreensão + responsabilidade civil. **Prevenção:** notificar Marinha; reclassificar.
> - **Inflatable / RIB com elétrica improvisada:** ISO 6185 + ABYC limitam capacidade elétrica em casco flexível; instalação errada compromete estrutura. **Prevenção:** seguir manual + ISO 6185; consultar fabricante.
> - **Embarcação tradicional (madeira) com elétrica moderna sem cuidado:** corrente parasita + casco molhado + bonding inadequado → corrosão acelerada + risco choque. **Prevenção:** isolador galvânico + bonding rigoroso + inspeção semestral.

## Classificação por uso (regulatório)

| Categoria | Definição BR | Regulação BR | Regulação Internacional |
|-----------|-------------|--------------|-------------------------|
| **Embarcação miúda** | <5 m, sem cabine | NORMAM-08 | RCD D (sheltered) |
| **Recreio amador** | <12 m, sem fins lucrativos | NORMAM-211 + NBR 14728 | RCD A/B/C/D + ISO 6185 + ABYC |
| **Recreio amador grande** | >12 m amador | NORMAM-211 + class. opcional | RCD + LY3 voluntário + class. |
| **Charter / esporte+lucro** | Fins lucrativos pequeno | NORMAM-201 + LESTA Lei 9.537 | + classification |
| **Comercial pequena** | <50 GT | NORMAM-201 | + classification |
| **Comercial maior** | 50-500 GT | NORMAM-201 + class. soc. | + classification + parcial SOLAS |
| **SOLAS** | ≥500 GT internacional | + SOLAS + STCW + MLC | + classification + IMO |
| **Mega-iate** | >24 m recreio | RCD + LY3 + class. | LY3 + PYC + classification |
| **HSC** | High-Speed Craft | HSC Code se aplicável | HSC Code (IMO) |
| **Militar** | Defesa | Regulação militar | — |

## Classificação por casco

### Monocasco (mono-hull)

```
              ┌─────────────────────┐
              │                     │
              │      ┌────┐         │
              │      │    │         │
              │     /│    │\        │
              │    / │ │  │ \       │
              │   /__│_│__│__\      │
              │       Casco         │
              └─────────────────────┘
```

- **Aplicação:** maioria das lanchas + veleiros + barcos de pesca.
- **Vantagens:** simples, barato, manobrável, comportamento clássico.
- **Desvantagens:** rolagem em mar agitado; espaço interno menor.

### Catamarã (twin-hull)

```
              ┌─────┐         ┌─────┐
              │     │  ponte  │     │
              │ casco-1   ╱╲   casco-2
              │  port  ╱    ╲  starboard │
              │     │ ╱      ╲ │     │
              └─────┘          └─────┘
```

- **Aplicação:** charter, performance vela, comercial.
- **Vantagens:** estabilidade, espaço, eficiência hidrodinâmica.
- **Desvantagens:** complexidade dupla (eletricamente — bonding cruzado pela ponte).

### Trimarã (3 hulls)

- Aplicação: vela performance / regata.
- Características: estabilidade do mono + velocidade do multicasco.

### Planning vs deslocamento

| Tipo | Velocidade típica | Casco |
|------|--------------------|-------|
| **Deslocamento** | 6-12 nós | Casco "fala" pela água — vela, trawler |
| **Semi-planning** | 12-25 nós | Híbrido |
| **Planning** | 25-100+ nós | Casco "voa" sobre água — lancha, performance |

## Classificação por propulsão

### Motor (combustão interna)

| Tipo | Combustível | Aplicação |
|------|-------------|-----------|
| **Diesel inboard** | Diesel | Yacht médio-grande, deslocamento |
| **Gasolina inboard/outboard** | Gasolina | Lanchas pequenas-médias |
| **Outboard** | Gasolina (4T predominante) | Lanchas pequenas |
| **Stern-drive (sail-drive)** | Diesel ou gasolina | Híbrido inboard + outboard |
| **IPS (Pod Drive)** | Diesel | Yacht médio-grande moderno |
| **Jet drive** | Gasolina ou diesel | Lanchas, jet skis |

### Vela

| Tipo | Características |
|------|------------------|
| **Sloop** | 1 mastro, jib + main |
| **Cutter** | 1 mastro, jib + staysail + main |
| **Ketch** | 2 mastros (mizzen menor que main) |
| **Yawl** | 2 mastros (mizzen mais à popa) |
| **Schooner** | 2+ mastros (foremast menor que mainmast) |

### Híbrido

| Tipo | Configuração |
|------|---------------|
| **Diesel-electric** | Motor diesel gera para motor elétrico (cargo, mega-iate) |
| **Parallel hybrid** | Diesel + motor elétrico em paralelo (Vetus-Maxwell, Volvo Penta IPS) |
| **Series hybrid** | Diesel ↔ banco grande ↔ motor elétrico |

### Full electric (emergente)

- Banco LiFePO4 grande (50-500 kWh).
- Motor elétrico (Torqeedo, Bellmarine, Oceanvolt).
- Charging shore + solar + regeneração.
- Padrão em evolução (ABYC E-13).

## Classificação por material do casco

| Material | Aplicação típica | Implicações elétricas |
|----------|-------------------|------------------------|
| **Fibra de vidro (GRP)** | Maioria recreio | Bonding em massa metálica selecionada |
| **Alumínio** | Workboats, performance | Bonding crítico (galvânica + eletrólise alta) |
| **Aço** | Comercial, expedition | Casco é "terra natural"; corrosão monitorada |
| **Madeira** | Tradicional | Bonding via cintas metálicas; vulnerável |
| **Inox** | Niche | Resistente a corrosão; bonding via fixação |
| **Composite avançado (carbono/Kevlar)** | Performance/regata | Não-condutor; bonding em metálicos selecionados |

## Implicações elétricas por tipo

### Lancha recreativa 25-40 ft (motor planning)

| Item | Configuração típica |
|------|---------------------|
| Tensão DC | 12V (alguns 24V em maiores) |
| Banco bateria | 1 partida + 1 serviço, 100-200 Ah cada |
| Inversor | 1000-2000W onda senoidal |
| Gerador | Não (em iate >35 ft sim, 5-12 kW) |
| Shore power | Sim, 110/220V single-phase |
| Cargas principais | Motor partida (alta corrente DC), trim/tab, bombas, eletrônica, iluminação |

### Veleiro recreativo 30-45 ft

| Item | Configuração típica |
|------|---------------------|
| Tensão DC | 12V (alguns 24V) |
| Banco bateria | 1 partida + 1-2 serviço, 200-400 Ah |
| Inversor | 1500-3000W |
| Gerador | Em yacht maior (8-12 kW) |
| Shore power | Sim |
| Cargas principais | Anchor windlass alta DC, autopilot, instrumentos, luzes nav, refrigeração |
| Geração alternativa | Solar 200-1000W; eólico 200-400W |

### Mega-iate 24+ m (motor)

| Item | Configuração típica |
|------|---------------------|
| Tensão DC | 24V/48V/110V mistos |
| Tensão AC | 220/380V tri-phase + 110V single-phase |
| Banco bateria | 1.000-10.000 Ah |
| Inversor | 5-50 kW |
| Gerador | 2-3 unidades 30-500 kW |
| Shore power | 200-400A 3-phase |
| Sistema | Digital switching CZone/EmpirBus completo |

### Catamarã charter

| Item | Configuração típica |
|------|---------------------|
| Tensão DC | 12V ou 24V (banco grande para AC + ar-condicionado) |
| Banco bateria | 600-1200 Ah por casco × 2 (paralelo via ponte) |
| Inversor | 3000-5000W |
| Solar | Painéis no teto (1-3 kW) |
| Cargas principais | Ar-condicionado AC, refrigeração, dessalinizador, autopilot |

### Embarcação elétrica (full electric)

| Item | Configuração típica |
|------|---------------------|
| Tensão DC bateria | 48V (small) / 96V (medium) / 400V+ (large) |
| Banco LiFePO4 | 50-500 kWh |
| Motor | Torqeedo / Bellmarine / Oceanvolt |
| Charging | Shore + solar + regen |
| BMS | Crítico (multi-string com balanceamento) |

## RCD categorias (UE)

| Categoria | Vento (Bft) | Ondas (m) | Aplicação |
|-----------|-------------|-----------|-----------|
| **A — Ocean** | até 8 Bft | até 4 m | Offshore navegação irrestrita |
| **B — Offshore** | até 8 Bft | até 4 m | Quase como A, mais restrição design |
| **C — Inshore** | até 6 Bft | até 2 m | Costeiro |
| **D — Sheltered** | até 4 Bft | até 0,3 m | Lago, rio, bay calmo |

## Classification societies (recapitulação)

| Society | País | Foco |
|---------|------|------|
| **ABS** | USA | Cargo + offshore + yacht |
| **DNV** | Noruega/Alemanha | Multi |
| **Lloyd's Register** | UK | Multi |
| **RINA** | Itália | Multi + yacht |
| **Bureau Veritas** | França | Multi + yacht |
| **ClassNK** | Japão | Cargo Asia |
| **KR** | Coreia | Cargo Asia |

## Boas práticas

- **Identificar tipo + uso ANTES de projetar.**
- **Consultar regulação local** (NORMAM no BR; USCG nos EUA; RCD na UE).
- **Classification society** quando aplicável (compulsório SOLAS; voluntário em recreio premium).
- **Documentar reclassificação** se uso muda (recreio → charter).
- **Margens** de design generosas em embarcação grande / offshore.
- **Redundância** em embarcação offshore irrestrita.

## Erros comuns

- "Recreio não precisa de classification." → Em mega-iate >24 m, é prática + alguns países exigem.
- "Categoria RCD é decoração." → É limite operacional e equipment exigido.
- "Catamarã = 2 monocascos paralelos." → Falso. Bonding cruzado + cabling pela ponte é essencial.
- "Embarcação elétrica é só trocar motor." → BMS + carregador + isolação + integração elétrica complexa.
- "Charter pode ser amador." → Falso. Fins lucrativos = comercial obrigatoriamente.

## Glossário

- **Embarcação miúda:** <5 m sem cabine.
- **Recreio amador:** lazer sem fins lucrativos.
- **Comercial:** fins lucrativos.
- **SOLAS:** ≥500 GT viagem internacional.
- **GT (Gross Tonnage):** medida de volume.
- **LOA (Length Over All):** comprimento total.
- **LWL (Load Water Line):** comprimento na linha d'água.
- **Boca:** largura máxima.
- **Calado:** profundidade.
- **Casco:** estrutura.
- **Mono-hull / catamarã / trimarã:** 1/2/3 cascos.
- **Planning vs deslocamento:** comportamento hidrodinâmico.
- **Inboard / outboard:** motor interno / externo.
- **Stern-drive (sail-drive):** propulsão híbrida.
- **IPS (Pod Drive):** Volvo Penta integrated propulsion.
- **Jet drive:** propulsão por jato d'água.
- **Sloop / cutter / ketch / yawl / schooner:** configurações de vela.
- **RIB (Rigid Inflatable Boat):** semi-rígido inflável.
- **HSC:** High-Speed Craft.
- **Hovercraft / hidrofoil:** veículos especiais.
- **GRP / FRP (Glass / Fiber Reinforced Plastic):** fibra de vidro.
- **NORMAM-201/211:** comerciais / recreio BR.
- **LESTA Lei 9.537/1997:** Lei Tráfego Aquaviário BR.
- **RCD 2013/53/EU:** Recreational Craft Directive UE — categorias A/B/C/D.
- **MED 2014/90/EU:** Marine Equipment Directive.
- **LY3 (Large Yacht Code 3):** padrão para mega-iates >24 m.
- **PYC (Passenger Yacht Code):** padrão para charter passageiros.
- **SOLAS:** Safety of Life at Sea.
- **MARPOL:** Marine Pollution.
- **STCW:** Standards Training Certification Watchkeeping.
- **MLC 2006:** Maritime Labour Convention.
- **HSC Code:** High-Speed Craft Code.
- **Polar Code:** IMO MEPC.264 + MSC.385.
- **ABYC:** American Boat and Yacht Council.
- **Classification society:** ABS, DNV, Lloyd's, RINA, BV, etc.
- **Bft (Beaufort):** escala de vento.
- **Vide [[Princípios Náuticos]] + [[Normas e Regulamentações — Abyc Iso e Brasil]]** — quadro normativo.

## Integração com outras notas

- [[Princípios Náuticos]] — fundamentos.
- [[Lei de Ohm e Cálculos Básicos]] — cálculo elétrico.
- [[Projeto Elétrico de Embarcação — Passo a Passo]] — projeto.
- [[DC vs AC — Corrente Contínua e Alternada]].
- [[Diagrama Unifilar — Documentação do Sistema Elétrico]].
- [[Dimensionamento de Banco de Baterias — Cálculo de Autonomia]].
- [[Dimensionamento de Cabos DC — Cálculo Prático]].
- [[Bancos de Bateria]] — escolha por tipo.
- [[Inversora (DC To AC)]] — dimensionamento.
- [[Gerador (DC)]] — quando incluir.
- [[Placa Solar (DC)]] / [[Eólico (DC)]] — geração alternativa.
- [[CAIS (Pier) (AC)]] — shore-power.
- [[Normas e Regulamentações — Abyc Iso e Brasil]].

## Perguntas que esta nota responde

- Quais são os tipos de embarcação no Brasil?
- Diferença elétrica entre lancha e veleiro?
- Catamarã ou monocasco para morar a bordo?
- RCD categorias A/B/C/D — qual aplicar?
- Mega-iate vs yacht: definição?
- Tipos de propulsão: motor, vela, híbrido, elétrico?
- Embarcação inflável é regulamentada?
- Charter vs recreio: diferença regulatória?
- Hovercraft, hidrofoil — categoria especial?
- Embarcação tradicional × moderna — implicações elétricas?
- Quando preciso de classification society?
- Como reclassificar embarcação que mudou de uso?
