---
title: "MOC — Distribuicao Protecao e Aterramento"
note_type: "moc"
domain: "40_Distribuicao_Protecao_e_Aterramento"
status: "moc-curated-plus"
fase_6_reescrita: 110
reviewed_on: "2026-04-29"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
review_level: "moc-curated-plus"
seo_title: "MOC Distribuição Proteção Aterramento: barramento, disjuntor, fusível, DR/ELCI, bonding, isolador galvânico"
seo_description: "Hub do domínio 40: 18 notas premium-l3 sobre distribuição AC/DC (barramento, quadro, hotline, linhas), proteção (disjuntor, fusível ANL/MIDI, DR/ELCI/GFCI, contator, relé), comutação (chaves, divisores, seletoras), aterramento (bonding ABYC E-11.16) e isolador galvânico/transformador isolamento."
seo_keywords:
  - "barramento DC marine"
  - "disjuntor DC AC"
  - "fusível ANL MIDI"
  - "ELCI 30mA marine"
  - "bonding ABYC E-11.16"
  - "isolador galvânico"
  - "hotline always-on"
geo_queries:
  - "Como dimensionar disjuntor DC vs AC?"
  - "Quando usar fusível ANL ou MIDI?"
  - "ELCI vs GFCI vs DR — qual a diferença?"
  - "Bonding é o mesmo que aterramento?"
  - "Quando preciso de isolador galvânico?"
normas_citadas: []
related_notes:
  - "Atlas Técnico"
  - "Fundamentos da Elétrica Náutica"
  - "MOC — Energia e Conversao"
---

# MOC — Distribuicao Protecao e Aterramento

> [!abstract] Sobre este domínio
> Domínio **40_Distribuicao_Protecao_e_Aterramento** é o **núcleo de proteção e topologia elétrica**: distribuição AC/DC (barramento, quadro, hotline always-on, linhas leve/pesada), proteção contra sobrecorrente (disjuntor, fusível ANL/MIDI/ATC, contator, relé), comutação (chaves gerais, seletoras), proteção diferencial (DR/ELCI/GFCI), aterramento e bonding (ABYC E-11.16), isolação galvânica (corrosão de marina). **Vir aqui** para projetar quadro, dimensionar proteção, instalar bonding, escolher disjuntor DC × AC ou resolver corrosão por marina. **18 notas, todas Tier S/A premium-l3.**

> [!tip] Trilhas de leitura
> - **Iniciante:** [[Aterramento]] → [[Bonding — Sistema de Interligação de Massas]] → [[Disjuntores (DC) e (AC)]] → [[Fusíveis DC — Proteção Contra Sobrecorrente]]
> - **Projetando quadro:** [[Quadro Elétrico e Painel de Distribuição AC-DC]] → [[Barramento DC - Bus Bar - Distribuição DC]] → [[Disjuntores (DC) e (AC)]] + [[Fusíveis DC — Proteção Contra Sobrecorrente]] → [[Linha Leve (AC)]] + [[Linha Pesada (AC)]]
> - **Projetando proteção AC marina:** [[Proteção Dr]] → [[Isolador Galvânico - Transformador de Isolamento]] (cluster shore-power)
> - **Projetando comutação automática:** [[Divisores de Carga (DC)]] → [[Hotline (DC)]] → [[Chaves Seletoras (AC)]] → [[Contatores (AC)]] + [[Relés e Relés de Estado Sólido]]
> - **Cabos e conexões:** [[Cabeamento Náutico]] → [[Terminais Conectores e Emendas]]

## Notas por categoria

### Distribuição (5)

- [[Quadro Elétrico e Painel de Distribuição AC-DC]] — 🔧 A — quadro central, IEC 61439-1/-3, dimensionamento por porte
- [[Barramento DC - Bus Bar - Distribuição DC]] — 🔧 A — Blue Sea 2105/2126/2127/2128, ABYC E-11.4.7
- [[Hotline (DC)]] — 🔧 A — barramento always-on (bomba porão, alarme), backfeed protection
- [[Linha Leve (AC)]] — 🔧 A — circuitos AC tomadas + iluminação cabine
- [[Linha Pesada (AC)]] — ⚡ S — ar-condicionado, geladeira, dessalinizador (cargas AC alta corrente)

### Proteção contra sobrecorrente (3)

- [[Disjuntores (DC) e (AC)]] — ⚡ S — MCB, MCCB, IEC 60947-2, DC × AC critical (DC sem zero crossing)
- [[Fusíveis DC — Proteção Contra Sobrecorrente]] — ⚡ S — ANL, MIDI, ATC, MRBF, Class T (≤7" da bateria)
- [[Relés e Relés de Estado Sólido]] — 🔧 A — relé eletromecânico × SSR (TRIAC AC, MOSFET DC)

### Comutação (4)

- [[Chaves Gerais (DC)]] — 🔧 A — battery isolator (ON/OFF/BOTH/1+2), ABYC E-11.4.7
- [[Chaves Seletoras (AC)]] — 🔧 A — ATS (Automatic Transfer Switch), shore × gerador × inversor
- [[Contatores (AC)]] — 🔧 A — IEC 60947-4-1 categorias AC-1/AC-3, motor switching
- [[Divisores de Carga (DC)]] — 🔧 A — combinador (ACR/VSR), isolador (diodo/FET), DC-DC charger

### Proteção diferencial (1)

- [[Proteção Dr]] — ⚡ S — DR/RCD/RCBO/ELCI/GFCI/GFPE, IEC 61008/61009, ABYC E-11.11.1.5/.6

### Aterramento e isolação (3)

- [[Aterramento]] — ⚡ S — em barco "terra" não é estaca enterrada — casco/bonding/shore-PE
- [[Bonding — Sistema de Interligação de Massas]] — ⚡ S — ABYC E-11.16, AWG 8 verde-amarelo, Ag/AgCl reference
- [[Isolador Galvânico - Transformador de Isolamento]] — ⚡ S — corrosão de marina, isolação AC, ABYC A-28

### Cabeamento (2)

- [[Cabeamento Náutico]] — 🔧 A — UL 1426 BC5W2 + IEC 60092-353 + SAE J1127/J1128 + IEC 60228 classes 1-6
- [[Terminais Conectores e Emendas]] — 🔧 A — crimpagem calibrada (ABYC E-11.13), DIN 46228/46234, heat-shrink

## Cross-domain links

| Para | Vá para |
|------|---------|
| Banco de bateria a proteger | [[MOC — Baterias e Armazenamento]] |
| Shore-power + gerador + inversor | [[MOC — Energia e Conversao]] |
| Proteção contra raio | [[Iluminação de Emergência a Bordo]] (parcial) + ABYC TE-04 |
| Corrosão galvânica + ânodo | [[MOC — Seguranca e Corrosao]] |
| Quadro elétrico de gerador | [[Gerador (AC)]] (em domínio 30) |
| Cálculo de bitola por queda de tensão | [[Dimensionamento de Cabos DC — Cálculo Prático]] |
| Diagrama unifilar | [[Diagrama Unifilar — Documentação do Sistema Elétrico]] |

## Quick-reference — top 7 dúvidas

1. **Disjuntor DC × AC — qual usar?** → SEMPRE específico para DC em circuitos DC (DC sem zero crossing — arc não interrompe). [[Disjuntores (DC) e (AC)]].
2. **ELCI vs GFCI vs DR — qual?** → ELCI 30mA/100ms (marine, ABYC E-11.11.1.6), GFCI 5mA/25ms (proteção pessoa, áreas molhadas), DR 30mA (BR equiv ELCI). [[Proteção Dr]].
3. **Fusível ANL × MIDI × ATC?** → ANL para 100-500A (banco principal), MIDI 30-200A (sub-banco), ATC 1-40A (carga individual). [[Fusíveis DC — Proteção Contra Sobrecorrente]].
4. **Bonding × Aterramento?** → Bonding (ABYC E-11.16) interliga massas para anti-corrosão; Aterramento é a referência shore-PE/casco. [[Neutro, Negativo, Terra, PE, Bonding e DR — Diferenças Críticas]] (em domínio 10).
5. **Quando isolador galvânico?** → Quando barco fica em marina + casco metálico/composto + shore-PE compartilhado. [[Isolador Galvânico - Transformador de Isolamento]].
6. **Bomba de porão + chave geral OFF — backfeed?** → SIM, se ramal manual está fora da hotline. [[Hotline (DC)]] + DEC-37.
7. **AC-1 × AC-3 × AC-15 (categoria contator)?** → AC-1 carga não-indutiva, AC-3 motor partida normal, AC-15 controle. [[Contatores (AC)]].

## Glossário rápido (termos do domínio)

- **MCB:** Miniature Circuit Breaker.
- **MCCB:** Molded Case Circuit Breaker.
- **RCBO:** RCD with Built-in Overcurrent.
- **ELCI:** Equipment Leakage Circuit Interrupter (30mA marine).
- **GFCI:** Ground Fault Circuit Interrupter (5mA pessoa).
- **DR:** Dispositivo Diferencial Residual (BR).
- **GFPE:** Ground Fault Protection of Equipment.
- **ANL / MIDI / ATC / MEGA:** tipos de fusível DC marine.
- **MRBF:** Marine Rated Battery Fuse.
- **Class T:** fusível alta corrente DC (rápido).
- **ATS:** Automatic Transfer Switch.
- **ACR / VSR:** Automatic Charging Relay / Voltage Sensitive Relay.
- **SSR:** Solid-State Relay.
- **TRIAC:** Triode for Alternating Current (SSR AC).
- **MOSFET:** Metal-Oxide-Semiconductor FET (SSR DC).
- **Bonding:** ABYC E-11.16 — interligação massas.
- **PE:** Protective Earth (verde-amarelo).
- **Hotline / always-on:** barramento DC sem chave (bomba porão).
- **Backfeed:** corrente reversa pela rota errada.
- **Isolador galvânico:** rompe DC entre barco e shore-PE.
- **Transformador de isolamento:** isolação galvânica AC + ajuste tensão.
- **Categoria AC-1 a AC-8b:** classificação de uso de contator (IEC 60947-4-1).
- **Tinned copper:** cobre estanhado marine-grade.
- **AWG / mm²:** bitolas USA / IEC.

## Quando NÃO entrar aqui

- **Bateria + carregador** → [[MOC — Baterias e Armazenamento]]
- **Shore-power AC pedestal + gerador** → [[MOC — Energia e Conversao]]
- **Cálculo Lei de Ohm + dimensionamento** → [[MOC — Fundamentos e Projeto]]
- **Ânodo + correntes parasitas** → [[MOC — Seguranca e Corrosao]]
- **Manual OEM (Blue Sea, Marinco)** → [[MOC — Revisao Manual]]

## Perguntas que esta página responde

- Como dimensionar disjuntor DC vs AC?
- Quando usar fusível ANL ou MIDI?
- ELCI vs GFCI vs DR — qual a diferença?
- Bonding é o mesmo que aterramento?
- Quando preciso de isolador galvânico?
- Como projetar quadro de distribuição AC-DC?
- Categorias de contator (AC-1, AC-3, AC-15) — quando usar cada?
