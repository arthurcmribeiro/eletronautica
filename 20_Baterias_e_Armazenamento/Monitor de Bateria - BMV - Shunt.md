---
title: "Monitor de Bateria / BMV / Shunt"
note_type: "technical-note"
domain: "20_Baterias_e_Armazenamento"
source_file: "MONITOR DE BATERIA BMV SHUNT 33a19734f7fb81f68a94d4b415eafa95.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "13"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
normas_citadas:
  - "ABYC E-11 (2023) — AC and DC Electrical Systems on Boats"
  - "ABYC E-10 (2023) — Storage Batteries"
  - "ABYC E-13 (2023) — Lithium Ion Batteries"
  - "ISO 13297:2020 — Small craft — AC and DC installations"
  - "ISO 16315:2016 — Electric propulsion system"
  - "NMEA 2000 (IEC 61162-3) — Comunicação de rede marítima"
  - "NMEA 0183 — Protocolo legado de instrumentação marítima"
  - "IEC 60051 — Direct acting indicating analogue electrical measuring instruments"
  - "IEC 61010-1 — Safety requirements for electrical equipment for measurement"
  - "ABNT NBR 5410:2004 — Instalações elétricas de baixa tensão"
  - "NORMAM-211/DPC — Embarcações de esporte e recreio"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://abycinc.org/news/standardsupdatewebinar/"
  - "https://www.iso.org/standard/83643.html"
  - "https://www.nmea.org/"
  - "https://www.iec.ch/"
aliases:
  - "MONITOR DE BATERIA BMV SHUNT"
  - "MONITOR DE BATERIA / BMV / SHUNT"
seo_title: "Monitor de Bateria / BMV / Shunt"
seo_description: "Monitor de bateria com shunt é o instrumento que mede corrente, tensão e balanço de carga/descarga do banco, permitindo estimar SoC e autonomia. Sua precisão depende de instalação correta, parametrização adequada e sincronizações consistentes."
seo_keywords:
  - "Monitor"
  - "Bateria"
  - "BMV"
  - "Shunt"
  - "20 Baterias e Armazenamento"
geo_queries:
  - "O que é Monitor de Bateria / BMV / Shunt em instalações elétricas náuticas?"
  - "Qual é a função de Monitor de Bateria / BMV / Shunt na embarcação?"
related_notes:
  - "Bancos de Bateria"
  - "Carregador de Bateria (AC To DC)"
  - "Tipos de Bateria"
  - "BMS — Battery Management System"
  - "Lítio LiFePO4 — Instalação e Cuidados Específicos"
  - "Monitoramento Remoto — VRM - Telemetria"
---

# Monitor de Bateria / BMV / Shunt

> [!abstract] Resumo técnico
> Monitor de bateria com shunt mede corrente, tensão e balanço acumulado de carga/descarga do banco para estimar SoC e autonomia. É uma ferramenta de gestão, não um oráculo: a qualidade do resultado depende da instalação do shunt, da parametrização e da rotina de sincronização.

> [!tip] Regra de decisão em 30 segundos
> 1. **Voltímetro não é monitor.** Tensão em repouso estima SoC em chumbo com ±10 %; sob carga ou logo após carga, erro passa de 30 %. Em LiFePO4, a curva é plana e voltímetro é inútil. Shunt + coulomb counting é o padrão técnico.
> 2. **Shunt sempre no cabo NEGATIVO, entre o banco e o barramento negativo.** Todo retorno passa pelo shunt — qualquer cabo negativo que desvie o shunt corrompe a medição.
> 3. **Configure a capacidade REAL, não a nominal.** Banco de 200 Ah com 5 anos pode ter 130 Ah reais; usar 200 Ah no monitor leva SoC a indicar 65 % quando já está vazio.
> 4. **Fator Peukert + eficiência de carga + tail current são parâmetros obrigatórios,** ajustados por química. LFP: Peukert 1,05, eficiência 95-98 %, tail current 2-4 %. Chumbo: Peukert 1,15-1,25, eficiência 80-85 %, tail current 2-4 %.
> 5. **Sincronização é rotina, não evento único.** Sem atingir 100 % com tail current baixa periodicamente, o SoC do monitor deriva. Em embarcação com consumo > geração, recalibrar manualmente.
> 6. **Instalação em posição acessível** para inspeção de terminal; shunt com parafusos frouxos gera resistência variável que distorce leitura de corrente.
> 7. **Monitor é complementar ao BMS**, não substituto. BMS mede tensão por célula e protege; monitor mede balanço do banco e reporta. Em lítio, são dois sistemas diferentes operando em paralelo.
> 8. **Dados históricos (mínimo SoC, ciclos profundos, tempo em float)** são o insumo para laudo de degradação e renegociação de garantia. Salvar em NMEA 2000, VRM ou app regularmente.
> 9. **Um monitor por banco.** SoC de banco de partida é irrelevante para banco de serviço e vice-versa. Embarcação com 3 bancos precisa de 3 shunts ou de monitor multi-bank (Simarine PICO).

> [!danger] Quando chamar um especialista
> - **SoC do monitor discordando sistematicamente do comportamento real do banco.** Exemplo: monitor indica 70 % mas inversor já corta por subtensão, ou monitor indica 40 % mas banco aguenta 8 horas de consumo alto. Pode ser capacidade mal configurada, célula em falha, cabo bypass, shunt com terminal frouxo, eficiência errada. Diagnóstico metódico com amperímetro de referência e ciclo controlado.
> - **Retrofit de monitor em instalação antiga sem diagrama unifilar.** Identificar onde cada cabo negativo termina, se há bond N-PE, se o alternador tem retorno direto ao banco ou passa por barramento. Sem mapear a rede DC, é inviável garantir que o shunt lê a corrente real.
> - **Integração de múltiplos monitores** (SmartShunt banco serviço + BMV banco partida + Wakespeed no alternador) em NMEA 2000 ou VE.Can. Conflito de IDs, duplicação de PGNs, latência e coerência de dados exigem configuração assistida.
> - **Banco lítio com BMS reportando SoC diferente do monitor.** BMS usa algoritmo próprio; monitor usa coulomb counting. Divergência > 10 % persistente indica problema em um dos dois — análise com datasheet da célula, versão de firmware do BMS e parâmetros do monitor.
> - **Eletropropulsão com múltiplos bancos em série-paralelo 48/96 V.** Shunts de 1000 A+, isolação galvânica, ground fault detection integrada. Monitor recreativo não cobre; exige sistema industrial com amperímetro de Hall isolado.
> - **Laudo pericial em sinistro com banco lítio.** Extrair histórico do monitor, do BMS e do VRM; reconstituir cadeia de eventos (corrente, tensão, temperatura, alarmes) no minuto da falha. Responsável técnico com ART/CREA.
> - **Consumo anormal de standby** (> 2 % ao dia) com monitor indicando descarga lenta sem causa aparente. Pode ser fuga à massa, equipamento sem chave de desligamento, iluminação LED mal projetada, BMS consumindo > 50 mA. Diagnóstico com amperímetro alicate e desligamento setor por setor.
> - **Conversão de banco 12 V → 24 V ou 24 V → 48 V mantendo monitor antigo.** Shunt pode ter faixa insuficiente, tensão de alimentação do monitor pode precisar ser reconfigurada, cabos de sense e alimentação precisam ser reavaliados.
> - **Monitor "desenhando" SoC fictício** em embarcação com consumo cíclico alto e geração solar intermitente. Sem sincronização em 100 % por semanas, o coulomb counter deriva — recalibrar com carga controlada no shore ou trocar o algoritmo para baseado em OCV (Open Circuit Voltage).

## O que é

O monitor de bateria (também chamado BMV — Battery Monitor, ou coulomb counter) é um instrumento que mede a corrente que entra e sai do banco de baterias e, com base no acumulado, calcula o estado de carga (SoC — State of Charge) em percentual. O ponto de medição de corrente é o **shunt** — uma resistência de baixo valor calibrada que produz uma queda de tensão proporcional à corrente.

É um dos instrumentos mais importantes para gestão de energia a bordo, especialmente quando a embarcação depende de autonomia e múltiplas fontes de carga.

## Função

| Função | O que mede/calcula |
| --- | --- |
| Estado de carga (SoC%) | Quanto de energia restante no banco (de 0 a 100%) |
| Corrente instantânea | Quantos amperes estão entrando (+) ou saindo (−) agora |
| Tensão do banco | Tensão atual em tempo real |
| Consumo acumulado | Ah consumidos desde a última carga completa |
| Tempo restante | Estimativa de tempo até descarga total |
| Potência instantânea (W) | Alguns modelos calculam V × I |
| Histórico | Ciclos, profundidade de descarga, temperatura |

## Como aparece na prática

- Display compacto no painel principal (Victron BMV-712)
- App no smartphone via Bluetooth (SmartShunt, SmartSolar)
- Integrado ao painel touchscreen do chartplotter via NMEA 2000
- Dados no dashboard VRM (monitoramento remoto)
- Shunt instalado no cabo negativo entre a bateria e o barramento negativo

## Fundamentos mínimos

**O shunt como sensor de corrente:**

O shunt é uma resistência de valor muito pequeno e precisão muito alta (tipicamente 500A / 50mV — 0,0001Ω). Ao circular corrente pelo shunt, gera-se uma queda de tensão proporcional (I = V/R). O monitor mede essa microvolátagem e calcula a corrente.

**Por que shunt no negativo:**

O monitor de bateria mede TODA a corrente que entra ou sai do banco. Para isso, o shunt deve estar em série com TODOS os cabos negativos. O cabo negativo principal é o ponto correto — se houver cabos negativos bypassando o shunt, a medição será incorreta.

**Diferença entre SoC por tensão vs SoC por coulomb counting:**

- Por tensão: estimativa limitada, especialmente sob carga, logo após carga ou em químicas de curva plana
- Por coulomb counting: muito superior para gestão diária, mas ainda depende de calibração, eficiência assumida e sincronização correta

**Necessidade de sincronização (sync):**

O monitor de bateria acumula Ah desde a última sincronização (quando o banco estava a 100%). Quando o banco chega a 100% (absorção completa), o monitor zera o contador e recalibra. Sem sincronização frequente, o SoC vai derivar.

## Características

| Parâmetro | Victron SmartShunt 500A |
| --- | --- |
| Corrente máxima | 500A (shunt 500A/50mV) |
| Precisão | ±1% na corrente, ±2% no SoC |
| Conectividade | Bluetooth (app VictronConnect) |
| Integração | VRM, Cerbo GX, NMEA 2000 (via adaptador) |
| Consumo próprio | < 4mA (desprezível) |
| Tensão de trabalho | 8–70V DC |
| Temperatura de operação | −40 a +50°C |

## Configurações

**Parâmetros críticos a configurar:**

| Parâmetro | O que define |
| --- | --- |
| Capacidade do banco (Ah) | Base de cálculo do SoC — deve ser a capacidade REAL, não a nominal |
| Fator Peukert | Correção para descarga rápida (baterias de chumbo) — para lítio, usar 1.05 |
| Corrente de carga completa (tail current) | Corrente abaixo da qual o monitor sincroniza para 100% |
| Tensão de carga completa | Tensão acima da qual o monitor aguarda a tail current |
| Eficiência de carga | Quanto Ah retorna para o banco a cada Ah carregado (95% lítio, 80–85% chumbo) |

**Erro mais comum na configuração:**

Colocar a capacidade nominal em vez da capacidade real. Um banco de 200Ah teórico com 5 anos de uso pode ter apenas 130Ah reais. Com 200Ah configurado, o monitor indicará 65% quando o banco já está vazio.

## Marcas e referências

- **Victron SmartShunt 500A** — melhor custo-benefício, Bluetooth nativo, integração VRM
- **Victron BMV-712** — mesma tecnologia + display físico
- **Victron BMV-700** — versão sem Bluetooth, display, econômico
- **Simarine PICO** — monitor naval premium, múltiplos bancos, display touchscreen
- **Empirbus / Garnet SeeLevel** — integração com nível de tanques
- **Wakespeed WS500** — monitor de alternador com comunicação avançada
- **Sterling Power BAM** — monitor básico acessível

## Instalação do shunt

**Posição correta:**

```
[BANCO (−)] → [SHUNT] → [BARRAMENTO NEGATIVO] → [todas as cargas e retornos]
```

**O que NÃO pode estar entre o banco e o shunt:**

- Nenhum retorno que se queira contabilizar pode bypassar o shunt
- Exceções e caminhos paralelos precisam ser tratados conscientemente no projeto

**O que pode estar entre o shunt e o barramento:**

- Todos os cabos negativos de carga e retorno
- Shunt do alternador (se houver monitor separado)

**Resistência do shunt:**

Verificar se os terminais do shunt estão bem apertados — resistência adicional por mau contato altera a medição de corrente.

## Problemas mais frequentes

| Problema | Causa | Solução |
| --- | --- | --- |
| SoC indica 100% mas banco está vazio | Falta sincronização | Verificar tensão de sync e tail current |
| SoC deriva ao longo de dias | Configuração de eficiência incorreta | Ajustar fator Peukert e eficiência |
| Corrente mostrando valor errado | Cabo negativo bypassando o shunt | Verificar que TODOS os negativos passam pelo shunt |
| Monitor não sincroniza | Banco nunca atinge carga completa (carregador fraco, consumo alto) | Verificar sistema de geração |
| Display não acende | Alimentação do monitor (tipicamente do banco) | Verificar cabo de alimentação do monitor |

## Diagnóstico prático

**Verificar se o shunt está medindo corretamente:**

```
1. Ligar um equipamento com corrente conhecida (ex: lâmpada 12W = 1A)
2. Monitor deve mostrar −1A de descarga
3. Se mostrar valor diferente → verificar calibração ou cabo bypassando
```

**Verificar sincronização:**

```
1. Carregar o banco completamente (shore power, absorção completa)
2. Monitor deve ir para 100% automaticamente
3. Se não foi → verificar configurações de tail current e tensão de sync
```

## Boas práticas profissionais

- Instalar shunt em posição acessível — inspeção e verificação de terminais facilitada
- Configurar todos os parâmetros antes de usar — capacidade real, não nominal
- Fazer ciclo de calibração inicial (descarga controlada + carga completa) para afinar o SoC
- Verificar que o monitor sincroniza corretamente após carga completa
- Em bancos de lítio: configurar eficiência de carga para 95–98% (vs 80–85% do chumbo)
- Revisar periodicamente se a capacidade configurada ainda representa a capacidade real do banco envelhecido

## Erros comuns

**Instalar shunt no positivo:**

O monitor funciona, mas a instalação no negativo é o padrão correto (ABYC, Victron). No negativo, o shunt monitora toda a corrente do sistema — mais confiável.

**Cabo negativo bypassando o shunt:**

O técnico instalou o shunt mas esqueceu de passar o retorno de um circuito pelo shunt. Resultado: o monitor não conta essa corrente → SoC deriva rapidamente.

**Não configurar a capacidade real:**

Configurar 200Ah em banco que tem 150Ah reais → o monitor indica "50%" quando o banco já está quase vazio.

**Ignorar o monitor após instalar:**

Instalar e não usar os dados. O monitor só agrega valor se consultado regularmente para gerenciar o consumo.

## Relação com outros sistemas

- **Banco de baterias:** o monitor fornece o SoC real — essencial para gestão de autonomia
- **Victron VRM:** dados do SmartShunt aparecem no dashboard remoto
- **Monitoramento Remoto — VRM - Telemetria:** o monitor alimenta dashboards, alarmes e histórico de autonomia
- **Automação:** Cerbo GX usa dados do shunt para ativar gerador, controlar cargas
- **BMS (lítio):** BMS monitora células individuais; shunt monitora o banco como um todo — complementares
- **NMEA 2000:** SmartShunt com adaptador publica dados no barramento de instrumentos

## Glossário rápido

- **Monitor de bateria / BMV (Battery Monitor)** — instrumento que mede corrente, tensão e integra no tempo para calcular SoC.
- **Shunt** — resistor calibrado de baixíssimo valor (0,0001 Ω = 500 A/50 mV) em série com o cabo negativo.
- **Queda de tensão no shunt** — proporcional à corrente (V = R × I); monitor lê em microvolts e calcula corrente.
- **Coulomb counting** — método de cálculo de SoC por integração de corrente no tempo (Ah in − Ah out).
- **SoC (State of Charge)** — percentual de carga atual em relação à capacidade.
- **SoH (State of Health)** — percentual de capacidade remanescente em relação à nova.
- **DoD (Depth of Discharge)** — complemento do SoC (DoD = 100 − SoC).
- **Ah (Ampère-hora)** — unidade de carga; base do coulomb counting.
- **Wh (Watt-hora)** — unidade de energia; Ah × V nominal.
- **Tail current** — corrente abaixo da qual o monitor considera "carga completa" (~2-4 % da nominal).
- **Sincronização (sync)** — evento em que o monitor zera contador e recalibra para 100 %; requer absorção completa + tail current atingida.
- **Fator Peukert** — coeficiente que corrige capacidade sob diferentes taxas de descarga. Chumbo 1,15-1,25; LFP 1,05.
- **Eficiência de carga (charge efficiency)** — Ah recuperado / Ah injetado; LFP 95-98 %, AGM 80-85 %, FLA 75-80 %.
- **OCV (Open Circuit Voltage)** — tensão em repouso (sem carga > 1-2 h); base para estimativa alternativa de SoC.
- **Drift do SoC** — erro acumulado do coulomb counter sem sincronização; corrigido por sync.
- **Multi-bank** — monitor com múltiplos shunts para 2+ bancos independentes.
- **Hall sensor** — alternativa ao shunt; mede corrente por campo magnético, sem resistor na linha.
- **Shunt de precisão (Class 0,1 / 0,5 / 1,0)** — classe de precisão IEC; náutico típico é 0,5-1,0 %.
- **Barramento negativo (negative bus bar)** — ponto de consolidação de todos os retornos; shunt fica entre banco e barramento.
- **Cabo negativo principal** — cabo de maior bitola do banco ao barramento; shunt em série.
- **Cabo de sense / sensor** — realimentação de tensão do monitor; mede a tensão real no banco, não no monitor.
- **Alimentação do monitor** — cabo dedicado fino que alimenta a eletrônica do monitor; protegido por fusível separado.
- **BMV-712 / SmartShunt / BMV-700** — linha Victron, referência de mercado náutico.
- **Simarine PICO / NAUT / SCQ25** — monitor naval premium com touchscreen e multi-bank.
- **Wakespeed WS500** — monitor de alternador com comunicação CAN.
- **VE.Direct** — interface serial Victron para SmartShunt → Cerbo GX → VRM.
- **VE.Can** — CAN bus Victron para integração entre monitor, inversor, MPPT.
- **NMEA 2000 (PGN 127508 / 127506)** — mensagens padrão de bateria na rede marítima.
- **VRM (Victron Remote Management)** — portal em nuvem que recebe dados de SmartShunt/Cerbo.
- **Cerbo GX** — gateway Victron que agrega dados de shunt, MPPT, inversor, gerador e publica em VRM.
- **Amperímetro alicate** — instrumento para verificar independentemente a corrente; base de calibração do monitor.
- **Multímetro** — voltímetro digital para validar tensão indicada pelo monitor.
- **Registrar de dados (data logger)** — função interna do monitor que grava histórico de SoC, V, I, T.
- **Alarme de SoC baixo** — configurável; aciona buzzer, relé, alarme NMEA.
- **Relé programável** — saída do monitor que comanda gerador auto-start, chave seletora, iluminação crítica.
- **Calibração de zero** — ajuste de offset do monitor com banco em repouso total.
- **Bias térmico** — erro do shunt por variação de temperatura; relevante em shunts de alta corrente.
- **BMS vs Monitor** — BMS mede célula, protege banco; monitor mede banco, gerencia autonomia.
- **OCV lookup table** — tabela de tensão em repouso vs SoC; fallback quando coulomb counter desvia.

## Normas aplicáveis

- **ABYC E-11 (2023)** — Medição e monitoramento de sistemas DC; localização do shunt, bitolagem do cabo negativo.
- **ABYC E-10 (2023)** — Storage batteries; identificação e rotulagem do banco; relevante para documentação.
- **ABYC E-13 (2023)** — Lithium ion batteries; exigências específicas para monitoramento de lítio.
- **ISO 13297:2020** — Small craft AC e DC; inclusive medição e instrumentação.
- **ISO 16315:2016** — Electric propulsion; monitoramento em bancos de alta potência.
- **NMEA 2000 (IEC 61162-3)** — Protocolo de rede marítima; PGNs específicos para bateria (127506, 127508, 127513).
- **NMEA 0183** — Protocolo legado; ainda presente em instrumentos antigos integrados.
- **IEC 60051** — Instrumentos analógicos indicadores; base histórica para amperímetros/voltímetros.
- **IEC 61010-1** — Requisitos de segurança para equipamentos de medição; aplicável à eletrônica do monitor.
- **ABNT NBR 5410:2004** — Instalações elétricas de baixa tensão; aplicável ao barramento e proteção.
- **NORMAM-211/DPC** — Embarcações de esporte e recreio; exigências brasileiras.
- **Manuais dos fabricantes** — configuração específica por modelo; parâmetros obrigatórios para precisão.

## Como ensinar este tópico

**Sequência recomendada:**

1. Problema: "seu banco tem 200Ah. Quanto tem agora?" → sem monitor, é chute
2. Mostrar app ao vivo: SoC%, corrente instantânea, tempo restante
3. Instalar shunt fisicamente — posição correta no negativo
4. Configurar parâmetros: capacidade real, eficiência, tail current
5. Fazer teste de calibração: descarregar e carregar, verificar que sincroniza em 100%

**Conceito-chave para fixar:**

"Gerenciar banco sem monitor é navegar sem GPS. Você chega — mas não sabe onde está."

## FAQ

**Posso usar o multímetro de tensão para estimar o SoC?**

Sim, aproximadamente, se a bateria estiver em repouso por pelo menos 1 hora sem carga ou carregamento. Mas a precisão é baixa e não fornece Ah restantes ou tempo estimado. O monitor de bateria é incomparavelmente mais preciso.

**SmartShunt ou BMV-712: qual escolher?**

SmartShunt se você usa smartphone para monitoramento (mais barato, mesmo desempenho). BMV-712 se quer display físico permanente no painel ou se o acesso ao smartphone é inconveniente a bordo.

**O monitor de bateria funciona com qualquer tipo de bateria?**

Sim — configura-se para chumbo-ácido, AGM, GEL ou LiFePO4 mudando os parâmetros (tensão de sync, tail current, eficiência, Peukert). A configuração correta por tipo de bateria é essencial para precisão.

## Visual didático

![Monitor de bateria: shunt e calculo de SoC](../_visuals/generated/monitor-bateria-shunt-fluxo.svg)

Mostrar por que shunt mede corrente real e entrega SoC melhor que voltimetro isolado.

**Cautela:** A posicao do shunt, referencia negativa e configuracao de capacidade/eficiencia devem seguir o fabricante.

Material de apoio: [Monitor de bateria: shunt e calculo de SoC](../_visuals/generated/monitor-bateria-shunt-fluxo.md)

## Integração com outras notas

- [[Bancos de Bateria]]
- [[Carregador de Bateria (AC To DC)]]
- [[Tipos de Bateria]]
- [[BMS — Battery Management System]]
- [[Lítio LiFePO4 — Instalação e Cuidados Específicos]]
- [[Monitoramento Remoto — VRM - Telemetria]]

## Perguntas que esta nota responde

- O que é Monitor de Bateria / BMV / Shunt em instalações elétricas náuticas?
- Qual é a função de Monitor de Bateria / BMV / Shunt na embarcação?
