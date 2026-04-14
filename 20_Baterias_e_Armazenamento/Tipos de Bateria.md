---
title: "Tipos de Bateria"
note_type: "comparison"
domain: "20_Baterias_e_Armazenamento"
source_file: "TIPOS DE BATERIA 17419734f7fb83e38ee80148dae5ba3c.md"
status: "technical-review-l1"
aliases:
  - "TIPOS DE BATERIA"
seo_title: "Tipos de Bateria"
seo_description: "Tipos de bateria em náutica devem ser comparados por química, função, profundidade de descarga, regime de carga, massa, manutenção e integração com o sistema elétrico. Não existe bateria universal; existe compatibilidade técnica com a aplicação."
seo_keywords:
  - "Tipos"
  - "Bateria"
  - "20 Baterias e Armazenamento"
geo_queries:
  - "O que é Tipos de Bateria em instalações elétricas náuticas?"
  - "Qual é a função de Tipos de Bateria na embarcação?"
related_notes:
  - "Alternador (DC)"
  - "Bancos de Bateria"
  - "Carregador de Bateria (AC To DC)"
  - "Monitor de Bateria / BMV / Shunt"
  - "BMS — Battery Management System"
  - "Lítio LiFePO4 — Instalação e Cuidados Específicos"
  - "Tipos de Embarcação"
---

# Tipos de Bateria

> [!abstract] Resumo técnico
> Tipos de bateria devem ser comparados por química, função, regime de carga, profundidade de descarga, manutenção e integração com o restante do sistema. Escolher a bateria só por preço ou Ah de catálogo leva a erro de projeto, baixa autonomia e envelhecimento prematuro.

## O que é

Bateria é um dispositivo eletroquímico que converte energia química em elétrica (descarga) e energia elétrica em química (carga). Em embarcações, ela cumpre funções críticas que vão da partida do motor ao sustento de toda a carga de bordo sem motor ligado.

Cada tecnologia tem uma química diferente, com comportamento elétrico, perfil de carga, ciclo de vida e custo específicos. Não existe "bateria universal" para uso náutico — a escolha correta depende da função, do sistema de carga e do orçamento.

As tecnologias mais relevantes para embarcações de esporte e recreio no Brasil:

- **Chumbo-ácido inundada (FLA)** — mais barata, exige manutenção, pouco tolerante a vibração
- **AGM (Absorbed Glass Mat)** — selada, resistente, padrão atual no mercado náutico brasileiro
- **GEL** — selada, curva de carga específica, tolerante a calor, comum em embarcações europeias
- **Lítio LiFePO4** — alta performance, exige BMS e integração correta, custo inicial mais alto

## Função na embarcação

As baterias servem a bordo como:

- **Banco de partida:** fornece corrente de pico alta e curta para o motor de arranque. Parâmetro relevante: CCA (Cold Cranking Amperes). Bateria automotiva pode servir aqui desde que protegida de vibração.
- **Banco de serviço:** fornece corrente moderada por tempo prolongado para iluminação, bombas, eletrônicos, rádio, GPS. Exige bateria de ciclo profundo.
- **Reserva de emergência:** terceiro banco em embarcações maiores, isolado para garantia de partida do motor principal.
- **Buffer de energia:** em sistemas com múltiplas fontes (shore power, solar, gerador, alternador), o banco recebe e entrega energia conforme disponibilidade.

A separação de bancos por função é um dos princípios fundamentais do projeto elétrico náutico. Misturar partida e serviço em um único banco é o erro mais comum e mais custoso.

## Como aparece na prática

**Embarcações nacionais menores (alumínio, pesca, lanchas populares):**

Quase sempre bateria automotiva convencional para tudo — partida e serviço misturados. Vida útil de 1-2 anos no melhor caso. Erro comum repetido por anos sem o proprietário entender a causa.

**Lanchas médias de fibra (18-28 pés):**

AGM como banco de serviço começa a aparecer, mas configuração raramente está correta. Bateria de partida separada às vezes existe, mas mal gerenciada — sem chave seletora adequada, sem fusível de banco.

**Barcos de vela e cruising:**

Configuração mais cuidadosa — banco de serviço AGM ou GEL de maior capacidade, alternador regulado, às vezes solar. Nível de organização elétrica superior ao mercado de potência.

**Embarcações importadas (Beneteau, Jeanneau, Azimut, etc.):**

AGM em configuração de banco, às vezes dois bancos separados (partida + serviço). Sistema projetado para padrão europeu.

**Embarcações premium e projetos modernos:**

LiFePO4 com BMS dedicado. Crescente especialmente em barcos acima de 40 pés ou projetos de integração elétrica completa.

## Fundamentos mínimos

**Por que a química importa:**

Cada tecnologia tem um perfil de tensão diferente durante carga e descarga. Usar carregador de AGM em GEL pode danificar as células ao longo do tempo. Usar carregador de chumbo em lítio pode causar incêndio.

**Conceitos essenciais:**

- **Capacidade (Ah):** quantidade de carga elétrica entregue sob um regime de ensaio. O valor real a bordo depende da taxa de descarga, temperatura e envelhecimento.
- **DoD (Depth of Discharge):** profundidade de descarga segura. AGM: 50%. GEL: 50-60%. LiFePO4: 80-90%.
- **C-rate:** taxa de carga/descarga em relação à capacidade. 1C em 100Ah = 100A. Chumbo-ácido prefere baixo C-rate de carga (C/5 a C/10).
- **Ciclos de vida:** número de ciclos carga/descarga antes de perda significativa de capacidade.
- **Tensão de corte:** deve ser interpretada com carga, repouso, química e proteção do sistema. Não existe um único número útil para todos os cenários.
- **SoC (State of Charge):** percentual de carga atual. Monitorar SoC real exige shunt — voltímetro sozinho é impreciso para chumbo.

## Características principais por tecnologia

**Chumbo-ácido inundada (FLA):**

- Custo mais baixo de todas as tecnologias
- Exige ventilação obrigatória — libera H₂ durante carga (explosivo)
- Exige reposição de água destilada periodicamente
- Alta sensibilidade a vibração
- DoD recomendado depende da vida útil desejada e da ficha técnica do fabricante
- Ciclos: 200-400 a 50% DoD
- Tensão nominal: 12V (6 células de 2V cada)

**AGM (Absorbed Glass Mat):**

- Eletrólito absorvido em mantas de fibra de vidro
- Selada — sem necessidade de reposição de nível
- Tolerante a vibração e instalação em ângulo
- Baixa autodescarga (~3% ao mês)
- Aceita carga mais rápida que GEL
- Tensão de absorção: 14,4-14,7V
- DoD recomendado: 50%
- Ciclos: 300-600 a 50% DoD
- Muito difundida no mercado náutico brasileiro

**GEL:**

- Eletrólito em forma de gel (sílica + ácido sulfúrico)
- Selada, tolerante a temperaturas altas
- Tensão máxima de absorção: ~14,1V (menor que AGM — ponto crítico)
- Não aceita carga rápida — danifica as células
- Melhor performance em descarga profunda lenta
- DoD recomendado: 50-60%
- Ciclos: 500-800
- Encontrada em parte das embarcações importadas e em aplicações específicas

**Lítio LiFePO4:**

- Peso reduzido — 1/3 do chumbo para mesma capacidade útil
- Alta eficiência de carga: ~98% vs ~85% do chumbo
- Exige BMS (Battery Management System) — obrigatório
- Carga rápida possível dentro do limite declarado pelo fabricante e pela estratégia térmica do sistema
- Temperatura segura para carga: 0°C a 45°C
- DoD seguro: 80-90%
- Ciclos: 2000-5000 a 80% DoD
- Custo inicial: 3-5x maior que AGM equivalente
- Em alguns cenários de uso intensivo, o custo total de propriedade pode ser competitivo

## Configurações e variações comuns

**Banco de partida vs banco de serviço:**

Separação funcional é a prática correta na maioria das embarcações. Banco de partida privilegia corrente de pico e confiabilidade de arranque; banco de serviço privilegia ciclo e autonomia.

**Bancos em paralelo:**

Aumenta capacidade em Ah sem alterar tensão. Exige baterias do mesmo tipo, mesma marca, mesma idade e estado de carga equilibrado no momento da conexão. Baterias desiguais criam circulação de corrente permanente entre elas.

**Bancos em série:**

Dobra a tensão (dois 12V = 24V). Capacidade em Ah permanece igual à de uma bateria individual. Comum em sistemas 24V e motores diesel maiores.

**Sistema isolado para emergência:**

Terceiro banco separado em embarcações maiores. Garantia de partida mesmo com bancos de serviço descarregados.

**LiFePO4 com BMS centralizado:**

Configuração profissional. BMS monitora tensão de célula, temperatura e corrente. Protege contra sobrecarga, descarga profunda e curto-circuito. Pode comunicar com monitores e sistemas de bordo via NMEA 2000 ou CAN bus.

## Principais marcas

**Chumbo-ácido / AGM — Mercado nacional:**

- **Moura** — líder no Brasil, boa disponibilidade, qualidade consistente. Linha Estacionária/Solar para ciclo profundo.
- **Heliar** — tradicional, acessível. Linha Freedom com perfil de ciclo profundo.
- **Tudor / Exide** — presentes no varejo, qualidade adequada para uso básico.

**AGM — Mercado náutico importado:**

- **Victron Energy** — referência absoluta no náutico. AGM Deep Cycle e AGM Super Cycle. Ecossistema completo integrado.
- **Fullriver** — importada, boa qualidade, popular em instalações maiores.
- **Trojan** — americana, referência em ciclo profundo, popular em sistemas náuticos e off-grid.

**GEL:**

- **Victron GEL** — referência no náutico, curva de carga bem documentada.
- **Sonnenschein (Exide)** — tradicional europeia, qualidade técnica reconhecida.
- **Banner** — europeia, boa performance em aplicações náuticas.

**LiFePO4:**

- **Victron** — padrão premium, integração total com ecossistema Smart Battery System.
- **Battle Born** — americana, popular em barcos de cruising.
- **SOK / Ampere Time / LiTime** — chinesas, custo acessível, qualidade variável. Avaliar BMS integrado.

## Componentes e sistemas relacionados

- **Carregador de bateria** — deve ter perfil compatível com a química (AGM, GEL e LiFePO4 são configurações diferentes no carregador)
- **Alternador** — tensão, corrente contínua e estratégia de regulação devem ser compatíveis com a química e o banco
- **BMS** — obrigatório em LiFePO4. Pode ser integrado (bateria pronta) ou externo (bancos de células)
- **Monitor de bateria / Shunt** — mede SoC real por integração de corrente. Victron BMV, Victron SmartShunt, Simarine PICO
- **Chave seletora de banco** — isola e seleciona bancos. Blue Sea Systems, Mastervolt
- **Fusíveis de banco** — proteção contra curto-circuito. Fusível ANL ou MIDI próximo ao terminal positivo
- **Controlador MPPT solar** — deve ter perfil configurado para a química da bateria
- **Sistema de ventilação** — obrigatório para FLA, recomendado para AGM/GEL em compartimentos fechados

## Onde costuma dar problema

| Problema | Sintoma típico | Consequência |
| --- | --- | --- |
| Bateria automotiva como serviço | Descarga rápida, não sustenta carga por tempo | Vida útil 6-18 meses |
| Banco subdimensionado | Tensão cai com carga leve | Motor não parte, cargas caem |
| Tecnologias mistas em paralelo | Desequilíbrio de carga | Desgaste acelerado da bateria mais fraca |
| Carregador incorreto para GEL | Superaquecimento, inchamento | Dano prematuro, substituição antecipada |
| LiFePO4 sem BMS | Sem sintoma visível até a falha | Risco de incêndio, perda total do banco |
| Descarga profunda não revertida | Tensão abaixo de 10,5V | Sulfatação irreversível no chumbo |
| Terminais sem proteção | Corrosão branca nos bornes | Alta resistência de contato, perda de carga |

## Causas raiz

**Bateria morre em menos de 2 anos:**

Causa raiz mais comum: bateria automotiva usada como banco de serviço. A bateria automotiva tem placas finas otimizadas para corrente de pico, não para descarga cíclica. Cada ciclo profundo destrói uma camada de material ativo. Não é defeito de fabricação — é uso inadequado.

**Banco em paralelo desequilibrado:**

Causa raiz: baterias de idades, marcas ou estados de carga diferentes. A bateria mais fraca age como carga permanente para a mais forte — aquece e se degrada mais rapidamente, puxando o banco inteiro para baixo.

**GEL danificada por carregador AGM:**

Causa raiz: tensão de absorção incorreta. GEL aceita máximo ~14,1V. Carregadores AGM chegam a 14,4-14,7V. Diferença pequena no número, grande no dano acumulado ao longo de centenas de ciclos.

**LiFePO4 com BMS disparando frequentemente:**

Causa raiz: célula desequilibrada, temperatura extrema, limite de corrente inadequado ou sistema de carga não coordenado com o BMS.

## Diagnóstico prático

**Verificação rápida em campo:**

Tensão em repouso (sem carga há mais de 2h) — bateria de chumbo:

- 12,7V ou mais → carga completa (~100% SoC)
- 12,4V → ~75% SoC
- 12,2V → ~50% SoC
- 12,0V → ~25% SoC
- Abaixo de 11,8V → profundamente descarregada

Teste com carga (10A por 30 segundos): tensão caiu mais de 0,5V imediatamente? Bateria enfraquecida.

Teste de partida: durante cranking, tensão não deve cair abaixo de 9,6V (sistema 12V).

**Banco em paralelo com problema:**

Medir tensão individual de cada bateria após carga completa e 2h de repouso. Diferença acima de 0,2V indica desequilíbrio — bateria com menor tensão provavelmente com problema.

**AGM inchada:**

Visual direto: caixa deformada. Causa: sobrecarga por carregador com tensão incorreta. Não tem reparo — substituir imediatamente.

**LiFePO4 com BMS disparado:**

Banco "desaparece" — tensão sobe ao remover carga mas não fornece corrente. Verificar alarmes do BMS, temperatura das células e equilíbrio de célula.

## Boas práticas

✅ Separar sempre banco de partida do banco de serviço

✅ Dimensionar o banco pela profundidade de descarga compatível com a química e com a vida útil desejada

✅ Usar baterias do mesmo tipo, marca e lote em bancos em paralelo

✅ Instalar monitor de bateria com shunt — voltímetro sozinho não é suficiente

✅ Documentar data de instalação, capacidade e parâmetros do banco

✅ Proteger terminais com vaselina técnica ou spray anticorrosivo

✅ Instalar fusível de banco o mais próximo possível do terminal positivo

✅ Fixar mecanicamente contra vibração — suporte firme, cinta ou bandeja dedicada

✅ Verificar tensão e estado dos terminais a cada 3-6 meses

✅ Para FLA: verificar nível do eletrólito mensalmente em clima quente

## Cuidados de instalação

- **Fixação mecânica:** vibração a bordo é constante e intensa. Bateria mal fixada se move, quebra terminais, causa curto-circuito. Usar bandeja, suporte com cinta ou compartimento específico.
- **Ventilação:** FLA libera H₂ durante carga — explosivo. Compartimento ventilado com saída para o exterior é obrigatório. AGM e GEL dispensam ventilação rígida, mas local arejado ainda é preferível.
- **Proteção dos terminais:** ambiente marinho corrói cobre e chumbo rapidamente. Aplicar vaselina técnica ou spray de proteção após conexão.
- **Fusível de banco:** proteção contra curto-circuito na linha principal. ANL ou MIDI fuse dimensionado para o cabo, instalado no máximo 30cm do terminal positivo da bateria.
- **Distância de fontes de calor:** motor, escapamento, equipamentos eletrônicos. Calor reduz vida útil e pode degradar o eletrólito.
- **Cabos dimensionados para pico:** corrente de partida pode atingir 400-600A. Cabo subdimensionado aquece, cai tensão e pode causar incêndio.

## Cuidados de uso

- Não descarregar AGM/GEL abaixo de 50% com frequência — reduz drasticamente a vida útil
- Recarregar imediatamente após descarga profunda — sulfatação começa em poucas horas no chumbo
- Monitorar temperatura no verão — baterias de chumbo degradam mais rápido acima de 30°C
- Desconectar banco de serviço em longos períodos sem uso
- LiFePO4: nunca carregar abaixo de 0°C — dano permanente por deposição de lítio metálico
- Não aplicar equalização em AGM, GEL ou LiFePO4 — processo válido apenas para FLA inundada
- Nunca conectar baterias de datas de fabricação muito diferentes em paralelo

## Erros comuns

❌ **Usar bateria automotiva como banco de serviço** — erro mais comum e mais custoso. Dura 6-18 meses no máximo em ciclo profundo.

❌ **Misturar marcas, idades ou estados de carga em bancos paralelos** — desequilíbrio permanente, desgaste acelerado.

❌ **Usar carregador de carro (14,8V+) em AGM ou GEL** — tensão de equalização destrói baterias seladas.

❌ **Instalar LiFePO4 sem BMS** — risco real de incêndio. BMS não é opcional.

❌ **Não separar banco de partida do banco de serviço** — arrisca não partir o motor após uma noite de consumo.

❌ **Dimensionar pela disponibilidade de espaço, não pela demanda** — banco subdimensionado sofre descarga profunda constante.

❌ **Não proteger terminais em ambiente marinho** — corrosão visível em 3-6 meses de marina.

❌ **Ignorar data de fabricação na compra** — bateria estocada por 1+ ano perde capacidade. Verificar sempre.

❌ **Conectar lítio e chumbo no mesmo banco** — perfis de carga completamente incompatíveis. Nunca fazer isso.

## Relação com outros sistemas

- **Alternador:** tensão de regulagem precisa ser compatível com a química. AGM: 14,4-14,7V de absorção. GEL: máximo 14,1V. LiFePO4: exige regulador externo programável.
- **Carregador de cais:** perfil de carga (bulk/absorção/flutuação) deve ser configurado para o tipo correto. Carregador errado é a causa mais comum de dano em baterias de barco.
- **BMS (LiFePO4):** controla cada célula individualmente. Comunica com alternador, carregador e monitor em sistemas avançados via NMEA 2000 ou CAN bus.
- **Monitor de bateria:** shunt na linha negativa mede corrente real e integra para calcular SoC. Dados precisos de tensão, corrente, Ah consumidos e Ah restantes.
- **Controlador MPPT solar:** perfil configurável para AGM, GEL ou LiFePO4.
- **Sistema de distribuição DC:** chave seletora, barramento, disjuntores — todos dimensionados para a corrente máxima possível do banco.

## Brasil x referências internacionais

🌎 **Brasil x referências internacionais**

**Prática comum no Brasil:**

Bateria automotiva como banco de serviço é extremamente difundida, especialmente em embarcações menores. AGM começa a ser padrão apenas em instalações mais cuidadosas ou em embarcações importadas. Ventilação de compartimento raramente obedece a critérios formais.

**Referência ABYC E-10:**

Define separação formal de bancos (start / house / emergency), exige baterias marinhas certificadas, compartimento ventilado para FLA com saída exterior, fusível próximo ao terminal positivo, fixação mecânica adequada.

**Referência ISO 10133:**

Para embarcações menores — aborda proteção do circuito principal, bitolamento de cabos, instalação de baterias e proteção contra curto-circuito.

**Ponto de conflito:**

No Brasil, a maioria das instalações não usa baterias com certificação marinha específica e não segue rigorosamente a separação de bancos. A norma brasileira tem menor detalhamento técnico em instalação elétrica que a ABYC.

**Leitura equilibrada:**

Adotar os princípios funcionais da ABYC — separação de bancos, fixação, ventilação, fusível próximo ao terminal — é viável e recomendável independentemente de certificação formal. A lógica de segurança se aplica universalmente.

## Normas e referências aplicáveis

| Referência | O que orienta | Relevância prática | Cuidado no Brasil |
| --- | --- | --- | --- |
| ABYC E-10 | Sistemas de bateria em embarcações | Separação de bancos, ventilação, fixação, proteção | Contexto americano — adaptar para realidade local |
| ISO 10133 | Instalações elétricas DC em embarcações pequenas | Proteção, bitolamento, instalação | Embarcações menores: referência mais aplicável |
| Victron Energy (documentação técnica) | Parâmetros de produto e integração | Muito bem documentado — usar como referência prática | Produto premium — adaptar para outros fabricantes |
| Datasheets do fabricante | Perfis específicos de carga e descarga | Essencial para configurar carregador e alternador | Sempre consultar antes de qualquer instalação |

## Destaques para ensino

🧠 **Pontos de maior impacto didático:**

- **Bateria automotiva vs ciclo profundo** — entrada mais poderosa do tema. Mostrar com números: 50-100 ciclos profundos na automotiva vs 500+ na AGM de ciclo profundo.
- **Conceito de DoD** — banco de 100Ah AGM = 50Ah utilizáveis na prática. Poucos técnicos dimensionam considerando isso.
- **Incompatibilidade GEL × carregador AGM** — diferença de 0,3-0,6V na tensão de absorção, mas dano acumulado real em centenas de ciclos.
- **Custo total de propriedade LiFePO4** — 4 trocas de AGM em 10 anos vs 1 banco LiFePO4. Números reais mudam completamente a percepção de custo.
- **BMS como sistema de segurança, não acessório** — mostrar casos reais de incêndio por ausência de BMS.

📸 **Recursos visuais de alto impacto:**

- AGM inchada por sobrecarga — foto real
- Bateria automotiva destruída após 1 ano de uso como serviço — foto comparativa
- Gráfico de ciclos de vida por tecnologia (curva de capacidade × ciclos)

## Ideias de vídeo, aula prática ou demonstração

🎬 **Conteúdo sugerido:**

- **"Por que sua bateria de barco não dura"** — diferença prática entre automotiva e ciclo profundo. Alto potencial de engajamento.
- **Comparativo visual: AGM vs GEL vs LiFePO4** — peso, tamanho, terminais, preço. Fácil de filmar com produtos físicos.
- **Como testar uma bateria náutica com multímetro** — procedimento passo a passo em campo.
- **Configurando carregador para GEL vs AGM** — demonstração do erro mais comum.
- **Estudo de caso: incêndio por LiFePO4 sem BMS** — discussão técnica com fotos reais.

## Ideias de diagramas, circuitos ou imagens

📊 **Diagramas e visuais sugeridos:**

- **Diagrama: banco de partida + banco de serviço + chave seletora** — configuração básica mais importante
- **Curva de descarga comparativa: AGM vs GEL vs LiFePO4** — tensão × % de descarga
- **Perfil de carga (bulk / absorção / flutuação) por tecnologia** — lado a lado
- **Tabela comparativa consolidada:** tecnologia × DoD × ciclos × peso × custo × aplicação ideal
- **Diagrama de proteção:** localização do fusível de banco, distância do terminal, bitola
- **Foto real:** fixação correta em compartimento náutico, terminais protegidos, etiquetagem
- ❓ Perguntas frequentes

**Posso usar bateria de carro no barco?**

Para partida: funciona, com redução de vida útil por vibração e umidade. Para banco de serviço: não recomendado. Bateria automotiva morre em 6-18 meses em ciclo profundo.

**AGM e GEL são a mesma coisa?**

Não. Ambas são seladas, mas têm perfis de carga diferentes. AGM aceita 14,4-14,7V de absorção. GEL: máximo 14,1V. Usar carregador de AGM em GEL causa dano acumulado ao longo do tempo.

**Preciso de BMS para AGM?**

Não obrigatório, mas um monitor com shunt é altamente recomendado para controle real de SoC. BMS é obrigatório apenas para lítio.

**LiFePO4 pega fogo facilmente?**

LiFePO4 é a química mais estável da família lítio. Com BMS correto e instalação adequada, o risco é muito baixo. O perigo real está em instalações sem BMS ou com BMS inadequado.

**Quantos Ah preciso para meu barco?**

Some todas as cargas em watts, divida por 12V para obter ampères, multiplique pelas horas de uso diário. Dobre para AGM (usa 50%) ou multiplique por 1,25 para LiFePO4 (usa 80%).

**Posso misturar AGM e GEL no mesmo banco?**

Não. Perfis de carga diferentes causam desequilíbrio e dano. Sempre usar o mesmo tipo, marca e lote.

**Quanto tempo dura uma bateria AGM em uso náutico?**

Com uso correto (não descarregar abaixo de 50%, carregador compatível, ambiente ventilado): 4-7 anos. Com uso incorreto: 1-3 anos.

## Integração com outras notas

- [[Bancos de Bateria]]
- [[Alternador (DC)]]
- [[Carregador de Bateria (AC To DC)]]
- [[Monitor de Bateria / BMV / Shunt]]
- [[BMS — Battery Management System]]
- [[Lítio LiFePO4 — Instalação e Cuidados Específicos]]
- [[Tipos de Embarcação]]
- [[Tipos de Lâmpadas e LEDs Náuticos]]

## Perguntas que esta nota responde

- O que é Tipos de Bateria em instalações elétricas náuticas?
- Qual é a função de Tipos de Bateria na embarcação?
