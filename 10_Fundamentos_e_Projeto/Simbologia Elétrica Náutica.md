---
title: "Simbologia Elétrica Náutica"
note_type: "reference"
domain: "10_Fundamentos_e_Projeto"
source_file: "SIMBOLOGIA ELÉTRICA NÁUTICA 33a19734f7fb81fbbb62e50e4f846193.md"
status: "technical-review-l1"
aliases:
  - "SIMBOLOGIA ELÉTRICA NÁUTICA"
seo_title: "Simbologia Elétrica Náutica"
seo_description: "SIMBOLOGIA ELÉTRICA NÁUTICA — Os símbolos gráficos usados em diagramas elétricos náuticos. Leitura universal: um símbolo certo diz mais que um parágrafo de texto."
seo_keywords:
  - "Simbologia"
  - "10 Fundamentos e Projeto"
geo_queries:
  - "O que é Simbologia Elétrica Náutica em instalações elétricas náuticas?"
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

# Simbologia Elétrica Náutica

> [!abstract] Resumo técnico
> SIMBOLOGIA ELÉTRICA NÁUTICA — Os símbolos gráficos usados em diagramas elétricos náuticos. Leitura universal: um símbolo certo diz mais que um parágrafo de texto.

## O que é

Simbologia elétrica é o conjunto de representações gráficas padronizadas usadas em diagramas e esquemas elétricos para representar componentes, conexões e funções de um circuito. Assim como a música tem partituras, a elétrica tem diagramas — e a simbologia é a linguagem deles.

Os desenhos abaixo são ilustrações didáticas da ideia de cada símbolo; em projeto formal, a forma gráfica final deve seguir a biblioteca/padrão adotado (IEC, ANSI/IEEE ou biblioteca do software).

## Por que padronizar

- Um símbolo é universal — independe do idioma
- Facilita comunicação entre profissionais de diferentes países
- Reduz erros de interpretação
- Obrigatório em projetos profissionais e documentação técnica

## Símbolos fundamentais DC

| Símbolo | Nome | Descrição |
| --- | --- | --- |
| ─┤├─ (dois traços) | Bateria (célula) | Um par de traços = uma célula |
| ─┤┤┤├─ (múltiplos traços) | Banco de baterias | Múltiplas células = banco |
| ─/─ | Chave aberta (switch) | Circuito aberto / desligado |
| ─/─ (com mola) | Chave normalmente aberta (NA) | Estado padrão = aberto |
| ─┤─ | Chave normalmente fechada (NF) | Estado padrão = fechado |
| ─[X]─ | Fusível | Elemento de proteção |
| ─[─]─ | Disjuntor | Proteção resetável |
| ─(R)─ | Resistor / carga resistiva | Elemento com resistência |
| ○ | Lâmpada / LED | Carga luminosa |
| ─(M)─ | Motor elétrico | Carga motora |
| ─◁─ | Diodo | Conduz em uma direção |
| ─◁├─ | Diodo Zener | Condução em tensão específica |
| ─[≡]─ | Relé | Contato controlado por bobina |
| ⏚ | Terra / GND | Referência de potencial zero |
| ─→─ | Seta de corrente | Direção convencional da corrente |

## Símbolos AC

| Símbolo | Nome | Uso |
| --- | --- | --- |
| ─~─ | Fonte AC | Gerador ou shore power |
| ⊗ | Transformador | Shore isolation transformer |
| ─[≈]─ | Inversor | DC → AC |
| ─[AC]─ | Carga AC genérica | Equipamento de corrente alternada |
| ─[DR]─ | Dispositivo diferencial | Proteção contra corrente residual/falha à terra |
| N | Neutro | Condutor de retorno AC |
| L | Fase (Live) | Condutor energizado AC |
| PE / ⏚ | Terra de proteção (Protective Earth) | Terra AC de segurança |

## Símbolos de conexão e fiação

| Símbolo | Significado |
| --- | --- |
| Ponto sólido (●) no cruzamento | Os fios se conectam (junção) |
| Cruzamento sem ponto | Os fios se cruzam sem conectar |
| Linha contínua | Condutor elétrico (cabo) |
| Linha tracejada | Cabo de controle / sinal / blindagem |
| Linha dupla | Condutor de potência (alta corrente) |
| Retângulo com número | Componente numerado (referência ao projeto) |
| Flecha com rótulo | Conexão que continua em outra folha |

## Símbolos de medição e sensores

| Símbolo | Componente |
| --- | --- |
| ─(V)─ | Voltímetro |
| ─(A)─ | Amperímetro |
| ─(Ω)─ | Ohmímetro |
| ─(W)─ | Wattímetro |
| ─(T)─ | Termômetro / sensor de temperatura |
| □ com antena | Sensor sem fio / NMEA wireless |
| Diamante | Sensor genérico |

## Padrões de simbologia

**IEC 60617 (padrão internacional / europeu / brasileiro):**

- Usado na NBR e na maioria dos softwares europeus
- Símbolos mais estilizados

**ANSI/IEEE (padrão americano):**

- Usado em normas ABYC e equipamentos americanos
- Alguns símbolos diferentes do IEC (ex: resistor = retângulo no IEC, zigue-zague no ANSI)

**Na náutica brasileira:**

A maioria dos diagramas mistura os dois padrões. O importante é que o diagrama tenha legenda explicando os símbolos usados.

## Cores padrão em diagramas

As cores abaixo são convenções frequentes, não um idioma universal. O ponto obrigatório é haver legenda clara e consistência interna.

| Cor da linha | Significado |
| --- | --- |
| Vermelho | Positivo DC (+) |
| Preto | Negativo DC (−) |
| Verde | PE / terra de proteção e, em alguns diagramas, bonding |
| Azul | Neutro AC (N) |
| Marrom ou laranja | Fase AC (L) |
| Amarelo | Sinal / controle |
| Cinza | Cabo de sinal / dado |

## Simbologia específica náutica

| Símbolo | Componente |
| --- | --- |
| ─[VSR]─ | Voltage Sensing Relay (relé de carga) |
| ─[ANL]─ | Fusível ANL principal |
| ─[SHUNT]─ | Shunt de monitor de bateria |
| ⚓ | Ponto de aterramento / bonding náutico |
| ─[ISO]─ | Transformador de isolamento |
| ~[INV]~ | Inversor DC/AC |
| ─[CHG]─ | Carregador de bateria |
| ─[MPPT]─ | Controlador MPPT solar |

## Como aplicar em diagramas reais

**Hierarquia visual:**

- Fonte de energia no topo (bateria, shore power)
- Proteções logo abaixo (fusíveis, disjuntores)
- Cargas na base (equipamentos)
- Retorno ao longo do lado inferior

**Identificação de componentes:**

- Cada componente recebe um código alfanumérico (ex: F1 = fusível 1, CB1 = circuit breaker 1, M1 = motor 1)
- Código corresponde à lista de componentes do projeto

## Boas práticas profissionais

- Incluir legenda completa em qualquer diagrama entregue ao cliente
- Usar software de CAD elétrico com biblioteca de símbolos padrão (QElectroTech, AutoCAD Elec.)
- Não inventar símbolos — usar os padronizados para garantir leitura universal
- Quando misturar padrões IEC e ANSI: documentar na legenda

## Como ensinar este tópico

**Sequência recomendada:**

1. Apresentar os 10 símbolos mais comuns — quiz visual (mostrar símbolo, nomear)
2. Identificar símbolos em um diagrama real de embarcação
3. Construir um diagrama simples ao vivo (3–4 componentes) usando símbolos corretos
4. Exercício: dado um circuito verbal ("bateria + fusível + chave + lâmpada"), desenhar o diagrama

**Conceito-chave para fixar:**

"Simbologia é o idioma dos diagramas. Quem não conhece o idioma não consegue ler a mensagem."

## FAQ

**Há um padrão único de simbologia náutica?**

Não existe padrão exclusivo para náutica. Usam-se os padrões gerais IEC ou ANSI/IEEE, com símbolos adicionais criados pelos fabricantes (Victron, Garmin) para seus produtos específicos.

**Posso usar qualquer símbolo, desde que tenha legenda?**

Tecnicamente sim — uma legenda clara resolve ambiguidades. Mas usar símbolos não-padrão dificulta a leitura por outros profissionais e cria risco de erro de interpretação.

**QElectroTech tem biblioteca de símbolos náuticos?**

Tem biblioteca IEC geral. Não tem símbolos náuticos específicos por padrão — mas é possível criar e importar símbolos customizados.

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

- O que é Simbologia Elétrica Náutica em instalações elétricas náuticas?
