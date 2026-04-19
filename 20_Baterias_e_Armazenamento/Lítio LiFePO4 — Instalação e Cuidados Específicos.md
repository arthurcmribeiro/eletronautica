---
title: "Lítio LiFePO4 — Instalação e Cuidados Específicos"
note_type: "technical-note"
domain: "20_Baterias_e_Armazenamento"
source_file: "LÍTIO LiFePO4 — INSTALAÇÃO E CUIDADOS ESPECÍFICOS 33a19734f7fb8100a5ade14e95f2692c.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "11"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction: "Brasil"
normas_citadas:
  - "ABYC E-13 (2023) — Lithium Ion Batteries"
  - "ABYC E-11 (2023) — AC and DC Electrical Systems on Boats"
  - "ABYC E-10 (2023) — Storage Batteries"
  - "IEC 62619:2022 — Safety requirements for secondary lithium batteries (industrial)"
  - "IEC 62620:2014 — Secondary lithium cells for industrial applications"
  - "IEC 63056:2020 — Lithium batteries in electrical energy storage systems"
  - "UL 1973:2022 — Batteries for stationary, vehicle auxiliary, and light electric rail"
  - "UL 9540A — Thermal runaway fire propagation test"
  - "UL 2580 — Batteries for electric vehicles"
  - "UN 38.3 — Transporte aéreo/marítimo de baterias lítio"
  - "SAE J2464 — Electric vehicle REESS safety and abuse testing"
  - "ISO 13297:2020 — Small craft — AC and DC installations"
  - "ISO 16315:2016 — Small craft — Electric propulsion system"
  - "NBR 5410:2004 — Instalações elétricas de baixa tensão"
  - "NORMAM-211/DPC — Embarcações de esporte e recreio"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://abycinc.org/news/standardsupdatewebinar/"
  - "https://www.iso.org/standard/56180.html"
  - "https://www.iec.ch/"
  - "https://www.ul.com/"
aliases:
  - "LÍTIO LiFePO4 — INSTALAÇÃO E CUIDADOS ESPECÍFICOS"
seo_title: "Lítio LiFePO4 — Instalação e Cuidados Específicos"
seo_description: "LiFePO4 é uma química de lítio amplamente usada em náutica por oferecer boa vida cíclica, alta eficiência e baixo peso, desde que instalada com BMS, proteção contra sobrecorrente e estratégia correta de carga por alternador, carregador e inversor."
seo_keywords:
  - "Lítio"
  - "LiFePO4"
  - "Instalação"
  - "Cuidados"
  - "Específicos"
  - "20 Baterias e Armazenamento"
geo_queries:
  - "O que é Lítio LiFePO4 — Instalação e Cuidados Específicos em instalações elétricas náuticas?"
related_notes:
  - "Alternador (DC)"
  - "Bancos de Bateria"
  - "BMS — Battery Management System"
  - "Inversora (DC To AC)"
  - "Carregador de Bateria (AC To DC)"
  - "Monitor de Bateria / BMV / Shunt"
  - "Tipos de Bateria"
---

# Lítio LiFePO4 — Instalação e Cuidados Específicos

> [!abstract] Resumo técnico
> LiFePO4 é uma química de lítio tecnicamente atraente para náutica por combinar boa vida cíclica, alta eficiência e massa reduzida. Em compensação, exige BMS, proteção contra sobrecorrente e coordenação cuidadosa com alternador, carregadores, inversores e estratégia de desligamento.

> [!tip] Regra de decisão em 30 segundos
> 1. **LiFePO4 não é "AGM melhorada". É sistema diferente — exige BMS, carregador específico, cabeamento redimensionado, alternador com regulador externo ou DC-DC, fusível com AIC adequado à Isc do lítio.**
> 2. **Nunca troque chumbo → lítio "1 por 1".** Retrofit é reprojeto; exige projeto elétrico assinado com ART/CREA, datasheet da célula, configuração do BMS e registro na pasta técnica da embarcação.
> 3. **BMS é requisito, não acessório.** ABYC E-13 (2023) e IEC 62619:2022 não abrem exceção — bateria LiFePO4 sem BMS certificado não é instalação; é acúmulo de risco.
> 4. **Não carregue LiFePO4 abaixo de 0 °C.** Deposição de lítio metálico é irreversível e gera risco de curto interno + thermal event. BMS bloqueia por projeto; a solução é aquecedor de célula, não bypass.
> 5. **Fusível ≤ 178 mm do terminal positivo** com AIC suficiente para a Isc do banco (pode ultrapassar 10 kA). Fusível automotivo blade 32 V não é adequado — usar Class T, MRBF ou ANL marítimo.
> 6. **Alternador sem regulador externo programável não serve** — banco lítio de baixa impedância aceita toda a corrente que o alternador puder dar, supera regime térmico e queima em poucos minutos. DC-DC charger é solução simples para separar domínios.
> 7. **Carregador de AGM/GEL em lítio = dano garantido.** Perfil de 3 estágios com equalização é incompatível. Reconfigurar para perfil LiFePO4 ou trocar carregador.
> 8. **Nunca misture LiFePO4 com chumbo no mesmo banco.** Curvas de tensão incompatíveis — chumbo puxa lítio para baixo, lítio sobrecarrega chumbo. Bancos separados, com isolador ou DC-DC charger coordenando.
> 9. **Documente data de instalação, lote das células, parâmetros configurados no BMS e histórico de ciclos.** Sem esse registro, laudo em caso de sinistro fica impossível e garantia normalmente invalidada.

> [!danger] Quando chamar um especialista
> - **Retrofit de AGM/GEL para LiFePO4 em embarcação existente.** Exige projeto integrado: reavaliar alternador (regulador externo ou DC-DC), carregador (perfil LiFePO4), BMS (compatibilidade com inversor/carregador), fusível (AIC), bitola de cabo (Isc do lítio), ventilação (calor de balanceamento), topologia de aterramento e documentação. ART/CREA obrigatório.
> - **Banco DIY com células prismáticas soltas (CATL, EVE, Winston).** Montagem exige busbar com aperto por torquímetro, teste de capacidade inicial célula-a-célula, topbalance com fonte de bancada, validação do BMS contra datasheet da célula, registro fotográfico e de parâmetros. Não é projeto de fim de semana — é fabricação de bateria.
> - **"Puff event", inchamento ou venting em célula LiFePO4.** Isolar, ventilar, **não apagar com água sem checar fabricante**, acionar seguradora, laudo pericial com ART/CREA. Preservar célula, BMS e registros para análise — não descartar antes da perícia.
> - **Eletropropulsão com bancos > 10 kWh, 48 V, 96 V ou 400 V.** ISO 16315:2016 + IEC 62619/62620 + ABYC E-30 (draft) como base; exige interlock, contatores, pré-carga, detecção de ground fault, cooling, E-stop.
> - **Importação de barco com bateria LiFePO4 instalada por estaleiro estrangeiro.** Verificar certificação UL/IEC, compatibilidade do BMS com rede de bordo brasileira, manual em português, treinamento do operador, plano de emergência. Não basta "estava funcionando lá fora".
> - **Alternador do motor aceitando LiFePO4 sem regulador externo** — risco térmico iminente. Não use o sistema até ter regulador programável (Balmar, Wakespeed WS500) ou DC-DC charger (Victron Orion-Tr Smart, Sterling) dimensionado.
> - **BMS disparando frequentemente sem padrão identificado.** Célula com falha interna, temperatura oculta, carregador mal configurado, cabo subdimensionado ou BMS defeituoso — diagnóstico com app, multímetro, termômetro IR e registro de parâmetros.
> - **Carregador solar MPPT, shore charger, inversor/carregador sem configuração explícita para LiFePO4.** Configure antes de qualquer ciclo — não confie em "autodetect" de química.
> - **Laudo pericial após sinistro** (incêndio, inchamento, curto em banco lítio). Responsável técnico com ART/CREA, reconstituição causal, fotos, registros do BMS e monitor, conclusão sobre causa raiz e nexo.

## O que é

LiFePO4 (Lithium Iron Phosphate — Fosfato de Lítio e Ferro) é uma química de bateria recarregável da família dos íons de lítio, desenvolvida com foco em segurança e ciclos de vida elevados. Diferentemente do chumbo-ácido, o LiFePO4 mantém tensão estável durante quase toda a descarga, tem maior eficiência de carga/descarga, menor peso e maior número de ciclos — ao custo de maior preço inicial e necessidade obrigatória de BMS.

## Comparação LiFePO4 vs AGM (chumbo-ácido)

| Característica | AGM 100Ah | LiFePO4 100Ah |
| --- | --- | --- |
| Tensão nominal | 12V | 12,8V (4 células × 3,2V) |
| Peso | ~28–30 kg | ~12–14 kg |
| DOD máximo seguro | 50% | 80% |
| Capacidade útil real | 50Ah | 80Ah |
| Ciclos de vida (DOD 50/80%) | 400–600 | 2.000–5.000 |
| Eficiência de carga (roundtrip) | 80–85% | 95–98% |
| Corrente de carga máxima | 0,25C (25A/100Ah) | 0,5–1C (50–100A/100Ah) |
| Tempo de carga completa | 8–12h | 2–3h (1C) |
| Autodescarga/mês | 3–5% | < 2% |
| Tolerância a sobretensão | Moderada | Baixa (precisa de BMS) |
| Segurança sem BMS | Razoável | Perigoso |
| Preço (100Ah 12V) | R$500–800 | R$2.000–4.000 |

## Por que a tensão importa mais no LiFePO4

**Curva de descarga:**

- AGM: tensão cai progressivamente de 12,7V (100%) até 11,5V (0%) — curva inclinada
- LiFePO4: tensão permanece em ~13,2V de 90% a 20% e só cai nas extremidades — curva plana

**Impacto prático:**

Com LiFePO4, equipamentos recebem tensão estável por quase toda a autonomia. Com AGM, a tensão cai progressivamente — alguns equipamentos falham antes de o banco estar realmente vazio.

**O problema para o carregador:**

A curva plana também significa que a leitura por tensão é menos intuitiva e que o carregador precisa ser configurado para a química instalada. Muitos bancos LiFePO4 trabalham bem em faixas como 14,2–14,4 V, outros admitem valores diferentes. O ponto correto vem do fabricante da bateria e do BMS, não de um único número universal.

## Parâmetros de carga corretos

| Parâmetro | LiFePO4 4S (12V) |
| --- | --- |
| Tensão de absorção (bulk/CV) | 14,2–14,6V |
| Tensão de flutuação (float) | 13,5V (ou sem float — desconectar) |
| Tensão de corte de descarga | 11,5–12,0V (10,0V no limite absoluto) |
| C-rate de carga máxima | 0,5C–1C (50–100A para 100Ah) |
| Temperatura de carga | 0°C a 45°C (não carregar abaixo de 0°C sem aquecedor) |

**Alternadores e LiFePO4:**

Nem todo alternador automotivo ou marítimo original suporta bem um banco LiFePO4 de baixa impedância sem controle adicional. O risco principal é o banco aceitar corrente elevada por tempo prolongado, levando o alternador a operar fora do regime térmico previsto. A solução depende da arquitetura:

- Regulador externo com limitação/configuração apropriada
- DC-DC charger entre alternador e banco de lítio quando a arquitetura pedir desacoplamento
- Limitação de campo/corrente e integração com o BMS em sistemas mais completos

## Como aparece na prática

- Baterias prontas com case (Battle Born, Victron, SOK, Epoch, Ampere Time)
- Bancos DIY com células prismáticas (CATL, EVE) + BMS externo
- Instalação como substituição direta de AGM (verificar compatibilidade do carregador)
- Bancos de 100Ah, 200Ah, 300Ah como módulos empilháveis

## Células prismáticas vs cilíndricas

**Prismáticas (padrão náutico):**

- Formato retangular, mais fáceis de empacotar
- Capacidades maiores por célula (50–280Ah típico)
- LiFePO4 é quase exclusivamente prismático em náutica

**Cilíndricas (18650, 21700):**

- Formato de pilha — usadas em baterias de laptops, e-bikes
- Menos comuns em náutica (configuração complexa para alta capacidade)
- Tesla, e-bikes e ferramentas elétricas usam este formato

## Segurança: LiFePO4 vs outras químicas de lítio

| Química | Energia específica | Segurança | Uso náutico |
| --- | --- | --- | --- |
| LiFePO4 | Menor | **Mais segura** (sem thermal runaway) | Padrão recomendado |
| NMC (Lítio Manganês Cobalto) | Maior | Menor — risco de fogo em abuso | Baterias de ferramentas, e-veículos |
| NCA (Lítio Níquel Cobalto Alumínio) | Maior | Menor | Tesla (veículos) |
| LTO (Lítio Titanato) | Menor | Muito segura | Alta performance industrial |

**LiFePO4 tem estabilidade térmica superior a outras químicas de lítio**, mas isso não significa risco zero. Ainda pode haver aquecimento anormal, venting, dano interno e evento perigoso em caso de sobrecarga, curto, esmagamento ou falha severa de instalação. A vantagem real é a janela de segurança maior, não imunidade a falhas.

## Marcas e referências

**Baterias prontas (plug-and-play com BMS integrado):**

- **Battle Born** (EUA) — 100Ah, 200Ah, 10 anos de garantia, referência americana
- **Victron Smart Lithium** — integração perfeita com ecossistema Victron
- **Epoch** (EUA) — excelente custo-benefício, Bluetooth nativo
- **SOK Battery** — boa qualidade, preço acessível, popular em DIY
- **Ampere Time** (Litime) — opção econômica, menor garantia

**Células para bancos DIY:**

- **CATL (China)** — maior fabricante do mundo, células de altíssima qualidade
- **EVE Energy** — segunda opção de referência em células prismáticas
- **Winston Battery** — referência em células LTO

## Problemas mais frequentes

| Problema | Causa | Diagnóstico/Solução |
| --- | --- | --- |
| Banco não carrega completamente | Carregador com tensão inadequada (< 14,2V) | Reconfigurar carregador para LiFePO4 |
| BMS desconectando frequentemente | Desbalanceamento de células | Verificar tensão por célula via app |
| Alternador superaquecendo | LiFePO4 não limita a corrente do alternador | Instalar regulador externo ou DC-DC charger |
| Banco não carrega em tempo frio | BMS bloqueando carga abaixo de 0°C | Instalar aquecedor de bateria |
| Expansão/inchaço de célula | Sobrecarga ou curto-circuito interno | Substituir célula, verificar BMS |

## Boas práticas profissionais

- Verificar compatibilidade de TODAS as fontes de carga antes da instalação (alternador, shore power, solar, inversor/carregador)
- Instalar BMS de qualidade — é a proteção da bateria cara
- Usar comunicação BMS-carregador quando possível (VE.Bus, CAN bus)
- Não misturar LiFePO4 com chumbo-ácido no mesmo banco
- Documentar claramente a instalação — LiFePO4 tem parâmetros distintos do chumbo

## Erros comuns

**Usar carregador de chumbo-ácido sem adaptar:**

O risco não é apenas "ser de chumbo" ou "ser de lítio". O problema é usar um perfil sem validar tensões, tempos de absorção, comportamento de float e coordenação com o BMS. Alguns carregadores programáveis servem bem ao LiFePO4; outros não.

**Conectar em paralelo com banco de chumbo-ácido:**

Química incompatível. O banco de chumbo vai tentar "puxar" o lítio para sua tensão mais baixa durante a descarga — causa estresse em ambos.

**Esperar que o BMS "se vire" sem monitoramento:**

O BMS protege, mas não informa sem monitoramento. Banco com célula desbalanceada acumula problema silenciosamente — BMS passa a desligar cada vez mais frequentemente até falha total.

**Instalar sem ventilação adequada:**

LiFePO4 não gera H₂ como o chumbo — mas gera calor em cargas altas. Ventilação mínima para evitar acúmulo de temperatura.

## Relação com outros sistemas

- **BMS:** obrigatório, não opcional
- **Monitor de bateria:** configurar para LiFePO4 (DOD 80%, eficiência 97%, Peukert 1.05)
- **Alternador:** precisa ser avaliado quanto à corrente contínua suportável, estratégia de limitação e coordenação com o BMS
- **Carregador de bateria:** deve ser certificado ou configurado para LiFePO4
- **Inversor/carregador Victron:** configuração específica para LiFePO4 via VE.Bus

## Glossário rápido

- **LiFePO4 (Lithium Iron Phosphate)** — química de lítio com cátodo de fosfato de ferro; 3,2 V nominais por célula; padrão náutico atual.
- **LFP** — abreviação comercial de LiFePO4.
- **NMC (Nickel Manganese Cobalt)** — química lítio de maior densidade; menos estável; uso em automotivo, raro em náutica.
- **NCA, LCO, LMO, LTO** — outras químicas lítio, mais raras em náutica recreativa.
- **Célula prismática** — formato retangular, capacidades de 50-280 Ah; padrão em packs náuticos.
- **Célula cilíndrica (18650, 21700)** — formato de pilha, usado em laptops, Tesla, e-bikes; pouco comum em náutica por exigir muitas unidades em paralelo.
- **4S, 8S, 16S** — 4/8/16 células em série (12 V / 24 V / 48 V nominais).
- **4S2P, 8S4P** — configurações série-paralelo para aumentar capacidade do pack.
- **Tensão nominal** — 3,2 V/célula em LiFePO4; 12,8 V em 4S.
- **Tensão de absorção (bulk/CV)** — 14,2-14,6 V em 4S; alto nível de carga.
- **Tensão de flutuação (float)** — 13,5 V ou carregador desconectado; LiFePO4 não precisa de float contínuo.
- **Tensão de corte de descarga** — 2,5-2,8 V/célula; BMS desconecta.
- **DoD (Depth of Discharge)** — 80-90 % seguro em LiFePO4; muito maior que chumbo.
- **SoC (State of Charge)** — percentual de carga; leitura por tensão é pouco confiável (curva plana) — usar shunt.
- **SoH (State of Health)** — percentual de capacidade remanescente; cai com ciclos e tempo.
- **C-rate** — múltiplos da capacidade: 1C em 100 Ah = 100 A. LiFePO4 tolera 0,5C-1C em carga.
- **Curva plana de tensão** — tensão permanece em ~13,2 V de 90 % a 20 %; vantagem para equipamentos, desafio para medição.
- **BMS (Battery Management System)** — obrigatório; monitora célula, protege, balanceia.
- **BMS integrado** — dentro do case (Battle Born, Victron Smart Lithium).
- **BMS externo** — módulo separado para bancos DIY com células soltas.
- **Balanceamento passivo / ativo** — passivo dissipa, ativo transfere.
- **Topbalance** — equalização inicial das células antes do primeiro uso.
- **Ciclo** — uma descarga + recarga; LiFePO4: 2.000-5.000 ciclos a 80 % DoD.
- **Eficiência round-trip** — energia recuperada / energia armazenada; LiFePO4 95-98 %, AGM 80-85 %.
- **Autodescarga** — perda natural em repouso; LiFePO4 < 2 % ao mês.
- **Temperatura de carga** — 0 °C a 45 °C. Carregar abaixo de 0 °C deposita lítio metálico (dano permanente).
- **Aquecedor de bateria** — acessório que permite operar lítio em climas frios; comando pelo BMS.
- **Venting** — liberação de gás por válvula de alívio; indica dano irreversível.
- **Thermal runaway** — reação exotérmica em cadeia; LiFePO4 resiste melhor que NMC, mas não é imune.
- **Regulador externo programável** — Balmar MC-614, Wakespeed WS500; controla campo do alternador para proteger banco lítio.
- **DC-DC charger** — conversor isolado entre alternador e banco lítio; desacopla domínios (Victron Orion-Tr Smart, Sterling BB1260).
- **Fusível Class T** — fusível de alta AIC (20-100 kA) para banco lítio grande.
- **MRBF (Marine Rated Battery Fuse)** — fusível parafusado no terminal positivo; 30-300 A.
- **ANL fuse** — fusível em barramento; 35-750 A.
- **AIC (Ampere Interrupting Capacity)** — capacidade do fusível de interromper a Isc.
- **Isc (corrente de curto-circuito)** — em LiFePO4 pode ultrapassar 10 kA no banco nu.
- **Pré-carga (precharge)** — resistor que limita inrush ao conectar inversor; evita corte espúrio.
- **E-stop / interlock** — botão de emergência que comanda BMS a abrir contator.
- **Ground fault detection** — em bancos isolados de 48 V+ detecta fuga à massa.
- **VE.Bus / VE.Can** — protocolos Victron para integração BMS-inversor-carregador.
- **CAN bus / NMEA 2000** — protocolos padronizados para comunicação BMS com sistema.
- **UN 38.3** — requisito de transporte (importação); sem este certificado, a bateria não pode voar nem viajar por mar.
- **Drop-in replacement** — bateria lítio com case, BMS e terminais compatíveis com AGM equivalente; pronta para "trocar 1 por 1" — **mas ainda requer reconfigurar carregador, alternador e fusível.**

## Normas aplicáveis

- **ABYC E-13 (2023) — Lithium Ion Batteries** — referência mais completa; trata BMS, instalação, ensaios, ventilação, proteção mecânica, desligamento de emergência.
- **ABYC E-11 (2023)** — regra do fusível ≤ 178 mm do terminal positivo, proteção de cabo, bitolagem, cores.
- **ABYC E-10 (2023)** — storage batteries; separação de bancos, ventilação, fixação.
- **IEC 62619:2022** — Safety requirements for secondary lithium cells and batteries (industrial); referenciada em datasheets de células importadas.
- **IEC 62620:2014** — Desempenho e durabilidade de packs lítio industriais.
- **IEC 63056:2020** — Baterias lítio em sistemas de armazenamento de energia (BESS).
- **UL 1973:2022** — Ensaio de segurança de pack completo (estacionário/auxiliar/light rail).
- **UL 9540A** — Thermal runaway fire propagation; relevante em packs múltiplos.
- **UL 2580** — Baterias para veículos elétricos; base para eletropropulsão.
- **UN 38.3** — transporte aéreo/marítimo; obrigatório para importação.
- **SAE J2464** — Ensaios de segurança e abuso para REESS (Rechargeable Energy Storage System) em veículos elétricos.
- **ISO 13297:2020** — AC e DC em pequenas embarcações.
- **ISO 16315:2016** — Sistemas de propulsão elétrica; base para projetos > 10 kWh.
- **NBR 5410:2004** — Base brasileira AC; aplicável após shore inlet.
- **NORMAM-211/DPC** — Exigências administrativas e de segurança da autoridade marítima brasileira para esporte e recreio.
- **Documentação do fabricante da bateria, do BMS e do sistema de carga** — obrigatória para parametrização e limites reais do conjunto.
- **Datasheet da célula individual** (CATL, EVE, Winston) — base para configurar BMS em bancos DIY.

## Como ensinar este tópico

**Sequência recomendada:**

1. Comparação visual: peso de 200Ah AGM vs 200Ah LiFePO4 — impacto imediato
2. Curva de descarga ao vivo: mostrar tensão estável do LiFePO4 vs queda do AGM
3. Cálculo de custo por ciclo: LiFePO4 sai mais barato em 5+ anos
4. O problema com o alternador: por que não funciona diretamente, soluções
5. BMS: o que protege, como monitorar, como o BMS conversa com o sistema

**Conceito-chave para fixar:**

"LiFePO4 não é só uma bateria mais cara. É uma tecnologia completamente diferente — com requisitos de instalação diferentes. Tratar como AGM é destruir o investimento."

## FAQ

**LiFePO4 pode pegar fogo?**

A probabilidade de evento térmico severo é menor que em outras químicas de lítio, mas não é nula. Projeto correto, BMS, proteção contra curto, instalação mecânica e coordenação de carga continuam sendo obrigatórios.

**Posso usar o alternador do motor para carregar LiFePO4?**

Pode, mas a resposta técnica depende do alternador, da potência, do regime térmico, da química do banco, do BMS e da forma de limitação de corrente. Em muitos casos, regulador externo ou DC-DC charger são a solução correta.

**LiFePO4 pode ser instalado em compartimento fechado?**

Ele não exige ventilação por hidrogênio como a bateria inundada, mas o compartimento ainda precisa respeitar controle térmico, acessibilidade, proteção mecânica e instruções do fabricante. Em áreas com GLP/combustível, a análise deve considerar todo o sistema elétrico, inclusive contatores, fusíveis e o próprio BMS.

**Qual a vida útil real do LiFePO4 a bordo?**

10–15 anos com uso e carga corretos. Battle Born e Victron garantem 10 anos (3.000–5.000 ciclos a DOD 80%). Comparado a AGM que dura 3–5 anos em uso intenso.

## Integração com outras notas

- [[Bancos de Bateria]]
- [[Alternador (DC)]]
- [[BMS — Battery Management System]]
- [[Carregador de Bateria (AC To DC)]]
- [[Inversora (DC To AC)]]
- [[Monitor de Bateria / BMV / Shunt]]
- [[Tipos de Bateria]]

## Perguntas que esta nota responde

- O que é Lítio LiFePO4 — Instalação e Cuidados Específicos em instalações elétricas náuticas?
