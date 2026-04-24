---
title: "Barramento DC / Bus Bar / Distribuição DC"
note_type: "component"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "BARRAMENTO DC BUS BAR DISTRIBUIÇÃO DC 33a19734f7fb8164a172ccbe349aec67.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "56"
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
  - "https://webstore.iec.ch/publication/59922"
  - "https://www.ul.com/services/ul-1059"
normas_citadas:
  - "ABYC E-11 (AC and DC Electrical Systems on Boats)"
  - "ABYC E-10 (Storage Batteries)"
  - "ABYC E-30 (Electric Propulsion Systems)"
  - "ABYC H-31 (Seacocks, Thru-Hull, Drains) — referência para separação elétrica e bonding de metais imersos"
  - "ABYC A-31 (Battery Chargers and Inverters)"
  - "ABYC TE-4 (Lightning Protection)"
  - "ISO 10133:2012 (Small craft — Electrical systems — Extra-low-voltage DC)"
  - "ISO 13297:2020 (Small craft — Electrical systems — AC installations)"
  - "ISO 8846:1990 (Small craft — Electrical devices — Protection against ignition of surrounding flammable gases)"
  - "ISO 10088:2022 (Small craft — Permanently installed fuel systems) — distância mínima a fontes de ignição"
  - "ISO 13918 (Welding — Studs and ceramic ferrules) — para barramentos soldados"
  - "IEC 60364-1 a 60364-7 (Low-voltage electrical installations)"
  - "IEC 61439-1 (Low-voltage switchgear and controlgear assemblies — Part 1: General rules)"
  - "IEC 61439-3 (Distribution boards intended to be operated by ordinary persons)"
  - "IEC 60947-1 (Low-voltage switchgear and controlgear)"
  - "IEC 60529 (Degrees of protection provided by enclosures — IP Code)"
  - "IEC 60228 (Conductors of insulated cables)"
  - "IEC 62262 (Degrees of protection against external mechanical impacts — IK Code)"
  - "IEC 61641 (Arc fault testing for assemblies)"
  - "UL 1059 (Terminal Blocks)"
  - "UL 508A (Industrial Control Panels)"
  - "UL 489 (Molded-Case Circuit Breakers)"
  - "UL 891 (Dead Front Switchboards)"
  - "NFPA 70 (National Electrical Code — NEC) artigos 555 (marinas) e 230/240 (alimentação e proteção)"
  - "NFPA 70E (Electrical Safety in the Workplace) — distância de arco e EPI"
  - "ABNT NBR 5410 (Instalações elétricas de baixa tensão)"
  - "ABNT NBR 14039 (Instalações elétricas de média tensão)"
  - "ABNT NBR IEC 61439-1/-2 (Conjuntos de manobra e controle)"
  - "ABNT NBR IEC 60529 (Graus de proteção — IP)"
  - "ABNT NBR 5419 (Proteção contra descargas atmosféricas)"
  - "NORMAM-05/DPC (Embarcações de esporte e recreio)"
  - "NORMAM-01/DPC (Embarcações empregadas na navegação em mar aberto)"
  - "USCG 33 CFR 183 Subpart I (Electrical Systems) — jurisdição EUA"
  - "DIN 43671 (Busbars made of copper — design and dimensioning)"
  - "EN 50272-2 (Safety requirements for secondary batteries and battery installations — stationary)"
family_clusters:
  - "ABYC-USCG (EUA)"
  - "ISO-IEC (internacional)"
  - "ABNT-NORMAM (Brasil)"
  - "EN-DIN (Europa)"
aliases:
  - "BARRAMENTO DC BUS BAR DISTRIBUIÇÃO DC"
  - "BARRAMENTO DC / BUS BAR / DISTRIBUIÇÃO DC"
  - "Bus bar DC"
  - "Barra de distribuição DC"
seo_title: "Barramento DC / Bus Bar / Distribuição DC"
seo_description: "BARRAMENTO DC — Elemento de distribuicao que organiza correntes, terminais e retornos do sistema DC, exigindo capacidade, protecao, isolamento e arquitetura coerente com a embarcacao."
seo_keywords:
  - "Barramento DC"
  - "Bus bar"
  - "Distribuicao DC"
  - "40 Distribuicao Protecao e Aterramento"
geo_queries:
  - "Como dimensionar barramento DC em embarcacao?"
  - "Qual a funcao do bus bar no sistema eletrico nautico?"
  - "Como posicionar o barramento negativo em relacao ao shunt?"
related_notes:
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
  - "Aterramento"
  - "Bonding — Sistema de Interligação de Massas"
  - "Cabeamento Náutico"
  - "Chaves Gerais (DC)"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Disjuntores (DC) e (AC)"
  - "Monitor de Bateria / BMV / Shunt"
---

# Barramento DC / Bus Bar / Distribuição DC

> [!abstract] Resumo técnico
> Barramento DC é o elemento de distribuição que organiza múltiplos circuitos do sistema de corrente contínua. Em embarcações, ele não é apenas uma "barra para parafusos": sua capacidade de corrente, isolamento, posição na arquitetura, proteção a montante e relação com negativos, shunts e retornos determinam robustez, manutenibilidade e segurança. ABYC E-11 (EUA) e ISO 10133 (internacional) tratam o barramento como parte inseparável do alimentador e da proteção — dimensionar a barra sem redimensionar cabo e fusível é erro crônico de projeto.

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **Dimensione a barra pela corrente real do conjunto** (não pela soma dos disjuntores), com margem ≥ 125% da corrente contínua plausível (ABYC E-11.5.4.1 / NEC 210.20).
> 2. **Proteção principal a montante é obrigatória** — fusível ou disjuntor ≤ 178 mm do polo da bateria (ABYC E-11.4.7 / ISO 10133 §6.8), dimensionado para o cabo alimentador, não para a barra.
> 3. **Shunt vem ANTES do barramento negativo** — todo retorno passa pelo shunt; retorno fora do shunt falseia monitor de bateria e leva a descarga descontrolada.
> 4. **Negativo DC ≠ bonding ≠ PE de AC** — interligação existe em pontos controlados (normalmente ponto de aterramento único da embarcação), não ao longo de qualquer barra metálica (ABYC E-11.16 / NBR 5410 §6.4).
> 5. **Torque é especificação, não intuição** — use chave de torque calibrada conforme fabricante (tipicamente 8-14 Nm para M8, 15-25 Nm para M10) e marque terminais com caneta de torque.
> 6. **Tampa isolante + IP adequado ao compartimento** — IP20 mínimo em sala de máquinas abrigada, IP44+ em cofferdam ou porão molhado (IEC 60529 / NBR IEC 60529).
> 7. **Nunca use o polo da bateria como barramento** — mais de 2-3 cabos no polo viola ABYC E-10.7 (limite de 4 conexões totais, incluindo cabo principal).
> 8. **Cobre estanhado é padrão náutico** — latão e aço níquelado são aceitáveis em corrente baixa (< 100 A); alumínio é proibido em contato direto com cobre sem isolador dielétrico.
> 9. **Reserve 25-40% de capacidade** para expansão futura e simultaneidade real; documente cada posição com tag de função e identificação do cabo.

> [!danger] Quando chamar um especialista
> Estes 9 cenários exigem engenheiro elétrico náutico, não improviso de eletricista generalista:
> 1. **Corrente contínua > 400 A no barramento principal** — entra em regime de barramento industrial (DIN 43671), com requisitos de curto-circuito, força eletromagnética e aquecimento por efeito pelicular que fogem do dimensionamento empírico de bordo.
> 2. **Sistema com inversor/carregador > 3 kW e banco Li-Fe > 200 Ah** — a corrente de curto pode ultrapassar 10.000 A; exige estudo de seletividade e fusível classe T ou CNN.
> 3. **Paralelismo de bancos de baterias em barramento comum** — requer análise de equalização, correntes de circulação e isolamento galvânico entre bancos (ABYC E-11.10).
> 4. **Retrofit de embarcação com metais mistos imersos** (aço + alumínio + bronze) — relação barramento negativo × bonding × ânodos exige projeto de proteção catódica integrado (ABYC E-2 / ISO 13174).
> 5. **Barramento em compartimento com risco de gás inflamável** (sala de baterias chumbo-ácido, compartimento de tanque de combustível) — exige componentes ignition-protected conforme ISO 8846 / UL 1500.
> 6. **Modificação da arquitetura de aterramento da embarcação** (mudar ponto de conexão negativo-casco, introduzir isolador galvânico, adicionar ILG/isolador de loop de terra) — mexer em um barramento sem redesenhar a arquitetura corrompe toda a referência de massa.
> 7. **Investigação de corrosão galvânica ou eletrólise recorrente** — pode indicar corrente de fuga pelo casco via barramento negativo incorretamente posicionado.
> 8. **Certificação CE/RCD ou inspeção DPC/USCG** — requer conformidade documental com ISO 10133/13297 (UE) ou ABYC/USCG 33 CFR 183 (EUA), com memorial de cálculo e dossiê técnico.
> 9. **Arco elétrico durante operação ou sinais de fusão em terminal** — suspeita de arc flash: desligue imediatamente, isole o sistema e acione especialista; NFPA 70E exige análise de risco de arco para sistemas > 50 V com energia > 1 kW.

## O que é

Barramento DC é um condutor coletivo, normalmente metálico, usado para concentrar conexões de um mesmo potencial elétrico. Em instalações náuticas aparecem, em geral:

- barramentos positivos de distribuição;
- barramentos negativos de retorno;
- barramentos dedicados por subsistema (navegação, iluminação, tração, eletrônica);
- módulos com proteção integrada (fuse blocks e power distribution modules).

O barramento reduz improviso no polo da bateria, melhora organização, facilita expansão e diagnóstico, e é o ponto físico onde arquitetura elétrica, proteção, monitoramento e manutenção se encontram.

## Função na embarcação

- distribuir energia DC para vários circuitos de forma ordenada;
- concentrar retornos negativos respeitando a topologia do shunt e do bonding;
- criar pontos claros de medição, teste e manutenção;
- sustentar arquitetura modular de proteção e expansão;
- permitir separação lógica entre bancos, cargas e subsistemas (house × engine × thruster × eletrônica).

## Fundamentos mínimos

### Capacidade de corrente não depende só do metal

A capacidade real do barramento depende de:

- seção condutiva (mm² ou área equivalente);
- material e acabamento (cobre estanhado > cobre nu > latão > aço níquelado);
- temperatura ambiente (cada +10°C reduz ~8% da ampacidade);
- ventilação e proximidade de outras fontes de calor;
- tipo de borne e área efetiva de contato;
- corrente contínua e simultaneidade real (não a soma das placas).

### Proteção não está "no barramento"

O barramento não substitui proteção. O circuito precisa ter:

- proteção principal a montante (fusível ou disjuntor) dimensionada para o cabo alimentador, com corte ≤ 178 mm (7 polegadas) do polo da bateria (ABYC E-11.4.7) — ou ≤ 100 mm se o cabo passar por anteparo condutivo;
- proteção individual dos ramais, quando aplicável;
- coordenação de seletividade entre proteção principal e ramais (curva e capacidade de interrupção adequadas à Icc presumida).

### Barramento negativo não é licença para misturar tudo

Negativo DC, PE de AC, bonding e referência de instrumentação têm relações próprias na arquitetura da embarcação. Em alguns sistemas existe interligação controlada em um ponto único (normalmente próximo ao alternador ou ao quadro principal); em outros, há separação deliberada. Tratar qualquer barra metálica como "terra universal" é erro conceitual que produz:

- ruído em sondas, GPS e sistemas NMEA;
- corrosão galvânica acelerada;
- corrente de fuga em marina (com risco a nadadores — ESD, electric shock drowning);
- falseamento do monitor de bateria.

### O shunt muda a topologia do negativo

Quando houver monitor de bateria por shunt (BMV-712, SmartShunt, Balmar SG200 etc.), a posição do barramento negativo precisa respeitar o caminho de medição: **todo retorno da carga passa pelo shunt**, e o shunt fica entre o barramento negativo (lado "Load/Battery monitor") e o polo negativo da bateria. Retornos ligados do lado errado (direto ao polo da bateria, saltando o shunt) falseiam corrente, consumo, estado do banco e algoritmos de SoC.

## Tipos e arquiteturas comuns

### Barramento simples

- barra condutiva com múltiplos pontos de conexão (parafusos roscados M5–M12);
- útil para retorno negativo ou distribuição simples em até ~200 A;
- exige disciplina de proteção nos ramais externos;
- exemplos: Blue Sea 2300/2301/2302, Victron Busbar 250/600/1000A, Lenco/Littelfuse busbar strips.

### Barramento com proteção integrada (fuse block / power distribution module)

- combina distribuição e fusíveis/disjuntores em um mesmo módulo;
- melhora organização em sistemas compactos;
- não elimina necessidade de proteção principal do alimentador;
- exemplos: Blue Sea 5025/5026/5028 (ST Blade), Blue Sea SafetyHub 150, Victron Lynx Distributor, Mastervolt MasterBus PowerModule.

### Barramento modular de alta corrente

- usado em bancos, inversores, carregadores e sistemas mais densos (> 250 A contínuos);
- permite módulos dedicados para distribuição, fusíveis classe T/ANL/MRBF e medição;
- exemplos: Victron Lynx Power In / Lynx Shunt / Lynx Distributor, Mastervolt DC Distribution 500A, Blue Sea PowerBar 1000.

### Barramento de anteparo (through-bulkhead)

- atravessa anteparo estanque com isolação e vedação classificada;
- usado em divisão de compartimentos (sala de baterias × sala de máquinas × casco);
- exige bucha passante dielétrica e torque controlado em ambos os lados.

## Dimensionamento — tabela de referência por corrente

| Corrente contínua (A) | Material/seção típica | Torque M10 (Nm) | Classe proteção montante | Exemplos de fabricante |
| --- | --- | --- | --- | --- |
| ≤ 100 | Cobre estanhado 15×3 mm (~45 mm²) | 8–12 | MIDI/MEGA/ANL 125 A | Blue Sea 2300, Victron 150A |
| 100–250 | Cobre estanhado 20×5 mm (~100 mm²) | 10–14 | ANL/MRBF/Classe T 300 A | Blue Sea 2301, Victron 250A, Lynx Distributor |
| 250–500 | Cobre estanhado 30×6 mm (~180 mm²) | 15–20 | Classe T 400–600 A | Victron 600A, Mastervolt 500A |
| 500–1000 | Cobre estanhado 40×8 mm (~320 mm²) | 20–30 | Classe T/CNN 800–1200 A | Victron 1000A, Blue Sea PowerBar 1000 |
| > 1000 | Cobre com reforço térmico, projeto customizado | conforme projeto | Classe T/CNN + análise seletividade | projeto dedicado (DIN 43671) |

Valores indicativos; sempre consultar datasheet e regra de margem ≥ 125% da corrente contínua plausível.

## Projeto e instalação

### O que precisa ser definido

1. corrente contínua plausível do conjunto (não soma dos disjuntores);
2. corrente de curto presumida (Icc) e proteção a montante com capacidade de interrupção adequada;
3. quantidade real de ramais e reserva de expansão (25–40%);
4. ambiente de instalação (temperatura, umidade, vibração, risco de gás);
5. necessidade de tampa, isolamento e segregação física;
6. posição relativa a bateria, chave geral, shunt e proteção principal;
7. material e acabamento (cobre estanhado é padrão);
8. regime de torque e marcação visual.

### Diretrizes práticas

- evitar usar o borne da bateria como "barramento improvisado" (ABYC E-10.7 limita 4 conexões por polo);
- instalar o barramento em local seco, acessível e protegido, com IP compatível com o compartimento;
- usar módulo e terminais compatíveis com a corrente real do sistema;
- identificar entradas e saídas por função (ex.: "+24V HOUSE", "NEG SHUNT LOAD", "BONDING");
- manter caminho elétrico coerente entre banco, proteção, chave, barramento e carga;
- usar cabo alimentador com seção ≥ 125% da maior corrente contínua esperada;
- torquear com chave calibrada conforme fabricante (nunca "no aperto");
- marcar terminal com caneta de torque após aperto final para evidenciar afrouxamento futuro;
- aplicar graxa dielétrica ou spray de proteção marinho em conexões expostas a salinidade;
- não misturar metais diferentes em contato direto (cobre × alumínio sem isolador = corrosão galvânica garantida).

## Onde costuma dar problema

| Problema | Causa provável | Correção |
| --- | --- | --- |
| aquecimento anormal | subdimensionamento, mau aperto ou área de contato ruim | redimensionar, re-torquear com chave calibrada, substituir terminais corroídos |
| queda de tensão localizada | conexão degradada ou excesso de corrente | medir queda sob carga; se > 100 mV em trecho curto, investigar aperto/área |
| corrosão recorrente | ambiente agressivo, materiais inadequados ou proteção ruim | trocar para cobre estanhado, aplicar graxa dielétrica, melhorar IP/ventilação |
| leitura errada do monitor de bateria | retorno ligado do lado errado do shunt | refazer topologia: tudo passa pelo shunt antes do polo negativo |
| crescimento desordenado do sistema | falta de reserva e de documentação | instalar barramento com 30% de reserva; manter diagrama unifilar atualizado |
| arco ou fusão de terminal | alta Icc + proteção inadequada ou contato frouxo | estudo de seletividade; trocar para fusível classe T com Icc suficiente |
| ruído em eletrônica ao ligar cargas pesadas | negativo de sinais misturado com negativo de potência | segregar barra de sinal da barra de potência; ponto único de união |

## Diagnóstico prático

1. **Medir queda de tensão** de um extremo ao outro sob carga máxima (multímetro em milivolt, DC).
2. **Verificar aperto** com chave de torque calibrada em cada terminal; procurar oxidação e integridade.
3. **Inspeção visual** e, quando disponível, **termografia** — hotspot > 20°C acima do ambiente indica problema.
4. **Confirmar topologia do shunt**: todo retorno de carga deve passar pelo shunt antes do polo negativo.
5. **Validar proteção a montante**: fusível/disjuntor compatível com cabo alimentador e com Icc presumida.
6. **Testar continuidade de bonding** entre negativo DC e ponto de aterramento único da embarcação (resistência < 0,1 Ω).
7. **Verificar isolação** entre barramento e casco condutivo (> 1 MΩ com megôhmetro 500 V DC, em embarcações com sistema DC isolado).

## Boas práticas profissionais

- dimensionar com margem coerente para expansão e simultaneidade (25–40%);
- proteger contra contato acidental e queda de ferramenta metálica (tampa com parafuso cativo);
- usar materiais e acabamento compatíveis com ambiente marinho (cobre estanhado, inox A4 nas fixações);
- documentar função e destino de cada ponto relevante (tag + diagrama unifilar);
- revisar aperto e condição superficial como parte da manutenção periódica (anual ou 500 h);
- separar barramentos por função quando a arquitetura exigir clareza e governança (house/engine/eletrônica);
- manter registro de torque e de data da última inspeção em etiqueta próxima ao barramento;
- em refits, fotografar antes de desconectar — a topologia de retorno do shunt é frequentemente perdida.

## Erros comuns

- concentrar múltiplos cabos grandes no polo da bateria em vez de usar barramento (viola ABYC E-10.7);
- tratar negativo DC, bonding e PE como se fossem a mesma barra sem critério;
- esquecer que o barramento precisa de proteção principal a montante (ABYC E-11.4.7: ≤ 178 mm do polo);
- crescer o sistema sem rever capacidade, ventilação e identificação;
- passar retorno fora do shunt e depois culpar o monitor de bateria;
- usar parafuso M6 e terminal anel para 250 A (área de contato insuficiente → aquecimento);
- misturar cobre e alumínio sem isolador dielétrico (corrosão galvânica);
- instalar barramento positivo sem tampa em compartimento acessível (risco de curto por ferramenta);
- usar latão (Cu + Zn) em ambiente marinho de alta salinidade sem estanhar (dezincificação).

## Relação com outros sistemas

- **[[Quadro Elétrico e Painel de Distribuição AC-DC]]** — organização dos circuitos derivados.
- **[[Cabeamento Náutico]]** — alimentadores e ramais do barramento.
- **[[Fusíveis DC — Proteção Contra Sobrecorrente]]** e **[[Disjuntores (DC) e (AC)]]** — coordenação de proteção.
- **[[Aterramento]]** e **[[Bonding — Sistema de Interligação de Massas]]** — relação arquitetural entre referências e massas.
- **[[Monitor de Bateria / BMV / Shunt]]** — posição correta do barramento negativo em sistemas monitorados.
- **[[Chaves Gerais (DC)]]** — sequência chave → proteção → barramento → carga.
- **[[Terminais Conectores e Emendas]]** — interface física entre cabo e barramento.

## Normas e referências

### Por família e jurisdição

| Família | Norma | Escopo |
| --- | --- | --- |
| **ABYC (EUA)** | E-11 §4.7, §5.4, §16 | proteção a montante, dimensionamento, bonding |
| ABYC | E-10 §7 | limite de conexões no polo da bateria |
| ABYC | E-30 | sistemas de propulsão elétrica (barramentos de alta corrente) |
| ABYC | A-31 | carregadores e inversores (barramento DC downstream) |
| **ISO (internacional)** | ISO 10133:2012 | sistemas DC em embarcações pequenas |
| ISO | ISO 13297:2020 | sistemas AC em embarcações pequenas |
| ISO | ISO 8846:1990 | proteção contra ignição em atmosfera inflamável |
| **IEC (internacional/Europa)** | IEC 60364-1 a -7 | instalações elétricas de baixa tensão |
| IEC | IEC 61439-1/-3 | conjuntos de manobra e controle (quadros) |
| IEC | IEC 60529 | graus de proteção (IP) |
| IEC | IEC 61641 | teste de arco interno em conjuntos |
| **UL (EUA)** | UL 1059 | terminal blocks |
| UL | UL 508A | painéis de controle industriais |
| **NFPA (EUA)** | NFPA 70 art. 555 | marinas e instalações flutuantes |
| NFPA | NFPA 70E | segurança elétrica no trabalho (arc flash) |
| **USCG (EUA)** | 33 CFR 183 Subpart I | sistemas elétricos em embarcações de recreio |
| **ABNT (Brasil)** | NBR 5410 | instalações elétricas de baixa tensão |
| ABNT | NBR IEC 61439-1/-2 | conjuntos de manobra e controle |
| ABNT | NBR IEC 60529 | graus de proteção (IP) — adoção nacional |
| ABNT | NBR 5419 | proteção contra descargas atmosféricas |
| **NORMAM (Brasil)** | NORMAM-05/DPC | embarcações de esporte e recreio |
| NORMAM | NORMAM-01/DPC | embarcações em navegação marítima |
| **DIN/EN (Europa)** | DIN 43671 | barramentos de cobre — projeto e dimensionamento |
| EN | EN 50272-2 | segurança em instalações de baterias estacionárias |

### Comparação prática entre jurisdições

- **EUA (ABYC + USCG)**: foco em distâncias máximas (≤ 178 mm do polo até a proteção), limite de 4 conexões por polo, regras prescritivas de cabeamento.
- **Internacional (ISO/IEC)**: abordagem baseada em desempenho (ISO 10133 exige proteção sem prescrever distância rígida); IEC 61439 trata o conjunto como sistema.
- **Brasil (ABNT + NORMAM)**: NBR 5410 não cobre especificidades náuticas; NORMAM-05 remete a ABYC/ISO para recreio e adota SOLAS/IEC para comercial.
- **Europa (EN/DIN)**: DIN 43671 é referência técnica para barramentos industriais (> 400 A); EN 50272-2 trata bancos estacionários.

## Glossário rápido

1. **Ampacidade** — corrente máxima contínua que um condutor ou barramento suporta sem exceder limite térmico.
2. **Arc flash** — descarga elétrica violenta por ionização do ar em curto-circuito; NFPA 70E exige análise para sistemas > 50 V e energia > 1 kW.
3. **Arco** — condução elétrica através de gás ionizado; em DC é mais perigoso que AC por não ter zero natural de corrente.
4. **Barra coletiva** — condutor que reúne múltiplas conexões de mesmo potencial.
5. **Barramento neutro** — barra de referência zero em sistema AC (não confundir com negativo DC).
6. **Bolt-on** — conexão por parafuso (terminal anel + porca).
7. **Bonding** — interligação de massas metálicas para igualar potencial e controlar corrosão galvânica (ABYC E-11.16).
8. **Borne** — ponto físico de conexão.
9. **Bucha passante** — isolador dielétrico que permite travessia de condutor através de anteparo condutivo.
10. **Capacidade de interrupção (Icn/Icu)** — maior corrente de curto que um disjuntor pode abrir com segurança.
11. **Classe T (fusível)** — fusível de alta capacidade de interrupção (20 kA+), padrão para bancos Li-Fe.
12. **Cobre estanhado** — cobre com camada de estanho que resiste à corrosão marinha.
13. **Coeficiente de temperatura** — variação de resistência com a temperatura (cobre ~0,4%/°C).
14. **Condutividade** — inverso da resistividade; cobre puro ~5,8×10⁷ S/m.
15. **Contato elétrico** — área efetiva de aperto entre dois condutores.
16. **Corrente contínua (DC)** — corrente de sentido único, usada em sistemas de bateria.
17. **Corrosão galvânica** — degradação de metal em contato com outro metal em meio eletrolítico.
18. **Densidade de corrente** — corrente por área de seção (A/mm²); em barramento típico 2–4 A/mm².
19. **Diagrama unifilar** — representação esquemática de um sistema elétrico com cada fase/polo representado por uma linha única.
20. **Dielétrico** — material isolante que suporta campo elétrico sem conduzir.
21. **ESD (electric shock drowning)** — afogamento por choque elétrico em marina por corrente de fuga no meio aquático.
22. **Fusível MRBF (Marine Rated Battery Fuse)** — fusível montado diretamente no polo da bateria; típico 30–300 A.
23. **Fusível ANL** — fusível limitador para alta corrente; típico 80–750 A.
24. **Fusível MIDI/MEGA** — fusível limitador de médio/alto calibre (30–500 A).
25. **Ground (terra)** — em AC, condutor de proteção (PE); em DC, depende da arquitetura.
26. **IP (Ingress Protection)** — código IEC 60529 de proteção contra pó (1º dígito) e água (2º dígito).
27. **IK** — código IEC 62262 de proteção contra impacto mecânico.
28. **Icc (corrente de curto-circuito presumida)** — maior corrente que o sistema pode entregar em curto franco.
29. **Isolador galvânico** — dispositivo que bloqueia corrente DC no PE entre embarcação e marina, preservando proteção AC.
30. **Lug** — terminal anel para bolt-on.
31. **Megôhmetro** — instrumento que mede resistência de isolação em DC (tipicamente 500 V ou 1000 V).
32. **Negativo comum** — ponto único onde negativos de cargas se encontram.
33. **NFPA 70E** — norma americana de segurança elétrica ocupacional; define EPI e distâncias de arco.
34. **Ponto único de aterramento** — nó único onde se unem negativo DC, bonding e PE (quando aplicável na arquitetura).
35. **Power distribution module (PDM)** — módulo integrado de distribuição + proteção.
36. **Queda de tensão (ΔV)** — diferença de tensão entre dois pontos sob carga; limite prático < 3% em DC.
37. **Retorno** — caminho elétrico do negativo da carga até o polo negativo da bateria.
38. **Seletividade** — coordenação entre proteções para que apenas a proteção mais próxima do defeito atue.
39. **Shunt** — resistor calibrado de baixa resistência usado para medir corrente.
40. **Simultaneidade** — fator que estima quantas cargas operam ao mesmo tempo.
41. **SoC (State of Charge)** — estado de carga do banco em %.
42. **Subsistema** — agrupamento funcional (house, engine, thruster, eletrônica).
43. **Tap-off** — derivação a partir de um barramento.
44. **Terminal anel (ring terminal)** — terminal fechado para bolt-on.
45. **Torque** — momento de aperto aplicado a parafuso (N·m).
46. **Tripping curve** — curva tempo × corrente de atuação de disjuntor.
47. **UL 1059** — norma americana para terminal blocks.
48. **USCG 33 CFR 183** — regulamento federal americano para sistemas elétricos em embarcações de recreio.
49. **Via de curto** — caminho elétrico entre fontes de corrente em condição de falta.
50. **Zona de arco (arc flash boundary)** — distância mínima em que um operador sofreria queimadura de 2º grau; NFPA 70E.

## FAQ

**Posso ligar todos os consumidores diretamente no polo da bateria?**

Fisicamente possível em sistemas muito pequenos (até ~3 cargas leves), mas não é a prática profissional. ABYC E-10.7 limita o polo da bateria a 4 conexões totais (incluindo o cabo principal). Barramento melhora organização, manutenção e segurança, e é obrigatório em sistemas médios e grandes.

**Barramento negativo é sempre o mesmo ponto do bonding?**

Não como regra universal. A relação entre negativo DC, bonding e PE depende da arquitetura adotada (negativo isolado do casco × negativo aterrado). Deve ser tratada explicitamente em projeto e documentada no diagrama unifilar. ABYC E-11.16 recomenda ponto único de união, quando aplicável.

**Se há espaço para mais um cabo, posso adicionar mais uma carga?**

Só depois de verificar: corrente total do sistema, proteção a montante, seção do cabo alimentador, aquecimento atual do barramento e reserva funcional do sistema. Adicionar sem recalcular é a causa #1 de falha por subdimensionamento progressivo.

**Posso usar barramento de latão em ambiente marinho?**

Latão funciona em baixa corrente (< 100 A) em ambiente seco (sala de instrumentos). Em ambiente de alta salinidade (casaria, cofferdam), o zinco do latão sofre dezincificação — use cobre estanhado.

**Qual o torque correto em parafuso M10 de barramento?**

Varia por fabricante e material. Para cobre com porca em latão/inox, tipicamente 15–20 N·m. Sempre consulte o datasheet; use chave de torque calibrada; marque com caneta de torque após aperto.

**Preciso de estudo de arc flash para meu barramento de 500 A?**

Em embarcação de recreio sob ABYC/USCG, não é mandatório, mas recomendável. Em embarcação comercial sob SOLAS/classificadora ou ambiente industrial (marina, estaleiro) sob NFPA 70E, sim — sistemas > 50 V com energia de arco > 1 kW exigem análise.

## Visual didático

![Barramento DC: distribuicao e protecao](../_visuals/generated/barramento-dc-distribuicao-protecao.svg)

Mostrar barramento como ponto organizado de distribuicao, nao como lugar para empilhar cabos no borne da bateria.

**Cautela:** Corrente nominal, material, isolacao, torque e protecao dependem de projeto e fabricante.

Material de apoio: [Barramento DC: distribuicao e protecao](../_visuals/generated/barramento-dc-distribuicao-protecao.md)

## Integração com outras notas

- [[Quadro Elétrico e Painel de Distribuição AC-DC]]
- [[Aterramento]]
- [[Bonding — Sistema de Interligação de Massas]]
- [[Cabeamento Náutico]]
- [[Chaves Gerais (DC)]]
- [[Fusíveis DC — Proteção Contra Sobrecorrente]]
- [[Disjuntores (DC) e (AC)]]
- [[Monitor de Bateria / BMV / Shunt]]
- [[Terminais Conectores e Emendas]]

## Perguntas que esta nota responde

- O que é barramento DC em instalações elétricas náuticas?
- Como posicionar e dimensionar um bus bar com critério técnico?
- Quais erros de arquitetura e manutenção aparecem em barramentos de bordo?
- Como a ABYC, ISO, IEC e NBR tratam o barramento DC?
- Quando é necessário estudo de arc flash em sistema DC de embarcação?
