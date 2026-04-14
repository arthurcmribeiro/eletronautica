---
title: "Gerador (AC)"
note_type: "component"
domain: "30_Energia_e_Conversao"
source_file: "GERADOR (AC) 0ee19734f7fb82d89da2817e8a73a815.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "GERADOR (AC)"
seo_title: "Gerador (AC)"
seo_description: "Gerador AC é a fonte autônoma de energia da embarcação quando o cais não está disponível ou quando a demanda AC supera o que o banco/inversor pode entregar. Seu desempenho depende de frequência, tensão, AVR, governor, ventilação, exaustão e comutação correta entre fontes."
seo_keywords:
  - "Gerador"
  - "30 Energia e Conversao"
geo_queries:
  - "O que é Gerador (AC) em instalações elétricas náuticas?"
  - "Qual é a função de Gerador (AC) na embarcação?"
related_notes:
  - "Gerador (DC)"
  - "Alternador (DC)"
  - "Arranque"
  - "Aterramento"
  - "CAIS (Pier) (AC)"
  - "Carregador Elétrico para Tender e Jet Ski"
  - "Eólico (DC)"
  - "Inversora (DC To AC)"
  - "Proteção Dr"
  - "Placa Solar (DC)"
---

# Gerador (AC)

> [!abstract] Resumo técnico
> Gerador AC é a fonte autônoma de energia da embarcação quando o cais não está disponível ou quando a demanda AC supera o que o banco/inversor pode entregar. O ponto crítico não é só "gerar tensão", mas manter frequência, AVR, ventilação, exaustão e comutação corretas com o restante do sistema AC.

## O que é

O gerador marino é um grupo gerador composto por motor de combustão interna (diesel ou gasolina) acoplado a um alternador AC, formando uma unidade que produz energia elétrica 220V/60Hz de forma autônoma. É marinizado — adaptado para operar em ambiente marinho com resfriamento por água salgada e proteção contra corrosão e vibração.

**Diferença entre gerador marino e grupo gerador terrestre:**

- Marinização: sistema de resfriamento adaptado para água salgada (bomba de água salgada, trocador de calor, filtro de água salgada)
- Montagem antivibrante: coxins especiais que absorvem vibração e não transmitem para o casco
- Escape molhado (wet exhaust): mistura de gases de escape com água de resfriamento antes de expelir — reduz temperatura e ruído
- Sistema de proteção: desligamento automático por alta temperatura, baixa pressão de óleo, baixa tensão da bateria de partida

## Função

| Função | Detalhe |
| --- | --- |
| Fonte de 220V AC autônoma | Alimenta ar-condicionado, carregadores, tomadas, equipamentos de galley |
| Independência da marina | Navegar e ancorar com conforto completo sem shore power |
| Recarga do banco de baterias | Via carregador de bateria integrado ou externo |
| Operação do ar-condicionado | Principal justificativa de custo em embarcações de recreio no Brasil |

## Como aparece na prática

**Muito comum no Brasil:**

- Geradores Onan 4–8kW em lanchas de 28–40 pés
- Posicionados na casa de máquinas, com escape para o exterior do casco
- Operação manual: ligar via painel de controle do gerador ou via painel principal do barco
- Resfriamento por água salgada com filtro de crivo na entrada

**Comum em barcos importados:**

- Panda, Northern Lights ou Mastervolt em veleiros e trawlers europeus
- Partida remota integrada ao painel principal da embarcação
- Sistema de transferência automática entre shore power e gerador
- Bateria de partida dedicada separada do banco de serviço

**Mais presente em embarcações maiores/premium:**

- Geradores de 10–25kW para embarcações > 50 pés com múltiplos equipamentos AC
- Sistema de paralelo de geradores (dois geradores em paralelo para redundância)
- Controle de carga automático — liga e desliga cargas conforme a capacidade do gerador
- Silenciadores avançados (sound shield) — redução de ruído abaixo de 65 dB

## Fundamentos mínimos

**Relação RPM × Frequência:**

A frequência da energia gerada é diretamente proporcional à rotação do motor. No Brasil (60Hz):

- Motor 4 polos: 1.800 RPM = 60Hz (mais silencioso, mais eficiente em carga parcial)
- Motor 2 polos: 3.600 RPM = 60Hz (mais leve, mais compacto, maior desgaste)

Um motor funcionando em 1.750 RPM em vez de 1.800 RPM produz 58,3Hz — frequência incorreta que afeta equipamentos sensíveis. O governor (regulador de velocidade) mantém a RPM constante independentemente da carga aplicada.

**Escovado vs Brushless:**

- **Escovado:** usa escovas de carvão no rotor — mais antigo, mais simples de diagnosticar, escovas precisam de manutenção/troca periódica
- **Brushless:** sem escovas — mais confiável, menor manutenção, diagnóstico mais complexo

**Sistema de excitação:**

O alternador precisa de corrente de excitação para iniciar a geração. Geradores escovados usam resistor de excitação ou diodo (AVR). Geradores brushless usam excitadora independente (PMG — Permanent Magnet Generator).

## Características

| Parâmetro | Valor típico |
| --- | --- |
| Potência | 3,5kW a 25kW (recreio); acima para comercial |
| Tensão de saída | Conforme o padrão do conjunto e da embarcação |
| Frequência | 60Hz (Brasil) |
| Tensão de controle/partida | 12V ou 24V, conforme o conjunto |
| Consumo de combustível | 0,5–1,5 L/h por kW de carga (diesel) |
| Nível de ruído | 60–75 dB (com sound shield); 70–85 dB (sem) |
| Temperatura máxima de operação | 50–70°C no compartimento |

## Configurações comuns

**Gerador diesel simples (mais comum no Brasil):**

- Motor diesel monocilíndrico ou bicilíndrico acoplado a alternador brushless
- Resfriamento por água salgada com trocador de calor
- Escape molhado com caixa separadora de água
- Painel de controle simples: chave de partida, voltímetro, frequencímetro, hora-ímetro

**Gerador com controle integrado ao painel do barco:**

- Partida e parada via painel principal da embarcação
- Monitoramento de carga, temperatura e pressão de óleo no painel
- Alarme de falha integrado ao sistema de alarme geral do barco

**Sistema com transferência automática (ATS):**

- Chave automática que seleciona shore power ou gerador dependendo da disponibilidade
- Gerador liga automaticamente quando shore power falha (em embarcações de longa permanência)

## Marcas e referências

- **Onan (Cummins)** — a mais popular no Brasil, ampla rede de assistência, peças disponíveis, linhas MDKD e MDKBJ
- **Kohler Marine** — americana, qualidade premium, presente em embarcações importadas de alto padrão
- **Northern Lights (Lugger)** — robustos, usados em embarcações de trabalho e cruzeiro de longa distância
- **Panda** — alemã, muito compactos e silenciosos, presentes em veleiros e trawlers europeus
- **Mase** — italiana, boa qualidade, presente em embarcações mediterrâneas importadas
- **Mastervolt** — linha premium com integração completa ao ecossistema elétrico (CZone, alternadores, carregadores)
- **Swell Energy** — fabricante nacional brasileiro, alternativa de custo, crescente presença no mercado
- **Westerbeke** — americana tradicional, muito presente em veleiros de cruzeiro oceânico

## Componentes relacionados

- Motor de combustão (diesel ou gasolina marinizado)
- Alternador AC integrado (brushless ou escovado)
- AVR (Automatic Voltage Regulator) — mantém tensão de saída estável
- Governor (regulador de velocidade) — mantém RPM e frequência estáveis com variação de carga
- Sistema de resfriamento por água salgada (bomba, filtro, trocador de calor, termostato)
- Sistema de escape molhado (mistura gases com água, caixa separadora, mangueira de escape)
- Motor de arranque do gerador (12V DC)
- Bateria de partida do gerador (independente do banco de serviço)
- Painel de controle do gerador (partida, parada, monitoramento)
- Sistema de proteção automática (alta temperatura, baixa pressão de óleo, baixa tensão)

## Problemas mais frequentes

| Problema | Sintoma | Causa provável |
| --- | --- | --- |
| Não parte | Silêncio ou click ao acionar | Bateria de partida fraca, motor de arranque, solenóide de STOP travado |
| Parte mas não gera | Motor funcionando, sem 220V | AVR com defeito, excitadora queimada, regulador, diodos do alternador |
| Frequência incorreta | Equipamentos com comportamento estranho | Governor desregulado, motor fora de RPM, excesso de carga (fumaça preta) |
| Superaquecimento | Proteção desliga automaticamente | Filtro de água salgada entupido, rotor da bomba quebrado, trocador entupido |
| Baixa pressão de óleo | Proteção desliga, alarme | Nível de óleo baixo, sensor defeituoso, bomba de óleo com problema |
| Vibração excessiva | Ruído incomum, vibração no casco | Coxins antivibrantes desgastados, motor com problema mecânico |
| Para sozinho | Desligamento não programado | Superaquecimento, baixa pressão de óleo, baixa tensão da bateria, solenóide |

## Causas raiz

**Filtro de água salgada entupido (causa mais frequente de superaquecimento):**

O filtro de crivo na entrada da água salgada acumula algas, cracas e detritos. Em 1–3 temporadas sem limpeza, o fluxo reduz drasticamente. O trocador de calor não consegue resfriar o motor. A proteção de temperatura desliga o gerador. Solução simples — limpeza do filtro.

**Rotor da bomba de água salgada desgastado:**

O rotor de borracha da bomba de água salgada tem vida útil de 1–2 temporadas (ou 500–800 horas). Com o rotor desgastado, o fluxo de água cai mesmo com o filtro limpo. Síntoma idêntico ao filtro entupido — mas o filtro está limpo.

**Solenóide de STOP travado:**

O solenóide de parada para o motor ao ser acionado (elétrico para o motor). Quando trava na posição fechada, impede o motor de partir — não é falta de combustível, não é bateria fraca, é o solenóide mecanicamente travado. Teste: retirar o solenóide e partir o motor mecanicamente confirma o diagnóstico.

**Regulador de tensão (AVR) com falha:**

O AVR controla a tensão de saída do alternador. Com defeito, a tensão pode sair alta (>240V, queimando equipamentos), baixa (<200V, equipamentos não funcionam) ou instável. Antes de trocar o alternador inteiro, sempre verificar o AVR.

## Diagnóstico prático

**Gerador não gera energia (motor funcionando, sem 220V):**

```jsx
Passo 1: Verificar tensão de saída do alternador com voltímetro
Resultado normal: 210–230V AC em 60Hz
Sem tensão: problema no alternador ou circuito de excitação

Passo 2 (geradores escovados): Verificar escovas — desgaste > 50% → trocar
Passo 2 (geradores brushless): Verificar AVR — entrada DC de excitação deve estar presente

Passo 3: Testar excitação manual
Aplicar 12V DC diretamente no terminal de excitação do alternador
Se gerar tensão → problema no AVR ou circuito de excitação
Se não gerar → problema no alternador (bobinas ou diodos)

Passo 4: Verificar diodos de potência com multímetro
Diodo em curto → tensão de saída zero ou instável
```

**Gerador superaquece:**

```jsx
Passo 1: Verificar fluxo de água salgada na saída do escape
Normal: fluxo contínuo de água junto com os gases
Sem água: bomba ou filtro com problema

Passo 2: Verificar filtro de água salgada
Limpar se sujo (causa mais comum)

Passo 3: Com filtro limpo e sem água no escape:
Verificar rotor da bomba de água salgada (retirar e inspecionar)
Rotor desgastado, palhetas quebradas → substituir

Passo 4: Verificar termostato (válvula termostática)
Termostato travado fechado → motor superaquece mesmo com bomba funcionando
```

**Frequência incorreta:**

```jsx
Frequencímetro ou multímetro com função Hz:
Normal: 59–61 Hz em carga normal
Fora da faixa com carga: governor desregulado ou excesso de carga
Verificar carga total aplicada (W) vs capacidade do gerador (W)
Se carga > 80% da capacidade: fumaça preta, RPM cai, frequência cai
```

## Boas práticas profissionais

- Realizar manutenção preventiva no ciclo: mensal (visual), trimestral (filtros e fluidos), anual (revisão completa)
- Trocar rotor da bomba de água salgada anualmente ou a cada 500 horas
- Nunca operar o gerador com menos de 30–40% de carga por período prolongado (wet stacking — acúmulo de carbono)
- Verificar e anotar tensão, frequência e temperatura de saída como baseline para comparação futura
- Manter anôdo do trocador de calor — protege internamente contra corrosão galvânica
- Testar o gerador por pelo menos 30 minutos em carga real (AC ligado) antes de longas viagens

## Cuidados de instalação

- Montagem em coxins antivibrantes adequados ao peso do gerador — nunca rigidamente fixado
- Escape: caixa separadora de água (waterlock) instalada abaixo do nível de saída do escape no motor — evita retorno de água para o motor
- Entrada de água salgada: filtro de crivo de fácil acesso para limpeza (manutenção frequente)
- Ventilação do compartimento: o gerador consome ar para combustão — compartimento vedado sufoca o motor
- Bandeja de contenção de óleo: obrigatória para conter vazamentos — exigência de segurança e meio ambiente
- Combustível: gerador deve ter linha de combustível independente do motor principal ou linha compartilhada com válvula de isolamento

## Cuidados de uso

- Nunca operar com o compartimento completamente fechado — o motor precisa de ar fresco
- Não desligar abruptamente com carga máxima — reduzir a carga antes de desligar
- Operação mínima mensal: pelo menos 30 minutos em carga real evita problemas de armazenamento
- Verificar nível de óleo e refrigerante antes de cada uso prolongado
- Em parada por temporada: tratar o combustível com aditivo estabilizador — diesel degrada em 3–6 meses

## Erros comuns

**Trocar o alternador inteiro antes de verificar o AVR:**

O AVR é uma peça de R$300–800. O alternador novo custa R$3.000–15.000. Testar o AVR primeiro sempre.

**Ignorar o filtro de água salgada:**

"Gerador superaqueceu — deve ser o trocador." O filtro é a causa número 1 e a solução mais barata. Verificar primeiro.

**Operar em carga muito baixa (wet stacking):**

Gerador rodando horas com apenas a luz do painel ligada. A câmara de combustão não atinge temperatura ideal — acúmulo de carbono, óleo não queima, desgaste prematuro.

**Não testar o solenóide de STOP:**

"Motor não parte — bateria fraca." Trocar a bateria e o motor ainda não parte. O solenóide estava travado fechando o injetor/borboleta. Teste simples evita troca desnecessária.

**Remover o solenóide de STOP permanentemente:**

Feito para "resolver" o problema do solenóide travado. Sem o solenóide, não é possível parar o motor eletricamente — apenas mecanicamente (tampando a entrada de ar). Risco grave de emergência.

## Relação com outros sistemas

- **Shore power:** gerador é a alternativa ao shore power em navegação e fundeio
- **Carregador de bateria:** principal carga do gerador — usa a energia AC para recarregar o banco DC
- **Ar-condicionado:** maior carga AC a bordo — dimensiona o gerador na maioria das embarcações
- **Painel AC:** o gerador alimenta o mesmo painel que o shore power — transferência automática ou manual
- **Banco de baterias:** gerador usa banco para partir — bateria de partida dedicada é o ideal
- **Aterramento:** o gerador pode constituir fonte derivada e exigir tratamento explícito do PE e do bond neutro-terra
- **Proteção Dr:** a estratégia diferencial/leakage precisa considerar a topologia do gerador e da transferência entre fontes
- **Sistema de alarme:** temperatura, pressão de óleo e falha do gerador devem integrar o alarme geral

## Brasil x Internacional

| Aspecto | Brasil | Internacional |
| --- | --- | --- |
| Marca mais comum | Onan | Onan, Kohler, Northern Lights (EUA); Panda, Mase (Europa) |
| Tensão de saída | 220V 60Hz | 120V/240V 60Hz (EUA); 230V 50Hz (Europa) |
| Manutenção preventiva | Geralmente negligenciada | Ciclos rigorosos por hora de uso |
| Diagnóstico antes de trocar | Raro — troca direta | Diagnóstico sistemático primeiro |
| Anôdo do trocador | Frequentemente esquecido | Inspecionado anualmente |
| Wet stacking | Muito comum | Prevenido com carga mínima de 40% |

**Realidade brasileira:** O gerador é tratado como "ou funciona ou não funciona." Manutenção preventiva é negligenciada até a primeira falha grave. A maioria dos problemas é evitável com limpeza do filtro de água salgada, troca anual do rotor e verificação do AVR.

## Normas aplicáveis

- **ABYC E-11** — AC Electrical Systems (instalação do gerador, aterramento, GFCI)
- **ABYC A-33** — Exhaust Systems (sistema de escape molhado, waterlock, retorno de água)
- **NFPA 302** — Fire Protection for Pleasure and Commercial Motorcraft
- **ABNT NBR 5410** e família **ABNT/IEC** aplicável — referência complementar para princípios de baixa tensão, identificação e proteção
- **NORMAM-211** — referencial regulatório brasileiro a ser confirmado primeiro para amadores, embarcações de esporte e recreio e universo correlato

## Como ensinar este tópico

**Sequência recomendada:**

1. Mostrar o gerador fisicamente — identificar motor, alternador, bomba de água, trocador, sistema de escape
2. Explicar a relação RPM × frequência — com frequencímetro ao vivo
3. Percorrer o circuito de água salgada: entrada → filtro → bomba → trocador → escape
4. Demonstrar diagnóstico de "não gera": excitação manual → AVR → escovas → diodos
5. Mostrar a manutenção preventiva real: troca do rotor, limpeza do filtro, verificação do anôdo

**Conceito-chave para fixar:**

"O gerador é um motor de combustão com alternador AC. Problemas mecânicos (água, combustível, óleo) são mais frequentes que problemas elétricos. Diagnosticar a mecânica antes de mexer na elétrica."

## Ideias de vídeos

- **"Gerador superaqueceu: diagnóstico em 5 passos"** — filtro → rotor → trocador → termostato
- **"Gerador não gera: como diagnosticar o alternador"** — excitação manual, AVR, escovas, diodos
- **"Troca do rotor da bomba de água salgada"** — manutenção mais crítica e mais simples do gerador
- **"Frequência do gerador: o que acontece quando sai de 60Hz"** — consequências práticas
- **"Escovado vs Brushless: como diagnosticar cada tipo"** — diferenças de diagnóstico na prática
- **"Manutenção preventiva completa do gerador Onan"** — óleo, filtros, anôdo, rotor, correias

## Diagramas sugeridos

- Circuito de resfriamento por água salgada: entrada → filtro → bomba → trocador de calor → escape molhado
- Circuito elétrico de geração: alternador → AVR → disjuntor geral → painel AC
- Diagrama de excitação: PMG ou resistor → AVR → campo do rotor → tensão de saída
- Fluxograma de diagnóstico de "não gera": verificações em sequência lógica
- Esquema de instalação completa: gerador + escape + combustível + elétrico + ventilação

## FAQ

**Quantas horas roda um gerador marino antes de revisão?**

Manutenção de óleo e filtro: a cada 250 horas. Revisão completa (válvulas, correias, rotor): a cada 500–1.000 horas. Com manutenção adequada, vida útil de 5.000–10.000 horas é possível.

**Posso usar óleo automotivo no gerador marino?**

Não recomendado. Use óleo marino ou conforme especificação do fabricante. Motores de gerador operam em temperaturas e condições diferentes — óleo incorreto pode reduzir vida útil significativamente.

**O gerador pode operar com a embarcação em movimento?**

Sim, desde que o sistema de resfriamento funcione corretamente com a embarcação em velocidade. Em algumas velocidades, a pressão de entrada de água salgada aumenta — verificar que o sistema suporta.

**Qual a carga mínima para operar o gerador?**

Mínimo 30–40% da capacidade nominal. Abaixo disso, o motor não atinge temperatura ideal de combustão — wet stacking progressivo. Se precisar operar em carga baixa, ligar cargas temporariamente (aquecedor, secador) para subir a carga.

**O gerador pode funcionar em paralelo com o shore power?**

Nunca, sem sistema de interlock. Conectar shore power e gerador em paralelo sem sincronização causa dano imediato a ambos (diferença de fase e frequência). O interlock elétrico ou mecânico é obrigatório para prevenir isso.

## Integração com outras notas

- [[Gerador (DC)]]
- [[Alternador (DC)]]
- [[Arranque]]
- [[Aterramento]]
- [[CAIS (Pier) (AC)]]
- [[Carregador Elétrico para Tender e Jet Ski]]
- [[Eólico (DC)]]
- [[Inversora (DC To AC)]]
- [[Proteção Dr]]
- [[Placa Solar (DC)]]

## Perguntas que esta nota responde

- O que é Gerador (AC) em instalações elétricas náuticas?
- Qual é a função de Gerador (AC) na embarcação?
