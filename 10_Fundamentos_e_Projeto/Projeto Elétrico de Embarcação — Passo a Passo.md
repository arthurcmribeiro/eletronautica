---
title: "Projeto Elétrico de Embarcação — Passo a Passo"
note_type: "procedure"
domain: "10_Fundamentos_e_Projeto"
source_file: "PROJETO ELÉTRICO DE EMBARCAÇÃO — PASSO A PASSO 33a19734f7fb816c9ebbcc180815b545.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "27"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
  - "internacional"
normas_citadas:
  - "ABYC E-11 (2023) — AC & DC Electrical Systems on Boats"
  - "ABYC E-2 (2020) — Cathodic Protection / Bonding"
  - "ABYC E-4 (2019) — Lightning Protection"
  - "ABYC E-8 (2020) — AC Generators on Boats"
  - "ABYC E-9 (2019) — DC Electrical Systems / Alternators and Chargers"
  - "ABYC E-10 (2018) — Storage Batteries (chumbo-ácido e lítio)"
  - "ABYC A-16 (2020) — Electric Navigation Lights"
  - "ABYC TE-4 (2018) — Lightning Protection (technical note)"
  - "ABYC A-4 (2018) — Fire Fighting Equipment"
  - "ISO 13297:2020 — Small craft — Electrical systems — AC & DC installations (sucessora de ISO 10133)"
  - "ISO 8846:1990 — Small craft — Electrical devices — Protection against ignition of flammable gases"
  - "ISO 10134:2019 — Small craft — Electrical devices — Lightning protection"
  - "IEC 60092-101 — Definitions and general requirements"
  - "IEC 60092-201 — System design — General"
  - "IEC 60092-202 — System design — Protection"
  - "IEC 60092-301 — Equipment — Generators and motors"
  - "IEC 60092-352 — Choice and installation of electrical cables"
  - "IEC 60092-401 — Installation and test of completed installation"
  - "IEC 60092-507 — Pleasure craft"
  - "IEC 60364-series — Low-voltage electrical installations (referência cruzada AC shore-to-boat)"
  - "IEC 61162-1/-2/-3 (NMEA 0183/2000) — Rede digital de instrumentação e controle"
  - "ABNT NBR 5410:2004 + emendas — Instalações elétricas de baixa tensão"
  - "ABNT NBR IEC 60364 — Instalações elétricas de baixa tensão (adoção brasileira)"
  - "NORMAM-201/DPC — Tráfego e permanência (embarcações comerciais)"
  - "NORMAM-204/DPC — Segurança da Marinha Mercante"
  - "NORMAM-205/DPC — Embarcações de passageiros"
  - "NORMAM-211/DPC — Embarcações de esporte e recreio"
  - "CE-RCD Directive 2013/53/EU — Recreational Craft Directive (marcação CE)"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
aliases:
  - "PROJETO ELÉTRICO DE EMBARCAÇÃO — PASSO A PASSO"
seo_title: "Projeto Elétrico de Embarcação — Passo a Passo"
seo_description: "PROJETO ELÉTRICO — Planejamento e documentação completa do sistema elétrico da embarcação antes da execução. A diferença entre um sistema confiável e um sistema prob."
seo_keywords:
  - "Projeto"
  - "Embarcação"
  - "Passo"
  - "10 Fundamentos e Projeto"
geo_queries:
  - "O que é Projeto Elétrico de Embarcação — Passo a Passo em instalações elétricas náuticas?"
  - "Qual é a função de Projeto Elétrico de Embarcação — Passo a Passo na embarcação?"
related_notes:
  - "Tipos de Embarcação"
  - "DC vs AC — Corrente Contínua e Alternada"
  - "Diagrama Unifilar — Documentação do Sistema Elétrico"
  - "Dimensionamento de Banco de Baterias — Cálculo de Autonomia"
  - "Dimensionamento de Cabos DC — Cálculo Prático"
  - "Fase e Neutro"
  - "Ferramentas do Eletricista Náutico"
  - "Inspeção de Cabos Terminais e Conexões"
---

# Projeto Elétrico de Embarcação — Passo a Passo

> [!abstract] Resumo técnico
> PROJETO ELÉTRICO — Planejamento e documentação completa do sistema elétrico da embarcação antes da execução. A diferença entre um sistema confiável e um sistema problemático começa aqui.

> [!tip] Regra de decisão em 30 segundos
> 1. **Load list antes de tudo** — nenhum cálculo de banco, cabo ou proteção faz sentido sem levantamento completo de cargas (equipamento, potência, tensão, horas/dia) e **perfil de uso realista** (o que fica ligado simultaneamente, não o pior caso somado).
> 2. **Banco dimensionado por Wh/dia × autonomia ÷ DOD** — chumbo-ácido trabalha até 50% DOD (vida útil), LiFePO4 até 80% DOD (ABYC E-10). Margem de envelhecimento: +20-30%.
> 3. **Cabo dimensionado por ABYC E-11 Tabela VI (corrente) + Tabela VI-A (queda de tensão 3% críticos / 10% não-críticos)** — duas restrições, adota-se a maior seção. Dobrar comprimento (ida+volta).
> 4. **Proteção no positivo, ≤7" (178 mm) do barramento** — fusível ≤ capacidade do cabo (ABYC E-11), nunca ≤ carga. Baterias sempre com fusível classe T ou MRBF próximo ao polo positivo.
> 5. **Bonding ABYC E-2 é parte do projeto, não acessório** — todas as massas metálicas submersas interligadas + ânodos dimensionados; projeto elétrico sem diagrama de bonding é projeto incompleto.
> 6. **Diagrama unifilar AC + DC obrigatório** — sem single-line diagram legível, não há como fazer manutenção, perícia ou reforma controlada. AC e DC **em diagramas separados**, nunca misturados.
> 7. **Cargas transitórias verificadas separadamente** — motor de partida (200-1000 A), compressor AC (inrush 5-8×), guincho âncora — não entram na média diária, exigem dimensionamento específico de cabo/proteção.
> 8. **Documentação legível a bordo** — projeto no escritório que não chega ao barco é projeto inútil; pasta física + cópia digital + identificação de cabos/circuitos no próprio painel.
> 9. **Revisão obrigatória a cada adição de equipamento** — acrescentar geladeira, inverter, conversor, painel solar sem recálculo de cabo-tronco/barramento/banco é a principal causa de incêndio elétrico pós-reforma.

> [!danger] Quando chamar um especialista (engenheiro eletricista náutico / surveyor)
> 1. **Projeto do zero em embarcação > 12 m ou com sistema AC a bordo** — ART de engenheiro, compatibilização com NORMAM-211 (recreio) ou NORMAM-201/204/205 (comercial), e interface com certificadora (BV, Lloyd's, RINA, ABS) quando aplicável.
> 2. **Retrofit de banco chumbo→lítio em arquitetura central** — LiFePO4 exige BMS, reconfiguração de alternador (field regulator ou DC-DC charger), revisão de fusível classe T, bonding e ventilação; cálculo e laudo técnico antes da troca (ABYC E-10 + TE-13 drafts).
> 3. **Eletrificação, híbrido ou propulsão elétrica** — projeto de bus ≥ 48 V DC exige estudo de curto-circuito, coordenação de proteções, isolação galvânica e análise térmica; fora do escopo de instalador generalista.
> 4. **Sistema AC 110/220 V com shore power + gerador + inverter** — ATS (automatic transfer switch), isolador galvânico ou transformador de isolação, ELCI/RCD/GFCI, distribuição por polaridade — ABYC E-11 + IEC 60092-series + NBR 5410 cruzados; erro aqui mata (choque fatal em água).
> 5. **Certificação para classe comercial, charter ou exportação** — BV/Lloyd's/RINA para NORMAM-201/204/205 brasileiro; CE-RCD Directive 2013/53/EU para mercado europeu; USCG + ABYC para EUA. Cada regime exige projeto formal com traceability de normas.
> 6. **Perícia pós-sinistro (incêndio, choque elétrico, eletrocussão)** — engenheiro com experiência em perícia (IBAPE, Abracem) + documentação do projeto original = base para defesa do proprietário/instalador; sem projeto, presunção de culpa.
> 7. **Survey para compra/venda, seguro ou mudança de bandeira** — surveyor homologado avalia projeto vs instalação real; ausência ou divergência gera cláusulas de exceção na apólice e redução de valor na venda.
> 8. **Mudança de classe NORMAM-211 (recreio) → NORMAM-201/205 (comercial/charter)** — reclassificação exige reprojeto completo (RBNA ou sociedade classificadora), adequação a normas mais rígidas e inspeção DPC.
> 9. **Projeto em áreas classificadas (tanques de combustível, compartimento de baterias, lazareto com glp)** — zona Ex, ABYC E-11 seção 11 + ISO 8846 (ignition protection) + IEC 60079-series; equipamento não certificado nessas áreas = risco de explosão.

## O que é

Projeto elétrico náutico é o conjunto de documentos técnicos que descrevem, dimensionam e organizam todos os sistemas elétricos de uma embarcação — antes da instalação. Inclui levantamento de cargas, dimensionamento de cabos e proteções, seleção de equipamentos, diagrama unifilar, diagrama de bonding e layout de instalação.

Em embarcações de recreio no Brasil, a maioria das instalações é feita sem projeto formal — o que explica a alta incidência de problemas, reformas e riscos de incêndio.

## Função

| Função | Resultado prático |
| --- | --- |
| Documentação | Registro de toda a instalação para manutenção futura |
| Dimensionamento | Cabos e proteções corretos desde o início |
| Planejamento | Evita retrabalho e adaptações improvisadas |
| Segurança | Identificação de riscos antes da execução |
| Base para auditoria e perícia | Facilita interface com seguradora, survey e reforma controlada |
| Referência para diagnóstico | Facilita troubleshooting futuro |

## Como aparece na prática

- Planilha de carga (load list) com todos os consumidores
- Diagrama unifilar AC e DC
- Diagrama de bonding
- Especificação de cabos por circuito (bitola, comprimento, tipo)
- Especificação de proteções (fusíveis, disjuntores, valores)
- Layout de instalação (onde cada painel, bateria, gerador fica)
- Documentação da topologia de aterramento, bonding e pontos de conexão entre sistemas quando aplicável

## Fundamentos mínimos

**Sequência lógica do projeto:**

```jsx
1. Levantamento de cargas (o que vai existir no barco)
       ↓
2. Análise de perfil de uso (o que fica ligado ao mesmo tempo e por quanto tempo)
       ↓
3. Dimensionamento do banco de baterias (capacidade necessária)
       ↓
4. Dimensionamento do sistema de geração/carregamento
       ↓
5. Dimensionamento de cabos (corrente, queda de tensão, temperatura)
       ↓
6. Especificação de proteções (fusíveis e disjuntores)
       ↓
7. Diagrama unifilar
       ↓
8. Layout físico
       ↓
9. Lista de materiais
```

**Queda de tensão de projeto:**

- Circuitos críticos ou sensíveis costumam ser tratados em faixa mais conservadora
- Cargas gerais podem admitir quedas maiores, conforme o padrão adotado e a tolerância do equipamento
- Circuitos de partida e outras cargas transitórias exigem verificação específica de desempenho, e não apenas um número genérico

**Cálculo de bitola de cabo:**

```jsx
I = P / V (corrente em amperes)
R_máx = (ΔV_máx) / I (resistência máxima admitida)
Comprimento = ida + volta (dobrar comprimento físico)
Seção = (ρ × L) / R_máx
ρ (cobre) = 0,0175 Ω·mm²/m
```

## Características de um bom projeto

| Item | Requisito |
| --- | --- |
| Levantamento de cargas | Completo — cada consumidor com potência e horas/dia |
| Perfil de uso | Realista — não somar tudo como se ligasse ao mesmo tempo |
| Dimensionamento de banco | Autonomia coerente com a missão, o perfil de uso e a estratégia de recarga |
| Dimensionamento de cabos | Por cálculo, não por "costume" |
| Proteções | Fusível em cada circuito, no positivo, próximo ao barramento |
| Documentação | Legível, atualizada, a bordo |
| Revisão | Prevista — sistema elétrico evolui com o barco |

## Etapas detalhadas

**Etapa 1 — Levantamento de cargas:**

| Equipamento | Potência (W) | Tensão | Horas/dia | Wh/dia |
| --- | --- | --- | --- | --- |
| Piloto automático | 20–80W | 12V | 8h | 160–640 |
| VHF | 6W (RX) / 25W (TX) | 12V | 8h RX / 0,5h TX | 60,5 |
| GPS/Chartplotter | 15–25W | 12V | 8h | 120–200 |
| Radar | 30–50W | 12V | 4h | 120–200 |
| Bomba de porão | 5A × 12V = 60W | 12V | 0,25h | 15 |
| Iluminação LED total | 30–60W | 12V | 5h | 150–300 |
| Geladeira DC | ~40W médio (ciclo) | 12V | contínuo (duty ~40%) | 400–800 |
| **Total típico veleiro** |  |  |  | **1.000–2.200 Wh/dia** |

**Etapa 2 — Dimensionamento do banco:**

```jsx
Consumo diário: 1.000 Wh/dia (exemplo)
Autonomia desejada: 2 dias sem recarga
Consumo total: 2.000 Wh
DOD máximo recomendado: 50% (chumbo-ácido) / 80% (LiFePO4)
Capacidade banco chumbo-ácido: 2.000 / 0,5 = 4.000 Wh ÷ 12V = 333 Ah
Capacidade banco LiFePO4: 2.000 / 0,8 = 2.500 Wh ÷ 12V = 208 Ah
```

## Ferramentas de projeto

- **Planilha Excel / Google Sheets** — levantamento de cargas e cálculo de banco
- **CAD elétrico (QElectroTech, EPLAN, AutoCAD Electrical)** — diagrama unifilar profissional
- **Victron VictronConnect / VRM** — monitoramento e planejamento integrado
- **ABYC DC Wiring Sizing Chart** — tabela de referência para bitola de cabos
- **Ancor Marine Wire Size Calculator** — calculadora online gratuita

## Documentos que o projeto deve incluir

- **Load List (Planilha de cargas)** — todos os consumidores com potência, tensão e horas de uso
- **Battery Bank Sizing (Dimensionamento do banco)** — cálculo de capacidade e autonomia
- **Charging System Sizing (Sistema de geração)** — alternador, carregador, painel solar, gerador
- **Cable Schedule (Lista de cabos)** — circuito, bitola, comprimento, tipo, fusível
- **Single Line Diagram (Diagrama unifilar)** — esquema elétrico simplificado AC e DC
- **Bonding Diagram** — interligação de todas as massas metálicas
- **Equipment List** — especificação de cada equipamento instalado

## Problemas por falta de projeto

| Consequência | Causa típica |
| --- | --- |
| Incêndio elétrico | Cabo subdimensionado sem fusível adequado |
| Banco descarregando rápido | Consumo real maior que o estimado sem levantamento |
| Equipamentos queimando | Proteções erradas ou ausentes |
| Cabos superaquecendo | Queda de tensão excessiva por bitola insuficiente |
| Dificuldade de manutenção | Sem documentação — técnico não sabe o que é o quê |
| Corrosão acelerada | Bonding ausente por falta de planejamento |

## Causas raiz dos problemas de projeto

**Ausência total de projeto:**

Embarcações no Brasil são frequentemente montadas por intuição — "coloco um fio desse tamanho porque parece certo." Sem cálculo, sem margem, sem proteção correta.

**Projeto desatualizado:**

O projeto foi feito para a embarcação original. Com o tempo, novos equipamentos são adicionados sem revisão — banco insuficiente, cabos sobrecarregados, proteções incompatíveis.

**Projeto copiado de outro barco:**

"Esse barco igual ao meu, vou copiar o projeto." Perfis de uso, equipamentos e autonomia diferem entre embarcações aparentemente iguais.

## Diagnóstico (auditoria do sistema existente)

**Para embarcações sem projeto:**

```jsx
1. Fotografar todo o sistema existente (painel, baterias, distribuidores)
2. Medir corrente em cada circuito com alicate amperímetro (carga normal de uso)
3. Verificar bitola dos cabos existentes (comparar com corrente medida)
4. Identificar fusíveis/disjuntores existentes e seus valores
5. Medir queda de tensão em cabos críticos (motor de partida, bomba principal)
6. Documentar o que foi encontrado → gerar retroengenharia do projeto
```

## Boas práticas profissionais

- Iniciar qualquer novo projeto ou reforma com levantamento de cargas completo
- Usar perfil de uso realista — não máximo teórico
- Dimensionar banco com reserva de projeto compatível com envelhecimento, incerteza de uso e criticidade da missão
- Documentar o projeto com revisão datada
- Manter cópia do projeto a bordo (pasta física + digital)
- Revisar o projeto sempre que um equipamento novo for instalado
- Usar norma ABYC como referência técnica (tabelas de bitola, proteção, etc.)

## Cuidados ao executar sem projeto

**Se não houver projeto formal:**

- Ao menos fazer levantamento de cargas informal
- Seguir regra prática: fusível ≤ capacidade do cabo, não da carga
- Usar bitola sempre acima do calculado por corrente (margem de temperatura)
- Documentar o que foi instalado mesmo que de forma simples

## Erros comuns

**Projetar por kVA total sem perfil de uso:**

Somar todas as cargas como se ligassem ao mesmo tempo gera banco superdimensionado e sistema sobredimensionado. Perfil de uso realista é mais útil.

**Não incluir cargas de partida (inrush):**

Motor de ar-condicionado na partida puxa 5–8× a corrente nominal. Sem considerar isso, o fusível geral é subdimensionado.

**Esquecer as cargas parasitas:**

Relés, displays em standby, eletrônicos em modo espera, carregadores de celular — somam 50–200W que ficam ligados o dia todo. Impacto real no banco.

**Projeto em papel que não sai do escritório:**

Projeto impecável que nunca chega ao barco. Manter documentação acessível a bordo é parte do projeto.

**Não incluir plano de manutenção:**

O projeto deve indicar quando inspecionar cabos, terminais, baterias, fusíveis. Sem isso, o sistema se deteriora sem intervenção.

## Relação com outros sistemas

- **Banco de baterias:** dimensionamento é o coração do projeto
- **Diagrama unifilar:** documento derivado do projeto
- **Bonding:** parte integrante do projeto elétrico
- **Painel de distribuição:** resultado do dimensionamento de circuitos
- **Todos os sistemas:** o projeto é o documento que os integra

## Brasil x Internacional

| Aspecto | Brasil | Internacional |
| --- | --- | --- |
| Projeto obrigatório | Não (embarcações de recreio) | Recomendado (ABYC) / Obrigatório (certificação Lloyd's, BV) |
| Profissionais que fazem projeto | Minoria | Padrão em instalações sérias |
| Documentação a bordo | Rara | Comum em embarcações certificadas |
| Ferramentas de projeto | Planilha Excel improvisada | Software dedicado |
| Auditoria pós-instalação | Inexistente | Inspeção por seguradora em embarcações novas |

## Normas aplicáveis

**Referência técnica de projeto (ABYC — mais usada na prática):**

- **ABYC E-11 (2023)** — *AC & DC Electrical Systems on Boats*: tabelas de bitola (Tabela VI), queda de tensão (Tabela VI-A, 3%/10%), proteção no positivo ≤7", identificação por cor, proteção ≤178 mm do polo/barramento. **Documento mestre do projeto elétrico náutico.**
- **ABYC E-2 (2020)** — *Cathodic Protection*: bonding, interligação de massas metálicas submersas, dimensionamento de ânodos de sacrifício. Parte integrante do projeto (não acessório).
- **ABYC E-4 (2019) / TE-4 (2018)** — *Lightning Protection*: projeto do sistema de proteção contra raios, air terminals, eletrodos submersos, bonding específico.
- **ABYC E-8 (2020)** — *AC Generators on Boats*: projeto de circuito de gerador, ATS, paralelismo com shore power.
- **ABYC E-9 (2019)** — *DC Electrical Systems / Alternators and Chargers*: dimensionamento de alternador, regulação, carga multi-banco.
- **ABYC E-10 (2018)** — *Storage Batteries*: dimensionamento, ventilação, fixação, DOD chumbo-ácido vs LiFePO4, fusível classe T ou MRBF.
- **ABYC A-16 (2020)** — *Electric Navigation Lights*: homologação e instalação das luzes de navegação (cruzamento com COLREGs 72).
- **ABYC A-4 (2018)** — *Fire Fighting Equipment*: interface do projeto elétrico com detecção/supressão de incêndio.

**Normas internacionais para embarcações de recreio (ISO):**

- **ISO 13297:2020** — *Small craft — Electrical systems — AC & DC installations* (sucessora de ISO 10133, unificando AC e DC).
- **ISO 8846:1990** — *Small craft — Electrical devices — Protection against ignition of flammable gases* (ignition protection em áreas com combustível/GLP).
- **ISO 10134:2019** — *Small craft — Electrical devices — Lightning protection*.

**Normas internacionais para embarcações comerciais (IEC 60092-series — *Electrical installations in ships*):**

- **IEC 60092-101** — Definitions and general requirements.
- **IEC 60092-201** — System design — General.
- **IEC 60092-202** — System design — Protection.
- **IEC 60092-301** — Equipment — Generators and motors.
- **IEC 60092-352** — Choice and installation of electrical cables.
- **IEC 60092-401** — Installation and test of completed installation.
- **IEC 60092-507** — Pleasure craft (consolidação para recreio).
- **IEC 60364-series** — Low-voltage electrical installations (cruzamento para instalação AC shore-to-boat).
- **IEC 61162-1/-2/-3 (NMEA 0183 / 2000)** — Rede digital de instrumentação e controle a bordo.

**Normas brasileiras (ABNT + DPC):**

- **ABNT NBR 5410:2004 + emendas** — *Instalações elétricas de baixa tensão*: referência para AC a bordo (shore power, gerador, inverter) e princípios de proteção/identificação.
- **ABNT NBR IEC 60364** — adoção brasileira da série IEC 60364.
- **NORMAM-211/DPC** — embarcações de esporte e recreio (regime amador).
- **NORMAM-201/DPC** — tráfego e permanência (embarcações comerciais).
- **NORMAM-204/DPC** — Segurança da Marinha Mercante.
- **NORMAM-205/DPC** — embarcações de passageiros (charter, travessia).

**Diretiva europeia (recreio, mercado CE):**

- **CE-RCD Directive 2013/53/EU** — *Recreational Craft Directive*: marcação CE obrigatória para embarcações de recreio colocadas no mercado europeu; exige projeto conforme harmonised standards (ISO 13297, ISO 8846, ISO 10134, etc.).

## Glossário rápido

- **ABYC (American Boat & Yacht Council)** — organização norte-americana que edita as normas técnicas voluntárias mais adotadas no projeto elétrico náutico (E-11, E-2, E-8, E-9, E-10, etc.).
- **ABS / Bureau Veritas / Lloyd's Register / RINA** — sociedades classificadoras (IACS) que certificam embarcações comerciais conforme SOLAS + IEC 60092.
- **Alternador de bordo** — gerador DC acoplado ao motor de propulsão; dimensionamento via ABYC E-9 e capacidade de carga do banco.
- **ART (Anotação de Responsabilidade Técnica)** — documento CREA que formaliza responsabilidade do engenheiro sobre o projeto; obrigatória em instalações comerciais e recomendada em recreio > 12 m.
- **As-built** — documentação "como construído": reflete a instalação real (pós-execução), que pode diferir do projeto original; parte obrigatória do dossiê.
- **Banco de baterias** — conjunto de baterias ligadas em série/paralelo para atingir tensão e Ah de projeto (ver [[Dimensionamento de Banco de Baterias — Cálculo de Autonomia]]).
- **BMS (Battery Management System)** — eletrônica embarcada em lítio que gerencia balanceamento, proteção e comunicação; obrigatório em LiFePO4.
- **Bonding (ABYC E-2)** — interligação equipotencial de todas as massas metálicas submersas + gerador + blocos motor + tanques; reduz corrosão galvânica e elimina diferenças de potencial perigosas.
- **Cable tray / Conduíte marine-grade** — encaminhamento organizado dos cabos com suportes a cada 450 mm (ABYC E-11).
- **CAD elétrico (QElectroTech, EPLAN, AutoCAD Electrical)** — software para diagramas unifilares profissionais.
- **Carga parasita** — consumo contínuo de equipamentos em standby (relés, displays, carregadores ociosos): 50-200 W/dia típico; entra no cálculo do banco.
- **CE-RCD (Recreational Craft Directive)** — regulamentação europeia obrigatória para embarcações de recreio; exige declaração de conformidade ICNN + harmonised standards.
- **Classe de proteção IP (IEC 60529)** — grau de proteção contra poeira e água; IP-67 típico para convés, IP-22 para cabine.
- **Curto-circuito nominal (I_cc)** — corrente presumível de falta franca; dimensiona capacidade de interrupção de fusíveis (AIC — Amperage Interrupting Capacity).
- **Diagrama unifilar (single-line diagram)** — representação simplificada do sistema elétrico com barramentos, proteções, cargas e fontes; documento central do projeto.
- **DOD (Depth of Discharge)** — profundidade de descarga: 50% máximo em chumbo-ácido (vida útil), 80% em LiFePO4 (ABYC E-10).
- **DPC (Diretoria de Portos e Costas)** — autoridade marítima brasileira que edita as NORMAM e fiscaliza via CP/DL/AG.
- **ELCI (Equipment Leakage Circuit Interrupter)** — proteção diferencial AC em shore power (ABYC E-11), equivalente a RCD/DR 30 mA.
- **EMC (Compatibilidade Eletromagnética)** — coexistência de sistemas sem interferência; ABYC E-11 + IEC 60533.
- **Fusível classe T / MRBF** — fusíveis de alta AIC (até 20.000 A) exigidos próximos aos bancos LiFePO4 e cabos de partida.
- **Galvanic isolator** — dispositivo em série com o terra do shore power; bloqueia DC galvânica e permite passagem de AC de falta.
- **GFCI (Ground Fault Circuit Interrupter)** — proteção diferencial AC em tomadas (equivalente europeu: RCD; brasileiro: DR).
- **Ignition protection (ISO 8846)** — equipamento classificado para não ignitar vapores de combustível; obrigatório em compartimento de motor gasolina.
- **Inrush current** — corrente de partida transitória (5-8× nominal em motores AC/bombas); dimensiona proteção time-delay.
- **Isolador galvânico vs transformador de isolação** — duas soluções para corrosão galvânica via shore power; transformador é mais caro e mais seguro (isolação total).
- **Kill switch (battery switch)** — chave geral de bateria; exigida por ABYC E-11 em todo circuito DC principal.
- **Load list** — planilha com todos os consumidores (W, V, h/dia, Wh/dia); base do cálculo do banco.
- **MRBF (Marine Rated Battery Fuse)** — fusível de alta AIC instalado diretamente no polo da bateria.
- **NEC (National Electrical Code) Art. 555** — regulamentação AC para marinas nos EUA (referência cruzada para shore power).
- **NMEA 2000 (IEC 61162-3)** — rede digital de instrumentação (CAN bus a 250 kbps); substitui cabeamento analógico ponto-a-ponto.
- **NORMAM (Normas da Autoridade Marítima)** — normas brasileiras DPC; 201 (tráfego), 204 (SMM), 205 (passageiros), 211 (recreio).
- **Payload eletrônico** — equipamentos embarcados (GPS, radar, VHF, autopilot); consumo médio contínuo típico 80-200 W.
- **Peak load vs continuous load** — carga de pico (transitória, inrush) vs contínua; ABYC exige ambos no dimensionamento.
- **Perfil de uso (duty cycle)** — fração do dia em que cada equipamento opera; multiplicador honesto para dimensionar banco.
- **Queda de tensão (voltage drop)** — ΔV = R × I; ABYC E-11 fixa 3% em circuitos críticos (nav, eletrônica, partida) e 10% em não-críticos (iluminação cabine).
- **RCD / DR (Dispositivo Diferencial Residual)** — proteção diferencial 30 mA em AC; equivalente IEC/ABNT ao ELCI/GFCI.
- **Resistividade (ρ) do cobre** — 0,0175 Ω·mm²/m; base do cálculo de seção.
- **Retroengenharia do projeto** — processo de documentar embarcação existente sem projeto original (fotografar, medir, mapear, registrar).
- **Shore power** — alimentação AC externa (marina); exige ATS, isolador galvânico/transformador, ELCI/RCD, polaridade correta.
- **Single-point failure** — componente cuja falha derruba todo o sistema; projeto eletrico robusto deve identificá-los (ex.: barramento positivo único, gerador isolado).
- **Size, Derating e Ampacity** — termos ABYC: Size = bitola AWG/mm², Ampacity = capacidade de corrente contínua, Derating = fator por temperatura ambiente e agrupamento.
- **Surveyor marítimo** — profissional homologado (RBNA, Abracem, IBAPE) para vistoria; avalia projeto vs execução.
- **Tabela VI ABYC E-11** — tabela de ampacity para cabos marine-grade (AWG 18 a 4/0); base primária de dimensionamento.
- **Tabela VI-A ABYC E-11** — tabela de queda de tensão por AWG e comprimento em amp-feet.
- **TBC (Thermal Breaker / Magnetic Breaker / Switchable Fuse)** — tipos de proteção; ABYC E-11 detalha aplicação de cada um.
- **Voltage sag** — queda transitória de tensão durante partida de cargas grandes; deve ser avaliado no projeto.
- **Wet cell vs AGM vs gel vs LiFePO4** — tecnologias de bateria, cada uma com curva de tensão, DOD e ventilação próprias (ABYC E-10).

## Como ensinar este tópico

**Sequência recomendada:**

1. Mostrar embarcação real sem projeto — cabeamento caótico, fusíveis errados, banco subdimensionado
2. Iniciar levantamento de cargas ao vivo — cada equipamento, cada hábito de uso
3. Calcular banco necessário com fórmula simples
4. Gerar primeiro diagrama unifilar simplificado juntos
5. Discutir: quanto custaria um incêndio elétrico vs custo de fazer o projeto

**Conceito-chave para fixar:**

"Projeto não é burocracia — é a diferença entre um barco confiável e um barco que te deixa na mão (ou pior)."

## Ideias de vídeos

- **"Por que 90% das embarcações no Brasil não têm projeto elétrico"** — realidade do mercado
- **"Como fazer o levantamento de cargas do seu barco"** — planilha passo a passo
- **"Dimensionando banco de baterias do zero"** — cálculo prático, sem fórmula complicada
- **"Auditoria elétrica: como encontrar os problemas antes que eles te encontrem"** — checklist ao vivo em embarcação real
- **"Projeto elétrico náutico: do levantamento ao diagrama"** — série completa

## Diagramas sugeridos

- Fluxo do projeto: levantamento → banco → geração → cabos → proteções → diagrama → layout
- Template de Load List (planilha modelo com todas as colunas necessárias)
- Exemplo de diagrama unifilar simplificado (DC + AC com legenda clara)
- Fórmula visual de dimensionamento de banco: consumo × autonomia ÷ DOD = capacidade

## FAQ

**Preciso de engenheiro para fazer o projeto?**

Para embarcações de recreio, não há exigência legal de ART. Mas um projeto feito por profissional qualificado (eletricista náutico ou engenheiro especializado) tem muito mais valor em caso de sinistro ou venda.

**O projeto precisa ser refeito se eu mudar equipamentos?**

Sim, sempre que equipamentos forem adicionados ou substituídos. Um projeto desatualizado é pior que nenhum — dá falsa segurança.

**Existe software gratuito para projeto elétrico náutico?**

QElectroTech é gratuito e serve para diagramas unifilares. Para dimensionamento, uma planilha bem organizada no Excel/Sheets resolve. Software dedicado como o da Victron (para sistemas Victron) é gratuito.

**Qual é o erro mais caro por falta de projeto?**

Incêndio elétrico. Segundo estatísticas da BOAT/US (EUA), problemas elétricos são a principal causa de incêndio a bordo — e a maioria é prevenível com projeto adequado.

**Como fazer retroengenharia do projeto de uma embarcação sem documentação?**

Fotografar todo o sistema, medir correntes com alicate amperímetro, identificar bitolas, mapear fusíveis. É trabalhoso mas viável. A partir daí, gerar o documento de retroengenharia e atualizar com cada intervenção.

## Visual didático

![Projeto eletrico: fluxo de entregaveis](../_visuals/generated/projeto-eletrico-fluxo-entregaveis.svg)

Mostrar que projeto eletrico nautico nao e uma lista de equipamentos, mas uma sequencia auditavel de decisoes tecnicas.

**Cautela:** Este fluxo e uma estrutura editorial e didatica. O projeto real deve considerar normas aplicaveis, manual dos fabricantes, vistoria e condicoes da embarcacao.

Material de apoio: [Projeto eletrico: fluxo de entregaveis](../_visuals/generated/projeto-eletrico-fluxo-entregaveis.md)

## Integração com outras notas

- [[Tipos de Embarcação]]
- [[DC vs AC — Corrente Contínua e Alternada]]
- [[Diagrama Unifilar — Documentação do Sistema Elétrico]]
- [[Dimensionamento de Banco de Baterias — Cálculo de Autonomia]]
- [[Dimensionamento de Cabos DC — Cálculo Prático]]
- [[Fase e Neutro]]
- [[Ferramentas do Eletricista Náutico]]
- [[Inspeção de Cabos Terminais e Conexões]]

## Perguntas que esta nota responde

- O que é Projeto Elétrico de Embarcação — Passo a Passo em instalações elétricas náuticas?
- Qual é a função de Projeto Elétrico de Embarcação — Passo a Passo na embarcação?

