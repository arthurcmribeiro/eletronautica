---
title: "MOC — Energia e Conversao"
note_type: "moc"
domain: "30_Energia_e_Conversao"
status: "moc-curated-plus"
fase_6_reescrita: 109
reviewed_on: "2026-04-29"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
review_level: "moc-curated-plus"
seo_title: "MOC Energia e Conversão: shore-power, alternador, inversor, gerador, solar, eólica, transformador"
seo_description: "Hub do domínio 30: 11 notas premium-l3 sobre fontes de energia (shore-power CAIS, gerador AC/DC, alternador DC, painel solar, aerogerador), conversão (inversor DC-AC, transformador bivolt/entrada), arranque e carregador para tender/jet ski."
seo_keywords:
  - "shore power náutico"
  - "alternador DC marine"
  - "inversor pure sine wave"
  - "gerador onan marine"
  - "painel solar barco"
  - "aerogerador silentwind"
geo_queries:
  - "Como dimensionar shore-power para minha embarcação?"
  - "Gerador AC ou DC: qual escolher?"
  - "Solar + eólica + alternador: como integrar?"
  - "Inversor pure sine wave vs modified: diferença?"
  - "Como ligar tender elétrico à fonte do barco?"
normas_citadas: []
related_notes:
  - "Atlas Técnico"
  - "Fundamentos da Elétrica Náutica"
  - "MOC — Baterias e Armazenamento"
---

# MOC — Energia e Conversao

> [!abstract] Sobre este domínio
> Domínio **30_Energia_e_Conversao** cobre **fontes e conversão de energia** a bordo: shore-power AC (interface com marina), geração local (alternador DC do motor, gerador AC/DC dedicado, painel solar, aerogerador), conversão entre níveis (inversor DC-AC, transformador bivolt/entrada) e sistemas auxiliares (arranque do motor, carregador para tender elétrico/jet ski). **Vir aqui** para escolher fonte, dimensionar gerador, integrar solar/eólica, projetar shore-power ou retrofitar inversor. **11 notas, mistura Tier S/A premium-l3.**

> [!tip] Trilhas de leitura
> - **Iniciante:** [[CAIS (Pier) (AC)]] → [[Alternador (DC)]] → [[Inversora (DC To AC)]]
> - **Projetando off-grid:** [[Placa Solar (DC)]] → [[Eólico (DC)]] → [[Inversora (DC To AC)]] (banco em [[MOC — Baterias e Armazenamento]])
> - **Projetando shore-power:** [[CAIS (Pier) (AC)]] → [[Transformador Entrada]] → [[Transformador Bivolt]] → [[Isolador Galvânico - Transformador de Isolamento]] (em domínio 40)
> - **Diagnosticando partida:** [[Arranque]] → [[Alternador (DC)]]
> - **Mega-iate / charter:** [[Gerador (AC)]] + [[Gerador (DC)]] → [[Inversora (DC To AC)]] + [[Transformador Entrada]]

## Notas por categoria

### Shore-power e interface com marina (3)

- [[CAIS (Pier) (AC)]] — ⚡ S — interface marina, NEC Article 555, IEC 60364-7-709, topologia BR
- [[Transformador Entrada]] — ⚡ S — entrada AC isolada/regulada, mega-iate
- [[Transformador Bivolt]] — ⚡ S — adaptação 110V↔220V, multi-jurisdição

### Geração local — DC (4)

- [[Alternador (DC)]] — ⚡ S — gerador DC do motor de combustão (12V/24V/48V)
- [[Gerador (DC)]] — ⚡ S — gerador DC dedicado (Onan/Cummins, mega-iate)
- [[Placa Solar (DC)]] — ⚡ S — painel fotovoltaico, MPPT, dimensionamento, PWM × MPPT
- [[Eólico (DC)]] — 🔧 A — aerogerador marine (Silentwind, Air Breeze), IEC 61400-2

### Geração local — AC (1)

- [[Gerador (AC)]] — ⚡ S — gerador AC dedicado (Onan, Kohler, Cummins), 110V/220V/380V

### Conversão (1)

- [[Inversora (DC To AC)]] — ⚡ S — DC→AC, pure sine wave × modified, fator de potência, dimensionamento VA

### Sistemas auxiliares (2)

- [[Arranque]] — 🔧 A — motor de partida, ignition protection (ISO 8846, gasolina), CCA/MCA, queda <5%
- [[Carregador Elétrico para Tender e Jet Ski]] — 🔧 A — onboard charger AC/DC para tender (LFP/AGM) + PWC (12V)

## Cross-domain links

| Para | Vá para |
|------|---------|
| Banco a carregar | [[MOC — Baterias e Armazenamento]] |
| Shore-power inlet + isolador galvânico | [[Isolador Galvânico - Transformador de Isolamento]] (em [[MOC — Distribuicao Protecao e Aterramento]]) |
| Disjuntor / fusível dedicado | [[MOC — Distribuicao Protecao e Aterramento]] |
| Cabeamento (AWG/mm² + queda) | [[Cabeamento Náutico]] + [[Dimensionamento de Cabos DC — Cálculo Prático]] |
| Bonding do gerador / inversor | [[Bonding — Sistema de Interligação de Massas]] |
| Diagrama unifilar do sistema | [[Diagrama Unifilar — Documentação do Sistema Elétrico]] |
| Manual OEM (Onan, Volvo, Mercury) | [[MOC — Revisao Manual]] |

## Quick-reference — top 5 dúvidas

1. **Quanto consome um inversor de 3000W?** → 250-300A em 12V (com PF 0.9 + perda 10%). [[Inversora (DC To AC)]] (dimensionar VA não W).
2. **Solar + eólica + alternador no mesmo banco?** → SIM, se cada fonte tiver controlador dedicado + bateria comum compatível. [[Placa Solar (DC)]] + [[Eólico (DC)]] + [[Alternador (DC)]].
3. **Pure sine wave × modified — qual?** → Pure sine para eletrônica sensível, modified só para cargas resistivas (em desuso). [[Inversora (DC To AC)]].
4. **Gerador AC ou DC?** → AC para mega-iate com cargas AC grandes (ar-condicionado), DC para charge banco em yacht médio. [[Gerador (AC)]] vs [[Gerador (DC)]].
5. **Shore-power 110V × 220V no Brasil?** → Marinas são heterogêneas — pedestal pode ser 127V, 220V fase-fase ou 220V fase-neutro. [[CAIS (Pier) (AC)]] + [[Isolador Galvânico - Transformador de Isolamento]].

## Glossário rápido (termos do domínio)

- **Shore-power:** alimentação AC do pedestal de marina.
- **Inlet:** conector de entrada AC no casco (Marinco, Hubbell, Furrion).
- **Pedestal:** poste da marina com tomada AC + breakers.
- **Pure sine wave:** onda senoidal verdadeira (inversor premium).
- **Modified sine wave:** onda quasi-senoidal (inversor legacy, em desuso).
- **VA × W:** potência aparente × ativa (inversor dimensionado em VA).
- **PF (Power Factor):** cos φ (carga indutiva 0.7-0.9).
- **CCA / MCA:** Cold / Marine Cranking Amps (SAE J537).
- **MPPT:** Maximum Power Point Tracking (otimização de painel solar).
- **PWM:** Pulse Width Modulation (controlador solar simples).
- **Cut-in / Rated / Cut-out:** vento mínimo / nominal / máximo (aerogerador).
- **Isolador galvânico:** rompe corrente DC entre barco e marina (corrosão).
- **Transformador de isolamento:** isola galvanicamente AC + ajusta tensão.
- **PMSG:** Permanent Magnet Synchronous Generator (aerogerador moderno).
- **Solenoide:** relé alta corrente + atuador mecânico do starter.
- **NMMA TC-W3 / FC-W:** óleo 2T / 4T outboard.
- **NEC Article 555:** marinas USA.
- **IEC 60364-7-709:** marinas internacional.

## Quando NÃO entrar aqui

- **Tipo de bateria a usar** → [[MOC — Baterias e Armazenamento]]
- **BMV / monitor de banco** → [[MOC — Baterias e Armazenamento]]
- **Disjuntor + fusível do gerador** → [[MOC — Distribuicao Protecao e Aterramento]]
- **Bonding e isolador galvânico** → [[MOC — Distribuicao Protecao e Aterramento]]
- **Cabos DC / AC** → [[Cabeamento Náutico]] (em domínio 40)

## Perguntas que esta página responde

- Como dimensionar shore-power para minha embarcação?
- Gerador AC ou DC: qual escolher?
- Solar + eólica + alternador: como integrar?
- Inversor pure sine wave vs modified: diferença?
- Como ligar tender elétrico à fonte do barco?
- Quando preciso de transformador de isolamento?
- Como dimensionar VA do inversor?
