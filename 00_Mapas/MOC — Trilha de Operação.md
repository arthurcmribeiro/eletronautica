---
title: "MOC — Trilha de Operação"
note_type: "moc"
domain: "00_Mapas"
status: "moc-curated-plus"
fase_6_reescrita: 139
reviewed_on: "2026-04-29"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
review_level: "moc-curated-plus"
aliases:
  - "Trilha de Operação"
  - "MOC Operação"
  - "Checklist operacional elétrica náutica"
seo_title: "Trilha de Operação: checklist elétrico, energia, segurança, conforto e rotina de bordo"
seo_description: "Trilha operacional para usar uma embarcação com segurança: pré-saída, energia, baterias, shore-power, alarmes, porão, navegação, climatização, água, sanitário, galley e manutenção preventiva."
seo_keywords:
  - "checklist elétrica náutica"
  - "operação de bordo"
  - "manutenção preventiva embarcação"
  - "segurança elétrica barco"
geo_queries:
  - "O que revisar antes de sair da marina?"
  - "Como operar energia e baterias no cruzeiro?"
  - "Como evitar pane elétrica em charter?"
  - "Quais alarmes conferir antes de dormir a bordo?"
  - "Como transformar a vault em rotina de operação?"
normas_citadas: []
related_notes:
  - "MOC — Trilha do Iniciante"
  - "MOC — Trilha do Projetista"
  - "MOC — Trilha do Diagnosticador"
  - "MOC — Segurança Integrada"
---

# MOC — Trilha de Operação

> [!abstract] Sobre esta trilha
> Esta trilha transforma a base técnica em rotina de uso real: sair da marina, passar a noite fundeado, operar cargas, monitorar banco, responder a alarmes e registrar manutenção. **Venha aqui** quando o objetivo não for estudar nem projetar, mas operar uma embarcação com disciplina técnica e custo-benefício.

> [!tip] Como usar
> - **Antes da saída:** siga Etapa 1 e Etapa 2.
> - **Durante cruzeiro/fundeio:** siga Etapa 3 e Etapa 4.
> - **Depois de retorno ou pane:** siga Etapa 5 e chame [[MOC — Trilha do Diagnosticador]].
> - **Para transformar em produto/curso:** use esta trilha como checklist de aula prática do Instituto Porta do Mar.

## Etapa 1 — Pré-saída elétrica (15-30 min)

| Ordem | Nota | O que verificar |
|---|---|---|
| 1 | [[Manutenção Preventiva Elétrica — Checklist]] | inspeção visual, aquecimento, terminais, rotina trimestral/semestral/anual |
| 2 | [[Referência Rápida — Valores de Campo]] | tensões típicas, queda, fusível, cabo, sinais de alerta |
| 3 | [[Bancos de Bateria]] | banco de partida separado, banco de serviço, paralelismo indevido |
| 4 | [[Monitor de Bateria - BMV - Shunt]] | SoC, corrente de repouso, histórico e alarmes |
| 5 | [[Quadro Elétrico e Painel de Distribuição AC-DC]] | circuitos identificados, sem disjuntor mascarando falha |

**Saída esperada:** barco energizado com estado conhecido, sem depender de “parece normal”.

## Etapa 2 — Shore-power, inversor e fontes

| Situação | Sequência recomendada |
|---|---|
| Saindo da marina | [[CAIS (Pier) (AC)]] → [[Isolador Galvânico - Transformador de Isolamento]] → desligamento ordenado de cargas AC |
| Entrando na marina | verificar pedestal → [[Proteção Dr]] → [[Transformador Entrada]] / [[Transformador Bivolt]] quando aplicável |
| Fundeio com AC | [[Inversora (DC To AC)]] → [[Bancos de Bateria]] → [[Monitor de Bateria - BMV - Shunt]] |
| Recarga em navegação | [[Alternador (DC)]] → [[Carregador de Bateria (AC To DC)]] → [[BMS — Battery Management System]] |

**Regra operacional:** fonte muda, risco muda. Não trate shore-power, gerador, inversor e alternador como “energia genérica”.

## Etapa 3 — Alarmes e segurança enquanto a embarcação está em uso

- [[Sistema de Alarme Geral - Painel de Alarmes]] — painel vivo, alarmes audíveis e circuito protegido.
- [[Alarme de Alagamento - Sensor de Porão]] — sensor testado e bomba associada funcional.
- [[Detector de CO — Monóxido de Carbono]] — especialmente com gerador, aquecedor ou cockpit fechado.
- [[Detector de Gás GLP - GN]] — galley, paiol e ventilação.
- [[Extintor Automático — Combate a Incêndio na Casa de Máquinas]] — pronto e dentro da validade/condição.
- [[Iluminação de Emergência a Bordo]] — não depender só de lanterna solta.

**Ponto de decisão:** qualquer alarme real exige causa raiz. Resetar sem investigar é aceitar recorrência.

## Etapa 4 — Cargas de conforto e autonomia

### Hotelaria e refrigeração

- [[Geladeira - Freezer de Bordo]] — ciclo, ventilação e consumo diário.
- [[Icemaker - Máquina de Gelo]] — carga auxiliar, água e prioridade.
- [[Fogão - Cooktop Elétrico - Galley]] — potência AC e segurança de uso.

### Água, sanitário e porão

- [[Bomba de Água Pressurizada]] — pressostato, acumulador e vazamento.
- [[Boiler]] — carga elétrica/AC e risco de operação sem água.
- [[Holding Tank - Y-Valve - Sistema de Esgoto]] — rota correta e status do tanque.
- [[Sistema Sanitário a Vácuo - VacuFlush - SailVAC]] — vácuo, bomba e ciclo anormal.
- [[Bomba de Porão]] — operação manual/automática, sem travamento.

### Climatização

- [[Ar-Condicionado Marine — Sistema Completo]] — bomba de água, filtros, fluxo e consumo.
- [[Ar-Condicionado Marine 12V DC]] — uso limitado por autonomia.
- [[Ar-Condicionado Chiller - Chilled Water Marine]] — operação em embarcação maior.

## Etapa 5 — Retorno, registro e manutenção

1. Registrar consumo, alarmes e comportamento anormal no log da embarcação.
2. Comparar tensão/corrente com [[Referência Rápida — Valores de Campo]].
3. Se houve falha, abrir [[MOC — Trilha do Diagnosticador]] antes de trocar peça.
4. Se houve corrosão acelerada, revisar [[MOC — Seguranca e Corrosao]] e [[Bonding — Sistema de Interligação de Massas]].
5. Se a autonomia não fechou, revisar [[Dimensionamento de Banco de Baterias — Cálculo de Autonomia]].

## Hubs úteis durante operação

| Demanda | Hub |
|---|---|
| Segurança integrada | [[MOC — Segurança Integrada]] |
| Diagnóstico de sintoma | [[MOC — Trilha do Diagnosticador]] |
| Valores rápidos | [[Referência Rápida — Valores de Campo]] |
| Utilidades de bordo | [[MOC — Hidraulica Climatizacao e Utilidades]] |
| Navegação e comunicação | [[MOC — Navegacao Instrumentacao e Comunicacao]] |
| Automação, internet e telemetria | [[MOC — Automacao Conectividade e Monitoramento]] |

## Quick-reference — top 7 decisões

1. **Dormir fundeado:** monitor de bateria, alarme de porão, CO/GLP e luz de âncora.
2. **Ligar ar-condicionado:** confirmar fonte AC, bomba de água e proteção.
3. **Usar inversor:** calcular corrente DC e impacto no banco.
4. **Conectar shore-power:** checar pedestal, proteção diferencial e corrosão galvânica.
5. **Resetar alarme:** só depois de entender causa provável.
6. **Partida fraca:** não insistir; medir bateria/cabo/queda.
7. **Ânodo estranho:** fotografar, registrar tempo de consumo e investigar sistema.

## Quando NÃO entrar aqui

- Se está aprendendo do zero → [[MOC — Trilha do Iniciante]]
- Se está projetando instalação nova → [[MOC — Trilha do Projetista]]
- Se já há sintoma ou pane → [[MOC — Trilha do Diagnosticador]]
- Se a dúvida é normativa → [[Normas e Regulamentações — Abyc Iso e Brasil]]

## Perguntas que esta trilha responde

- O que revisar antes de sair da marina?
- Como operar energia, baterias e cargas de conforto sem pane?
- Quais alarmes precisam estar vivos durante uso real?
- Como transformar conhecimento técnico em checklist de oficina/charter?
- Quando uma ocorrência operacional deve virar diagnóstico formal?
