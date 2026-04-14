---
title: "Bomba Ar Condicionado"
note_type: "component"
domain: "70_Hidraulica_Climatizacao_e_Utilidades"
source_file: "BOMBA AR CONDICIONADO 1c019734f7fb832497ea815983a848a7.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
review_level: "engineering-curated"
aliases:
  - "BOMBA AR CONDICIONADO"
  - "Sea water pump"
  - "Raw water pump do ar-condicionado"
seo_title: "Bomba do ar-condicionado marinho: água do mar, vazão, instalação e falhas"
seo_description: "Guia técnico sobre a bomba de água do mar do ar-condicionado marinho: vazão, escorva, strainer, perda de carga, biofouling, proteção elétrica e integração com condensador."
seo_keywords:
  - "bomba ar condicionado marinho"
  - "sea water pump marine ac"
  - "raw water pump condensador barco"
  - "strainer ar-condicionado embarcação"
geo_queries:
  - "Por que o ar-condicionado marinho entra em alta pressão ou para de gelar?"
  - "Como especificar e instalar a bomba de água do mar do ar-condicionado?"
related_notes:
  - "Ar-Condicionado Marine — Sistema Completo"
  - "Blower"
  - "Casa de Máquinas e Paiol"
  - "Bomba de Porão"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Disjuntores (DC) e (AC)"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
---

# Bomba Ar Condicionado

> [!abstract] Resumo técnico
> A bomba do ar-condicionado marinho garante a circulação de água do mar pelo condensador. Sem vazão real, o sistema perde capacidade, entra em proteção e pode sofrer degradação prematura. O problema costuma estar menos na “bomba que queimou” e mais em escorva, strainer, incrustação, perda de carga e comando.

## O que é

Em sistemas marinhos que rejeitam calor para a água do mar, essa bomba alimenta o condensador com fluxo contínuo e suficiente.

Ela é parte da cadeia:

- tomada de mar;
- válvula de fundo;
- `strainer`;
- bomba;
- condensador;
- descarga visível acima da linha d'água, quando aplicável.

## Função real no sistema

Sua função não é apenas “jogar água”.

Ela precisa:

- garantir vazão mínima exigida pelo fabricante;
- vencer a perda de carga do circuito;
- operar de forma confiável em ambiente úmido e sujeito a incrustação;
- acompanhar o regime de operação da climatização.

## Tipos de bomba

Dependendo da arquitetura, podem aparecer:

- bombas centrífugas;
- bombas autoescorvantes;
- arranjos com bomba dedicada para uma unidade;
- arranjos com bomba central para múltiplos evaporadores/condensadores.

Não existe um tipo universalmente superior. O correto depende de geometria, posição da bomba, necessidade de escorva e filosofia do fabricante.

## Critérios de especificação

Os critérios certos são:

- vazão requerida pelo condensador ou conjunto;
- altura manométrica total;
- posição relativa entre bomba e linha d'água;
- tolerância a ar na linha;
- compatibilidade com água salgada;
- duty cycle;
- consumo elétrico e estratégia de proteção;
- facilidade de limpeza do `strainer` e do circuito.

## Strainer e água de mar

O `strainer` é componente crítico do sistema.

Ele protege a bomba e o condensador contra:

- algas;
- areia;
- conchas;
- incrustação solta;
- resíduos aspirados na tomada de mar.

Muita “falha de bomba” é, na prática, restrição hidráulica a montante.

## Escorva, posição e descarga

O projeto deve considerar:

- posição da bomba em relação à linha d'água;
- possibilidade de perda de escorva;
- inclinação e bolsões de ar na tubulação;
- necessidade de vent ou purga;
- visualização da descarga para confirmação operacional.

Em campo, olhar a descarga costuma ser um dos melhores diagnósticos rápidos.

## Biofouling e incrustação

Esse sistema sofre com:

- crescimento biológico;
- cracas e incrustações em tomada, válvula e trocador;
- depósito de resíduos no `strainer`;
- perda progressiva de capacidade térmica.

Em água quente e parada, o fouling se acelera.

## Proteção elétrica e comando

O circuito da bomba deve ser coordenado com a lógica do ar-condicionado.

Pontos importantes:

- proteção compatível com a corrente real;
- cabeamento adequado;
- acionamento sincronizado ao sistema de climatização;
- possibilidade de detectar falta de fluxo ou condição anormal em arranjos mais sofisticados.

Ver também:

- [[Fusíveis DC — Proteção Contra Sobrecorrente]]
- [[Disjuntores (DC) e (AC)]]
- [[Ar-Condicionado Marine — Sistema Completo]]

## Falhas mais comuns

As falhas recorrentes são:

- falta de vazão por `strainer` obstruído;
- bomba operando sem escorva;
- biofouling no circuito;
- perda de desempenho por cabeça manométrica mal avaliada;
- alimentação elétrica insuficiente;
- descarga bloqueada ou mal roteada.

## Diagnóstico profissional

O diagnóstico deve responder:

1. Existe água efetivamente circulando?
2. A vazão é suficiente para o sistema instalado?
3. A bomba está escorvada e dentro da curva adequada?
4. O problema é hidráulico, térmico ou elétrico?

Ensaios úteis:

- confirmar fluxo na descarga;
- inspecionar `strainer` e tomada de mar;
- verificar queda de tensão na bomba em operação;
- medir corrente real;
- revisar estado do condensador e sinais de alta pressão;
- comparar comportamento com uma ou várias unidades ligadas.

## Boas práticas

- instalar `strainer` acessível e realmente inspecionável;
- documentar vazão mínima do sistema;
- prever manutenção periódica da tomada e do trocador;
- evitar trajetos desnecessários e perdas de carga artificiais;
- validar a bomba pelo circuito real, não pelo catálogo isolado.

## Erros comuns

- escolher bomba apenas por vazão livre;
- instalar sem considerar escorva e bolsões de ar;
- ignorar crescimento biológico no circuito;
- diagnosticar tudo como “compressor ruim” quando falta fluxo de água;
- usar materiais inadequados para serviço contínuo com água salgada.

## Integração com outras notas

- [[Ar-Condicionado Marine — Sistema Completo]]
- [[Casa de Máquinas e Paiol]]
- [[Bomba de Porão]]
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]]

## Perguntas que esta nota responde

- Como especificar corretamente a bomba de circulação do ar-condicionado marinho?
- Onde nascem as falhas de vazão e proteção por alta pressão?
- Como diferenciar problema de bomba, de strainer e de trocador térmico?
