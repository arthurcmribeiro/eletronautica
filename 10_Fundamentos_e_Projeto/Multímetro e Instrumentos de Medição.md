---
title: "Multímetro e Instrumentos de Medição"
note_type: "technical-note"
domain: "10_Fundamentos_e_Projeto"
source_file: "MULTÍMETRO E INSTRUMENTOS DE MEDIÇÃO 33a19734f7fb811e9400c7b0f34bc486.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "MULTÍMETRO E INSTRUMENTOS DE MEDIÇÃO"
seo_title: "Multímetro e Instrumentos de Medição"
seo_description: "MULTÍMETRO E INSTRUMENTOS DE MEDIÇÃO — O instrumento de medição mais versátil e mais importante do eletricista náutico. Saber usar o multímetro corretamente é a dife."
seo_keywords:
  - "Multímetro"
  - "Instrumentos"
  - "Medição"
  - "10 Fundamentos e Projeto"
geo_queries:
  - "O que é Multímetro e Instrumentos de Medição em instalações elétricas náuticas?"
  - "Quais erros comuns aparecem em Multímetro e Instrumentos de Medição?"
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

# Multímetro e Instrumentos de Medição

> [!abstract] Resumo técnico
> MULTÍMETRO E INSTRUMENTOS DE MEDIÇÃO — O instrumento de medição mais versátil e mais importante do eletricista náutico. Saber usar o multímetro corretamente é a diferença entre diagnóstico preciso e adivinhação cara.

## O que é

O multímetro é um instrumento eletrônico que mede múltiplas grandezas elétricas — tensão (AC e DC), corrente (AC e DC), resistência, continuidade, diodo e, em modelos avançados, capacitância, frequência e temperatura. Em elétrica náutica, é a ferramenta de diagnóstico mais usada em campo.

## Tipos de multímetro

**Multímetro analógico (ponteiro):**

- Leitura por ponteiro em escala impressa
- Útil para visualizar variações (ponteiro se move com a grandeza)
- Menos preciso que digital para leituras pontuais
- Raramente usado profissionalmente hoje

**Multímetro digital (DMM):**

- Leitura numérica no display
- Preciso, fácil de ler
- Padrão atual para qualquer trabalho elétrico profissional

**Multímetro True RMS:**

- Tipo especial de digital que calcula o valor RMS real da forma de onda
- Essencial para medições AC em sistemas com inversores, variadores e distorção harmônica
- Modelos não-True RMS medem corretamente apenas formas de onda próximas da senoidal ideal
- Para trabalho náutico profissional, é a opção mais prudente como padrão de ferramenta

## Categorias de segurança (CAT)

| Categoria | Aplicação | Tensão máxima |
| --- | --- | --- |
| CAT I | Eletrônicos protegidos | 150V |
| CAT II | Tomadas domésticas, equipamentos portáteis | 300V |
| CAT III | Painéis de distribuição, instalações fixas | 600V |
| CAT IV | Entrada de energia, cabos externos | 1000V |

**Para trabalho náutico:**

- Sistema DC (12/24V): CAT II é suficiente
- Sistema AC (shore power, gerador): mínimo CAT III 600V
- Nunca usar multímetro CAT I em circuito AC de 220V — risco de explosão do instrumento em sobretensão

## Funções e como usar cada uma

### Tensão DC (VDC)

```
Configuração: modo DCV, escala acima da tensão esperada (ex: 20V para sistema 12V)
Conexão: preto no negativo (−), vermelho no ponto positivo a medir
Resultado: tensão em relação ao negativo (GND)
Aplicação: verificar carga da bateria, tensão no equipamento, queda de tensão
```

**Leituras de referência para sistema 12V:**

- Só fazem sentido com química conhecida e bateria em repouso
- Em chumbo-ácido, 12,6–12,8V costuma indicar carga elevada; 12,0V já representa bateria bastante descarregada
- Durante carga, tensões na faixa de absorção/float dependem de química, temperatura e configuração do carregador
- Tensão alta isoladamente não basta para diagnosticar falha; é preciso comparar com o setpoint esperado do equipamento

### Tensão AC (VAC)

```
Configuração: modo VAC, escala 200V ou 600V (para 220V)
Conexão: preto em neutro ou terra, vermelho na fase
Resultado: tensão eficaz (RMS)
Aplicação: verificar shore power, saída de gerador/inversor
```

**Leituras normais:**

- 220V ± 10% (198–242V) → OK na marina
- < 190V → subtensão — problema na marina ou no cabo
- 

    > 250V → sobretensão — risco para equipamentos
    > 

### Corrente DC (ADC) — ponteira em série

```
⚠️ ATENÇÃO: modo corrente exige abrir o circuito e inserir o multímetro em SÉRIE
Configuração: modo ADC, selecionar escala adequada (ex: 10A)
Conexão: inserir o multímetro em série no circuito positivo
Fusível de proteção do multímetro: verificar o fusível interno antes
Aplicação: medir correntes pequenas de stand-by, consumo preciso em bancada ou ramos específicos
```

**Corrente de stand-by (consumo em repouso):**

```
Desligar os circuitos conhecidos e garantir que a corrente esperada está dentro da faixa do instrumento
Inserir o multímetro em série apenas em circuitos de baixa corrente ou usar alicate/shunt para o banco principal
Consumo de repouso aceitável depende da embarcação; alarmes, monitores e roteadores podem justificar correntes permanentes
```

### Resistência (Ω)

```
Configuração: modo Ω, circuito completamente desligado e desconectado
Conexão: preto e vermelho nos dois pontos a medir
Resultado: resistência em ohms
Aplicação: testar fusível, continuidade de cabo, resistência de terminal
```

**Leituras de referência:**

- Fusível OK: < 1Ω
- Fusível queimado: OL (overload — circuito aberto)
- Em cabos curtos, a resistência é muito baixa e pode ficar abaixo da confiabilidade prática do multímetro comum
- Para cabos e terminais de potência, o método mais útil em campo costuma ser medir queda de tensão sob carga

### Continuidade (buzzer)

```
Configuração: modo buzzer (ícone de som)
Conexão: igual ao modo Ω
Resultado: bipe sonoro se resistência < 30–50Ω (depende do modelo)
Aplicação: verificar continuidade de cabo, confirmar que fusível está OK, rastrear circuito
Vantagem: não precisa olhar o display — o som indica continuidade
```

### Diodo

```
Configuração: modo diodo
Conexão: vermelho no anodo, preto no catodo
Resultado: queda de tensão do diodo (0,5–0,7V para diodo de silício)
Se OL: diodo invertido (ou aberto)
Se 0V: diodo em curto
Aplicação: verificar diodos de isolamento de bancos, retificadores de alternador
```

## Medição de queda de tensão — técnica prática

**Medir queda de tensão em um cabo sob carga:**

```
1. Equipamento ligado e em operação (carga presente)
2. Preto na extremidade onde o cabo sai da fonte (ex: barramento)
3. Vermelho na outra extremidade (ex: terminal do equipamento)
4. Resultado: tensão entre os dois pontos = queda de tensão no cabo
Aceitável: < 0,36V em sistema 12V (3%)
```

**Medir queda de tensão em um terminal:**

```
Preto em um lado do terminal
Vermelho no outro lado
Com corrente passando
Queda > 0,1V em terminal = mau contato
```

## Erros clássicos com multímetro

**Medir corrente no modo tensão:**

O multímetro em modo tensão tem altíssima impedância interna. Se colocado em série num circuito (como se fosse amperímetro), praticamente nenhuma corrente passa e o circuito fica aberto. Não queima o multímetro, mas não mede nada.

**Medir tensão no modo corrente:**

O multímetro em modo corrente tem baixíssima impedância. Se colocado em paralelo num circuito (como voltímetro), cria um curto-circuito. Queima o fusível interno do multímetro — e pode criar faísca.

**Usar escala abaixo da grandeza esperada:**

Colocar na escala 2V para medir 12V — o display mostra "OL" (overload). Sempre começar pela escala mais alta e ir diminuindo.

**Não verificar se está no modo certo antes de medir:**

Esqueceu no modo Ω e foi medir tensão AC de 220V → fusível interno queima / pode danificar o instrumento.

## Cuidados de uso e manutenção

- Verificar o fusível interno periodicamente (especialmente após medição de corrente em escala errada)
- Armazenar em bolsa com proteção para as pontas
- Não deixar em modo corrente quando não está medindo (risco de curto acidental)
- Verificar a bateria do multímetro — leitura instável pode ser bateria fraca
- Limpar as pontas com pano seco — contaminação por óleo ou sal afeta leituras

## Marcas recomendadas

| Marca/Modelo | Faixa de preço | Nível |
| --- | --- | --- |
| Fluke 107 | R$500–700 | Profissional acessível |
| Fluke 117 | R$1.200–1.500 | Profissional completo |
| UNI-T UT139C | R$150–200 | Bom custo-benefício |
| Brymen BM235 | R$300–400 | Excelente resolução |
| Klein MM600 | R$400–600 | Robusto, popular nos EUA |
| Genérico < R$50 | < R$50 | NÃO USAR |

## Boas práticas profissionais

- Sempre verificar o modo selecionado antes de conectar as pontas
- Começar pela escala mais alta ao medir grandeza desconhecida
- Em sistema AC: usar CAT III mínimo, verificar a categoria do instrumento
- Manter um multímetro de reserva a bordo (o principal pode cair na água)
- Usar ponteiras de qualidade — pontas ruins têm alta resistência de contato

## Como ensinar este tópico

**Sequência recomendada:**

1. Apresentar o instrumento: knobs, displays, terminais (V/Ω, COM, A, 10A)
2. Demonstrar cada modo em circuito real: tensão DC (bateria), tensão AC (tomada), resistência (fusível), continuidade (cabo)
3. Erro clássico ao vivo: colocar no modo corrente e tentar medir tensão — faz o fusível queimar → lição memorável
4. Técnica de queda de tensão: medir antes e depois de um cabo sob carga
5. Corrente parasita: inserir em série, desligar equipamentos um a um
6. Exercício: dado um circuito com problema, usar o multímetro para diagnosticar

**Conceito-chave para fixar:**

"Modo errado + ponta no lugar errado = multímetro morto. Checar sempre: modo e escala antes de conectar."

## FAQ

**Por que meu multímetro mostra leitura instável?**

Bateria fraca (troca a pilha), pontas com mau contato, cabo com resistência variável. Em AC: forma de onda com harmônicas (necessita True RMS).

**Posso medir 48V com multímetro de escala 20V?**

Não — você estará acima da escala selecionada. Selecionar escala acima da tensão esperada (ex: 200V ou 600V).

**Qual a diferença prática de True RMS vs não-True RMS?**

Em circuito próximo da senóide ideal, a diferença pode ser pequena. Em saídas de inversor, cargas não lineares ou sistemas com distorção harmônica, a leitura pode ficar materialmente errada num instrumento não-True RMS. Para diagnóstico confiável de AC a bordo, o True RMS é a referência profissional.

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

- O que é Multímetro e Instrumentos de Medição em instalações elétricas náuticas?
- Quais erros comuns aparecem em Multímetro e Instrumentos de Medição?
