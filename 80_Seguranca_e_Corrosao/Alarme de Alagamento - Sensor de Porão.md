---
title: "Alarme de Alagamento / Sensor de Porão"
note_type: "technical-note"
domain: "80_Seguranca_e_Corrosao"
source_file: "ALARME DE ALAGAMENTO SENSOR DE PORÃO 33a19734f7fb81d2ba97e64f015d6859.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "38"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
  - "internacional"
normas_citadas:
  - "ABYC H-22 (2021) — Electric Bilge Pump Systems (base para sensor e alarme)"
  - "ABYC H-23 — Design, Construction and Compliance of Recreational Vessels (cross-ref)"
  - "ABYC A-16 — Electric Navigation Lights (referência para circuito sempre-energizado)"
  - "ABYC A-24 — Carbon Monoxide Detection Systems (integração de alarmes)"
  - "ABYC E-11 (2023) — AC & DC Electrical Systems (alimentação + proteção)"
  - "ABYC T-12 — Telemetry and data systems (monitoramento remoto)"
  - "ISO 15083:2020 — Small craft — Bilge pumping systems"
  - "ISO 11812 — Small craft — Watertight cockpits and quick-draining cockpits"
  - "ISO 9093 — Small craft — Seacocks and through-hull fittings"
  - "ISO 12215 — Small craft — Hull construction and scantlings"
  - "SOLAS Chapter II-1 Regulation 35-1 — Bilge pumping arrangements"
  - "SOLAS Chapter II-1 Regulation 22-1 — Internal watertight integrity (flooding detection)"
  - "USCG 33 CFR Part 183 — Boats and Associated Equipment"
  - "USCG 46 CFR Subchapter K / Subchapter T — Small Passenger Vessels"
  - "USCG 46 CFR 182 — Uninspected Vessels (bilge systems)"
  - "NFPA 72 — National Fire Alarm and Signaling Code (integração)"
  - "UL 1500 — Ignition Protection Test for Marine Products"
  - "UL 1524 — Marine Alarm Systems"
  - "IEC 61162-3 / NMEA 2000 — Maritime navigation and radiocommunication equipment — digital interfaces"
  - "NMEA 2000 PGN 130310 — Environmental Parameters"
  - "NMEA 2000 PGN 130311 — Temperature Extended Range"
  - "DNV Rules Pt 4 Ch 6 — Piping systems (bilge)"
  - "Lloyd's Register Rules for Ships Pt 5 — Piping systems"
  - "NBR 17240 — Sistemas de detecção e alarme de incêndio (referência cruzada)"
  - "NORMAM-211/DPC — Esporte e recreio"
  - "NORMAM-201/204/DPC — Comercial / SMM"
  - "CE-RCD Directive 2013/53/EU — Recreational Craft Directive"
review_level: "engineering-curated"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "ALARME DE ALAGAMENTO SENSOR DE PORÃO"
  - "ALARME DE ALAGAMENTO / SENSOR DE PORÃO"
seo_title: "Alarme de Alagamento / Sensor de Porão"
seo_description: "ALARME DE ALAGAMENTO — Sistema de alto nivel de agua no porao que complementa a bomba de bilge, exige sensor independente, alimentacao nao seccionada e aviso perceptivel ao operador."
seo_keywords:
  - "Alarme de alagamento"
  - "High water alarm"
  - "Sensor de porao"
  - "Bilge alarm"
  - "80 Seguranca e Corrosao"
geo_queries:
  - "Como instalar alarme de alagamento em embarcacao?"
  - "Qual a diferenca entre bomba de porao e alarme de alto nivel?"
related_notes:
  - "Bomba de Porão"
  - "Sistema de Alarme Geral / Painel de Alarmes"
  - "Monitoramento Remoto — VRM / Telemetria"
  - "Sensor de Nível de Água"
  - "Hotline (DC)"
---

# Alarme de Alagamento / Sensor de Porão

> [!abstract] Resumo técnico
> Alarme de alagamento, ou high water alarm, é o sistema que avisa quando o nível de água no porão ultrapassa a condição normal de bombeamento. Ele não substitui a bomba de porão: atua como camada de alerta e diagnóstico para inundação progressiva, falha da bomba ou entrada anormal de água.

> [!tip] Regra de decisão em 30 segundos
> 1. **Alarme ≠ bomba — funções SEPARADAS com sensores INDEPENDENTES** — alarme detecta FALHA da bomba, não é seu gatilho. Usar o mesmo float para ambos = ponto único de falha.
> 2. **Sensor de alarme ACIMA do nível de partida da bomba** — diferença típica 10–15 cm; alarme dispara somente quando bomba não vence, não quando está trabalhando normalmente.
> 3. **Alimentação NÃO seccionada pela chave geral (always-on / hotline DC)** — ABYC H-22 + E-11; circuito permanentemente energizado com fusível dedicado + bateria dedicada (ou sempre-flutuando no house bank).
> 4. **Três nós obrigatórios: sensor + lógica + indicação** — sensor no porão, módulo com bateria de backup, buzzer + LED no posto de comando; painel de comando é inútil se não é ouvido/visto.
> 5. **Múltiplos compartimentos = múltiplos sensores** — ABYC H-22 + ISO 15083; casa de máquinas, poço de cada compartimento estanque, lazarette, proa; cada zona de flutuação tem sua detecção.
> 6. **Float switch mecânico > capacitivo/ultrassônico em água suja** — óleo, combustível, detritos, algas: sensor ótico/capacitivo falso-positivo; mecânico robusto mas requer limpeza do pivô.
> 7. **Teste mensal: levantar manualmente float + confirmar buzzer + LED + piscar remoto** — ABYC H-22 7.5 + NBR 17240; registrar data; sistema sem teste documentado é sistema sem valor.
> 8. **Integração NMEA 2000 (PGN 130310/130311) + SMS/email = camada remota complementar** — VRM Victron, Siren Marine, GOST, BRNKL; NÃO substitui alarme local, apenas adiciona resiliência fora do barco.
> 9. **Backup de bateria dedicado (9V alcalina, Li-ion 18650 ou AGM 7 Ah) com float charger** — se bateria principal falha (curto, incêndio, vandalismo), alarme sobrevive 24–72 h; bateria datada + trocada.

> [!danger] Emergência imediata / quando chamar especialista
> 1. **Barco afundando com alarme disparado (nível sobe visivelmente)** — MAYDAY no VHF canal 16 + posição GPS + natureza; coletes salva-vidas em todos; localizar fonte de vazamento (hull, eixo, seacock, stuffing box); bomba manual reserva (Whale Gusher, Edson); evacuação para vaso/liferaft se não controlar em 5 min.
> 2. **Alarme dispara em marina/atracadouro sem ninguém a bordo** — vizinho + marina + deslocar imediatamente; pode ser furo ativo, rachadura de casco, seacock rompido; NÃO ligar equipamento elétrico até inspeção (risco fogo + choque em água).
> 3. **Alarme dispara em navegação longa** — desligar autopilot + volta ao rumo manual + todos coletes; capitão inspeciona compartimentos em ordem (popa primeiro em lancha planadora); fechar seacocks desnecessários; localizar + estancar + bombear.
> 4. **Bomba principal falhou + alarme disparado** — ativar bomba reserva elétrica + bomba manual; se ambas falham, bombeamento via balde ou desviar bomba de água do motor (emergência extrema); VHF para auxílio.
> 5. **Alarme alto-nível vence sozinho o bombeamento (nível sobe apesar da bomba)** — taxa de entrada > capacidade de bomba; buscar porto/abrigo mais próximo + bomba de apoio externa; análise pós-acidente de estanqueidade.
> 6. **Alarme mudo ou bateria fraca encontrado em inspeção rotineira** — sistema sem valor real; reinstalar com alimentação independente + bateria nova + teste funcional antes da próxima operação; risco de afundamento silencioso.
> 7. **Retrofit de hull (seacock novo, thru-hull, janela, dogleg de eixo) sem revisar sensores alto-nível** — novo ponto de risco potencialmente sem cobertura; adicionar sensor na zona afetada.
> 8. **Charter, aluguel ou escola náutica sem alarme alto-nível funcional e documentado** — responsabilidade civil em caso de submersão; NORMAM-201 + ISO 15083 + inspeção periódica com laudo.
> 9. **Perícia pós-submersão / sinistro com alagamento** — preservar: bateria do alarme (data), sensor (posição original), cabeamento, módulo, data log NMEA 2000 se disponível; laudo IBAPE + seguradora; base para responsabilização do estaleiro/marina/manutenção.

## O que é

É um sistema composto por:

- sensor ou chave de alto nível;
- lógica de alarme;
- aviso sonoro e/ou visual;
- eventualmente integração com monitoramento remoto.

Seu papel é detectar condição anormal de água, não apenas ligar a bomba.

## Função na embarcação

- alertar subida anormal do nível de água;
- indicar que a bomba não está vencendo a entrada de água ou falhou;
- permitir ação rápida da tripulação;
- complementar a bomba automática e o monitoramento do barco.

## Fundamentos mínimos

### Bomba de porão e alarme são funções diferentes

- bomba: remove água;
- alarme: informa condição anormal.

Se ambos dependem do mesmo sensor ou da mesma lógica, perde-se independência funcional.

### Alarme de alto nível pede sensor independente

A arquitetura mais robusta usa sensor dedicado de alarme acima do nível normal de acionamento da bomba automática, para indicar anomalia e não operação rotineira.

### Alimentação precisa continuar disponível

Alarme de alto nível perde grande parte do valor se fica morto quando a chave principal é desligada. A estratégia de alimentação deve refletir a função de segurança do sistema.

### Um único compartimento pode não bastar

Embarcações com múltiplos espaços sujeitos a inundação podem precisar de mais de um sensor, conforme a compartimentação e os pontos de risco.

## Projeto e instalação

### O que precisa ser definido

1. quais espaços estão sujeitos a alagamento;
2. qual o nível normal de partida da bomba;
3. qual o nível de alarme desejado;
4. onde o operador verá e ouvirá o aviso;
5. se haverá notificação remota;
6. como o circuito será alimentado e protegido.

### Diretrizes práticas

- instalar sensor de alarme independente e acima do nível de trabalho normal da bomba;
- posicionar o aviso em ponto perceptível ao operador;
- manter a fiação fora da água e protegida mecanicamente;
- prever teste periódico simples e claro;
- documentar a lógica do sistema e as zonas atendidas.

## Onde costuma dar problema

| Problema | Causa provável |
| --- | --- |
| alarme não dispara | sensor travado, circuito sem alimentação adequada ou instalação errada |
| alarme falso recorrente | sensor mal posicionado, detritos, turbulência ou contaminação |
| alarme soa mas ninguém percebe | buzzer fraco, ausência de indicação no ponto de operação |
| bomba atua e ninguém sabe | ausência de alarme ou de indicador de bomba em operação |
| compartimento crítico sem cobertura | projeto incompleto da compartimentação |

## Diagnóstico prático

1. Confirmar que o sistema permanece energizado conforme a arquitetura definida.
2. Testar o sensor de alarme de forma controlada.
3. Verificar diferença de nível entre acionamento da bomba e acionamento do alarme.
4. Inspecionar estado do sensor, do chicote e do módulo de alarme.
5. Confirmar que o aviso chega ao posto de comando ou área ocupada relevante.

## Boas práticas profissionais

- usar sensor independente para o alarme de alto nível;
- alimentar por circuito não seccionado quando a função exigir vigilância contínua;
- prever alarme visual e sonoro perceptíveis;
- adicionar monitoramento remoto apenas como complemento, não substituto do alarme local;
- testar periodicamente bomba, sensor de bomba e sensor de alto nível separadamente.

## Erros comuns

- chamar bomba automática de "alarme";
- usar o mesmo sensor da bomba como único elemento de detecção;
- alimentar o sistema de modo que ele fique morto com o barco parado;
- instalar aviso quase inaudível ou escondido;
- ignorar compartimentos secundários propensos a entrada de água.

## Relação com outros sistemas

- **[[Bomba de Porão]]** — sistema complementar, com função diferente.
- **[[Sistema de Alarme Geral / Painel de Alarmes]]** — centralização do aviso.
- **[[Monitoramento Remoto — VRM / Telemetria]]** — camada remota complementar.
- **[[Sensor de Nível de Água]]** — comparação entre medição de tanque e detecção de inundação.
- **[[Hotline (DC)]]** — lógica de circuito permanentemente disponível, quando aplicável.

## Normas e referências

- requisitos aplicáveis da embarcação para bilge systems e high water alarm;
- documentação do sensor e do módulo de alarme;
- boas práticas de alimentação, proteção e teste periódico do sistema.

## Normas aplicáveis (organizadas por família)

High water alarm cruza quatro áreas normativas: **sistema de porão recreativo** (ABYC H-22, ISO 15083), **subdivisão e estanqueidade comercial** (SOLAS II-1), **integração elétrica e alarme** (ABYC E-11, NFPA 72, UL 1524), **monitoramento remoto** (NMEA 2000 / IEC 61162-3).

### ABYC (recreio USA)

- **ABYC H-22 (2021) — Electric Bilge Pump Systems** — norma central: exige sensor independente para alarme alto-nível, alimentação sempre-ligada, teste funcional, documentação.
- **ABYC H-23 — Design, Construction and Compliance of Recreational Vessels** — referência cruzada para arquitetura geral.
- **ABYC A-16 — Electric Navigation Lights** — exemplo paradigma de circuito sempre-energizado; mesmo padrão se aplica ao alarme.
- **ABYC A-24 — Carbon Monoxide Detection Systems** — modelo de integração de múltiplos alarmes em painel único.
- **ABYC E-11 (2023) — AC & DC Electrical Systems** — alimentação, proteção por fusível, seção mínima de cabo, identificação.
- **ABYC T-12 — Telemetry and Data Systems** — para integração com monitoramento remoto (VRM, Siren Marine, BRNKL, GOST).

### ISO (pequena embarcação internacional)

- **ISO 15083:2020 — Small craft — Bilge pumping systems** — equivalente internacional de ABYC H-22; exige alarme de alto nível em embarcações habitáveis > 6 m.
- **ISO 11812 — Small craft — Watertight cockpits and quick-draining cockpits** — referência de cockpit auto-drenante; complementa bilge.
- **ISO 9093 — Small craft — Seacocks and through-hull fittings** — pontos primários de risco de alagamento; detecção alto-nível é backup.
- **ISO 12215 — Small craft — Hull construction and scantlings** — estrutura; base de integridade do casco.

### IMO / SOLAS (embarcação comercial)

- **SOLAS Chapter II-1 Regulation 35-1 — Bilge pumping arrangements** — subdivisão e bombeamento em navio comercial.
- **SOLAS Chapter II-1 Regulation 22-1 — Internal watertight integrity** — integração de detecção de alagamento em passageiros.
- **IMO MSC.1/Circ.1291** — Flooding detection systems in passenger ships — detalha sensores de alto nível em cada compartimento estanque.

### USCG (USA)

- **USCG 33 CFR Part 183** — regulamento federal embarcação recreativa.
- **USCG 46 CFR Subchapter K** — embarcações de passageiros > 150 pax.
- **USCG 46 CFR Subchapter T** — charter pequeno passageiro.
- **USCG 46 CFR 182** — embarcações não-inspecionadas; referência de bilge.

### Fire/alarm integration (USA)

- **NFPA 72 — National Fire Alarm and Signaling Code** — quando alarme de porão integra ao sistema geral, NFPA 72 define protocolo de sinalização, priorização, teste.

### Certificação de componentes

- **UL 1500 — Ignition Protection Test for Marine Products** — ignição protegida para componentes em casa de máquinas.
- **UL 1524 — Marine Alarm Systems** — certificação USA de sistema de alarme marinho integrado.

### Interfaces digitais (monitoramento)

- **IEC 61162-3 / NMEA 2000** — rede CAN marítima; padrão para comunicar sensores digitais.
- **NMEA 2000 PGN 130310 — Environmental Parameters** — PGN para parâmetros ambientais (inclui água de porão em alguns dispositivos).
- **NMEA 2000 PGN 130311 — Temperature Extended Range** — útil para sensor de água/temperatura associado.
- **SignalK** — protocolo aberto para dados marinhos; bridge para NMEA 2000.

### Classificadoras (comercial)

- **DNV Rules Pt 4 Ch 6 — Piping systems (bilge)** — regras DNV para bilge comercial.
- **Lloyd's Register Rules for Ships Pt 5** — piping and bilge systems.
- **ABS Steel Vessel Rules Pt 4 Ch 6** — bilge systems.
- **Bureau Veritas NR 467 Pt C Ch 1 Sec 10** — bilge pumping.

### Brasil

- **NBR 17240 — Sistemas de detecção e alarme de incêndio** — referência cruzada; conceitos de sinalização se aplicam.
- **NORMAM-211/DPC — Esporte e recreio** — exigências de sistema de segurança.
- **NORMAM-201/204/DPC — Comercial / SMM** — comercial classificada segue sociedade classificadora.

### Europa (RCD)

- **CE-RCD Directive 2013/53/EU** — embarcação CE habitável com acomodação exige sistema de bombeamento + detecção conforme ISO 15083.

### Como usar este conjunto normativo na prática

| Situação | Norma-chave |
|---|---|
| Projeto novo recreio USA | ABYC H-22 + E-11 + UL 1524 |
| Projeto recreio Europa CE | ISO 15083 + RCD + EN ISO 15083 |
| Comercial classificada > 24m | SOLAS II-1 + classificadora (DNV Pt 4 Ch 6) |
| Charter / aluguel Brasil | NORMAM-211 + ABYC H-22 (best practice) + manutenção anual |
| Integração ao sistema de alarme geral | NFPA 72 + UL 1524 + T-12 |
| Monitoramento remoto | NMEA 2000 + SignalK + VRM/Siren/BRNKL |
| Retrofit pós-reforma hull | ISO 9093 (seacocks) + H-22 (sensor adicional) |
| Navio passageiro > 150 pax | MSC.1/Circ.1291 + SOLAS II-1 Reg 22-1 |

## Glossário rápido

### Terminologia de porão e detecção

- **High water alarm (alarme de alto nível)** — sistema de alerta que dispara quando água no porão excede nível normal de bombeamento; ABYC H-22 obrigatório em embarcação habitável.
- **Bilge** — porão; compartimento inferior do casco onde água se acumula.
- **Sump** — poço de porão; zona deprimida onde água converge.
- **Working level / nível de trabalho** — nível normal de partida da bomba automática; tipicamente 2–5 cm acima do piso.
- **Alarm level / nível de alarme** — altura onde o sensor de alarme dispara; 10–15 cm acima do working level.
- **Normal bilge** — pequena quantidade de água aceitável (condensação, spray, stuffing box); não deve disparar alarme.

### Tipos de sensor

- **Float switch mecânico** — boia com contato de mercúrio ou microswitch interno; mais robusto em água suja.
- **Reed switch (magnético)** — boia com ímã + reed switch interno; selado, sem contato direto com água.
- **Mercury switch** — boia com tubo de mercúrio; PROIBIDO em muitos mercados por ambiental (RoHS, REACH).
- **Capacitive level sensor** — sensor sem partes móveis; mede mudança capacitiva; sujeito a falso-positivo em água com óleo/combustível.
- **Ultrasonic level sensor** — eco de som; bom para tanques abertos; requer tampa com geometria.
- **Optical water detector** — detecção infravermelha refletida por superfície de água; sujeito a falso-positivo em superfície suja.
- **Conductive probe** — dois eletrodos; fecha circuito quando água conduz; falha em água muito doce ou muito suja.
- **Solid state (Gems, Dwyer)** — sem partes móveis, sensor de estado; mais caro, mais durável.

### Arquitetura do alarme

- **Sensor dedicado (independent sensor)** — sensor exclusivo do alarme, separado do sensor da bomba; arquitetura correta H-22.
- **Sensor compartilhado** — mesmo float aciona bomba + alarme; não é recomendado; único ponto de falha.
- **Módulo de lógica (control unit)** — processa sinal do sensor, aplica delay anti-ripple, aciona saídas.
- **Buzzer piezo** — sinal sonoro de alta frequência (2–4 kHz); perceptível em barco com motor.
- **LED vermelho / âmbar** — indicador visual; no posto de comando e na cabine.
- **Repeat station / repetidor** — painel secundário em segunda posição de timoneiro.
- **Silencer / mute** — botão para silenciar temporariamente sem desligar proteção.

### Alimentação

- **Always-on circuit (hotline DC)** — circuito permanentemente energizado, não passa pela chave geral; ABYC H-22.
- **Dedicated bilge battery** — bateria exclusiva do alarme; AGM 7–12 Ah típico.
- **Float charger** — carregador que mantém bateria sempre plena sem sobrecarregar.
- **Fused circuit** — fusível próprio dimensionado para corrente do alarme + buzzer + LED.
- **Backup battery (9V, 18650, AGM pequena)** — redundância interna do módulo; autonomia 24–72h.
- **Low battery warning** — aviso de bateria fraca (beep periódico); ABYC H-22 obrigatório.

### Compartimentação e zonas

- **Single zone alarm** — apenas um sensor; aceitável em embarcação pequena monohull < 25 ft.
- **Multiple zone alarm** — múltiplos sensores em diferentes compartimentos; obrigatório H-22 em embarcação habitável ou multihull.
- **Watertight bulkhead** — anteparo estanque; cada compartimento estanque exige seu sensor.
- **Zone indicator** — display que mostra qual zona disparou; útil para diagnóstico rápido.

### Integração remota (monitoramento)

- **NMEA 2000** — rede marítima CAN 250 kbps; padrão IEC 61162-3.
- **PGN 130310 / 130311** — PGNs ambientais; alguns fabricantes transmitem nível de porão aqui.
- **SignalK** — protocolo aberto; bridge para NMEA 2000 via gateways.
- **VRM (Victron Remote Management)** — plataforma Victron; alarme via email/SMS.
- **Siren Marine** — serviço comercial de monitoramento (LTE-M + Cloud).
- **GOST Global** — serviço similar (rastreamento + alarme).
- **BRNKL** — outro serviço (hub on-board + cloud).
- **Cellular gateway (LTE-M / NB-IoT)** — módem + cloud; baixo consumo.
- **Satellite gateway (Iridium, Inmarsat)** — para embarcação oceânica sem cobertura celular.
- **WiFi marina** — limitado à marina; não serve para embarcação em mar aberto.

### Falhas comuns e diagnóstico

- **Float stuck (boia travada)** — detritos, óleo, cabo torto; float não sobe ou não desce.
- **Wire chafe (cabo esfolado)** — cabo encostado em aresta; curto intermitente.
- **Corroded terminal** — terminal corroído no sensor; continuidade ruim.
- **False positive (falso alarme)** — sensor sensível a ondulação, combustível na superfície.
- **Silent failure** — alarme não dispara mas parece estar ok; detectado só no teste funcional.

### Componentes relacionados

- **Seacock (válvula de costado)** — válvula no thru-hull; fonte #1 de vazamento se mal manutenida.
- **Thru-hull fitting** — peça que atravessa o casco; bronze, marelon, nylon.
- **Stuffing box / gaxeta de eixo** — vedação do eixo do leme/propulsor; fonte típica de gotejamento.
- **Shaft seal PSS (packless shaft seal)** — vedação moderna sem gaxeta.
- **Bilge drain** — dreno de porão (em trailer / drenar em seco).
- **Limber hole** — furo de comunicação entre compartimentos para água drenar até o sump.
- **Strainer / filtro de bomba** — captura detritos antes de entrarem na bomba.

### Bomba (cross-ref)

- **Bomba automática** — com float próprio; liga quando water level atinge trigger.
- **Bomba manual de emergência** — Whale Gusher, Edson, Henderson; reserva mecânica.
- **Bomba de alto volume (high-capacity emergency)** — Rule 3700/8000 GPH; emergência + navios maiores.
- **Bomba de motor (engine-driven / crash pump)** — desvia água de refrigeração para bombear; emergência extrema.

### Testes e inspeção

- **Monthly manual test** — elevar float manualmente + confirmar buzzer + LED + remoto.
- **Annual professional inspection** — limpeza de sensor, teste de bateria, verificação de cabeamento.
- **Log de teste** — caderno/app com data + resultado + técnico; obrigatório em comercial.
- **Bump test** — teste rápido de resposta; não substitui verificação anual.

### Jurisdição e classificação

- **ABYC H-22** — padrão americano recreio.
- **ISO 15083** — padrão internacional pequena embarcação.
- **SOLAS II-1** — padrão marítimo comercial internacional.
- **NORMAM-201/204/211** — regulamento brasileiro.
- **RCD 2013/53/EU** — certificação europeia.

## FAQ

**Alarme de alagamento substitui a bomba de porão?**

Não. Ele complementa a bomba com função de alerta.

**Posso usar o mesmo float da bomba para acionar o alarme?**

É possível em arquiteturas simples, mas reduz independência funcional e tende a piorar a qualidade do alerta. Sensor dedicado é abordagem melhor.

**Notificação remota resolve o problema sozinha?**

Não. Ela ajuda quando o barco está desacompanhado, mas não substitui alarme local robusto.

## Integração com outras notas

- [[Bomba de Porão]]
- [[Sistema de Alarme Geral / Painel de Alarmes]]
- [[Monitoramento Remoto — VRM / Telemetria]]
- [[Sensor de Nível de Água]]
- [[Hotline (DC)]]

## Perguntas que esta nota responde

- Qual a função real do alarme de alagamento em uma embarcação?
- Como ele deve se relacionar com a bomba de porão?
- Quais erros tornam um high water alarm praticamente inútil?
