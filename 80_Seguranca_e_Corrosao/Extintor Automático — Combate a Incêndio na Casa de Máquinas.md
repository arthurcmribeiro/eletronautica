---
title: "Extintor Automático — Combate a Incêndio na Casa de Máquinas"
note_type: "technical-note"
domain: "80_Seguranca_e_Corrosao"
source_file: "EXTINTOR AUTOMÁTICO — COMBATE A INCÊNCIO NA CASA D 33a19734f7fb819ca540d12e729e7ba5.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "37"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
  - "internacional"
normas_citadas:
  - "ABYC A-4 (2021) — Fire Fighting Equipment"
  - "ABYC A-14 — Fire Extinguishers (portable)"
  - "ABYC A-23 — Fire Suppression Equipment (fixed systems) — referenciada"
  - "ABYC A-25 — Gasoline Fuel Systems (referência cruzada)"
  - "ABYC A-26 — LPG/CNG Systems (referência cruzada)"
  - "ABYC H-22 — Electric Bilge Pumps (referência cruzada)"
  - "ABYC P-1 — Exhaust Systems"
  - "ABYC E-11 (2023) — AC & DC Electrical Systems (disparo + intertravamento)"
  - "ISO 9094:2017 — Small craft — Fire protection"
  - "ISO 14520-1:2015 — Gaseous fire-extinguishing systems — General"
  - "ISO 14520-9 — HFC-227ea extinguishing systems"
  - "ISO 14520-15 — IG-01 (Argon)"
  - "SOLAS Chapter II-2 — Construction — Fire protection, detection and extinction (navio > 500 GT)"
  - "IMO FSS Code — International Code for Fire Safety Systems"
  - "IMO MSC.1/Circ.1516 — Unified Interpretation of Chapter II-2"
  - "IMO MSC/Circ.1165 — Revised Guidelines for Fixed Gas Fire-Extinguishing Systems"
  - "NFPA 302 — Fire Protection Standard for Pleasure and Commercial Motor Craft"
  - "NFPA 10 — Standard for Portable Fire Extinguishers"
  - "NFPA 2001 — Standard on Clean Agent Fire Extinguishing Systems"
  - "NFPA 12 — Standard on Carbon Dioxide Extinguishing Systems"
  - "NFPA 17 — Standard for Dry Chemical Extinguishing Systems"
  - "NFPA 72 — National Fire Alarm and Signaling Code"
  - "USCG 46 CFR Subchapter K / Subchapter T — Small Passenger Vessels"
  - "USCG 33 CFR Part 183 — Boats and Associated Equipment"
  - "UL 2166 — Clean Agent Extinguishing Systems (Halocarbon)"
  - "UL 2127 — Inert Gas Clean Agent Extinguishing Systems"
  - "FM 5600 — Clean Agent Extinguishing System Components"
  - "EN 15004 — Clean agent fire extinguishing systems"
  - "DNV-CG-0080 Pt 3 — Fire Safety"
  - "Lloyd's Register Rules — Fire Safety"
  - "ABS Steel Vessel Rules — Fire Safety"
  - "NBR 15808 — Extintores portáteis de incêndio"
  - "NBR 12962 — Inspeção e manutenção de extintores"
  - "NBR 17240 — Sistemas de detecção e alarme de incêndio"
  - "NR-23/MTE — Proteção contra incêndios"
  - "NORMAM-211/DPC — Esporte e recreio"
  - "NORMAM-201/204/DPC — Comercial / SMM"
  - "CE-RCD Directive 2013/53/EU — Recreational Craft Directive"
  - "EPA SNAP (Significant New Alternatives Policy) — Halon phase-out"
  - "Protocolo de Montreal — Halon 1301 phase-out"
  - "AIM Act (American Innovation and Manufacturing) — HFC phase-down"
review_level: "engineering-curated"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "EXTINTOR AUTOMÁTICO — COMBATE A INCÊNDIO NA CASA DE MÁQUINAS"
  - "Sistema fixo de supressão"
  - "Fire suppression engine room"
seo_title: "Extintor automático na casa de máquinas: projeto, disparo e integração"
seo_description: "Guia técnico sobre sistemas fixos automáticos de supressão de incêndio em casa de máquinas: agentes limpos, volume protegido, desligamentos automáticos, inspeção e operação segura."
seo_keywords:
  - "extintor automático casa de máquinas"
  - "fire suppression embarcação"
  - "supressão fixa incêndio engine room"
  - "FM-200 Novec barco"
geo_queries:
  - "Como funciona o extintor automático da casa de máquinas em embarcações?"
  - "Quais cuidados técnicos existem na instalação de supressão automática de incêndio no compartimento do motor?"
related_notes:
  - "Blower"
  - "Casa de Máquinas e Paiol"
  - "Detector de CO — Monóxido de Carbono"
  - "Detector de Gás GLP - GN"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
  - "Sistema de Alarme Geral - Painel de Alarmes"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
---

# Extintor Automático — Combate a Incêndio na Casa de Máquinas

> [!abstract] Resumo técnico
> Sistema fixo automático de supressão de incêndio em casa de máquinas é um subsistema de segurança crítica, normalmente pré-engenheirado, dimensionado para um volume de compartimento e integrado a alarmes, desligamentos e procedimentos operacionais. Não é "um extintor preso no teto": é um sistema que precisa funcionar mesmo quando ninguém consegue entrar no compartimento.

> [!tip] Regra de decisão em 30 segundos
> 1. **Sistema pré-engenheirado dimensionado por VOLUME do compartimento + agente + quantidade de bicos** — não é "um cilindro qualquer"; fabricante calcula por m³ via tabela de concentração de projeto (FK-5-1-12: 4,2–5,9 %; HFC-227ea: 7,0–9,0 %).
> 2. **Agente limpo para recreio: FM-200 (HFC-227ea) legado / Novec 1230 (FK-5-1-12) moderno** — CO₂ em espaço ocupado = risco asfixia; Halon 1301 fase out Protocolo de Montreal (ainda legalmente reciclado, mas sem nova instalação).
> 3. **Integração OBRIGATÓRIA ao disparar: desliga motor + gerador + blower + ventilação** — sem isso, motor puxa ar e o agente não mantém concentração; "hold time" mínimo 10 min conforme NFPA 2001.
> 4. **Ativação por descarga térmica (glass bulb 79°C, 93°C, 141°C) ou detector térmico ativo** — frangível sob temperatura de projeto + acionamento manual redundante (cabo + botão).
> 5. **Pós-disparo: NÃO abrir compartimento** — reintroduz O₂ e reinicia fogo; esperar 30–45 min + aproximar com EPI + ventilar controlado com blower reverso.
> 6. **Inspeção mensal visual (pressão + integridade), anual profissional, hidrostático 5–12 anos** — cilindro descarregado = sem proteção; pesar (balança) + manômetro + data de validade.
> 7. **Extintor portátil (ABYC A-14) + extintor fixo (ABYC A-4) são complementares, NÃO substitutos** — portátil para cockpit, galley, salão; fixo para casa de máquinas fechada.
> 8. **Comercial > 24 m / SOLAS II-2** — sistema precisa ser homologado por classificadora (DNV, BV, LR, RINA, ABS) + FSS Code + laudo anual; não basta comprar caixa ABYC.
> 9. **Charter/aluguel Brasil: NORMAM-201/211 + NBR 17240 + NR-23 + extintores NBR 15808/12962** — documentação rastreável é tão importante quanto sistema funcional.

> [!danger] Quando chamar emergência / especialista
> 1. **Fumaça visível ou cheiro de queimado em casa de máquinas durante navegação** — EMERGÊNCIA: desligar motor imediatamente, NÃO abrir o compartimento, acionar disparo manual se automático atrasar, preparar extintor portátil na aproximação; radiar Mayday se fogo persistir.
> 2. **Falha de disparo automático durante incêndio** — acionamento manual via cabo + botão; se falhar, combate pela porta com extintor portátil mantendo abertura mínima + EPI; abandono como opção se não controlar em 3 min.
> 3. **Sistema sem manutenção documentada > 1 ano** — antes da próxima operação, inspeção profissional completa; qualquer incidente com sistema não-conforme vira responsabilidade civil/penal + perda de seguro.
> 4. **Retrofit de motor maior (troca de propulsão) em casa de máquinas existente sem revisão do sistema fixo** — volume protegido pode estar subdimensionado; recalcular concentração de projeto; reinstalar conforme novo layout.
> 5. **Casa de máquinas com ventilação permanente (furo, frincha, dreno aberto)** — concentração do agente não se estabelece no tempo de hold; selar aberturas ou instalar dampers automáticos fechados no disparo.
> 6. **CO₂ em embarcação recreativa com compartimento acessível a pessoas** — risco alto de asfixia; pre-discharge alarm + evacuação obrigatória + sinal visual/sonoro 30 s antes de descarga; considerar troca por clean agent.
> 7. **Charter/aluguel/escola náutica sem sistema ou com sistema vencido** — responsabilidade civil e penal em caso de incêndio com vítima; ABYC A-4 + NFPA 302 + NORMAM-201 exigem sistema + extintores; NR-23 exige brigada.
> 8. **Perícia pós-incêndio com suspeita de falha do sistema** — preservar: cilindro (pesar), bicos, tubulação, cabos elétricos, glass bulb ou detector; laudo IBAPE + perito Abracem + corpo de bombeiros; cadeia de custódia.
> 9. **Embarcação comercial classificada > 24 m sem certificação SOLAS II-2 + classificadora vigente** — operação ilegal; vistoria anual + hidrostático + testes funcionais documentados; apólice de seguro exige comprovação.

## O que é

É um sistema fixo destinado a detectar condição térmica de incêndio e descarregar agente extintor no compartimento protegido, normalmente a casa de máquinas ou um compartimento técnico equivalente.

Em embarcações de recreio, os arranjos mais comuns usam:

- cilindro pressurizado com agente limpo;
- elemento de atuação térmica ou detector/sistema equivalente;
- descarga por bico difusor;
- indicação de condição do cilindro;
- integração com alarme e, em sistemas mais completos, com disparo remoto e desligamentos automáticos.

## O que ele deve proteger

O foco principal é o compartimento onde coexistem:

- combustível;
- superfícies quentes;
- óleo;
- alternadores, starters, cabeamento e equipamentos elétricos;
- motores, geradores e exaustão.

Esse conjunto faz da casa de máquinas o local mais crítico da embarcação para incêndio oculto.

## O que muda de um sistema profissional para um improvisado

Sistema profissional considera:

- volume real protegido;
- estanqueidade relativa do compartimento;
- agente correto para a aplicação;
- posição dos bicos;
- integração com alarme;
- lógica de desligamento de motores, geradores e ventilação;
- manutenção certificada.

Sistema improvisado foca só no cilindro e esquece todo o resto.

## Agentes mais comuns

Nas embarcações de recreio, predominam agentes limpos. Em termos práticos:

- HFC-227ea/FM-200 aparece amplamente em sistemas legados e ainda é muito encontrado;
- FK-5-1-12/Novec 1230 aparece como solução moderna de agente limpo;
- CO2 existe, mas exige muito mais cautela por risco de asfixia e por características de aplicação.

A escolha do agente não deve ser feita só por preço. Devem entrar na análise:

- compatibilidade com ocupação humana;
- volume do compartimento;
- requisitos do fabricante do sistema;
- disponibilidade de manutenção e recarga;
- implicações ambientais e regulatórias.

## Dimensionamento correto

Em sistemas pré-engenheirados, o dimensionamento não deve ser reduzido a fórmula genérica de internet. O procedimento correto é seguir a tabela e o manual do fabricante para:

- volume máximo protegido;
- altura e geometria do compartimento;
- tipo de agente;
- número e tipo de bicos;
- temperatura de projeto;
- restrições de instalação.

Compartimento com ventilação aberta, passagem excessiva ou volume mal calculado compromete a concentração efetiva do agente.

## Integração obrigatória ou fortemente recomendável

Em projeto sério, o disparo do sistema deve conversar com outros subsistemas. Os mais importantes são:

- alarme visual e sonoro;
- desligamento de motores principais e auxiliares, quando aplicável;
- desligamento de geradores;
- parada de ventiladores e [[Blower]];
- fechamento ou bloqueio de ventilação forçada, quando a arquitetura do barco exigir;
- indicação no [[Sistema de Alarme Geral - Painel de Alarmes]].

Sem isso, o agente pode ser descarregado enquanto:

- o compartimento continua sendo ventilado;
- o motor segue puxando ar;
- a fonte de ignição continua ativa.

## Operação correta

Após disparo, a regra prática é:

- não abrir o compartimento imediatamente;
- não religar motor, gerador ou ventilação sem avaliação;
- ventilar e inspecionar de forma controlada;
- tratar o disparo como evento sério, não como falsa falha até prova contrária.

Abrir a casa de máquinas cedo demais pode reintroduzir oxigênio e reiniciar o incêndio.

## Inspeção e manutenção

Verificações típicas incluem:

- indicador de pressão, quando existente;
- massa do cilindro, quando aplicável;
- validade e conformidade da manutenção;
- integridade de suportes, bicos e linhas;
- condição do dispositivo de atuação térmica;
- teste funcional dos alarmes e intertravamentos sem descarregar agente;
- revisão profissional conforme manual e legislação aplicável.

Periodicidade exata depende do sistema, do agente, do fabricante e da jurisdição. Não é profissional tratar "recarregar a cada x anos" como verdade universal.

## Falhas típicas em campo

As mais comuns são:

- cilindro sem carga adequada;
- sistema instalado para volume maior do que consegue proteger;
- bico mal posicionado;
- ventilação não interrompida;
- motor/gerador continuando em funcionamento após disparo;
- sistema presente, mas sem manutenção real;
- tripulação sem procedimento claro de resposta.

## Diagnóstico profissional

O diagnóstico deve responder:

1. O compartimento está dentro do envelope do sistema instalado?
2. O agente e o modelo são adequados para a aplicação?
3. Há integração funcional com alarme, ventilação e desligamento?
4. A manutenção está rastreável e compatível com o fabricante?
5. A tripulação sabe o que fazer antes, durante e depois do disparo?

## Boas práticas

- usar sistema de fabricante reconhecido e manual disponível;
- dimensionar pelo volume e pela configuração real do compartimento;
- prever desligamento e bloqueio de ventilação conforme projeto;
- manter extintores portáteis complementares para outras áreas;
- registrar inspeções e manutenções;
- treinar resposta operacional do proprietário ou tripulação.

## Erros comuns

Os mais perigosos são:

- comprar o cilindro sem fechar a lógica de desligamentos;
- assumir que qualquer cilindro serve para qualquer casa de máquinas;
- manter o sistema sem inspeção formal;
- abrir o compartimento imediatamente após descarga;
- confundir proteção automática fixa com substituição total dos extintores portáteis.

## Referências de projeto

Para esta nota, o ponto mais seguro é sempre remeter ao conjunto:

- manual do fabricante do sistema;
- regulamentação aplicável à classe e ao tipo da embarcação;
- requisitos de integração com motores, geradores e ventilação.

## Normas aplicáveis (organizadas por família)

Sistema fixo de combate a incêndio em casa de máquinas cruza cinco áreas normativas: **embarcação recreativa** (ABYC, ISO 9094, NFPA 302), **sistema de agente limpo** (NFPA 2001, ISO 14520, UL 2166, EN 15004), **embarcação comercial** (SOLAS II-2, FSS Code, classificadoras), **extintores portáteis** (NFPA 10, ABYC A-14, NBR 15808/12962), **jurisdição local** (NORMAM, NR-23).

### ABYC (American Boat & Yacht Council) — recreio USA

- **ABYC A-4 (2021) — Fire Fighting Equipment** — norma central para sistema fixo e portátil em recreio USA; define tipos de compartimento, classificação de fogo, requisitos mínimos.
- **ABYC A-14 — Fire Extinguishers (portable)** — complementa A-4; exigências de extintor portátil classe B/C; quantidades mínimas por LOA.
- **ABYC A-23 — Fire Suppression Equipment (fixed systems)** — referência específica para sistemas fixos; integração com motor/ventilação.
- **ABYC A-25 — Gasoline Fuel Systems** — referência cruzada; motor a gasolina tem maior risco de deflagração.
- **ABYC A-26 — LPG and CNG Fueled Appliances** — referência cruzada; risco de gás combustível.
- **ABYC H-22 — Electric Bilge Pumps** — referência cruzada; bomba de porão durante incêndio.
- **ABYC P-1 — Installation of Exhaust Systems** — estanqueidade do escape; previne fogo a bordo.
- **ABYC E-11 (2023) — AC & DC Electrical Systems on Boats** — alimentação do disparo + intertravamento elétrico do motor/gerador.

### ISO (internacional, pequena embarcação)

- **ISO 9094:2017 — Small craft — Fire protection** — equivalente internacional de ABYC A-4; obrigatório para certificação CE.
- **ISO 14520-1:2015 — Gaseous fire-extinguishing systems — General** — norma guarda-chuva de sistemas de agente limpo.
- **ISO 14520-9 — HFC-227ea extinguishing systems (FM-200)** — específico para sistemas HFC-227ea.
- **ISO 14520-5 — FK-5-1-12 (Novec 1230) extinguishing systems**
- **ISO 14520-15 — IG-01 (Argon) extinguishing systems**

### NFPA (USA, referência técnica dominante)

- **NFPA 302 — Fire Protection Standard for Pleasure and Commercial Motor Craft** — norma central para embarcação motor recreativa/comercial; aplicação USA.
- **NFPA 10 — Portable Fire Extinguishers** — padrão de extintor portátil; seleção, instalação, manutenção, inspeção, recarga.
- **NFPA 2001 — Clean Agent Fire Extinguishing Systems** — norma técnica para sistemas de agente limpo (HFC, FK, inert gas); define concentração, hold time, enclosure integrity, door fan test.
- **NFPA 12 — Carbon Dioxide Extinguishing Systems** — para sistemas CO₂; inclui pre-discharge alarm, evacuação, sinalização.
- **NFPA 17 — Dry Chemical Extinguishing Systems** — pó químico (BC, ABC); menos comum em recreio moderno.
- **NFPA 72 — National Fire Alarm and Signaling Code** — código de detecção e alarme; integração com sistema fixo.

### IMO / SOLAS (embarcação comercial internacional > 24 m ou > 500 GT)

- **SOLAS Chapter II-2 — Construction — Fire protection, detection and extinction** — capítulo central de segurança contra incêndio em navio mercante.
- **IMO FSS Code — International Code for Fire Safety Systems** — obrigatório; Chapter 5 cobre sistemas fixos a gás.
- **IMO MSC.1/Circ.1516 — Unified Interpretation of Chapter II-2** — interpretação unificada de detalhes operacionais.
- **IMO MSC/Circ.1165 — Revised Guidelines for the Approval of Equivalent Fixed Gas Fire-Extinguishing Systems** — aprovação de sistemas alternativos ao Halon 1301.
- **IMO MSC/Circ.1312 — Revised Guidelines for CO₂ Fixed Systems**.

### USCG (USA, comercial)

- **USCG 46 CFR Subchapter K — Small Passenger Vessels Carrying More Than 150 Passengers** — embarcação pequena de passageiros.
- **USCG 46 CFR Subchapter T — Small Passenger Vessels Under 100 GT** — charter, escola náutica.
- **USCG 33 CFR Part 183 — Boats and Associated Equipment** — regulamento federal embarcação recreativa.

### Certificação de componentes (USA)

- **UL 2166 — Clean Agent Extinguishing Systems (Halocarbon)** — certificação USA para sistemas com HFC-227ea, FK-5-1-12, HFC-125, HFC-23.
- **UL 2127 — Inert Gas Clean Agent Extinguishing Systems** — certificação para sistemas IG-01, IG-100, IG-55, IG-541 (Inergen).
- **UL 300 — Fire Testing of Fire Extinguishing Systems (commercial cooking equipment)** — para sistemas de galley comercial (wet chemical).
- **FM 5600 — Clean Agent Extinguishing System Components** — certificação FM Global para componentes.

### Europa

- **EN 15004-1 — Clean agent fire extinguishing systems — General** — equivalente europeu de NFPA 2001.
- **EN 15004-2 — HFC-227ea extinguishing systems**
- **EN 15004-5 — FK-5-1-12 extinguishing systems**
- **EN 12094 — Components for clean agent systems**
- **CE-RCD Directive 2013/53/EU — Recreational Craft Directive** — exige conformidade a ISO 9094.

### Sociedades classificadoras (comercial)

- **DNV-CG-0080 Pt 3 — Fire Safety** — classe notation DNV para proteção contra incêndio.
- **Lloyd's Register Rules for Ships Pt 6 Ch 4** — Fire Safety.
- **ABS Steel Vessel Rules Pt 5-1 Ch 7** — Fire Safety Systems.
- **Bureau Veritas Rules NR 467 Pt C Ch 4** — Fire Safety.
- **RINA Rules Pt C Ch 4** — Fire Protection.

### Brasil (norma técnica e trabalhista)

- **NBR 15808 — Extintores portáteis de incêndio** — requisitos, seleção, instalação.
- **NBR 12962 — Inspeção, manutenção e recarga em extintores de incêndio** — periodicidade, rastreabilidade.
- **NBR 17240 — Sistemas de detecção e alarme de incêndio** — projeto, instalação, manutenção.
- **NR-23/MTE — Proteção contra incêndios** — regulamento trabalhista; aplicável a charter, escola náutica.
- **NORMAM-211/DPC — Esporte e recreio** — regulamento DPC; inclui equipamento mínimo de segurança.
- **NORMAM-201/204/DPC — Comercial / SMM** — embarcação classificada; exige sistema conforme classificadora.

### Regulatório ambiental (agente extintor)

- **Protocolo de Montreal — Halon 1301 phase-out** — proibida nova produção; reciclado disponível.
- **EPA SNAP (Significant New Alternatives Policy)** — USA; lista agentes aprovados substitutos de Halon.
- **AIM Act (American Innovation and Manufacturing)** — HFC phase-down (reduz HFC-227ea, HFC-125 progressivamente).
- **Regulation (EU) 517/2014** — F-gas regulation; limita HFC na Europa.

### Como usar este conjunto normativo na prática

| Situação | Norma-chave |
|---|---|
| Projeto novo recreio USA | ABYC A-4 + NFPA 302 + NFPA 2001 + UL 2166 |
| Projeto comercial < 24m | NFPA 302 + USCG 46 CFR Subchapter T |
| Projeto comercial > 24m / > 500 GT | SOLAS II-2 + FSS Code + classificadora |
| Embarcação CE Europa | ISO 9094 + EN 15004 + RCD |
| Recreio Brasil | ABYC A-4 + NBR 15808/12962/17240 + NORMAM-211 |
| Charter / aluguel Brasil | NORMAM-201 + NR-23 + extintores NBR + sistema ABYC |
| Retrofit motor > volume existente | ISO 14520 + recálculo NFPA 2001 concentração |
| Seleção agente limpo moderno | FK-5-1-12 (Novec 1230) > HFC-227ea (GWP) |
| Perícia pós-incêndio | IBAPE + Abracem + bombeiros + preservação |
| Inspeção anual | NBR 12962 + fabricante + rastreabilidade |

## Glossário rápido

### Agentes extintores

- **Agente limpo (Clean Agent)** — gás extintor sem resíduo elétrico-condutivo; seguro para equipamento eletrônico; categoria reconhecida NFPA 2001 e ISO 14520.
- **HFC-227ea / FM-200** — heptafluoropropano; agente limpo dominante em sistemas legados (2000–2020); concentração de projeto ~7,0–9,0 %; GWP 3.350.
- **FK-5-1-12 / Novec 1230 (3M)** — fluoroketona; agente moderno sustentável; concentração 4,2–5,9 %; GWP < 1; vida atmosférica 5 dias.
- **HFC-125 / ECARO-25** — pentafluoroetano; alternativa a FM-200; GWP 3.500.
- **CO₂ (dióxido de carbono)** — agente tradicional inerte; extingue por deslocamento de oxigênio; concentração de projeto 34–62 %; RISCO ASFIXIA em espaço ocupado.
- **Halon 1301 (BTM)** — bromotrifluorometano; agente histórico; PROIBIDO Protocolo de Montreal (nova produção); ainda permitido em sistemas com reciclagem certificada.
- **IG-01 (Argon)** — gás inerte puro; 100 % Ar; concentração 40–52 %.
- **IG-100 (Nitrogênio)** — 100 % N₂; concentração 40–43 %.
- **IG-55 (Argonite)** — 50 % N₂ + 50 % Ar.
- **IG-541 (Inergen)** — 52 % N₂ + 40 % Ar + 8 % CO₂.

### Conceitos de concentração (NFPA 2001, ISO 14520)

- **Design concentration (concentração de projeto)** — concentração mínima requerida no compartimento para extinguir a classe de fogo + fator de segurança.
- **Extinguishing concentration** — concentração mínima determinada experimentalmente em cup-burner test.
- **NOAEL (No Observed Adverse Effect Level)** — concentração sem efeito fisiológico observável em humano; limite superior em espaço ocupado.
- **LOAEL (Lowest Observed Adverse Effect Level)** — concentração com primeiro efeito fisiológico; limite absoluto.
- **Hold time (tempo de retenção)** — tempo que a concentração se mantém após descarga; mínimo 10 min NFPA 2001.
- **Enclosure integrity (integridade do compartimento)** — capacidade de manter concentração; medida por door fan test (peel test).
- **Door fan test / peel test** — teste com ventilador em porta para medir vazamento; ESTA (Enclosure Integrity Test) ou NFPA 2001 Annex C.

### Componentes do sistema

- **Glass bulb (bulbo de vidro frangível)** — detector mecânico; líquido térmico expande e quebra vidro a temperatura específica (57 °C, 68 °C, 79 °C, 93 °C, 141 °C, 182 °C, 227 °C).
- **Fusible link (elo fusível)** — metal soldado que derrete a temperatura específica; detector térmico mecânico.
- **Detector térmico ativo (rate-of-rise + fixed temperature)** — eletrônico; dispara sistema via painel; redundância com glass bulb.
- **Detector de fumaça (smoke detector)** — não usado em casa de máquinas (vapor de óleo confunde); reservado para cabine.
- **Acionamento manual (manual release)** — cabo mecânico + botão elétrico; obrigatório em NFPA 2001 como redundância.
- **Pressure gauge (manômetro)** — indicador de carga do cilindro; verde = pressão nominal.
- **Siphon tube** — tubo interno do cilindro; alcance do agente líquido.
- **Distribuidor / manifold** — tubulação que conecta cilindros aos bicos.
- **Nozzle (bico)** — difusor final; orifício calibrado.
- **Orifice plate (placa de orifício)** — calibração de vazão por bico.
- **Discharge time (tempo de descarga)** — tipicamente 10 s para halocarbon, 60–120 s para inert gas.
- **Pre-discharge alarm** — alarme sonoro + visual antes da descarga (30 s típico); evacuação obrigatória em sistemas CO₂.
- **Abort switch** — botão para cancelar descarga durante pré-alarme.
- **Manual bypass** — chave para isolar sistema durante manutenção.
- **Tamper indicator** — selo de integridade; rompimento revela manipulação.

### Teste e manutenção

- **Hydrostatic test** — teste hidrostático do cilindro a 1,5× pressão de trabalho; periodicidade 5–12 anos conforme agente/norma (CO₂: 5 anos; HFC: 12 anos).
- **Recarga / refill** — agente + pressurização após disparo; técnico certificado + balança.
- **Weight check** — pesagem periódica do cilindro; perda > 5 % = recarga obrigatória.
- **Functional test** — teste de intertravamento elétrico (shutdown) sem descarga do agente; simulação.
- **Certificação DNV / ABS / LR / BV / RINA** — aprovação para comercial classificada.
- **Service tag / etiqueta de serviço** — registro de inspeção, data, técnico.

### Intertravamento elétrico (shutdown)

- **Engine shutdown (shutdown de motor)** — corta alimentação de combustível + ignição; relé aciona solenoide na bomba ou válvula de combustível.
- **Ventilation damper (damper de ventilação)** — damper automático que fecha ao disparo do sistema; mantém hold time.
- **Fire door / damper** — porta ou damper corta-fogo.
- **Bilge pump auto-off** — pode continuar (alguns projetos), mas blower DEVE desligar.

### Padrões ambientais (regulatório)

- **GWP (Global Warming Potential)** — potencial de aquecimento global relativo ao CO₂ em 100 anos; FM-200 = 3.350; Novec 1230 = 1.
- **ODP (Ozone Depletion Potential)** — potencial de destruição de ozônio; Halon 1301 = 16; HFC = 0.
- **Kigali Amendment (2016)** — emenda ao Protocolo de Montreal; reduz HFC progressivamente.
- **AIM Act (2020)** — lei americana de redução de HFC.
- **Regulation (EU) 517/2014** — F-gas regulation Europa.

### Padrões de classes de fogo (base NFPA 10 / ISO 3941)

- **Classe A** — sólidos (madeira, papel, tecido).
- **Classe B** — líquidos inflamáveis (gasolina, diesel, óleo).
- **Classe C** — gases inflamáveis (GLP, GN).
- **Classe D** — metais (Mg, Na, K).
- **Classe K (USA) / F (Europa)** — óleo de cozinha (galley).
- **Classe elétrica** — energizado; clean agent + CO₂ são seguros; água/foam NÃO.

### Tipos de sistema

- **Pre-engineered system** — sistema com projeto pré-definido pelo fabricante; limites de volume, número de bicos, comprimento de tubo tabelados; recreio típico.
- **Engineered system** — sistema projetado por engenheiro de incêndio para compartimento específico; comercial > 24 m.
- **Total flooding (inundação total)** — descarga que preenche todo o compartimento; padrão para casa de máquinas.
- **Local application** — descarga direcionada a equipamento específico; rarissimo em marítimo.
- **Combined agent system** — agente gasoso + spray de água; sistemas especializados comerciais.

## Visual didático

![Extintor automatico: deteccao e resposta](../_visuals/generated/extintor-automatico-casa-maquinas.svg)

Mostrar extintor automatico como parte de um sistema de resposta, nao como item isolado.

**Cautela:** Sistema de combate a incendio deve seguir fabricante, classe de agente, volume protegido, inspecao e requisitos aplicaveis.

Material de apoio: [Extintor automatico: deteccao e resposta](../_visuals/generated/extintor-automatico-casa-maquinas.md)

## Integração com outras notas

- [[Blower]]
- [[Casa de Máquinas e Paiol]]
- [[Detector de CO — Monóxido de Carbono]]
- [[Detector de Gás GLP - GN]]
- [[Quadro Elétrico e Painel de Distribuição AC-DC]]
- [[Sistema de Alarme Geral - Painel de Alarmes]]
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]]

## Perguntas que esta nota responde

- O que diferencia um sistema fixo de supressão realmente correto de um cilindro apenas instalado?
- Por que desligar motor e ventilação faz parte da eficácia do sistema?
- Que pontos precisam ser verificados para dizer que a proteção da casa de máquinas é confiável?
