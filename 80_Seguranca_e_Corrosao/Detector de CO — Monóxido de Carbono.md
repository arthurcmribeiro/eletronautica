---
title: "Detector de CO — Monóxido de Carbono"
note_type: "technical-note"
domain: "80_Seguranca_e_Corrosao"
source_file: "DETECTOR DE CO — MONÓXIDO DE CARBONO 33a19734f7fb8179a514c1c8f11fd5f3.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "35"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
  - "internacional"
normas_citadas:
  - "ABYC A-24 (2022) — Carbon Monoxide Detection Systems"
  - "ABYC A-1 — Marine Liquefied Petroleum Gas (LPG) Systems"
  - "ABYC A-25 — Gasoline Fuel Systems"
  - "ABYC P-1 — Installation of Exhaust Systems for Propulsion and Auxiliary Engines"
  - "ABYC H-2 — Ventilation of Boats Using Gasoline"
  - "ABYC H-33 — Diesel Fuel Systems"
  - "ABYC E-11 (2023) — AC & DC Electrical Systems on Boats (alimentação do detector)"
  - "ISO 12133:2011 — Small craft — Carbon monoxide (CO) detection systems"
  - "ISO 10240 — Small craft — Owner's manual (exige instruções sobre CO)"
  - "UL 2034 — Single and Multiple Station Carbon Monoxide Alarms (referência residencial)"
  - "UL 2075 — Gas and Vapor Detectors and Sensors (comercial/industrial)"
  - "UL 1524 — Marine Alarm Systems"
  - "EN 50291-1 — Electrical apparatus for the detection of CO (domestic premises)"
  - "EN 50291-2 — Electrical apparatus for the detection of CO (caravans, boats)"
  - "NFPA 72 — National Fire Alarm and Signaling Code (absorveu NFPA 720/2019)"
  - "NFPA 302 — Fire Protection Standard for Pleasure and Commercial Motor Craft"
  - "USCG 33 CFR Part 183 — Boats and Associated Equipment"
  - "USCG Navigation and Vessel Inspection Circular NVIC 10-92 — Carbon Monoxide"
  - "USCG Boating Safety Circular — CO awareness campaign"
  - "OSHA 29 CFR 1910.1000 — Air Contaminants (TWA 50 ppm para CO)"
  - "ACGIH TLV — 25 ppm TWA (mais conservador)"
  - "WHO Guidelines — 9 ppm (8h em ambiente ocupado)"
  - "NORMAM-211/DPC — Esporte e recreio"
  - "NORMAM-201/204/DPC — Comercial / SMM"
  - "NBR 14008 — Detectores de gás (referência industrial)"
  - "CE-RCD Directive 2013/53/EU — Recreational Craft Directive"
review_level: "engineering-curated"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "DETECTOR DE CO — MONÓXIDO DE CARBONO"
seo_title: "Detector de CO — Monóxido de Carbono"
seo_description: "DETECTOR DE CO — Alarme marinho para monoxido de carbono, gas toxico gerado por combustao, com foco em cenarios de acumulacao, instalacao correta e resposta imediata a alarme."
seo_keywords:
  - "Detector de CO"
  - "Monoxido de carbono"
  - "Seguranca a bordo"
  - "80 Seguranca e Corrosao"
geo_queries:
  - "Como instalar detector de CO em embarcacao?"
  - "Quais sao os riscos de monoxido de carbono em barcos?"
related_notes:
  - "Detector de Gás GLP / GN"
  - "Sistema de Alarme Geral / Painel de Alarmes"
  - "Extintor Automático — Combate a Incêndio na Casa de Máquinas"
  - "CAIS (Pier) (AC)"
  - "Aquecedor de Bordo - Cabin Heater"
  - "Gerador (AC)"
---

# Detector de CO — Monóxido de Carbono

> [!abstract] Resumo técnico
> Detector de CO é um alarme destinado a avisar a presença de monóxido de carbono em níveis perigosos dentro de áreas ocupáveis da embarcação. CO é gás tóxico, invisível e inodoro, associado a motores, geradores, aquecedores, fogões e outras fontes de combustão. Em barcos, o risco existe tanto em cabine quanto em áreas externas sujeitas a recirculação de exaustão.

> [!tip] Regra de decisão em 30 segundos
> 1. **CO é inodoro, incolor e incapacitante** — humano NÃO sente antes da intoxicação; só detector eletroquímico calibrado protege. Sintoma inicial confunde com enjoo/cansaço/ressaca.
> 2. **Zona crítica = onde se dorme** — cabine, beliche, área de descanso; instalar na altura da cabeça (CO tem densidade próxima ao ar, 0,97); NÃO no teto como detector de fumaça.
> 3. **Detector marinho ABYC A-24 ou ISO 12133, NÃO residencial UL 2034** — residencial doméstico não resiste a vibração, umidade salina, choque mecânico; certificação EN 50291-2 (caravans/boats) é o mínimo em Europa.
> 4. **Detector de fumaça ≠ detector de CO ≠ detector de GLP** — sensores, posicionamento e resposta completamente diferentes; não economizar comprando um que "faz tudo" sem certificação específica.
> 5. **Teste funcional mensal + substituir sensor 5-7 anos** — sensor eletroquímico degrada com o tempo mesmo sem disparos; end-of-life signal no beep periódico; detector "funcional" aos 10 anos é falso positivo de segurança.
> 6. **Alarme = emergência imediata** — evacuar para ar livre, desligar motor/gerador/aquecedor, ventilar, atender sintomáticos; NUNCA "reset + continuar" sem investigar.
> 7. **Fontes principais: gerador, motor, aquecedor catalítico, fogão GLP, cabin heater diesel** — station wagon effect em popa aberta + vento de popa + barco parado (marcha lenta ou fundeado) concentra CO em área de banho/cockpit.
> 8. **ABYC A-24 exige detector em cada cabine/espaço de sono + espaço adjacente à fonte de combustão** — não adianta "um único detector no salão" em embarcação com múltiplos compartimentos fechados.
> 9. **NORMAM-211 não detalha CO; ABYC A-24 + ISO 12133 são a referência técnica** — sucata de certificação em charter/aluguel vira responsabilidade civil; USCG NVIC 10-92 + boating safety awareness cobrem educação.

> [!danger] Quando chamar emergência / especialista
> 1. **Pessoas sintomáticas a bordo (dor de cabeça, náusea, tontura, confusão, sonolência anormal)** — EMERGÊNCIA MÉDICA: evacuar para ar livre, oxigênio 100% se disponível, SAMU/Marinha; COHb (carboxihemoglobina) sanguínea precisa ser medida; câmara hiperbárica se COHb > 25%.
> 2. **Alarme de CO enquanto gerador/motor/aquecedor ligado** — desligar TUDO + ventilação máxima + todos fora da cabine; não usar o barco até inspecionar sistema de exaustão por profissional com analisador de gás de combustão (CO/CO₂/O₂).
> 3. **Múltiplas pessoas com sintomas simultâneos** — resgate prioritário; nunca entrar em área suspeita sem SCBA (Self-Contained Breathing Apparatus); casos fatais documentados de resgatadores.
> 4. **Gerador diesel novo, modificado ou com exaustão reencaminhada sem inspeção profissional** — risco de vazamento pelo coletor, mangote, silenciador; ABYC P-1 define requisitos de estanqueidade; analisador de combustão + teste fumaça.
> 5. **Substituição de aquecedor catalítico ou cabin heater (Webasto/Espar/Wallas) sem revisão de duto de exaustão** — retrofit mal feito causou mortes documentadas; instalador certificado + teste CO pós-instalação obrigatório.
> 6. **Motor a gasolina em marcha lenta > 30 min com popa aberta ou em fundeio** — station wagon effect garantido; CO acumula em cockpit; risco alto para passageiros em área de banho/plataforma; desligar ou mover.
> 7. **Charter, aluguel, escola náutica ou operação comercial sem detector de CO certificado e testado** — responsabilidade civil + penal em caso de acidente; NORMAM-201 exige equipamento de segurança mínimo; ABYC A-24 para vistoria voluntária.
> 8. **Sinistro com morte ou internação suspeita de CO** — preservar embarcação como evidência (não ligar motor/gerador), chamar perícia IML + perícia técnica com analisador; histórico COHb > 10% em não-fumante = CO; laudo IBAPE / Abracem.
> 9. **Perícia pós quase-acidente ou histórico de sintomas recorrentes** — inspeção completa de exaustão + ventilação + detectores; analisador contínuo por 24h em cenário de uso normal; relatório baseline para seguro + revenda.

## O que é

É um dispositivo de alarme, normalmente com sensor eletroquímico ou tecnologia equivalente, projetado para detectar CO em ambientes ocupáveis. O objetivo não é medir qualidade do ar com precisão laboratorial, e sim:

- alertar exposição perigosa;
- induzir resposta imediata da tripulação;
- reduzir risco de intoxicação durante repouso, permanência em cabine ou operação.

## Função na embarcação

- detectar CO gerado por fontes de combustão;
- avisar a tripulação antes de incapacidade ou intoxicação grave;
- complementar ventilação, manutenção e inspeção de exaustão;
- apoiar uma cultura de segurança em embarcações com espaços ocupáveis.

## Fundamentos mínimos

### CO não tem cheiro e pode se confundir com "mal-estar"

Fontes oficiais de segurança náutica alertam que sintomas de CO podem se parecer com enjoo, cansaço ou intoxicação alcoólica. Isso atrasa a reação e torna o detector ainda mais importante.

### O risco existe dentro e fora da cabine

CO pode se acumular em interiores, sob coberturas, próximo à popa, em áreas de plataforma e em cenários de recirculação de exaustão. A guarda costeira dos EUA destaca o chamado *station wagon effect* ou *back drafting*, especialmente em baixa velocidade, marcha lenta, embarcação parada e proximidade de outras embarcações.

### Detector não substitui manutenção de exaustão

Alarme é camada de proteção, não licença para operar com motor, gerador, aquecedor ou escape em condição duvidosa.

### Detector marinho não deve ser tratado como acessório doméstico genérico

Em ambiente náutico, vibração, umidade e disponibilidade de alimentação importam. O conjunto precisa ser compatível com a aplicação e mantido conforme instruções do fabricante.

## Projeto e instalação

### O que precisa ser definido

1. quais espaços são ocupáveis e onde as pessoas dormem;
2. quais fontes de combustão existem a bordo;
3. como a exaustão pode recircular em condição real de uso;
4. se o detector será alimentado por bateria própria, alimentação DC ou sistema integrado;
5. política de teste, substituição e resposta ao alarme.

### Diretrizes práticas

- instalar alarme marinho ou solução explicitamente adequada ao ambiente da embarcação;
- posicionar os alarmes em ou próximo dos espaços ocupáveis e de pernoite, conforme instrução do fabricante;
- não instalar no bilge só porque "é onde ficam os gases", pois CO não se comporta como GLP;
- evitar pontos de ventilação direta ou locais que descaracterizem a amostragem do ambiente;
- manter alimentação coerente com a função de segurança do equipamento.

## Onde costuma dar problema

| Problema | Causa provável |
| --- | --- |
| alarme ausente em barco com fonte de combustão | subestimação do risco |
| detector vencido ou ignorado | falta de manutenção e de cultura de segurança |
| alarme "falso" recorrente | exaustão real, produto inadequado ou instalação ruim |
| alarme fora de posição útil | instalação em ponto inadequado |
| risco persistente apesar do detector | vazamento de exaustão, ventilação ruim ou operação insegura |

## Diagnóstico prático

1. Confirmar data de substituição e integridade do equipamento.
2. Executar teste funcional pelo método previsto pelo fabricante.
3. Inspecionar o sistema de exaustão e as fontes de combustão.
4. Verificar cenários reais de recirculação de gases.
5. Confirmar que a tripulação sabe como responder ao alarme.

## Resposta ao alarme

- levar pessoas imediatamente para ar fresco;
- desligar fontes de combustão quando isso puder ser feito com segurança;
- ventilar a embarcação;
- tratar sintomas como emergência médica;
- não "resetar e seguir" sem investigar a causa.

## Boas práticas profissionais

- usar detector adequado ao ambiente marinho;
- testar regularmente conforme o fabricante;
- substituir o alarme ou sensor dentro do prazo recomendado;
- incorporar inspeção de exaustão, mangotes e ventilação à rotina técnica;
- instruir tripulação e passageiros sobre sintomas e resposta.

## Erros comuns

- achar que diesel ou gerador "não precisam" de preocupação com CO;
- instalar detector de fumaça achando que substitui detector de CO;
- ignorar alarme porque "ninguém sentiu cheiro";
- montar detector em local sem relação com a zona ocupada;
- usar detector vencido como se fosse proteção válida.

## Relação com outros sistemas

- **[[Aquecedor de Bordo - Cabin Heater]]** e **[[Gerador (AC)]]** — fontes potenciais de CO.
- **[[Sistema de Alarme Geral / Painel de Alarmes]]** — integração de aviso centralizado.
- **[[Extintor Automático — Combate a Incêndio na Casa de Máquinas]]** — segurança em espaços técnicos, mas com risco diferente.
- **[[Detector de Gás GLP / GN]]** — gás diferente, risco diferente e estratégia de instalação diferente.

## Normas e referências

- U.S. Coast Guard Boating Safety — material educativo e checklists sobre CO em embarcações;
- documentação do fabricante do detector;
- requisitos aplicáveis de certificação e instalação do equipamento utilizado.

## Normas aplicáveis (organizadas por família)

CO em embarcação é regulado em três camadas: **detector propriamente dito** (ABYC, ISO, UL, EN), **fonte de CO** (ABYC exaustão, ventilação, combustíveis), **infraestrutura de resposta** (NFPA, USCG, NORMAM).

### ABYC (American Boat & Yacht Council) — referência técnica primária

- **ABYC A-24 (2022) — Carbon Monoxide Detection Systems** — a norma central: define onde instalar (cada cabine de sono + espaços adjacentes a fontes de combustão), tipo de sensor, certificação UL/EN, teste, vida útil, sinal de end-of-life, alimentação redundante.
- **ABYC A-1 — Marine Liquefied Petroleum Gas (LPG) Systems** — fogão e aquecedor a GLP são fonte secundária de CO; exigências de ventilação cruzam com A-24.
- **ABYC A-25 — Gasoline Fuel Systems** — motor a gasolina é a fonte #1 de CO (diesel produz menos); exige ventilação mecânica conforme H-2.
- **ABYC P-1 — Installation of Exhaust Systems for Propulsion and Auxiliary Engines** — estanqueidade do escape; vazamento no coletor/mangote/silenciador é a causa raiz de muitos acidentes.
- **ABYC H-2 — Ventilation of Boats Using Gasoline** — ventilação natural + mecânica obrigatórias; blower antes de dar partida; requisito de fluxo cfm.
- **ABYC H-33 — Diesel Fuel Systems** — diesel gera menos CO que gasolina mas ainda gera; exaustão mal encaminhada é risco.
- **ABYC E-11 (2023) — AC & DC Electrical Systems on Boats** — alimentação do detector deve ser circuito dedicado, sempre energizado (não passar por chave geral), conforme A-24.

### ISO (pequena embarcação internacional)

- **ISO 12133:2011 — Small craft — Carbon monoxide (CO) detection systems** — equivalente internacional de ABYC A-24; exigências de posicionamento, teste, certificação.
- **ISO 10240 — Small craft — Owner's manual** — manual do proprietário deve incluir instruções sobre CO, sintomas, resposta ao alarme.

### UL (certificação USA do detector)

- **UL 2034 — Single and Multiple Station Carbon Monoxide Alarms** — certificação residencial (residência fixa); é referência para o sensor, não para o ambiente marinho.
- **UL 2075 — Gas and Vapor Detectors and Sensors** — certificação comercial/industrial; mais robusto que UL 2034.
- **UL 1524 — Marine Alarm Systems** — sistema de alarme marinho integrado (combina CO + gás + smoke + bilge + etc.).

### EN (Europa)

- **EN 50291-1 — Electrical apparatus for the detection of CO (domestic premises)** — certificação residencial.
- **EN 50291-2 — Electrical apparatus for the detection of CO (caravans, boats)** — certificação específica para ambiente móvel (vibração, umidade, faixa térmica). É o equivalente europeu de ABYC A-24.

### NFPA (segurança contra incêndio)

- **NFPA 72 — National Fire Alarm and Signaling Code** — absorveu NFPA 720 (retirada em 2019); cobre integração de alarmes de CO em sistema geral.
- **NFPA 302 — Fire Protection Standard for Pleasure and Commercial Motor Craft** — exigências de detecção e combate a incêndio em embarcação recreativa e comercial; detector de CO parte do conjunto.

### USCG (autoridade marítima USA)

- **USCG 33 CFR Part 183 — Boats and Associated Equipment** — regulamento federal; define equipamento obrigatório.
- **USCG Navigation and Vessel Inspection Circular NVIC 10-92 — Carbon Monoxide** — circular técnica sobre CO em embarcações; referência histórica e educativa.
- **USCG Boating Safety Circular** — campanhas de conscientização periódicas; material educativo oficial.

### Higiene industrial (limites de exposição)

- **OSHA 29 CFR 1910.1000 — Air Contaminants** — limite legal USA: CO TWA 50 ppm (8 horas), Ceiling 200 ppm.
- **ACGIH TLV — 25 ppm TWA** — limite recomendado pela Associação Americana de Higienistas Industriais; mais conservador que OSHA.
- **WHO Guidelines — 9 ppm (8h em edifício ocupado)** — limite sanitário OMS; base de guidelines residenciais em vários países.
- **ABYC A-24 — limiar de alarme:** deve disparar entre 70 ppm (60-240 min) e 400 ppm (4-15 min); níveis calibrados para proteger população em repouso/sono.

### Brasil

- **NORMAM-211/DPC — Esporte e recreio** — não detalha detector de CO especificamente, mas exige sistema de segurança adequado; inspeção por agente da capitania.
- **NORMAM-201/204/DPC — Comercial / SMM** — embarcação classificada segue sociedade classificadora (DNV, BV, RINA, LR, ABS) que adota ISO 12133 ou equivalente.
- **NBR 14008 — Detectores de gás** — referência industrial brasileira; aplica-se mais a detector de gases combustíveis (GLP/GN), mas conceitos de calibração/teste se estendem.

### Europa (RCD)

- **CE-RCD Directive 2013/53/EU — Recreational Craft Directive** — embarcação certificada CE com espaço ocupável fechado e fonte de combustão deve ter detector CO conforme EN 50291-2.

### Como usar este conjunto normativo na prática

| Situação | Norma-chave |
|---|---|
| Projeto novo, recreio USA | ABYC A-24 + UL 2034/2075 + certificação EN 50291-2 |
| Retrofit detector em barco existente | ABYC A-24 posicionamento + marine-grade UL 1524 |
| Embarcação comercial classificada | ISO 12133 + sociedade classificadora |
| Embarcação CE (Europa) | EN 50291-2 + RCD |
| Charter / aluguel Brasil | NORMAM-211 + ABYC A-24 (melhor prática) + inspeção anual |
| Investigação pós-acidente | NVIC 10-92 + IBAPE + analisador combustão |
| Sistema integrado multi-alarme | UL 1524 + NFPA 72 |
| Ventilação preventiva gasolina | ABYC A-25 + H-2 (blower) |
| Exaustão estanque | ABYC P-1 + teste fumaça |

## Glossário rápido

### Gás e fisiologia

- **CO (monóxido de carbono)** — CO, gás inodoro, incolor, densidade 0,97 (próxima ao ar; NÃO sobe como H₂ nem desce como GLP); produto de combustão incompleta de hidrocarboneto (gasolina, diesel, GLP, madeira).
- **CO₂ (dióxido de carbono)** — CO₂, gás da respiração normal; NÃO é o mesmo; detector de CO não detecta CO₂ e vice-versa; confundir é erro grave.
- **COHb (carboxihemoglobina)** — CO ligado à hemoglobina no sangue; afinidade 240× maior que O₂; bloqueia transporte de oxigênio; medido em % do total de hemoglobina.
- **Hipóxia** — baixa oxigenação dos tecidos; primeiro efeito do CO; confusão, sonolência, perda de coordenação.
- **Anóxia** — ausência total de oxigenação; estágio letal.
- **Antídoto: oxigênio 100%** — O₂ hiperbárico acelera dissociação CO-hemoglobina; tempo de meia-vida do COHb cai de 5h (ar ambiente) para 1h (O₂ 100%) e 20 min (hiperbárico).
- **Câmara hiperbárica** — tratamento padrão para COHb > 25% ou sintomas graves; centros no Brasil: Hospital Universitário USP, Hospital Naval.

### Unidades e limites

- **ppm (partes por milhão)** — unidade de concentração atmosférica de CO; 1 ppm = 1 cm³ de CO por m³ de ar.
- **TWA (Time-Weighted Average)** — limite de exposição média ao longo de 8 horas (turno de trabalho).
- **STEL (Short-Term Exposure Limit)** — limite de exposição média em 15 minutos; mais alto que TWA.
- **Ceiling** — limite máximo instantâneo; nunca exceder.
- **30 ppm** — limite WHO 24h; percebido como "ar fresco, tudo bem".
- **50 ppm** — OSHA TWA 8h.
- **70 ppm** — ABYC A-24 limite de alarme em 60–240 min.
- **150 ppm** — ABYC A-24 limite de alarme em 10–50 min; começa dor de cabeça em pessoa saudável.
- **400 ppm** — ABYC A-24 limite de alarme em 4–15 min; dor de cabeça severa em 1–2h; risco de morte em 2–3h.
- **800 ppm** — dor de cabeça + náusea + tontura em 45 min; morte em 2–3h.
- **1600 ppm** — dor de cabeça grave em 20 min; morte em 1h.
- **6400 ppm** — morte em 10–15 min.
- **12800 ppm** — morte em < 3 min.

### Tipos de sensor

- **Detector eletroquímico** — tecnologia padrão para CO; célula com eletrólito oxida CO e gera corrente proporcional; seletivo, preciso, mas vida útil 5–7 anos.
- **Detector MOS (Metal-Oxide Semiconductor)** — sensor SnO₂ aquecido; muda resistência com CO; mais barato mas sujeito a cross-sensitivity com H₂, álcool, solventes.
- **Detector IR (Infrared)** — absorção em 4,6 μm; caro; usado em monitoramento industrial contínuo; não típico em embarcação recreativa.
- **Cross-sensitivity** — sensibilidade cruzada a outros gases; MOS sensibiliza a GLP, álcool, solventes → alarme falso.

### Fenômenos de acúmulo náutico

- **Station wagon effect** — acúmulo de CO na popa aberta quando vento é de popa para proa; barco parado ou em marcha lenta; cabin van é o equivalente automotivo.
- **Back drafting** — exaustão recircula pela tomada de ar da cabine; típico em embarcação fechada com gerador externo.
- **Exhaust recirculation** — genérico para qualquer caminho de retorno de exaustão.
- **Indian file / lineup effect** — vários barcos fundeados próximos, exaustão de um entra no outro; comum em marinas lotadas.

### Categorias de detector

- **Residencial (UL 2034 / EN 50291-1)** — certificado para casa/apartamento; NÃO resiste a vibração, umidade salina, choque.
- **Marinho (ABYC A-24 / ISO 12133 / EN 50291-2 / UL 1524)** — certificado para ambiente marinho; obrigatório em embarcação.
- **RV / Caravan (EN 50291-2)** — certificação compartilhada com marinho na Europa; ambiente móvel.
- **Combo alarm** — detector combinado (CO + fumaça + gás); verificar certificação de cada função separadamente; não comprar "3 em 1" sem certificação tripla.

### Alimentação e vida útil

- **Hardwired** — alimentado pelo sistema DC da embarcação; recomendado em ABYC A-24; circuito dedicado sempre energizado.
- **Battery-only** — alimentação por pilha/bateria própria; mais flexível mas exige troca e teste rigorosos.
- **Bateria 10 anos (sealed Li)** — bateria selada de lítio com vida útil = vida útil do sensor; substituir unidade inteira.
- **Bateria 9V alcalina** — bateria substituível; tempo médio 6–12 meses; exige disciplina de troca.
- **End-of-Life signal** — beep periódico (ex: 1× a cada 30 s) quando sensor atinge fim de vida; substituir imediatamente.
- **Vida útil sensor: 5–7 anos (UL 2034 antigo: 5; UL 2034 novo: 7; ABYC A-24: segue fabricante)** — depois disso, leitura errática.

### Funcionalidades

- **Hush button / silencing** — botão de silêncio temporário após teste ou falso alarme; 10 min típico; não desliga proteção.
- **Interconnected alarms** — múltiplos detectores ligados em rede; quando um dispara, todos disparam; obrigatório em embarcação com múltiplas cabines.
- **Peak memory** — memória de concentração máxima detectada; útil para diagnóstico pós-evento.
- **Digital display** — leitura numérica em ppm; mais diagnóstico, especialmente em investigação.

### Fontes típicas em embarcação

- **Motor a gasolina (stern drive, outboard, inboard)** — maior produtor de CO; gasolina rica em combustão incompleta.
- **Motor diesel** — produz menos CO que gasolina (combustão mais completa), mas ainda produz; NÃO é "seguro".
- **Gerador marinho (Onan, Kohler, Northern Lights, Fischer Panda, Mase)** — fonte principal em fundeio; pode ser diesel ou gasolina.
- **Aquecedor catalítico (Mr. Heater, Catalytic Heater)** — propano/butano; alta produção de CO se mal ventilado.
- **Cabin heater diesel (Webasto, Espar/Eberspächer, Wallas)** — duto de exaustão separado; se mal instalado/manutenido, vaza CO em cabine.
- **Aquecedor de água a gás (instant water heater)** — idem cabin heater; exige exaustão dedicada.
- **Fogão GLP / forno / churrasqueira** — em uso prolongado com pouca ventilação, acumula CO.

### Análise pós-evento

- **Analisador de combustão** — instrumento portátil que mede CO, CO₂, O₂, NOx na exaustão; diagnóstico de motor/gerador.
- **Analisador de ambiente (CO meter)** — leitura direta de CO em ppm no ar; uso em investigação de vazamento.
- **Teste fumaça** — gerador de fumaça não-tóxica injetado na exaustão; revela vazamentos visualmente.
- **Monitor contínuo 24h** — datalogger de CO instalado por técnica para mapear padrão em cenário de uso.

### Sigla e padrão

- **SCBA (Self-Contained Breathing Apparatus)** — equipamento autônomo de respiração; obrigatório para resgate em ambiente com CO suspeito.
- **NVIC 10-92** — USCG Navigation and Vessel Inspection Circular sobre CO; referência histórica.
- **ABYC A-24** — padrão técnico americano de detecção de CO em recreio.
- **ISO 12133** — padrão internacional de detecção de CO em small craft.
- **EN 50291-2** — padrão europeu para detector CO em caravan/boat.

## FAQ

**CO é problema só em cabine fechada?**

Não. Pode haver risco também em cockpit coberto, popa, plataforma e áreas de recirculação de exaustão.

**Detector de fumaça substitui detector de CO?**

Não. São dispositivos de finalidade diferente.

**Se o alarme disparou e depois parou, posso ignorar?**

Não. O evento precisa ser tratado como indício de condição insegura até que a causa seja entendida.

## Visual didático

![Detectores de CO e gas: riscos diferentes](../_visuals/generated/detectores-co-gas-camadas.svg)

Mostrar que CO e gas combustivel exigem sensores, posicionamento e resposta diferentes.

**Cautela:** Instalacao, vida util e posicionamento dos sensores devem seguir manual do fabricante e boas praticas de seguranca.

Material de apoio: [Detectores de CO e gas: riscos diferentes](../_visuals/generated/detectores-co-gas-camadas.md)

## Integração com outras notas

- [[Detector de Gás GLP / GN]]
- [[Sistema de Alarme Geral / Painel de Alarmes]]
- [[Extintor Automático — Combate a Incêndio na Casa de Máquinas]]
- [[Aquecedor de Bordo - Cabin Heater]]
- [[Gerador (AC)]]

## Perguntas que esta nota responde

- Por que detector de CO é crítico em embarcações?
- Onde estão os cenários reais de acúmulo de monóxido de carbono no barco?
- Como instalar e operar detector de CO com seriedade técnica?
