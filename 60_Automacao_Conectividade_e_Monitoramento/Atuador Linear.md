---
title: "Atuador Linear"
note_type: "component"
domain: "60_Automacao_Conectividade_e_Monitoramento"
source_file: "ATUADOR LINEAR 5a319734f7fb8392ad8b81db5fd17f98.md"
status: "technical-review-l1"
aliases:
  - "ATUADOR LINEAR"
seo_title: "Atuador Linear"
seo_description: "ATUADOR LINEAR — Componente eletromecanico que converte energia eletrica em movimento linear e exige dimensionamento serio de forca, curso, duty cycle, corrente de bloqueio, comando e protecao."
seo_keywords:
  - "Atuador linear"
  - "Automacao de bordo"
  - "Comando eletromecanico"
  - "60 Automacao Conectividade e Monitoramento"
geo_queries:
  - "O que e atuador linear em instalacoes eletricas nauticas?"
  - "Como dimensionar e diagnosticar atuador linear de bordo?"
related_notes:
  - "Automação de Bordo — Sistemas Domoticos"
  - "Sistema de Alarme Geral / Painel de Alarmes"
  - "Relés e Relés de Estado Sólido"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Disjuntores (DC) e (AC)"
  - "Plataforma de Popa Elétrica - Hidráulica"
  - "Flap"
  - "Motor de Trim - Tilt"
---

# Atuador Linear

> [!abstract] Resumo técnico
> Atuador linear é um conjunto eletromecânico que transforma energia elétrica em deslocamento linear. Em embarcações, ele só é confiável quando o projeto considera força real da carga, geometria de montagem, curso útil, duty cycle, corrente de bloqueio, fim de curso, proteção do circuito e estratégia de comando.

## O que é

Atuador linear é, em geral, um motor DC acoplado a redutor e a um mecanismo de conversão rotativo-linear, normalmente por fuso. O conjunto desloca uma haste ou corpo móvel para empurrar, puxar, abrir, fechar, elevar ou posicionar um elemento mecânico.

Em aplicações navais, o atuador raramente falha por "problema elétrico puro". O mais comum é a soma de:

- especificação de força inadequada;
- instalação com desalinhamento;
- limite mecânico mal definido;
- ciclo de trabalho acima do admissível;
- proteção elétrica ruim;
- ambiente agressivo para vedações, conectores e cabo móvel.

## Função na embarcação

- acionar flaps e superfícies auxiliares;
- abrir escotilhas, paióis e compartimentos;
- movimentar plataformas, mesas, assentos e tampas;
- posicionar suportes, antenas e alguns acessórios;
- executar movimentos comandados por botoeira, relé, controlador ou automação.

## Fundamentos mínimos

### Força nominal não é força disponível em qualquer geometria

A força informada pelo fabricante depende da geometria real do sistema. Mudança de ângulo, braço de alavanca e ponto de fixação altera drasticamente o esforço exigido do atuador.

### Curso total não é o mesmo que curso útil

Parte do curso pode ser perdida por batentes, articulações, ângulos de montagem ou zonas proibidas do mecanismo. O que importa no projeto é o curso útil sob carga.

### Duty cycle é limitante térmico real

Muitos atuadores são feitos para operação intermitente. Quando o sistema exige repetição frequente ou manutenção prolongada em carga, o aquecimento do motor e do redutor vira fator crítico.

### Corrente de bloqueio precisa entrar no projeto

Quando o atuador chega ao fim do curso, encontra obstáculo ou trabalha travado, a corrente pode subir várias vezes acima da corrente em regime. A proteção deve ser coordenada com o cabo e com o perfil real de partida e bloqueio.

### Fim de curso não substitui projeto mecânico

Fim de curso interno é proteção complementar. O sistema mecânico ainda precisa respeitar alinhamento, batentes coerentes e zona segura de movimento.

## Tipos e variantes comuns

### Atuador com fim de curso interno

- solução mais comum;
- simplifica comando de abrir/fechar;
- não dispensa controle de reversão e proteção do circuito.

### Atuador com realimentação de posição

- pode usar potenciômetro, hall ou encoder;
- indicado quando é preciso saber posição, sincronizar movimentos ou integrar com controle.

### Atuadores em par

- comuns em plataformas e tampas grandes;
- exigem atenção a sincronismo, distribuição de carga e torção estrutural;
- dois atuadores em paralelo sem controle adequado podem "brigar" entre si.

### Atuadores industriais adaptados

- podem funcionar em áreas protegidas;
- só fazem sentido quando vedação, conectores, materiais e duty cycle forem compatíveis com ambiente marítimo.

## Projeto e instalação

### O que deve ser definido antes da compra

1. carga real e pior caso de esforço;
2. curso útil exigido;
3. velocidade aceitável;
4. tensão do sistema;
5. duty cycle necessário;
6. estratégia de comando e reversão;
7. nível de vedação e resistência à corrosão.

### Comando elétrico

Os arranjos mais comuns são:

- botoeira reversora;
- par de relés/contatores de reversão;
- ponte H eletrônica;
- controlador dedicado com leitura de posição.

Em qualquer caso, é preciso prever:

- reversão segura de polaridade;
- intertravamento para evitar comandos opostos simultâneos;
- proteção contra curto e sobrecorrente;
- parada em condição anormal.

### Instalação mecânica

- evitar esforço lateral sobre a haste;
- usar pontos de articulação compatíveis com o curso angular do mecanismo;
- confirmar que nada entra em travamento antes do fim de curso elétrico;
- proteger o chicote em zonas móveis e pontos de esmagamento;
- garantir drenagem e vedação coerentes com o ambiente.

## Onde costuma dar problema

| Problema | Causa provável |
| --- | --- |
| atuador não se move | ausência de alimentação, comando defeituoso, proteção aberta ou motor queimado |
| atua com pouca força | queda de tensão, carga acima do projeto ou atrito mecânico excessivo |
| para antes do esperado | fim de curso antecipado, geometria errada ou bloqueio mecânico |
| aquece em excesso | duty cycle excedido ou corrente elevada por esforço anormal |
| movimenta um lado e torce o conjunto | sincronismo ruim entre atuadores ou estrutura deformando |
| falha recorrente em ambiente salino | vedação, conectores ou chicote incompatíveis |

## Diagnóstico prático

1. Confirmar tensão nos terminais durante o acionamento.
2. Medir queda de tensão no positivo e no retorno sob carga.
3. Comparar corrente em operação com a condição mecânica observada.
4. Isolar se a falha está no comando, no chicote ou no atuador.
5. Verificar alinhamento, batentes e liberdade de movimento com o sistema desenergizado.
6. Testar fim de curso e reversão sem insistir em condição de bloqueio.

### Leituras úteis

- tensão chegando ao atuador durante a carga;
- corrente de partida e de regime;
- temperatura percebida após ciclos repetidos;
- simetria de curso e esforço em atuadores duplos.

## Boas práticas profissionais

- dimensionar a proteção pelo cabo e pelo perfil de corrente do circuito, não por "achismo";
- prever margem mecânica e elétrica, sem usar o atuador no limite contínuo;
- documentar curso, polaridade, lógica de comando e posição de repouso;
- usar conectores e selagem compatíveis com névoa salina e vibração;
- inspecionar articulações, pinos, buchas e chicote como parte da manutenção;
- em aplicações críticas, preferir realimentação de posição ou confirmação de estado.

## Erros comuns

- comprar por força nominal sem analisar geometria;
- confiar apenas no fim de curso interno para segurar o sistema;
- instalar atuador rígido em mecanismo que pede articulação adequada;
- ignorar corrente de bloqueio no dimensionamento de cabo e proteção;
- usar par de atuadores sem estratégia de sincronismo;
- tratar falha mecânica como se fosse apenas falha elétrica.

## Relação com outros sistemas

- **[[Automação de Bordo — Sistemas Domoticos]]** — lógica de comando, integração e supervisão.
- **[[Sistema de Alarme Geral / Painel de Alarmes]]** — indicação de falha, posição ou condição anormal.
- **[[Relés e Relés de Estado Sólido]]** — reversão e acionamento de carga.
- **[[Fusíveis DC — Proteção Contra Sobrecorrente]]** e **[[Disjuntores (DC) e (AC)]]** — proteção do circuito.
- **[[Plataforma de Popa Elétrica - Hidráulica]]** e **[[Flap]]** — aplicações práticas do princípio.

## Normas e referências

- documentação elétrica e mecânica do fabricante do atuador;
- especificações de duty cycle, IP, corrente de bloqueio e carga admissível;
- boas práticas de cabeamento, proteção de circuitos e comando DC da embarcação.

## FAQ

**Todo atuador linear é autotravante?**

Não. Muitos apresentam efeito de autotravamento pelo conjunto fuso/redutor, mas isso depende da construção e não deve ser presumido sem documentação do fabricante.

**Posso usar o fim de curso interno como único limitador do sistema?**

Não é a abordagem mais segura. O projeto mecânico deve evitar esforço destrutivo mesmo se houver falha de ajuste, desalinhamento ou desgaste.

**Se o atuador está lento, o problema é sempre elétrico?**

Não. Desalinhamento, corrosão, articulação travada, sobrecarga e duty cycle excedido são causas frequentes.

## Integração com outras notas

- [[Automação de Bordo — Sistemas Domoticos]]
- [[Sistema de Alarme Geral / Painel de Alarmes]]
- [[Relés e Relés de Estado Sólido]]
- [[Fusíveis DC — Proteção Contra Sobrecorrente]]
- [[Disjuntores (DC) e (AC)]]
- [[Plataforma de Popa Elétrica - Hidráulica]]
- [[Flap]]
- [[Motor de Trim - Tilt]]

## Perguntas que esta nota responde

- O que é atuador linear em instalações elétricas náuticas?
- Como dimensionar corretamente um atuador linear de bordo?
- Quais são as falhas mais comuns de atuadores lineares em embarcações?
