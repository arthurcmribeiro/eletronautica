---
title: "Voltímetro / Amperímetro (DC e AC)"
note_type: "technical-note"
domain: "10_Fundamentos_e_Projeto"
source_file: "VOLTIMETRO AMPERIMETRO (DC) e (AC) e7d19734f7fb827bba7a819fb2653ee0.md"
status: "technical-review-l1"
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

## Normas e referências técnicas

- **ABYC E-11** — AC and DC Electrical Systems on Boats: instrumentação recomendada, shunts, proteção de circuitos de medição
- **ISO 13297** — Electrical systems on recreational craft
- **ABNT NBR 16033** — Instalações elétricas em embarcações
- Documentação Victron: Application Note "BMV Battery Monitor Installation" — referência prática completa

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
