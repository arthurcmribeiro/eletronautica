---
title: "BMS — Battery Management System"
note_type: "technical-note"
domain: "20_Baterias_e_Armazenamento"
source_file: "BMS — BATTERY MANAGEMENT SYSTEM 33a19734f7fb81519181fa235e718c78.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://abycinc.org/news/standardsupdatewebinar/"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "BMS — BATTERY MANAGEMENT SYSTEM"
seo_title: "BMS — Battery Management System"
seo_description: "BMS é o sistema de supervisão, proteção e coordenação de um banco de baterias de lítio. Sua função não é apenas cortar em falha, mas monitorar células, temperatura, corrente e integração com as fontes e cargas do sistema."
seo_keywords:
  - "BMS"
  - "Battery"
  - "Management"
  - "System"
  - "20 Baterias e Armazenamento"
geo_queries:
  - "O que é BMS — Battery Management System em instalações elétricas náuticas?"
  - "Qual é a função de BMS — Battery Management System na embarcação?"
related_notes:
  - "Alternador (DC)"
  - "Bancos de Bateria"
  - "Carregador de Bateria (AC To DC)"
  - "Inversora (DC To AC)"
  - "Lítio LiFePO4 — Instalação e Cuidados Específicos"
  - "Monitor de Bateria / BMV / Shunt"
  - "Tipos de Bateria"
---

# BMS — Battery Management System

> [!abstract] Resumo técnico
> BMS é o sistema de supervisão e proteção do banco de lítio. Ele monitora células, corrente, temperatura e permissões de carga/descarga, e precisa ser coordenado com carregadores, alternadores, inversores e estratégias de desligamento do sistema.

## O que é

O BMS (Battery Management System) é o circuito eletrônico inteligente integrado a bancos de baterias de lítio (LiFePO4, NMC, LTO) que monitora continuamente o estado de cada célula individual e protege o banco contra condições que causariam dano irreversível ou risco de segurança: sobretensão, subtensão, sobrecorrente, temperatura excessiva e desbalanceamento de células.

Em sistemas de chumbo-ácido não se usa BMS no sentido aplicado ao lítio, porque a gestão da química e a proteção são tratadas de outra forma. Em bancos LiFePO4 de uso náutico, a supervisão por BMS é parte do sistema, não acessório opcional.

## Função

| Proteção | Condição | Ação |
| --- | --- | --- |
| Sobretensão de célula | Acima do limite definido para a célula e o fabricante | Reduz ou interrompe carregamento |
| Subtensão de célula | Abaixo do limite definido para a célula e o fabricante | Reduz ou interrompe descarga |
| Sobrecorrente de carga | Corrente > limite configurado | Desconecta carga ou carregamento |
| Sobrecorrente de partida | Pico de corrente > limite de curto | Desconecta (proteção de curto) |
| Temperatura alta | Acima da faixa segura definida pelo fabricante | Limita ou interrompe operação |
| Temperatura baixa | Abaixo da faixa segura de carga | Bloqueia ou limita carregamento |
| Balanceamento | Diferença entre células > threshold | Balancea passivo ou ativo |

## Como aparece na prática

- Módulo eletrônico integrado dentro do case da bateria (baterias prontas como Battle Born, Lithionics, Victron Smart Lithium)
- Módulo externo para bancos DIY (montagem própria com células soltas)
- Comunicação com o sistema via: display próprio, Bluetooth (app), CAN bus (NMEA 2000), VE.Bus (Victron)
- LED de status ou display de tensão por célula
- Relé ou MOSFET de potência que isola o banco quando proteção ativa

## Fundamentos mínimos

**Células em série vs banco:**

Um banco LiFePO4 de 12V é formado por 4 células de 3,2V em série (4 × 3,2V = 12,8V nominal). O BMS monitora cada célula individualmente — a tensão total do banco não revela o problema de uma célula desbalanceada.

**Balanceamento passivo vs ativo:**

| Tipo | Mecanismo | Eficiência | Custo |
| --- | --- | --- | --- |
| Passivo | Dissipa excesso em resistência (calor) | Baixa | Barato |
| Ativo | Transfere energia de célula mais cheia para mais vazia | Alta | Caro |

A maioria dos BMS acessíveis usa balanceamento passivo. Em bancos maiores, ciclos intensos ou células com maior dispersão, o balanceamento ativo pode ser vantajoso, mas não substitui seleção correta de células e boa montagem do banco.

**Comunicação BMS → sistema:**

BMS modernos podem comunicar limites dinâmicos de carga/descarga a carregadores, inversores e controladores. Isso permite reduzir corrente antes de um corte duro. Sem essa coordenação, a desconexão abrupta pode criar indisponibilidade de cargas, alarmes ou eventos elétricos indesejados no sistema.

## Parâmetros de configuração

| Parâmetro | Valor típico LiFePO4 |
| --- | --- |
| Tensão de corte superior (por célula) | Definida pelo fabricante da célula e pela estratégia do sistema |
| Tensão de corte inferior (por célula) | Definida pelo fabricante da célula e pela reserva de segurança adotada |
| Tensão de flutuação alvo | Muitas arquiteturas LiFePO4 trabalham com float reduzido ou sem float sustentado |
| Corrente máxima de carga (C-rate) | 0,5C a 1C (50–100A para banco 100Ah) |
| Corrente máxima de descarga | 1C a 2C |
| Temperatura máxima de operação | 45–60°C |
| Temperatura mínima para carga | 0°C (sem aquecimento) |

## Tipos de BMS por topologia

**BMS centralizado (comum em baterias prontas):**

- Um único módulo controla todas as células
- Mais simples, menor custo
- Ponto único de falha

**BMS distribuído (modular):**

- Um módulo por célula ou grupo de células
- Mais robusto, maior custo
- Usado em bancos grandes industriais

**BMS com relé de potência:**

- Usa relé eletromecânico para isolar o banco
- Mais simples, consome mais energia, gera arco no relé em alta corrente

**BMS com MOSFET de estado sólido:**

- Usa transistores MOSFET para isolação
- Sem arco elétrico, sem desgaste mecânico
- Padrão em baterias de qualidade

## Marcas e referências

- **Daly BMS** — barato, amplamente usado em bancos DIY, funcional
- **JBD/Overkill Solar** — melhor qualidade que Daly, app Bluetooth
- **Electrodacus** — DIY de alta qualidade, comunicação avançada
- **Victron Smart Lithium** — bateria pronta com BMS integrado e VE.Bus
- **Battle Born** — bateria americana pronta, BMS robusto, 10 anos de garantia
- **REC BMS** — BMS profissional com CAN bus, usado em iates
- **Orion BMS** — industrial, altamente configurável, caro

## Problemas mais frequentes

| Problema | Causa | Diagnóstico |
| --- | --- | --- |
| BMS desconectando banco frequentemente | Célula desbalanceada atingindo limite | Medir tensão de cada célula |
| BMS não permite carregamento | Temperatura abaixo de 0°C | Verificar temperatura do banco |
| BMS corta sob alta corrente | Corrente de pico excede limite configurado | Reduzir carga simultânea ou reconfigurar limite |
| Banco nunca atinge 100% | BMS interrompendo absorção prematuramente | Verificar configuração de tensão de corte |
| BMS morreu | Sobretensão externa, inversão de polaridade | Substituir BMS, verificar causa |
| Células com diferença > 0,2V | Desbalanceamento acumulado | Balanceamento manual ou ciclos de equalização |

## Diagnóstico prático

**Verificar estado das células:**

```
Via app Bluetooth do BMS (JBD, Daly, Victron):
→ Ver tensão individual de cada célula
→ Diferença entre maior e menor > 0,1V = desbalanceamento relevante
→ Diferença > 0,3V = problema sério de balanceamento

Sem app: medir tensão total do banco
→ Dividir por número de células (4 para 12V)
→ Resultado é a média — não revela desbalanceamento
```

**Verificar proteção ativa:**

```
BMS desconectou → verificar qual proteção ativou:
→ LED/app indica motivo (sobretensão, subtensão, temp, sobrecorrente)
→ Resolver a condição que causou a proteção
→ Nunca "forçar" o BMS a reconectar sem resolver a causa
```

## Boas práticas profissionais

- Nunca instalar banco LiFePO4 sem estratégia de BMS/supervisão adequada ao banco e à aplicação
- Verificar compatibilidade do BMS com o carregador/inversor (tensão de absorção, comunicação)
- Configurar o BMS com parâmetros corretos para o tipo de célula (não usar padrão de fábrica sem verificar)
- Comunicar o BMS com o sistema (Victron VE.Bus, NMEA 2000) para proteção suave
- Inspecionar as células periodicamente — balanceamento acumulado indica célula com problema

## Cuidados de instalação

- Verificar polaridade antes de conectar — inversão de polaridade destrói o BMS instantaneamente
- Instalar fusível entre o banco e o BMS (em série com o positivo) — o BMS não é o fusível do sistema
- Verificar que os cabos do BMS têm bitola adequada para a corrente máxima configurada
- Ventilação adequada — BMS com balanceamento passivo gera calor durante o balanceamento

## Erros comuns

**Usar carregador ou inversor sem coordenar limites com o BMS:**

O problema não é apenas "ser de chumbo" ou "ser de lítio". O problema é carregar fora da janela aceita pela célula e sem coordenação com o BMS. Isso gera cortes frequentes, envelhecimento prematuro e instabilidade do sistema.

**Instalar banco LiFePO4 sem qualquer BMS:**

"As células são LiFePO4, são mais seguras." Mais seguras que NMC, sim — mas ainda precisam de proteção contra sobrecorrente, subtensão e desbalanceamento.

**Ignorar a comunicação BMS-carregador:**

BMS sem comunicação desconecta abruptamente. Inversor em carregamento pode sofrer dano (pico de tensão na desconexão brusca). Usar comunicação para desligamento suave.

## Relação com outros sistemas

- **Banco de baterias LiFePO4:** o BMS é parte integrante, não acessório
- **Carregador de bateria:** deve ser compatível com a janela de tensão/corrente do banco e, idealmente, receber limites do BMS
- **Alternador:** precisa ser tratado junto com o BMS quando o banco puder absorver corrente elevada por longos períodos
- **Inversor/carregador Victron:** comunicação VE.Bus com BMS para proteção integrada
- **Monitor de bateria (BMV/Shunt):** complementa o BMS — monitoramento do banco como um todo
- **VRM:** dados do BMS podem aparecer no painel remoto Victron

## Normas aplicáveis

- **IEC 62619** — Secondary cells and batteries for use in industrial applications — Safety requirements (inclui BMS)
- **UN38.3** — transporte de baterias de lítio (para importação/exportação)
- **ABYC E-11** — referência geral para sistemas elétricos DC
- **Especificações do fabricante** — parâmetros de configuração por tipo de célula

## Como ensinar este tópico

**Sequência recomendada:**

1. Por que o lítio é diferente: sensibilidade a sobretensão e subtensão — sem BMS, morre rápido
2. O que o BMS monitora: mostrar app ao vivo — tensão de cada célula em tempo real
3. Proteções: simular subtensão (descarregar célula) — BMS desconecta
4. Balanceamento: o que é, por que acumula, como corrigir
5. Integração com Victron: como BMS e MultiPlus conversam, por que isso importa

**Conceito-chave para fixar:**

"O BMS é o sistema nervoso do banco de lítio. Sem ele, o banco não dura — e pode ser perigoso."

## FAQ

**Posso usar banco LiFePO4 sem BMS se for muito cuidadoso?**

Não recomendado. O desbalanceamento de células ocorre gradualmente e é invisível sem monitoramento por célula. Uma célula desbalanceada não aparece na tensão total do banco até o momento em que atinge o limite — e então o dano já pode ser irreversível.

**BMS externo ou bateria com BMS interno?**

Para usuário final: bateria com BMS interno (plug-and-play, sem configuração). Para instalações técnicas com personalização: BMS externo configurável. Para bancos DIY com células soltas: BMS externo obrigatório.

**O BMS garante balanceamento perfeito?**

BMS com balanceamento passivo equilibra na carga (topo do ciclo). Células com diferença grande de capacidade nunca ficam perfeitamente balanceadas por BMS passivo. BMS ativo equilibra em qualquer ponto do ciclo — solução superior para bancos com células heterogêneas.

## Integração com outras notas

- [[Bancos de Bateria]]
- [[Alternador (DC)]]
- [[Carregador de Bateria (AC To DC)]]
- [[Inversora (DC To AC)]]
- [[Lítio LiFePO4 — Instalação e Cuidados Específicos]]
- [[Monitor de Bateria / BMV / Shunt]]
- [[Tipos de Bateria]]

## Perguntas que esta nota responde

- O que é BMS — Battery Management System em instalações elétricas náuticas?
- Qual é a função de BMS — Battery Management System na embarcação?
