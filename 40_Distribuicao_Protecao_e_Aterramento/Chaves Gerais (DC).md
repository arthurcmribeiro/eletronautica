---
title: "Chaves Gerais (DC)"
note_type: "technical-note"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "CHAVES GERAIS (DC) 15919734f7fb834fbeda01362553ce8a.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "58"
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
  - "https://www.ul.com/services/ul-1107"
normas_citadas:
  - "ABYC E-11 (AC and DC Electrical Systems on Boats) — §11.4.7 localização, §11.5 dimensionamento de dispositivos"
  - "ABYC E-10 (Storage Batteries) — §10.7 limite de conexões no polo, §10.9 chaves de bateria"
  - "ABYC E-30 (Electric Propulsion Systems) — chaves de tração"
  - "ABYC A-31 (Battery Chargers and Inverters)"
  - "ISO 10133:2012 (Small craft — Electrical systems — Extra-low-voltage DC) — §6.8 seccionamento"
  - "ISO 8846:1990 (Small craft — Electrical devices — Protection against ignition of surrounding flammable gases) — chaves ignition-protected"
  - "ISO 13297:2020 (Small craft — Electrical systems — AC installations) — referência para seccionamento AC"
  - "IEC 60947-3 (Low-voltage switchgear — Switches, disconnectors, switch-disconnectors and fuse-combination units)"
  - "IEC 60947-5 (Low-voltage switchgear — Control circuit devices)"
  - "IEC 60529 (IP Code)"
  - "IEC 62262 (IK Code) — impacto mecânico"
  - "IEC 60092-504 (Electrical installations in ships — Control and instrumentation)"
  - "IEC 60092-302 (Switchgear and controlgear for ships)"
  - "UL 1107 (Marine Switches)"
  - "UL 98 (Enclosed and Dead-Front Switches)"
  - "UL 489 (Molded-Case Circuit Breakers)"
  - "UL 508 (Industrial Control Equipment)"
  - "SAE J1171 (Marine Ignition Protection)"
  - "SAE J1194 (Rollover Protective Structures — aplicável a chave principal acessível)"
  - "NFPA 70 (NEC) — art. 230.70 (disconnecting means), art. 555 (marinas)"
  - "ABNT NBR 5410 (Instalações elétricas de baixa tensão) — §5.7 seccionamento e comando"
  - "ABNT NBR IEC 60947-3 (Chaves seccionadoras)"
  - "ABNT NBR IEC 60529 (graus de proteção IP)"
  - "NORMAM-05/DPC (Embarcações de esporte e recreio)"
  - "NORMAM-01/DPC (Embarcações em navegação marítima)"
  - "USCG 33 CFR 183.460 (Conductors in circuits of less than 50 V — battery switch)"
  - "USCG 46 CFR 111.12 (Main power supply cables and switchgear)"
  - "DNV-RU-SHIP Pt.4 Ch.8 §3 (Switchgear for ships)"
family_clusters:
  - "ABYC-USCG (EUA)"
  - "ISO-IEC (internacional)"
  - "ABNT-NORMAM (Brasil)"
  - "DNV-classificadoras (navios)"
aliases:
  - "CHAVES GERAIS (DC)"
  - "Chave de bateria"
  - "Battery switch"
  - "Chave seccionadora DC"
seo_title: "Chaves Gerais (DC)"
seo_description: "CHAVES GERAIS DC — Dispositivos de seccionamento e isolamento do sistema de corrente continua, com importancia critica para seguranca, manutencao, gerenciamento de bancos e manobra de emergencia."
seo_keywords:
  - "Chave geral DC"
  - "Seccionamento de bateria"
  - "Battery switch"
  - "40 Distribuicao Protecao e Aterramento"
geo_queries:
  - "Como especificar chave geral DC em embarcacao?"
  - "Qual a funcao da chave geral de bateria no barco?"
  - "Posso manobrar battery switch com motor ligado?"
related_notes:
  - "Barramento DC / Bus Bar / Distribuição DC"
  - "Chaves Seletoras (AC)"
  - "Divisores de Carga (DC)"
  - "Hotline (DC)"
  - "Banco de Baterias"
  - "Disjuntores (DC) e (AC)"
---

# Chaves Gerais (DC)

> [!abstract] Resumo técnico
> Chave geral DC é o dispositivo de seccionamento principal do sistema de corrente contínua ou de um banco específico. Em embarcações, ela precisa ser pensada como elemento de segurança, manutenção e governança elétrica, não como simples "liga/desliga" instalado perto da bateria sem critério. ABYC E-11.4.7 e USCG 33 CFR 183.460 exigem chave principal com acessibilidade imediata, corte completo do circuito de partida, e coordenação com proteção a montante — tudo documentado em diagrama unifilar.

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **Dimensione pelo pico mais severo**, não pela média — partida diesel pode exigir 800-1500 A pico em 3 s; use chave com rating "cranking" distinto do "continuous" (ex.: Blue Sea 6006: 500 A cont. / 2500 A cranking).
> 2. **Chave ≠ proteção** — chave secciona, fusível/disjuntor protege. Fusível sempre ≤ 178 mm (7") do polo da bateria (ABYC E-11.4.7).
> 3. **Acessível em < 3 segundos** — chave principal deve ser alcançável da posição do operador sem abrir painel ou usar ferramenta (USCG 33 CFR 183.460; SOLAS II-1 regra 42).
> 4. **Ignition-protected em compartimento com gás** (bateria ventilada chumbo-ácido, paiol de combustível) — ISO 8846 / SAE J1171 / UL 1107.
> 5. **Chave seletora 1-2-BOTH-OFF**: BOTH é operação paralela (emergência ou troca entre bancos com alternador ativo), não rotina; ON-rotation com motor ligado em chave NÃO-AFD (alternator field disconnect) destrói o alternador.
> 6. **IP classification pelo ambiente** — IP54+ em ambiente externo protegido, IP66 em convés exposto; IK08 mínimo para resistência a impacto.
> 7. **Cor vermelha padrão** (SOLAS/IMO) para chave de emergência e desligamento geral; sinalização luminosa ou fosforescente facilita operação em baixa luz.
> 8. **Torque especificado** em porcas dos terminais — afrouxamento é causa #1 de aquecimento; marque com caneta de torque.
> 9. **Documentar exatamente o que a chave corta e o que NÃO corta** — hotline (bilge pump, CO detector) permanece energizada por arquitetura — isso deve estar etiquetado junto à chave.

> [!danger] Quando chamar um especialista
> Estes 9 cenários exigem engenheiro elétrico náutico ou certificador:
> 1. **Sistema com banco Li-Fe > 200 Ah e inversor > 3 kW** — corrente de curto presumida > 10 kA; exige chave com capacidade de interrupção coordenada (IEC 60947-3 utilization category DC-22B mínimo) e fusível classe T coordenado.
> 2. **Propulsão elétrica ou híbrida** — ABYC E-30 exige chave principal com dispositivo de segurança integrado (anti-faísca, arc-free, pre-charge para capacitores de controlador); chave de bateria comum falha catastroficamente em DC > 48 V com inversor.
> 3. **Retrofit que substitui chave manual por contactor automático/BMS** — integração com sistema de gerenciamento de banco (VSR, ACR, Cerbo/Cyrix) exige lógica de pré-carga, proteção de inversor e coordenação com alternador.
> 4. **Embarcação comercial sob classificadora (DNV, Lloyd's, BV, RINA, ABS)** — exige chave certificada naval (IEC 60092-302) com certificado de classe; chave de recreio não é aceita.
> 5. **Sistema DC > 72 V** (propulsão, solar high-voltage) — regime de "high voltage DC" com risco de arco sustentado; exige chave com câmara de extinção de arco magnético (DC-rated, não AC-rated adaptada).
> 6. **Paralelismo permanente de bancos com diferentes químicas** (chumbo + Li-Fe) — arquitetura errada causa corrente de equalização destrutiva; exige DC-DC isolador ou contator com lógica BMS.
> 7. **Compartimento classificado (Zone 1/2 por gás inflamável)** — exige chave Ex (ATEX, IECEx ou classe I div. 1/2 nos EUA); chave marine-grade comum não serve.
> 8. **Investigação de fusão ou arco em chave em operação** — suspeita de arc fault: isolar imediatamente o banco pelo fusível MRBF, não pela chave avariada.
> 9. **Certificação CE/RCD, NMMA ou USCG inspection** — requer dossiê com memorial de cálculo de Icc presumida, coordenação cabo-chave-proteção, teste de operação sob carga.

## O que é

Chave geral DC é o dispositivo usado para conectar ou isolar um banco, um conjunto de cargas ou um subsistema. Dependendo da arquitetura, pode assumir papéis diferentes:

- **chave de seccionamento do banco** (main battery switch);
- **chave de serviço** (house battery switch);
- **chave de arranque** (engine/start battery switch);
- **chave seletora entre bancos** (1-2-BOTH-OFF, com ou sem AFD);
- **chave de emergência ou manutenção** (lockout/tagout).

## Função na embarcação

- permitir isolamento elétrico seguro para manutenção ou emergência;
- facilitar manutenção e atendimento a emergência (incêndio, alagamento);
- separar bancos ou serviços conforme a arquitetura;
- reduzir dependência de desconexão direta no borne da bateria (risco de curto com ferramenta);
- organizar a operação do sistema DC (quem liga o quê, em que ordem);
- em alguns casos, permitir combinação paralela de bancos para partida em emergência (BOTH).

## Fundamentos mínimos

### Chave geral não substitui proteção contra sobrecorrente

Ela secciona e isola. A proteção do cabo e do circuito continua dependendo de fusíveis, disjuntores ou solução equivalente na arquitetura correta. ABYC E-11.4.7: proteção principal ≤ 178 mm (7") do polo da bateria, independentemente da posição da chave.

### Nem tudo deve necessariamente morrer na mesma chave

Alguns circuitos podem exigir alimentação permanente ou rota dedicada, conforme a estratégia da embarcação:

- bombas de porão automáticas (ABYC E-11.10.2 permite hotline);
- detector de CO e gás (SOLAS II-2 para navio; recomendação forte para recreio);
- memória de plotter/inversor (volátil);
- rádio/EPIRB de emergência em embarcação oceânica.

A arquitetura precisa deixar isso explícito em diagrama e etiqueta.

### Corrente contínua e corrente de manobra importam

A chave deve suportar o serviço real do sistema, incluindo:

- **corrente contínua plausível** (soma com fator de simultaneidade);
- **corrente de pico** (partida diesel: 3-5× da contínua; inversor com carga resistiva: 1,5× por 100 ms; motor elétrico de winch: 6-8× por 200 ms);
- **corrente de interrupção** (abertura sob falha — DC-rated, não apenas AC);
- **esforço de manobra** (quantidade de ciclos de comutação sob carga — IEC 60947-3);
- **ambiente térmico e mecânico** (vibração do motor, temperatura da sala de máquinas).

### Operação com fontes ativas exige disciplina

Troca de posição sob condição inadequada pode ser problemática:

- **Motor ligado + chave seletora NÃO-AFD** = alternador vê carga desconectada momentaneamente = pico de tensão que destrói diodos do alternador e possivelmente ECU;
- **Inversor ligado + seccionamento brusco** = capacitor do inversor descarrega em arco ou alarme;
- **Banco paralelo com tensões diferentes** = corrente de equalização destrutiva.

A forma correta de operar depende do tipo exato da chave, da topologia e das fontes ativas no sistema. Manual do fabricante e projeto valem mais que regra decorada de cais.

## Tipos e arquiteturas comuns

### Chave simples ON/OFF

- adequada para seccionamento claro de banco ou grupo de cargas;
- simples e robusta quando bem escolhida;
- exemplos: Blue Sea 6006/9001/9003, Marinco BM-series, Victron Battery Switch.

### Chave seletora de bancos (1-2-BOTH-OFF)

- permite escolher banco ou combinar bancos conforme a arquitetura;
- exige etiquetagem, documentação e operação consciente;
- **com AFD (Alternator Field Disconnect)**: desabilita o campo do alternador durante a comutação — permite manobra com motor ligado;
- **sem AFD**: manobra com motor ligado pode destruir alternador;
- exemplos: Blue Sea 9001e/9003e (com AFD), Perko 8501/8511.

### Solução com gerenciamento automático

- usa **ACR (Automatic Charging Relay)**, **VSR (Voltage Sensitive Relay)**, **DC-DC isolator/charger** ou lógica equivalente (Victron Cerbo/SmartBMS, Mastervolt MasterBus);
- reduz dependência da operação manual, mas não elimina necessidade de seccionamento físico coerente;
- vantagem: combinação/separação automática conforme estado de carga; desvantagem: adiciona complexidade e ponto de falha eletrônico.

### Contactor/solenoide de alta corrente

- comando remoto (12/24 V) de alta corrente (100-500 A);
- usado em BMS Li-Fe (disconnect sob low voltage cut-off);
- exemplos: Gigavac GV200/GX14, TE Connectivity EV200, Blue Sea ML-ACR.

### Chave de emergência (emergency cutoff)

- cor vermelha, acesso imediato, geralmente com lockout/tagout;
- às vezes instalada junto ao posto de comando ou perto da escotilha principal;
- SOLAS II-1 regra 42 para navio comercial.

## Dimensionamento — tabela de referência

| Uso | Corrente cont. | Corrente pico (cranking) | Chave típica | Fabricantes |
| --- | --- | --- | --- | --- |
| Banco house pequeno (até 100 Ah) | 100 A | 250 A | Blue Sea 6005 "mini" | Blue Sea, Perko |
| Banco house médio (100-300 Ah) | 300 A | 800 A | Blue Sea 6006/9001 | Blue Sea, Marinco |
| Banco house grande + inversor até 3 kW | 600 A | 1500 A | Blue Sea 9003e (AFD) | Blue Sea, Victron |
| Banco start diesel 4-6L | 300 A | 1000 A | Blue Sea 6006 | Blue Sea, Perko |
| Banco start diesel 8-12L | 500 A | 2000 A | Blue Sea 6006 cranking | Blue Sea, Cole Hersee |
| Propulsão elétrica até 10 kW @ 48 V | 300 A | 500 A | contactor Gigavac GV200 | Gigavac, TE |
| Propulsão 20+ kW ou Li-Fe > 200 Ah | conforme projeto | conforme projeto | contactor Ex específico + pre-charge | projeto dedicado |

## Projeto e instalação

### O que precisa ser definido

1. qual banco ou subsistema a chave secciona;
2. quais circuitos ficam a montante (sempre energizados) e a jusante (cortados pela chave);
3. corrente contínua e picos envolvidos (incluindo interrupção sob falha);
4. ambiente de instalação (IP, IK, temperatura, risco de gás);
5. acessibilidade (tempo de acesso < 3 s em emergência);
6. operação normal, manutenção e emergência;
7. interação com alternador (AFD), carregadores, inversores e combinações de banco;
8. sinalização visual (luz, fosforescência, etiqueta);
9. lockout/tagout para manutenção.

### Diretrizes práticas

- instalar em local acessível e claramente identificado (etiqueta gravada, não adesiva);
- escolher componente com rating coerente com o serviço real (com margem ≥ 25% na contínua, ≥ 2× no pico);
- evitar chicotes longos e desprotegidos entre bateria, proteção e chave;
- documentar exatamente o que a chave corta e o que não corta (hotline, bilge, detector de gás, memória de inversor);
- tratar seletora manual com cuidado especial quando houver múltiplas fontes e bancos — AFD é obrigatório se houver alternador ativo;
- torquear terminais conforme especificação e marcar com caneta de torque;
- usar terminais de cobre estanhado com heat-shrink adesivo;
- evitar instalar chave em local sujeito a alagamento direto (mesmo IP66 degrada após submersão repetida).

## Onde costuma dar problema

| Problema | Causa provável | Correção |
| --- | --- | --- |
| aquecimento na chave | subdimensionamento, contato degradado ou terminação frouxa | re-torquear, medir queda de tensão, trocar se ΔV > 100 mV @ corrente nominal |
| queda de tensão significativa | resistência de contato ou conexões deficientes | inspeção visual dos contatos internos (se acessível), substituição preventiva a cada 5-7 anos |
| operador não entende a posição da chave | etiquetagem ruim ou arquitetura confusa | redesenhar etiqueta, adicionar diagrama unifilar ao lado da chave |
| banco é descarregado indevidamente | lógica de separação e operação mal definidas | revisar arquitetura; instalar ACR/VSR; adicionar monitor de bateria |
| falha em manutenção | circuito supostamente isolado ainda permanece energizado (hotline não documentada) | etiquetar cada circuito hotline; usar lockout/tagout + multímetro antes de trabalhar |
| alternador queima após manobra com motor ligado | chave seletora sem AFD | trocar por modelo com AFD (Blue Sea 9001e/9003e) ou desligar motor antes de manobrar |
| arco sustentado ao abrir sob carga | chave AC-rated usada em DC | trocar por chave DC-rated com câmara magnética |

## Diagnóstico prático

1. **Medir queda de tensão** através da chave sob carga máxima (multímetro em mV) — limite prático < 100 mV @ corrente nominal.
2. **Inspecionar terminais**, aquecimento (termografia se disponível) e integridade mecânica.
3. **Confirmar a posição e a lógica real** de cada polo ou seleção (teste de continuidade com multímetro).
4. **Verificar se a arquitetura documentada** corresponde ao instalado (diagrama unifilar × realidade).
5. **Avaliar se a chave está sendo usada** dentro do regime de corrente e operação para o qual foi selecionada (tabela do fabricante × medição real).
6. **Testar AFD** (se aplicável): acionar o campo do alternador em teste antes de manobrar seletora com motor ligado.
7. **Verificar IP/IK** do compartimento de instalação (ambiente ainda compatível com classificação da chave?).

## Boas práticas profissionais

- usar chave identificada e compatível com a corrente e o ambiente;
- posicionar a chave de modo acessível para operação e emergência (< 3 s de acesso);
- separar claramente banco de partida, banco de serviço e circuitos permanentes quando existirem;
- medir e registrar quedas de tensão em inspeções periódicas (anual ou 500 h);
- treinar a operação correta conforme a topologia do barco, sem improviso;
- substituir chave preventivamente a cada 5-7 anos em uso intensivo (contatos desgastam mesmo sem falha aparente);
- manter etiqueta atualizada após retrofit (a chave pode ter mudado de função sem ser visivelmente diferente);
- em embarcação de aluguel/charter, incluir briefing sobre posição da chave principal em check-in do cliente;
- proteger contra acionamento acidental em seletoras críticas (cover, lockout simples);
- documentar torque de aperto e data da última inspeção em etiqueta próxima.

## Erros comuns

- tratar chave geral como proteção contra curto-circuito;
- escolher componente pela aparência ou preço, não pelo rating;
- deixar a função real da chave ambígua para o operador;
- usar a seletora sem entender as consequências para bancos e fontes ativas;
- esquecer que circuitos permanentes e bypass precisam estar documentados;
- manobrar seletora NÃO-AFD com motor ligado (alternador queima);
- instalar chave em local sujeito a alagamento direto;
- deixar hotline (bilge, CO) permanentemente energizada sem fusível individual próximo ao banco;
- usar chave AC em circuito DC (arco sustentado sem câmara de extinção);
- dimensionar apenas pela corrente contínua e ignorar pico de partida.

## Relação com outros sistemas

- **[[Barramento DC / Bus Bar / Distribuição DC]]** — distribuição a jusante da chave.
- **[[Banco de Baterias]]** — banco ou bancos controlados pela chave.
- **[[Divisores de Carga (DC)]]** e soluções de gestão de banco — interação operacional.
- **[[Hotline (DC)]]** — circuitos que podem permanecer fora da chave.
- **[[Disjuntores (DC) e (AC)]]** — proteção coordenada do sistema.
- **[[Cabeamento Náutico]]** — cabo alimentador até a chave.
- **[[Chaves Seletoras (AC)]]** — análogo em AC (transfer switches).

## Normas e referências

### Por família e jurisdição

| Família | Norma | Escopo |
| --- | --- | --- |
| **ABYC (EUA)** | E-11 §4.7 | localização e acessibilidade |
| ABYC | E-10 §9 | chaves de bateria |
| ABYC | E-30 | propulsão elétrica |
| **USCG (EUA)** | 33 CFR 183.460 | battery switch em embarcação de recreio |
| USCG | 46 CFR 111.12 | switchgear em navio comercial |
| **UL (EUA)** | UL 1107 | chaves marítimas |
| UL | UL 98 | chaves encapsuladas |
| UL | UL 508 | equipamento de controle |
| **SAE (EUA)** | SAE J1171 | marine ignition protection |
| **NFPA (EUA)** | NFPA 70 art. 230.70 | disconnecting means |
| **ISO (internacional)** | ISO 10133:2012 | sistemas DC em pequenas embarcações |
| ISO | ISO 8846:1990 | ignition protection |
| **IEC (internacional)** | IEC 60947-3 | switchgear BT — switches |
| IEC | IEC 60947-5 | dispositivos de comando |
| IEC | IEC 60529 | IP code |
| IEC | IEC 60092-302 | switchgear para navios |
| **ABNT (Brasil)** | NBR 5410 §5.7 | seccionamento e comando |
| ABNT | NBR IEC 60947-3 | chaves seccionadoras |
| ABNT | NBR IEC 60529 | IP code |
| **NORMAM (Brasil)** | NORMAM-05/DPC | embarcações de esporte e recreio |
| NORMAM | NORMAM-01/DPC | navegação marítima |
| **Classificadoras** | DNV-RU-SHIP Pt.4 Ch.8 §3 | switchgear para navios |

### Comparação prática entre jurisdições

- **EUA (ABYC + USCG)**: prescrição clara de acessibilidade (< 3 s) e distância da proteção (≤ 178 mm do polo); UL 1107 exige teste de ignição.
- **Internacional (ISO/IEC)**: abordagem por utilization category (DC-20 a DC-23 em IEC 60947-3); ISO 10133 orienta sem prescrever marca ou distância rígida.
- **Brasil (ABNT + NORMAM)**: NBR 5410 predial não cobre náutica; NORMAM remete a ABYC/ISO para recreio e SOLAS/IEC para comercial.
- **Navio classificado**: IEC 60092-302 é obrigatório — chave de recreio (mesmo marine-grade) não é aceita.

## Glossário rápido

1. **ACR (Automatic Charging Relay)** — relé que conecta bancos automaticamente ao detectar tensão de carga.
2. **AFD (Alternator Field Disconnect)** — terminal que desabilita o campo do alternador durante manobra.
3. **Arc flash** — descarga elétrica violenta por ionização do ar em curto-circuito.
4. **BMS (Battery Management System)** — sistema de gerenciamento de banco, principalmente em Li-Fe.
5. **Banco house / service** — banco de baterias para cargas gerais do barco.
6. **Banco start / engine** — banco dedicado à partida do motor.
7. **Battery switch** — chave geral de bateria.
8. **Break capacity (Icu)** — capacidade de interrupção em curto; diferente em DC e AC.
9. **Bypass** — circuito paralelo que contorna a chave (hotline).
10. **Câmara de extinção de arco** — compartimento magnético que alonga e extingue o arco em DC.
11. **Category (utilization — IEC 60947-3)** — DC-20/21/22/23: grau de severidade do serviço (A/B conforme tempo de corte).
12. **Chave gaveta** — tipo de chave com movimento deslizante, comum em painéis industriais.
13. **Chave rotativa (rotary switch)** — chave com movimento circular, padrão em battery switch náutico.
14. **Contactor** — chave comandada eletricamente (solenoide interno).
15. **Continuous current** — corrente contínua contínua nominal.
16. **Cranking current** — corrente de partida do motor, muito maior que a contínua.
17. **Curto-circuito presumido (Icc)** — maior corrente que o sistema pode entregar em falha franca.
18. **DC-20/21/22/23** — categorias de uso em IEC 60947-3 — DC-22B é típico para battery switch marine.
19. **Dead-front** — painel com partes energizadas atrás de superfície isolante — padrão de segurança.
20. **Disconnector** — chave seccionadora sem capacidade de corte sob carga.
21. **Drip loop** — alça no cabo para escorrer água por gravidade.
22. **Emergency cutoff** — chave de desligamento de emergência, cor vermelha, acesso imediato.
23. **Ex (ATEX/IECEx)** — classificação para atmosfera explosiva.
24. **Fuse-combination unit** — chave com fusível embutido (IEC 60947-3).
25. **Galvanic equalization current** — corrente parasita entre bancos paralelos com tensões diferentes.
26. **Hotline** — circuito permanentemente energizado (fora da chave geral) — bilge, CO detector.
27. **Ignition-protected** — componente que não gera faísca externa capaz de inflamar gás (ISO 8846).
28. **IK code** — grau de proteção contra impacto mecânico (IEC 62262).
29. **Inrush current** — pico de corrente ao ligar carga (capacitor, motor, transformador).
30. **IP code** — grau de proteção contra pó e água (IEC 60529).
31. **Isolator** — sinônimo de chave seccionadora sem capacidade de corte sob carga.
32. **LOC (Lockout/Tagout)** — procedimento de bloqueio e etiquetagem para manutenção segura.
33. **Load break switch** — chave com capacidade de corte sob carga nominal.
34. **Main battery switch** — chave principal do banco house ou start.
35. **Make capacity** — capacidade de fechar em curto sem soldar contatos.
36. **Marine-grade** — construção e materiais resistentes ao ambiente marinho (cobre estanhado, inox, IP elevado).
37. **MRBF (Marine Rated Battery Fuse)** — fusível montado no polo da bateria.
38. **Off-position (O)** — posição de aberto/isolado da chave.
39. **On-position (I)** — posição de fechado/conectado.
40. **Paralelo momentâneo** — conexão temporária de dois bancos (posição BOTH).
41. **Pre-charge** — circuito que pré-carrega capacitor de inversor/controlador antes do fechamento da chave principal.
42. **Rotary switch** — chave rotativa com múltiplas posições (1-2-BOTH-OFF).
43. **Selector switch** — chave seletora entre fontes/bancos.
44. **Single-pole / double-pole** — chave com 1 ou 2 polos comandados simultaneamente.
45. **Solenoid** — eletroímã que aciona o contato interno em contactor.
46. **Switch-disconnector** — chave com função de comando e seccionamento.
47. **Torque marking** — marca de aperto feita com caneta especial após torque calibrado.
48. **Utilization category** — classificação de uso em IEC 60947-3 (AC-1 a AC-23, DC-20 a DC-23).
49. **VSR (Voltage Sensitive Relay)** — relé sensível à tensão que combina bancos durante carga.
50. **Zero-crossing** — ponto da onda AC em que a corrente é zero — DC não tem, daí o desafio de extinção de arco.

## FAQ

**Toda carga deve passar pela chave geral?**

Não como dogma. Depende da arquitetura e dos circuitos que precisam permanecer alimentados (hotline). ABYC E-11.10.2 permite circuitos hotline (bilge automática, CO detector, memória de inversor) fora da chave, desde que tenham fusível individual próximo ao banco.

**Chave seletora manual ainda faz sentido?**

Pode fazer, mas exige projeto e operação claros. Em muitos casos, soluções automáticas de gerenciamento de banco (ACR, VSR, DC-DC) trazem mais previsibilidade. A regra é: se o operador não entende a lógica, troque por automático.

**Se a chave gira e parece funcionar, ela está boa?**

Não necessariamente. Queda de tensão, aquecimento e degradação de contato podem existir mesmo com sensação mecânica aparentemente normal. Medir ΔV sob carga é o único diagnóstico confiável.

**Posso usar chave AC-rated em DC se o rating em ampères for suficiente?**

Não em corrente significativa. DC não tem zero-crossing natural, então o arco sustenta muito mais tempo ao abrir sob carga. Chave AC-rated pode soldar ou queimar. Use chave com rating DC específico e categoria utilization DC-22B ou superior.

**Posso manobrar a chave seletora com o motor ligado?**

Só se a chave tiver AFD (Alternator Field Disconnect) ou se o alternador estiver desligado antes da manobra. Sem AFD, a tensão de saída do alternador dispara ao ser desconectada abruptamente e queima diodos (e possivelmente regulador e ECU).

**Preciso de chave ignition-protected mesmo em bateria selada AGM/Li-Fe?**

Recomendável em qualquer caso; obrigatório se houver compartimento compartilhado com bateria ventilada chumbo-ácido, tanque de combustível ou paiol de gás. ABYC E-11.5.1 e ISO 8846 cobrem o requisito.

## Visual didático

![Chaves gerais e seletoras: isolamento e manobra](../_visuals/generated/chaves-gerais-seletoras-isolamento.svg)

Diferenciar desligar, selecionar banco, paralelar emergencia e isolar para manutencao.

**Cautela:** Nunca manobre chaves de bateria ou AC sem entender carga, alternador, inversor e recomendacao do fabricante.

Material de apoio: [Chaves gerais e seletoras: isolamento e manobra](../_visuals/generated/chaves-gerais-seletoras-isolamento.md)

## Integração com outras notas

- [[Barramento DC / Bus Bar / Distribuição DC]]
- [[Chaves Seletoras (AC)]]
- [[Divisores de Carga (DC)]]
- [[Hotline (DC)]]
- [[Banco de Baterias]]
- [[Disjuntores (DC) e (AC)]]
- [[Cabeamento Náutico]]
- [[Terminais Conectores e Emendas]]

## Perguntas que esta nota responde

- O que faz uma chave geral DC em embarcações?
- Como especificar e operar corretamente uma chave de bateria?
- Quais falhas aparecem em chaves gerais mal dimensionadas ou mal documentadas?
- Qual a diferença entre battery switch, seletora 1-2-BOTH-OFF e contactor?
- Quando é obrigatório usar chave com AFD ou ignition-protection?
