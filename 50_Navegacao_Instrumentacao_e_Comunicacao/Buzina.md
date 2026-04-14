---
title: "Buzina"
note_type: "technical-note"
domain: "50_Navegacao_Instrumentacao_e_Comunicacao"
source_file: "BUZINA e2519734f7fb835c88cc01ee230c806c.md"
status: "technical-review-l1"
aliases:
  - "BUZINA"
seo_title: "Buzina"
seo_description: "Buzina é meio de sinalização sonora da embarcação. Os requisitos de intensidade, alcance e arranjo dependem do porte e das regras aplicáveis de sinalização sonora."
seo_keywords:
  - "Buzina"
  - "50 Navegacao Instrumentacao e Comunicacao"
geo_queries:
  - "O que é Buzina em instalações elétricas náuticas?"
  - "Como diagnosticar falhas em Buzina?"
related_notes:
  - "AIS (Automatic Identification System)"
  - "Bússola Eletrônica (Compass / HDG Sensor)"
  - "Chartplotter / GPS / MFD"
  - "Dsc — Chamada Seletiva Digital"
  - "EPIRB / Beacon de Emergência"
  - "Estação de Vento / Anemômetro"
  - "Mob — Man Overboard — Sistema de Detecção"
  - "NAVEGAÇÃO (BB, BE e Alcançado)"
---

# Buzina

> [!abstract] Resumo técnico
> Buzina é meio de sinalização sonora da embarcação. Os requisitos de audibilidade e o tipo de dispositivo dependem do porte da embarcação e do enquadramento das regras de sinalização sonora. Instalação inadequada ou corrosão tornam o sistema pouco confiável quando ele mais importa.

## O que é e exigência regulatória

Buzina náutica é um dos meios possíveis de sinalização sonora previstos nas COLREGs (Regulamento Internacional para Evitar Abalroamentos no Mar), cujo arranjo depende do porte e da categoria operacional da embarcação:

- Toda embarcação deve ter aparelho para fazer sinais sonoros
- Embarcações abaixo de 12m: whistle (apito) é suficiente
- Embarcações de 12m a 20m: deve ter apito E sino
- Embarcações acima de 20m: apito, sino e gongo

**Sinais obrigatórios:**

- Restrição de visibilidade: um som longo a cada 2 minutos (a motor), dois sons longos + um curto a cada 2 minutos (à vela)
- Manobra: sinais específicos para virar a BB, virar a BE, inverter marcha
- Em fundeio com visibilidade restrita: sino rápido por 5 segundos a cada minuto

**Sonoridade mínima:**

As especificações de potência sonora variam por comprimento — consultar COLREGS Anexo III para os valores exatos.

## Tipos de buzina náutica

**Buzina elétrica (horn):**

Motor ou solenoide que vibra uma membrana metálica. 12V DC. Mais potente e confiável que buzinas a ar comprimido pequenas.

**Buzina a ar comprimido com compressor:**

Compressor elétrico pressuriza câmara, ar expulso pelos dutos gera som. Potente, mas com motor adicional para manutenção.

**Buzina de pressão (lata pressurizada):**

Manual, sem elétrica. Limitada em uso — latas se esgotam. Adequada como backup, não como instalação primária.

**Buzina eletrônica (piezo):**

Emite som por piezoelétrico. Baixo consumo, compacta, menor volume. Adequada para embarcações pequenas com exigência menor.

## Instalação, problemas e diagnóstico

**Posicionamento correto:**

A buzina deve estar onde possa ser ouvida ao redor da embarcação — geralmente no arco ou na proa superior. Protegida de respingos diretos, mas não obstruída por estrutura que reduza propagação do som.

**Corrente típica:**

Buzinas elétricas de 12V consomem 2-8A no acionamento (frações de segundo). Baixo impacto no banco.

**Problemas comuns:**

| Problema | Causa provável |
| --- | --- |
| Buzina não funciona | Fusível queimado, corrosão nos terminais, bobina com defeito |
| Som fraco | Membrana corroída, câmara de ressonância obstruída por insetos/lama |
| Buzina ativa intermitentemente sozinha | Contato do botão com curto (umidade) |

**Diagnóstico rápido:**

Medir tensão nos terminais da buzina ao pressionar o botão. Se 12V e não soa: buzina com defeito. Se sem tensão: problema na chave ou no fusível.

## Marcas e boas práticas

**Marcas:**

- **Kahlenberg** — americana, referência em buzinas de alta qualidade para embarcações maiores
- **Fiamm** — italiana, popular em embarcações europeias, boa qualidade
- **Marinco** — linha completa para marine
- **Marco** — italiana, linha extensa de buzinas marinas
- **Plastimo** — acessível, presente no mercado nacional

✅ Boas práticas:

- Testar a buzina antes de qualquer saída ao mar
- Limpar a abertura de saída de som periodicamente (acúmulo de sujeira reduz volume)
- Manter backup (buzina de lata pressurizada) no kit de emergência
- Verificar borracha de vedação do botão — umidade nos contatos causa falhas intermitentes

❌ Erros comuns:

- Buzina de carro em lugar de buzina marinha — degradação acelerada por névoa salina
- Buzina obstruída por estrutura ou na posição errada — som não propaga corretamente
- Não testar antes de sair — falha descoberta em situação de nevoeiro
- ❓ Perguntas frequentes

**Toda embarcação precisa de buzina?**

Toda embarcação deve dispor de meio de sinalização sonora compatível com as regras aplicáveis. Embarcações menores podem atender com apito/whistle; em outras, o arranjo exige também sino ou outros dispositivos conforme comprimento e regra específica.

**A buzina pode ser acionada por painel?**

Sim — muitos painéis modernos têm botão de buzina integrado que aciona a buzina externa. Isso é preferível a botões expostos na estrutura externa que oxidam.

**Buzina marinha vs buzina de carro — qual a diferença real?**

A marinha tem vedação IP67+, material resistente à névoa salina, e é projetada para exposição permanente ao ambiente externo. A de carro se corrói em 1-2 temporadas de uso náutico.

## Integração com outras notas

- [[AIS (Automatic Identification System)]]
- [[Bússola Eletrônica (Compass / HDG Sensor)]]
- [[Chartplotter / GPS / MFD]]
- [[Dsc — Chamada Seletiva Digital]]
- [[EPIRB / Beacon de Emergência]]
- [[Estação de Vento / Anemômetro]]
- [[Mob — Man Overboard — Sistema de Detecção]]
- [[NAVEGAÇÃO (BB, BE e Alcançado)]]

## Perguntas que esta nota responde

- O que é Buzina em instalações elétricas náuticas?
- Como diagnosticar falhas em Buzina?
