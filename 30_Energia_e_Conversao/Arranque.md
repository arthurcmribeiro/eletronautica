---
title: "Arranque"
note_type: "technical-note"
domain: "30_Energia_e_Conversao"
source_file: "ARRANQUE 26519734f7fb8343900c015a28ddc9c8.md"
status: "premium-l3"
fase_6_reescrita: 102
reviewed_on: "2026-04-26"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://webstore.iec.ch/publication/2697"
  - "https://www.imo.org/"
review_level: "engineering-curated"
aliases:
  - "ARRANQUE"
  - "Sistema de partida"
  - "Starter motor"
  - "Marine starter"
  - "Arranque marine"
  - "Motor de partida"
seo_title: "Arranque em embarcações: SAE J1171, ABYC E-11, ISO 8846, motor de partida marine, solenoide, queda de tensão, banco de partida"
seo_description: "Guia técnico premium do sistema de arranque em embarcações: motor de partida (Bosch / Delco / Mitsubishi / Hitachi marine), solenoide, banco de partida (CCA × MCA), bitola de cabo (ABYC E-11.4 ≤3% queda), ABYC E-11 + ISO 8846 ignition protection + SAE J1171, falhas comuns, diagnóstico estruturado."
seo_keywords:
  - "arranque embarcação"
  - "starter motor marine"
  - "ignition protected starter"
  - "ISO 8846"
  - "SAE J1171"
  - "CCA MCA bateria partida"
  - "queda tensão partida"
  - "Bosch Delco Mitsubishi marine"
  - "solenoide partida"
  - "ABYC E-11"
geo_queries:
  - "Por que motor não dá partida no barco?"
  - "Queda de tensão durante partida do motor?"
  - "CCA × MCA bateria de partida marine?"
  - "Como dimensionar cabo de partida?"
  - "Solenoide de partida defeituoso — diagnóstico?"
  - "Starter marine vs automotivo: diferença?"
  - "ISO 8846 ignition protection: o que é?"
  - "Bateria de partida vs bateria de serviço: posso usar a mesma?"
  - "Motor diesel vs gasolina: arranque diferente?"
  - "Arc flash em barramento DC durante partida?"
normas_citadas:
  - "ABYC E-11 (AC and DC Electrical Systems on Boats)"
  - "ABYC E-11.4 (Wire sizing)"
  - "ABYC E-11.5 (Overcurrent protection)"
  - "ABYC E-11.16 (Bonding)"
  - "ABYC TE-04 (Lightning protection)"
  - "ISO 8846 (Small craft — Ignition protection)"
  - "ISO 13297 (AC installations)"
  - "ISO 28848 (DC installations)"
  - "ISO 8849 (Bilge pumps DC)"
  - "ISO 21487 (Fuel tanks)"
  - "IEC 60092-507 (Pleasure craft)"
  - "IEC 60092-202 (Marine — Starting)"
  - "SAE J1171 (Ignition protection of marine electrical devices)"
  - "SAE J537 (Marine batteries)"
  - "SAE J930 (Marine cable)"
  - "SAE J1127 / J1128 (Battery cable)"
  - "UL 1500 (Ignition Protection Test for Marine Products)"
  - "UL 1426 (Boat Cable BC5W2)"
  - "USCG 33 CFR 183 Subpart I (Electrical Systems)"
  - "USCG 33 CFR 183.610 (Power-driven boats — gasoline)"
  - "BCI Group sizes (Battery Council International)"
  - "ABNT NBR 14728"
  - "ABNT NBR 5410"
  - "DPC NORMAM-211/DPC"
  - "DPC NORMAM-201/DPC"
  - "EU Directive 2013/53/EU (RCD)"
  - "Manual técnico Bosch / Delco / Mitsubishi / Hitachi marine starters"
  - "Manual técnico Yanmar / Volvo Penta / MerCruiser / Cummins / Caterpillar"
related_notes:
  - "Tipos de Bateria"
  - "Bancos de Bateria"
  - "Carregador de Bateria (AC To DC)"
  - "Alternador (DC)"
  - "Cabeamento Náutico"
  - "Dimensionamento de Cabos DC — Cálculo Prático"
  - "Lei de Ohm e Cálculos Básicos"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Disjuntores (DC) e (AC)"
  - "Chaves Gerais (DC)"
  - "Bonding — Sistema de Interligação de Massas"
  - "Multímetro e Instrumentos de Medição"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
  - "Inspeção de Cabos Terminais e Conexões"
---

# Arranque

> [!abstract] Resumo técnico
> O **arranque (sistema de partida / starter motor)** é o conjunto **bateria de partida + chave de ignição + solenoide + motor de partida + cablagem dedicada** que **fornece corrente alta (200-1.500 A pico em 12V; 100-700 A em 24V)** durante 2-15 segundos para girar o motor diesel ou gasolina até a primeira combustão. **Motor de partida marine** difere do automotivo por **ignition protection (ISO 8846 + SAE J1171 + UL 1500)** — em motor a gasolina, USCG 33 CFR 183.610 + ISO 8846 são obrigatórios para evitar ignição de vapores. **Cablagem é crítica** — queda de tensão >5% durante partida → torque insuficiente → motor não gira → starter queima em segundos por sobrecorrente. **Bateria de partida** é especificada em **CCA (Cold Cranking Amps) + MCA (Marine Cranking Amps)** + capacidade de reserva (RC). **NÃO compartilhar** bateria de partida com cargas de serviço — banco dedicado preserva CCA para next start. Padrões: **ABYC E-11.4** (cabo) + **E-11.5** (proteção) + **E-11.16** (bonding) + **ISO 8846 / SAE J1171 / UL 1500** (ignition protection) + **SAE J537** (baterias marine).

> [!tldr] TL;DR — 9 regras inegociáveis
> 1. **Motor de partida marine ignition-protected** (ISO 8846 + SAE J1171 + UL 1500) é OBRIGATÓRIO em motor a gasolina (USCG 33 CFR 183.610). Starter automotivo em barco a gasolina = ignição de vapor + explosão.
> 2. **Banco de partida dedicado** (NÃO compartilhar com serviço) — preserva CCA + isola cargas em standby.
> 3. **Queda de tensão durante partida ≤5%** (não os 3% gerais). Cabo dimensionado para CORRENTE DE PICO (LRA), não nominal.
> 4. **Bitola típica:** 2/0 AWG ou 3/0 AWG para diesel pequeno; 4/0 AWG para diesel grande. Cobre tinned (UL 1426 BC5W2 / SAE J1127 / IEC 60092-353).
> 5. **Fusível MRBF / Class T no polo positivo** da bateria (≤7" — ABYC E-11.5.4) — proteção contra curto durante manobra.
> 6. **Chave geral de bateria** (battery isolator, ON/OFF/BOTH) entre banco e starter — facilita manutenção + isolamento.
> 7. **CCA / MCA dimensionado para o motor** — datasheet do motor (Yanmar 2GM20: ~250 CCA; Volvo Penta D2-40: ~600 CCA; Caterpillar C9: ~1500 CCA).
> 8. **Tempo de partida ≤15 segundos** (manuais OEM). Excedeu? Pause 60-120 s antes de tentar de novo (sobreaquecimento de starter).
> 9. **Bonding do bloco do motor** ao barramento de bonding (ABYC E-11.16) + isolador galvânico no shore-power.

> [!danger] Cenários de risco
> - **Starter automotivo em motor a gasolina** = ignição de vapor → explosão na casa de máquinas. **Caso histórico:** múltiplos casos USCG documentados. **Prevenção:** USCG 33 CFR 183.610 + ISO 8846 + SAE J1171; substituir só por marine ignition-protected.
> - **Cabo subdimensionado** + queda >10% durante partida → torque insuficiente → starter "patina" tentando vencer compressão → corrente sobe a 1.500-2.000 A → cabo aquece a >100°C → derretimento isolação → fogo. **Prevenção:** dimensionar para CCA pico; bitola 2/0-4/0 AWG; conexões limpas.
> - **Bateria de partida descarregada** por cargas em standby (rádio, eletrônica, vazamento) → falha de partida em offshore noturno → SAR. **Prevenção:** banco dedicado + chave geral OFF quando desocupado; monitor de bateria.
> - **Solenoide travado em ON** (defeito mecânico) → starter girando contínuo → queima em 30-60 s + risco de fogo elétrico. **Prevenção:** verificar release de chave de ignição; treinar tripulação para desligar fusível principal em emergência.
> - **Polaridade DC invertida em retrofit** → solenoide queima imediatamente; barramento DC severamente danificado. **Prevenção:** fusível polarizado; teste antes de energizar; documentação rigorosa.
> - **Arc flash durante manutenção** em barramento DC: chave de fenda escorrega entre + e − da bateria de partida → arco 1.500-3.000 K → queimadura grave. **Prevenção:** desligar fusível principal antes; usar luva e óculos; barramento em local protegido.
> - **Bateria de partida em parallel com banco serviço** sem isolation: descarga acelerada do banco serviço para partida + recarga ineficiente → ambos bancos degradam. **Prevenção:** dual-bank com ACR/VSR/combinador; chave 1-2-BOTH-OFF; tipos compatíveis.
> - **Starter desgastado** após 5-10 anos: escovas gastas + carbono acumulado → corrente sobe + torque cai → motor difícil partir. **Prevenção:** revisão do starter a cada 5 anos; substituir escovas; limpeza.
> - **Vapor de gasolina em casa de máquinas + arc do solenoide non-IP** → ignição. **Prevenção:** blower 4 min antes de partir motor a gasolina (ABYC H-2.6 + UL 1128 + USCG 33 CFR 183 Subpart K); detector de gás.
> - **Tensão da bateria <11,5V em 12V (durante partida)** → starter não dá torque suficiente → motor não pega → tripulação tenta múltiplas vezes → bateria descarrega completamente → SAR. **Prevenção:** pre-start check (tensão > 12,4V repouso); manter banco saudável.

## O que é (definição rigorosa)

O **sistema de arranque** é o conjunto eletromecânico que:

1. **Banco de partida** — fornece corrente alta DC (12V / 24V) por curto período.
2. **Chave de ignição** — comando do operador para iniciar partida.
3. **Solenoide** — relé de alta corrente que conecta bateria → starter; também engata a engrenagem do starter no volante do motor.
4. **Motor de partida (starter motor)** — motor DC série com pinion gear que gira o flywheel do motor a 50-200 rpm.
5. **Cablagem dedicada** — cabos de bitola alta (2/0 - 4/0 AWG) de baixa resistência.
6. **Proteção elétrica** — fusível MRBF/Class T próximo ao polo + chave geral.
7. **Bonding** ao bloco do motor.

### Banco de partida — métricas

- **CCA (Cold Cranking Amps):** corrente em -18°C × 30s mantendo ≥7,2V (12V).
- **MCA (Marine Cranking Amps):** corrente em 0°C × 30s mantendo ≥7,2V (~25% maior que CCA).
- **RC (Reserve Capacity):** minutos a 25A mantendo ≥10,5V.
- **Ah (Amp-hour):** capacidade em ciclo (menos relevante para partida).

### Motor de partida marine

- **Bosch / Delco / Mitsubishi / Hitachi / Iskra (marine variants)**.
- **Tensão:** 12V (motor pequeno-médio) / 24V (motor grande).
- **Potência:** 1-10 kW.
- **Tempo de operação:** S2 30 segundos máximo.
- **Pinion gear:** engata em flywheel do motor (RING gear).

### Solenoide

- **Bobina de ativação:** 5-15A em 12V.
- **Contato principal:** 200-1.500A em 12V.
- **Função dupla:** elétrica (conectar bateria → starter) + mecânica (empurrar pinion para engatamento).

## Falhas comuns

| Falha | Causa | Diagnóstico |
|-------|-------|-------------|
| Motor não gira ("click") | Bateria fraca / conexão suja | Multímetro tensão sob carga |
| Motor gira lento | Queda de tensão excessiva | Multímetro durante partida |
| Motor gira mas não dá partida | Combustível / compressão / spark | Starter não é o problema |
| Starter "free-wheels" | Pinion não engata | Solenoide / pinion / ring gear |
| Starter contínuo após release | Solenoide travado | Substituir solenoide |
| Cheiro de queimado | Starter sobreaquecido | Pausa + diagnóstico térmico |
| Fusível abre em partida | Subdimensionado | Recalcular ou conexão fraca |

## Diagnóstico estruturado

### Etapa 1 — Pre-check

- Tensão banco em repouso (>12,4V em 12V chumbo).
- Conexões limpas + apertadas.
- Chave geral ON.
- Fusível íntegro.

### Etapa 2 — Tentativa de partida

- Multímetro em terminais do starter durante crank.
- Tensão durante partida (deve ≥10V em 12V; ≥21V em 24V).
- Corrente durante partida (alicate amperímetro AC+DC) — comparar com nominal.

### Etapa 3 — Diagnóstico

- Se tensão cai <9V: bateria fraca ou cabo subdimensionado.
- Se corrente normal mas torque baixo: starter desgastado.
- Se starter não engata: solenoide ou pinion.
- Se "click" mas não gira: bobina solenoide OK + contato principal queimado.

## Boas práticas

- **Banco de partida dedicado** preservado.
- **Chave geral OFF** quando barco desocupado.
- **Inspeção semestral** dos cabos + conexões.
- **Limpeza de terminais** (escova de aço + dielectric grease).
- **Revisão do starter a cada 5 anos** (escovas).
- **Bonding íntegro** ao bloco.
- **Backup de bateria** ou jumpstart para emergência.
- **Manutenção do motor** (compressão, óleo, combustível) — starter é apenas parte.

## Erros comuns

- "Starter automotivo é igual." → Falso. Ignition protection é obrigatório em gasolina.
- "Bateria mais cara é sempre melhor." → CCA dimensionado pelo motor.
- "Cabo grosso resolve tudo." → Conexão suja anula bitola.
- "Try and try again." → Tempo > 15s queima starter.

## Glossário

- **CCA:** Cold Cranking Amps.
- **MCA:** Marine Cranking Amps (~25% > CCA).
- **RC:** Reserve Capacity.
- **Solenoide:** relé alta corrente + atuador mecânico.
- **Pinion gear:** engrenagem do starter.
- **Ring gear:** coroa do flywheel.
- **Flywheel:** volante do motor.
- **Crank:** acionamento de partida.
- **Ignition protection:** ISO 8846 + SAE J1171 + UL 1500.
- **MRBF / Class T:** fusível alta corrente DC.
- **2/0 / 3/0 / 4/0 AWG:** bitola alta.
- **Tinned copper:** UL 1426 BC5W2.
- **BCI Group:** Battery Council International (24, 27, 31, 4D, 8D).
- **Vide [[Lei de Ohm e Cálculos Básicos]] + [[Bancos de Bateria]]**.

## Integração com outras notas

- [[Tipos de Bateria]] / [[Bancos de Bateria]] — banco dedicado.
- [[Carregador de Bateria (AC To DC)]] / [[Alternador (DC)]] — recarga.
- [[Cabeamento Náutico]] / [[Dimensionamento de Cabos DC — Cálculo Prático]] — bitola.
- [[Lei de Ohm e Cálculos Básicos]] — fundamentos.
- [[Fusíveis DC — Proteção Contra Sobrecorrente]] / [[Disjuntores (DC) e (AC)]] — proteção.
- [[Chaves Gerais (DC)]] — battery isolator.
- [[Bonding — Sistema de Interligação de Massas]] — aterramento.
- [[Multímetro e Instrumentos de Medição]] — diagnóstico.
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]] — procedimento.
- [[Inspeção de Cabos Terminais e Conexões]] — empírico.

## Perguntas que esta nota responde

- Por que motor não dá partida no barco?
- Queda de tensão durante partida do motor?
- CCA × MCA bateria de partida marine?
- Como dimensionar cabo de partida?
- Solenoide de partida defeituoso — diagnóstico?
- Starter marine vs automotivo: diferença?
- ISO 8846 ignition protection: o que é?
- Bateria de partida vs bateria de serviço: posso usar a mesma?
- Motor diesel vs gasolina: arranque diferente?
- Arc flash em barramento DC durante partida?
- Starter desgastado: quando substituir?
- Quanto tempo é seguro tentar partir?
