---
title: "Ar-Condicionado Marine 12V DC"
note_type: "technical-note"
domain: "70_Hidraulica_Climatizacao_e_Utilidades"
source_file: null
status: "fase-5-reescrita-premium"
fase_6_reescrita: "44"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
  - "internacional"
normas_citadas:
  - "ABYC E-11 (2023) — AC & DC Electrical Systems on Boats"
  - "ABYC A-6 — Standard for Ground Fault Protection"
  - "ABYC A-26 — Heating systems (cross-ref — ciclo reverso)"
  - "ABYC A-31 — Battery Chargers and Inverters (cross-ref — gestão DC)"
  - "ABYC E-13 — Lithium Ion Batteries (integração banco lítio)"
  - "ABYC H-2 — Ventilation"
  - "ABYC H-27 — Seacocks, Thru-Hull Connections (condensação SW, quando houver)"
  - "ISO 10133:2020 — Small craft — Electrical systems — Extra-low voltage DC"
  - "ISO 13297:2020 — Small craft — Electrical systems — AC and DC"
  - "ISO 8846:2020 — Electrical devices — Protection against ignition"
  - "ISO 9093:2022 — Small craft — Seacocks and through-hull fittings"
  - "ISO 16315:2016 — Small craft — Electric propulsion system (cross-ref DC alta corrente)"
  - "IEC 60335-2-40 — Household and similar electrical appliances — Safety — Heat pumps, air-conditioners and dehumidifiers"
  - "IEC 60068-series — Environmental testing"
  - "IEC 62133 — Secondary cells and batteries (cross-ref para lítio)"
  - "IEC 62619 — Lithium batteries for industrial applications"
  - "EN 14511 — Air conditioners, liquid chilling packages and heat pumps — Testing and rating"
  - "EN 378 — Refrigerating systems and heat pumps — Safety and environmental requirements"
  - "ASHRAE 15 — Safety Standard for Refrigeration Systems"
  - "ASHRAE 34 — Designation and Safety Classification of Refrigerants"
  - "ASHRAE 62.1 — Ventilation for Acceptable Indoor Air Quality"
  - "AHRI 210/240 — Performance Rating of Unitary Air-Conditioning Equipment"
  - "UL 484 — Room Air Conditioners"
  - "UL 1995 — Heating and Cooling Equipment"
  - "UL 60335-2-40 — Safety of heat pumps, air-conditioners"
  - "UL 1500 — Ignition-Protected Marine Products"
  - "UL 1426 — Electrical Cables for Boats"
  - "NFPA 302 — Pleasure and Commercial Motor Craft"
  - "NFPA 70 (NEC) — National Electrical Code"
  - "NEC Art. 440 — Air-conditioning and refrigerating equipment"
  - "NEC Art. 551 — RV Parks e Art. 553 (referência cruzada de sistemas DC veiculares)"
  - "NBR 5410:2004 + emendas — Instalações elétricas de baixa tensão"
  - "NBR 16401-1/-2/-3 — Instalações de ar-condicionado"
  - "NBR 15960 — Sistemas de refrigeração com uso de refrigerantes inflamáveis"
  - "NBR 13971 — Sistemas de refrigeração, condicionamento de ar e ventilação — Manutenção programada"
  - "Protocolo de Montreal — Substâncias que destroem a camada de ozônio"
  - "Emenda de Kigali (2016) — Phase-down de HFCs"
  - "EPA SNAP Program — Significant New Alternatives Policy"
  - "AIM Act (USA, 2020) — HFC phase-down"
  - "EU F-gas Regulation (EU) 517/2014"
  - "Section 608 Technician Certification (EPA, 40 CFR Part 82 Subpart F)"
  - "Resolução CONAMA 267/2000 — Substâncias que destroem a camada de ozônio (Brasil)"
  - "CE-RCD Directive 2013/53/EU — Recreational Craft Directive"
  - "ECE R10 Rev.6 — Electromagnetic compatibility (cross-ref equipamento DC veicular/marine)"
  - "NORMAM-211/DPC — Esporte e recreio"
  - "NORMAM-201/204/DPC — Comercial / SMM"
review_level: "engineering-curated"
aliases:
  - "AR-CONDICIONADO 12V"
  - "AC DC marine"
  - "BLDC AC marine"
  - "Compressor inverter 12V marine"
seo_title: "Ar-condicionado marine 12V DC: quando faz sentido, dimensionamento e falhas"
seo_description: "Guia técnico sobre AC 12V DC marine: compressor BLDC inverter, integração com banco lítio, vantagens em ancoragem prolongada, limites reais e falhas típicas."
seo_keywords:
  - "ar condicionado 12v barco"
  - "ac dc marine"
  - "compressor bldc inverter barco"
  - "dometic coolair webasto bluecool marine"
geo_queries:
  - "Quando vale a pena instalar ar-condicionado 12V em embarcação de recreio?"
  - "Qual o consumo real de AC 12V DC marine em ancoragem?"
  - "AC 12V DC marine substitui AC 220V tradicional no barco?"
related_notes:
  - "Ar-Condicionado Marine — Sistema Completo"
  - "Banco de Baterias — Lítio LFP"
  - "CAIS (Pier) (AC)"
  - "Fusíveis Gerais DC"
  - "Gerador (AC)"
  - "Hotline (DC)"
  - "Inversora (DC To AC)"
  - "Linha Pesada (AC)"
  - "Proteção Dr"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
---

# Ar-Condicionado Marine 12V DC

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **AC 12 V DC marine ≠ miniatura de AC 220 V.** Arquitetura diferente: compressor BLDC inverter alimentado direto da bateria, sem inversor AC no caminho, tipicamente condensação a ar (não água do mar) em unidades pequenas.
> 2. **Faz sentido em barco sem gerador e com banco lítio LFP grande.** Vela 30–45 pés, trawler pequeno, lancha com lítio 400–800 Ah @ 12 V ou 200–400 Ah @ 24 V dedicado a ancoragem.
> 3. **NÃO faz sentido em barco grande com múltiplas cabines.** Consumo se multiplica rápido e derrete o banco; AC 220 V + gerador continua sendo a solução dimensional.
> 4. **Consumo típico 12 V:** 15–90 A para 3 000–10 000 BTU/h com compressor inverter; a 12 V um split de 10 000 BTU pode puxar **70–90 A em regime**.
> 5. **Cabo marine grosso é obrigatório.** Corrente contínua alta + queda de tensão ≤ 3% → 35–70 mm² (2/0–1 AWG) para distâncias típicas; errar aqui destrói o driver eletrônico e compromete partida.
> 6. **Fusível de alta corrente (Class T ou MRBF)** próximo à bateria, dimensionado pela corrente real e com capacidade de interrupção (AIC) compatível com o banco lítio (30 kA+ em LFP grande).
> 7. **Compressor BLDC inverter = soft start nativo.** Inrush mínimo, modulação contínua; não exige soft starter externo. Por isso compatível com banco lítio sem stress de pico.
> 8. **Refrigerantes usados:** R-134a (mais comum em DC), R-410A (em unidades maiores), R-32 ou R-290 em modelos recentes/europeus. **Mesmas obrigações regulatórias do AC 220 V** (Montreal, Kigali, F-gas, CONAMA 267, EPA Section 608).
> 9. **Família normativa primária:** ABYC E-11 + ABYC E-13 (lítio) + IEC 60335-2-40 + ISO 13297/10133 para elétrica; ASHRAE 15/34 + EN 378 + NBR 16401 para refrigeração; regulamentação de refrigerante em paralelo ao AC 220 V.

> [!danger] Quando chamar um especialista
> 1. **AC 12 V "adaptado" de camper (Dometic CoolAir, Indel Webasto) sem análise elétrica** — unidade projetada para caminhão/trailer pode não estar certificada para ambiente marine (UL 1500 / ISO 8846, ignition protection). Risco em compartimento de gasolina.
> 2. **Banco de baterias chumbo-ácido dimensionado para AC 12 V** — subestimar consumo: chumbo entrega menos capacidade útil (50%) que lítio (80–100%); AC derruba o banco em 2–3 h e mata a bateria em meses por descarga profunda.
> 3. **Cabo 16–25 mm² para unidade de 60 A+ em barco longo** — queda de tensão > 3%, aquecimento, compressor desarmando por subtensão e driver eletrônico falhando. Cabo subdimensionado é a causa mais comum de falha em retrofit.
> 4. **Sem fusível dedicado próximo à bateria** — curto no cabo principal entre banco e AC = incêndio em segundos. Lítio LFP entrega correntes de curto de 3 000–10 000 A; fusível obrigatório.
> 5. **Sem BMS com limite de corrente coordenado** — banco lítio sem proteção de sobrecorrente no pack pode fornecer corrente destrutiva; AC 12 V puxando 90 A + inversor + outros consumidores pode exceder o limite do BMS e disparar proteção em momento crítico.
> 6. **Driver eletrônico do compressor queimado após transitório de shore/gerador** — ripple, pico de recarga ou partida de outro motor grande na linha. Equipamento 12 V DC exige "DC limpo"; regulador instável ou transiente de recarga pode matar o controle inverter.
> 7. **Vazamento de refrigerante em compartimento fechado** — mesmas obrigações do AC 220 V (Montreal/Kigali/F-gas/CONAMA 267); HFC em espaço confinado pode deslocar O₂. Técnico certificado obrigatório para manuseio.
> 8. **Charter ou comercial dependendo exclusivamente de AC 12 V sem backup** — consumo prolongado em ancoragem com ocupação plena pode esvaziar o banco antes da noite acabar; passageiros sem climatização em barco tropical = reclamação e risco térmico.
> 9. **Retrofit de AC 12 V em barco que já tem AC 220 V tradicional sem análise integrada** — duas arquiteturas competindo (consumo DC + gerador + inversor + shore) sem PMS nem plano de uso documentado; diagnóstico futuro vira pesadelo.

> [!abstract] Resumo técnico
> Ar-condicionado marine 12 V DC é a arquitetura em que o compressor opera direto em corrente contínua (tipicamente 12 V, 24 V ou 48 V), alimentado pelo banco de baterias, sem inversor AC no caminho. É viabilizado por compressores BLDC inverter modernos (Secop, Danfoss, Embraco) e pela maturação do lítio LFP náutico. Oferece climatização silenciosa, sem shore power nem gerador, com consumo proporcional à carga térmica — mas impõe disciplina de projeto elétrico acima do habitual.

## O que é

Diferente do AC 220 V tradicional, o AC 12 V marine:

- **elimina o inversor AC** do caminho (a conversão DC→AC→DC no compressor inverter é desnecessária);
- **usa compressor BLDC inverter** (brushless DC com driver eletrônico);
- **modula rotação** conforme a demanda térmica real (ao contrário do compressor ON/OFF);
- **puxa corrente proporcional à carga**, não corrente fixa;
- **opera em silêncio quase absoluto** (sem motor de 60 Hz nem partida brusca);
- **se integra naturalmente a banco lítio LFP** de médio a grande porte.

## Quando faz sentido (e quando não faz)

### Casos em que a arquitetura 12 V DC é ganhadora

- barco vela 30–45 pés com banco lítio 400–800 Ah @ 12 V ou 200–400 Ah @ 24 V;
- ancoragem prolongada sem gerador e com solar/eólico razoável;
- cabine master isolada em trawler pequeno ou lancha;
- climatização noturna sem ruído (uso residencial a bordo);
- backup discreto em barco que tem AC 220 V mas quer operar sem gerador à noite;
- refit em barco sem espaço para gerador dedicado.

### Casos em que a arquitetura NÃO faz sentido

- embarcação grande (> 45 pés) com múltiplas cabines e uso contínuo;
- charter com ocupação plena e expectativa de AC permanente;
- barco sem banco de baterias compatível (chumbo-ácido pequeno, sem lítio);
- substituição direta de AC 220 V dimensional (10 000+ BTU/h × várias cabines);
- operação 24/7 sem fonte de recarga equivalente ao consumo.

## Principais fabricantes e produtos

### Dedicados ao náutico

- **Webasto BlueCool S-Series DC** — inverter 12/24 V, 5 000–12 000 BTU;
- **MABRU DC** — unidade self-contained 12/24 V;
- **Velair DC (Dometic)** — família marine 12/24 V;
- **Climma DC (Veco)** — linha italiana;
- **CTM Climatizzatori DC** — mercado europeu;
- **FridgeWize / Coolblue DC** — retrofit marine.

### Adaptados de camper/veicular (usar com cautela)

- **Dometic CoolAir RTX / CoolAir SP**;
- **Indel Webasto Cruise**;
- **Truma Saphir / Aventa**.

Quando adaptados, verificar sempre:

- certificação marine (UL 1500 / ISO 8846) em compartimento com gasolina;
- tolerância a tensão variável (alternador de 13,8 V a 14,6 V + carregador);
- resistência à corrosão do gabinete;
- classe de proteção IP do driver eletrônico.

## Arquitetura elétrica

### Topologia

```
Banco LFP → Fusível Class T/MRBF → Shunt BMS → Cabo marine →
Chave seccionadora → Distribuidor/Disjuntor DC → AC 12 V
```

Pontos críticos:

1. **Fusível de alta capacidade próximo à bateria** (Class T preferencial em lítio grande).
2. **Cabo marine estanhado (UL 1426 / ABYC E-11)** dimensionado pela corrente máxima + queda de tensão ≤ 3%.
3. **Chave seccionadora** classificada para a corrente e tensão do sistema.
4. **Disjuntor DC** na entrada do equipamento, coordenado com cabo e fusível.
5. **Aterramento / bonding** conforme ABYC E-11 e ISO 13297.
6. **Filtro / proteção contra ripple** quando a instalação for sensível (driver BLDC pode sofrer com ripple de carregador).

### Cabos e proteções (tabela orientativa 12 V)

| Potência AC | BTU/h | Corrente regime | Cabo típico (< 5 m) | Fusível próximo bateria |
|---|---|---|---|---|
| 400 W | 3 000 | 35 A | 16 mm² (6 AWG) | 50 A |
| 700 W | 5 000 | 60 A | 25 mm² (4 AWG) | 80 A |
| 900 W | 7 000 | 80 A | 35 mm² (2 AWG) | 100 A |
| 1 200 W | 10 000 | 100–110 A | 50 mm² (1/0 AWG) | 150 A |

Em 24 V DC, as correntes caem pela metade e os cabos reduzem bitola — motivo pelo qual sistemas 24 V e 48 V DC têm ganhado espaço em barcos maiores.

### Integração com banco lítio LFP

- **Capacidade útil do banco** ≥ consumo da noite + margem (60–80%);
- **BMS com monitoramento de corrente contínua** compatível com a corrente do AC;
- **Limite de corrente do pack** deve acomodar AC + outros consumos;
- **Recarga diurna** (solar + alternador + shore charger) dimensionada para repor o consumo noturno + consumo do dia;
- **Cut-off de subtensão coordenado** com a proteção do AC (evitar que o BMS corte enquanto o AC ainda está tentando partir).

## Integração com arquitetura geral do barco

- **Shore power + carregador**: carregador DC deve ter capacidade de alimentar o AC simultaneamente com a recarga do banco, sem ripple excessivo.
- **Gerador (quando houver)**: opção de carregar o banco via gerador curto período → AC roda do banco, silencioso.
- **Solar**: painéis bem dimensionados viabilizam AC "grátis" durante o dia em regiões tropicais.
- **Alternador**: durante navegação, pode alimentar AC direto + carregar banco.
- **Inversor AC**: permanece no barco para cargas 220 V (bomba de AC tradicional, eletrodomésticos), mas NÃO no caminho do AC 12 V DC.

## Desempenho real

### Consumo típico em regime (banco 12 V)

- 3 000 BTU/h → 400–500 W → **33–42 A**
- 5 000 BTU/h → 600–800 W → **50–65 A**
- 7 000 BTU/h → 800–1 000 W → **65–85 A**
- 10 000 BTU/h → 1 100–1 300 W → **90–110 A**

### Consumo noturno (10 h de operação)

- 5 000 BTU/h modulado (60% de média) → ~350 Ah em 12 V
- 7 000 BTU/h modulado (70% de média) → ~470 Ah em 12 V
- 10 000 BTU/h modulado (80% de média) → ~720 Ah em 12 V

Números aproximados — dependem de isolação do barco, carga térmica, temperatura externa e da eficiência específica do modelo (COP típico 2,5–3,5).

### Redução de consumo em 24 V / 48 V

Mesma potência, corrente cai pela metade (24 V) ou por quatro (48 V), cabos mais finos, perdas resistivas menores. Tendência forte em barcos novos > 40 pés.

## Refrigerante e regulação

Mesmas obrigações que AC 220 V:

- **R-134a** (GWP 1430, A1) — ainda comum em DC pequeno;
- **R-410A** (GWP 2088, A1) — em unidades maiores;
- **R-32** (GWP 675, A2L — levemente inflamável) — unidades recentes europeias;
- **R-290 / propano** (GWP 3, A3 — inflamável) — em algumas unidades pequenas europeias; **exige precauções** (ISO 5149 / EN 378 / NBR 15960).

Manuseio por técnico certificado (EPA Section 608 nos EUA; CTF/MAPA/IBAMA + capacitação técnica no Brasil; F-gas certificate na UE).

## Falhas típicas

- **Cabo subdimensionado**: queda de tensão > 3%, aquecimento, compressor desarma por subtensão, driver eletrônico falha;
- **Fusível ausente ou inadequado**: risco de curto destrutivo;
- **Driver eletrônico queimado**: transiente de shore power, ripple alto do carregador, tensão reversa, surto atmosférico;
- **Sensor de temperatura com leitura errada**: equipamento modula errado, consumo sobe ou capacidade some;
- **Ventilação do condensador (air-cooled) obstruída**: alta pressão, equipamento desarma;
- **Banco subdimensionado**: descarga profunda, vida útil despencando;
- **Retrofit sem análise integrada**: conflito entre AC 12 V, inversor AC, carregador e BMS.

## Diagnóstico profissional

Perguntas úteis:

1. Qual a corrente real nos terminais do AC sob carga, e qual a tensão simultânea? (separa problema elétrico de problema térmico)
2. A queda de tensão entre bateria e AC está ≤ 3% sob corrente máxima?
3. O banco lítio tem capacidade útil noturna para sustentar o AC + o resto dos consumos?
4. O BMS limita corrente em algum cenário (carga ou descarga) que afete o AC?
5. O circuito de condensação (ar ou água do mar) está livre e trabalhando?
6. O driver eletrônico está registrando falhas (log interno, código de erro)?
7. Houve evento recente (shore power, solda a bordo, raio) que possa explicar falha eletrônica?

Testes típicos:

- medição de corrente de regime com alicate DC;
- medição de tensão na bateria e no AC simultaneamente (queda real);
- verificação de ripple AC no barramento DC (osciloscópio ou multímetro AC em DC-coupled);
- inspeção do log do BMS e do driver;
- teste de vazamento de refrigerante;
- conferência de vazão/temperatura no lado condensador.

## Boas práticas

- dimensionar cabo pela **corrente máxima real + queda de tensão**, não pela corrente nominal do catálogo;
- usar fusível próximo à bateria obrigatoriamente (Class T ou MRBF em lítio);
- instalar filtro/protetor de surto dedicado em retrofit em barco velho;
- registrar consumo real por operação (data-logger ou BMS avançado);
- projetar banco com 60–80% de margem além do consumo noturno previsto;
- reservar dia seguinte para recarga (solar + navegação + shore se disponível);
- tratar AC 12 V como **sistema**, não como eletrodoméstico.

## Erros comuns

- confundir camper com marine (certificação, corrosão, ignition protection);
- dimensionar pelo watt sem olhar corrente e queda de tensão;
- esquecer que o banco chumbo não serve para AC prolongado;
- omitir fusível próximo à bateria;
- partir o AC simultaneamente com outros picos (partida de motor, windlass, bow thruster);
- usar AC 12 V como substituto do AC 220 V em barco grande — não é a ferramenta certa para o problema.

## Visual didático

> *Espaço reservado para diagrama futuro: "AC 12 V DC marine — banco lítio, cabo, fusível, driver inverter, condensador, evaporador, sensor".*

## Normas aplicáveis

AC 12 V DC marine fica na interseção de **elétrica DC de baixa tensão com alta corrente**, **equipamento de refrigeração**, **banco de baterias (tipicamente lítio)** e **regulação ambiental de refrigerante**. Quatro camadas normativas simultâneas.

### Recreio / Small craft (foco principal)

- **ABYC E-11 (2023) — AC & DC Electrical Systems on Boats**: alimentação DC, cabos, fusíveis, proteção, bonding.
- **ABYC E-13 — Lithium Ion Batteries**: integração com banco LFP (quando for o caso).
- **ABYC A-31 — Battery Chargers and Inverters**: interação com sistema de recarga.
- **ABYC A-26 — Heating systems**: ciclo reverso / bomba de calor DC.
- **ABYC H-2 — Ventilation**: renovação de ar ambiente.
- **ABYC H-27 — Seacocks**: condensação a água do mar quando aplicável.
- **ISO 10133:2020 — Electrical systems — Extra-low voltage DC**: norma central para o lado DC em embarcação de recreio.
- **ISO 13297:2020 — Electrical systems — AC and DC**: documento internacional complementar.
- **ISO 16315:2016 — Electric propulsion system**: referência cruzada para sistemas DC de alta corrente.
- **ISO 8846:2020 — Ignition protection**.
- **CE-RCD Directive 2013/53/EU**: exigência europeia.

### Equipamento de refrigeração

- **IEC 60335-2-40 — Safety of heat pumps, air-conditioners and dehumidifiers**: norma de segurança do equipamento (inclui DC).
- **UL 484 — Room Air Conditioners** e **UL 60335-2-40**: certificação americana.
- **UL 1995 — Heating and Cooling Equipment**.
- **EN 14511 — Testing and rating of air conditioners, chillers and heat pumps**.
- **EN 378 — Refrigerating systems and heat pumps — Safety and environmental**.
- **ASHRAE 15 — Safety Standard for Refrigeration Systems**.
- **ASHRAE 34 — Refrigerants designation and safety classification**.
- **ASHRAE 62.1 — Indoor Air Quality**.
- **AHRI 210/240 — Performance Rating**.
- **NBR 16401-1/-2/-3**: instalações de AC no Brasil.
- **NBR 15960 — Refrigerantes inflamáveis**: relevante para R-32 / R-290.
- **NBR 13971 — Manutenção programada**.

### Banco de baterias (quando lítio)

- **IEC 62133 — Secondary cells and batteries**: segurança de células e packs.
- **IEC 62619 — Lithium batteries for industrial applications**.
- **ABYC E-13**: a norma marine específica.
- **UL 1973 / UL 9540**: referência americana para packs estacionários / marine.

### Refrigerantes e regulação ambiental

- **Protocolo de Montreal** + **Emenda de Kigali (2016)**.
- **EPA SNAP Program** + **AIM Act (2020)**.
- **EU F-gas Regulation (UE) 517/2014**.
- **EPA Section 608 Technician Certification**.
- **Resolução CONAMA 267/2000** (Brasil).

### Comercial / classificada

- **IEC 60092-series** (navios).
- **DNV-RU-SHIP Pt 4 Ch 8** e **Lloyd's Register Rules Pt 6**.
- **NORMAM-201/204/DPC** (comercial) e **NORMAM-211/DPC** (recreio).

### Comparação rápida por jurisdição

| Tema | EUA (ABYC + UL + EPA) | Brasil (NBR + NORMAM + CONAMA) | Internacional / Comercial (IEC + ISO + Classificadoras) | Europa (CE-RCD + F-gas + EN) |
|---|---|---|---|---|
| Referência DC marine | ABYC E-11 + E-13 | NBR 5410 (parcial) + NORMAM | ISO 10133 + IEC 60092 | ISO 10133 + 13297 |
| Equipamento AC (segurança) | UL 484 + UL 60335-2-40 | NBR 16401 | IEC 60335-2-40 | EN 60335-2-40 |
| Refrigerante regulado | EPA SNAP + AIM Act + Section 608 | CONAMA 267 + MAPA | Montreal + Kigali | EU F-gas 517/2014 |
| Banco lítio | ABYC E-13 + UL 1973 | NBR em construção + boa prática | IEC 62133 + 62619 | IEC + EN equivalente |
| IAQ (qualidade do ar) | ASHRAE 62.1 | NBR 16401 | — | EN 13779/16798 |
| Ignition protection | UL 1500 + ISO 8846 | NBR (geral) + NORMAM | ISO 8846 | ISO 8846 |

## Glossário rápido

- **AC 12V DC marine**: ar-condicionado alimentado direto em corrente contínua (tipicamente 12 V, 24 V ou 48 V) do banco de baterias, sem inversor AC no caminho.
- **Compressor BLDC (Brushless DC)**: motor síncrono de imã permanente com driver eletrônico, sem escovas; coração do AC DC moderno.
- **Driver inverter**: eletrônica de potência que modula velocidade do compressor BLDC; precisa de DC "limpo".
- **Inverter compressor**: termo comercial para compressor com modulação de velocidade (não confundir com inversor AC).
- **Secop / Danfoss / Embraco**: principais fabricantes de compressor BLDC para aplicação DC marine / refrigeração móvel.
- **Self-contained DC**: unidade com compressor + condensador + evaporador + driver em um único gabinete; tipicamente condensação a ar.
- **Air-cooled vs. SW-cooled**: condensação a ar (mais comum em DC pequeno, típico de camper) vs. condensação a água do mar (em DC maior / marine dedicado).
- **BTU/h**: unidade de capacidade frigorífica.
- **COP (Coefficient of Performance)**: eficiência; tipicamente 2,5–3,5 em AC DC marine moderno.
- **Modulação contínua**: compressor ajusta rotação à demanda, sem ciclos ON/OFF; economiza muito consumo.
- **Soft start nativo**: inerente ao compressor inverter; dispensa soft starter externo.
- **Ripple DC**: ondulação residual na tensão DC (vinda de carregador/retificador); alto ripple destrói driver eletrônico.
- **Transiente**: pico ou depressão rápida de tensão; driver precisa de proteção contra surto.
- **Banco LFP (LiFePO₄)**: lítio ferro fosfato, padrão marine moderno, tolera descarga profunda.
- **BMS (Battery Management System)**: proteção + monitoramento do pack lítio; limita corrente, tensão, temperatura.
- **Capacidade útil**: fração da capacidade nominal que pode ser usada repetidamente (LFP ~80–100%, chumbo ~50%).
- **DOD (Depth of Discharge)**: profundidade de descarga.
- **SoC (State of Charge)**: estado de carga do banco.
- **Shunt / monitor de bateria**: sensor de corrente para medir consumo em tempo real (Victron BMV, SmartShunt, REC, etc.).
- **Cabo marine estanhado**: cobre estanhado com isolação adequada; UL 1426 + ABYC E-11.
- **AWG / mm²**: bitola do cabo; em DC de alta corrente, dimensionar pela queda de tensão é mais crítico que pela ampacidade.
- **Queda de tensão (%)**: diferença entre tensão na origem e tensão no equipamento; ≤ 3% para AC DC.
- **Fusível Class T**: fusível de altíssima capacidade de interrupção (AIC 20–200 kA), obrigatório em lítio grande.
- **Fusível MRBF (Marine Rated Battery Fuse)**: fusível compacto montado direto no terminal da bateria.
- **Fusível ANL**: fusível de lâmina, comum em barco; AIC menor (5–6 kA) — inadequado para lítio grande.
- **Chave seccionadora DC**: chave de isolamento dimensionada para DC (arco sustentado exige construção específica).
- **Disjuntor DC**: proteção contra sobrecorrente dimensionada para DC; tempo de atuação e corte do arco diferem do AC.
- **Shore charger**: carregador AC→DC alimentado do cais; precisa entregar corrente suficiente para AC + recarga.
- **DC-DC charger**: conversor entre banco-motor e banco-serviço; útil em retrofit.
- **Solar charge controller (MPPT)**: otimiza geração solar; essencial para viabilizar AC DC em ancoragem.
- **Alternador regulado / alternator regulator**: regulador externo para otimizar recarga durante navegação.
- **R-134a / R-410A / R-32 / R-290**: refrigerantes; obrigações regulatórias idênticas às do AC 220 V.
- **GWP / ODP / A1 / A2L / A3**: ver nota [[Ar-Condicionado Marine — Sistema Completo]].
- **EPA Section 608**: certificação obrigatória nos EUA para manuseio de HFC.
- **CONAMA 267/2000**: resolução brasileira.
- **EU F-gas 517/2014**: regulamento europeu.
- **Ignition protection (UL 1500 / ISO 8846)**: característica obrigatória em compartimento com gasolina.
- **IP rating**: proteção da carcaça contra pó e água (IEC 60529).
- **ECE R10**: norma de EMC (compatibilidade eletromagnética) veicular/marine.
- **Silencio de operação**: métrica comercial relevante em AC DC marine — típico 40–50 dB @ 1 m para unidades bem projetadas.
- **Split DC marine**: unidade com condensadora e evaporadora separadas, alimentação DC; raro mas existe.
- **Retrofit**: instalação em barco existente, tipicamente substituindo ou complementando AC 220 V.
- **PMS (Power Management System)**: em barco com AC DC + AC 220 V + inversor + shore + gerador + solar, integração via PMS deixa de ser luxo.

## Integração com outras notas

- [[Ar-Condicionado Marine — Sistema Completo]] (nota-mãe, AC 220 V)
- [[CAIS (Pier) (AC)]]
- [[Fusíveis DC — Proteção Contra Sobrecorrente]]
- [[Gerador (AC)]]
- [[Hotline (DC)]]
- [[Inversora (DC To AC)]]
- [[Linha Pesada (AC)]]
- [[Proteção Dr]]
- [[Quadro Elétrico e Painel de Distribuição AC-DC]]

## Perguntas que esta nota responde

- Quando o AC 12 V DC marine é a arquitetura certa e quando não é?
- Quanto o AC 12 V DC realmente consome em 10 horas de ancoragem?
- Como dimensionar cabo, fusível e banco para AC 12 V DC em embarcação de recreio?
- Quais são as diferenças reais entre AC 12 V DC marine e AC 220 V tradicional?
- Quais cuidados regulatórios se aplicam ao refrigerante do AC DC (iguais ao AC 220 V)?
