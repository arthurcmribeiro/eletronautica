---
title: "Transformador Entrada"
note_type: "technical-note"
domain: "30_Energia_e_Conversao"
source_file: "TRANSFORMADOR ENTRADA 58419734f7fb83baae88811eb7c459cf.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "TRANSFORMADOR ENTRADA"
seo_title: "Transformador Entrada"
seo_description: "Transformador de entrada adapta tensão de shore power ao padrão interno da embarcação, mas não deve ser confundido automaticamente com transformador de isolamento. O ponto crítico é distinguir adaptação de tensão, frequência, topologia e separação elétrica."
seo_keywords:
  - "Transformador"
  - "Entrada"
  - "30 Energia e Conversao"
geo_queries:
  - "O que é Transformador Entrada em instalações elétricas náuticas?"
  - "Qual é a função de Transformador Entrada na embarcação?"
related_notes:
  - "Alternador (DC)"
  - "Arranque"
  - "CAIS (Pier) (AC)"
  - "Carregador Elétrico para Tender e Jet Ski"
  - "Eólico (DC)"
  - "Gerador (AC)"
  - "Gerador (DC)"
  - "Inversora (DC To AC)"
  - "Isolador Galvânico / Transformador de Isolamento"
  - "Transformador Bivolt"
---

# Transformador Entrada

> [!abstract] Resumo técnico
> Transformador de entrada adapta a tensão do shore power ao padrão elétrico da embarcação, mas não deve ser confundido automaticamente com solução completa de topologia. Em muitos cenários brasileiros o problema não é só `quanto volts entram`, e sim `como eles entram`; nesses casos, a nota complementar correta é [[Transformador Bivolt]].

## O que é

O transformador de entrada (step-up ou step-down) é o equipamento usado para adaptar a tensão disponível no shore power à tensão compatível com o sistema interno da embarcação. Dependendo da topologia, ele pode ser um autotransformador ou um transformador de dois enrolamentos. Essa distinção é essencial para entender o que ele faz e o que ele não faz.

**Quando é necessário:**

- Barco americano com sistema interno 120V/60Hz conectado a marina brasileira de 220V/60Hz → step-down 220→120V
- Barco europeu com sistema 230V/50Hz conectado a marina brasileira de 220V/60Hz → step-down + ajuste de frequência (inversor separado)
- Barco brasileiro 220V conectado a marina americana de 120V → step-up 120→220V
- Barco americano 240V (dois circuitos de 120V) conectado a marina brasileira de 220V monofásico → step-up + adaptação

**Diferença fundamental de nomenclatura:**

- **Transformador de entrada / adaptação:** o foco é compatibilizar níveis de tensão
- **Transformador de isolamento:** o foco é criar separação elétrica entre marina e sistema de bordo, podendo ou não acumular adaptação de tensão

**Expressão de campo no Brasil:**

Em muitas embarcações, o instalador chama qualquer solução de adaptação de "transformador bivolt". Isso é insuficiente. Quando a embarcação migra entre marinas `220 V fase-neutro` e `220 V fase-fase`, a discussão deixa de ser apenas step-up/step-down e passa a envolver também neutralização, PE, DR e sistema derivado. Nesses casos, consultar [[Transformador Bivolt]] é obrigatório.

## Função

| Função | Detalhe |
| --- | --- |
| Adaptar tensão AC | Converte shore power para tensão compatível com o sistema do barco |
| Proteger equipamentos | Equipamentos 120V protegidos de 220V que destruiria imediatamente |
| Permitir navegação internacional | Barco usa shore power em qualquer marina com o transformador adequado |
| Reduzir corrente de linha | Step-up: aumenta tensão, reduz corrente — menor perda no cabo de pier |

## Como aparece na prática

**Muito comum no Brasil:**

- Barcos americanos importados (Searay, Wellcraft, Chaparral) com sistema interno 120V conectados a marinas brasileiras de 220V — exigem step-down
- Transformador portátil (plugado no pedestal, antes do cabo de pier) — solução temporária para visitantes

**Comum em barcos importados:**

- Transformador fixo instalado internamente, entre o inlet de bordo e o painel AC
- Charles Industries, Victron, Mastervolt — modelos para uso marino
- Alguns modelos com taps ajustáveis (110/115/120V entrada; 220/230/240V saída)

**Mais presente em embarcações maiores/premium:**

- Transformador de isolamento com função step-up/down integrada — resolve adaptação de tensão e segurança galvânica em um único componente
- Inversor/carregador de alta potência com entrada universal (80–260V AC) — elimina a necessidade de transformador de entrada em muitos casos

## Fundamentos mínimos

**Relação de transformação:**

A relação de espiras determina a relação de tensão. Um transformador step-down 2:1 converte 220V em 110V. A corrente aumenta na mesma proporção (com perdas mínimas): 10A em 220V → ~20A em 110V. O transformador não cria energia — apenas adapta tensão × corrente.

**Frequência:**

Transformadores de tensão funcionam na frequência do shore power. Um transformador de 60Hz ligado a shore power de 50Hz (marina europeia) pode superaquecer ou operar de forma incorreta. Para adaptação de frequência, o caminho correto é retificação + inversão (inversor).

**Dimensionamento em VA (volt-amperes):**

O transformador deve ser dimensionado para a potência máxima simultânea das cargas que serão alimentadas. Carga de 3.000W → transformador de pelo menos 3.750VA (fator de segurança 1,25). Transformadores marinhos são dimensionados em kVA.

**Fator de potência:**

Cargas resistivas (aquecedor, chuveiro): FP=1 → VA = W.

Cargas indutivas (motor de compressor do AC, carregadores switching): FP 0,7–0,9 → VA > W.

Dimensionar pelo VA, não pelo W declarado nos equipamentos.

## Características

| Parâmetro | Valor típico |
| --- | --- |
| Potência | 1,5kVA a 15kVA |
| Eficiência | 95–98% (perdas no núcleo) |
| Temperatura de operação | -20°C a +55°C |
| Isolação térmica | IP23 a IP44 (uso marino) |
| Peso | 10–60kg (núcleo de ferro — pesados) |
| Frequência | 50Hz ou 60Hz (especificar) |
| Tensões de entrada/saída | Configuráveis com taps (110/120V, 220/230/240V) |

## Configurações comuns

**Step-down 220V → 120V (mais comum para barcos americanos no Brasil):**

- Entrada: shore power brasileiro 220V/60Hz
- Saída: 120V/60Hz para o sistema interno do barco
- Dimensionamento: conforme carga total do barco (geralmente 3–8kVA)

**Step-up 120V → 220V (barcos brasileiros em marinas americanas):**

- Entrada: shore power americano 120V/60Hz
- Saída: 220V/60Hz para o painel AC brasileiro
- Menos comum (poucas embarcações brasileiras navegam nos EUA)

**Transformador com taps ajustáveis:**

- Permite configurar entrada e saída para diferentes padrões de marina
- Ideal para embarcações que navegam internacionalmente
- Charles Industries e Victron oferecem modelos com múltiplos taps

**Autotransformador vs transformador de dois enrolamentos:**

- Autotransformador: bobina única com derivações — mais leve e econômico, sem separação elétrica entre entrada e saída
- Transformador de dois enrolamentos: primário e secundário separados — pode fornecer separação elétrica e, quando projetado para isso, assumir papel de isolamento

## Marcas e referências

- **Charles Industries** — americana, referência em transformadores marinhos, ampla linha de step-up/down e isolamento, encontrada em barcos americanos importados
- **Victron Energy** — transformadores de isolamento com função step-up/down integrada, linha premium
- **Mastervolt** — linha MaraTron, transformadores de alta qualidade para uso marino
- **Hubbell Marine** — transformadores marinhos para embarcações de trabalho e recreio
- **Toroid** — fabricante de transformadores toroidais (menor peso, menor campo magnético), alguns modelos para uso marino
- **Importados genéricos** — disponíveis no Brasil via comércio eletrônico, qualidade variável — verificar classificação IP e especificação de frequência antes de comprar

## Componentes relacionados

- Inlet de bordo (entra antes do transformador)
- Disjuntor de entrada (protege o transformador)
- Medidor de tensão e frequência (verifica o shore power antes de conectar)
- Transformador de isolamento (pode substituir o step-up/down quando integrado)
- Inversor/carregador com entrada universal (alternativa ao transformador em muitos casos)
- Painel AC de distribuição (recebe a saída do transformador)

## Problemas mais frequentes

| Problema | Sintoma | Causa provável |
| --- | --- | --- |
| Transformador superaquece | Carcaça quente, cheiro de queimado | Sobrecarregado além da capacidade nominal |
| Tensão de saída incorreta | Equipamentos funcionam mal ou não ligam | Tap configurado incorretamente, transformador com defeito |
| Ruído (zumbido) excessivo | Zumbido audível constante | Frequência do shore power diferente do projeto, sobrecarga |
| Disjuntor de entrada disparando | Desligamento ao conectar cargas | Transformador sobrecarregado ou curto em carga |
| Transformador muito quente em vazio | Aquece mesmo sem carga | Núcleo dimensionado incorretamente para a frequência |

## Causas raiz

**Superaquecimento por sobrecarga:**

A carga total conectada ultrapassa a capacidade do transformador. Ao ligar o ar-condicionado + carregador + aquecedor simultaneamente, o transformador é forçado além do nominal — aquece, pode queimar.

**Tensão de saída incorreta:**

Tap ajustado para 110V quando o shore power fornece 220V resulta em 220V na saída — dobro do esperado, destrói equipamentos 110V imediatamente. Verificar a configuração do tap antes de conectar qualquer carga.

**Frequência incompatível:**

Transformador de 60Hz operando em marina europeia de 50Hz — o núcleo opera em condição diferente do projeto, aquece mais e pode saturar. A saída pode ter tensão incorreta.

## Diagnóstico prático

**Verificar tensão de saída:**

```
Multímetro → modo VAC
Medir nos terminais de saída do transformador (antes do painel AC)
Resultado esperado: 110–120V (step-down) ou 215–225V (step-up ou sem conversão)
Se fora: verificar tap e tensão de entrada
```

**Verificar temperatura em operação:**

```
Termômetro de contato ou câmera termográfica no corpo do transformador
Após 30 minutos com carga normal
< 60°C: normal
60–80°C: atenção — pode estar próximo da capacidade nominal
> 80°C: sobrecarregado → reduzir carga
```

**Verificar tap configurado:**

```
Com transformador desligado e desenergizado:
Verificar a posição dos taps na borneira de entrada e saída
Confirmar que correspondem ao shore power disponível e ao sistema do barco
Sempre medir a saída após reconfigurar — nunca confiar apenas na posição visual do tap
```

## Boas práticas profissionais

- Dimensionar o transformador para 125% da carga máxima simultânea — nunca no limite
- Instalar disjuntor termomagnético na entrada do transformador, dimensionado para a corrente do primário
- Fixar mecanicamente em base antivibrante — transformadores com núcleo de ferro produzem vibração
- Verificar e anotar a configuração de taps antes de conectar ao shore power
- Medir tensão de saída na primeira conexão em cada nova marina
- Ventilar o compartimento onde o transformador está instalado — gera calor significativo em carga

## Cuidados de instalação

- Instalar em posição protegida de respingos — IP44 mínimo para uso próximo a águas
- Deixar espaço ao redor para ventilação — pelo menos 10cm em todos os lados
- Cabo de saída do transformador deve ser dimensionado para a corrente de saída (maior corrente no step-down)
- Fixar com parafusos — transformadores pesam 10–60kg e podem se soltar com movimento do mar
- Identificar claramente os taps disponíveis e a configuração atual — evita erros futuros

## Cuidados de uso

- Nunca conectar o shore power sem confirmar a tensão do pedestal e a configuração do tap
- Desligar o transformador antes de reconfigurar os taps — nunca manipular taps com o transformador energizado
- Monitorar temperatura durante o primeiro uso com carga completa em nova marina
- Em suspeita de sobrecarga (aquecimento, disjuntor disparando): desligar cargas não essenciais antes de reinvestigar

## Erros comuns

**Conectar sem verificar o tap:**

Tap configurado para 110V de saída, shore power de 220V → saída de 220V → equipamentos 110V destruídos imediatamente. O erro mais caro e o mais evitável.

**Subdimensionar o transformador:**

Comprar "pela potência do ar-condicionado" sem somar carregador, aquecedor e outras cargas simultâneas. O transformador opera saturado — superaquece e tem vida útil muito reduzida.

**Confundir step-down com isolador galvânico:**

"Tenho transformador, estou protegido da corrosão." O step-down sem isolação galvânica não protege contra corrosão — apenas adapta tensão.

**Usar em frequência incorreta:**

Transformador especificado para 60Hz ligado a marina europeia de 50Hz — zumbido excessivo, aquecimento anormal, tensão de saída pode ser incorreta.

## Relação com outros sistemas

- **Shore power:** o transformador fica imediatamente após o inlet — primeiro componente do sistema AC interno
- **Isolador galvânico / Transformador de isolamento:** tratam problemas diferentes da mera adaptação de tensão
- **Painel AC:** recebe a tensão adaptada do transformador
- **Carregador de bateria:** primeiro equipamento beneficiado pela tensão correta
- **Inversor/carregador com entrada universal:** alternativa ao transformador — muitos inversores modernos aceitam 80–265V AC de entrada, eliminando a necessidade do step-up/down

## Brasil x Internacional

| Aspecto | Brasil | Internacional |
| --- | --- | --- |
| Tensão das marinas | 220V/60Hz | 120/240V/60Hz (EUA); 230V/50Hz (Europa) |
| Barcos importados com 120V | Muito comuns | Padrão nos EUA |
| Transformador step-down a bordo | Necessário em muitos barcos americanos importados | Padrão em barcos americanos exportados |
| Transformador com taps ajustáveis | Pouco conhecidos no Brasil | Padrão em embarcações que navegam internacionalmente |

**Realidade brasileira:** A maioria dos importadores de embarcações americanas não instala o transformador step-down adequado. O proprietário conecta o shore power de 220V direto em um barco de 120V — resultado: destruição imediata dos equipamentos. É um dos erros mais caros e mais evitáveis na elétrica náutica.

## Normas aplicáveis

- **ABYC E-11 (2023)** — AC Electrical Systems (dimensionamento, proteção, instalação)
- **NEMA** — padrões americanos de conectores e tensões
- **IEC 60076** — transformadores de potência (referência técnica)
- **ABNT NBR 5410 (2004 + emendas)** e família **ABNT/IEC** aplicável — referência complementar para princípios de baixa tensão, identificação e proteção

## Como ensinar este tópico

**Sequência recomendada:**

1. Mostrar o problema: barco americano 120V + marina brasileira 220V — o que acontece sem o transformador
2. Explicar a relação tensão × corrente no transformador (lei da conservação de potência)
3. Demonstrar como verificar e configurar os taps — prática ao vivo
4. Medir tensão de entrada e saída após configuração — confirmar antes de conectar cargas
5. Diferenciar step-down de isolador galvânico — funções distintas, frequentemente confundidas

**Conceito-chave para fixar:**

"Step-down adapta tensão. Isolador galvânico protege de corrosão. São soluções para problemas diferentes — podem ser necessários os dois simultaneamente."

## Ideias de vídeos

- **"Barco americano no Brasil: como instalar o step-down"** — passo a passo completo
- **"Configurando os taps do transformador: cuidado com esse erro"** — demonstração do risco de tap errado
- **"Step-down vs isolador galvânico: qual a diferença?"** — explicação clara com diagrama
- **"Como dimensionar o transformador para o seu barco"** — cálculo de carga total

## Diagramas sugeridos

- Diagrama de sistema completo: pedestal → inlet → transformador step-down → painel AC
- Esquema de taps: como as diferentes configurações de taps alteram a relação de transformação
- Comparativo: sistema sem transformador (120V no barco, 220V na marina) vs com step-down
- Diagrama de dimensionamento: soma de cargas simultâneas → seleção do kVA mínimo

## FAQ

**Meu inversor aceita 110–220V. Preciso de transformador?**

Depende. Inversores/carregadores com entrada universal (80–265V) já fazem a adaptação internamente — eliminam a necessidade de transformador de entrada para a função de carregamento. Mas outras cargas 110V do barco (tomadas, equipamentos fixos) ainda precisam do step-down para operar corretamente.

**Posso usar um transformador industrial comum no barco?**

Em teoria funciona — mas transformadores industriais não têm proteção IP adequada para ambiente marinho, podem ser muito pesados e não têm as certificações exigidas para embarcações. Para uso permanente, usar transformador especificado para uso marino.

**O transformador de entrada protege meu barco da corrosão galvânica?**

Não. Apenas adapta tensão. Para proteção galvânica, é necessário isolador galvânico (proteção básica) ou transformador de isolamento (proteção completa).

**Posso conectar qualquer carga ao transformador step-down?**

Sim, desde que a carga total não exceda a capacidade nominal e as cargas sejam compatíveis com a tensão de saída. Não conectar cargas 220V na saída 110V do step-down — destruição imediata.

## Integração com outras notas

- [[Alternador (DC)]]
- [[Arranque]]
- [[CAIS (Pier) (AC)]]
- [[Carregador Elétrico para Tender e Jet Ski]]
- [[Eólico (DC)]]
- [[Gerador (AC)]]
- [[Gerador (DC)]]
- [[Inversora (DC To AC)]]
- [[Isolador Galvânico / Transformador de Isolamento]]

## Perguntas que esta nota responde

- O que é Transformador Entrada em instalações elétricas náuticas?
- Qual é a função de Transformador Entrada na embarcação?
