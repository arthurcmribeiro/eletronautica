---
title: "MOC — Diagnóstico e Manutenção"
note_type: "moc"
domain: "00_Mapas"
status: "moc-curated-plus"
fase_6_reescrita: 145
reviewed_on: "2026-04-29"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
review_level: "moc-curated-plus"
normas_citadas: []
aliases:
  - "Hub de Diagnóstico e Manutenção"
  - "MOC Troubleshooting"
seo_title: "MOC Diagnóstico e Manutenção: troubleshooting, medição, inspeção, corrosão e manutenção preventiva"
seo_description: "Hub transversal para diagnosticar e manter sistemas elétricos náuticos: multímetro, alicate, inspeção, cabos, baterias, AC/DC, proteção, corrosão, alarmes, porão, navegação e utilidades."
seo_keywords:
  - "diagnóstico elétrico náutico"
  - "troubleshooting embarcação"
  - "manutenção preventiva elétrica"
  - "correntes parasitas"
geo_queries:
  - "Como diagnosticar falha elétrica em embarcação?"
  - "Quais medições fazer antes de trocar componente?"
  - "Como separar sintoma de causa raiz?"
  - "Que manutenção preventiva reduz pane elétrica?"
related_notes:
  - "MOC — Trilha do Diagnosticador"
  - "MOC — Segurança Integrada"
  - "Referência Rápida — Valores de Campo"
---

# MOC — Diagnóstico e Manutenção

> [!abstract] Sobre este hub
> Este hub transversal organiza o caminho de campo: observar sintoma, medir corretamente, isolar causa raiz, corrigir, retestar e registrar. Ele não substitui [[MOC — Trilha do Diagnosticador]], mas serve como índice técnico rápido para manutenção e troubleshooting por família de sistema.

> [!tip] Rota de trabalho recomendada
> 1. Comece em [[Troubleshooting — Diagnóstico de Falhas Elétricas]].
> 2. Escolha a ferramenta em [[Multímetro e Instrumentos de Medição]] e [[Voltímetro - Amperímetro (DC e AC)]].
> 3. Compare com [[Referência Rápida — Valores de Campo]].
> 4. Se houver sintoma recorrente, siga [[MOC — Trilha do Diagnosticador]].
> 5. Depois da correção, registre e transforme em rotina via [[Manutenção Preventiva Elétrica — Checklist]].

## Instrumentação e medição

- [[Multímetro e Instrumentos de Medição]] — instrumento principal para tensão, continuidade, resistência e segurança de medição.
- [[Voltímetro - Amperímetro (DC e AC)]] — leitura de painel, corrente e tensão em operação.
- [[Ferramentas do Eletricista Náutico]] — kit de bancada/campo, EPI, crimpagem e medição.
- [[Referência Rápida — Valores de Campo]] — valores típicos para triagem e comparação.

## Método e inspeção

- [[Troubleshooting — Diagnóstico de Falhas Elétricas]] — método estruturado de causa raiz.
- [[Inspeção de Cabos Terminais e Conexões]] — inspeção visual, térmica e mecânica de conexões.
- [[Manutenção Preventiva Elétrica — Checklist]] — rotina antes que o sintoma vire pane.
- [[Terminais Conectores e Emendas]] — crimpagem, emenda e ponto fraco recorrente.
- [[Cabeamento Náutico]] — cabo correto, ambiente marinho e queda de tensão.

## Sintomas por família de sistema

### Partida, bateria e recarga

- [[Bancos de Bateria]]
- [[Monitor de Bateria - BMV - Shunt]]
- [[BMS — Battery Management System]]
- [[Carregador de Bateria (AC To DC)]]
- [[Arranque]]
- [[Alternador (DC)]]

### AC, shore-power e conversão

- [[CAIS (Pier) (AC)]]
- [[Gerador (AC)]]
- [[Inversora (DC To AC)]]
- [[Proteção Dr]]
- [[Isolador Galvânico - Transformador de Isolamento]]
- [[Transformador Entrada]]
- [[Transformador Bivolt]]

### Distribuição, proteção e aquecimento

- [[Fusíveis DC — Proteção Contra Sobrecorrente]]
- [[Disjuntores (DC) e (AC)]]
- [[Barramento DC - Bus Bar - Distribuição DC]]
- [[Quadro Elétrico e Painel de Distribuição AC-DC]]
- [[Chaves Gerais (DC)]]
- [[Relés e Relés de Estado Sólido]]

### Corrosão, fuga e ambiente

- [[Correntes Parasitas — Stray Currents]]
- [[Eletrólise]]
- [[Anôdo]]
- [[Bonding — Sistema de Interligação de Massas]]
- [[Aterramento]]

### Utilidades e segurança

- [[Bomba de Porão]]
- [[Ar-Condicionado Marine — Sistema Completo]]
- [[Sistema de Alarme Geral - Painel de Alarmes]]
- [[Detector de CO — Monóxido de Carbono]]
- [[Detector de Gás GLP - GN]]

### Navegação e comunicação

- [[NMEA 2000 - NMEA 0183 — Rede de Instrumentos]]
- [[VHF]]
- [[AIS (Automatic Identification System)]]
- [[Piloto Automático]]
- [[Bússola Eletrônica (Compass - HDG Sensor)]]

## Quick-reference — top 7 sintomas

1. **Motor não parte:** banco, queda de tensão, cabo, solenoide e arranque.
2. **Disjuntor desarma:** curto, sobrecarga, fuga, aquecimento ou componente errado.
3. **Bateria descarrega parada:** carga always-on, fuga, BMS, monitor mal calibrado.
4. **Ânodo acaba rápido:** corrente parasita, shore-power, bonding ou liga errada.
5. **VHF/MFD reinicia:** queda de tensão, ruído, conexão ou circuito compartilhado.
6. **Bomba de porão falha:** alimentação, boia/sensor, impeller, backfeed ou proteção.
7. **Ar-condicionado arma e desarma:** bomba de água, fluxo, alimentação AC ou proteção.

## Quando NÃO entrar aqui

- Se você precisa de passo a passo por sintoma → [[MOC — Trilha do Diagnosticador]]
- Se você está montando projeto novo → [[MOC — Trilha do Projetista]]
- Se é rotina antes de saída → [[MOC — Trilha de Operação]]
- Se o foco é risco de vida/incêndio/porão → [[MOC — Segurança Integrada]]

## Perguntas que este mapa ajuda a responder

- Por onde começo quando o sintoma é difuso?
- Quais medições devo fazer antes de trocar componente?
- Em quais notas procurar causa raiz por família de sistema?
- Como transformar manutenção corretiva em preventiva?
