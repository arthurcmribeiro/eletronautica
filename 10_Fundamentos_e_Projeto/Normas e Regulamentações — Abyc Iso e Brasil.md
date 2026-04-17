---
title: "Normas e Regulamentações — Abyc Iso e Brasil"
note_type: "reference"
domain: "10_Fundamentos_e_Projeto"
source_file: "NORMAS E REGULAMENTAÇÕES — ABYC, ISO E BRASIL 33a19734f7fb81cb8e17dd284ca1cc01.md"
status: "technical-review-l1"
reviewed_on: "2026-04-16"
review_jurisdiction:
  - "Brasil"
  - "internacional"
normas_citadas:
  - "ABYC E-11 (2023)"
  - "ABYC E-2 (2020)"
  - "ABYC E-10 (2023)"
  - "ABYC E-13 (2022)"
  - "ABYC A-28 (edição a verificar)"
  - "ABYC A-31 (edição a verificar)"
  - "ISO 13297:2020"
  - "ISO 10133 (retirada, histórico)"
  - "ABNT NBR 5410 (2004 + emendas)"
  - "NORMAM-211 (2022 rev. aplicável via DPC)"
  - "NORMAM-02 (substituída, histórico)"
  - "IEC 61008"
  - "IEC 61009"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://www.iso.org/standard/45867.html"
  - "https://www.iso.org/standard/83643.html"
  - "https://abycinc.org/standards/"
aliases:
  - "NORMAS E REGULAMENTAÇÕES — ABYC, ISO E BRASIL"
  - "Vademecum normativo da elétrica náutica"
seo_title: "Normas da elétrica náutica no Brasil: ABYC, ISO, NORMAM, NBR e comparação prática"
seo_description: "Vademecum técnico de normas para elétrica náutica: o que é regulatório no Brasil, o que é referência de engenharia em ABYC e ISO, onde as filosofias divergem e por que o caso brasileiro exige cuidado especial com shore power, tensões, neutro e aterramento."
seo_keywords:
  - "ABYC E-11 (2023) Brasil"
  - "ISO 13297:2020"
  - "NORMAM-211 (2022 rev. aplicável via DPC)"
  - "NBR 5410 embarcação"
  - "normas elétrica náutica"
  - "10 Fundamentos e Projeto"
geo_queries:
  - "Quais normas realmente valem para elétrica náutica no Brasil?"
  - "ABYC serve para barco no Brasil?"
  - "Qual a diferença entre ABYC, ISO e NORMAM?"
related_notes:
  - "Aterramento"
  - "CAIS (Pier) (AC)"
  - "Fase e Neutro"
  - "Isolador Galvânico / Transformador de Isolamento"
  - "Projeto Elétrico de Embarcação — Passo a Passo"
  - "Proteção Dr"
  - "Transformador Bivolt"
---

# Normas e Regulamentações — Abyc Iso e Brasil

> [!abstract] Resumo técnico
> A base normativa da elétrica náutica não cabe em uma única sigla. No Brasil, a **NORMAM** define o eixo regulatório para embarcações de esporte e recreio; **ABNT/NBR** e família **IEC** oferecem referências complementares de baixa tensão e identificação; **ABYC** e **ISO** são os corpos de engenharia mais úteis para projeto, instalação e diagnóstico. O erro clássico é tratar uma dessas camadas como suficiente, ou transplantar uma filosofia estrangeira sem revalidar a topologia real das marinas brasileiras.

## Como esta nota deve ser usada

Use esta página como **nota-mestre normativa** para responder quatro perguntas:

1. qual documento tem força regulatória;
2. qual documento ajuda a projetar melhor;
3. qual filosofia elétrica está por trás de cada referencial;
4. onde a realidade brasileira obriga adaptação.

## Primeiro princípio: norma regulatória não é a mesma coisa que norma de engenharia

Há pelo menos quatro camadas diferentes em jogo:

| Camada | Exemplos | Para que serve |
| --- | --- | --- |
| Regulatória brasileira | NORMAM da Autoridade Marítima | inscrição, operação, requisitos administrativos e de segurança sob a ótica regulatória |
| Projeto/instalação náutica | ABYC, ISO small craft | arquitetura elétrica de bordo, instalação, proteção, inspeção |
| Instalação elétrica geral de baixa tensão | ABNT/NBR e IEC | princípios complementares de proteção, identificação, coordenação e segurança |
| Norma de produto | IEC 61008, IEC 61009, catálogos de fabricante | requisitos do próprio equipamento, como DR, RCBO, transformador, isolador |

Se o profissional mistura essas camadas, a conclusão costuma ficar juridicamente fraca e tecnicamente pior ainda.

## Ecossistema brasileiro: o que é obrigatório e o que é complementar

### NORMAM

A Marinha do Brasil, por meio da Diretoria de Portos e Costas, passou a referenciar **NORMAM-211 (2022 rev. aplicável via DPC)** para amadores, embarcações de esporte e/ou recreio e para cadastramento/funcionamento de marinas, clubes e entidades náuticas.

O que isso significa na prática:

- a referência anterior centrada em `NORMAM-02` não deve mais ser tratada como base vigente para esse universo;
- a NORMAM é indispensável para enquadramento regulatório brasileiro;
- a NORMAM **não é** um manual completo de arquitetura elétrica de embarcação.

### ABNT / NBR / IEC adotadas no Brasil

No lado brasileiro de engenharia elétrica, a referência mais sólida e estável continua sendo:

- **ABNT NBR 5410 (2004 + emendas)** para princípios de baixa tensão;
- família **IEC / ABNT NBR IEC** para identificação de condutores, dispositivos e conjuntos;
- adoções brasileiras de normas ISO/IEC específicas, quando aplicáveis ao assunto e disponíveis no catálogo vigente.

Ponto crítico: **ABNT/NBR predial ou industrial não substitui uma norma náutica de bordo**. Ela ajuda a resolver princípios, não o ambiente marinho por completo.

## Ecossistema internacional: onde entram ABYC e ISO

### ABYC

ABYC é o corpo técnico mais útil quando o assunto é instalação real, manutenção, inspeção e diagnóstico em embarcação de recreio. Para elétrica, os documentos centrais são:

| Documento | Tema |
| --- | --- |
| ABYC E-11 (2023) | sistemas AC e DC em embarcações |
| ABYC E-2 (2020) | prevenção de corrosão galvânica |
| ABYC E-13 (2022) | baterias de íons de lítio |
| ABYC A-28 (edição a verificar) | galvanic isolators (verificar edição vigente) <!-- TODO-CITAÇÃO --> |
| ABYC A-31 (edição a verificar) | lightning protection |
| ABYC A-20 / A-25 | battery chargers e inverter/chargers (verificar cláusula vigente) <!-- TODO-CITAÇÃO --> |

ABYC é uma referência de engenharia. Não é lei brasileira. Ainda assim, ela costuma ser mais útil que a regulação local quando a pergunta é "como projetar e instalar sem improviso".

### ISO / IEC small craft

No universo europeu e internacional, a família ISO small craft continua central. Dois pontos importantes:

- **ISO 13297:2020** é hoje a referência internacional principal para sistemas elétricos em pequenas embarcações;
- **ISO 10133** foi retirada, e a própria ISO informa que a edição mais nova disponível migra a lógica para **ISO 13297:2020**.

Isso corrige um problema comum de material antigo: citar ISO 10133 como se ainda fosse a referência viva e isolada para DC de pequenas embarcações.

## Comparação prática: ABYC, modelo europeu/ISO e Brasil real

### Visão estratégica

| Aspecto | ABYC / América do Norte | ISO / IEC / Europa | Brasil regulatório e de campo |
| --- | --- | --- | --- |
| Natureza | engenharia voluntária altamente detalhada | engenharia internacional harmonizada | mistura de regulação marítima, NBR e prática heterogênea de concessionárias/marinas |
| Ambiente de origem | marinas e embarcações com ecossistema norte-americano | small craft europeias e CE | realidade elétrica regionalmente desigual |
| Uso ideal | projeto, instalação, inspeção e retrofit | projeto de pequenas embarcações e conformidade internacional | enquadramento legal e adaptação ao fornecimento local |
| Risco de uso cego | importar solução sem adaptar topologia | assumir que o ambiente de marina local corresponde ao europeu | achar que só a NORMAM basta para engenharia de bordo |

### Tabela comparativa de itens que afetam a vida prática

| Item | ABYC / prática norte-americana | ISO / prática europeia | Brasil de campo |
| --- | --- | --- | --- |
| Frequência dominante | 60 Hz | 50 Hz em grande parte da Europa | 60 Hz |
| Monofásico mais típico | 120 V ou 120/240 V split-phase | 230 V monofásico | 127/220 V, 220/380 V, 120/240 V em importados e derivações locais |
| Significado prático de `220/230 V` | pode significar 240 V entre L1 e L2 com neutro central | geralmente 230 V monofásico com neutro definido pela fonte | pode ser `fase-neutro` ou `fase-fase`; o valor sozinho não resolve |
| Split-phase | muito presente | menos central | aparece em embarcações importadas, não como padrão nacional de marina |
| Trifásico | existe em marinas maiores e iates maiores, muitas vezes em ecossistema mais padronizado | existe em infraestrutura maior, normalmente organizado em torno de 400/230 V | distribuição de concessionária frequentemente é `220/380` ou `127/220` em estrela com neutro; a embarcação muitas vezes recebe apenas um subconjunto dessa rede |
| Neutro entregue ao barco | comum no modelo esperado pela instalação | comum no modelo monofásico europeu | nem sempre; em muitos pontos o barco recebe dois ativos e PE |
| Filosofia de neutro/terra | bond neutro-PE tratado na origem ou em sistema derivado conforme arquitetura | idem, com lógica própria do sistema e forte disciplina de instalação | frequentemente mal interpretado, sobretudo quando se assume neutro inexistente ou se tenta criá-lo dentro do barco |
| Identificação de condutores | hot preto/vermelho, neutral branco, grounding verde/verde-amarelo em convenções usuais | PE verde-amarelo, neutro azul claro quando presente, fases em cores não reservadas | em linha com IEC/ABNT para identificação, mas a realidade de campo pode estar longe do ideal |
| Proteção diferencial | GFCI/ELCI/RCD conforme arranjo | RCD/RCBO fortemente presentes | presença muito irregular; marinas e barcos mais antigos frequentemente deficientes |
| Filosofia de shore power | ecossistema relativamente coerente dentro do padrão local | ecossistema mais previsível em 230 V / 50 Hz | altíssima variabilidade de pedestal, tensão, topologia e qualidade de PE |
| Papel do transformador de isolamento | solução premium e consolidada | muito usado em embarcações de maior robustez | passa de opcional de luxo para solução estratégica em muitas marinas |
| Regulador/fiscalizador | não é papel da ABYC | depende da certificação e do país | Marinha regula o universo marítimo; concessionária define parte da realidade da alimentação terrestre |

Manuais técnicos de concessionárias brasileiras deixam claro que o país convive com secundários `127/220`, `220/380` e variações de fornecimento de baixa tensão. Para o eletricista náutico, isso reforça uma regra simples: **o pedestal da marina não pode ser presumido pela memória do último barco**.

### Identificação de condutores: o que é útil guardar

| Função | Convenção ABYC/Norte-Americana | Convenção IEC/ABNT/Brasil |
| --- | --- | --- |
| Condutor ativo | preto, vermelho e outras cores de fase conforme arquitetura | fases em cores não reservadas |
| Neutro | branco | azul claro quando houver neutro |
| PE / proteção | verde ou verde-amarelo | verde ou verde-amarelo |

O importante aqui não é decorar cor. O importante é entender que **a função elétrica vem antes da cor**.

## O caso brasileiro em que ABYC é mal utilizada

O problema não é adotar ABYC como referência técnica. O problema é fazer isso da forma preguiçosa:

- estaleiro ou instalador assume um mundo `L + N + PE`;
- cria barramento de neutro;
- liga esse barramento ao universo `PE/negativo DC/bonding`;
- o barco vai para uma marina com `220 V entre dois ativos`;
- um dos ativos passa a atuar como neutro falso.

Essa transposição mal feita pode causar:

- circulação de corrente por condutores de proteção;
- interpretação errada de DR/ELCI;
- tensões de toque anormais;
- dano a módulos eletrônicos e sistemas sensíveis;
- arco, aquecimento e incêndio.

Conclusão técnica: **ABYC serve, desde que a alimentação brasileira seja reinterpretada e o projeto seja tropicalizado.**

### Caso específico: `220 V fase-fase sem neutro` em marina brasileira

Esse é o cenário mais perigoso da transposição mal feita de ABYC/ISO (pensados para neutro definido) para a realidade elétrica brasileira. Exemplo comum:

- O barco foi projetado para `L + N + PE` (uma fase viva, um neutro aterrado na origem, um PE).
- A marina entrega `220 V fase-fase` entre dois ativos (`L1` e `L2`), sem neutro, com PE separado — configuração típica de secundário `220/380` ou `127/220` quando o pedestal expõe só dois ativos.
- O instalador amarra um dos ativos ao barramento "neutro" do barco, que está interligado ao PE/negativo DC/bonding.
- Resultado: um dos condutores ativos passa a circular corrente pelo sistema de proteção, elevando o potencial das massas do casco em relação ao meio aquático.

Consequências práticas: tensões de toque anormais em corrimões e costados; risco elevado de eletrocussão de banhistas próximos; corrosão galvânica acelerada; leituras erráticas de DR/ELCI; dano silencioso em eletrônica sensível. A solução certa é **transformador de isolamento** ou **isolador galvânico** correto para o cenário — ver [[Isolador Galvânico / Transformador de Isolamento]] e [[CAIS (Pier) (AC)]].

## Vademecum por assunto

| Assunto | Referência de engenharia mais útil | Observação prática |
| --- | --- | --- |
| Arquitetura AC/DC geral | ABYC E-11 (2023) | continua sendo a referência mais acionável de campo |
| Shore power e interface com marina | ABYC E-11 (2023) + ISO 13297:2020 + documentação do equipamento | no Brasil, validar também a topologia real da concessionária/marina |
| Baterias convencionais | ABYC E-10 (2023) / E-11 | cruzar com fabricante e requisitos do equipamento |
| Lítio | ABYC E-13 (2022) + fabricante | sem documentação do sistema, a norma não salva o projeto |
| Carregadores e inverter/chargers | ABYC A-31 (edição a verificar) | indispensável cruzar com o manual da plataforma instalada |
| Corrosão galvânica e bonding | ABYC E-2 (2020) + arquitetura do casco | não tratar bonding como extensão casual do terra AC |
| Galvanic isolators | ABYC A-28 (edição a verificar) | importante em barcos com shore power sem transformador de isolamento |
| DR / RCD / RCBO | IEC 61008 / 61009 + arquitetura do sistema | o dispositivo certo depende da topologia e das eletrônicas embarcadas |
| Identificação de condutores e proteção BT | ABNT NBR 5410 (2004 + emendas) e família IEC/ABNT aplicável | complementar, nunca substitutiva da norma náutica |
| Regulação de esporte e recreio no Brasil | NORMAM-211 (2022 rev. aplicável via DPC) | regula o ambiente marítimo, não substitui o detalhamento de instalação |

## O que a NORMAM faz e o que ela não faz

### O que ela faz

- enquadra o universo de amadores e embarcações de esporte/recreio;
- orienta procedimentos administrativos, operacionais e requisitos regulatórios;
- alcança também marinas, clubes e entidades náuticas em seu escopo específico.

### O que ela não faz sozinha

- não substitui uma filosofia completa de cabeamento e proteção comparável a ABYC E-11 (2023);
- não resolve, por si, a topologia do shore power recebido pelo barco;
- não elimina a necessidade de diagrama, cálculo, coordenação de proteção e validação de fabricante.

## Como citar normas sem se comprometer tecnicamente

Sempre que possível, cite assim:

- documento;
- edição/ano;
- tópico ou cláusula;
- contexto de aplicação;
- limitação assumida.

Exemplo de postura correta:

> "Projeto de entrada AC analisado à luz da filosofia de proteção da ABYC E-11 (2023), complementado por ABNT NBR 5410 (2004 + emendas) para princípios de BT e verificação do enquadramento regulatório brasileiro segundo a NORMAM-211 (2022 rev. aplicável via DPC) vigente."

Exemplo de postura errada:

> "Sistema conforme ABYC" sem dizer edição, sem dizer escopo e sem descrever a topologia real do barco.

## Regras práticas para a sua base técnica

- nunca citar `NORMAM-02` como base vigente para esporte/recreio sem checar o enquadramento atual;
- nunca citar `ISO 10133` como referência viva sem dizer que foi retirada/substituída;
- nunca dizer "segue ABYC" sem explicar se o barco foi projetado para `L + N + PE`, `L1 + L2 + PE`, `split-phase` ou sistema derivado;
- sempre separar **regulação**, **engenharia** e **manual de fabricante**;
- em nota de Obsidian, deixar claro quando a informação depende da edição vigente ou de norma paga.

## Fontes institucionais e catálogos oficiais

- [Portal de normas da DPC / Marinha do Brasil](https://www.marinha.mil.br/dpc/normas)
- [Serviço GOV.BR que já referencia a NORMAM-211 (2022 rev. aplicável via DPC) para embarcações de esporte e recreio](https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes)
- [ABYC Standards](https://abycinc.org/standards/)
- [ISO 13297:2020](https://www.iso.org/standard/69551.html)
- [ISO 10133:2012, retirada, com indicação de migração para ISO 13297:2020](https://www.iso.org/standard/45867.html)

## FAQ

**ABYC é obrigatória no Brasil?**

Não. Ela é referência de engenharia, não obrigação legal brasileira.

**A NORMAM basta para projetar uma instalação elétrica de bordo robusta?**

Não. Ela é necessária para enquadramento regulatório, mas não substitui um referencial técnico profundo de projeto e instalação.

**ISO 10133 ainda deve ser usada?**

Somente com contexto histórico ou documental. A própria ISO informa que a edição retirada foi sucedida pela ISO 13297:2020.

**A norma brasileira predial resolve a embarcação?**

Não. Ela ajuda em princípios de BT, identificação, proteção e linguagem técnica, mas não descreve integralmente o ambiente náutico de bordo.

**Qual é a maior diferença prática entre o modelo americano e o brasileiro?**

Na prática de campo, o maior risco está na topologia da alimentação e no tratamento de neutro, PE e fontes derivadas. O Brasil convive com uma realidade muito mais heterogênea de pedestal e concessionária.

## Integração com outras notas

- [[Aterramento]]
- [[CAIS (Pier) (AC)]]
- [[Fase e Neutro]]
- [[Isolador Galvânico / Transformador de Isolamento]]
- [[Projeto Elétrico de Embarcação — Passo a Passo]]
- [[Proteção Dr]]
- [[Transformador Bivolt]]

## Perguntas que esta nota responde

- O que é regulatório no Brasil e o que é referência de engenharia?
- NORMAM-211 (2022 rev. aplicável via DPC) substitui NORMAM-02 para esporte e recreio?
- ABYC serve para o Brasil?
- Onde ABYC costuma ser mal aplicada no Brasil?
- ISO 10133 ainda está vigente?
- Qual a diferença entre ABYC, ISO e NBR?
- O que muda em tensões, fases, neutro e PE na prática?
- Como citar norma sem se comprometer tecnicamente?
- Qual documento usar para shore power, DR, bonding, baterias e lítio?
- Como montar uma base normativa séria no Obsidian?
