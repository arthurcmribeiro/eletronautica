---
title: "Contatores (AC)"
note_type: "technical-note"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "CONTATORES (AC) f0f19734f7fb820895d40138dc40c1ac.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "60"
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
  - "https://webstore.iec.ch/publication/4116"
normas_citadas:
  - "IEC 60947-4-1 (Contactors and motor-starters — Electromechanical contactors and motor-starters)"
  - "IEC 60947-4-2 (AC semiconductor motor controllers and starters — soft-starters)"
  - "IEC 60947-5-1 (Control circuit devices — Electromechanical)"
  - "IEC 60947-1 (Low-voltage switchgear and controlgear — General rules)"
  - "IEC 60947-6-2 (Control and protective switching devices — CPS)"
  - "IEC 60947-8 (Control units for built-in thermal protection — PTC)"
  - "IEC 60529 (IP Code)"
  - "IEC 62262 (IK Code)"
  - "IEC 60092-302 (Electrical installations in ships — Switchgear and controlgear)"
  - "IEC 60034-1 (Rotating electrical machines — Rating and performance)"
  - "UL 508 (Industrial Control Equipment)"
  - "UL 60947-4-1 (Contactors — harmonized with IEC)"
  - "NEMA ICS 2 (Industrial Control and Systems — Controllers, Contactors and Overload Relays)"
  - "NEMA ICS 5 (Industrial Control and Systems — Control Circuit and Pilot Devices)"
  - "ABYC E-11 (AC and DC Electrical Systems on Boats)"
  - "ABYC A-6 (HVAC) — partida de compressores"
  - "ABYC A-7 (Boat Heating Systems)"
  - "ABYC A-31 (Battery Chargers and Inverters)"
  - "ISO 13297:2020 (Small craft — Electrical systems — AC installations)"
  - "ISO 8846:1990 (Ignition protection)"
  - "NFPA 70 (NEC) art. 430 (motors, motor circuits, controllers)"
  - "ABNT NBR IEC 60947-4-1 (Contatores e pré-partidas)"
  - "ABNT NBR 5410 (Instalações elétricas de baixa tensão)"
  - "ABNT NBR IEC 60529 (IP)"
  - "NORMAM-05/DPC (Embarcações de esporte e recreio)"
  - "NORMAM-01/DPC (Embarcações em navegação marítima)"
  - "DNV-RU-SHIP Pt.4 Ch.8 §4 (Distribution systems)"
family_clusters:
  - "IEC-ABNT (internacional/Brasil)"
  - "UL-NEMA (EUA)"
  - "ABYC-USCG (EUA marine)"
  - "DNV-classificadoras (navios)"
aliases:
  - "CONTATORES (AC)"
  - "Contator AC"
  - "AC contactor"
  - "Contator de potência"
seo_title: "Contatores (AC) em embarcações: seleção, falhas e diagnóstico"
seo_description: "Critérios profissionais para aplicação de contatores AC em embarcações: categoria de emprego, bobina, intertravamento, falhas típicas e integração com ar-condicionado, boilers e cargas pesadas."
seo_keywords:
  - "contatores AC embarcações"
  - "contator compressor ar condicionado náutico"
  - "contator carga indutiva"
  - "comando de potência embarcação"
geo_queries:
  - "Como selecionar um contator AC para ar-condicionado náutico?"
  - "Quais falhas são mais comuns em contatores AC de embarcações?"
  - "Qual categoria de emprego (AC-1/AC-3/AC-4) escolher?"
related_notes:
  - "Ar-Condicionado Marine — Sistema Completo"
  - "Chaves Seletoras (AC)"
  - "Disjuntores (DC) e (AC)"
  - "Gerador (AC)"
  - "Inversora (DC To AC)"
  - "Linha Pesada (AC)"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
  - "Relés e Relés de Estado Sólido"
---

# Contatores (AC)

> [!abstract] Resumo técnico
> Contator AC é um dispositivo de manobra para comutar cargas de potência com alta frequência operacional e com capacidade de suportar arco, inrush e regime de serviço muito superiores aos de um relé comum. Em embarcações, aparece principalmente em ar-condicionado, resistências, bombas AC e sequências automáticas de partida/parada. IEC 60947-4-1 (internacional) e UL 508 (EUA) padronizam o componente por **categoria de emprego** (AC-1 a AC-4), e a seleção correta depende mais do tipo de carga que da corrente nominal — um contator AC-1 30 A falha ao comandar um compressor AC-3 de 15 A.

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **Categoria de emprego é mais importante que corrente** — AC-1 (resistência pura) / AC-3 (motor gaiola em gaiola, partida direta) / AC-4 (motor com reversão, inching, jog). Um contator AC-3 30 A serve um motor de 7,5 kW; um AC-1 30 A, não.
> 2. **Dimensione pelo FLC (Full Load Current) × fator de categoria** — para AC-3 use valor nominal direto; para AC-4 dimensione 2× o FLC; para AC-1 fica igual; exemplo: motor de 11 kW 400V trifásico ~ 22 A → contator AC-3 25 A.
> 3. **Bobina com supressão sempre** — bobina AC: varistor/RC snubber; bobina DC: diodo freewheel + TVS. Sem supressão, eletrônica de comando queima por sobretensão de abertura (kickback 300-800 V).
> 4. **Inrush de motor é 6-8× FLC por 100-300 ms** — contator subdimensionado solda contato em 10-20 partidas.
> 5. **Relé térmico/eletrônico é OBRIGATÓRIO** para motor — contator não protege contra sobrecarga; dimensione relé para 1,05-1,15× FLC com classe 10 (padrão) ou classe 20 (cargas de inércia alta).
> 6. **Intertravamento mecânico + elétrico** em reversão ou paralelismo de dois contatores — não confie em temporização de relé; use kit físico do fabricante.
> 7. **Contato auxiliar NO (normally open)** para selo/hold-in no circuito de comando (ladder); **NC (normally closed)** para sinal de "desligado" em PLC.
> 8. **Vida elétrica × vida mecânica** — vida mecânica tipicamente 10⁷ ciclos; vida elétrica em AC-3 tipicamente 10⁶; em AC-4 pode cair para 2×10⁵ — dimensione para duração esperada.
> 9. **Marine-grade quando possível** — contator industrial em casaria com salinidade sofre corrosão de bornes em 2-3 anos; prefira linha marine ou proteja em painel IP55+ com secante.

> [!danger] Quando chamar um especialista
> Estes 9 cenários exigem engenheiro elétrico ou integrador, não improviso de eletricista generalista:
> 1. **Motor trifásico > 15 kW em embarcação com gerador** — análise de queda de tensão na partida, seletividade de proteção, soft-starter ou VFD; partida direta pode fazer gerador "cair" (undervoltage trip) e causar blackout do barco.
> 2. **Ar-condicionado marine com múltiplos compressores e sequenciamento automático** — lógica de load shedding, priorização de bombas de água do mar, anti-short-cycle (delay > 3 min entre partidas), gerenciamento por BMS/PLC.
> 3. **Retrofit de compressor R-410A/R-454B para R-290 (propano)** — compartimento passa a zona classificada (Ex) — exige contator ATEX/IECEx ou gestão por IS (intrinsically safe).
> 4. **Sistema com VFD (Variable Frequency Drive) + contator by-pass** — filtro dv/dt, reatância de motor, análise EMC, coordenação com proteção diferencial tipo B (drives trifásicos geram DC residual que cega RCD tipo A).
> 5. **Banco de capacitores para correção de fator de potência** — contator de capacitor (AC-6b em IEC 60947-4-1) com resistor de pre-charge; capacitor em paralelo sem pre-charge gera inrush > 200× FLC.
> 6. **Transformador de isolação ou shore power > 100 A** — inrush magnético (10-25× nominal por 10-30 ciclos) exige contator específico (AC-6a) ou resistor de partida comutado.
> 7. **Navio comercial sob classificadora** — contator IEC 60092-302 certificado classe DNV/Lloyd's/BV/ABS; contator UL/NEMA industrial não é aceito.
> 8. **Investigação de partida intermitente, contato soldado ou bobina queimada recorrente** — análise de transitórios de comutação, qualidade da alimentação, coordenação de proteções.
> 9. **Certificação CE/RCD, ABYC compliance ou inspeção USCG** — dossiê técnico com diagrama de comando, memorial de categoria de emprego, teste de operação.

## O que é

Contator é um equipamento de **comando**, não de proteção. Sua função é abrir e fechar circuitos de potência mediante o acionamento de uma bobina de controle, normalmente por termostato, controlador, PLC, pressostato, relé intermediário ou sistema de automação.

A diferença prática entre um relé e um contator não é apenas "tamanho". O contator é construído para:

- suportar manobra repetitiva sob carga (10⁵ a 10⁷ ciclos);
- lidar melhor com correntes de partida e com arco elétrico (câmara de extinção dupla ou soprador magnético);
- aceitar acessórios de intertravamento, contatos auxiliares e sinalização;
- operar em categorias de emprego específicas para motores, resistências e cargas mistas (IEC 60947-4-1).

## Onde se aplica a bordo

As aplicações mais típicas são:

- **compressores e bombas de água do mar** de [[Ar-Condicionado Marine — Sistema Completo]] — cargas AC-3 com partida direta ou AC-4 com reversão de bomba;
- **resistências de [[Boiler]]** e aquecedores — cargas AC-1 puras;
- **cargas de [[Linha Pesada (AC)]]** comandadas remotamente — load shedding;
- **sequências de partida**, permissivos e intertravamentos em quadros AC;
- **comutação de cargas** em sistemas com [[Gerador (AC)]], [[Inversora (DC To AC)]] e automação;
- **partida de motores de winch elétrico/hidráulico** (em AC) — AC-4 com reversão;
- **comutação de bancos de capacitores** para correção de fator de potência (AC-6b) — mais raro em recreio, comum em comercial.

## Princípio de funcionamento

Quando a bobina é energizada, o núcleo magnético atrai o conjunto móvel e fecha os contatos principais. Ao retirar o comando, a mola de retorno abre os contatos. O arco que aparece na abertura é controlado por geometria de contato e câmara de extinção apropriadas ao equipamento.

Isso importa porque:

- cargas **resistivas puras** (AC-1) são relativamente fáceis de manobrar — arco se extingue no zero natural da AC;
- **motores, compressores e transformadores** (AC-3, AC-4, AC-6a) impõem inrush e fator de potência menores — o arco pode sustentar-se por meio ciclo ou mais;
- **capacitores** (AC-6b) têm inrush capacitivo violento (dI/dt alto) — exigem pre-charge ou contator específico;
- selecionar apenas pela corrente nominal quase sempre leva a erro.

### Categorias de emprego IEC 60947-4-1 — detalhes

| Categoria | Carga | Make | Break | Exemplo |
| --- | --- | --- | --- | --- |
| **AC-1** | resistiva, FP > 0,95 | 1× Ie | 1× Ie | aquecedor, resistência de boiler, load bank |
| **AC-2** | motor de rotor bobinado | 2,5× Ie | 2,5× Ie | uso raro em náutica |
| **AC-3** | motor gaiola, partida e parada normal | 6× Ie | 1× Ie | compressor scroll, bomba centrífuga |
| **AC-4** | motor gaiola, partida + plug + inching | 6× Ie | 6× Ie | winch com reversão, guincho AC |
| **AC-5a** | comutação de lâmpadas de descarga | 3× Ie | 3× Ie | iluminação fluorescente |
| **AC-5b** | comutação de lâmpadas incandescentes | 1,5× Ie | 1,5× Ie | iluminação rara em AC náutico |
| **AC-6a** | comutação de transformadores | 20× Ie make / 1× Ie break | — | transformador de isolação |
| **AC-6b** | comutação de capacitores | 20× Ie / 1× Ie | — | banco de capacitores |
| **AC-7a** | eletrodoméstico indutivo leve | 1,5× Ie | 1,5× Ie | uso doméstico |
| **AC-7b** | motor eletrodoméstico | 8× Ie | 8× Ie | uso doméstico |

Fator Ie = corrente nominal de emprego.

## Critérios corretos de seleção

### 1. Categoria de emprego

A escolha deve seguir a categoria de utilização do fabricante e da família do contator. Em termos práticos:

- **cargas resistivas e aquecimento** → AC-1;
- **motores e compressores partida normal** → AC-3;
- **motores com reversão, inching, frenagem** → AC-4;
- **transformadores e indutores** → AC-6a;
- **capacitores** → AC-6b.

Contator "de mesma corrente" pode ser adequado para uma resistência (AC-1) e inadequado para um compressor (AC-3).

### 2. Corrente e regime real da carga

Avaliar:

- **corrente nominal em regime** (Ie);
- **corrente de partida** (LRA — Locked Rotor Amps ou Inrush);
- **número de manobras por hora** (frequência: ex. AC-3 acima de 1000 op/h exige contator de alta durabilidade);
- **temperatura interna do painel** (derating por temperatura: tipicamente -10% a 40°C, -20% a 55°C);
- **altitude, ventilação e grau de proteção** exigido.

Compressores de ar-condicionado, bombas e motores exigem margem real de projeto. O dado crítico não é só a corrente estabilizada, mas o comportamento na partida e na abertura sob carga.

### 3. Tensão e natureza da bobina

A bobina pode ser:

- **AC** (24 V, 48 V, 110 V, 120 V, 220 V, 230 V, 240 V, 380 V, 400 V, 440 V, 480 V AC);
- **DC** (12 V, 24 V, 48 V, 110 V, 220 V DC);
- **universal**, em linhas específicas (faixa ampla 24-240 V AC/DC com eletrônica interna).

Em embarcações, é comum usar **bobina DC** quando o comando vem de eletrônica de bordo ou automação em 12 V ou 24 V. Nesses casos:

- a tensão precisa bater com o circuito de comando (tolerância tipicamente -15%/+10%);
- deve-se prever supressão de surtos compatível com a eletrônica de acionamento.

**Bobinas DC normalmente pedem diodo freewheel + TVS ou módulo supressor** especificado pelo fabricante. **Bobinas AC usam RC snubber, varistor ou supressor equivalente, nunca um diodo simples** (o diodo em AC funciona como retificador meio-ciclo — aquece e queima).

### 4. Contatos auxiliares e intertravamento

Em arquitetura profissional, o contator raramente trabalha sozinho. São comuns:

- **contatos auxiliares NO/NC** para realimentação (selo/hold-in), alarme e sinal de posição;
- **intertravamento mecânico** (barra entre dois contatores impede fechamento simultâneo);
- **intertravamento elétrico** (NC do contator A em série com bobina de B);
- **permissivo** de pressostato, fluxo, temperatura e nível;
- **bloqueio de partidas simultâneas** para gerenciamento de carga (load shedding);
- **módulo de supressão** para bobina (ACI — arc suppressor, RC ou varistor);
- **flag mecânico de sinalização** (bandeira indicando "fechado").

### 5. Relé de sobrecarga (overload relay)

Contator **não protege contra sobrecarga**. Para motor, é obrigatório instalar:

- **relé térmico bimetálico** (classe 10 padrão, classe 20 para carga de inércia alta como centrifuga longa, classe 5 para alta frequência);
- **relé eletrônico** (oferece proteção mais precisa, reset remoto, comunicação Modbus/IO-Link);
- **proteção térmica do motor (PTC)** via módulo IEC 60947-8 para motores com termistor interno.

Dimensionar relé para 1,05-1,15× FLC do motor.

## O que ele não substitui

Contator não substitui:

- **disjuntor** (proteção contra curto-circuito);
- **fusível** (proteção contra curto-circuito de alta energia);
- **DR/RCD** (proteção diferencial contra falta à terra);
- **relé de proteção térmica ou eletrônico de motor** (proteção contra sobrecarga);
- **chave seccionadora de manutenção** (lockout/tagout).

Quem protege é o sistema de proteção a montante e, quando aplicável, o relé de sobrecarga ou o próprio controlador do equipamento.

## Modos de falha mais comuns

Os defeitos mais recorrentes em campo são:

- **bobina aberta ou degradada** — resistência fora da especificação, isolamento rompido;
- **tensão de comando insuficiente** para fechamento confiável (< 85% da nominal AC, < 80% DC) — contator vibra ("chattering") e solda;
- **contatos principais erodidos, soldados ou com resistência elevada** — queda de tensão > 1 V sob carga;
- **vibração mecânica** por subtensão, sujeira ou armadura desgastada;
- **aquecimento por aperto ruim** nos terminais (torque fora de especificação);
- **contator subdimensionado** para o regime da carga (categoria errada);
- **uso de contator AC em aplicação DC**, o que é tecnicamente inadequado (arco sustentado, sem zero-crossing);
- **falha da câmara de extinção** (material cerâmico rachado por choque térmico).

Em ambiente marinho, **oxidação, condensação e salinidade** aceleram falhas de contato e de bornes. Contator industrial aberto em casaria sem IP adequado tem vida útil 3-5× menor.

## Diagnóstico profissional

### Verificação do circuito de comando

Confirmar:

- **presença da tensão correta** na bobina (multímetro AC/DC);
- **compatibilidade** entre tensão de comando e bobina instalada (etiqueta × realidade);
- **integridade de termostatos, pressostatos, sensores de fluxo e permissivos**;
- **presença de supressão de surtos** quando exigida;
- **resistência da bobina** desconectada (comparar com datasheet — tipicamente 50-500 Ω para bobinas 24 V DC, 1-10 kΩ para 230 V AC).

Se há comando, mas o contator não fecha, suspeitar de bobina defeituosa, travamento mecânico ou subtensão.

### Verificação do circuito de potência

Com carga em operação, medir:

- **tensão a montante e a jusante**;
- **queda de tensão nos contatos** (ΔV < 100 mV típico; > 500 mV indica contato degradado);
- **corrente por fase ou por polo** (alicate amperímetro);
- **aquecimento localizado** em bornes e contatos (termografia se disponível).

Queda de tensão anormal em contator fechado aponta contato degradado. Corrente acima do esperado pode indicar problema na carga, não no contator.

### Diagnóstico em compressores e motores

Se o contator opera, mas o equipamento não parte corretamente, verificar antes de condená-lo:

- **subtensão da fonte** (gerador sob carga pode cair 10-15% em partida);
- **capacitor de partida, protetor térmico ou soft-start** do compressor;
- **bloqueio mecânico** (compressor travado por líquido, bomba com impeller preso);
- **proteção de motor atuando** (thermal overload, PTC);
- **seletividade inadequada** do disjuntor a montante (disjuntor curva C quando motor precisa curva D);
- **desequilíbrio de fases** > 2% em sistema trifásico (NEMA MG-1 limita a 1%).

## Boas práticas de projeto e montagem

- selecionar contator pela **categoria de emprego**, não só pela corrente;
- prever proteção adequada a montante e, quando necessário, **relé de sobrecarga** (bimetálico ou eletrônico);
- instalar em quadro ventilado, seco e com acesso para inspeção (IP55+ em casaria, IP65 em convés);
- usar **terminais corretos, torque controlado** (conforme datasheet, tipicamente 1,7-3,0 Nm para M4, 6-8 Nm para M8) e reaperto em manutenção;
- **separar circuito de comando do circuito de potência** (canalizações distintas ou blindagem);
- **documentar** claramente bobina, contatos principais, auxiliares e lógica de intertravamento em diagrama de comando (ladder ou FBD);
- manter **peça de reposição** quando o equipamento comandado for crítico à operação;
- instalar **módulo de supressão de surto** compatível com a bobina (varistor/RC em AC, diodo+TVS em DC);
- evitar **acionamentos simultâneos** de múltiplos contatores pesados (pico de corrente na fonte de comando) — usar temporização ou soft-starter;
- em painel trifásico, **marcar ordem de fases** (L1/L2/L3 ou R/S/T) para garantir rotação correta do motor;
- prever **ventilação forçada ou natural** em painéis com múltiplos contatores pesados (cada contator dissipa 3-20 W em regime).

## Erros de projeto e de campo

Os mais danosos são:

- usar **relé comum onde deveria haver contator** (vida elétrica inadequada);
- usar **contator AC em carga DC** (arco sustentado sem zero-crossing);
- **ignorar corrente de partida** do compressor (dimensionar só por FLC);
- **acionar bobina DC sem supressão** adequada (kickback destrói PLC/microcontrolador);
- **proteger o circuito apenas "porque o disjuntor geral existe"** (sem relé térmico específico, motor queima);
- **deixar o contator como único ponto de seccionamento** de manutenção (exige seccionadora separada para lockout);
- **escolher contator AC-1 para compressor AC-3** (vida elétrica colapsa);
- **ignorar derating por temperatura** em sala de máquinas quente (40-60°C ambiente interno);
- **não reapertar terminais** após primeiras horas de operação (afrouxamento térmico inicial);
- **misturar contatores de marcas/famílias diferentes** em partida estrela-triângulo (intertravamento mecânico incompatível).

## Relação com outros sistemas

- **[[Ar-Condicionado Marine — Sistema Completo]]** — aplicação típica de contator AC-3/AC-4 em compressor/bomba.
- **[[Chaves Seletoras (AC)]]** — muitos ATS usam contatores internamente (break-before-make).
- **[[Disjuntores (DC) e (AC)]]** — proteção a montante, coordenação com relé térmico.
- **[[Gerador (AC)]]** — fonte típica com impacto de partida em contator a jusante.
- **[[Inversora (DC To AC)]]** — fonte com limite de pico que influi em partida direta.
- **[[Linha Pesada (AC)]]** — cargas típicas comandadas por contator.
- **[[Quadro Elétrico e Painel de Distribuição AC-DC]]** — invólucro do contator.
- **[[Relés e Relés de Estado Sólido]]** — alternativa para cargas menores ou comutação de alta frequência.

## Normas e referências

### Por família e jurisdição

| Família | Norma | Escopo |
| --- | --- | --- |
| **IEC (internacional)** | IEC 60947-4-1 | contatores e partidas eletromecânicas |
| IEC | IEC 60947-4-2 | soft-starters AC |
| IEC | IEC 60947-5-1 | dispositivos de comando |
| IEC | IEC 60947-1 | switchgear BT — regras gerais |
| IEC | IEC 60947-8 | proteção térmica PTC |
| IEC | IEC 60529 / 62262 | IP / IK |
| IEC | IEC 60092-302 | switchgear para navios |
| IEC | IEC 60034-1 | máquinas rotativas — rating |
| **UL (EUA)** | UL 508 | industrial control equipment |
| UL | UL 60947-4-1 | contatores harmonizados com IEC |
| **NEMA (EUA)** | NEMA ICS 2 | controladores, contatores, overload |
| NEMA | NEMA ICS 5 | dispositivos de controle e piloto |
| **NFPA (EUA)** | NFPA 70 art. 430 | motores e controladores |
| **ABYC (EUA marine)** | E-11 | sistemas AC e DC em embarcações |
| ABYC | A-6 | HVAC e partida de compressor |
| ABYC | A-7 | boilers e aquecedores |
| **ISO (internacional marine)** | ISO 13297:2020 | AC em pequenas embarcações |
| ISO | ISO 8846:1990 | ignition protection |
| **ABNT (Brasil)** | NBR IEC 60947-4-1 | contatores |
| ABNT | NBR 5410 | instalações de baixa tensão |
| ABNT | NBR IEC 60529 | IP |
| **NORMAM (Brasil)** | NORMAM-05/-01 | recreio / marítimo |
| **Classificadoras** | DNV-RU-SHIP Pt.4 Ch.8 §4 | navios classificados |

### Comparação prática entre famílias

- **IEC 60947-4-1**: categoria de emprego AC-1 a AC-8b e DC-1 a DC-13; conceito europeu amplamente usado globalmente.
- **NEMA ICS 2**: classificação por size (00, 0, 1, 2, 3, 4, 5) baseada em HP de motor em 480 V ou 240 V; mais conservador que IEC.
- **UL 508 / UL 60947-4-1**: harmonização entre NEMA tradicional e IEC moderna; UL 60947-4-1 é o padrão atual para novos projetos.
- **ABYC**: não define categoria própria — remete a NEMA/IEC para o componente; foca em aplicação marine (ignition protection, IP).

## Glossário rápido

1. **AC-1 a AC-8b** — categorias de emprego IEC 60947-4-1 em corrente alternada.
2. **AC coil** — bobina AC do contator; usa varistor/RC como supressor.
3. **Accessory module** — módulo acessório (supressor, timer, contato auxiliar).
4. **Arc chute** — câmara de extinção do arco.
5. **Auxiliary contact (NA/NO/NF/NC)** — contato auxiliar normalmente aberto/fechado.
6. **Bimetallic overload relay** — relé térmico bimetálico (classe 10/20/5).
7. **Capacitor switching** — comutação de banco de capacitores (AC-6b).
8. **Chattering** — vibração por subtensão ou bobina marginal.
9. **Class 10/20/5 (overload)** — tempo de disparo do relé térmico (s em 7,2× FLC).
10. **Coil inrush** — pico de corrente no fechamento da bobina (~6× hold).
11. **Coil hold** — corrente de manutenção após selo magnético.
12. **Contact lifetime** — vida útil do contato (elétrica e mecânica).
13. **Contactor** — contator eletromecânico.
14. **DC-1 a DC-13** — categorias de emprego em corrente contínua.
15. **Derating** — redução de capacidade por temperatura ou altitude.
16. **Diode freewheel** — diodo roda-livre para bobina DC.
17. **Direct-on-line (DOL)** — partida direta do motor pelo contator.
18. **Electrical life** — número de ciclos elétricos até falha.
19. **Fator de potência (FP)** — cos φ da carga.
20. **FLC / FLA (Full Load Current/Amps)** — corrente nominal do motor em regime.
21. **Hold-in / sealing contact** — contato auxiliar NO em paralelo com botão start (selo).
22. **Ie (corrente nominal de emprego)** — corrente que o contator conduz em regime AC-X.
23. **Impulse withstand voltage (Uimp)** — tensão suportável de impulso (kV).
24. **Inching (jog)** — partida repetitiva e curta para posicionamento.
25. **Inrush current** — corrente de partida — 6-8× FLC em motor gaiola.
26. **Interlock (mechanical/electrical)** — intertravamento mecânico/elétrico.
27. **IP code** — proteção contra pó e água (IEC 60529).
28. **Latched contactor** — contator de engate mecânico — mantém posição sem energia constante.
29. **LRA (Locked Rotor Amps)** — corrente de rotor travado, inrush máxima do motor.
30. **Main contact** — contato principal do circuito de potência.
31. **Mechanical life** — vida útil mecânica sem carga (tipicamente 10⁷).
32. **Motor starter** — partida de motor = contator + relé de sobrecarga.
33. **Normally Closed (NC)** — contato normalmente fechado.
34. **Normally Open (NO)** — contato normalmente aberto.
35. **Operational voltage (Ue)** — tensão nominal de emprego.
36. **Overload relay** — relé de sobrecarga (bimetálico ou eletrônico).
37. **Pick-up / drop-out voltage** — tensão de atração/desarme da bobina.
38. **Plug braking (reversão para frenagem)** — inversão rápida para frenar — AC-4.
39. **Poles (2-pole / 3-pole / 4-pole)** — número de polos principais.
40. **Pre-charge resistor** — resistor de pré-carga para capacitor/inversor.
41. **Pull-in / drop-out time** — tempo de fechamento/abertura da bobina.
42. **PTC thermistor (protection)** — termistor PTC embutido no motor.
43. **Rated insulation voltage (Ui)** — tensão nominal de isolação.
44. **RC snubber** — snubber RC para bobina AC.
45. **Relay (control relay)** — relé de comando, diferente de contator.
46. **Reversing contactor pair** — par de contatores para reversão (intertravado).
47. **Service factor** — fator de serviço do motor (NEMA 1.0/1.15).
48. **Size (NEMA 00 a 5)** — tamanho NEMA de contator por HP.
49. **Soft-starter** — partida suave por semicondutor (SCR) — AC-53.
50. **Star-delta (Y-Δ) starter** — partida estrela-triângulo para reduzir inrush.
51. **Suppression (coil)** — supressão de surto de abertura da bobina.
52. **Surge suppressor / MOV** — supressor de surto / varistor.
53. **TeSys / LC1 / 3RT / CJX** — famílias comerciais: Schneider TeSys/LC1, Siemens Sirius 3RT, Chint CJX, ABB AF, Eaton DILM.
54. **Thermal magnetic overload** — proteção térmica + magnética (motor protection circuit breaker).
55. **Utilization category** — ver AC-X / DC-X.

## FAQ

**Como escolher corretamente um contator AC para uso náutico?**

Comece pela categoria de emprego (AC-1 resistiva / AC-3 motor partida normal / AC-4 motor com reversão). Depois, some FLC nominal × fator de categoria × margem marine (1,25×). Finalize com tensão de bobina compatível com o comando (AC ou DC) e classificação IP do painel.

**Quando um relé não é suficiente e o circuito pede contator?**

Corrente > 20 A em regime contínuo, carga indutiva (motor, compressor, transformador, bobina), manobra frequente (> 50 ciclos/dia), ambiente com vibração ou necessidade de intertravamento com outro dispositivo. Relé comum falha em qualquer desses cenários.

**Quais defeitos fazem um contator fechar, vibrar ou queimar em serviço?**

- Fechar e vibrar: subtensão na bobina (< 85% nominal), bobina marginal, ou contato auxiliar de selo ruim.
- Queimar a bobina: sobretensão, bobina AC alimentada com DC (sem limitação), curto no circuito de comando.
- Soldar os contatos: categoria inadequada (AC-1 num motor AC-3), inrush excessivo, sobrecarga sustentada por falta de relé térmico.

**Posso usar contator trifásico comandando apenas monofásico?**

Sim, em 2 polos, desligando o 3º. Mas a corrente de cada polo deve ser coerente com a categoria (ex.: contator trifásico AC-3 25 A opera uma fase a 25 A). Não paraleliza polos para "somar corrente" — a resistência de contato entre polos não é idêntica, gera desequilíbrio.

**Qual a diferença entre AC-3 e AC-4?**

AC-3: partida e parada normal do motor em gaiola — inrush 6× Ie no make, break em 1× Ie (motor já acelerado).
AC-4: partida seguida de reversão ou inching — break também em 6× Ie (motor ainda rotacionando, stop-and-reverse). Vida elétrica cai 5-10× em AC-4 comparado a AC-3.

**Preciso mesmo de supressão na bobina?**

Em comando por PLC, microcontrolador ou saída de relé eletrônico: sim, obrigatório. Em bobina AC industrial alimentada por contato de botoeira sem eletrônica, pode-se omitir. Em bobina DC comandada por transistor sem diodo freewheel, a sobretensão de abertura (Ldi/dt) queima o transistor em milissegundos.

**Contator AC aguenta DC se a corrente for menor?**

Não de forma segura. O arco em DC sustenta-se sem zero-crossing natural. Um contator AC-3 480 V tem sopro magnético otimizado para AC; em DC 24-48 V consegue romper, mas a partir de 60-80 V DC o arco soldá a partir de poucas operações. Use contator DC-rated (DC-1 a DC-13 em IEC 60947-4-1).

## Integração com outras notas

- [[Ar-Condicionado Marine — Sistema Completo]]
- [[Chaves Seletoras (AC)]]
- [[Disjuntores (DC) e (AC)]]
- [[Gerador (AC)]]
- [[Inversora (DC To AC)]]
- [[Linha Pesada (AC)]]
- [[Quadro Elétrico e Painel de Distribuição AC-DC]]
- [[Relés e Relés de Estado Sólido]]

## Perguntas que esta nota responde

- Como escolher corretamente um contator AC para uso náutico?
- Quando um relé não é suficiente e o circuito pede contator?
- Quais defeitos fazem um contator fechar, vibrar ou queimar em serviço?
- O que é categoria de emprego AC-1/AC-3/AC-4 e por que importa mais que a corrente?
- Que tipo de supressão de surto cada tipo de bobina precisa?
