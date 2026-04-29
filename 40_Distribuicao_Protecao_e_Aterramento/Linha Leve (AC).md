---
title: "Linha Leve (AC)"
note_type: "system"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "LINHA LEVE (AC) f9e19734f7fb82ebb08a01bde9cf45c6.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "63"
tier_fase_6: "A"
reviewed_on: "2026-04-21"
review_jurisdiction:
  - "Brasil"
  - "internacional"
review_level: "engineering-curated"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
normas_citadas:
  - "ABYC E-11 (AC and DC Electrical Systems on Boats) — §11.5 branch circuits, §11.11 AC protection"
  - "ABYC E-11 §11.5.1 (20 A branch circuit default, 15 A allowed)"
  - "ABYC E-11 §11.11.1.5 (GFCI em áreas molhadas)"
  - "ABYC E-11 §11.11.1.6 (ELCI de 30 mA na entrada AC)"
  - "ISO 13297:2020 (Small craft — AC electrical systems — General requirements)"
  - "ISO 8846:1990 (Small craft — Electrical devices — Protection against ignition of flammable gases)"
  - "IEC 60364-7-709 (Marinas and similar locations)"
  - "IEC 60364-4-41 (Protection against electric shock)"
  - "IEC 60364-4-42 (Protection against thermal effects)"
  - "IEC 60364-4-43 (Protection against overcurrent)"
  - "IEC 60947-2 (Low-voltage circuit breakers)"
  - "IEC 61008-1 (RCCBs sem proteção de sobrecorrente)"
  - "IEC 61009-1 (RCBOs com proteção de sobrecorrente)"
  - "IEC 60898-1/2 (Circuit breakers for household — AC/DC)"
  - "NFPA 70 (NEC) art. 555 — Marinas, Boatyards, Docking Facilities"
  - "NFPA 70 art. 555.35 — GFPE 30 mA, GFCI 5 mA em marinas"
  - "NFPA 70 art. 210 — Branch circuits"
  - "NFPA 70 art. 406 — Receptacles"
  - "UL 943 (GFCI — Ground-Fault Circuit Interrupters)"
  - "UL 498 (Receptacles)"
  - "UL 1449 (Surge Protective Devices)"
  - "UL 1699B (Arc-Fault Circuit Interrupters)"
  - "ABNT NBR 5410:2004 — Instalações elétricas de baixa tensão"
  - "ABNT NBR 5410 §5.1.3.2 — DR ≤ 30 mA em áreas molhadas"
  - "ABNT NBR 14136:2012 — Plugues e tomadas 2P+T"
  - "ABNT NBR IEC 60884-1:2019 — Plugues e tomadas uso doméstico"
  - "ABNT NBR IEC 60669-1 — Interruptores"
  - "NORMAM-05/DPC — Embarcações de esporte e recreio"
  - "NORMAM-01/DPC — Embarcações em navegação marítima"
  - "USCG 33 CFR 183.420 — Grounded AC systems"
  - "USCG 46 CFR 111 — Electrical Engineering Uninspected Passenger Vessels"
family_clusters:
  - "ABYC-USCG (EUA)"
  - "ISO-IEC (internacional)"
  - "NFPA-UL (EUA industrial/marina)"
  - "ABNT-NORMAM (Brasil)"
aliases:
  - "LINHA LEVE (AC)"
  - "Circuitos AC de uso geral"
  - "Light AC branch circuits"
  - "AC convenience circuits"
  - "Cabin AC receptacles"
seo_title: "Linha leve AC em embarcações: tomadas, circuitos de uso geral e proteção"
seo_description: "Arquitetura técnica da linha leve AC em embarcações: circuitos de uso geral, proteção diferencial, setorização, quedas de tensão e integração com shore power, gerador e inversor."
seo_keywords:
  - "linha leve AC embarcação"
  - "tomadas AC barco"
  - "circuitos de uso geral náutico"
  - "proteção diferencial AC embarcações"
geo_queries:
  - "Como organizar a linha leve AC de uma embarcação?"
  - "Quais proteções usar em circuitos AC de uso geral no barco?"
  - "Qual a diferença entre GFCI americano e DR brasileiro em um barco?"
related_notes:
  - "CAIS (Pier) (AC)"
  - "Chaves Seletoras (AC)"
  - "Disjuntores (DC) e (AC)"
  - "Fase e Neutro"
  - "Inversora (DC To AC)"
  - "Linha Pesada (AC)"
  - "Proteção Dr"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
---

# Linha Leve (AC)

> [!abstract] Resumo técnico
> Linha leve AC é a camada de distribuição em corrente alternada dedicada a **tomadas e cargas de uso geral** (TV, som, carregadores, pequenos eletrodomésticos, pontos de apoio em cabine, salão e cockpit). O critério de separação em relação à [[Linha Pesada (AC)]] não é um número mágico de watts, mas **natureza da carga** (inrush, regime, essencialidade), **setorização** (zonas independentes para não derrubar o barco inteiro a cada falha) e **coordenação de proteções** (disjuntor de ramal + DR/GFCI + ELCI de entrada). ABYC E-11 §11.5.1 estabelece o circuito de ramal padrão em 20 A (15 A admitido); §11.11.1.5-1.6 exige GFCI em áreas molhadas e ELCI 30 mA no shore-power inlet. IEC 60364-7-709 e ABNT NBR 5410 estruturam a linha leve por zonas de umidade, com DR ≤ 30 mA em banheiro, galley e áreas externas. Linha leve mal setorizada = falha em um ponto derruba salão, camarotes e cockpit de uma vez.

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **Setorize por zona, não por disjuntor único** — salão, camarotes, banheiros, galley, cockpit, áreas externas: cada zona em ramal próprio com disjuntor independente.
> 2. **Ramal padrão ABYC**: 20 A 120 V ou 16 A 220/230 V (ABYC E-11 §11.5.1), cabo AWG 12 / 2,5 mm² mínimo; 15 A só se toda a arquitetura for coerente com essa corrente.
> 3. **GFCI/DR em áreas molhadas não é opção** — banheiro, galley, cockpit, áreas externas, proa aberta: DR 30 mA dedicado por zona (ABNT NBR 5410 §5.1.3.2; ABYC E-11 §11.11.1.5; NFPA 70 art. 210.8).
> 4. **ELCI 30 mA na entrada de shore-power** — independente do DR de zona; ABYC E-11 §11.11.1.6 (obrigatório em barco novo US 2011+). Protege contra fuga do cabo do cais, cruzeiro de corrente para água.
> 5. **Tomada marine-grade ou industrial para uso marítimo**, não tomada residencial — ambiente vibra, salino e úmido desmonta Pial/Ilumi em 1-2 anos; Hubbell, Marinco, Pass & Seymour têm linha marine.
> 6. **Plugue 2P+T aterrado, sempre** — nunca remover pino terra em adaptador "benjamin"; circuito sem terra = risco de tensão no casco + DR sem referência para atuar.
> 7. **Limite de pontos por ramal**: 8-10 tomadas em 20 A 120 V / 12-15 tomadas em 16 A 230 V (ABNT NBR 5410 estima ~100 VA por tomada em cálculo de projeto).
> 8. **Separação de fontes é responsabilidade da chave seletora**, não da linha leve — inversor, gerador, shore: ver [[Chaves Seletoras (AC)]] para transferência; linha leve só recebe a fonte selecionada.
> 9. **Queda de tensão ≤ 3% do neutral-to-hot**, medida em carga nominal — se > 5%, cabo subdimensionado ou emenda ruim (ABYC E-11.17, NBR 5410 §6.2.7).
> 10. **Documentação no quadro + etiqueta por ramal** — "CAM 01", "BAN MASTER", "GALLEY", "COCKPIT EXT", com tabela de cargas esperadas afixada na porta do quadro.

> [!danger] Quando chamar um especialista
> Estes 9 cenários exigem engenheiro elétrico náutico ou integrador:
> 1. **Disparo diferencial fantasma em UPS / inversor online / fonte chaveada** — correntes de fuga capacitivas normais de uma fonte chaveada somadas em várias cargas disparam DR tipo AC; solução exige DR tipo A ou tipo B (IEC 61008-1) e possivelmente redistribuição de circuitos por fonte.
> 2. **Embarcação com shore-power híbrido 120/240 V (EUA)** — transformador isolador, sistema dual-leg, ELCI por perna, neutro flutuante vs. neutro aterrado (ABYC E-11 §11.6); qualquer erro coloca tensão no casco.
> 3. **Retrofit com dois circuitos independentes em cabines com plugues europeu e americano** — passageiros de várias nacionalidades; exige transformador step-down ou dois barramentos separados com tomada Schuko/NEMA/ABNT claramente identificadas.
> 4. **Tensão no casco medida com voltímetro AC entre mastro/batente e água** — indica cruzeiro de neutro, fuga fase-terra, ou ELCI não aterrado; risco de eletrocussão de banhistas no entorno da embarcação.
> 5. **Linha leve alimentada por inversor a partir de banco Li-Fe** — dimensionamento de inversor, BMS cutoff, possível shock de inrush (carregador de ferramenta, secador) derruba o inversor se não houver soft-start.
> 6. **Instalação comercial (charter, cruzeiro, turismo)** — NORMAM-05, CE/RCD, ABYC Certified; linha leve entra em ensaio com instrumentação calibrada, resistência de isolação 500 V, teste de disparo em 5 e 30 mA em cada zona.
> 7. **Arc-Fault intermitente detectado por AFCI** (IEC 62606 / UL 1699B) — fagulha em luminária, borne frouxo, cabo degradado atrás de forro; localização exige termografia + oscilograma + divisão do ramal em trechos.
> 8. **Integração de sistema solar AC-coupled ou hybrid inverter** (Victron MultiPlus-II, Outback Radian, SMA) em barco — requer ATS, anti-islanding UL 1741-SA, neutro de gerador comutado, e linha leve protegida contra ilhamento.
> 9. **Instalação onde o proprietário reporta choques leves em torneira, chuveiro, escada de popa** — sintoma clássico de tensão fuga-casco; exige teste de resistência de isolação em cada ramal, ensaio de continuidade do aterramento, possível isolador galvânico ou transformador isolador no shore.

## O que é

Na prática de projeto, a linha leve AC reúne os circuitos destinados a:

- tomadas de uso geral;
- pequenos eletrodomésticos (TV, som, notebook, fritadeira de ar, sanduicheira, secador);
- entretenimento e eletrônica de cabine;
- auxiliares de conforto de baixa ou média potência;
- circuitos que não exigem ramal dedicado por alto inrush ou potência sustentada (contrastando com ar-condicionado, boiler, carregador de ≥ 40 A — que são **[[Linha Pesada (AC)]]**).

Ela convive com a linha pesada no mesmo quadro AC, mas **não é "o resto"** — continua exigindo projeto, proteção e documentação do mesmo modo que qualquer outra camada elétrica.

### O que esta nota cobre

- critério para separar linha leve de linha pesada (não é só potência);
- setorização por zona e limite de pontos por ramal;
- proteção diferencial por zona + ELCI de entrada;
- seleção de tomada, plugue, cabo e conexão para ambiente marinho;
- integração com chave seletora de fontes (shore / gerador / inversor);
- normas por jurisdição (ABYC, NFPA/UL, IEC, ABNT, NORMAM);
- falhas em campo e diagnóstico.

## O que diferencia da linha pesada

A diferença útil não é apenas a potência. Linha leve costuma ter:

- **cargas mais dispersas** (várias tomadas pequenas em vários cômodos);
- **maior quantidade de pontos** de consumo;
- **maior importância de setorização** (falha em banheiro não pode apagar salão);
- **mais interação com usuários finais** (hóspede enfia plugue estranho);
- **mais risco de improviso** com extensões, adaptadores e plugues.

Linha pesada, por sua vez, tende a ter **circuitos dedicados** para cargas específicas (ar-condicionado split, compressor de geladeira, boiler, carregador de banco, talha), cada uma com ramal exclusivo, disjuntor próprio e, em muitos casos, contator e proteção térmica dedicada.

### Limite prático usado em projeto

| Categoria | Potência típica por circuito | Ramal típico | Fonte |
| --- | --- | --- | --- |
| **Linha leve** — tomada 2P+T genérica | ≤ 1.500 W em 120 V / ≤ 3.000 W em 230 V | 15-20 A, AWG 12 / 2,5 mm² | ABYC E-11 §11.5.1 |
| **Linha leve reforçada** — galley com cafeteira+micro | 1.800-2.400 W | 20 A dedicada, AWG 12 / 2,5 mm² | ABNT NBR 5410 §9.5.2.1 |
| **Fronteira / caso a caso** — lava-louça portátil, secador, fritadeira grande | 1.500-2.500 W | 20-25 A dedicada, AWG 10 / 4 mm² | avaliação por projeto |
| **Linha pesada** — ar-cond. split, boiler, carregador ≥ 40 A | ≥ 3.000 W | ramal dedicado, cabo específico | ver [[Linha Pesada (AC)]] |

## Arquitetura recomendada

A distribuição madura de linha leve AC costuma incluir:

- **alimentação a partir do quadro AC principal** (pós-seletora de fontes, pós-ELCI geral);
- **divisão por áreas ou funções** — não por "sobra de disjuntor livre";
- **proteção por circuito** (disjuntor AC 15-20 A ou RCBO combinado);
- **proteção diferencial** por zona ou geral + RCBO localizado;
- **identificação clara no quadro** (etiqueta por ramal);
- **compatibilidade com a fonte ativa** — shore, gerador, inversor, ou combinação.

Em vez de "um único disjuntor para todas as tomadas", o correto é pensar por **zonas estruturadas**:

- **salão** (tomadas de TV, som, iluminação de apoio);
- **camarotes** (1 circuito por camarote quando possível; hóspede desliga sem afetar armador);
- **banheiros** (circuito dedicado com DR 30 mA ABNT ou GFCI 5 mA ABYC/NFPA);
- **galley** (2 circuitos: um para cafeteira/micro, outro para fritadeira/sanduicheira — alto simultâneo);
- **cockpit / área externa** (circuito separado com DR 30 mA + caixa IP65);
- **sala de máquinas / compartimento técnico** (se houver tomada para diagnóstico/ferramenta — dedicada, AC não-inversor).

### Topologia típica

```
  Shore Inlet            Gerador             Inversor
  (50A/240V)            (7-15 kVA)          (3-5 kVA)
       │                    │                    │
       ├── Isolador         │                    │
       │   Galvânico        │                    │
       │                    │                    │
       └──────┬─────────────┴────────────┬───────┘
              │                          │
              ▼                          │
       [CHAVE SELETORA]                  │
         Break-before-Make               │
              │                          │
              ▼                          │
       [ELCI 30 mA]   ← ABYC E-11.11.1.6 │
              │                          │
       [DISJ. GERAL AC]                  │
              │                          │
              ├─── [DR 30mA] ── [DJ 16A] ── Salão
              ├─── [DR 30mA] ── [DJ 16A] ── Camarote 1
              ├─── [DR 30mA] ── [DJ 16A] ── Camarote 2
              ├─── [DR 30mA] ── [DJ 20A] ── Galley Cafeteira
              ├─── [DR 30mA] ── [DJ 20A] ── Galley Mesa
              ├─── [DR 30mA] ── [DJ 16A] ── Banheiro Master (RCBO)
              ├─── [DR 30mA] ── [DJ 16A] ── Banheiro Convidados
              └─── [DR 30mA] ── [DJ 16A] ── Cockpit / Externo IP65
```

## Cargas típicas

São exemplos usuais de carga da linha leve:

| Carga | Potência típica | Ramal adequado |
| --- | --- | --- |
| TV LED 32-55" | 60-150 W | 16 A salão |
| Home theater / soundbar | 50-200 W | 16 A salão |
| Notebook + monitor | 90-200 W | 16 A qualquer |
| Carregador de celular / smartwatch | 5-45 W | qualquer |
| Secador de cabelo | 1.200-2.000 W | **20 A dedicada** (banheiro) |
| Chapinha / modelador | 80-200 W | 16 A banheiro |
| Cafeteira elétrica | 600-1.200 W | 20 A galley |
| Micro-ondas | 900-1.500 W | **20 A dedicada** (galley) |
| Fritadeira de ar | 1.400-1.800 W | **20 A dedicada** |
| Sanduicheira / grill | 700-1.500 W | 20 A galley |
| Ferro de passar | 1.000-1.800 W | 20 A dedicada |
| Carregador ferramenta elétrica | 50-300 W | 16 A qualquer |
| Aquecedor portátil | 1.000-2.000 W | **linha pesada** (> 1.500 W contínuo) |

Mesmo nessa faixa, um conjunto de pequenas cargas pode saturar um circuito mal setorizado: galley com cafeteira 1.000 W + micro 1.200 W + sanduicheira 1.500 W simultâneos = 3.700 W = 16 A a 230 V = **estoura disjuntor de 16 A** se estiverem no mesmo ramal.

## Critérios corretos de projeto

### 1. Setorização

Setorizar melhora:

- **diagnóstico** — falha localizada em um ramal;
- **seletividade** — a proteção mais próxima atua, não o geral;
- **continuidade operacional** — resto do barco segue funcionando;
- **manutenção** — técnico desliga um ramal sem interferir em outros.

Uma falha em um banheiro, por exemplo, não deveria apagar todas as tomadas do barco. Se apagar, o projeto está errado.

**Regra prática**: em barco de 40-60 pés, 8-12 ramais de linha leve não são exagero — são o mínimo para operação confortável e manutenção segura.

### 2. Proteção diferencial

Circuitos de uso geral e áreas úmidas exigem proteção diferencial bem pensada. A aplicação pode ser:

- **DR geral 30 mA por zona** — um DR por setor (salão, camarotes, banheiros, cockpit);
- **RCBO por circuito** — combinação DR + disjuntor em um só dispositivo (mais caro, mais seletivo);
- **combinação de proteção geral e proteção adicional localizada** — ELCI 30 mA na entrada + RCBO 30 mA por ramal molhado.

**Tipos de DR / GFCI por padrão**:

| Tipo | Onde usa | Sensibilidade |
| --- | --- | --- |
| **GFCI (EUA)** | banheiros, galley, cockpit, áreas externas em US | **5 mA** UL 943 |
| **ELCI (EUA)** | entrada de shore-power em US | **30 mA** ABYC E-11.11.1.6 |
| **DR tipo AC (BR/EU)** | corrente senoidal limpa | 30 mA ABNT/IEC 61008 |
| **DR tipo A (BR/EU)** | cargas com eletrônica (fonte chaveada) | 30 mA, captura senoidal + pulsante |
| **DR tipo B (BR/EU)** | inversores, VFDs, carregador EV | 30 mA, captura DC residual |
| **GFPE (EUA)** | marinas, docas | **30 mA** NFPA 70 art. 555.35 |

A solução depende da **topologia do quadro**, da **seletividade desejada** e da **presença de fontes eletrônicas** que possam exigir dispositivos adequados ao tipo de corrente residual esperado.

> [!warning] Atenção — tipo AC é insuficiente em quadro com inversor/fonte chaveada
> DR tipo AC só captura corrente residual senoidal limpa. Inversor de bordo, UPS e fontes chaveadas de eletrônica injetam componentes DC e pulsantes na fuga capacitiva normal — um DR tipo AC pode **não disparar** ou disparar em valor fora do nominal. Use DR **tipo A** em barco com eletrônica moderna, **tipo B** em barco com inversor híbrido, variadores ou carregador EV.

### 3. Queda de tensão e comprimento

Mesmo na linha leve, cabos longos, conexões ruins e adaptadores improvisados degradam tensão em carga. Isso afeta desempenho, aquece conexões e aumenta falhas intermitentes.

**Meta ABYC E-11.17 / ABNT NBR 5410 §6.2.7**: ΔV ≤ 3% da tensão nominal sob corrente nominal. Para circuitos críticos (carregador, eletrônica sensível), ΔV ≤ 2%.

**Fórmula prática** (AC monofásico, cobre):

```
ΔV (V) ≈ 2 × L (m) × I (A) × ρ (Ω·mm²/m) / S (mm²)
```

Onde ρ(Cu) ≈ 0,0172 Ω·mm²/m. Para cabo 2,5 mm² a 16 A por 20 m: ΔV ≈ 2 × 20 × 16 × 0,0172 / 2,5 ≈ 4,4 V → 1,9% em 230 V (ok), 3,7% em 120 V (ajustar para AWG 10 / 4 mm²).

### 4. Ambiente de instalação

Em embarcação, tomada, borne e caixa sofrem com:

- **vibração** (motor, hélice, onda);
- **condensação** (umidade noturna, ar-condicionado);
- **spray salino** (área externa, entrada de cockpit);
- **ciclos térmicos** (sol direto na tomada externa);
- **mau uso por adaptação de plugues** (hóspede usa adaptador chinês forçando terminais).

Tomada "residencial comum" pode funcionar, mas **isso não a torna boa solução técnica** para ambiente marinho. Em áreas externas ou de alta exposição:

- **IP44 mínimo** para cockpit coberto;
- **IP55-IP65** para exposição direta a spray;
- **marine-grade** (Hubbell HBL, Marinco, Pass & Seymour Weather-Protected) — bornes em bronze dourado, contato estanhado, caixa em policarbonato ou alumínio marinizado;
- **tomadas com tampa mola** em todas as áreas externas;
- **cabo marine-grade** (cobre estanhado classe 5, jaqueta XLPE ou EPR) até o ponto.

## Integração com as fontes AC

Linha leve pode ser alimentada por:

- **[[CAIS (Pier) (AC)]]** — shore-power 30 A/120 V ou 50 A/240 V com ELCI 30 mA e GFPE 30 mA no cais (NFPA 70 art. 555);
- **[[Gerador (AC)]]** — 3-15 kVA monofásico ou trifásico, neutro aterrado no gerador;
- **[[Inversora (DC To AC)]]** — 1-5 kVA a partir de banco 12/24/48 V, senoidal pura;
- **sistemas híbridos** com transferência automática (MultiPlus-II, Outback, Mastervolt).

O projeto precisa garantir coerência entre:

- **seletora ou transferência de fontes** (ver [[Chaves Seletoras (AC)]]);
- **presença ou não de neutro referenciado** conforme a topologia (gerador tem neutro aterrado na caixa; inversor pode ser float ou bondado);
- **atuação correta de [[Proteção Dr]]** (exige referência de terra coerente);
- **limites de potência do inversor** quando a linha leve for alimentada em navegação ou fundeio (não ligar secador 2 kW num inversor 2 kVA sem soft-start).

### Matriz de fontes e limitações

| Fonte | Potência típica | DR compatível | Cuidado principal |
| --- | --- | --- | --- |
| Shore 30 A 120 V (EUA) | 3,6 kW | GFCI 5 mA + ELCI 30 mA | conexão do neutro no quadro |
| Shore 50 A 240 V (EUA) | 12 kW | ELCI 30 mA por perna | sistema dual-leg, balanceamento |
| Shore 16-32 A 230 V (BR/EU) | 3,7-7,4 kW | DR 30 mA + ELCI equivalente | cabo suje no cais |
| Gerador 5-10 kVA | 5-10 kW | DR 30 mA | soft-start em AC motores |
| Inversor 2-5 kVA | 2-5 kW | DR tipo A ou B | saturação por motor single-phase |
| MultiPlus-II 3000 VA híbrido | 2,4 kW + passthrough | DR tipo B | ajuste de transferência 20 ms |

## Falhas típicas em campo

As mais comuns são:

- **tomada aquecendo por borne frouxo** — detectada com termografia ou toque (nunca tocar se > 45 °C);
- **circuito caindo por excesso de carga agregada** — 3 kW de galley num ramal 16 A;
- **disparo diferencial intermitente com equipamento específico** — UPS velho, carregador de ferramenta sem filtro;
- **ponto de tomada "morto" por emenda ou borne solto** — normalmente atrás de forro, difícil diagnóstico;
- **tensão baixa por conector, adaptador ou cabo inadequado** — "benjamin" 6 em 1, adaptador NEMA→Schuko;
- **circuito de uso geral misturado com carga que deveria estar em linha pesada** — fritadeira grande + micro + cafeteira no mesmo ramal;
- **DR que dispara após 30 minutos** — corrente de fuga capacitiva somada de várias fontes chaveadas (UPS + carregadores + adaptadores);
- **tensão no casco** — fuga fase-terra em carga com aterramento ruim; medível entre casco e água com voltímetro AC.

## Diagnóstico profissional

O diagnóstico deve seguir o caminho da energia, do cais até a carga:

1. **fonte AC** (shore/gerador/inversor) — medir V entre fase e neutro, entre fase e terra, entre neutro e terra;
2. **entrada do quadro** — antes da seletora e após;
3. **dispositivo de proteção geral** (ELCI, disjuntor geral, DR geral);
4. **circuito derivado** (disjuntor de ramal, DR de zona);
5. **ponto de consumo** (tomada, caixa de derivação);
6. **carga conectada** (equipamento em si).

**Medições úteis**:

- **tensão sem carga e com carga** — diferença aponta queda no cabo;
- **corrente do circuito** (clamp AC) — confirmar soma de cargas;
- **continuidade e integridade de bornes** (clamp torque a 2-3 N·m em borne pequeno);
- **temperatura de tomadas, conectores e disjuntores** — termografia em regime de carga nominal;
- **comportamento do DR/RCBO com diferentes cargas** — teste de disparo em 5 mA e 30 mA (MRT-12 ou similar);
- **resistência de isolação fase-terra e neutro-terra** — megômetro 500 V, esperar ≥ 1 MΩ;
- **tensão entre casco e água** — com fonte AC ligada; deve ser ≤ 0,5 V AC.

## Boas práticas

- **dividir a linha leve por setores ou funções** desde o projeto inicial;
- **usar componentes adequados ao ambiente marinho** ou, no mínimo, a áreas úmidas e vibrantes (IP44+);
- **evitar adaptadores permanentes** como solução estrutural (benjamin, régua descartável);
- **manter diagrama e identificação de circuitos atualizados** após cada retrofit;
- **prever circuitos externos com cuidado adicional** de vedação (IP55+) e proteção (DR 30 mA dedicado);
- **coordenar o uso da linha leve com a potência disponível** no cais, no gerador ou no inversor;
- **etiquetar cada disjuntor** com nome da zona e lista de tomadas alimentadas;
- **instalar torneiras de teste de DR** no quadro (botão "TEST" — acionar a cada 30 dias);
- **medir corrente de cada ramal em regime normal** e registrar no dossiê da embarcação;
- **usar proteção contra surtos (SPD/DPS)** na entrada de shore-power — tempestade no cais injeta surto no cabo.

## Erros que fragilizam a base técnica

Frases a evitar:

- "todas as tomadas num disjuntor só, pra simplificar o quadro";
- "linha leve é coisa de pouca corrente, tomada residencial dá conta";
- "DR pode ficar só no geral do quadro";
- "adaptador benjamin é temporário" (nunca é temporário);
- "tensão no casco é normal em barco";
- "se caiu o DR, é ele que está com defeito" (quase sempre é a instalação);
- "circuito externo não precisa de DR dedicado, já tem o do quadro";
- "plug sem terra funciona igual, é só não tomar choque".

Todas simplificam demais e induzem instalação ruim — algumas são **ilegais** conforme ABNT NBR 5410 e ABYC E-11.

## Relação com outros sistemas

- **[[CAIS (Pier) (AC)]]** — fonte primária em marina; ELCI é a primeira barreira.
- **[[Chaves Seletoras (AC)]]** — define qual fonte alimenta a linha leve.
- **[[Disjuntores (DC) e (AC)]]** — proteção de sobrecorrente por ramal.
- **[[Fase e Neutro]]** — arquitetura de referência de neutro aterrado ou flutuante.
- **[[Inversora (DC To AC)]]** — fonte AC em fundeio/navegação.
- **[[Linha Pesada (AC)]]** — diferença de escopo e ramais dedicados.
- **[[Proteção Dr]]** — DR/RCBO/GFCI/ELCI detalhado.
- **[[Quadro Elétrico e Painel de Distribuição AC-DC]]** — estrutura onde linha leve vive.
- **[[Hotline (DC)]]** — exemplo de circuito "always-on" em DC; linha leve AC em geral **não** deve ter tomadas sempre energizadas sem justificativa.
- **[[Aterramento - Negativo - Terra]]** — referência de terra compartilhada com linha leve.

## Normas e referências

### Por família e jurisdição

| Família | Norma | Escopo |
| --- | --- | --- |
| **ABYC (EUA)** | E-11 §11.5.1 | branch circuit 20 A default |
| ABYC | E-11 §11.11.1.5 | GFCI 5 mA em áreas molhadas |
| ABYC | E-11 §11.11.1.6 | ELCI 30 mA na entrada AC |
| ABYC | E-11 §11.17 | queda de tensão ≤ 3% |
| **USCG (EUA)** | 33 CFR 183.420 | grounded AC systems |
| USCG | 46 CFR 111 | Uninspected Passenger Vessels |
| **NFPA (EUA)** | NFPA 70 art. 210 | branch circuits |
| NFPA | NFPA 70 art. 406 | receptacles |
| NFPA | NFPA 70 art. 555.35 | GFPE 30 mA em marina |
| **UL (EUA)** | UL 943 | GFCI 5 mA |
| UL | UL 498 | receptacles |
| UL | UL 1449 | SPD |
| UL | UL 1699B | AFCI |
| **ISO (internacional)** | ISO 13297:2020 | AC electrical systems small craft |
| ISO | ISO 8846:1990 | ignition protection |
| **IEC (internacional)** | IEC 60364-7-709 | marinas |
| IEC | IEC 60364-4-41 | proteção contra choque |
| IEC | IEC 60364-4-42 | proteção térmica |
| IEC | IEC 60364-4-43 | sobrecorrente |
| IEC | IEC 60947-2 | LV circuit breakers |
| IEC | IEC 61008-1 | RCCB |
| IEC | IEC 61009-1 | RCBO |
| IEC | IEC 60898-1/2 | disjuntores residenciais AC/DC |
| **ABNT (Brasil)** | NBR 5410 §5.1.3.2 | DR 30 mA em áreas molhadas |
| ABNT | NBR 14136:2012 | plugue 2P+T brasileiro |
| ABNT | NBR IEC 60884-1 | plugues e tomadas domésticas |
| ABNT | NBR IEC 60669-1 | interruptores |
| **NORMAM (Brasil)** | NORMAM-05 / NORMAM-01 | recreio / marítimo |

### Comparação prática entre jurisdições

- **EUA (ABYC + NFPA + UL)**: circuito de ramal padrão 20 A / 120 V, GFCI 5 mA em áreas molhadas, ELCI 30 mA obrigatório na entrada do shore-power desde 2011 (ABYC E-11.11.1.6), GFPE 30 mA no cais (NFPA 555).
- **Internacional (ISO/IEC)**: ISO 13297 cobre AC em pequenas embarcações; IEC 60364-7-709 cobre marinas; RCBO tipo A/B é padrão em Europa para cargas eletrônicas.
- **Brasil (ABNT + NORMAM)**: NBR 5410 §5.1.3.2 exige DR 30 mA em áreas molhadas; plugue 2P+T (NBR 14136) substituiu universalmente o NEMA e o Schuko desde 2011; NORMAM-05 remete a ABYC/ISO para detalhamento.
- **Europa (CE/RCD + IEC)**: CE/RCD Directiva 2013/53/UE exige conformidade com ISO 13297; DR tipo A é o padrão para circuito com eletrônica; tipo B onde houver inversor.
- **Navio classificado (SOLAS / IACS)**: regras de classe (DNV, Lloyd's, BV, ABS); normalmente não é aplicável a recreio.

## Glossário rápido

1. **AC (Alternating Current)** — corrente alternada.
2. **AFCI** — Arc-Fault Circuit Interrupter (UL 1699B).
3. **Anti-islanding** — proteção contra ilhamento (UL 1741-SA).
4. **ATS (Automatic Transfer Switch)** — chave de transferência automática de fontes.
5. **Backfeed** — corrente que volta pelo ramal errado e reenergiza barramento.
6. **Branch circuit** — circuito de ramal.
7. **Cable gland (prensa-cabo)** — vedação de cabo na caixa.
8. **Clamp meter** — alicate amperímetro AC/DC.
9. **Coordenação de proteções** — seletividade entre disjuntor geral e ramal.
10. **Corrente de fuga** — corrente residual entre fase e terra.
11. **DR (Dispositivo Residual)** — termo ABNT para RCCB/RCBO/GFCI.
12. **Dual-leg** — sistema 120/240 V com duas fases de 120 V (EUA).
13. **ELCI** — Equipment Leakage Circuit Interrupter (ABYC, 30 mA).
14. **EPR** — Ethylene Propylene Rubber (isolação de cabo marine).
15. **GFCI** — Ground-Fault Circuit Interrupter (5 mA, UL 943).
16. **GFPE** — Ground-Fault Protection of Equipment (30 mA, NFPA 555).
17. **Hot (fio)** — condutor fase (vermelho/preto, EUA).
18. **Hubbell / Marinco / Pass & Seymour** — fabricantes marine-grade de tomadas.
19. **Identificação de ramal** — etiqueta no disjuntor + plaqueta na tomada.
20. **Inrush current** — corrente de partida (motor, fonte chaveada).
21. **IP44/55/65** — grau de proteção contra água e poeira (IEC 60529).
22. **Isolador galvânico** — dispositivo que bloqueia corrente DC no terra do cais.
23. **MCB (Miniature Circuit Breaker)** — disjuntor residencial (IEC 60898).
24. **MCCB (Molded Case Circuit Breaker)** — disjuntor caixa moldada (IEC 60947-2).
25. **Marine-grade** — componente especificado para ambiente marítimo (vibração, sal, umidade).
26. **NEMA 5-15 / 5-20** — plugue americano 15 A / 20 A.
27. **Neutro aterrado / flutuante** — referência do neutro à terra ou não.
28. **Pino-terra** — terceiro pino do plugue 2P+T.
29. **RCBO** — Residual Current Breaker with Overcurrent (DR + disjuntor em um).
30. **RCCB / RCD** — Residual Current Circuit Breaker / Device (DR puro).
31. **Ramal dedicado** — circuito exclusivo para uma carga.
32. **Schuko (CEE 7/4)** — plugue europeu 2P+T 16 A.
33. **Senoidal pura (inversor)** — THD < 3%.
34. **Setorização** — divisão por zonas.
35. **Shore-power inlet** — tomada de cais (Hubbell HBL, Marinco).
36. **Soft-start** — partida suave de inversor/motor.
37. **Split-phase** — 120/240 V com neutro central (EUA).
38. **SPD / DPS** — Surge Protective Device / Dispositivo de Proteção contra Surto.
39. **Standby AC** — modo espera de equipamentos AC.
40. **Step-down transformer** — transformador redutor (240→120 V).
41. **Tensão no casco** — tensão AC medida entre casco e água.
42. **Tipo AC / A / B (DR)** — classificação de DR por corrente residual detectada.
43. **Torque de aperto** — torque específico do parafuso (borne, disjuntor).
44. **Tripolar (2P+T)** — fase + neutro + terra.
45. **UPS (Uninterruptible Power Supply)** — no-break.
46. **Voltage drop (ΔV)** — queda de tensão.
47. **Weather-Protected (WP/WR)** — tomada externa com selo de intempéries.
48. **XLPE** — Cross-Linked Polyethylene (isolação de cabo).
49. **Zonas molhadas** — banheiro, galley, cockpit externo, proa aberta.
50. **Zoneamento AC** — divisão de circuitos por função e risco.

## FAQ

**Como separar corretamente a linha leve da linha pesada em uma embarcação?**

Critério prático: **linha leve** reúne circuitos ≤ 1.500 W em 120 V ou ≤ 3.000 W em 230 V, com pontos de tomada dispersos e cargas de uso variável (TV, som, eletrônica de cabine, pequenos eletrodomésticos). **Linha pesada** tem ramais dedicados para uma única carga de alto inrush ou potência sustentada (ar-condicionado split, boiler, carregador ≥ 40 A, compressor de geladeira grande). Cargas de fronteira (secador 2 kW, fritadeira grande) ficam em ramal dedicado 20-25 A que, formalmente, ainda é linha leve mas com capacidade reforçada.

**Quais critérios tornam um circuito AC de uso geral realmente bem projetado?**

Cinco critérios: (1) setorização por zona funcional — não por sobra de disjuntor; (2) ramal padrão 16-20 A com cabo coerente (2,5 mm² ou AWG 12); (3) DR 30 mA em áreas molhadas + ELCI 30 mA na entrada; (4) tomadas marine-grade ou mínimo IP44 em áreas de umidade; (5) documentação — diagrama unifilar + etiqueta por ramal + tabela de cargas afixada no quadro.

**Como evitar que tomadas e circuitos de conveniência virem ponto de falha recorrente?**

Evitar três armadilhas frequentes: (a) sobrecarga por acúmulo de cargas num mesmo ramal (galley com cafeteira+micro+sanduicheira simultâneos estoura 16 A); (b) tomada residencial em área exposta (sal+vibração destrói em 12-24 meses); (c) adaptadores "benjamin" e réguas de qualidade duvidosa que se tornam permanentes. Solução: setorizar corretamente, especificar IP44+ nas áreas úmidas, e treinar operação para não usar adaptadores.

**Qual a diferença entre GFCI americano e DR brasileiro?**

**GFCI (UL 943)** é a sensibilidade **5 mA** destinada a proteção de pessoas contra choque em áreas molhadas — padrão americano para banheiro, galley, cockpit, áreas externas. **DR 30 mA (ABNT NBR 5410 / IEC 61008)** é a sensibilidade padrão europeia e brasileira para proteção de pessoas, tem curva de atuação mais tolerante a fugas capacitivas naturais. Em **barco** a recomendação técnica é combinar: **ELCI 30 mA na entrada** (norma ABYC e equivalente europeu) + **DR ou GFCI de maior sensibilidade no ramal molhado** (5 mA ABYC, 30 mA ABNT/IEC — alguns projetos adotam 10 mA como compromisso).

**Posso usar tomada 2P (sem terra) em barco?**

Não. Qualquer tomada na linha leve AC deve ser 2P+T com o pino-terra conectado à malha de terra da embarcação. Ausência do terra: (i) DR não atua por falta de referência coerente; (ii) carcaça metálica de equipamento energiza-se em falha; (iii) tensão pode aparecer no casco via fuga indireta. ABNT NBR 14136 exige 2P+T desde 2011; ABYC E-11.3 exige 3-wire (hot+neutral+ground) em todo AC de bordo.

**Como lidar com disparo intermitente de DR em barco antigo?**

Três causas mais comuns: (1) **soma de fugas capacitivas** de várias fontes chaveadas ultrapassa 15-25 mA (limite prático do DR 30 mA) — solução: redistribuir cargas entre DRs, ou trocar por DR tipo A/B; (2) **umidade em caixa de tomada externa** gera fuga intermitente — solução: vedar IP55+; (3) **equipamento específico defeituoso** (geladeira velha com fuga de compressor, UPS com capacitor inchado) — solução: isolar ramal a ramal até identificar o ofensor. Nunca resolver "aumentando a corrente do DR" — corrente > 30 mA não protege mais a pessoa contra choque.

**Inversor pode alimentar a linha leve toda?**

Depende do dimensionamento. Inversor 2 kVA ≈ 8,7 A em 230 V ≈ 16,7 A em 120 V. Se o pico momentâneo da linha leve estourar isso (secador + micro simultâneos), inversor desliga por proteção. Solução: (a) inversor maior (3-5 kVA); (b) contatoria automática que desconecta ramais pesados quando na alimentação por inversor (MultiPlus-II PowerAssist faz isso); (c) educação do operador — "em fundeio não ligue secador+micro juntos".

## Integração com outras notas

- [[CAIS (Pier) (AC)]]
- [[Chaves Seletoras (AC)]]
- [[Disjuntores (DC) e (AC)]]
- [[Fase e Neutro]]
- [[Inversora (DC To AC)]]
- [[Linha Pesada (AC)]]
- [[Proteção Dr]]
- [[Quadro Elétrico e Painel de Distribuição AC-DC]]
- [[Aterramento - Negativo - Terra]]
- [[Hotline (DC)]]

## Perguntas que esta nota responde

- Como separar corretamente a linha leve da linha pesada em uma embarcação?
- Quais critérios tornam um circuito AC de uso geral realmente bem projetado?
- Como evitar que tomadas e circuitos de conveniência virem ponto de falha recorrente?
- Qual a diferença entre GFCI americano e DR brasileiro em um barco?
- Posso usar tomada 2P (sem terra) em barco?
- Como lidar com disparo intermitente de DR em barco antigo?
- Inversor pode alimentar a linha leve toda?
