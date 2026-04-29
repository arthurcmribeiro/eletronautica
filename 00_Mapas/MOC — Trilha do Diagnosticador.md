---
title: "MOC — Trilha do Diagnosticador"
note_type: "moc"
domain: "00_Mapas"
status: "moc-curated-plus"
fase_6_reescrita: 138
reviewed_on: "2026-04-29"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
review_level: "moc-curated-plus"
aliases:
  - "Trilha de troubleshooting"
  - "Workflow de diagnóstico elétrico náutico"
seo_title: "Trilha do diagnosticador: método estruturado de troubleshooting elétrico náutico"
seo_description: "Trilha de diagnóstico elétrico náutico em 5 etapas: levantamento → medição → árvore de decisão → causa raiz → correção. Multímetro, alicate, megger, termovisor + falhas mais comuns por domínio + checklist pós-correção."
seo_keywords:
  - "troubleshooting elétrico náutico"
  - "diagnóstico falha barco"
  - "Fluke 87V marine"
  - "alicate amperímetro DC"
  - "megger isolação cabo"
geo_queries:
  - "Como diagnosticar falha elétrica em embarcação?"
  - "Por que multímetro mostra leitura errada?"
  - "Como achar curto-circuito no barco?"
  - "O que é stray current e como diagnosticar?"
normas_citadas: []
related_notes:
  - "Atlas Técnico"
  - "Fundamentos da Elétrica Náutica"
  - "MOC — Trilha do Iniciante"
  - "MOC — Trilha do Projetista"
  - "MOC — Diagnóstico e Manutenção"
---

# MOC — Trilha do Diagnosticador

> [!abstract] Para quem é esta trilha
> Para quem **vai resolver problema agora** (em campo) ou **investigar comportamento anômalo** sistematicamente. Pressuposto: você tem ferramenta básica (multímetro True RMS + alicate AC+DC) e fundamentos da [[MOC — Trilha do Iniciante]]. Aqui o **método estruturado em 5 etapas**, com referência rápida por sintoma, ferramentas e checklist pós-correção. Tempo médio por diagnóstico: **30-90 min** (não conta o reparo).

> [!tip] Quando NÃO seguir esta trilha
> - Você quer **prevenir** problema → [[Manutenção Preventiva Elétrica — Checklist]] direto.
> - Você está **projetando do zero** → [[MOC — Trilha do Projetista]].
> - Você é **iniciante** → [[MOC — Trilha do Iniciante]] primeiro.

## Etapa 1 — Levantamento estruturado (10-20 min)

Antes de medir, entender o sintoma e o histórico.

| # | Nota | Por que ler |
|---|------|-------------|
| 1 | [[Troubleshooting — Diagnóstico de Falhas Elétricas]] | ⚡ S — método estruturado em 6 passos |
| 2 | [[Manutenção Preventiva Elétrica — Checklist]] | ⚡ S — última manutenção / mudanças recentes |

**Perguntas chave:**
- Sintoma exato (não dispara / dispara constantemente / leitura errática)?
- Quando começou (após instalação? mudança de carga? tempestade?)?
- Histórico (manutenção, modificação, surto)?
- Embarcação em aço/alumínio? (afeta diagnóstico de bonding/corrosão)

## Etapa 2 — Medição com ferramenta correta (15-30 min)

Sem dado correto, diagnóstico é chute.

| # | Nota | Tier | Quando usar |
|---|------|------|-------------|
| 3 | [[Multímetro e Instrumentos de Medição]] | ⚡ S | Sempre — primeira ferramenta |
| 4 | [[Voltímetro - Amperímetro (DC e AC)]] | ⚡ S | Tensão sob carga + corrente |
| 5 | [[Ferramentas do Eletricista Náutico]] | 🔧 A | Toolkit completo (Fluke + Hioki + termovisor + megger) |

**Categorias de medição (IEC 61010):**
- **Cat I:** circuito eletrônico interno.
- **Cat II:** ponto de uso (tomada).
- **Cat III:** distribuição (quadro principal).
- **Cat IV:** origem da instalação (shore-power inlet).

**Multímetro errado em Cat errado** = arc flash + queimadura grave.

## Etapa 3 — Árvores de decisão por sintoma

### Sintoma: motor não dá partida

```
Tensão banco repouso?
├── <12.4V → bateria descarregada → carregar / substituir
└── ≥12.4V → tentar partida com multímetro
              Tensão durante crank?
              ├── <10V → cabo subdimensionado OU bateria fraca em carga
              │         → [[Arranque]] + [[Cabeamento Náutico]] + [[Dimensionamento de Cabos DC — Cálculo Prático]]
              └── ≥10V → starter OK
                         "Click" mas não gira?
                         ├── Solenoide travado → substituir solenoide
                         └── Pinion não engata → mecânico (revisar starter)
```

### Sintoma: choque ao tocar casco metálico

```
Casco molhado?
├── Sim → fuga AC para casco
│         ├── ELCI dispara? Não → ELCI ausente ou defeituoso → [[Proteção Dr]]
│         └── ELCI dispara? Sim → identificar circuito (isolar 1 a 1)
│                                  → [[Correntes Parasitas — Stray Currents]]
│                                  → ABYC E-11.16 [[Bonding — Sistema de Interligação de Massas]]
└── Não → corrente parasita DC ou estática
          → measurement Ag/AgCl reference electrode
          → [[Eletrólise]] + [[Anôdo]]
```

### Sintoma: ânodo consumido em < 6 meses

```
Casco metálico ou fibra?
├── Fibra → bonding incorreto (extras "aterrados") OU isolador galvânico ausente
│           → [[Isolador Galvânico - Transformador de Isolamento]]
│           → [[Bonding — Sistema de Interligação de Massas]]
└── Metálico/Al → corrente parasita DC ou marina vizinha "vampira"
                   → [[Correntes Parasitas — Stray Currents]]
                   → Megger isolação cabos vs casco (>100 MΩ)
```

### Sintoma: leitura de heading "caça" no piloto auto

```
Mar agitado?
├── Sim → fluxgate sem AHRS → upgrade
│         → [[Bússola Eletrônica (Compass - HDG Sensor)]]
│         → [[Piloto Automático]]
└── Não → calibração não feita / interferência magnética próxima
          → swinging compass + afastar metais/alto-falantes
          → ISO 22090-2 §6.5
```

### Sintoma: VHF/GPS ruído ao ligar luz/inversor/algo

```
EMI confirmada (intermitente com fonte)?
├── Sim → driver eletrônico sem EMC certificado
│         → trocar para marine-grade IEC 61547
│         → ferrite cores no cabo
│         → segregar cabo da antena (>30 cm)
│         → [[Tipos de Lâmpadas e LEDs Náuticos]]
│         → [[Inversora (DC To AC)]]
└── Não → antena, conector ou aterramento → [[VHF]] ou [[Chartplotter - GPS - MFD]]
```

## Etapa 4 — Causa raiz por categoria

| Categoria | Notas críticas |
|-----------|----------------|
| **Cabo / conexão** | [[Cabeamento Náutico]] + [[Inspeção de Cabos Terminais e Conexões]] + [[Terminais Conectores e Emendas]] |
| **Bateria / banco** | [[Tipos de Bateria]] + [[Bancos de Bateria]] + [[Monitor de Bateria - BMV - Shunt]] |
| **Carga / consumo** | [[Lei de Ohm e Cálculos Básicos]] + [[Dimensionamento de Cabos DC — Cálculo Prático]] |
| **Proteção** | [[Disjuntores (DC) e (AC)]] + [[Fusíveis DC — Proteção Contra Sobrecorrente]] + [[Proteção Dr]] |
| **Bonding / aterramento** | [[Bonding — Sistema de Interligação de Massas]] + [[Aterramento]] + [[Correntes Parasitas — Stray Currents]] |
| **EMC / interferência** | [[Tipos de Lâmpadas e LEDs Náuticos]] + [[Inversora (DC To AC)]] + [[Wi-Fi a Bordo — Roteador Marine e Conectividade]] |
| **Sensor / instrumento** | [[Bússola Eletrônica (Compass - HDG Sensor)]] + [[Sonda - Profundímetro - Sonar]] + [[Estação de Vento - Anemômetro]] |
| **Bomba / atuador** | [[Bomba de Porão]] + [[Atuador Linear]] + [[Macerador - Bomba de Águas Negras]] |

## Etapa 5 — Checklist pós-correção

- [ ] Sintoma original resolvido (validar com mesma medição da Etapa 2)
- [ ] Não introduziu falha nova (megger isolação se mexeu em cabo)
- [ ] Documentar no `_Editorial/Log de Evolução.md` ou diário de bordo
- [ ] Atualizar diagrama unifilar se topologia mudou
- [ ] Inspeção visual: sem fios soltos, conexões secas, dielectric grease aplicado
- [ ] Re-testar com motor ligado e cargas em uso normal
- [ ] Verificar bonding (resistência entre massa e barramento <0,01 Ω)
- [ ] Conferir ânodos não foram afetados pela intervenção

## Ferramentas mínimas no toolkit

- **Multímetro True RMS** (Fluke 87V / 179 / T6)
- **Alicate amperímetro AC+DC** (Fluke 376/377/393 FC)
- **Termômetro IR** (Fluke 62 MAX) — encontrar conexão fraca por aquecimento
- **Megohmímetro** (Fluke 1587 FC) — isolação >100 MΩ vs casco
- **Detector de tensão** sem contato (IEC 61243)
- **EPI:** óculos ANSI Z87.1, luva isolada IEC 60900, capacete ANSI Z89.1

## Hubs transversais relacionados

- [[MOC — Diagnóstico e Manutenção]] — hub geral de troubleshooting + manutenção
- [[MOC — Segurança Integrada]] — alarmes + porão + corrosão

## Quick-reference — top 7 sintomas

1. **Motor não dá partida** → árvore Etapa 3 + [[Arranque]]
2. **Bateria descarrega rápido** → [[Monitor de Bateria - BMV - Shunt]] + parasita standby (medir em standby OFF)
3. **Choque ao tocar casco** → [[Correntes Parasitas — Stray Currents]] + ELCI
4. **Ânodo come muito rápido** → árvore Etapa 3 + [[Isolador Galvânico - Transformador de Isolamento]]
5. **Inversor desliga sob carga** → [[Inversora (DC To AC)]] (rated VA × W + queda DC)
6. **VHF/GPS com ruído** → árvore Etapa 3 + [[Tipos de Lâmpadas e LEDs Náuticos]]
7. **Disjuntor não abre em curto DC** → [[Disjuntores (DC) e (AC)]] (DC sem zero crossing precisa rated DC)

## Glossário rápido (termos do diagnosticador)

- **True RMS:** medição correta de qualquer onda (DMM premium).
- **Cat II/III/IV:** categoria de medição IEC 61010.
- **Megger:** medidor de isolação (>100 MΩ marine).
- **Termovisor IR:** câmera infravermelha — conexão fraca esquenta.
- **Stray current:** corrente parasita DC.
- **Backfeed:** corrente reversa pela rota errada (DEC-37).
- **Crimp pull-test:** teste de tração na crimpagem (ABYC E-11.13).
- **Drip loop:** alça invertida no cabo para evitar capilaridade.
- **Ag/AgCl reference electrode:** eletrodo de referência para potencial galvânico.
- **NMEA monitor:** software para ver mensagens NMEA (Maretron, Actisense).

## Quando NÃO entrar aqui

- **Vai projetar do zero** → [[MOC — Trilha do Projetista]]
- **Vai operar barco** → [[MOC — Trilha de Operação]]
- **Vai estudar conceito** → [[MOC — Trilha do Iniciante]]

## Perguntas que esta trilha responde

- Como diagnosticar falha elétrica em embarcação?
- Por que multímetro mostra leitura errada?
- Como achar curto-circuito no barco?
- O que é stray current e como diagnosticar?
- Como começar troubleshooting estruturado?
- Que ferramenta usar em cada categoria de medição?
- Como diagnosticar EMI no VHF/GPS?
