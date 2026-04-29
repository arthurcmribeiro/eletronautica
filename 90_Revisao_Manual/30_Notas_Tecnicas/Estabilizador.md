---
title: "Estabilizador"
note_type: "technical-note"
domain: "90_Revisao_Manual"
source_file: "ESTABILIZADOR bed19734f7fb83f5b4ae011fe6302611.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "51"
tier_fase_6: "A"
reviewed_on: "2026-04-21"
review_jurisdiction:
  - "Brasil"
  - "internacional"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
  - "https://www.seakeeper.com/"
  - "https://www.abtmarine.com/"
  - "https://www.cmcmarine.com/"
  - "https://naiad.com/"
review_level: "engineering-curated"
normas_citadas:
  - "ABYC A-16 - Electrical Safety"
  - "ABYC E-11 - AC and DC Electrical Systems on Boats"
  - "ABYC E-13 - Lithium-Ion Batteries (for gyro battery systems)"
  - "ABYC H-3 - Boat Hull Maintenance (bonding of submerged actuators)"
  - "ABYC P-24 - Electric Propulsion Systems"
  - "ISO 10133:2017 - Small craft - Extra-low-voltage DC installations"
  - "ISO 13297:2020 - Small craft - AC installations"
  - "ISO 12215 - Small craft - Hull construction and scantlings (fin mounting reinforcement)"
  - "ISO 16315:2016 - Small craft - Electric propulsion system"
  - "ISO 8846:1990 - Small craft - Electrical devices - Protection against ignition of flammable gases"
  - "ISO 19665:2021 - Small craft - Stabilizing appendages - Fin stabilizer"
  - "IEC 60529:2013 - Degrees of protection provided by enclosures (IP Code)"
  - "IEC 61508:2010 - Functional safety of electrical/electronic/programmable electronic safety-related systems"
  - "IMO MSC.137(76) - Standards for ship manoeuvrability (reference for stabilization trials)"
  - "SOLAS II-1 - Construction - Subdivision and stability, machinery and electrical installations"
  - "DNV-GL Ship Rules Pt.6 Ch.5 - Passenger comfort (ride control and stabilization)"
  - "Lloyd's Register LR-PCR - Passenger Comfort Rating"
  - "ABS Guide for Passenger Comfort on Ships"
  - "CE Machinery Directive 2006/42/EC (for EU-flagged vessels)"
  - "EN ISO 12100:2010 - Safety of machinery - General principles for design"
  - "EN ISO 13849-1:2015 - Safety-related parts of control systems"
  - "ISO 3448:1992 - Industrial liquid lubricants - ISO viscosity classification"
  - "ISO 11158:2023 - Hydraulic fluids Family H"
  - "ISO 6743-4:2015 - Classification - Family H (Hydraulic systems)"
  - "ISO 4406:2021 - Hydraulic fluid power - Fluid contamination coding"
  - "DIN 51524 Part 3 - HVLP hydraulic fluids"
  - "NEMA MG 1 - Motors and Generators (for gyro motor drives)"
  - "ISO 8846:1990 - Ignition protection"
  - "UL 1500 - Ignition-Protected Marine Products"
  - "SAE J1171 - Marine Ignition Protection"
  - "NBR 11213:2020 - Óleos hidráulicos"
  - "NBR 14134:2015 - Óleos lubrificantes - Terminologia"
  - "NORMAM-01/DPC - Embarcações empregadas na navegação em mar aberto"
  - "NORMAM-03/DPC - Embarcações empregadas na navegação interior"
  - "NORMAM-05/DPC - Homologação de material de salvatagem"
aliases:
  - "ESTABILIZADOR"
  - "Estabilizador de movimento"
  - "Stabilizer"
  - "Anti-roll system"
  - "Fin stabilizer"
  - "Gyro stabilizer"
seo_title: "Estabilizador de embarcação: fins, giroscópio, hidráulica, energia e diagnóstico"
seo_description: "Guia técnico sobre estabilizadores de movimento em embarcações: aletas (ABT/CMC/NAIAD/Quantum), giroscópios (Seakeeper), demanda elétrica/hidráulica, fluido ISO VG 46 HVLP, sensores, controle e falhas."
seo_keywords:
  - "estabilizador embarcação"
  - "gyro stabilizer boat"
  - "fin stabilizer marine"
  - "anti-roll boat system"
  - "Seakeeper"
  - "ABT TRAC CMC NAIAD Quantum"
  - "óleo hidráulico estabilizador"
geo_queries:
  - "Qual a diferença entre estabilizador giroscópico e de aletas na embarcação?"
  - "Como diagnosticar perda de desempenho no estabilizador de movimento do barco?"
  - "Qual fluido hidráulico usar em estabilizador ABT ou NAIAD?"
  - "O Seakeeper precisa de gerador ligado permanentemente?"
related_notes:
  - "Óleos Hidráulicos Marine — Guia Completo"
  - "Flap"
  - "Thruster"
  - "Motor de Trim - Tilt"
  - "Plataforma de Popa Elétrica - Hidráulica"
  - "Gerador (AC)"
  - "Bancos de Bateria"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
---

# Estabilizador

> [!abstract] Resumo técnico
> Nesta base, `Estabilizador` refere-se ao sistema de estabilização de movimento da embarcação, e não a estabilizador de tensão. O tema envolve sensores inerciais, lógica de controle, atuadores hidráulicos ou giroscópios, energia disponível e comportamento hidrodinâmico ou giroscópico do sistema. É das cargas mais complexas do barco: integração com hidráulica, elétrica, eletrônica e estrutura exige abordagem sistêmica.

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **Duas famílias tecnológicas** — (a) aletas hidráulicas (ABT-TRAC, CMC, NAIAD Dynamics, Quantum Marine), que atuam com escoamento; (b) giroscópio (Seakeeper, Mitsubishi ARG, TOHMEI), que atua por momento angular independente da velocidade.
> 2. **Aletas exigem velocidade mínima (6-8 nós tipicamente)** — NAIAD/Quantum "Zero Speed" usam aletas rotativas que funcionam em fundeio.
> 3. **Giroscópio funciona em fundeio E em navegação** — vantagem principal do Seakeeper; desvantagem: consumo elétrico alto (2-5 kW regime) e warm-up de 30-45 min.
> 4. **Energia é restrição central** — aletas hidráulicas 10-40 kW de pico (sistemas grandes); giroscópio 2-5 kW contínuo + 5-10 kW partida.
> 5. **Fluido hidráulico em aletas: ISO VG 46 HVLP** é padrão — bombas axiais de alta pressão (200-350 bar) pedem classe de limpeza ISO 4406 17/15/12 ou melhor.
> 6. **Giroscópio NÃO tem hidráulica "de aletas"** — tem refrigeração a água do volante (bomba + trocador); fluido é glicol/água; não é fluido hidráulico.
> 7. **IMU/sensor inercial + CPU definem desempenho** — hardware bom com software antigo tem desempenho fraco; firmware é parte do produto.
> 8. **Estabilizador não anula ondas** — reduz rolagem em 70-90% em condição calibrada; não substitui navegação/catamarã/comportamento de casco.
> 9. **Integração elétrica exige projeto** — gerador + banco + conversor + proteção dimensionados como sistema, não como "adicionar estabilizador".

> [!danger] Quando chamar um especialista (9 cenários)
> 1. **Ruído metálico novo no giroscópio** — rolamento do volante em alta rotação (até 10000 RPM) é ponto crítico; parar operação até inspeção especializada.
> 2. **Volante do giroscópio não acelera ou acelera sem controle** — inversor ou motor comprometido; warm-up normal 30-45 min; fora disso é falha.
> 3. **Aleta hidráulica com movimento limitado em apenas um sentido** — válvula, cilindro ou atuador angular comprometido; risco de esforço estrutural assimétrico em mar agitado.
> 4. **Vazamento hidráulico visível em sistema de fins** — alta pressão (200-350 bar); risco de perda súbita de função E de contaminação do interior do casco.
> 5. **Óleo leitoso em sistema de fins** — água no circuito; exige drenagem e diagnóstico de trocador de calor antes de qualquer operação.
> 6. **Falha de IMU detectada no sistema** — estabilizador pode operar em modo degradado sem sinalização clara; inspeção urgente de técnico certificado do fabricante.
> 7. **Sobrecarga em gerador quando estabilizador ativa** — banco/gerador subdimensionado ou fator de potência degradado; risco de desarme em mar agitado.
> 8. **Vibração do casco quando giroscópio ativo** — desbalanceamento do volante ou fixação comprometida; risco estrutural grave.
> 9. **Perícia pós-acidente (virada, rolagem severa)** — estabilizador pode ter registrado evento; preservar logs e dados; evidência para investigação.

## O que é

O estabilizador é o sistema usado para reduzir rolagem (movimento de adernamento) e, em certas arquiteturas, melhorar conforto e comportamento dinâmico da embarcação.

As principais tecnologias são:

- **aletas estabilizadoras (`fins`)** — apêndices hidrodinâmicos que geram força de oposição quando o barco rola;
- **giroscópios estabilizadores** — volante de massa rotativo em cardan que gera momento correctivo;
- **sistemas ativos correlatos** em embarcações específicas (tanques de rolagem anti-roll tanks, jato/water-based em alguns).

## O que ele não é

Não se trata aqui de regulador ou estabilizador de tensão AC. Esse uso do termo é diferente e não corresponde ao escopo desta base temática.

## Aletas versus giroscópio

As soluções mais comuns têm comportamentos distintos:

| Característica | Aletas (fins) | Giroscópio |
|---|---|---|
| Fabricantes | ABT-TRAC, CMC Marine, NAIAD Dynamics, Quantum Marine | Seakeeper, Mitsubishi ARG, TOHMEI |
| Funcionamento com barco parado | Limitado (exceto "Zero Speed" rotativas) | Sim (modo fundeio é padrão) |
| Velocidade mínima de operação | 6-8 nós (convencionais) / 0 kt (Zero Speed) | 0 kt (estático e dinâmico) |
| Peso do equipamento | Baixo (aletas são leves; peso estrutural é do reforço) | Alto (volante 100-1500 kg) |
| Consumo elétrico | Baixo (bomba hidráulica 200-500 W típico entre ciclos) | Alto (motor + refrigeração 2-5 kW contínuo) |
| Consumo hidráulico | Alto (picos 10-40 kW em manobra severa) | Nulo |
| Warm-up | Imediato (alguns minutos para aquecer óleo) | 30-45 min para volante atingir RPM |
| Barulho | Silencioso | Zumbido audível do volante (abafado em gabinete) |
| Instalação | Requer apêndice externo + reforço estrutural | Interno; reforço estrutural local |

Escolher entre eles envolve:

- porte da embarcação (gyros pequenos cobrem barcos até 12-15 m; fins cobrem qualquer tamanho);
- velocidade típica (veleiro ou trawler lento pende para gyro);
- uso em navegação ou fundeio (fundeio pede gyro ou Zero Speed fin);
- energia disponível (gyro exige gerador "esperando");
- espaço e peso;
- custo (gyro tipicamente mais caro para o mesmo "nível de conforto").

## Aletas — hidráulica e controle

### Arquitetura

- **aletas submersas** nas laterais do casco, próximas ao meio-nau;
- **bomba hidráulica central** (geralmente axial de pistões, 200-350 bar);
- **acumuladores hidropneumáticos** para resposta rápida;
- **atuadores rotativos** (torque motors) ou cilindros lineares para girar aletas;
- **IMU (Inertial Measurement Unit)** com acelerômetros e giroscópios MEMS;
- **CPU de controle** com algoritmo PID ou modelo mais sofisticado.

### Fluido hidráulico

Sistemas de fins são hidraulicamente exigentes:

- **Fluido padrão** — ISO VG 46 HVLP (DIN 51524 Part 3) em quase todos os fabricantes; alguns sistemas premium usam fluido sintético específico;
- **Pressão** — 200-350 bar em regime, picos até 400 bar em manobra severa;
- **Classe de limpeza** — ISO 4406 17/15/12 ou melhor (servo-válvulas exigem baixa contaminação);
- **Volume** — 20-80 L em barcos 15-25 m; 100-300 L em mega-yachts;
- **Troca** — anual em uso intenso ou conforme análise laboratorial;
- **Filtragem** — filtro de alta pressão + filtro de retorno + respiro com desumidificante.

**Riscos específicos:**

- contaminação reduz vida útil de servo-válvulas em 60-80%;
- ar no circuito causa ruído, perda de resposta e cavitação;
- superaquecimento (> 80°C contínuo) oxida fluido e degrada vedação.

Ver também:

- [[Óleos Hidráulicos Marine — Guia Completo]]

### Ride control vs anti-roll

Alguns sistemas (NAIAD Ride Control, Humphree Interceptor com IMU) fazem mais que anti-roll:

- controle de atitude longitudinal (pitch/trim);
- redução de arfagem em ondas de proa;
- integração com flap/interceptor em comando unificado.

## Giroscópio — arquitetura

### Como funciona

- **volante de alta densidade** (ferro ou tungstênio) girando em alta rotação (5000-10000 RPM);
- **cardan (gimbal)** permite que o eixo do volante se incline;
- **quando o barco rola**, o volante resiste por momento angular e gera momento oposto;
- **controle ativo**: freio no cardan ou motor controla o ângulo de precessão, otimizando o momento restaurador.

### Componentes

- **motor do volante** — AC trifásico com inversor; pode ser síncrono permanente ou indução;
- **mancais/rolamentos** — ponto crítico de confiabilidade; manutenção especializada;
- **sistema de refrigeração** — água/glicol (glycol-water mix), bomba, trocador de calor marine;
- **freio/atuador do cardan** — hidráulico ou eletromecânico;
- **IMU e CPU** — idêntico conceitualmente ao de fins.

### Consumo real

Seakeeper típico:

- **warm-up** (30-45 min): 3-6 kW (volante acelerando contra inércia);
- **regime** (volante em RPM nominal): 2-4 kW (perdas em rolamentos + refrigeração);
- **trabalhando em onda severa**: 5-8 kW (pico momentâneo).

O barco precisa ter gerador dimensionado para o consumo contínuo + pico, ou banco + inversor que sustente.

## Energia e integração

Estabilizador é sistema relevante para a arquitetura energética.

Dependendo da tecnologia, ele pode exigir:

- **alimentação AC significativa** (gyro: 3-phase 230V/400V em grandes; 115/230V em pequenos);
- **apoio de gerador** (quase sempre em gyro; em fins de barcos grandes);
- **suporte de banco/inversor em certas fases** (warm-up rápido pode usar banco em paralelo com gerador);
- **controle dedicado e proteção coordenada** (breaker + filtros EMC + partida suave).

Ver também:

- [[Gerador (AC)]]
- [[Bancos de Bateria]]
- [[Quadro Elétrico e Painel de Distribuição AC-DC]]

## Sensores e controle

O sistema depende de:

- **sensores inerciais** — IMU com giroscópios MEMS (gyro) e acelerômetros;
- **lógica de controle** — PID tunado, Kalman filter, ou modelos mais sofisticados;
- **atuação coerente** — válvulas servo (fins), freio de cardan ou motor (gyro);
- **calibração** — a cada instalação, e re-calibração após mudanças estruturais ou de carga;
- **leitura correta do estado da embarcação** — carga, atitude, velocidade, ondas.

Em estabilização ativa, software, sensores e hidráulica/mecânica importam tanto quanto a potência.

**Firmware como parte do produto:** fabricantes liberam atualizações periódicas de algoritmo; barco antigo com firmware desatualizado rende menos que novo com firmware atual.

## Relação com outros sistemas de atitude

É importante não confundir:

- [[Flap]], que corrige atitude e pode influenciar dinâmica mas não é estabilização ativa de rolagem;
- [[Motor de Trim - Tilt]], que altera o ângulo do propulsor;
- [[Thruster]], que auxilia manobra lateral (não estabiliza em navegação);
- **Estabilizador**, que ataca rolagem e comportamento dinâmico específico em navegação e/ou fundeio.

## Falhas mais comuns

### Em fins

- degradação de servo-válvula por contaminação;
- vazamento de cilindro/atuador angular;
- perda de calibração do sensor de posição da aleta;
- bomba hidráulica desgastada (pressão não alcança);
- contaminação do fluido (água, partícula, oxidação);
- falha de acumulador hidropneumático (pré-carga perdida).

### Em giroscópio

- desgaste/falha de rolamento do volante (ponto crítico);
- inversor do motor com defeito;
- falha da bomba de refrigeração (volante superaquece);
- falha de sensor inercial (perda de função);
- desbalanceamento do volante (após impacto ou falha de rolamento);
- vazamento no sistema de glicol/água.

### Genéricas

- indisponibilidade por falta de energia adequada;
- erro de sensor ou calibração;
- expectativa operacional incompatível com a tecnologia instalada;
- falha de comunicação entre IMU e CPU (cabo, NMEA 2000, CAN);
- atualização de firmware mal-sucedida.

## Diagnóstico profissional

Perguntas essenciais:

1. O sistema está recebendo energia e comando adequados (medir tensão AC no sistema durante operação)?
2. Os sensores estão coerentes (comparar leitura de IMU com outros sensores do barco)?
3. O comportamento ruim decorre de falha ou de limitação normal da tecnologia (velocidade abaixo da mínima, mar além do envelope)?
4. O problema é mecânico, hidráulico, elétrico ou de controle?
5. Qual é o histórico de manutenção e atualização de firmware?
6. Em fins: o fluido está limpo, nível correto, sem emulsão?
7. Em gyro: warm-up está em tempo normal? Ruído de rolamento é característico?

Ensaios úteis:

- revisar alarmes e status do sistema via interface do fabricante;
- validar alimentação elétrica e proteção sob carga real;
- verificar condições de operação em que o problema ocorre;
- comparar resposta dinâmica com o modo/configuração ativa;
- inspecionar atuadores e elementos mecânicos conforme a tecnologia;
- em sistemas com log interno: exportar dados para análise de fabricante.

## Boas práticas

- tratar estabilização como sistema integrado ao projeto do barco;
- alinhar expectativa do operador com a tecnologia instalada;
- manter rotina de inspeção elétrica, mecânica e de controle (semestral em uso intenso);
- documentar modos de uso, limitações e procedimentos de partida/parada;
- seguir manual do fabricante para fluido, filtro e intervalos de manutenção;
- atualizar firmware conforme releases do fabricante;
- registrar horas de operação do volante (gyro) e de bomba (fins) para manutenção preditiva.

## Erros comuns

- confundir estabilização de movimento com correção de trim;
- superestimar o que o sistema pode fazer em qualquer condição;
- ignorar dependência energética (instalar gyro sem ajustar gerador/banco);
- reduzir diagnóstico a "mecânica" e esquecer sensores e controle;
- usar o termo `estabilizador` de forma ambígua (risco editorial);
- usar fluido hidráulico errado em fins (HLP genérico em sistema que pede HVLP);
- ignorar warm-up do gyro (sistema operado frio = desgaste acelerado).

## Normas aplicáveis

### 1. Padrão elétrico e de instalação (ABYC/ISO)

- **ABYC A-16** — Electrical Safety;
- **ABYC E-11** — AC and DC Electrical Systems on Boats;
- **ABYC E-13** — Lithium-Ion Batteries (se banco LFP suportar gyro);
- **ABYC H-3** — Bonding de apêndices submersos (aletas);
- **ABYC P-24** — Electric Propulsion Systems (integração com sistemas elétricos maiores);
- **ISO 10133:2017** — Extra-low-voltage DC installations;
- **ISO 13297:2020** — AC installations;
- **ISO 16315:2016** — Electric propulsion system;
- **ISO 19665:2021** — Fin stabilizer appendages;
- **ISO 12215** — Hull construction and scantlings (reforço estrutural).

### 2. Hidráulica e fluidos (fins)

- **ISO 3448:1992** — Viscosity classification (VG 46);
- **ISO 11158:2023** — Hydraulic fluids Family H;
- **ISO 6743-4:2015** — Classification (HVLP);
- **ISO 4406:2021** — Fluid contamination coding;
- **DIN 51524 Part 3** — HVLP minimum requirements;
- **NBR 11213:2020** — Óleos hidráulicos (Brasil).

### 3. Segurança funcional e de máquinas

- **IEC 61508:2010** — Functional safety (lógica de controle);
- **CE Machinery Directive 2006/42/EC** (embarcações UE);
- **EN ISO 12100:2010** — Safety of machinery;
- **EN ISO 13849-1:2015** — Safety-related parts of control systems.

### 4. Certificação comercial e conforto

- **IMO MSC.137(76)** — Standards for ship manoeuvrability;
- **SOLAS II-1** — Construction — Subdivision and stability;
- **DNV-GL Ship Rules Pt.6 Ch.5** — Passenger comfort;
- **Lloyd's Register LR-PCR** — Passenger Comfort Rating;
- **ABS Guide for Passenger Comfort on Ships**.

### 5. Proteção ambiental e ignição

- **IEC 60529:2013** — IP Code;
- **ISO 8846:1990** — Protection against ignition;
- **UL 1500** — Ignition-Protected Marine Products;
- **SAE J1171** — Marine Ignition Protection.

### 6. Brasil (Marinha/ABNT)

- **NORMAM-01/DPC** — Embarcações em mar aberto;
- **NORMAM-03/DPC** — Embarcações em navegação interior;
- **NORMAM-05/DPC** — Homologação de material de salvatagem (referência);
- **NBR 11213:2020** — Óleos hidráulicos;
- **NBR 14134:2015** — Lubrificantes — Terminologia.

### Tabela comparativa por jurisdição

| Aspecto | EUA (ABYC) | Internacional (ISO/IEC/IMO) | Europa (EN/CE) | Brasil (Marinha/ABNT) |
|---|---|---|---|---|
| Instalação elétrica | ABYC E-11, A-16 | ISO 13297 | CE 2006/42/EC | NORMAM |
| Apêndices / fins | ABYC H-3 | ISO 19665, ISO 12215 | CE Machinery | NORMAM |
| Fluido hidráulico | — (OEM) | ISO 11158, ISO 4406 | DIN 51524 | NBR 11213 |
| Segurança funcional | — (ABYC indireto) | IEC 61508 | EN ISO 13849 | — |
| Conforto passageiros | ABS Guide | IMO, DNV-GL, LR-PCR | — | NORMAM (embarcações profissionais) |

## Glossário rápido

- **Estabilizador** — sistema que reduz rolagem (e em alguns casos, pitch/heave) da embarcação.
- **Aleta / Fin** — apêndice hidrodinâmico submerso; gera força quando gira.
- **Giroscópio estabilizador** — volante rotativo em cardan que gera momento restaurador.
- **Seakeeper** — fabricante dominante de giroscópio marine recreacional.
- **ABT-TRAC** — fabricante tradicional de fins hidráulicos marine.
- **NAIAD Dynamics** — fabricante de fins e Ride Control.
- **Quantum Marine** — fabricante com linha Zero Speed (fins rotativos em fundeio).
- **CMC Marine** — fabricante italiano de fins eletromecânicos e hidráulicos.
- **Mitsubishi ARG / TOHMEI** — fabricantes japoneses de giroscópios.
- **Anti-roll tank** — tanque parcialmente preenchido que gera momento restaurador passivo ou ativo.
- **Zero Speed fin** — aleta rotativa que funciona parada (NAIAD, Quantum).
- **Ride Control** — sistema que combina estabilização de rolagem com correção de atitude.
- **IMU (Inertial Measurement Unit)** — sensor com acelerômetros + giroscópios MEMS.
- **MEMS** — Micro-Electro-Mechanical Systems; tecnologia de sensores miniaturizados.
- **PID** — Proportional-Integral-Derivative; lei de controle padrão.
- **Kalman filter** — algoritmo de fusão sensorial.
- **CPU de controle** — unidade processadora do estabilizador.
- **Firmware** — software embarcado; fabricante libera atualizações que melhoram desempenho.
- **Servo-válvula** — válvula proporcional de alta precisão; sensível a contaminação.
- **Torque motor (atuador angular)** — atuador rotativo hidráulico que gira a aleta.
- **Acumulador hidropneumático** — reservatório pressurizado que armazena energia/amortece picos.
- **Volante (flywheel)** — massa rotativa do giroscópio; ferro ou tungstênio.
- **Cardan (gimbal)** — suporte articulado que permite inclinação do eixo do volante.
- **Precessão** — mudança de orientação do eixo do volante quando torque é aplicado.
- **Momento angular** — produto do momento de inércia pela velocidade angular; reserva de estabilização.
- **Warm-up** — período para volante atingir RPM nominal (30-45 min em Seakeeper).
- **Rolamento do volante** — ponto de manutenção crítica em giroscópio; falha é grave.
- **Refrigeração a glicol-água** — em giroscópio, trocador remove calor do motor/rolamentos.
- **Inversor do motor** — conversor AC-AC que varia frequência do motor do volante.
- **ISO VG 46** — viscosidade 46 cSt @ 40°C; padrão em fins.
- **HVLP** — óleo hidráulico com VI alto (> 140); mantém viscosidade em faixa térmica.
- **ISO 4406 17/15/12** — classe de limpeza típica de sistemas com servo-válvulas.
- **Filtro beta ratio** — eficiência de retenção de partículas do filtro.
- **Respiro com desumidificante** — respiro com sílica/gel que evita entrada de umidade.
- **PCR (Passenger Comfort Rating)** — classificação Lloyd's Register de conforto.
- **SOLAS** — Safety of Life at Sea; convenção IMO de segurança.
- **DNV-GL / Lloyd's Register / ABS** — sociedades classificadoras principais.
- **CE Machinery Directive 2006/42/EC** — diretiva UE de segurança de máquinas.
- **IEC 61508** — safety integrity level (SIL) de sistemas de controle.
- **Roll damping** — amortecimento de rolagem natural do casco (diferente de estabilização ativa).
- **Pitch / Heave / Roll / Yaw** — seis graus de liberdade do movimento do barco.
- **Anti-roll** — redução de rolagem lateral (objetivo principal de estabilizador).
- **Dead band** — faixa de insensibilidade do controlador; tuning afeta desempenho.
- **Heading hold** — auxiliar de autopilot; interage com estabilização.
- **Mar Beaufort 4-5** — envelope típico onde estabilizador marca diferença grande.
- **Mar Beaufort 7+** — além do envelope normal de conforto; estabilizador ajuda mas não anula.

## Integração com outras notas

- [[Óleos Hidráulicos Marine — Guia Completo]]
- [[Flap]]
- [[Thruster]]
- [[Motor de Trim - Tilt]]
- [[Plataforma de Popa Elétrica - Hidráulica]]
- [[Gerador (AC)]]
- [[Bancos de Bateria]]
- [[Quadro Elétrico e Painel de Distribuição AC-DC]]
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]]

## Perguntas que esta nota responde

- O que é estabilizador de movimento na embarcação?
- Como diferenciá-lo de flap, trim e thruster?
- Onde nascem as falhas de desempenho ou indisponibilidade do sistema?
- Qual fluido hidráulico usar em fins ABT/NAIAD/Quantum/CMC?
- Por que o Seakeeper pede gerador ligado permanentemente?
- Quando preferir fins versus giroscópio?
- Quais normas regulam conforto e estabilização em embarcação comercial?
