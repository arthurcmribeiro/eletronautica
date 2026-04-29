---
title: "Carregador de Bateria (AC To DC)"
note_type: "technical-note"
domain: "20_Baterias_e_Armazenamento"
source_file: "CARREGADOR DE BATERIA (AC to DC) 64e19734f7fb83f6879701f63709d32e.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "12"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
normas_citadas:
  - "ABYC E-11 (2023) — AC and DC Electrical Systems on Boats"
  - "ABYC A-31 (2024) — Battery Chargers and Inverters"
  - "ABYC E-13 (2023) — Lithium Ion Batteries (em banco LFP)"
  - "ABYC E-10 (2023) — Storage Batteries"
  - "ABYC A-28 (2023) — Galvanic Isolators (interface shore power)"
  - "ISO 13297:2020 — Small craft — AC and DC installations"
  - "ISO 8846:2022 — Protection against ignition of surrounding flammable gases"
  - "IEC 60335-2-29 — Safety of battery chargers"
  - "IEC 62040-1 — UPS (conceitos aplicáveis a inversor/carregador)"
  - "UL 1236 — Battery chargers for charging engine-starter batteries"
  - "UL 458 — Power converters/inverters for marine use"
  - "NMEA 2000 (IEC 61162-3) — Comunicação de rede marítima"
  - "ABNT NBR 5410:2004 + emendas — Instalações elétricas de baixa tensão"
  - "NORMAM-211/DPC — Embarcações de esporte e recreio"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://abycinc.org/news/standardsupdatewebinar/"
  - "https://www.iso.org/standard/83643.html"
  - "https://www.iec.ch/"
  - "https://www.ul.com/"
aliases:
  - "CARREGADOR DE BATERIA (AC to DC)"
seo_title: "Carregador de Bateria (AC To DC)"
seo_description: "Carregador de bateria AC/DC é o equipamento que converte a energia AC disponível no cais ou no gerador em energia DC controlada para recarga e manutenção do banco. O ponto crítico é coordenar perfil de carga, corrente, temperatura, química e proteção do sistema."
seo_keywords:
  - "Carregador"
  - "Bateria"
  - "20 Baterias e Armazenamento"
geo_queries:
  - "O que é Carregador de Bateria (AC To DC) em instalações elétricas náuticas?"
  - "Qual é a função de Carregador de Bateria (AC To DC) na embarcação?"
related_notes:
  - "Bancos de Bateria"
  - "CAIS (Pier) (AC)"
  - "Monitor de Bateria / BMV / Shunt"
  - "Tipos de Bateria"
  - "BMS — Battery Management System"
  - "Gerador (AC)"
  - "Inversora (DC To AC)"
  - "Lítio LiFePO4 — Instalação e Cuidados Específicos"
  - "Carregador Elétrico para Tender e Jet Ski"
---

# Carregador de Bateria (AC To DC)

> [!abstract] Resumo técnico
> CARREGADOR DE BATERIA (AC→DC) — Conversor inteligente que transforma corrente alternada do cais ou gerador em DC regulado para recarregar o banco de baterias com segurança.

> [!tip] Regra de decisão em 30 segundos
> 1. **Carregador profissional ≠ retificador.** Multietapas (bulk/absorption/float), compensação de temperatura, perfil por química e proteção integrada são requisito, não diferencial.
> 2. **O perfil de carga é ditado pela química da bateria, não pelo default de fábrica do carregador.** AGM ≠ GEL ≠ FLA ≠ LiFePO4 — diferença de 0,3-0,6 V em absorção destrói bateria em centenas de ciclos.
> 3. **Dimensionar a corrente entre 10-30 % da capacidade do banco.** Banco 200 Ah → 20-50 A de carregador. Acima disso, sem coordenação térmica, ativa proteção e encurta vida.
> 4. **Fusível DC ≤ 178 mm do terminal positivo da bateria** (ABYC E-11), dimensionado para o cabo e com AIC adequado à Isc do banco. Carregador não substitui fusível.
> 5. **Sonda de temperatura no centro do banco é requisito**, não acessório. Variação de 30 °C altera a tensão ideal em ~0,6 V — sem compensação, o carregador supercarrega no verão e subcarrega no inverno.
> 6. **Lítio exige comunicação com BMS** (VE.Bus, CAN, NMEA 2000) ou perfil rigorosamente alinhado ao datasheet da célula. Carregador "lithium auto" genérico não substitui comunicação real.
> 7. **Shore power deve passar por transformador de isolamento ou isolador galvânico** antes do carregador — proteção contra ESD e corrosão galvânica na marina.
> 8. **Nunca conecte ao cais sem verificar polaridade e PE.** Polaridade invertida + carregador = banco sob potencial do neutro alienígena; um curto qualquer vira incêndio ou ESD.
> 9. **Documente no painel: marca, modelo, perfil configurado, corrente nominal, data de instalação, versão de firmware.** Sem registro, laudo em sinistro fica impossível.

> [!danger] Quando chamar um especialista
> - **Retrofit de chumbo → lítio mantendo carregador antigo.** Perfil, absorção, float, comunicação e corrente são todos diferentes. Reconfigurar ou substituir o carregador; projeto com ART/CREA.
> - **Carregador superaquecendo repetidamente** (desliga por proteção térmica, case quente ao toque). Causa pode ser banco com célula em curto interno puxando corrente indefinidamente, ventilação obstruída, corrente dimensionada acima da capacidade do carregador, ou falha interna. Abrir e medir sem diagnóstico é risco de choque.
> - **Inversor/carregador (MultiPlus, Quattro, Combi) em embarcação com múltiplas fontes AC** (shore + gerador + solar). Transfer switch, paralelização, neutro comutado e bond N-PE dependente da fonte ativa são decisões de projeto que exigem parecer técnico assinado.
> - **Sistema com shore power 120/240V split-phase americano em marina 220 V brasileira.** Não conecte. Transformador de isolamento com enrolamento adequado + reconfiguração do carregador é condição.
> - **BMS desconectando durante carga** sem causa aparente. Pode ser célula em falha, shunt mal dimensionado, cabo com queda excessiva, tensão de absorção alta demais para a temperatura atual. Investigação com app, multímetro, termômetro IR.
> - **Incêndio ou sinistro envolvendo carregador** (case derretido, fumaça, faísca no shore inlet, banco danificado). Preservar cena, acionar seguradora, laudo pericial com ART/CREA, análise de causa raiz.
> - **Eletropropulsão com carregamento rápido AC → DC 48/96/400 V.** ISO 16315:2016 + UL 2202 (onboard EV charger) + IEC 61851 (EV charging infrastructure) — não é domínio recreativo comum; exige projeto integrado.
> - **Embarcação importada com carregador 120 V/60 Hz marítimo americano operando em 220 V/60 Hz brasileiro.** Reavaliação de entrada AC, transformador, reconfiguração do carregador, verificação de polaridade e ajuste de cabo AC de entrada.
> - **Shore power com corrosão galvânica detectável** (zinco consumido rapidamente, partes de aço com corrosão branca acelerada). Antes de trocar zinco, diagnosticar: pode ser isolador galvânico com falha, ausência de PE, bond N-PE errado ou neutro partido da marina. Carregador ligado entra na cadeia.

## O que é

O carregador de bateria é um conversor AC/DC que transforma a tensão alternada da rede elétrica (cais ou gerador) em tensão contínua regulada, adequada para carregar baterias de forma segura e controlada.

**Não é um simples retificador.** Um carregador profissional é um equipamento eletrônico inteligente que ajusta tensão e corrente conforme o estado de carga da bateria, segue curvas de carregamento específicas por tipo de química, protege contra sobrecarga e curto-circuito, compensa temperatura e monitora o processo em tempo real.

**Tipos principais:**

- **Carregador on/off:** desliga ao atingir tensão de corte — obsoleto, prejudica baterias
- **Carregador multietapas (3–4 stages):** bulk → absorption → float → equalização (opcional) — padrão atual
- **Inversor/Carregador:** integra inversão DC→AC com carregamento AC→DC (Victron MultiPlus, Mastervolt Combi)
- **Carregador DC/DC (B2B):** carrega banco de serviço a partir do alternador, sem conflito — não confundir com este tópico

## Função

Converter AC (220V/60Hz do cais ou gerador) em DC regulado para:

- Recarregar banco de baterias de forma completa e segura
- Manter banco em flutuação durante a permanência no cais
- Compensar consumos de standby (alarme, VHF, GPS) sem descarregar o banco
- Estender vida útil das baterias com curva de carga correta

É a principal fonte de carregamento quando o barco está atracado.

## Como aparece na prática

Embarcação atracada → conectada ao shore power → carregador detecta AC → entra em bulk com limite de corrente → migra para absorção conforme tensão e algoritmo configurados → reduz para manutenção/standby quando aplicável. Os valores exatos dependem da química, da temperatura, do fabricante e da estratégia de uso.

**Cena típica:** barco na marina durante a semana. Na sexta-feira à noite o proprietário chega, o banco está em 100% porque o carregador passou a semana em float compensando consumos de standby. Na saída do fim de semana, banco pleno.

**Cena problemática:** carregador configurado para AGM em banco de GEL → tensão de absorption 14,7V destruindo células aos poucos → após 18 meses banco morre prematuramente.

## Fundamentos mínimos

**Curva de carregamento em 4 etapas:**

- **Bulk:** corrente máxima constante — tensão sobe rapidamente (0% → ~80% de carga)
- **Absorption:** tensão constante no valor de absorção — corrente cai gradualmente (80% → ~95%)
- **Float:** tensão reduzida de manutenção — corrente mínima (~5% → manutenção)
- **Equalização (opcional):** etapa controlada aplicável apenas quando a química e o fabricante permitirem

**Por que cada bateria tem tensões diferentes:**

A química da bateria determina a janela segura de tensão e corrente. O perfil final deve vir do fabricante da bateria e da arquitetura do sistema. Tratar valores de catálogo como universais é fonte clássica de erro.

## Características técnicas

| Parâmetro | Valores típicos |
| --- | --- |
| Tensão de saída | 12V / 24V / 48V |
| Corrente de carregamento | 10A / 20A / 30A / 60A / 100A |
| Entrada AC | 90–265V, 50/60Hz (bivolt universal) |
| Eficiência | 85–95% |
| Proteção IP | IP22 (interior seco) / IP65 (spray) |
| Saídas simultâneas | 1 / 2 / 3 bancos independentes |

**Tensões por tipo de bateria (sistema 12V):**

| Tipo | Absorption | Float | Equalização |
| --- | --- | --- | --- |
| AGM | Faixa típica conforme fabricante | Faixa típica conforme fabricante | Em geral não |
| GEL | Faixa típica conforme fabricante | Faixa típica conforme fabricante | Em geral não |
| Inundada (líquida) | Faixa típica conforme fabricante | Faixa típica conforme fabricante | Possível, quando o fabricante permitir |
| Lítio LFP | Faixa típica conforme fabricante/BMS | Muitas arquiteturas usam float reduzido ou sem float sustentado | Não |

**Dimensionamento — regra prática:**

- Corrente de carregamento = valor compatível com a química, o banco e o tempo disponível de recarga
- Banco 200Ah: carregador 20–50A
- Banco 400Ah: carregador 40–100A
- Corrente muito baixa pode alongar excessivamente a recarga e impedir absorção plena em chumbo
- Corrente alta sem coordenação térmica e de tensão reduz a vida útil e pode ativar proteções

## Configurações comuns

**Configuração 1 — Carregador dedicado simples (muito comum no Brasil):**

Victron Blue Smart 12V/30A ou similar → uma saída → banco de serviço. Conectado ao painel AC do cais via shore power.

**Configuração 2 — Multi-output (2 bancos independentes):**

Uma unidade com saídas independentes para banco de motor (start) e banco de serviço. Correntes e perfis diferentes para cada banco. Elimina a necessidade de dois carregadores separados.

**Configuração 3 — Inversor/Carregador integrado (mais presente em embarcações maiores/premium):**

Victron MultiPlus ou Mastervolt Combi. Quando há AC externo: carrega e alimenta cargas AC simultaneamente via transfer switch automático. Um equipamento faz tudo.

**Configuração 4 — Sistema híbrido solar + cais:**

MPPT solar carrega durante o dia; carregador AC carrega à noite e no cais. BMS coordena ambos em sistemas lítio para não sobrecarregar. Configuração ideal para embarcações com permanência fora do cais.

## Marcas e referências

**Premium (muito comum no Brasil e em barcos importados):**

- **Victron Energy** — Blue Smart IP65 (portátil), IP22 (fixo), Phoenix Charger, Skylla TG. Bluetooth integrado, app VictronConnect, configuração completa. Referência do mercado atual.
- **Mastervolt** — ChargeMaster, linha náutica completa, alta qualidade, presente em embarcações europeias
- **ProMariner** — ProNautic Series, muito difundido em embarcações americanas importadas
- **Xantrex** — TrueCharge 2, tradição em náutica norte-americana

**Intermediário:**

- **NOCO Genius** — excelente custo-benefício para manutenção e uso não permanente
- **CTEK** — popular para carregamento lento e manutenção de longa duração
- **Intelbras** — presente no mercado brasileiro para aplicações mais simples

**A evitar em instalações fixas náuticas:**

- Carregadores de carro genéricos (sem proteção para ambiente marinho)
- Carregadores de 2 estágios sem controle de temperatura
- Equipamentos sem especificação para uso contínuo e múltipla química

## Componentes relacionados

- **Banco de baterias:** receptor direto — compatibilidade de química e tensão é crítica
- **BMS (sistemas lítio):** autoriza ou interrompe carregamento; deve comunicar-se com o carregador
- **Shore power / transformador:** fonte AC de entrada do carregador
- **Gerador AC:** fonte AC alternativa quando fora do cais
- **Fusível DC (perto do banco):** proteção do circuito de saída do carregador, coordenada com o cabo
- **Monitor de bateria (BMV/SmartShunt):** monitora estado de carga independentemente
- **MPPT solar:** fonte DC complementar — ambos carregam o mesmo banco
- **Transfer switch:** chaveamento automático shore power / gerador → carregador

## Problemas mais frequentes

1. **Bateria nunca carrega 100% (estagna em 80–90%)** — absorption muito curta, tensão insuficiente, bateria sulfatada, célula defeituosa consumindo internamente
2. **Carregador não inicia carregamento** — tensão DC muito baixa (bateria excessivamente descarregada), fusível aberto, BMS desconectado, polaridade invertida
3. **Permanece em bulk indefinidamente** — corrente muito alta para banco pequeno, temperatura alta limitando via BMS, célula defeituosa com curto interno
4. **Superaquecimento do carregador** — ventilação inadequada, ambiente quente, ventilador interno com falha
5. **Sulfatação acelerada das baterias** — float prolongado com tensão alta, sem ciclo de equalização periódico em baterias inundadas
6. **Falha no carregamento de lítio** — BMS desconectou o banco por proteção de célula; carregador sem comunicação com BMS
7. **Ruído elétrico / interferência** — carregador mal filtrado introduz harmônicos no barramento DC

## Causas raiz

| Problema | Causa raiz real |
| --- | --- |
| Bateria morre prematuramente | Perfil errado configurado (ex: AGM em banco GEL) |
| Banco nunca chega a 100% | Absorption muito curta OU tensão de absorption abaixo do valor correto |
| Carregador queima precocemente | Ambiente quente sem ventilação + operação contínua 24h/7d |
| BMS desconecta durante carga | Célula fora dos limites de tensão — banco desequilibrado, não falha do carregador |
| Sulfatação acelerada | Carga cronicamente insuficiente, absorção curta, perfil inadequado ou operação prolongada sem completar recarga |

## Diagnóstico prático

**Passo 1 — Acompanhar as fases com multímetro:**

- Conectar ao shore power, medir tensão DC na bateria a cada 15 minutos
- Bulk: tensão sobe progressivamente, corrente máxima
- Absorption: tensão estável (~14,4V AGM), corrente caindo
- Float: tensão cai para ~13,6V, corrente mínima
- Se ficar preso em uma fase: diagnóstico necessário

**Passo 2 — Verificar tensão de saída do carregador:**

- Medir nos terminais DC do próprio carregador (não na bateria)
- Diferença > 0,3V entre carregador e bateria = queda excessiva no cabeamento (cabo fino ou conexão oxidada)

**Passo 3 — Via Bluetooth (Victron):**

- App VictronConnect → histórico completo de tensão, corrente e fases
- Verificar: tensão mínima atingida, tempo em absorption, erros registrados, temperatura de compensação

**Passo 4 — Eficiência:**

- Medir potência AC de entrada (wattímetro AC)
- Medir potência DC de saída (V × A)
- Eficiência = Pdc / Pac × 100%
- Carregadores bons: > 90%

**Ferramenta mínima:** multímetro digital, app VictronConnect (se Victron).

## Boas práticas profissionais

- Selecionar perfil de carga **exatamente** correspondente ao tipo de bateria instalada — nunca usar perfil genérico
- Usar sonda de temperatura para compensação — variação de 30°C altera a tensão ideal em ~0,6V
- Dimensionar para 10–20% da capacidade do banco (equilíbrio entre tempo de carga e saúde da bateria)
- Instalar proteção DC o mais próximo possível da fonte conforme a topologia e a norma aplicável
- Instalar em local ventilado, longe de fontes de calor e respingos
- Garantir comunicação entre carregador e BMS em sistemas lítio (CANBUS ou configuração de tensão correta)
- Aplicar equalização somente quando a bateria inundada e o fabricante permitirem, e dentro do intervalo recomendado
- Documentar: data de instalação, perfil configurado, corrente nominal
- Inspecionar conexões DC a cada 6 meses — oxidação = resistência = calor = falha

## Cuidados de instalação

- Cabo DC calibrado para a corrente máxima do carregador + 25% de margem
- Comprimento mínimo possível no cabo DC (queda de tensão máxima 3%)
- Fusível DC tipo ANL ou maxi-fuse a < 30cm do banco positivo
- Carregador fixado em superfície firme com folga mínima de 10cm em todos os lados para ventilação
- Nunca instalar próximo a baterias de chumbo-ácido inundadas — gases emitidos corroem componentes eletrônicos
- Cabo de entrada AC protegido por disjuntor no painel AC (10–16A conforme a potência)
- Sonda de temperatura instalada próxima ao centro do banco (não no terminal)

## Cuidados de uso

- Nunca conectar o barco ao cais sem verificar polaridade do shore power primeiro (risco de dano e corrosão galvânica)
- Ao trocar o banco de baterias, reconfigurar o perfil do carregador para a nova química
- Não operar outros equipamentos de alta corrente simultaneamente ao carregador se o cais tiver capacidade limitada
- Em saídas longas sem cais, planejar gerador AC ou painel solar complementar

## Erros comuns de instaladores

- **Configurar perfil errado** (ex: inundada para banco AGM) → sobretensão progressiva → bateria seca prematuramente em 12–18 meses
- **Subdimensionar a corrente** — carregador de 10A para banco de 400Ah → absorption nunca completa → bateria estagna em 80%
- **Sem sonda de temperatura** — em climas quentes (verão brasileiro, casa de máquinas), tensão ideal é menor que a tensão nominal programada → supercarregamento em dias quentes
- **Sem fusível DC** — em curto-circuito, o cabo pega fogo antes de qualquer proteção atuar
- **Ignorar compatibilidade com lítio** — carregador programado para AGM pode não ter protocolo correto para LFP, especialmente sem comunicação BMS
- **Instalar sem ventilação** — vida útil reduzida drasticamente em ambiente confinado e quente
- **Usar carregador de carro** em instalação fixa náutica — sem proteção contra umidade, vibração e maresia

## Relação com outros sistemas

- **Banco de Baterias:** receptor direto — química e tensão devem ser perfeitamente compatíveis
- **BMS (lítio):** controla permissão de carregamento; falha de comunicação = banco não carrega sem razão aparente
- **CAIS (Pier) (AC) / Transformador de Isolamento:** fonte AC primária do carregador
- **Gerador AC:** fonte AC alternativa quando fora do cais — carregador trabalha da mesma forma
- **Inversor/Carregador:** frequentemente substitui o carregador dedicado em instalações modernas
- **MPPT Solar:** fonte DC complementar — ambos carregam o banco, não interferem entre si em sistemas bem projetados
- **Monitor de bateria (BMV/SmartShunt):** verifica o estado real do banco independentemente do carregador
- **Painel AC:** distribuição AC da embarcação que alimenta o carregador — proteção pelo disjuntor AC

## Brasil x Internacional

| Aspecto | Brasil | Internacional (ABYC/Europa) |
| --- | --- | --- |
| Marca dominante | Victron (crescendo) + genéricos | Victron / Mastervolt / ProMariner |
| Perfil configurado | Frequentemente genérico ou incorreto | Configurado conforme a ficha técnica da bateria |
| Fusível DC | Frequentemente ausente | Exigido por ABYC E-11 (2023) |
| Sonda de temperatura | Raramente usada | Padrão em instalações profissionais |
| Compatibilidade lítio | Em evolução rápida | Bem documentada, comunicação BMS estabelecida |
| Inversor/Carregador | Crescendo mas ainda não dominante | Padrão em embarcações europeias acima de 35 pés |

**Realidade brasileira:** muitas embarcações ainda operam com carregadores simples de 2 estágios ou carregadores de carro adaptados. A evolução para sistemas multietapas com Victron está crescendo rapidamente, especialmente com a chegada de iates europeus usados e a influência de técnicos capacitados.

## Glossário rápido

- **Carregador de bateria (AC→DC)** — conversor inteligente que transforma AC do cais/gerador em DC regulado para recarga.
- **Retificador** — conversor AC→DC simples, sem controle de perfil; não é carregador profissional.
- **Carregador on/off** — tipo antigo, desliga ao atingir corte; obsoleto em uso náutico.
- **Carregador multietapas (3-4 stages)** — padrão atual: bulk → absorção → float → (equalização).
- **Bulk** — primeira fase, corrente constante máxima, tensão sobe progressivamente (0 % → ~80 %).
- **Absorção (absorption / CV)** — tensão constante, corrente cai à medida que banco se aproxima de 100 %.
- **Float / flutuação** — tensão reduzida de manutenção, compensa consumos de standby.
- **Equalização** — tensão extra-alta (~15,5 V) para dessulfatar FLA; **proibida em AGM, GEL, LFP**.
- **Perfil de carga** — conjunto de parâmetros: tensão de bulk, absorção, float, tempo de absorção, corrente.
- **Compensação de temperatura** — sonda no centro do banco ajusta tensão ideal (-3 mV/°C/célula chumbo).
- **Curva V × I** — gráfico de tensão e corrente ao longo do ciclo de carga.
- **C-rate** — corrente como múltiplo da capacidade. 0,1C = 10 A em banco 100 Ah.
- **Corrente nominal do carregador** — saída máxima em Amperes a 12/24/48 V.
- **Dimensionamento 10-30 %** — regra prática: carregador = 10-30 % da capacidade Ah do banco.
- **Eficiência round-trip** — Pdc/Pac; carregadores bons > 90 %.
- **Fator de potência (PF)** — razão entre potência ativa e aparente; PFC ativo é padrão atual.
- **Harmônicos** — deformação da onda AC de entrada causada pelo carregador; limite por norma.
- **Shore power** — alimentação AC do cais na marina.
- **Transfer switch / MTS / ATS** — chave que alterna entre shore e gerador; manual ou automática.
- **Inversor/carregador combo** — equipamento único (Victron MultiPlus/Quattro, Mastervolt Combi, Magnum) que carrega no shore e inverte da bateria.
- **DC-DC charger (B2B)** — não é AC→DC; carrega banco de serviço a partir do alternador ou outro banco; relevante em LFP.
- **Sonda de temperatura** — NTC que mede temperatura do banco e envia ao carregador.
- **Sense wire** — cabo de realimentação que mede tensão no próprio terminal da bateria (não do carregador).
- **Isolamento galvânico** — transformador separa rede do cais do banco; evita corrosão galvânica.
- **IP22 / IP65 / IP67** — classes de proteção contra poeira e água; IP22 para interior seco, IP65 para respingo.
- **PFC ativo** — correção de fator de potência por circuito eletrônico; padrão em carregador moderno.
- **Resonant / LLC / PSFB** — topologias de conversão de potência em carregadores modernos.
- **BMS comm (VE.Bus / CAN / NMEA 2000)** — comunicação obrigatória em lítio: carregador respeita limites dinâmicos.
- **Float drop / voltage drop** — queda de tensão entre carregador e bateria; > 0,3 V = cabo subdimensionado.
- **Bulk hours / absorption hours** — tempo acumulado em cada fase; base para diagnóstico.
- **Tail current** — corrente que define transição de absorção para float (~2-4 % da corrente de bulk).
- **Equalization schedule** — cronograma (a cada 30-60 dias) para FLA; ignorado em seladas.
- **Fusível DC de saída** — proteção entre carregador e banco; ≤ 178 mm do positivo, AIC compatível.
- **AIC (Ampere Interrupting Capacity)** — capacidade do fusível de cortar a Isc do banco.
- **Storage mode / standby** — modo de manutenção do banco sem carga ativa; consumo mínimo.
- **Nuisance trip** — desligamento do carregador por proteção sem falha real; sintoma comum.
- **Reverse polarity protection** — proteção contra inversão de polaridade nos terminais DC.
- **Reverse current protection** — proteção contra retorno de corrente do banco para o carregador desligado.
- **ESD (Electric Shock Drowning)** — risco em marinas de água doce; carregador integra cadeia AC.
- **Corrosão galvânica** — degradação de metal por corrente DC entre embarcações via PE comum.

## Normas e referências técnicas

- **ABYC E-11 (2023)** — AC and DC Electrical Systems on Boats: requisitos para carregadores, proteção, localização do fusível DC, bitolagem.
- **ABYC A-31 (2024)** — Battery Chargers and Inverters: padrão específico do ABYC consolidado em edição 2024; define teste, identificação e instalação de carregadores e inversores/carregadores marítimos. *(Nota: em edições anteriores a numeração ABYC sofreu realocações; confirmar edição vigente no momento do laudo.)*
- **ABYC E-13 (2023)** — Lithium Ion Batteries: relevante quando carregador alimenta banco LFP.
- **ABYC E-10 (2023)** — Storage Batteries: separação de bancos, fusível, ventilação.
- **ABYC A-28 (2023)** — Galvanic Isolators: interface entre shore power e embarcação.
- **ISO 13297:2020** — Electrical systems on recreational craft AC e DC.
- **ISO 8846:2022** — Protection against ignition of surrounding flammable gases: ignition protection em ambiente motor/banco.
- **IEC 60335-2-29** — Safety of battery chargers: base normativa do equipamento.
- **IEC 62040-1** — Uninterruptible Power Systems: conceitos aplicáveis ao inversor/carregador.
- **UL 1236** — Battery chargers for engine-starter batteries: referência americana para carregador de partida.
- **UL 458** — Power converters/inverters for marine use: inversor/carregador certificado para náutica.
- **NMEA 2000 (IEC 61162-3)** — Comunicação com BMS, MFD, monitor em redes modernas.
- **ABNT NBR 5410 (2004 + emendas)** — Base brasileira para AC de baixa tensão; aplicável ao circuito AC que alimenta o carregador.
- **NORMAM-211/DPC** — Exigências administrativas e de segurança da autoridade marítima brasileira.
- **Compatibilidade com lítio** — nem sempre normatizada explicitamente; responsabilidade do instalador alinhar carregador, BMS e datasheet da célula; registrar na pasta técnica da embarcação.

## Como ensinar este tópico

**Progressão recomendada:**

1. Mostrar o problema: banco descarregado → necessidade de repor energia
2. Comparar: carregador simples vs multietapas — curva de V × I no tempo
3. Tabela de tensões por tipo de bateria — "cada química tem sua janela"
4. Demonstração: configurar Victron Blue Smart para AGM vs GEL — diferença nas tensões
5. Caso prático: diagnóstico de banco que nunca chega a 100%
6. Integração: carregador + MPPT solar + inversor como sistema unificado

**Onde inserir no material:**

- Logo após banco de baterias (o carregador serve o banco)
- Antes de inversora (complementa a lógica shore power → carga → descarga → recarga)
- Conectar com: Shore Power (fonte AC), Lítio/AGM (compatibilidade), Monitor de bateria (verificação)

## Ideias de vídeos e aulas práticas

- **"Carregador de bateria náutico: como funciona cada fase"** — gráfico de V × I em tempo real durante ciclo completo
- **"Como configurar o perfil correto para sua bateria"** — demo no VictronConnect, mostrando diferença AGM vs GEL vs Lítio
- **"Bateria que nunca carrega 100%: como diagnosticar"** — análise das fases com multímetro
- **"Carregador dedicado vs Inversor/Carregador: qual escolher?"** — comparativo prático com custo-benefício
- **"Erros que matam sua bateria: supercarregamento e subcarregamento"** — explicação visual das curvas

## Diagramas sugeridos

- **Gráfico V × I durante ciclo completo de carga** — AGM vs Lítio (linhas sobrepostas para comparação)
- **Esquema elétrico:** shore power → painel AC → disjuntor → carregador → fusível DC → banco de baterias → barramento DC
- **Diagrama de sistema híbrido:** MPPT solar + carregador AC → banco → BMS → inversor
- **Tabela visual** de tensões por tipo de bateria (bulk, absorption, float, equalização)
- **Fluxograma de diagnóstico:** banco não carrega → checklist sequencial

## FAQ

**Posso usar um carregador de carro na minha embarcação?**

Não para instalação fixa. Carregadores automotivos não têm proteção contra maresia, não são projetados para operação contínua, e raramente têm perfis adequados para AGM ou lítio náutico. Use apenas em emergência e substitua por equipamento náutico adequado.

**Qual a diferença entre carregador e inversor/carregador?**

O carregador só converte AC→DC (carrega o banco). O inversor/carregador também converte DC→AC (alimenta cargas AC com a bateria). O inversor/carregador substitui ambos com a vantagem do transfer switch automático — quando há AC externo, usa o cais e carrega; sem AC, inverte da bateria.

**Preciso desligar o carregador quando for navegar?**

Sim, o carregador deve ser desconectado do shore power antes de lançar. O transfer switch automático (presente nos inversores/carregadores) faz isso automaticamente.

**Por que meu carregador fica em absorption horas e horas sem passar para float?**

Pode ser banco muito descarregado (demorou muito para subir ao longo da bulk), corrente de carregamento baixa demais para o banco, célula defeituosa com resistência alta, ou temperatura muito alta limitando o processo via BMS. Verifique a corrente real com alicate amperímetro.

**Carregador com Bluetooth vale o custo extra?**

Sim para uso profissional. O histórico de carregamento no app revela problemas que passariam despercebidos — tensão mínima atingida, tempo em cada fase, erros registrados. Victron Blue Smart é a referência com melhor custo-benefício atualmente.

## Integração com outras notas

- [[Bancos de Bateria]]
- [[CAIS (Pier) (AC)]]
- [[Monitor de Bateria / BMV / Shunt]]
- [[Tipos de Bateria]]
- [[BMS — Battery Management System]]
- [[Gerador (AC)]]
- [[Inversora (DC To AC)]]
- [[Lítio LiFePO4 — Instalação e Cuidados Específicos]]
- [[Carregador Elétrico para Tender e Jet Ski]]

## Perguntas que esta nota responde

- O que é Carregador de Bateria (AC To DC) em instalações elétricas náuticas?
- Qual é a função de Carregador de Bateria (AC To DC) na embarcação?
