---
title: "Iluminação de Emergência a Bordo"
note_type: "technical-note"
domain: "55_Iluminacao_e_Sinalizacao"
source_file: "ILUMINAÇÃO DE EMERGÊNCIA A BORDO 33a19734f7fb8168b037e6556cf0b429.md"
status: "technical-review-l1"
aliases:
  - "ILUMINAÇÃO DE EMERGÊNCIA A BORDO"
seo_title: "Iluminação de Emergência a Bordo"
seo_description: "ILUMINAÇÃO DE EMERGÊNCIA — Sistema de iluminação destinado a manter orientação e segurança quando a energia principal falha, conforme a arquitetura e o perfil operacional da embarcação."
seo_keywords:
  - "Iluminação"
  - "Emergência"
  - "55 Iluminacao e Sinalizacao"
geo_queries:
  - "O que é Iluminação de Emergência a Bordo em instalações elétricas náuticas?"
  - "Qual é a função de Iluminação de Emergência a Bordo na embarcação?"
related_notes:
  - "Fitas Led / Iluminação Led"
  - "Dimmer — Controle de Intensidade Luminosa"
  - "Farol de Busca"
  - "Luz de Cortesia"
  - "Luz de Âncora"
  - "Luz Subaquática"
  - "Luzes Internas Teto"
  - "Strobo"
---

# Iluminação de Emergência a Bordo

> [!abstract] Resumo técnico
> ILUMINAÇÃO DE EMERGÊNCIA — Sistema de iluminação destinado a manter orientação e segurança quando a energia principal falha. O arranjo adequado depende do porte, do uso da embarcação, das rotas de fuga e da filosofia de alimentação de contingência.

## O que é

Sistema de iluminação que opera independentemente da energia elétrica principal da embarcação, garantindo visibilidade em situações de emergência — falha elétrica, fumaça, incêndio, evacuação noturna. Categorias:

- **Luminária de emergência com bateria interna:** lampada ou LED com bateria recarregável interna — carrega enquanto a energia está presente, acende automaticamente quando a energia falha
- **Faixas fosforescentes:** absorvem luz ambiente e emitem por horas no escuro — sem energia, sem manutenção elétrica
- **Lanternas portáteis de emergência:** armazenadas em ponto fixo de acesso rápido
- **LED HOTLINE:** iluminação conectada diretamente à bateria (sempre ligada, independente da chave geral)

## Função

- Iluminar corredores, saídas e escadas durante evacuação noturna
- Sinalizar a rota de saída (setas fosforescentes, faixas)
- Permitir localização de equipamentos de segurança no escuro (extintores, coletes, balsas)
- Orientação em caso de fumaça (faixas baixas = abaixo da fumaça)
- Em veleiros: iluminar o cockpit e saídas para o deck em emergência noturna

## Como aparece na prática

Em embarcações maiores (com cabines/corredores): luminárias de emergência no corredor principal, nas saídas para o deck e na casa de máquinas. Faixas fosforescentes na borda dos degraus.

Em embarcações de charter, passageiro ou operação com maior exigência de segurança, a necessidade e o nível de formalização do sistema tendem a ser maiores e devem ser verificados nas regras, inspeções e requisitos contratuais aplicáveis.

Em lanchas de dia: mínimo recomendado — lanterna portátil em local fixo e acessível.

## Fundamentos mínimos

| Tipo | Autonomia | Lux (mín.) | Recarga | Manutenção |
| --- | --- | --- | --- | --- |
| Luminária emergência bateria NiCd | 1–3h | 5–10 lux | Automática | Bateria 3–5 anos |
| Luminária emergência bateria LiFePO4 | 3–6h | 10–50 lux | Automática | Bateria 5–10 anos |
| LED HOTLINE direto | Contínuo (enquanto bateria OK) | Variável | N/A (direto bateria) | Fusível + manutenção bateria |
| Faixa fosforescente | 2–8h de emissão após carga | Baixo | Solar/luz ambiente | Limpar e reexpor à luz |
| Lanterna portátil | 4–12h | Variável | Manual (pilha/USB) | Pilha verificada periodicamente |

## Luminária de emergência — funcionamento

O tipo mais comum em embarcações maiores funciona assim:

```jsx
Energia principal disponível:
→ Circuito carrega a bateria interna continuamente
→ Luminária fica apagada (operação normal)

Falha de energia (black out):
→ Circuito detecta ausência de tensão
→ Bateria interna aciona automaticamente os LEDs
→ A luminária permanece energizada pelo tempo de autonomia previsto no projeto ou exigido pelo requisito aplicável
```

A bateria interna é o componente mais crítico. Em NiCd: perde capacidade gradualmente. Em LiFePO4: mais durável mas mais caro. Deve ser substituída a cada 3–5 anos independentemente de aparência.

## LED HOTLINE — alternativa prática

Uma solução simples e eficaz para embarcações de recreio:

```jsx
Bateria auxiliar → HOTLINE → fio sempre energizado → LED de baixo consumo
→ Não depende de nenhum circuito de energia principal
→ Permanece aceso enquanto a bateria auxiliar tiver carga
```

**Vantagem:** simples, sem bateria interna para gerenciar, custo baixo.

**Desvantagem:** se a bateria auxiliar estiver descarregada, não funciona. Saída: banco de baterias sempre mantido carregado.

## Faixas fosforescentes — sinalização passiva

- Absorvem luz durante o dia (luz solar ou artificial)
- Emitem por 2–8h no escuro (dependendo do produto e do nível de carga)
- Sem eletricidade, sem manutenção elétrica, sem falha por falta de bateria
- Aplicações: bordas de degraus, saídas, localização de equipamentos, setas direcionais
- Norma ISO 17631: retroreflective e fluorescent material para sinalizações de segurança

**Aplicação prática:** faixa fosforescente nas bordas de todos os degraus e escadas → visível no escuro → orienta evacuação mesmo sem nenhuma iluminação elétrica.

## Marcas e modelos

| Marca | Produto | Tipo | Certificação |
| --- | --- | --- | --- |
| **Hella Marine** | EasyFit Emergency | LED bateria | IMO / SOLAS |
| **Lumitec** | Emergency LED | LED bateria | IP67 |
| **Fire Angel** | Emergency Light | LED bateria | EN 60598-2-22 |
| **3M** | Safety Sign | Fosforescente | ISO 3864 |
| **Glow-in-dark tape** | — | Fosforescente | Vários |
| **Rule / Attwood** | LED HOTLINE | LED 12V direto | IP67 (marinho) |

**No Brasil:** mercado náutico tem poucas opções específicas. Luminárias industriais de emergência adaptadas são comuns.

## Problemas mais frequentes

| Problema | Causa raiz provável |
| --- | --- |
| Luminária não acende em teste | Bateria interna descarregada/vencida, circuito de carga com problema |
| Autonomia menor que o especificado | Bateria envelhecida, capacidade reduzida |
| LED HOTLINE apagado | Fusível queimado, bateria descarregada |
| Faixa fosforescente não brilha | Exposição insuficiente à luz (ficou tampada), produto vencido |
| Luminária não carrega | Circuito de recarga com problema, tomada sem tensão |

## Causas raiz

**Bateria interna vencida:** a causa mais comum. Após 3–5 anos, a bateria NiCd perde capacidade significativamente. A luminária parece funcional (LEDs acendem), mas apaga em minutos ao invés de 1–3h. O único teste eficaz é testar por duração completa — não apenas verificar se acende.

**Circuito de carga em falha:** se a tensão de carga cair por problema no circuito da embarcação, a bateria interna se descarrega gradualmente. Verificar tensão no pino de carga da luminária.

## Diagnóstico prático

```jsx
Teste de luminária de emergência:
Passo 1: Desligar a tensão de carga (simular falta de energia)
Passo 2: Verificar se a luminária acende automaticamente
Passo 3: Cronometrar a autonomia e comparar com a especificação do equipamento e com o requisito operacional adotado
Passo 4: Se apagar antes do tempo → bateria interna vencida → substituir
Passo 5: Restaurar a tensão de carga e verificar que retoma o carregamento

Teste LED HOTLINE:
Passo 1: Desligar toda a chave geral
Passo 2: LED HOTLINE deve permanecer aceso
Passo 3: Se apagou → não está em HOTLINE — corrigir a instalação
```

## Boas práticas profissionais

- Instalar iluminação de emergência em todas as rotas de evacuação
- Aplicar faixas fosforescentes nas bordas de degraus (backup sempre disponível)
- Testar autonomia completa da luminária anualmente (não apenas verificar se acende)
- Substituir baterias internas a cada 3–5 anos preventivamente
- Em embarcações de charter: manter registro de testes e substituições (exigido por inspeção)

## Cuidados de instalação

- Instalar em pontos que cubram a rota de evacuação (não apenas nos quartos)
- Fixação segura para suportar vibração e mar agitado
- IP mínimo: IP54 para interior / IP67 para exterior e casa de máquinas
- Certificar que o circuito de carga é sempre energizado (não na chave geral)
- Faixas fosforescentes: aplicar em superfície limpa e seca, área de exposição à luz

## Cuidados de uso

- Verificar periodicamente que as luminárias estão carregando (indicador de carga)
- Fazer teste de autonomia mínimo uma vez por ano
- Limpar faixas fosforescentes de depósitos de óleo/graxa (reduzem a emissão de luz)
- Substituir lanternas portáteis quando a pilha atingir 80% da vida útil

## Erros comuns de instaladores

- Instalar apenas nos quartos, esquecendo os corredores e saídas
- Conectar o circuito de carga na chave geral (sem energia, sem carga = bateria descarregada)
- Não fazer teste de autonomia
- Não instalar faixas fosforescentes como backup
- Instalar em local inacessível para substituição da bateria interna

## Relação com outros sistemas

- **Sistema elétrico principal:** fornece a carga contínua às baterias internas
- **Bateria da embarcação:** HOTLINE para LEDs diretos
- **Sistema de alarme geral:** pode integrar alarme de falha de iluminação de emergência
- **Sistema de incêndio:** iluminação de emergência crítica durante evacuação por fumaça
- **Coletes e equipamentos de segurança:** iluminação de emergência deve permitir localizá-los no escuro

## Brasil x Internacional

| Aspecto | Brasil | Internacional |
| --- | --- | --- |
| Iluminação emergência em recreio | Rara | Mais comum |
| Obrigatória em charter | Sim (quando inspecionado) | Obrigatória e verificada |
| Faixas fosforescentes | Quase ausentes | Padrão em embarcações de cruzeiro |
| Teste de autonomia | Raramente feito | Parte do log de segurança |
| LED HOTLINE como alternativa | Solução prática comum | Menos comum |

**Muito comum no Brasil:** ausência de iluminação de emergência dedicada — dependência de lanternas portáteis.

**Mais presente em embarcações maiores/premium:** sistema completo com luminárias de emergência, faixas fosforescentes e LED HOTLINE de backup.

## Normas e referências

- **SOLAS Chapter II-2 / Reg. 42:** Means of escape (iluminação de emergência — commercial)
- **IMO MSC/Circ.1032:** Emergency lighting (referência técnica)
- **IEC 60598-2-22:** Luminaires for emergency lighting
- **EN 1838:** Lighting applications — Emergency lighting
- **ISO 17631:** Retroreflective and fluorescent material (fosforescente)
- **NORMAM-01:** equipamentos de segurança (inclui iluminação)

## Como ensinar este tópico

**Sequência recomendada:**

1. Cenário real: evacuação noturna com falha elétrica — quanto você vê sem iluminação?
2. Explicar os tipos (bateria interna vs HOTLINE vs fosforescente)
3. Demonstrar o teste de autonomia (diferença entre "acende" e "dura o tempo necessário")
4. Mostrar aplicação de faixas fosforescentes
5. Discutir o plano de evacuação e como a iluminação se integra

## Ideias de vídeos

- "Iluminação de emergência no barco: por que é crítica e como instalar"
- "Teste de autonomia: sua luminária de emergência vai durar o tempo necessário?"
- "Faixas fosforescentes no barco: a solução mais simples e eficaz"
- "LED HOTLINE como iluminação de emergência: instalação e funcionamento"
- "Plano de evacuação noturna: onde fica cada equipamento no escuro?"

## Diagramas sugeridos

- Mapa de iluminação de emergência em embarcação típica (rotas de evacuação + posicionamento)
- Diagrama de circuito da luminária: carga automática + acionamento por falta de tensão
- Diagrama LED HOTLINE: bateria → fusível → LED permanente (sempre ligado)
- Comparativo: luminárias de bateria vs fosforescente vs HOTLINE (quando usar cada um)
- Escada de degraus com faixas fosforescentes: foto antes/depois (claro vs escuro)

## FAQ

**Lanterna portátil substitui a iluminação de emergência?**

Para uso simples: parcialmente. Mas depende de alguém lembrar de pegá-la no escuro, que a pilha esteja carregada, e que o local seja conhecido. Iluminação fixa automática é mais confiável.

**Faixa fosforescente funciona com luz artificial (lâmpada LED)?**

Sim. Qualquer luz visível carrega o fosforescente. LED azul/branco carrega mais eficientemente. Expor por pelo menos 30 minutos de luz intensa para carga máxima.

**LED HOTLINE gasta muita bateria?**

Depende do consumo. LEDs de 0.5–2W consomem 40–170mA em 12V. Em 24h = 1–4Ah consumidos. Significativo apenas se a bateria não for carregada. Usar LEDs de altíssima eficiência (>100 lm/W) minimiza o consumo.

**Com que frequência substituir a bateria da luminária de emergência?**

A vida útil depende da química, temperatura, regime de flutuação, ciclos de teste e especificação do fabricante. O critério correto é comparar a autonomia medida e o estado do equipamento com o requisito do sistema, e então substituir conforme o manual e o desempenho real observado.

**Quantas luminárias de emergência uma embarcação de 40' precisa?**

Mínimo: 1 por saída para o deck + 1 no corredor principal + 1 na casa de máquinas. Para embarcações com múltiplos camarotes, adicionar uma por corredor de cabines.

## Integração com outras notas

- [[Fitas Led / Iluminação Led]]
- [[Dimmer — Controle de Intensidade Luminosa]]
- [[Farol de Busca]]
- [[Luz de Cortesia]]
- [[Luz de Âncora]]
- [[Luz Subaquática]]
- [[Luzes Internas Teto]]
- [[Strobo]]

## Perguntas que esta nota responde

- O que é Iluminação de Emergência a Bordo em instalações elétricas náuticas?
- Qual é a função de Iluminação de Emergência a Bordo na embarcação?
