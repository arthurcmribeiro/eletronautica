---
title: "Tipos de Lâmpadas e LEDs Náuticos"
note_type: "comparison"
domain: "55_Iluminacao_e_Sinalizacao"
source_file: "TIPOS DE LÂMPADAS E LEDs NÁUTICOS 33a19734f7fb8172b40ec36bfc926c7e.md"
status: "technical-review-l1"
aliases:
  - "TIPOS DE LÂMPADAS E LEDs NÁUTICOS"
seo_title: "Tipos de Lâmpadas e LEDs Náuticos"
seo_description: "TIPOS DE LAMPADAS E LEDS NAUTICOS — Guia tecnico para escolha de tecnologias de iluminacao em embarcacoes, com foco em aplicacao, IP, CRI, EMC e compatibilidade real."
seo_keywords:
  - "Tipos"
  - "Lâmpadas"
  - "LEDs"
  - "Náuticos"
  - "55 Iluminacao e Sinalizacao"
geo_queries:
  - "O que e Tipos de Lampadas e LEDs Nauticos em instalacoes eletricas nauticas?"
related_notes:
  - "Dimmer — Controle de Intensidade Luminosa"
  - "Farol de Busca"
  - "Fitas Led / Iluminação Led"
  - "Iluminação de Emergência a Bordo"
  - "Luz de Cortesia"
  - "Luz de Âncora"
  - "Luz Subaquática"
  - "Luzes Internas Teto"
---

# Tipos de Lâmpadas e LEDs Náuticos

> [!abstract] Resumo técnico
> TIPOS DE LÂMPADAS E LEDs NÁUTICOS — Guia de referência para escolha de tecnologias de iluminação em embarcações. O critério certo não é só "brilha mais e custa menos", mas adequação à função, ao IP, ao ambiente térmico, ao CRI, à compatibilidade EMC e ao arranjo regulamentar quando aplicável.

## O que é

Esta nota consolida os principais tipos de fontes de luz e luminárias usados a bordo, com foco na decisão técnica: onde cada tecnologia faz sentido, onde não faz, e quais critérios separam um produto aceitável de um improviso caro.

## Tecnologias em uso

### Halógeno

- Ainda aparece em embarcações antigas.
- Tem boa qualidade de luz, mas consumo alto e muito calor.
- É sensível a vibração e menos eficiente que LED.

### Fluorescente de baixa tensão

- Está em declínio.
- Entrega eficiência intermediária, mas depende de eletrônica própria e costuma envelhecer mal em ambiente náutico.

### LED

- Hoje é a tecnologia dominante.
- Pode ser excelente ou péssima, dependendo de driver, óptica, dissipação, EMC e proteção ambiental.
- Não basta ser "LED"; é preciso ser LED adequado à função.

## Critérios de seleção

### Tensão e arquitetura

- Em sistemas DC, soluções de baixa tensão nativas costumam ser preferíveis.
- Em sistemas AC, luminárias AC podem fazer sentido quando integradas à arquitetura existente.
- Evite conversões desnecessárias quando a função pode ser atendida diretamente pela tensão disponível.

### IP

| IP | Uso típico |
| --- | --- |
| IP20 | interior realmente seco |
| IP44 | interior úmido ou banheiro |
| IP65 | áreas protegidas com respingo |
| IP67 | áreas externas e semi-expostas |
| IP68 | aplicações submersas específicas |

### Temperatura de cor

| Faixa | Aplicação prática |
| --- | --- |
| 2700–3000 K | descanso, convívio, camarotes |
| 3500–4000 K | uso geral, galley, circulação |
| 5000 K ou mais | áreas técnicas, quando realmente necessário |

### CRI

- `>= 80` é base aceitável para áreas de convívio.
- `>= 90` melhora a percepção de cor em leitura, galley e ambientes premium.
- valores baixos podem até funcionar, mas pioram conforto e percepção visual.

### EMC

Ruído conduzido ou irradiado por drivers ruins pode afetar:

- VHF
- GPS/chartplotter
- AIS
- receptores de rádio

O sintoma clássico é simples: a iluminação liga e a eletrônica fica pior.

## Onde usar cada tipo

**Luzes de navegação**

- usar conjunto/luminária certificada para a função e para o arranjo regulamentar aplicável

**Luz de âncora**

- luminária adequada ao arranjo de fundeio e à visibilidade exigida

**Iluminação interna**

- LED de baixa tensão ou solução compatível com a arquitetura da embarcação

**Cortesia**

- LED com proteção ambiental adequada e controle coerente de intensidade

**Fitas LED**

- boas para contorno e ambiente, desde que haja cuidado com IP, fixação, dissipação e queda de tensão

**Luz subaquática**

- produto específico de aplicação submersa, nunca adaptação improvisada

## Comparativo direto

| Tecnologia | Eficiência | Calor | Vibração | EMC | Vida útil |
| --- | --- | --- | --- | --- | --- |
| Halógeno | baixa | alta | ruim | boa | baixa |
| Fluorescente | média | média | média | variável | média |
| LED genérico | alta no papel | baixa a média | boa | muito variável | muito variável |
| LED bem especificado | alta | controlada | boa | boa | alta |

## Onde costuma dar problema

| Problema | Causa provável |
| --- | --- |
| vida útil curta | calor, driver ruim, IP inadequado |
| cor inconsistente | compra em lotes diferentes e baixa padronização |
| interferência no rádio | EMC ruim |
| desempenho ruim em ambiente úmido | IP irreal ou aplicação errada |
| falha com dimmer | incompatibilidade elétrica |

## Checklist prático

Antes de especificar uma luminária ou lâmpada:

- confirmar tensão e arquitetura de alimentação
- verificar IP real para o ambiente
- escolher temperatura de cor por função, não por moda
- confirmar CRI compatível com o uso
- verificar compatibilidade com dimmer
- avaliar dissipação térmica
- exigir documentação técnica e EMC críveis
- usar certificação adequada quando a função for regulamentada

## Brasil x referências internacionais

### Leitura equilibrada

No mercado local ainda é comum comprar LED pelo preço unitário. Em base técnica séria, o critério certo é custo total de propriedade: consumo, durabilidade, conforto, manutenção e impacto sobre a eletrônica de bordo.

## Normas e referências aplicáveis

- **COLREGs / USCG / ISO aplicáveis** — para funções regulamentadas como luzes de navegação.
- **IEC 60529** — grau de proteção IP.
- **Normas EMC e documentação do fabricante** — comportamento eletromagnético e elétrico do produto.

## FAQ

**Qualquer LED serve para luz de navegação?**

Não. Para função regulamentada, a luminária precisa ser apropriada e certificada para aquele arranjo.

**Por que LED barato às vezes dá problema no GPS ou VHF?**

Porque o problema não é o LED emissor em si, mas o driver e a eletrônica de alimentação, que podem gerar ruído.

**Vale sempre pagar mais caro?**

Nem sempre. Mas nas funções críticas ou difíceis de manter, economizar demais costuma sair caro.

## Integração com outras notas

- [[Dimmer — Controle de Intensidade Luminosa]]
- [[Farol de Busca]]
- [[Fitas Led / Iluminação Led]]
- [[Iluminação de Emergência a Bordo]]
- [[Luz de Cortesia]]
- [[Luz de Âncora]]
- [[Luz Subaquática]]
- [[Luzes Internas Teto]]

## Perguntas que esta nota responde

- O que é Tipos de Lâmpadas e LEDs Náuticos em instalações elétricas náuticas?
