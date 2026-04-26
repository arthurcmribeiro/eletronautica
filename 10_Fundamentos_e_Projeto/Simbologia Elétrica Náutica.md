---
title: "Simbologia Elétrica Náutica"
note_type: "reference"
domain: "10_Fundamentos_e_Projeto"
source_file: "SIMBOLOGIA ELÉTRICA NÁUTICA 33a19734f7fb81fbbb62e50e4f846193.md"
status: "premium-l3"
fase_6_reescrita: 98
reviewed_on: "2026-04-26"
review_jurisdiction: "Brasil + EUA + Internacional + Europa"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://webstore.iec.ch/publication/2697"
  - "https://www.iso.org/"
review_level: "engineering-curated"
aliases:
  - "SIMBOLOGIA ELÉTRICA NÁUTICA"
  - "Marine electrical symbols"
  - "Símbolos elétricos marine"
  - "Símbolos diagrama unifilar"
  - "IEC 60617 symbols"
seo_title: "Simbologia elétrica náutica: IEC 60617, ANSI/IEEE 315, ABNT NBR 5444, símbolos diagrama unifilar marine"
seo_description: "Guia técnico premium dos símbolos elétricos em diagramas náuticos: padrão IEC 60617 (internacional) × ANSI/IEEE 315 (USA) × ABNT NBR 5444 (Brasil) — bateria, fusível, disjuntor, chave, motor, transformador, gerador, capacitor, indutor, terra/bonding/PE, lâmpada, relé, semicondutor — interpretação correta + boas práticas de leitura."
seo_keywords:
  - "simbologia elétrica náutica"
  - "marine electrical symbols"
  - "IEC 60617"
  - "ANSI IEEE 315"
  - "ABNT NBR 5444"
  - "símbolo bateria fusível disjuntor"
  - "diagrama unifilar marine"
geo_queries:
  - "Como ler diagrama elétrico náutico?"
  - "Diferença entre símbolo IEC e ANSI?"
  - "Por que o símbolo de bateria tem barras desiguais?"
  - "Símbolo de bonding vs PE vs terra: qual é qual?"
  - "Como representar disjuntor DC vs AC no diagrama?"
  - "Símbolos brasileiros são iguais aos internacionais?"
  - "Onde encontrar tabela de símbolos completa?"
  - "Simbologia para LED diferente de lâmpada incandescente?"
normas_citadas:
  - "ABYC E-11 (AC and DC Electrical Systems on Boats)"
  - "ABYC TE-30 (Electronic Equipment Installation)"
  - "IEC 60617 (Graphical symbols for diagrams) — referência internacional"
  - "IEC 81714-1/-2 (Documentation symbols)"
  - "IEC 61175 (Designations for signals and connections)"
  - "IEC 81346-1/-2 (Industrial systems — structuring principles)"
  - "ISO 7000 (Graphical symbols for use on equipment)"
  - "ISO 14617 series (Graphical symbols for diagrams)"
  - "ANSI/IEEE Std 315 (Graphical Symbols for Electrical and Electronics Diagrams) — referência USA"
  - "ANSI Y32.2 (legacy USA)"
  - "DIN EN 60617 (German adoption)"
  - "JIS C 0617 (Japan)"
  - "ABNT NBR 5444 (Símbolos gráficos para instalações elétricas prediais)"
  - "ABNT NBR 5410 (Instalações elétricas BT)"
  - "ABNT NBR 14728"
  - "ABNT NBR ISO 7000"
  - "ABNT NBR IEC 60617"
  - "DPC NORMAM-211/DPC"
  - "EU Directive 2014/35/EU (LVD)"
  - "EU 2013/53/EU (RCD)"
related_notes:
  - "Lei de Ohm e Cálculos Básicos"
  - "Princípios Náuticos"
  - "Tipos de Embarcação"
  - "DC vs AC — Corrente Contínua e Alternada"
  - "Diagrama Unifilar — Documentação do Sistema Elétrico"
  - "Leitura de Diagramas e Esquemas Elétricos"
  - "Projeto Elétrico de Embarcação — Passo a Passo"
  - "Referência Rápida — Valores de Campo"
  - "Ferramentas do Eletricista Náutico"
  - "Cabeamento Náutico"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Disjuntores (DC) e (AC)"
  - "Bonding — Sistema de Interligação de Massas"
  - "Aterramento"
---

# Simbologia Elétrica Náutica

> [!abstract] Resumo técnico
> A **simbologia elétrica náutica** é a **linguagem visual padronizada** usada em **diagramas unifilares, esquemas elétricos, plantas de instalação** e documentação técnica de embarcações. **Existem 3 padrões dominantes simultâneos**: **IEC 60617** (internacional / Europa / Brasil — referência global), **ANSI/IEEE Std 315** (USA — diferenças significativas em alguns símbolos), e **ABNT NBR 5444 + IEC 60617** (Brasil — adopta IEC com algumas adições). **Em embarcação multinacional ou em manutenção de barco importado, identificar qual padrão foi usado no diagrama é o primeiro passo da leitura.** Símbolos críticos a dominar: **bateria** (barras alternadas longa/curta = pólo +/-), **fusível** (retângulo simples vs ANSI fuse), **disjuntor DC vs AC** (formas distintas), **chave geral** (com e sem retorno por mola), **motor** (M em círculo), **gerador** (G em círculo), **transformador** (2 indutores acoplados), **capacitor** (paralelas), **indutor** (loops ou hachura), **terra / bonding / PE** (3 símbolos distintos!), **lâmpada / LED** (X vs símbolo dedicado), **relé** (bobina + contatos NA/NF), **semicondutor** (diodos, LEDs, transistores). Padrões: **ABYC E-11** + **IEC 60617** + **ANSI/IEEE 315** + **ABNT NBR 5444**.

> [!tldr] TL;DR — 9 regras inegociáveis
> 1. **Identificar o padrão (IEC × ANSI × NBR)** ANTES de interpretar o diagrama. Diferenças críticas em fusível, disjuntor, indutor — leitura errada gera diagnóstico errado.
> 2. **Bateria (símbolo universal):** barras alternadas longa (+) / curta (-) — múltiplos pares = múltiplas células / mais tensão. Em barco recreativo, geralmente "12V" ou "24V" anotado externamente.
> 3. **Fusível:** retângulo IEC simples × ANSI "S" ou retângulo com diagonal. Marine usa frequentemente IEC.
> 4. **Disjuntor DC ≠ AC ≠ termomagnético.** Em barco: distinguir é crítico (DC sem zero-crossing precisa de disjuntor específico). Símbolos podem ser diferentes (vide [[Disjuntores (DC) e (AC)]]).
> 5. **Aterramento (3 símbolos distintos!):** **Terra (earth/ground)** — 3 linhas horizontais decrescentes; **Chassi (chassis ground)** — triângulo invertido; **PE (Protective Earth)** — círculo com 3 linhas; **Bonding** — geralmente convenção interna (vide [[Bonding — Sistema de Interligação de Massas]]). Não confundir em barco — Bonding ≠ PE ≠ Terra.
> 6. **Motor / Gerador:** M / G em círculo. Adicionar "DC" / "AC" para clareza. M com setas representa direção de rotação.
> 7. **Polaridade DC** crítica em diagramas marine — sempre indicar + e - claramente; ABYC E-11 padroniza vermelho (+) / preto ou amarelo (-).
> 8. **Convenção de cores ABYC E-11.4 e ABNT NBR 14728** vs IEC: USA usa verde para bonding; UE/BR usa verde-amarelo para PE; convenções diferem — anotar no diagrama.
> 9. **Diagrama unifilar marine** simplifica circuitos AC trifásicos em uma linha; útil em barcos comerciais com gerador 3-phase + shore-power; cabeamento real é multi-conductor.

> [!danger] Cenários de risco
> - **Confusão de padrão (IEC × ANSI):** instalador usa diagrama ANSI USA + interpreta como IEC → conexão errada de fusível/disjuntor → curto / fogo. **Prevenção:** anotar padrão na legenda do diagrama; treinar tripulação.
> - **PE confundido com Bonding em barco:** instalador residencial conecta "terra" do shore-power diretamente ao bonding → corrente galvânica + corrosão acelerada de hélice/eixos. **Prevenção:** vide [[Neutro, Negativo, Terra, PE, Bonding e DR — Diferenças Críticas]]; isolador galvânico.
> - **Polaridade DC invertida** (sinais + e - trocados no diagrama): instalação inverte polos → eletrônica destruída instantaneamente. **Prevenção:** documentação rigorosa; fusível polarized; teste antes de energizar.
> - **Símbolo de fusível desatualizado:** diagrama legacy com símbolo ANSI Y32.2 (não-padrão moderno) → técnico jovem não reconhece → ignora proteção em manutenção. **Prevenção:** atualizar diagrama; legenda de símbolos no documento.
> - **Símbolo de motor sem indicação DC/AC** + barco com ambos: tecnico instala disjuntor errado → DC arc não interrompido. **Prevenção:** sempre indicar tensão + tipo (DC/AC); manter consistência.
> - **Indutor confundido com bobina de relé** em diagrama mal feito: tecnico testa relé como se fosse fusível → não detecta falha real. **Prevenção:** símbolos padronizados; legenda; revisar diagrama em projeto.
> - **Diagrama defasado da realidade:** modificações elétricas sem atualizar diagrama → próxima manutenção encontra discrepância → trial-and-error → erros. **Prevenção:** atualizar diagrama com cada modificação; data + responsável.
> - **Sigla / abbreviation não documentada:** "MCB" "MCCB" "RCBO" "ELCI" usados sem explicação → técnico não-especialista não interpreta. **Prevenção:** legenda de abreviações no diagrama.
> - **Cores no diagrama divergentes da realidade:** diagrama mostra "vermelho = +" mas barco tem cabos onde isso foi violado → ambiguidade em diagnóstico. **Prevenção:** ABYC E-11.4 cores rigorosas; documentação.

## Padrões dominantes — visão comparativa

### IEC 60617 (Internacional / Europa / Brasil)

- **Família IEC 60617** — referência global; mais simbologia abstrata.
- **Adoptado por:** Europa, Brasil (ABNT NBR IEC 60617), Japão (JIS C 0617), Índia, China, etc.

### ANSI/IEEE Std 315 (USA)

- **Sucessor de ANSI Y32.2 (legacy).**
- **Algumas diferenças significativas:** fusível ("S" ou retângulo com diagonal), indutor (loop), capacitor não-polarizado.

### ABNT NBR 5444 (Brasil)

- **Adopta IEC 60617** com algumas adições nacionais (instalações prediais).
- **Em barco brasileiro:** ABNT NBR 14728 + ABNT NBR IEC 60617 + algumas convenções ABYC quando se segue padrão americano.

## Tabela de símbolos críticos (referência)

### Fontes de energia

| Item | IEC 60617 | ANSI/IEEE 315 | Notas |
|------|-----------|----------------|-------|
| **Bateria 1 célula** | `─\|\|─` (longa-curta) | `─\|\|─` | Universal |
| **Bateria múltiplas células** | `─\|\|\|\|─` | `─\|\|\|\|─` | Mais células = mais V |
| **Bateria com terminais marcados** | `+ ─\|\|─ −` | `+ ─\|\|─ −` | Polaridade explícita |
| **Gerador DC** | `─⊕─` (G dentro de círculo) | `─G─` (círculo) | "DC" anotado externamente |
| **Gerador AC** | `─⊗─` (G + til) | `─G_~_─` | "AC" + frequência |
| **Painel solar** | Retângulo com diagonal hatching | Mesmo | Múltiplos retângulos = string |
| **Aerogerador (eólico)** | Símbolo de turbina | Mesmo | Geralmente texto auxiliar |
| **Motor genérico** | `─Ⓜ─` (M em círculo) | `─M─` | + DC/AC + V + W |

### Proteção

| Item | IEC 60617 | ANSI/IEEE 315 |
|------|-----------|----------------|
| **Fusível** | Retângulo `─█─` | "S" ou retângulo com diagonal |
| **Fusível com indicador** | Retângulo + linha | Variação |
| **Disjuntor termomagnético (residencial)** | Retângulo com seta diagonal | Quadrado com x |
| **Disjuntor DC marine (ANL/MIDI)** | Retângulo + DC | Variação |
| **Disjuntor diferencial (RCD/ELCI)** | Retângulo com Δ ou "DR" | "GFCI" / "ELCI" |
| **Sobrecarga térmica** | Retângulo com curva térmica | Variação |
| **Surge protector** | Triângulo com seta | Variação |

### Comutação

| Item | IEC 60617 | ANSI/IEEE 315 |
|------|-----------|----------------|
| **Chave simples (SPST)** | Linha angular interrompida | Mesmo |
| **Chave de 2 posições (SPDT)** | Linha + 2 contatos | Mesmo |
| **Chave de bateria (rotativa OFF/1/2/BOTH)** | Setor circular | Variação |
| **Relé bobina** | Retângulo com identificador | Mesmo |
| **Contato NA (Normally Open)** | Linha angular | Mesmo |
| **Contato NF (Normally Closed)** | Linha com X | Mesmo |
| **Contator (multi-pole)** | Múltiplos contatos linkados | Mesmo |

### Carga / Consumidores

| Item | IEC 60617 | ANSI/IEEE 315 |
|------|-----------|----------------|
| **Lâmpada genérica** | X em círculo | Círculo com loop |
| **LED (Light Emitting Diode)** | Diodo com 2 setas saindo | Mesmo |
| **Resistor** | Retângulo `─█─` | Zigzag (legacy) ou retângulo |
| **Capacitor** | 2 paralelas iguais (não-polarizado) | Mesmo |
| **Capacitor polarizado** | 1 paralela curva + 1 reta | Mesmo |
| **Indutor / bobina** | Loops `─⊃⊃⊃⊃─` ou retângulo | Loops (sempre) |
| **Transformador** | 2 indutores acoplados | Mesmo |
| **Aquecedor / resistência** | Retângulo com hatching | Variação |
| **Relé estado sólido (SSR)** | Símbolo composto | Mesmo |

### Aterramento (3 símbolos críticos)

| Item | IEC 60617 | ANSI/IEEE 315 |
|------|-----------|----------------|
| **Terra (earth / ground)** | 3 linhas horizontais decrescentes | Mesmo |
| **Chassi (chassis ground)** | Triângulo invertido cheio | Mesmo |
| **PE (Protective Earth)** | Círculo com 3 linhas | Variação |
| **Bonding (em diagrama marine)** | Geralmente convenção interna ou letra "BG" | Mesmo |
| **Earth com Ω (impedance)** | Hatched | Variação |

### Conectores e terminais

| Item | IEC 60617 |
|------|-----------|
| **Terminal / borne** | Círculo cheio |
| **Conexão entre fios** | Ponto cheio em cruzamento |
| **Cruzamento sem conexão** | Ponte (overpass) |
| **Conector multi-pino** | Retângulo com pinos |

### Semicondutores

| Item | IEC 60617 |
|------|-----------|
| **Diodo** | Triângulo apontando + linha |
| **LED** | Diodo + 2 setas |
| **Foto-diodo** | Diodo + 2 setas entrando |
| **Zener** | Diodo + linha em zigzag no cátodo |
| **Transistor NPN/PNP** | Símbolos clássicos |
| **MOSFET** | N-channel / P-channel específicos |

## Convenção de cores (ABYC E-11.4 vs IEC vs ABNT)

| Função | ABYC E-11.4 (USA marine) | IEC (geral europeu) | ABNT NBR 14728 (BR marine) |
|---------|---------------------------|--------------------|------------------------------|
| **Positivo DC (+)** | Vermelho | Vermelho | Vermelho |
| **Negativo DC (−)** | Preto OU amarelo (preferido) | Preto | Preto |
| **Bonding** | Verde | (não definido) | Verde |
| **PE (AC protective earth)** | Verde + amarelo (faixa) | Verde + amarelo | Verde + amarelo |
| **Neutro AC** | Branco | Azul | Azul |
| **Fase AC (single)** | Preto | Marrom | Marrom |
| **Fase 1/2/3 (trifásico)** | Preto / Vermelho / Azul | Marrom / Preto / Cinza | Marrom / Preto / Cinza |

> [!warning] Mistura de padrões em barco multinacional
> Yacht importado USA com retrofit BR: documentar a convenção usada; usar etiquetas em cabos; manter consistência interna.

## Boas práticas de leitura de diagrama (ver [[Leitura de Diagramas e Esquemas Elétricos]])

1. **Identificar padrão e legenda** primeiro.
2. **Localizar fonte de energia** (bateria principal, banco serviço, alternador, gerador, shore-power).
3. **Seguir o circuito** da fonte ao consumidor — proteção (fusível) → comutação → consumidor → retorno (negativo).
4. **Anotar polaridade DC** (+ vermelho, − preto/amarelo).
5. **Identificar pontos de aterramento** (Bonding ≠ PE ≠ Chassi).
6. **Verificar tipo de proteção** (DC vs AC; ANL/MIDI vs MCB).
7. **Conferir cores** com a realidade do barco.

## Falhas comuns

| Falha | Causa | Solução |
|-------|-------|---------|
| Conexão errada DC | Polaridade não documentada | Sempre indicar + e − |
| Disjuntor errado DC vs AC | Símbolo ambíguo | Anotar tipo (DC, AC, ELCI) |
| Bonding vs PE confundidos | Símbolos similares | Legenda explícita |
| Diagrama defasado | Modificações sem update | Atualizar com cada mudança |
| Símbolo legacy não-reconhecido | Diagrama antigo ANSI Y32.2 | Modernizar; legenda completa |

## Boas práticas

- **Padronizar diagrama** (IEC 60617 preferível em projeto novo).
- **Legenda completa** com TODOS os símbolos usados.
- **Convenções de cores** anotadas.
- **Atualizar diagrama** com modificações.
- **Backup digital + papel** a bordo.
- **Versão control** (data + responsável).
- **Treinar tripulação** em interpretação básica.

## Erros comuns

- "Símbolos são óbvios." → Falso. IEC vs ANSI vs NBR diferem em alguns críticos.
- "Cores não importam no diagrama." → Falso. ABYC E-11.4 + ABNT especificam.
- "Diagrama defasado serve mesmo." → Falso. Erros em manutenção / próximo projeto.
- "PE = Bonding = Terra." → Falso. Vide [[Neutro, Negativo, Terra, PE, Bonding e DR — Diferenças Críticas]].

## Glossário

- **IEC 60617:** padrão internacional de símbolos.
- **ANSI/IEEE Std 315:** padrão USA.
- **ABNT NBR 5444:** Brasil predial.
- **ABNT NBR IEC 60617:** Brasil adotando IEC.
- **JIS C 0617:** Japão.
- **DIN EN 60617:** Alemanha.
- **Diagrama unifilar:** representação simplificada (1 linha por circuito).
- **Diagrama multifilar:** todos os condutores explícitos.
- **Esquema elétrico:** diagrama com componentes detalhados.
- **Planta de instalação:** localização física no barco.
- **Legenda:** explicação dos símbolos usados.
- **Convenção de cores:** ABYC E-11.4 / IEC / ABNT.
- **Polaridade DC:** + e − explícitos.
- **Bonding:** ABYC E-11.16.
- **PE (Protective Earth):** AC ground.
- **Earth / Ground:** referência genérica.
- **Chassi (chassis ground):** ponto de massa do equipamento.
- **NA / NF:** Normally Open / Normally Closed.
- **MCB:** Miniature Circuit Breaker.
- **MCCB:** Molded Case Circuit Breaker.
- **RCBO:** Residual Current Breaker with Overcurrent.
- **ELCI:** Equipment Leakage Circuit Interrupter (marine RCD).
- **GFCI:** Ground Fault Circuit Interrupter (USA).
- **DR:** Dispositivo Diferencial Residual (BR).
- **DPS:** Dispositivo de Proteção contra Surto.
- **SSR:** Solid-State Relay.
- **MCB Tipo B/C/D:** classes de disjuntor termomagnético.
- **Vide [[Leitura de Diagramas e Esquemas Elétricos]]** + [[Diagrama Unifilar — Documentação do Sistema Elétrico]].

## Integração com outras notas

- [[Lei de Ohm e Cálculos Básicos]] — fundamentos.
- [[Princípios Náuticos]] — contexto.
- [[Tipos de Embarcação]] — taxonomia.
- [[DC vs AC — Corrente Contínua e Alternada]].
- [[Diagrama Unifilar — Documentação do Sistema Elétrico]].
- [[Leitura de Diagramas e Esquemas Elétricos]].
- [[Projeto Elétrico de Embarcação — Passo a Passo]].
- [[Referência Rápida — Valores de Campo]].
- [[Ferramentas do Eletricista Náutico]].
- [[Cabeamento Náutico]].
- [[Fusíveis DC — Proteção Contra Sobrecorrente]] / [[Disjuntores (DC) e (AC)]].
- [[Bonding — Sistema de Interligação de Massas]] / [[Aterramento]].

## Perguntas que esta nota responde

- Como ler diagrama elétrico náutico?
- Diferença entre símbolo IEC e ANSI?
- Por que o símbolo de bateria tem barras desiguais?
- Símbolo de bonding vs PE vs terra: qual é qual?
- Como representar disjuntor DC vs AC no diagrama?
- Símbolos brasileiros são iguais aos internacionais?
- Onde encontrar tabela de símbolos completa?
- Simbologia para LED diferente de lâmpada incandescente?
- Convenção de cores: ABYC vs IEC vs ABNT?
- Diagrama unifilar vs multifilar: quando usar cada?
