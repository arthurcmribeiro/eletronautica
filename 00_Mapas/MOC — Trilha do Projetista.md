---
title: "MOC — Trilha do Projetista"
note_type: "moc"
domain: "00_Mapas"
status: "moc-curated-plus"
fase_6_reescrita: 137
reviewed_on: "2026-04-29"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
review_level: "moc-curated-plus"
aliases:
  - "Trilha de projeto"
  - "Workflow de projetista elétrico náutico"
seo_title: "Trilha do projetista: workflow completo para projetar instalação elétrica náutica"
seo_description: "Trilha estruturada em 7 fases para projetar instalação elétrica em embarcação: análise de uso → arquitetura → dimensionamento → seleção de equipamentos → proteção → diagrama unifilar → comissionamento. ~30 notas Tier S/A premium-l3 + checklists + normas mestre."
seo_keywords:
  - "projeto elétrico embarcação"
  - "workflow projetista marine"
  - "ABYC E-11 ABNT NBR 14728"
  - "diagrama unifilar"
  - "dimensionamento DC AC"
geo_queries:
  - "Como projetar instalação elétrica em barco?"
  - "Qual o workflow de um projeto náutico?"
  - "Por onde começar um retrofit elétrico?"
  - "Como dimensionar shore-power, banco e inversor?"
normas_citadas: []
related_notes:
  - "Atlas Técnico"
  - "Fundamentos da Elétrica Náutica"
  - "MOC — Trilha do Iniciante"
  - "MOC — Trilha do Diagnosticador"
  - "MOC — Trilha de Operação"
---

# MOC — Trilha do Projetista

> [!abstract] Para quem é esta trilha
> Para **eletricistas, técnicos e engenheiros** que vão projetar instalação elétrica completa ou retrofit significativo. Pressuposto: você dominou a [[MOC — Trilha do Iniciante]] (vocabulário + fundamentos + normas + ambiente marine). Aqui está o **workflow completo de projeto em 7 fases** com checklist, decisões críticas e cross-references. ~30 notas em sequência ordenada com tempo estimado de **20-30h de trabalho ativo** (não inclui execução).

> [!tip] Quando NÃO seguir esta trilha
> - Você é amador querendo aprender → [[MOC — Trilha do Iniciante]] primeiro.
> - Você está consertando algo → [[MOC — Trilha do Diagnosticador]].
> - Sua dúvida é regulamentar → [[Normas e Regulamentações — Abyc Iso e Brasil]] direto.
> - Mega-iate / SOLAS → este MOC ajuda mas você precisa de classification society + engenheiro registrado com ART.

## Fase 1 — Análise de uso e classificação (2-3h)

Antes de desenhar nada, entender o regime aplicável.

| # | Nota | Tier | Decisão |
|---|------|------|---------|
| 1 | [[Tipos de Embarcação]] | 🔧 A | Recreio amador (NORMAM-211) × comercial (NORMAM-201) × SOLAS × HSC |
| 2 | [[Princípios Náuticos]] | 🔧 A | Ambiente marine + classificação societies se aplicável |
| 3 | [[Normas e Regulamentações — Abyc Iso e Brasil]] | ⚡ S | Identificar normas aplicáveis (BR + EUA + UE conforme registro/operação) |
| 4 | [[Projeto Elétrico de Embarcação — Passo a Passo]] | ⚡ S | Workflow completo (ler na íntegra) |

**Saída desta fase:** documento de classificação + lista de normas aplicáveis + escopo do projeto.

## Fase 2 — Levantamento de cargas e cálculo de banco (3-5h)

Quanto consome, por quanto tempo, com que redundância.

| # | Nota | Tier |
|---|------|------|
| 5 | [[Lei de Ohm e Cálculos Básicos]] | 🔧 A |
| 6 | [[Dimensionamento de Banco de Baterias — Cálculo de Autonomia]] | ⚡ S |
| 7 | [[Tipos de Bateria]] | ⚡ S |
| 8 | [[Bancos de Bateria]] | ⚡ S |
| 9 | [[Lítio LiFePO4 — Instalação e Cuidados Específicos]] | ⚡ S (se LFP) |

**Saída:** lista de cargas DC + AC, autonomia desejada, química de bateria escolhida, banco dimensionado em Ah.

## Fase 3 — Arquitetura de geração e fluxo AC↔DC (3-4h)

De onde vem energia.

| # | Nota | Tier |
|---|------|------|
| 10 | [[CAIS (Pier) (AC)]] | ⚡ S |
| 11 | [[Alternador (DC)]] | ⚡ S |
| 12 | [[Carregador de Bateria (AC To DC)]] | ⚡ S |
| 13 | [[Inversora (DC To AC)]] | ⚡ S |
| 14 | [[Placa Solar (DC)]] (se solar) | ⚡ S |
| 15 | [[Eólico (DC)]] (se eólico) | 🔧 A |
| 16 | [[Gerador (AC)]] / [[Gerador (DC)]] (se aplicável) | ⚡ S |
| 17 | [[Transformador Bivolt]] / [[Transformador Entrada]] (se necessário) | ⚡ S |

**Saída:** topologia AC + DC, fluxo entre fontes, transferência (ATS) configurada.

## Fase 4 — Distribuição, proteção e comutação (3-5h)

Como distribuir e proteger.

| # | Nota | Tier |
|---|------|------|
| 18 | [[Quadro Elétrico e Painel de Distribuição AC-DC]] | 🔧 A |
| 19 | [[Barramento DC - Bus Bar - Distribuição DC]] | 🔧 A |
| 20 | [[Disjuntores (DC) e (AC)]] | ⚡ S |
| 21 | [[Fusíveis DC — Proteção Contra Sobrecorrente]] | ⚡ S |
| 22 | [[Proteção Dr]] | ⚡ S |
| 23 | [[Chaves Gerais (DC)]] | 🔧 A |
| 24 | [[Chaves Seletoras (AC)]] (ATS) | 🔧 A |
| 25 | [[Hotline (DC)]] | 🔧 A |
| 26 | [[Divisores de Carga (DC)]] | 🔧 A |
| 27 | [[Linha Leve (AC)]] / [[Linha Pesada (AC)]] | ⚡ A |

**Saída:** quadro central dimensionado, proteção coordenada, hotline para bombas porão/alarme, ATS configurado.

## Fase 5 — Aterramento e proteção contra corrosão (2-3h)

ABYC E-11.16 + isolador galvânico — em barco BR é estratégico.

| # | Nota | Tier |
|---|------|------|
| 28 | [[Aterramento]] | ⚡ S |
| 29 | [[Bonding — Sistema de Interligação de Massas]] | ⚡ S |
| 30 | [[Isolador Galvânico - Transformador de Isolamento]] | ⚡ S |
| 31 | [[Anôdo]] | ⚡ S |
| 32 | [[Correntes Parasitas — Stray Currents]] | ⚡ S |

**Saída:** plano de bonding + escolha de ânodos + isolador galvânico (se shore-power frequente).

## Fase 6 — Cabeamento e dimensionamento (2-3h)

Bitola correta = sem queda + sem aquecimento.

| # | Nota | Tier |
|---|------|------|
| 33 | [[Cabeamento Náutico]] | 🔧 A |
| 34 | [[Dimensionamento de Cabos DC — Cálculo Prático]] | ⚡ S |
| 35 | [[Terminais Conectores e Emendas]] | 🔧 A |

**Saída:** lista de bitolas (AWG/mm²) por circuito + tipos de terminais + crimping plan.

## Fase 7 — Diagrama unifilar e documentação (3-4h)

Documentar tudo.

| # | Nota | Tier |
|---|------|------|
| 36 | [[Diagrama Unifilar — Documentação do Sistema Elétrico]] | ⚡ S |
| 37 | [[Simbologia Elétrica Náutica]] | 🔧 A |
| 38 | [[Leitura de Diagramas e Esquemas Elétricos]] | 🔧 A |

**Saída:** diagrama unifilar do projeto + plant view de localização + lista de equipamentos + memorial descritivo.

## Especialidades por tipo de embarcação

| Embarcação | Adicionar |
|------------|-----------|
| **Veleiro** | [[Estação de Vento - Anemômetro]] + [[Piloto Automático]] + [[Bússola Eletrônica (Compass - HDG Sensor)]] (vela mode) |
| **Lancha pesca** | [[Sonda - Profundímetro - Sonar]] + [[Chartplotter - GPS - MFD]] + [[Farol de Busca]] + [[Som]] |
| **Mega-iate** | [[Automação de Bordo — Sistemas Domoticos]] (CZone, EmpirBus) + [[Monitoramento Remoto — VRM - Telemetria]] + [[Wi-Fi a Bordo — Roteador Marine e Conectividade]] + [[Starlink - Internet a Bordo]] |
| **Charter** | + LGPD compliance + [[Câmeras de Bordo - Sistema CFTV]] + [[Sistema de Alarme Geral - Painel de Alarmes]] |
| **Catamarã** | Bonding cruzado pela ponte + cabling especial + dois compartimentos elétricos |
| **Elétrico (full electric)** | [[BMS — Battery Management System]] + ABYC E-13 + estratégia de carga (shore + solar + regen) |

## Sub-trilhas por especialidade

- **Sanitário + galley + climatização:** [[MOC — Hidraulica Climatizacao e Utilidades]]
- **Iluminação completa:** [[MOC — Iluminacao e Sinalizacao]]
- **Navegação eletrônica:** [[MOC — Navegacao Instrumentacao e Comunicacao]]
- **Automação:** [[MOC — Automacao Conectividade e Monitoramento]]
- **Segurança redundante:** [[MOC — Segurança Integrada]]

## Checklist de fim de projeto

- [ ] Memorial descritivo com normas citadas (edição/ano/cláusula)
- [ ] Diagrama unifilar atualizado (formato IEC 60617)
- [ ] Lista de equipamentos com modelos e fabricantes
- [ ] Cálculos documentados (banco, cabo, fusível)
- [ ] Plano de bonding com Ag/AgCl reference electrode
- [ ] Escolha de ânodos justificada (zinco/Al/Mg)
- [ ] ATS configurado (shore × gerador × inversor)
- [ ] ELCI 30mA/100ms presente em circuitos AC marine
- [ ] Hotline DC com proteção contra backfeed (DEC-37)
- [ ] Manual de operação para tripulação
- [ ] ART (Anotação de Responsabilidade Técnica) emitida pelo engenheiro
- [ ] Conformidade DPC NORMAM (211 amador / 201 comercial) verificada

## Quick-reference — top 7 dúvidas

1. **Por onde começar projeto novo?** → Fase 1 + [[Projeto Elétrico de Embarcação — Passo a Passo]].
2. **Como dimensionar banco?** → Fase 2 + [[Dimensionamento de Banco de Baterias — Cálculo de Autonomia]].
3. **Inversor pure sine ou modified?** → Pure sine sempre (Fase 3 + [[Inversora (DC To AC)]]).
4. **Quando isolador galvânico?** → Fase 5 + [[Isolador Galvânico - Transformador de Isolamento]].
5. **Cabo automotivo serve?** → NÃO. Fase 6 + [[Cabeamento Náutico]].
6. **Quem assina o projeto?** → Engenheiro com CREA + ART (vide nota mestre Normas).
7. **Diagrama unifilar é obrigatório?** → SIM em comercial / SOLAS, prática consagrada em recreio. [[Diagrama Unifilar — Documentação do Sistema Elétrico]].

## Próximos passos

- **Após o projeto:** [[MOC — Trilha de Operação]] (manutenção + uso)
- **Em troubleshooting durante comissionamento:** [[MOC — Trilha do Diagnosticador]]
- **Para citar norma corretamente:** [[Normas e Regulamentações — Abyc Iso e Brasil]]

## Perguntas que esta trilha responde

- Como projetar instalação elétrica em barco?
- Qual o workflow de um projeto náutico?
- Por onde começar um retrofit elétrico?
- Como dimensionar shore-power, banco e inversor?
- Como documentar projeto para passar em inspeção?
- Que checklist seguir antes de comissionar?
- Quem deve assinar o projeto?
