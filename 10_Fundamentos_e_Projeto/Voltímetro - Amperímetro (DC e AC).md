---
title: "Voltímetro / Amperímetro (DC e AC)"
note_type: "technical-note"
domain: "10_Fundamentos_e_Projeto"
source_file: "VOLTIMETRO AMPERIMETRO (DC) e (AC) e7d19734f7fb827bba7a819fb2653ee0.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "32"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
  - "internacional"
normas_citadas:
  - "ABYC E-11 (2023) — AC & DC Electrical Systems on Boats (instrumentação de painel, shunts, proteção de circuitos de medição)"
  - "ABYC E-10 (2023) — Storage Batteries (monitoramento de banco, SoC, SoH)"
  - "ABYC E-13 (2022) — Lithium Ion Batteries (instrumentação específica LiFePO4)"
  - "ABYC E-8 (2020) — AC Generators (frequencímetro, voltímetro AC)"
  - "ABYC E-9 (2019) — DC Charging Systems (amperímetro alternador)"
  - "ISO 13297:2020 — Small craft — Electrical systems AC & DC (requisitos de monitoramento)"
  - "IEC 60051-1:2016 — Direct acting indicating analogue electrical measuring instruments (classes de exatidão)"
  - "IEC 60051-2:1984 — Amperímetros e voltímetros analógicos"
  - "IEC 60051-3:1984 — Wattímetros e varímetros"
  - "IEC 60051-7:1984 — Multifunction instruments"
  - "IEC 60688:2012 — Electrical measuring transducers (conversores)"
  - "IEC 61010-1:2010 — Safety requirements for measurement equipment (CAT I-IV)"
  - "IEC 61326-1:2020 — EMC requirements"
  - "IEC 60529 — Graus de proteção IP (painel náutico IP-54 mín)"
  - "IEC 60092-504 — Control and instrumentation on ships"
  - "IEC 60092-401 — Installation and test of completed installation"
  - "IEEE C57.13 — Standard Requirements for Instrument Transformers (TC/CT)"
  - "ANSI C12.20 — Electricity meters (0,1% e 0,2% accuracy classes)"
  - "NMEA 2000 (IEC 61162-3) — Rede digital para integração de instrumentação"
  - "Victron Application Note — BMV Battery Monitor Installation"
  - "ABNT NBR 5410:2004 + emendas — Instalações elétricas de baixa tensão"
  - "ABNT NBR IEC 61010-1:2010 — Segurança de instrumentos de medição"
  - "INMETRO Portaria 200/2002 — Regulamentação de instrumentos de medição"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "VOLTIMETRO AMPERIMETRO (DC) e (AC)"
  - "VOLTIMETRO/AMPERIMETRO (DC) e (AC)"
  - "Voltímetro / Amperímetro (DC e AC)"
seo_title: "Voltímetro / Amperímetro (DC e AC)"
seo_description: "VOLTÍMETRO / AMPERÍMETRO (DC e AC) — Instrumentos de medição elétrica que permitem ao operador monitorar tensão e corrente no painel — os olhos do sistema elétrico a."
seo_keywords:
  - "Voltímetro"
  - "Amperímetro"
  - "10 Fundamentos e Projeto"
geo_queries:
  - "O que é Voltímetro / Amperímetro (DC e AC) em instalações elétricas náuticas?"
  - "Qual é a função de Voltímetro / Amperímetro (DC e AC) na embarcação?"
related_notes:
  - "DC vs AC — Corrente Contínua e Alternada"
  - "Diagrama Unifilar — Documentação do Sistema Elétrico"
  - "Dimensionamento de Banco de Baterias — Cálculo de Autonomia"
  - "Dimensionamento de Cabos DC — Cálculo Prático"
  - "Fase e Neutro"
  - "Ferramentas do Eletricista Náutico"
  - "Inspeção de Cabos Terminais e Conexões"
  - "Lei de Ohm e Cálculos Básicos"
---

# Voltímetro / Amperímetro (DC e AC)

> [!abstract] Resumo técnico
> VOLTÍMETRO / AMPERÍMETRO (DC e AC) — Instrumentos de medição elétrica que permitem ao operador monitorar tensão e corrente no painel — os olhos do sistema elétrico a bordo.

> [!tip] Regra de decisão em 30 segundos
> 1. **Voltímetro isolado NÃO dá SoC confiável** — tensão cai artificialmente em descarga e sobe em carga; só faz sentido em repouso ≥ 2h com química/temperatura conhecidas; LiFePO4 com curva plana (13,0-13,3 V de 20-90% SoC) é PRATICAMENTE inútil.
> 2. **Monitor com shunt = SoC real em tempo real** — Victron BMV/SmartShunt, Simarine PICO, Trimetric; integra corrente no tempo (coulomb counting) + sincronização com banco cheio; instrumento de referência em banco > 100 Ah.
> 3. **Shunt SEMPRE no negativo principal** — todos os negativos passam por ele; instalar no positivo = inversão de sinal e risco de dano; shunt em ramal = contabiliza só aquele ramal.
> 4. **Bitola do cabo de sinal do shunt = fino (0,75 mm² típico) + fusível 1 A** — corrente de sinal é μA-mA; cabo grosso é desnecessário, fusível protege monitor em curto.
> 5. **Amperímetro AC exige TC (Transformador de Corrente)** — instalar instrumento direto na fase = queima; TC dimensionado à corrente máxima (100A/5A para até 100 A AC).
> 6. **Voltímetro AC em painel é informação operacional, não proteção** — faixa aceitável 198-242 V (220 V ±10%), < 190 V sinaliza cabo/marina com problema; a proteção real é o DR/ELCI/GFCI.
> 7. **Classe de exatidão IEC 60051 define utilidade** — classe 0,5 (±0,5% fundo de escala) profissional, classe 1,5 popular náutico, classe 2,5 automotivo (aceitável só para indicação).
> 8. **Sincronização do BMV exige "100% full charge"** — sem atingir flutuação total periodicamente, SoC deriva; parâmetros de charged voltage + tail current + charged detection time devem estar certos.
> 9. **NMEA 2000 (IEC 61162-3) integra instrumentação** — BMV + MPPT + Cerbo GX + plotter num único display; redução de cabeamento e consistência de dados.

> [!danger] Quando chamar um especialista (eletricista náutico / integrador Victron/Mastervolt)
> 1. **SoC sistematicamente errado mesmo após recalibração** — bypass de shunt (negativo conectado direto na bateria), capacidade programada incorreta, parâmetros de sincronização errados ou banco envelhecido com SoH << 100%; diagnóstico exige mapeamento de todos os negativos.
> 2. **Instrumentação de banco lítio multi-bateria em série/paralelo** — BMS de cada pack + BMV de banco + BMS-master: configuração coordenada exige conhecimento do ecossistema (Victron Lynx Distributor + Lynx Smart BMS + BMV-712 + Cerbo GX + VRM).
> 3. **Integração NMEA 2000 + Victron VE.Bus + SignalK + plotter Raymarine/Garmin/B&G** — protocolos diferentes, gateways (Victron Cerbo, Actisense NGT-1), mapeamento PGN, certificação NMEA; fora do escopo de integrador generalista.
> 4. **Medição de corrente em cabo-tronco de embarcação comercial (> 500 A DC, > 200 A AC)** — TC de precisão, shunt calibrado, integrador ANSI C12.20; laudo auditável pela classificadora (BV, Lloyd's, RBNA).
> 5. **Diagnóstico de instrumento queimado por surto (raio, falha shore power)** — análise de trilha de dano, identificação de origem, renovação coordenada de proteções (varistores MOV, GDT, TVS); substituição sem diagnóstico = queima repetida.
> 6. **Certificação de painel elétrico comercial (RBNA, BV)** — painel IP-54/56 + disjuntores certificados + instrumentação classe 1,5 + etiquetas normativas; exige desenho de conjunto + ART + conformidade IEC 61439-series.
> 7. **Perícia pós-sinistro com instrumento como evidência** — preservação do instrumento queimado, cadeia de custódia, laudo IBAPE/Abracem; trocar sem perícia = perda de evidência.
> 8. **Monitoramento remoto VRM com alarmes críticos (banco < 20% SoC, gerador overload, shore desconectado)** — configuração de regras + notificações push/email/SMS + integração IoT; exige conta VRM + modem/4G + configuração avançada.
> 9. **Instrumentação em embarcação hospitalar, OPV médico ou offshore crítico** — NBR 13534 (criticidade), redundância N+1, fail-safe em cada medição; projeto dedicado.

## Escopo

Esta nota trata de instrumentação de painel para monitoramento operacional. Para monitor de bateria com shunt e análise mais aprofundada de SoC, ver também [[Monitor de Bateria - BMV - Shunt]].

## O que é

Voltímetro e amperímetro são instrumentos de medição instalados no painel elétrico da embarcação para monitoramento em tempo real das grandezas elétricas fundamentais: tensão (V) e corrente (A).

**Tipos presentes em embarcações:**

- **Voltímetro DC:** monitora tensão do banco de baterias — instrumento mais básico e mais comum
- **Amperímetro DC:** mede corrente de carga ou descarga do banco — requer shunt externo
- **Monitor de banco completo (BMV):** combina voltímetro + amperímetro + cálculo de SoC em percentual e Ah
- **Voltímetro AC:** monitora tensão do shore power ou gerador
- **Amperímetro AC:** mede corrente AC via transformador de corrente (TC/CT)
- **Frequencímetro:** monitora frequência AC (60Hz no Brasil) — relevante em sistemas com gerador

**Distinção importante:**

Voltímetro simples e monitor de banco são instrumentos fundamentalmente diferentes em utilidade. Um mede tensão instantânea; o outro rastreia o estado de carga real (SoC) ao longo do tempo.

## Função

- Voltímetro DC: informar se o banco está carregando, em que nível de tensão, e alertar para tensão crítica
- Amperímetro DC: informar quanto corrente está entrando (carga) ou saindo (descarga) do banco
- Monitor com shunt: calcular SoC real em %, Ah consumidos e Ah restantes — controle real da energia
- Voltímetro AC: confirmar que a tensão do shore power ou gerador está dentro da faixa adequada (220V ±10%)
- Amperímetro AC: monitorar corrente total consumida do cais ou gerador

## Como aparece na prática

**Com voltímetro simples no painel:**

Operador olha e vê "12,1V" → interpreta como banco baixo. Mas está com motor ligado, gerando distorção de leitura. Ou o banco acabou de ser carregado e está em 13,6V — mas o estado real de carga é 70%. O voltímetro isolado engana sem contexto.

**Com monitor BMV:**

Operador vê "SoC: 67%, 8,3A saindo, 18h de autonomia restante". Decisão imediata: ligar gerador agora ou aguardar até amanhã. Informação completa para decisão correta.

**Voltímetro AC no painel:**

Operador conecta ao cais, olha o painel: 198V. Está dentro da faixa, mas no limite inferior. Se cair mais, o carregador pode não operar eficientemente. Com frequencímetro, confirma 60Hz — gerador está na rotação correta.

## Fundamentos mínimos

**O que a tensão DC diz (e não diz):**

- Em repouso e com a química correta considerada: pode correlacionar com SoC
- Durante carga: tensão sobe artificialmente — não reflete SoC real
- Durante descarga: tensão cai artificialmente pela resistência interna — não reflete SoC real
- Lítio LFP tem curva de tensão plana: 13,0–13,3V de 20% a 90% de carga — voltímetro é praticamente inútil para indicar SoC em lítio

**Por que o amperímetro com shunt é mais útil:**

O shunt mede corrente instantânea com alta precisão. O monitor integra a corrente no tempo (Ah = A × h) para calcular o SoC real — independentemente da tensão instantânea.

**Shunt — como funciona:**

Resistor de precisão de valor muito baixo (ex: 500A/75mV) instalado no negativo principal. Toda corrente que entra ou sai do banco passa pelo shunt. A queda de tensão de mV é proporcional à corrente — o monitor lê e calcula.

## Características técnicas

**Voltímetro DC:**

- Resolução: 0,01V (bom) ou 0,1V (básico)
- Exatidão: ±0,5% ou melhor
- Proteção IP: mínimo IP52 para uso em painel exposto
- Alimentação: 12V ou 24V DC (conforme o sistema)

**Shunt para amperímetro/monitor:**

- Valor padrão: 500A/75mV ou 500A/50mV
- Selecionar conforme corrente máxima esperada e margem coerente com o regime real do sistema
- Instalar no negativo principal — todos os negativos do banco passam pelo shunt

**Voltímetro AC:**

- Faixa: 0–300V AC
- Exatidão: ±1,5% ou melhor
- Alimentação: da própria linha AC medida

**Amperímetro AC:**

- Requer TC (Transformador de Corrente) proporcional à corrente máxima esperada
- TC 100A/5A: para sistemas até 100A AC

**Comparativo voltímetro simples vs monitor completo:**

| Função | Voltímetro simples | Monitor com shunt (BMV) |
| --- | --- | --- |
| Tensão DC | ✅ | ✅ |
| Corrente DC | ❌ | ✅ |
| SoC (%) real | ❌ | ✅ |
| Ah consumidos | ❌ | ✅ |
| Ah restantes | ❌ | ✅ |
| Histórico | ❌ | ✅ |
| Alarme de baixo SoC | ❌ | ✅ |
| Bluetooth / app | ❌ | ✅ (modelos modernos) |
| Custo | R$ 30–150 | R$ 500–1.200 |

## Configurações comuns

**Configuração 1 — Voltímetro simples no painel (muito comum no Brasil):**

Voltímetro LED ou analógico indicando tensão do banco. Informação mínima. Presente em praticamente 100% das embarcações com painel elétrico, mas insuficiente para controle real do sistema.

**Configuração 2 — Voltímetro DC + amperímetro de painel com shunt:**

Dois instrumentos separados. Shunt de 500A no negativo, amperímetro de painel conectado ao shunt. Informação de tensão + corrente instantânea — melhor que voltímetro só, mas sem cálculo de SoC.

**Configuração 3 — Monitor de banco completo (comum em lanchas bem equipadas):**

Victron BMV-712 ou SmartShunt 500A. Shunt único no negativo principal. Display com tensão, corrente, SoC%, Ah restantes. Bluetooth para app no celular. Configurável para qualquer tipo e capacidade de banco.

**Configuração 4 — Painel AC + DC combinado (mais presente em embarcações maiores/premium):**

Voltímetro AC + amperímetro AC (com TC) + frequencímetro para o sistema shore/gerador, combinado com voltímetro/amperímetro DC para o banco. Visão completa de ambos os sistemas em um único painel.

## Marcas e referências

**Monitores de banco completos (referência no mercado náutico):**

- **Victron BMV-712** — referência absoluta; Bluetooth integrado, app VictronConnect, histórico completo, alarmes programáveis. Com ou sem shunt (SmartShunt sem display dedicado)
- **Victron SmartShunt 500A** — shunt com Bluetooth, sem display físico — integra ao GX Device ou app
- **Simarine PICO** — monitor alternativo de qualidade, display colorido touch, múltiplos shunts
- **Trimetric (Bogart Engineering)** — popular em veleiros de cruzeiro americanos, muito confiável

**Voltímetros/amperímetros de painel:**

- **Faria Instruments** — referência americana em instrumentação náutica de painel
- **Seachoice / Perko** — linha náutica de qualidade intermediária
- **Genéricos LED** — disponíveis no mercado nacional, qualidade variável; aceitáveis para voltímetro básico

**Shunts:**

- **Victron shunts** — recomendados para uso com BMV Victron
- **Shunts genéricos** — aceitáveis se especificação correta (500A/75mV)

## Componentes relacionados

- **Banco de baterias:** o que está sendo monitorado — capacidade programada no monitor define precisão do SoC
- **BMS:** em lítio, o BMS já monitora célula a célula; o BMV monitora o banco como um todo (saída do BMS)
- **GX Device (Victron Cerbo/CCGX):** centraliza dados de todos os monitores em uma tela e no VRM
- **MPPT solar:** produção solar visível no monitor quando shunt instalado corretamente
- **Alternador:** corrente de entrada do alternador visível no amperímetro — diagnóstico em tempo real
- **Shore power:** voltímetro AC + amperímetro AC monitoram a qualidade da alimentação do cais

## Problemas mais frequentes

1. **SoC incorreto no monitor** — negativo de algum equipamento conectado diretamente na bateria (bypassando o shunt) — corrente não contabilizada
2. **Leitura de tensão oscilante** — mau contato no fio de sinal do voltímetro, conector oxidado
3. **Amperímetro sempre mostrando zero** — shunt instalado no positivo (posição errada) ou fio de sinal desconectado
4. **BMV indicando SoC incorreto gradualmente ao longo do tempo** — falta de sincronização (banco nunca atinge 100% completo para recalibrar)
5. **Voltímetro mostrando tensão diferente do multímetro** — calibração do instrumento; aceitável até ±0,2V
6. **Amperímetro AC não funciona** — TC instalado no positivo (deve ser no condutor de fase apenas) ou TC de calibre errado

## Causas raiz

| Problema | Causa raiz real |
| --- | --- |
| SoC crescendo mas banco não carrega | Negativo de alguma carga bypassando o shunt → monitor não conta saída de corrente |
| Monitor indicando banco cheio sempre | Banco mal calibrado (capacidade incorreta) OU shunt não instalado no negativo principal |
| Voltímetro com leitura diferente do real | Fio de sinal puxado de ponto distante no barramento — queda de tensão no próprio fio |
| Amperímetro AC queimado | Instalado sem TC na linha de corrente alta — corrente direta destruiu o instrumento |
| SoC deriva ao longo de dias | Banco nunca chega a 100% → monitor não sincroniza → erro acumulado |

## Diagnóstico prático

**Verificação de SoC incorreto:**

- Comparar leitura do BMV com medição direta de tensão no multímetro (banco em repouso >2h)
- Em chumbo-ácido, a tensão de repouso pode servir como cheque de plausibilidade, mas não substitui ensaio nem histórico de banco
- Se a leitura de SoC e a tensão de repouso estiverem incompatíveis para a química em questão, investigar parametrização, sincronização e bypass do shunt

**Verificar se o shunt está funcionando:**

- Ligar carga conhecida (ex: farol 5A)
- BMV deve mostrar corrente de saída ~5A
- Se mostrar 0A: shunt bypassado ou fio de sinal desconectado

**Verificar bypassagem do shunt:**

- Desligar todas as cargas
- Amperímetro deve mostrar corrente próxima a zero
- Se ainda mostrar corrente ou se banco descarrega enquanto amperímetro mostra zero: algum negativo está conectado diretamente na bateria, fora do circuito do shunt. Rastrear os negativos um por um.

**Sincronizar o BMV:**

- Deixar banco carregar completamente (absorption completa + float)
- BMV sincroniza automaticamente para 100% quando detecta banco pleno
- Se BMV não sincroniza: verificar se os critérios de sincronização estão configurados corretamente

## Boas práticas profissionais

- Instalar shunt **no negativo principal do banco** — todos os negativos de cargas devem se conectar no lado de carga do shunt, não na bateria diretamente
- Calibrar o monitor com a capacidade real do banco (não a capacidade nominal — bancos envelhecidos têm capacidade menor)
- Usar monitor com Bluetooth (Victron BMV-712 ou SmartShunt) para acesso via celular em qualquer lugar do barco
- Instalar voltímetro AC no painel de shore power — verificar polaridade e tensão antes de conectar cargas
- Para sistemas lítio: programar o monitor com os parâmetros corretos de LFP (tensão de referência diferente do chumbo)
- Verificar conexões do shunt a cada 6 meses — oxidação aumenta resistência e afeta leitura

## Cuidados de instalação

- Shunt: cabo de sinal (mV) deve ser fino (~0,75mm²) e protegido por fusível de sinal (1A)
- Shunt instalado no negativo principal — não no positivo, não no meio de algum ramal
- Fio de tensão do voltímetro DC: puxar de ponto representativo e protegido, evitando criar sense line longa e desprotegida
- Voltímetro AC: alimentado diretamente da linha AC que monitora — via fusível 1A
- TC do amperímetro AC: instalado ao redor do condutor de fase apenas (nunca ao redor do neutro ou de dois condutores juntos)
- Instrumentos de painel: fixar com vedação traseira para evitar entrada de umidade pelo painel

## Cuidados de uso

- Nunca tomar decisões de sistema baseadas apenas na tensão durante carga ou descarga ativa — esperar 30 min de repouso para leitura de SoC por tensão
- Para lítio: nunca usar voltímetro simples como indicador de SoC — a curva plana do LFP torna a tensão praticamente inútil para esse fim
- Após trocar banco de baterias: reprogramar capacidade do monitor (novo banco tem capacidade diferente)
- Verificar se o SmartShunt/BMV está conectado ao GX Device para logging remoto via VRM

## Erros comuns de instaladores

- **Instalar shunt no positivo** — posição errada; shunt deve ser no negativo principal
- **Conectar negativos de equipamentos diretamente na bateria** (bypassando o shunt) — corrente não contabilizada, SoC sempre errado
- **Não programar a capacidade do banco** no monitor — SoC calculado errado desde o início
- **Instalar amperímetro AC sem TC** — corrente alta queima o instrumento
- **Fio de sinal do BMV sem fusível de sinal** — curto no fio de sinal danifica o monitor
- **Usar voltímetro simples como único instrumento em banco energeticamente relevante** — controle insuficiente para gestão séria do banco

## Relação com outros sistemas

- **Banco de Baterias:** o sistema monitorado — capacidade e química definem os parâmetros do monitor
- **BMS (lítio):** o BMS tem monitoramento interno por célula; o BMV monitora o banco como um todo na saída do BMS
- **Alternador:** corrente de entrada visível no amperímetro DC em tempo real — diagnóstico imediato
- **MPPT Solar:** produção solar contabilizada pelo shunt — visível no monitor
- **Shore Power:** voltímetro AC verifica qualidade da alimentação do cais
- **Gerador AC:** frequencímetro indica se o gerador está na rotação correta (60Hz)
- **GX Device / Cerbo GX:** centraliza dados de todos os monitores em uma interface e no VRM remoto

## Brasil x Internacional

| Aspecto | Brasil | Internacional (ABYC/Europa) |
| --- | --- | --- |
| Instrumento mais comum | Voltímetro LED simples | Monitor com shunt (BMV ou similar) |
| Uso de monitor completo | Crescendo — ainda minoria | Padrão em embarcações >30 pés |
| Monitoramento AC | Raramente voltímetro/amperímetro no painel | Comum em embarcações com shore power permanente |
| Bluetooth/app | Crescendo com Victron | Padrão |
| Shunt instalado corretamente | Frequentemente bypassado por negativos avulsos | Rigoroso — todos os negativos pelo shunt |

## Normas aplicáveis

**ABYC — instrumentação de painel náutico:**

- **ABYC E-11 (2023)** — AC and DC Electrical Systems on Boats: instrumentação recomendada, shunts no negativo principal, proteção de circuitos de medição (fusível de sinal 1 A), bitola do cabo de sinal.
- **ABYC E-10 (2023)** — Storage Batteries: monitoramento de banco, SoC, SoH, histórico de ciclos.
- **ABYC E-13 (2022)** — Lithium Ion Batteries: instrumentação específica LiFePO4 (integração BMS + BMV).
- **ABYC E-8 (2020)** — AC Generators: voltímetro + amperímetro + frequencímetro de gerador.
- **ABYC E-9 (2019)** — DC Charging Systems: amperímetro de alternador em tempo real.

**ISO — embarcações de recreio:**

- **ISO 13297:2020** — Small craft — Electrical systems AC & DC: requisitos de monitoramento operacional.

**IEC — instrumentos de medição (segurança + exatidão):**

- **IEC 60051-1:2016** — Direct acting indicating analogue electrical measuring instruments: classes de exatidão (0,1; 0,2; 0,5; 1,0; 1,5; 2,5; 5,0).
- **IEC 60051-2:1984** — Amperímetros e voltímetros analógicos de indicação direta.
- **IEC 60051-3:1984** — Wattímetros e varímetros.
- **IEC 60051-7:1984** — Multifunction instruments.
- **IEC 60688:2012** — Electrical measuring transducers (conversores sinal-corrente 4-20 mA, sinal-tensão 0-10 V).
- **IEC 61010-1:2010** — Safety requirements for measurement (CAT I-IV).
- **IEC 61326-1:2020** — EMC requirements for measurement equipment.
- **IEC 60529** — Graus de proteção IP: painel náutico IP-54 mínimo, IP-65/67 em instalação externa.
- **IEC 60092-504** — Control and instrumentation on ships (comerciais).
- **IEC 60092-401** — Installation and test of completed installation.

**ANSI / IEEE — EUA:**

- **IEEE C57.13** — Standard Requirements for Instrument Transformers (TC e PT): classes 0,3, 0,6, 1,2 de exatidão.
- **ANSI C12.20** — Electricity meters: classes 0,1% e 0,2% para medidores fiscais (auditáveis).

**Integração digital:**

- **NMEA 2000 (IEC 61162-3)** — rede digital para integração de instrumentação (BMV, MPPT, GX, plotter).
- **Victron Application Note** — BMV Battery Monitor Installation: referência prática documentada.

**Brasil:**

- **ABNT NBR 5410:2004 + emendas** — princípios de baixa tensão, identificação e proteção.
- **ABNT NBR IEC 61010-1:2010** — segurança de instrumentos de medição.
- **INMETRO Portaria 200/2002** — regulamentação de instrumentos de medição.

## Glossário rápido

- **Accuracy class (classe de exatidão IEC 60051)** — erro máximo em % do fundo de escala: 0,5 (laboratório), 1,0-1,5 (industrial), 2,5 (popular).
- **Ah counter (contador de ampère-hora)** — integra corrente × tempo; base do cálculo de SoC no BMV.
- **Amperímetro DC direto** — instrumento com bobina em série no circuito (obsoleto, limitado a baixa corrente).
- **Amperímetro DC com shunt** — instrumento que lê queda de tensão no shunt (mV) e converte para corrente; padrão atual.
- **Amperímetro AC** — lê corrente AC via TC (transformador de corrente); instalação direta = queima.
- **ANSI C12.20 classe 0,1% / 0,2%** — medidores fiscais de energia (auditáveis pela concessionária).
- **Auto-ranging** — seleção automática de escala (em alguns modelos digitais).
- **Bluetooth (Victron VE.Direct)** — comunicação sem fio do SmartShunt/BMV para app no celular.
- **BMS (Battery Management System)** — eletrônica de lítio que gerencia células; fornece dados ao BMV via cabo de comunicação.
- **BMV (Battery Monitor Victron)** — linha de monitores Victron: BMV-700, BMV-702, BMV-712 Smart (BT), SmartShunt (sem display).
- **Burden (carga) de TC** — impedância conectada ao secundário do TC; excesso de burden satura o TC.
- **Cerbo GX / Color Control / Venus OS** — gateway Victron que centraliza dados de monitores + inversor + MPPT + gerador.
- **Charged voltage (tensão de banco cheio)** — parâmetro BMV; valor para considerar banco 100% (ex: 14,0 V em chumbo, 13,8 V em lítio).
- **Charged detection time** — tempo que banco precisa ficar na tensão cheia para sincronizar SoC (ex.: 3 min).
- **Class 1,5 IEC 60051** — exatidão ±1,5% do fundo de escala; padrão em instrumentos náuticos de painel.
- **Coulomb counting** — método de integração de corrente no tempo para calcular Ah consumidos (base do BMV).
- **CT (Current Transformer / TC)** — transformador que reduz corrente alta AC a valor seguro para o instrumento (100A/5A típico).
- **Derating por temperatura** — redução de exatidão em temperatura fora de 0-40 °C típico.
- **Digital display (segmentos LED ou LCD)** — leitura numérica; padrão atual (analógico é obsoleto).
- **Exatidão ±0,5 V em voltímetro 12 V** — 4% de erro; inadequado para diagnóstico de SoC.
- **Fail-safe reading** — display mostra zero ou infinito em falha; exige design adequado.
- **Fluke 107 / 117 (CAT III 600 V)** — referência profissional de multímetro para uso com amperímetro AC/DC.
- **Frequencímetro (Hz meter)** — mede frequência AC; 60 Hz nominal Brasil, 50 Hz Europa.
- **GX Device** — família Victron Cerbo/CCGX/Venus; interface centralizada.
- **Hall effect sensor** — sensor magnético que mede corrente DC sem contato (alicate DC+AC).
- **Input impedance ≥ 10 MΩ** — voltímetro digital não carrega o circuito; analógico tem ~20 kΩ/V (carrega circuito).
- **Isolação galvânica (opto-isolador)** — separação elétrica entre instrumento e circuito medido; crítico em AC.
- **Logging (registro)** — monitor com memória interna (BMV-702/712) armazena histórico de SoC, corrente, temperatura.
- **Low battery alarm** — alarme programável em monitor (SoC < X% ou V < Y); aciona buzzer ou notificação.
- **Margin de proteção (CAT)** — CAT III 600 V protege em circuito nominal 600 V com transientes 6 kV.
- **Measurement transducer** — converte grandeza em sinal 4-20 mA ou 0-10 V para SCADA/controlador.
- **Monitor centralizado (dashboard)** — display grande que integra tensão, corrente, SoC, autonomia, temperatura (ex.: Simarine PICO).
- **mV/A (sensibilidade do shunt)** — ex.: 500A/75mV = 0,15 mV/A; BMV lê essa relação para converter.
- **Multi-shunt BMV (Victron Lynx)** — monitoramento de múltiplos bancos simultâneos.
- **Negativo bypass** — erro comum: negativo de algum equipamento conectado direto na bateria sem passar pelo shunt; resulta em SoC errado.
- **NMEA 2000 integration** — BMV, MPPT, inverter publicam dados em PGNs (Parameter Group Numbers) específicos.
- **Panel meter (instrumento de painel)** — instrumento embutido em painel de embarcação (72x72 mm, 96x96 mm, 48x48 mm padrão).
- **PGN 127508 (NMEA 2000)** — Battery Status: voltage, current, temperature.
- **PGN 127509 (NMEA 2000)** — Inverter Status.
- **Power factor (cosφ) em AC** — fator de potência (real vs aparente); medidor AC avançado o mede.
- **Precisão vs exatidão** — precisão = repetibilidade, exatidão = proximidade do valor verdadeiro; dois conceitos diferentes.
- **Recalibração de capacidade (battery capacity)** — parâmetro programável no BMV: "este banco tem X Ah"; incorreto = SoC errado.
- **Redundant monitor** — segunda medição (BMV + voltímetro analógico paralelo) para tolerância a falha.
- **RS-485 Modbus** — protocolo industrial para instrumentação (alternativa ao NMEA 2000).
- **Shunt resistivo (resistência de precisão mΩ)** — resistor calibrado; ex.: 500A/75mV = 0,00015 Ω; dissipa 37,5 W a 500 A.
- **Sincronização automática (Auto-sync)** — BMV sincroniza SoC a 100% quando detecta banco cheio (charged voltage + tail current + time).
- **SmartShunt Victron (500A/1000A/2000A)** — shunt com Bluetooth integrado; sem display próprio (lê no app VictronConnect).
- **SoC (State of Charge)** — % de carga atual do banco; valor primário do monitor.
- **SoH (State of Health)** — % da capacidade nominal que o banco ainda entrega; fim de vida típico = 80%.
- **Tail current** — corrente mínima abaixo da qual banco é considerado cheio (tipicamente 2-4% da capacidade nominal).
- **TC classe 0,5 IEEE C57.13** — transformador de corrente com exatidão 0,5%; padrão fiscal/industrial.
- **Transformer-based AC meter** — instrumento AC que usa TC interno (sem fio externo).
- **True RMS voltmeter AC** — lê tensão AC não-senoidal corretamente; essencial em inverter.
- **VE.Direct (Victron)** — protocolo serial proprietário para comunicação entre Victron + BMV + MPPT + Cerbo GX.
- **VictronConnect (app)** — aplicativo gratuito para configurar BMV, MPPT, inverter via Bluetooth.
- **VRM (Victron Remote Management)** — portal web gratuito para monitoramento remoto; exige GX Device + internet.
- **Zero-crossing detection** — detecção de passagem por zero em AC; usado em wattímetros e medidores de fator de potência.

## Como ensinar este tópico

**Progressão recomendada:**

1. Problema: "como você sabe se seu banco está descarregando?" — voltímetro vs monitor
2. Limitações do voltímetro: mostrar mesma bateria em diferentes estados com tensão parecida
3. O shunt: mostrar fisicamente o componente e explicar como mede corrente
4. Demonstração: BMV exibindo SoC, corrente e autonomia — valor imediato para o operador
5. Erro clássico: negativo bypassando o shunt — mostrar como o SoC fica errado
6. Voltímetro AC: por que verificar tensão e frequência antes de ligar cargas do cais

**Onde inserir no material:**

- Após banco de baterias e fontes de carga (o monitor fecha o loop de informação)
- Antes de diagnóstico elétrico (os instrumentos são a ferramenta base do diagnóstico)
- Junto com divisores de carga (dois bancos exigem monitoramento de cada um)

## Ideias de vídeos e aulas práticas

- **"Voltímetro simples vs BMV: o que cada um realmente te diz"** — comparativo prático
- **"Como instalar o Victron SmartShunt: passo a passo"** — tutorial de campo
- **"Por que o SoC do seu monitor está errado: diagnóstico de shunt bypassado"** — caso clínico
- **"Monitoramento AC no painel: voltímetro, amperímetro e frequencímetro"** — sistema completo
- **"Quanto tempo de autonomia meu banco tem? Calculando com o BMV"** — uso prático do monitor

## Diagramas sugeridos

- **Diagrama de instalação do shunt:** banco → shunt → barramento negativo → todos os equipamentos passando pelo shunt
- **Erro clássico:** negativo bypassando o shunt diretamente na bateria — ilustrar onde o erro ocorre
- **Painel completo DC+AC:** layout de painel com voltímetro DC, BMV, voltímetro AC, amperímetro AC e frequencímetro
- **Curva de tensão por SoC:** AGM vs Lítio LFP — mostrar por que voltímetro não funciona para lítio
- **Circuito de sinal do shunt:** shunt → fio sinal mV → BMV → display

## FAQ

**Voltímetro LED barato de painel funciona bem?**

Para indicação básica de presença de tensão, sim. Para diagnóstico de SoC, não — resolução de 0,1V e exatidão de ±0,3V são insuficientes para distinção entre 70% e 100% de carga em chumbo-ácido. Aceitável como indicador de alarme de tensão crítica; insuficiente como instrumento de controle de energia.

**O BMV Victron vale o preço?**

Em muitos cenários, sim, especialmente quando o banco é caro, a autonomia é crítica ou a química exige gestão mais disciplinada. O retorno vem da redução de abuso do banco e da melhora no diagnóstico, não de um número mágico único de capacidade.

**O shunt precisa ser da mesma marca do monitor?**

Não necessariamente, mas usar shunt do mesmo fabricante simplifica calibração e garantia. Victron BMV com shunt Victron 500A/75mV é o conjunto mais documentado e testado do mercado náutico atual.

**Preciso de amperímetro de painel se já tenho monitor BMV?**

O BMV já exibe corrente em seu display. Amperímetro de painel adicional é redundância útil apenas em painéis grandes onde o BMV fica distante da estação de manobra, ou quando se quer exibir a corrente de forma mais visível.

**Como saber se algum negativo está bypassando o shunt?**

Desligar todas as cargas conhecidas. Se o amperímetro ainda mostrar corrente saindo (ou se o banco descarrega com amperímetro mostrando zero), existe um negativo conectado diretamente na bateria, fora do circuito do shunt. Rastrear os negativos um por um.

## Integração com outras notas

- [[DC vs AC — Corrente Contínua e Alternada]]
- [[Diagrama Unifilar — Documentação do Sistema Elétrico]]
- [[Dimensionamento de Banco de Baterias — Cálculo de Autonomia]]
- [[Dimensionamento de Cabos DC — Cálculo Prático]]
- [[Fase e Neutro]]
- [[Ferramentas do Eletricista Náutico]]
- [[Inspeção de Cabos Terminais e Conexões]]
- [[Lei de Ohm e Cálculos Básicos]]

## Perguntas que esta nota responde

- O que é Voltímetro / Amperímetro (DC e AC) em instalações elétricas náuticas?
- Qual é a função de Voltímetro / Amperímetro (DC e AC) na embarcação?
