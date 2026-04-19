---
title: "Iluminação de Emergência a Bordo"
note_type: "technical-note"
domain: "55_Iluminacao_e_Sinalizacao"
source_file: "ILUMINAÇÃO DE EMERGÊNCIA A BORDO 33a19734f7fb8168b037e6556cf0b429.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "26"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
  - "internacional"
normas_citadas:
  - "SOLAS Chapter II-1 Regulation 41 — Main source of electrical power and lighting"
  - "SOLAS Chapter II-1 Regulation 42 — Emergency source of electrical power in passenger ships"
  - "SOLAS Chapter II-1 Regulation 43 — Emergency source of electrical power in cargo ships"
  - "SOLAS Chapter II-2 Regulation 13 — Means of escape (iluminação em saídas)"
  - "IMO Resolution A.752(18) — Guidelines for safe working practices for ship personnel"
  - "IMO MSC/Circ.1032 — Emergency lighting (referência técnica)"
  - "IMO Resolution MSC.81(70) — Low location lighting (LLL)"
  - "IMO Resolution A.654(16) — Graphical symbols for fire control plans"
  - "IEC 60598-2-22 — Luminaires — Particular requirements — Luminaires for emergency lighting"
  - "IEC 60945 — Maritime navigation and radiocommunication equipment — General requirements"
  - "IEC 61508 / 61511 — Functional safety (quando integrado a sistema de controle)"
  - "EN 1838 — Lighting applications — Emergency lighting (europeu)"
  - "EN 50172 / IEC 62034 — Emergency escape lighting systems (testes automáticos)"
  - "ISO 15370 — Low location lighting (fotoluminescente em navios passageiros)"
  - "ISO 17631 — Ships and marine technology — Shipboard plans for fire protection, life-saving and escape"
  - "ISO 24409 — Design, location and use of shipboard safety signs"
  - "USCG 46 CFR Part 111 — Electrical engineering (iluminação emergência comercial)"
  - "USCG 46 CFR Part 112 — Emergency lighting and power systems"
  - "USCG 46 CFR Part 133 — Off-vessel survival craft equipment"
  - "ABYC A-16 (2023) — Electric Navigation Lights (interface com navlights backup)"
  - "ABYC E-11 (2023) — AC and DC Electrical Systems on Boats (hotline, fusível, bitola)"
  - "ABYC A-4 — Fire fighting equipment (iluminação de extintores)"
  - "NORMAM-201/DPC — Tráfego e Permanência de Embarcações"
  - "NORMAM-205/DPC — Navios e embarcações empregadas na navegação interior (embarcações de passageiros)"
  - "NORMAM-211/DPC — Embarcações de esporte e recreio"
  - "NR-30 MTE — Segurança e saúde no trabalho aquaviário"
  - "ABNT NBR 10898:2013 — Sistema de iluminação de emergência"
  - "ABNT NBR IEC 60598-2-22:2017 — Luminárias para iluminação de emergência"
  - "ABNT NBR 5410:2004 + emendas — Instalações elétricas de baixa tensão"
  - "ABNT NBR 13434 — Sinalização de segurança contra incêndio e pânico"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://abycinc.org/standards/"
  - "https://www.imo.org/en/OurWork/Safety/Pages/SOLAS.aspx"
  - "https://www.iso.org/standard/62326.html"
  - "https://www.gov.br/trabalho-e-previdencia/pt-br/assuntos/inspecao-do-trabalho/seguranca-e-saude-no-trabalho/normas-regulamentadoras-nrs"
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

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **Iluminação de emergência é sistema, não luminária isolada** — inclui fonte alternativa de energia (bateria interna, hotline, gerador emergência), luminárias com autonomia, sinalização fotoluminescente e lanternas portáteis; em SOLAS Cap II-1 Reg 42 é arquitetura auditável.
> 2. **Três camadas devem coexistir: automática elétrica + fotoluminescente passiva + portátil** — camada 1 garante acendimento automático ao blackout, camada 2 funciona sem energia nenhuma (low location lighting ISO 15370), camada 3 é a última linha de autonomia.
> 3. **Autonomia mínima em luminária de emergência é definida por norma, não fabricante** — IMO MSC/Circ.1032 recomenda ≥ 3 h em navios passageiros; EN 1838 exige ≥ 1 h em edificações; para cruzeiro recreio offshore, 3 h é referência técnica válida.
> 4. **Circuito de carga da luminária NÃO pode estar na chave geral** — ao desligar a chave, a bateria interna para de carregar e descarrega em dias/semanas; circuito dedicado permanente (hotline com fusível próprio ABYC E-11) é obrigatório para projeto correto.
> 5. **Teste de autonomia anual é a única verificação confiável** — "acende quando aperto o botão" não é teste; teste correto: simular blackout completo e cronometrar até apagar; registrar em log de manutenção (exigido em charter/comercial).
> 6. **Low Location Lighting (LLL, ISO 15370) é obrigatório em passageiros SOLAS** — faixa fotoluminescente a 15-30 cm do piso em corredores para evacuação em fumaça (fumaça sobe, visão abaixo dela é preservada); aplicação recreio é recomendação, não obrigação.
> 7. **Bateria NiCd 3-5 anos, LiFePO4 8-10 anos, Pb-ácida selada 2-3 anos** — substituição preventiva por tempo, NÃO por aparência (luminária pode acender por 30 s apenas e parecer funcionar).
> 8. **LED HOTLINE direto à bateria casa é a solução mais simples para recreio** — ABYC E-11 com fusível < 7 polegadas do banco, LED < 2 W consome < 0,15 A × 24 h = < 4 Ah/dia, desprezível se banco é mantido carregado.
> 9. **Sinalização adesiva fotoluminescente (ABNT NBR 13434) marca rotas de saída, extintores, coletes** — charge em luz ambiente durante o dia, emite por 2-8 h no escuro; sem energia, sem manutenção elétrica; complemento obrigatório.

> [!danger] Quando chamar um especialista (engenheiro elétrico/projetista de sistemas de segurança contra incêndio marítimo)
> 1. **Projeto de emergência em navio passageiro SOLAS (≥ 36 passageiros)** — arquitetura de sistema emergência com transferência automática (ATS), fonte emergência dedicada (gerador emergência ABAIXO de linha d'água, não no fundo), luminárias em cada compartimento, LLL em corredores; escopo completo de engenharia de projeto naval.
> 2. **Integração com sistema de detecção de incêndio e evacuação** — IMO/SOLAS Cap II-2 Reg 13 exige que detecção de fogo + alarme + iluminação emergência + portas corta-fogo operem em cadeia; projeto functional safety IEC 61508/61511.
> 3. **Embarcação de charter brasileira em inspeção DPC** — NORMAM-205 exige plano de combate a incêndio, iluminação emergência com autonomia ≥ 30 min, luminárias em saída e corredor, sinalização fotoluminescente em rotas de fuga; projeto aprovado pela Capitania é mandatório.
> 4. **Retrofit em embarcação de recreio > 12 m com uso comercial/charter** — mudança de NORMAM-211 (recreio) para NORMAM-201 (comercial) exige upgrade de iluminação emergência: ponto crítico em transição de uso.
> 5. **Testes de autonomia com dispositivo de self-test** — luminárias modernas (IEC 62034) têm auto-teste semanal/mensal com LED indicador de status; comissionamento requer programação de cronograma de teste e registro em sistema de gerenciamento.
> 6. **Embarcação com sistema AC 110/220 V e iluminação emergência AC** — sistemas > 12 V AC exigem proteção residual DR, aterramento conforme ABNT NBR 5410, separação de circuitos AC de emergência e normal; projeto elétrico AC com análise de falha.
> 7. **Gerador de emergência com partida automática** — transferência automática (ATS) requer comissionamento profissional, teste mensal sob carga, manutenção preventiva, combustível independente do motor principal; escopo de marinha mercante.
> 8. **Perícia pós-sinistro com alegação "iluminação emergência não funcionou"** — laudo forense envolvendo falha de evacuação noturna requer leitura de logs (se self-test), teste em laboratório das luminárias, verificação de manutenção; escopo jurídico.
> 9. **Embarcação com lítio e risco de thermal event** — iluminação emergência em área de bateria lítio deve considerar BMS trip, supressão H2/VOCs na ventilação, manter iluminação sobre válvulas de desconexão e saída de emergência; projeto específico ABYC TE-13 e equivalentes.

> [!info] Glossário rápido (≈ 46 termos)
> - **Iluminação de emergência** — sistema autônomo ativado em blackout.
> - **Emergency lighting (EM)** — categoria luminária IEC 60598-2-22.
> - **Escape lighting** — iluminação específica de rotas de fuga (EN 1838).
> - **Low Location Lighting (LLL)** — ISO 15370, faixa baixa em corredores.
> - **Anti-panic lighting** — ilumina área aberta para evitar pânico.
> - **Standby lighting** — ilumina operação essencial (sala de controle).
> - **Central battery system (CBS)** — bateria centralizada para várias luminárias.
> - **Self-contained luminaire** — luminária com bateria interna (mais comum recreio).
> - **ATS (Automatic Transfer Switch)** — transferência automática entre fontes AC.
> - **Emergency generator** — gerador de emergência dedicado.
> - **Fonte primária** — fonte de energia normal da embarcação.
> - **Fonte emergência** — fonte de energia alternativa (bateria ou gerador).
> - **Blackout** — falha total da fonte primária.
> - **Autonomia (backup time)** — tempo que a luminária opera sem fonte primária.
> - **Self-test (IEC 62034)** — teste automático periódico da luminária.
> - **Indicator LED** — LED de status (verde = OK; piscante = falha).
> - **Fotoluminescente (photoluminescent)** — material que emite após absorver luz.
> - **Fluorescente** — emite enquanto excitado (diferente de fotoluminescente).
> - **Fosforescente (sinônimo aqui)** — emite após excitação por horas.
> - **ISO 15370 low location** — faixa fotoluminescente em corredor passageiros.
> - **ISO 17631** — planos de escape e proteção incêndio em navios.
> - **ISO 24409** — sinais de segurança naval.
> - **SOLAS Cap II-1 Reg 42** — emergency power passenger ships.
> - **SOLAS Cap II-2 Reg 13** — means of escape.
> - **MSC/Circ.1032** — emergency lighting guidance.
> - **MSC.81(70)** — Low Location Lighting.
> - **Hotline** — circuito permanente ao banco DC.
> - **LED HOTLINE** — LED ligado direto à bateria (bypass chave geral).
> - **Fusível ABYC E-11** — < 7" do banco, proteção contra curto.
> - **IP-54 (interior)** — proteção ingress interna.
> - **IP-67 (exterior/máquinas)** — proteção exterior marinha.
> - **NiCd (nickel-cadmium)** — bateria tradicional de emergência, 3-5 anos.
> - **LiFePO4** — bateria moderna de emergência, 8-10 anos.
> - **Pb-ácida selada (SLA/VRLA)** — bateria standby, 2-3 anos.
> - **Cronograma de teste** — registro anual de autonomia.
> - **Lux** — unidade de iluminância (lm/m²); mínimo 1-5 lux em rota de escape.
> - **Lumens (lm)** — fluxo luminoso total.
> - **Luminária compacta** — unidade única com bateria + LED + drive.
> - **Luminária bulkhead** — fixada na antepara (parede).
> - **Exit sign (placa saída)** — sinalização luminosa fotoluminescente ou LED.
> - **Pictogram ISO 7010** — símbolos padronizados de segurança.
> - **NR-30 MTE** — norma brasileira trabalho aquaviário.
> - **NBR 10898** — sistema iluminação emergência brasileira.
> - **NBR 13434** — sinalização segurança incêndio e pânico.
> - **MBR (marcação a bordo)** — reembarcação e rota de escape.
> - **Checklist pré-viagem** — verificação periódica obrigatória.

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
| **Hella Marine** | EasyFit Emergency | LED bateria | IMO / SOLAS (edição a verificar) |
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

- **SOLAS Chapter II-1 Regulation 41** — Main source of electrical power and lighting (fonte primária de energia e iluminação de bordo).
- **SOLAS Chapter II-1 Regulation 42** — Emergency source of electrical power in passenger ships (fonte emergência obrigatória em passageiros).
- **SOLAS Chapter II-1 Regulation 43** — Emergency source of electrical power in cargo ships (fonte emergência em navios de carga).
- **SOLAS Chapter II-2 Regulation 13** — Means of escape (iluminação em saídas de fuga).
- **IMO Resolution A.752(18)** — Guidelines for safe working practices for ship personnel (iluminação para trabalho seguro).
- **IMO MSC/Circ.1032** — Emergency lighting (referência técnica detalhada).
- **IMO Resolution MSC.81(70)** — Low location lighting (LLL) sistemas fotoluminescentes em corredores de passageiros.
- **IMO Resolution A.654(16)** — Graphical symbols for fire control plans.
- **IEC 60598-2-22** — Luminaires — Particular requirements — Luminaires for emergency lighting (padrão internacional de luminárias de emergência).
- **IEC 60945** — Maritime navigation and radiocommunication equipment — General requirements (EMC, IP, vibração para ambientes marinhos).
- **IEC 61508 / IEC 61511** — Functional safety of electrical/electronic systems (quando integrado a sistema de controle e incêndio).
- **EN 1838** — Lighting applications — Emergency lighting (padrão europeu, 1 h autonomia mínima em edificações, aplicável como referência).
- **EN 50172 / IEC 62034** — Emergency escape lighting systems — Automatic test systems (luminárias com auto-teste).
- **ISO 15370** — Low location lighting on passenger ships (fotoluminescente a 15-30 cm do piso).
- **ISO 17631** — Ships and marine technology — Shipboard plans for fire protection, life-saving appliances and means of escape.
- **ISO 24409** — Design, location and use of shipboard safety signs.
- **USCG 46 CFR Part 111** — Electrical engineering (iluminação emergência comercial norte-americana).
- **USCG 46 CFR Part 112** — Emergency lighting and power systems.
- **USCG 46 CFR Part 133** — Off-vessel survival craft equipment.
- **ABYC A-16 (2023)** — Electric Navigation Lights (interface com navlights de backup).
- **ABYC E-11 (2023)** — AC and DC Electrical Systems on Boats (hotline, fusíveis, bitola do circuito de emergência).
- **ABYC A-4** — Fire fighting equipment (iluminação de extintores de incêndio).
- **NORMAM-201/DPC** — Tráfego e Permanência de Embarcações (comerciais brasileiras).
- **NORMAM-205/DPC** — Navios e embarcações empregadas na navegação interior (embarcações de passageiros; iluminação emergência obrigatória).
- **NORMAM-211/DPC** — Embarcações de esporte e recreio.
- **NR-30 MTE** — Segurança e saúde no trabalho aquaviário (iluminação de áreas de trabalho).
- **ABNT NBR 10898:2013** — Sistema de iluminação de emergência (padrão brasileiro de referência para projeto).
- **ABNT NBR IEC 60598-2-22:2017** — Luminárias para iluminação de emergência (adoção nacional do IEC 60598-2-22).
- **ABNT NBR 5410:2004 + emendas** — Instalações elétricas de baixa tensão (aplicável ao sistema AC 110/220 V de emergência).
- **ABNT NBR 13434** — Sinalização de segurança contra incêndio e pânico (rotas de fuga, sinais fotoluminescentes).

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
