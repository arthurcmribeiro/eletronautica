---
title: "Geladeira - Freezer de Bordo"
note_type: "technical-note"
domain: "70_Hidraulica_Climatizacao_e_Utilidades"
source_file: "GELADEIRA FREEZER DE BORDO 33a19734f7fb81f0887cfa7b6b50fe31.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "49"
tier_fase_6: "A"
reviewed_on: "2026-04-21"
review_jurisdiction:
  - "Brasil"
  - "internacional"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
  - "https://www.epa.gov/snap"
  - "https://www.epa.gov/section608"
  - "https://unep.org/ozonaction/who-we-are/about-montreal-protocol"
  - "https://www.ibama.gov.br/"
review_level: "engineering-curated"
normas_citadas:
  - "ABYC A-16 - Electrical Safety (low-voltage DC circuits)"
  - "ABYC E-11 - AC and DC Electrical Systems on Boats"
  - "ABYC A-31 - Battery Chargers and Inverters"
  - "ISO 10133:2017 - Small craft - Extra-low-voltage DC installations"
  - "ISO 13297:2020 - Small craft - AC installations"
  - "ISO 8846:1990 - Small craft - Electrical devices - Protection against ignition of flammable gases"
  - "ISO 9094:2015 - Small craft - Fire protection (refrigerant leak implications)"
  - "IEC 60335-2-24:2020 - Household and similar electrical appliances - Particular requirements for refrigerating appliances"
  - "IEC 60335-2-89:2019 - Particular requirements for commercial refrigerating appliances with incorporated or remote refrigerant unit"
  - "UL 250 - Household Refrigerators and Freezers"
  - "UL 471 - Commercial Refrigerators and Freezers"
  - "UL 60335-2-24 - Safety of Household Refrigerating Appliances"
  - "UL 1995 / CAN/CSA-C22.2 No. 236 - Heating and Cooling Equipment"
  - "EN 378:2016 - Refrigerating systems and heat pumps - Safety and environmental requirements"
  - "AHRI 1250:2020 - Performance Rating of Walk-in Coolers and Freezers"
  - "Protocolo de Montreal (1987) - Substances that Deplete the Ozone Layer"
  - "Emenda de Kigali (2016) - Montreal Protocol amendment on HFC phase-down"
  - "EPA SNAP (Significant New Alternatives Policy) - 40 CFR Part 82 Subpart G"
  - "EPA Section 608 - Stratospheric Ozone Protection (Clean Air Act 40 CFR Part 82 Subpart F)"
  - "AIM Act 2020 (American Innovation and Manufacturing Act) - HFC phase-down schedule"
  - "EU F-gas Regulation 517/2014 - Fluorinated greenhouse gases"
  - "CONAMA 267/2000 - Dispõe sobre a proibição da utilização de substâncias que destroem a camada de ozônio"
  - "CONAMA 340/2003 - Dispõe sobre a utilização de cilindros para envasamento de gases refrigerantes"
  - "IN IBAMA 207/2008 - Cadastro de importadores de gases refrigerantes"
  - "ISO 817:2014 - Refrigerants - Designation and safety classification (A1/A2/A2L/A3/B1/B2L/B3)"
  - "ISO 5149-1/2/3/4:2014 - Refrigerating systems and heat pumps - Safety and environmental requirements"
  - "ASHRAE 34-2022 - Designation and Safety Classification of Refrigerants"
  - "ASHRAE 15-2022 - Safety Standard for Refrigeration Systems"
  - "NMMA Certification - ABYC-based compliance for US recreational boats"
  - "NBR 16401:2008 - Instalações de ar-condicionado - Sistemas centrais e unitários"
  - "NBR 15960:2019 - Gases refrigerantes - Classificação"
  - "NBR 13971:2014 - Sistemas de refrigeração, condicionamento de ar e ventilação - Manutenção programada"
  - "Portaria MCT 86/2013 - Controle e certificação de técnicos em refrigeração"
  - "NORMAM-01/DPC - Embarcações empregadas na navegação em mar aberto"
  - "NORMAM-03/DPC - Embarcações empregadas na navegação interior"
aliases:
  - "GELADEIRA FREEZER DE BORDO"
  - "Refrigeração de bordo"
  - "Marine refrigerator"
  - "Marine freezer"
seo_title: "Geladeira e freezer de bordo: consumo, compressor, gases, instalação e autonomia"
seo_description: "Guia técnico sobre geladeira e freezer de bordo: compressor BD35F/BD50F, isolamento, ventilação do condensador, consumo real, refrigerantes (R-134a, R-600a, R-290), regulação (Montreal/Kigali/EPA/CONAMA) e integração com baterias."
seo_keywords:
  - "geladeira de bordo"
  - "freezer embarcação"
  - "compressor dc barco"
  - "consumo geladeira náutica"
  - "refrigerante R-134a R-600a"
  - "Secop Danfoss BD35F"
geo_queries:
  - "Como calcular o impacto da geladeira no banco de baterias do barco?"
  - "Por que a geladeira de bordo consome muito ou não gela bem?"
  - "Qual refrigerante usar na geladeira marítima e como é regulado?"
related_notes:
  - "Ar-Condicionado Marine — Sistema Completo"
  - "Ar-Condicionado Marine 12V DC"
  - "Icemaker - Máquina de Gelo"
  - "Bancos de Bateria"
  - "Carregador de Bateria (AC To DC)"
  - "Placa Solar (DC)"
  - "Gerador (AC)"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
---

# Geladeira - Freezer de Bordo

> [!abstract] Resumo técnico
> A refrigeração de bordo é uma das cargas contínuas mais relevantes da embarcação. O desempenho real depende menos da marca e mais da combinação entre compressor, isolamento, ventilação do condensador, temperatura ambiente, rotina de uso, qualidade da arquitetura elétrica e tipo de refrigerante. Refrigerantes são fortemente regulados (Montreal/Kigali/EPA SNAP/AIM Act/F-gas/CONAMA 267) — uso e descarte incorretos podem gerar infração ambiental.

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **Refrigeração de bordo é carga estrutural** — tipicamente 25-60 Ah/dia em DC 12V; dimensionar banco de baterias e geração como se fosse AC contínuo.
> 2. **Compressor BD (Danfoss/Secop BD35F/BD50F) é padrão técnico DC** — arranque suave, variável, faixa de tensão ampla (10.5-17 V); muito superior a termoelétrica em eficiência.
> 3. **Ventilação do condensador define consumo real** — nicho fechado sem ar circulante dobra o consumo e reduz vida do compressor pela metade.
> 4. **Isolamento domina autonomia** — 50-100 mm de poliuretano expandido é mínimo; equipamento doméstico residencial em barco tropical costuma falhar aqui.
> 5. **Refrigerantes DC marine modernos: R-134a (saída), R-600a (isobutano, A3 inflamável), R-290 (propano, A3 inflamável)** — equipamento selado de fábrica; NÃO recarregar em campo sem técnico certificado.
> 6. **Regulação de refrigerante é séria** — HFC (R-134a) em phase-down global (Kigali/AIM Act/EU F-gas); R-22 já banido em nova carga; HC (R-600a/R-290) é opção ambientalmente preferida mas inflamável.
> 7. **Queda de tensão destrói desempenho** — 12V DC com 0.5 V de queda (comum em chicote fino) reduz capacidade de refrigeração em até 20%.
> 8. **Sistema DC com inversor para AC residencial é antipadrão energético** — eficiência do inversor cobra 10-20%, compressor AC parte em pico, ciclo liga/desliga brutaliza banco.
> 9. **Recarga/descarte de refrigerante só com técnico certificado** — EPA Section 608 (EUA), Portaria MCT 86/2013 (Brasil); emissão intencional é infração ambiental federal.

> [!danger] Quando chamar um especialista (9 cenários)
> 1. **Cheiro de gás no compartimento do compressor** — vazamento de R-600a/R-290; HCs são inflamáveis (classe A3); ventilar, não gerar faíscas, parar sistema imediatamente.
> 2. **Compressor ciclando muito rápido (< 5 minutos ligado/desligado)** — carga de refrigerante baixa, condensador obstruído ou termostato com defeito; desgaste acelerado sem diagnóstico.
> 3. **Compressor não desliga / rodando 24 h sem atingir temperatura** — isolamento comprometido, vedação ruim, refrigerante insuficiente ou condensador entupido; risco de queima em horas.
> 4. **Gelo/cristalização na linha de sucção (linha volta para compressor)** — refrigerante excessivo ou evaporador com fluxo inadequado; compressor pode sofrer "golpe de líquido" e quebrar.
> 5. **Sistema novo que nunca atingiu temperatura** — possível carga errada ou falha no teste de fábrica; reclamar em garantia antes de abrir.
> 6. **Água acumulada no fundo / condensação excessiva** — dreno obstruído ou vedação comprometida; risco elétrico e de biofilme.
> 7. **Recarga necessária** — somente por técnico certificado EPA Section 608 (EUA) ou MCT/IBAMA (Brasil); emissão intencional de HFC é crime ambiental.
> 8. **Descarte de equipamento antigo** — refrigerante deve ser recuperado antes do descarte (CONAMA 267/2000 no Brasil, EPA Section 608 nos EUA); posto revendedor ou empresa certificada.
> 9. **Perícia pós-incêndio com suspeita de gás inflamável** — R-600a/R-290 em quantidades dentro do equipamento raramente causam incêndio sozinhos, mas vazamento + fonte de ignição em ambiente confinado é cenário documentado; preservar evidência.

## O que é

Esta nota trata de:

- geladeiras e freezers dedicados de bordo (DC, AC ou híbridos);
- soluções em compartimento construído (drawer, built-in) ou portátil (Waeco, ARB, Engel);
- impacto energético, térmico e operacional no barco;
- regulação e descarte de refrigerantes.

## Por que esse equipamento é central

Em barcos com pernoite ou autonomia real, a refrigeração afeta diretamente:

- dimensionamento de baterias (carga de 25-60 Ah/dia em DC 12V);
- necessidade de geração complementar (solar, gerador);
- conforto e autonomia em fundeio;
- qualidade do projeto elétrico;
- custo operacional (em charter, falha de geladeira é reclamação top 5).

É um erro tratar geladeira como "carga pequena e constante" sem olhar o conjunto.

## Tecnologias relevantes

### Compressor (padrão técnico sério)

É a solução tecnicamente mais confiável para uso contínuo. Pode operar em DC, AC ou em arranjos compatíveis com ambos.

**Compressores DC marine dominantes:**

- **Secop/Danfoss BD35F** — padrão mundial para geladeiras DC até ~150 L; 10-45 W em regime; 0.4-0.6 A em média;
- **Secop/Danfoss BD50F** — freezers e geladeiras maiores até ~250 L;
- **Secop/Danfoss BD80F e BD100F** — sistemas maiores, walk-in ou freezers grandes de pesca;
- **Embraco / Aspera** — alternativa técnica em alguns equipamentos;
- **Isotherm ASU (Automatic Start-Up)** — controle inteligente sobre Secop.

Vantagens do BD-Danfoss:

- partida suave sem pico alto;
- velocidade variável (2000-3500 RPM);
- operação em tensão ampla (10.5-17 V, alguns modelos até 10-45 V);
- proteção integrada contra subtensão;
- tolerância a inclinação (até 30° em muitos modelos).

### Termoelétrica (Peltier)

É simples, mas costuma ter eficiência muito inferior.

- COP típico 0.3-0.5 (compressor BD atinge 2.5-3.5);
- limite de ΔT (tipicamente 15-20°C abaixo do ambiente);
- consumo alto para resultado fraco;
- útil em cooler pequeno, não é solução para geladeira permanente.

### Sistemas especiais

- **Placas eutéticas** — sistema de "massa térmica" com compressor maior que opera por poucas horas/dia, congelando fluido eutético que mantém temperatura por 12-24 h; eficiente em veleiro com gerador/banco menor;
- **Refrigeração por água do mar (raw water cooled)** — condensador trocador de calor imerso ou com bomba; melhora eficiência em climas muito quentes;
- **Sistema split marine** — compressor em casa de máquinas, evaporador na caixa; reduz ruído e calor no espaço habitado.

## O que determina o consumo real

Os fatores dominantes são:

- **qualidade do isolamento** — 50-100 mm de PU é mínimo; 100-150 mm em tropical;
- **ventilação do condensador** — compartimento fechado e sem circulação aumenta consumo em 50-100%;
- **temperatura ambiente** — consumo duplica entre 25°C e 35°C em muitos sistemas;
- **frequência de abertura** — cada abertura injeta ar úmido quente;
- **massa térmica dos itens armazenados** — itens já frios mantêm ciclo; carga nova é trabalho extra;
- **ajuste de setpoint** — cada 1°C abaixo do necessário custa 5-10% de energia;
- **estado de vedação da porta ou tampa** — borracha ressecada é falha comum e invisível;
- **regime de alimentação elétrica** — tensão estável vs flutuante muda ciclo.

Dois equipamentos com o mesmo volume podem ter comportamento energético completamente diferente.

## Compressor e ventilação do condensador

Muita instalação ruim nasce aqui.

Se o condensador não rejeita calor adequadamente:

- o compressor trabalha mais;
- a temperatura interna sobe;
- o consumo aumenta (até dobrar);
- a vida útil cai (metade).

Logo, compartimento fechado e sem ventilação é uma das piores escolhas possíveis.

**Regras práticas:**

- mínimo 30-50 mm de espaço livre em cada face ventilada do condensador;
- entrada e saída de ar em alturas diferentes (efeito chaminé);
- exaustor/ventilador auxiliar quando o layout força nicho fechado;
- limpeza anual da serpentina (poeira e pelo de animal reduzem troca térmica).

## Isolamento

O isolamento é decisivo.

Em barcos de clima quente ou uso intenso:

- isolamento ruim destrói autonomia;
- pontes térmicas viram problema real (fixação metálica atravessando PU);
- tampa ou porta mal vedada aumenta umidade e gelo;
- freezer compartilha ou disputa capacidade com a geladeira dependendo da arquitetura.

Materiais típicos:

- **Poliuretano expandido (PU)** — padrão; condutividade 0.022-0.028 W/m·K;
- **Poliestireno (EPS)** — alternativa mais barata, condutividade 0.032-0.040 W/m·K;
- **Painel vácuo (VIP)** — alta performance, usado em equipamento premium; condutividade 0.005-0.008 W/m·K.

Em construção náutica custom (caixa marcenada), aceitar PU expandido in situ (espuma spray) é padrão de mercado desde 1980.

## Refrigerantes

### Histórico e regulação

Os refrigerantes usados em geladeira/freezer marine passaram por três gerações:

1. **CFC (R-12)** — banido desde 1996 (Protocolo de Montreal); destruidor de ozônio;
2. **HFC (R-134a)** — dominante nos anos 2000-2020; não destrói ozônio mas é gás de efeito estufa potente (GWP 1430); em phase-down (Kigali/AIM Act/EU F-gas);
3. **HC (R-600a isobutano, R-290 propano)** — dominantes em equipamento novo desde ~2015; GWP ≈ 3; classificados A3 (inflamável); carga limitada a 150 g em eletrodoméstico típico (IEC 60335-2-24).

### Classificação de segurança (ASHRAE 34 / ISO 817)

- **A1** — não inflamável, baixa toxicidade (R-134a);
- **A2L** — pouco inflamável, baixa toxicidade (R-32 em AC, raro em geladeira);
- **A3** — altamente inflamável (R-600a, R-290);
- **B1-B3** — toxicidade maior (raros em recreio).

### Regulação por jurisdição

| Jurisdição | Norma principal | Refrigerantes em phase-down |
|---|---|---|
| EUA | EPA SNAP (40 CFR Part 82 Subpart G) + AIM Act 2020 | R-134a, R-404A, R-410A (pós-2024 cronograma) |
| EUA — manuseio | EPA Section 608 (40 CFR Part 82 Subpart F) + certificação de técnico | Todos HFC/HCFC |
| União Europeia | EU F-gas 517/2014 + revisão 2024 | R-134a, R-404A (banidos novos desde 2020) |
| Internacional | Protocolo de Montreal + Emenda de Kigali 2016 | Cronograma global HFC phase-down |
| Brasil | CONAMA 267/2000 + CONAMA 340/2003 + IN IBAMA 207/2008 + Portaria MCT 86/2013 | CFC/HCFC banidos; HFC em redução progressiva |

### Prática em equipamento marine

- **Novo em 2026** — maioria já vem com R-600a ou R-290;
- **Usado** — R-134a ainda comum em equipamento 2005-2020;
- **Recarga** — exige técnico certificado; HC inflamável pede cuidado dobrado (sem fonte de ignição próxima durante serviço);
- **Descarte** — CONAMA 267/2000 proíbe liberação atmosférica; descarte via empresa certificada ou posto coletor.

## Integração com a arquitetura energética

A refrigeração precisa ser considerada junto com:

- [[Bancos de Bateria]]
- [[Placa Solar (DC)]]
- [[Carregador de Bateria (AC To DC)]]
- [[Gerador (AC)]]

O ponto-chave não é só o pico de corrente, mas a energia diária efetivamente exigida.

**Balanço típico (barco 40 pés, clima tropical):**

- geladeira DC 12V (130 L, BD35F): 30-45 Ah/dia;
- freezer DC 12V (80 L, BD50F): 40-60 Ah/dia;
- total: 70-105 Ah/dia só em refrigeração.

Um banco de serviço de 400-600 Ah útil precisa ser pensado em torno dessa base.

## DC, AC ou híbrido

Cada solução tem trade-offs:

- **DC dedicado** favorece autonomia sem depender de inversão permanente; compressor BD é padrão; sistema sobrevive com banco de baterias + solar sem gerador.
- **AC pode fazer sentido** com gerador operando várias horas/dia ou marina permanente com shore power; compressor industrial maior, arranque em pico alto.
- **Híbrido (AC/DC)** pode ser interessante quando a embarcação alterna modos de operação (marina vs fundeio); compressor universal que aceita 12/24 V DC ou 115/230 V AC existe em várias linhas (Isotherm, Vitrifrigo, Webasto).

O erro recorrente é usar equipamento inadequado ao perfil de uso do barco (geladeira residencial em veleiro de cruzeiro, por exemplo).

## Onde costuma falhar

As falhas recorrentes são:

- baixo desempenho por ventilação ruim;
- ciclo excessivo por isolamento deficiente;
- falhas por queda de tensão (chicote subdimensionado);
- consumo percebido como "absurdo" sem medição real;
- vedação ruim (borracha ressecada, dobradiça torta);
- condensador ou compartimento sujos;
- ventilador do condensador parado (comum em instalações com exaustor auxiliar esquecido);
- vazamento de refrigerante (raro em BD-Danfoss, mas ocorre em trocadores de calor marine-cooled).

## Diagnóstico profissional

Perguntas obrigatórias:

1. O equipamento atinge a temperatura desejada?
2. O compressor trabalha em regime coerente ou excessivo (duty cycle > 80% em temperatura normal é anormal)?
3. Há ventilação suficiente no condensador (temperatura na saída < 15°C acima do ambiente)?
4. A alimentação elétrica chega corretamente sob carga (queda < 3% no chicote)?
5. O problema é térmico, elétrico ou de uso?
6. Há indicação de vazamento (cheiro, ruído diferente, produção caindo sem troca de uso)?

Ensaios úteis:

- medir tensão no equipamento durante partida e regime (multímetro ou data logger);
- observar tempo ligado/desligado em condição estável;
- verificar temperatura no compartimento do condensador;
- inspecionar vedações e qualidade do isolamento percebido;
- medir consumo real ao longo de um ciclo representativo (pinça amperimétrica de longa duração);
- limpar condensador e reavaliar consumo.

## Boas práticas

- prever ventilação real no compartimento de instalação;
- pensar em refrigeração como carga estrutural do barco;
- armazenar itens já frios sempre que possível;
- evitar setpoints desnecessariamente agressivos (freezer a -15°C em vez de -20°C economiza 20-30%);
- manter vedação, limpeza e condensador em bom estado;
- dimensionar chicote DC com margem (queda de tensão < 3% sob pico);
- integrar monitoramento de consumo (shunt/BMS) para identificar desvio precoce;
- respeitar regulação de refrigerante (EPA 608, CONAMA 267) em qualquer intervenção.

## Erros comuns

- usar produto inadequado para uso contínuo de bordo (geladeira doméstica);
- instalar em nicho fechado sem rejeição de calor;
- ignorar impacto sobre baterias e geração;
- superdimensionar o freezer e subdimensionar a energia;
- diagnosticar "gás ruim" antes de checar o básico do sistema;
- recarregar refrigerante sem certificação técnica (ilegal e ineficaz);
- descartar equipamento sem recuperar refrigerante (infração ambiental).

## Normas aplicáveis

### 1. Padrão elétrico de recreio (ABYC/ISO)

- **ABYC A-16** — Electrical Safety (circuitos DC);
- **ABYC E-11** — AC and DC Electrical Systems on Boats;
- **ABYC A-31** — Battery Chargers and Inverters (quando usa inversor);
- **ISO 10133:2017** — Extra-low-voltage DC installations;
- **ISO 13297:2020** — AC installations;
- **ISO 8846:1990** — Electrical devices — Protection against ignition of flammable gases;
- **ISO 9094:2015** — Fire protection (implicações de refrigerante inflamável).

### 2. Equipamento de refrigeração (IEC/UL/EN)

- **IEC 60335-2-24:2020** — Household refrigerating appliances;
- **IEC 60335-2-89:2019** — Commercial refrigerating appliances;
- **UL 250** — Household Refrigerators and Freezers;
- **UL 471** — Commercial Refrigerators and Freezers;
- **UL 60335-2-24** — Safety of Household Refrigerating Appliances;
- **EN 378:2016** — Refrigerating systems and heat pumps — Safety and environmental requirements;
- **AHRI 1250:2020** — Performance Rating of Walk-in Coolers and Freezers.

### 3. Refrigerantes — Regulação ambiental (DEC-26)

- **Protocolo de Montreal (1987)** — Substances that Deplete the Ozone Layer;
- **Emenda de Kigali (2016)** — HFC phase-down global;
- **EPA SNAP (40 CFR Part 82 Subpart G)** — alternativas aceitas nos EUA;
- **EPA Section 608 (40 CFR Part 82 Subpart F)** — manuseio, recuperação, certificação de técnicos nos EUA;
- **AIM Act 2020** — cronograma de phase-down HFC nos EUA;
- **EU F-gas Regulation 517/2014 + revisão 2024** — União Europeia.

### 4. Refrigerantes — Classificação de segurança

- **ISO 817:2014** — Designation and safety classification (A1/A2/A2L/A3/B1/B2L/B3);
- **ASHRAE 34-2022** — Designation and Safety Classification of Refrigerants;
- **ASHRAE 15-2022** — Safety Standard for Refrigeration Systems;
- **ISO 5149-1/2/3/4:2014** — Safety and environmental requirements.

### 5. Brasil — Regulação específica

- **CONAMA 267/2000** — Proibição de substâncias que destroem a camada de ozônio;
- **CONAMA 340/2003** — Cilindros para envasamento de gases refrigerantes;
- **IN IBAMA 207/2008** — Cadastro de importadores de gases refrigerantes;
- **Portaria MCT 86/2013** — Controle e certificação de técnicos em refrigeração;
- **NBR 16401:2008** — Instalações de ar-condicionado;
- **NBR 15960:2019** — Gases refrigerantes — Classificação;
- **NBR 13971:2014** — Sistemas de refrigeração — Manutenção programada;
- **NORMAM-01/DPC** — Embarcações em mar aberto;
- **NORMAM-03/DPC** — Embarcações em navegação interior.

### Tabela comparativa por jurisdição

| Aspecto | EUA (ABYC/EPA/UL) | Internacional (ISO/IEC/ASHRAE) | Europa (EN/EU) | Brasil (ABNT/CONAMA/IBAMA) |
|---|---|---|---|---|
| Segurança elétrica | ABYC A-16, E-11 | ISO 10133, ISO 13297 | EN 60335 | NBR (referencia IEC) |
| Refrigeração | UL 250, 471 | IEC 60335-2-24/89 | EN 378 | NBR 13971, 15960 |
| Refrigerante phase-down | EPA SNAP + AIM Act | Montreal + Kigali | EU F-gas 517/2014 | CONAMA 267 |
| Manuseio refrigerante | EPA Section 608 | ISO 817, ASHRAE 34 | EU F-gas cert | Portaria MCT 86/2013 |
| Ignition protection | UL 1500, ISO 8846 | ISO 8846 | EN (referencia) | NORMAM |

## Glossário rápido

- **Geladeira de bordo** — refrigerador dedicado para embarcação; DC, AC ou híbrido.
- **Freezer de bordo** — congelador dedicado; tipicamente setpoint -15 a -20°C.
- **Built-in** — equipamento embutido em moveleiro custom (caixa marcenada).
- **Drawer** — gaveta de refrigeração/freezer; padrão premium (Vitrifrigo, U-Line, Isotherm).
- **Portátil** — equipamento autônomo (Engel, ARB, Waeco/Dometic Coolfreeze); DC 12/24V.
- **Compressor BD (Secop/Danfoss)** — linha BD35F/50F/80F/100F; padrão DC marine.
- **BD35F / BD50F** — modelos mais comuns; 35F para até ~150 L, 50F para freezer/maior.
- **ASU (Automatic Start-Up)** — controlador Isotherm sobre Secop; otimiza ciclos.
- **Embraco** — fabricante alternativo de compressor.
- **Compressor hermético** — compressor selado (não desmontável); padrão doméstico/marine.
- **Condensador** — trocador que rejeita calor; ar ou água.
- **Evaporador** — trocador que absorve calor do compartimento frio.
- **Trocador de calor water-cooled** — condensador imerso ou conectado a bomba de água do mar.
- **Placa eutética** — tanque com fluido eutético que armazena frio; congela uma vez, mantém 12-24 h.
- **Peltier (termoelétrico)** — efeito sólido; eficiência baixa, útil em cooler pequeno.
- **COP (Coefficient of Performance)** — relação calor removido / energia elétrica consumida.
- **Duty cycle** — tempo ligado / tempo total; em geladeira marine normal 30-50%.
- **Isolamento PU** — poliuretano expandido; condutividade 0.022-0.028 W/m·K.
- **Ponte térmica** — elemento condutor atravessando isolamento; falha clássica.
- **Vedação de porta (gasket)** — borracha magnética ou selo; falha silenciosa.
- **R-134a (HFC)** — refrigerante dominante 2000-2020; GWP 1430; em phase-down.
- **R-600a (isobutano)** — HC; GWP 3; classe A3 (inflamável); padrão atual em eletrodoméstico.
- **R-290 (propano)** — HC; GWP 3; classe A3 (inflamável); uso crescente.
- **GWP (Global Warming Potential)** — potencial de aquecimento global relativo ao CO₂.
- **ODP (Ozone Depletion Potential)** — potencial de destruição de ozônio.
- **Classe A1/A2L/A3** — classificação de segurança de refrigerante (ASHRAE 34 / ISO 817).
- **Protocolo de Montreal (1987)** — tratado global sobre substâncias que destroem ozônio.
- **Emenda de Kigali (2016)** — adiciona HFC ao Montreal; phase-down global.
- **EPA SNAP** — Significant New Alternatives Policy, EUA.
- **EPA Section 608** — regulação de manuseio/recuperação de refrigerante, EUA.
- **AIM Act 2020** — American Innovation and Manufacturing Act; phase-down HFC nos EUA.
- **EU F-gas 517/2014** — regulamento europeu de gases fluorados.
- **CONAMA 267/2000** — resolução brasileira que proíbe substâncias que destroem ozônio.
- **Portaria MCT 86/2013** — certificação de técnicos de refrigeração no Brasil.
- **Técnico certificado EPA 608** — habilitação nos EUA para manusear refrigerante.
- **Recuperação** — remover refrigerante do sistema para recipiente; obrigatória antes de descarte.
- **Reciclagem** — purificar refrigerante recuperado para reuso.
- **Descarte legal** — entrega a posto revendedor ou empresa certificada.
- **Carga de refrigerante** — quantidade de gás no sistema; típica 30-120 g em equipamento marine.
- **IEC 60335-2-24** — segurança de refrigerador doméstico (limite 150 g HC).
- **Inversor AC-DC** — penaliza eficiência em 10-20%; antipadrão em DC bem projetado.
- **Shore power** — alimentação AC de marina; viabiliza geladeira AC em uso misto.
- **Shunt / BMS** — monitoramento de carga; identifica desvio de consumo precoce.
- **Queda de tensão** — ABYC ≤ 3% em DC; 0.5V em 12V é 4%, já degrada.
- **Charter** — uso comercial; falha de geladeira top 5 em reclamações.
- **Secop (ex-Danfoss)** — marca atual dos compressores BD após spin-off.

## Integração com outras notas

- [[Ar-Condicionado Marine — Sistema Completo]]
- [[Ar-Condicionado Marine 12V DC]]
- [[Icemaker - Máquina de Gelo]]
- [[Bancos de Bateria]]
- [[Placa Solar (DC)]]
- [[Carregador de Bateria (AC To DC)]]
- [[Gerador (AC)]]
- [[Quadro Elétrico e Painel de Distribuição AC-DC]]

## Perguntas que esta nota responde

- Como a geladeira/freezer afeta autonomia e projeto elétrico?
- Por que esse sistema consome tanto quando está mal instalado?
- Como diferenciar falha térmica de falha elétrica na refrigeração de bordo?
- Qual refrigerante o equipamento usa e como ele é regulado?
- Quem pode manusear e descartar refrigerante legalmente no Brasil e nos EUA?
- Quais são as vantagens do compressor BD-Danfoss em relação a sistemas termoelétricos ou AC residenciais?
