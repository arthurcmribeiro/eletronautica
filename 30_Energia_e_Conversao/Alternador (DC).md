---
title: "Alternador (DC)"
note_type: "component"
domain: "30_Energia_e_Conversao"
source_file: "ALTERNADOR (DC) e2819734f7fb8224ab728189f1ab5518.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "14"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction: "Brasil"
normas_citadas:
  - "ABYC E-11 (2023) — AC and DC Electrical Systems on Boats"
  - "ABYC E-13 (2023) — Lithium Ion Batteries (interface com alternador)"
  - "ABYC E-10 (2023) — Storage Batteries"
  - "ABYC H-25 (2023) — Power feeds for engine-mounted accessories"
  - "ISO 13297:2020 — Small craft — AC and DC installations"
  - "ISO 8846:2022 — Small craft — Electrical devices — Protection against ignition of surrounding flammable gases"
  - "ISO 8849:2003 — Electrically operated DC bilge pumps (referência de motor DC marinizado)"
  - "SAE J1171 — Marine ignition protection for alternators and starters"
  - "UL 1500 — Ignition-protected marine products"
  - "NMEA 2000 (IEC 61162-3) — Comunicação de rede marítima"
  - "ABNT NBR 5410:2004 — Instalações elétricas de baixa tensão"
  - "NORMAM-211/DPC — Embarcações de esporte e recreio"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
  - "https://www.sae.org/"
  - "https://www.ul.com/"
aliases:
  - "ALTERNADOR (DC)"
seo_title: "Alternador (DC)"
seo_description: "Alternador é a principal fonte de recarga DC em embarcações motorizadas, mas seu comportamento depende de correia, polias, regulador, temperatura, banco conectado e estratégia de proteção. Em sistemas modernos, não pode ser tratado como carregador universal."
seo_keywords:
  - "Alternador"
  - "30 Energia e Conversao"
geo_queries:
  - "O que é Alternador (DC) em instalações elétricas náuticas?"
  - "Qual é a função de Alternador (DC) na embarcação?"
related_notes:
  - "Arranque"
  - "Bancos de Bateria"
  - "BMS — Battery Management System"
  - "CAIS (Pier) (AC)"
  - "Carregador Elétrico para Tender e Jet Ski"
  - "Eólico (DC)"
  - "Gerador (AC)"
  - "Gerador (DC)"
  - "Inversora (DC To AC)"
  - "Lítio LiFePO4 — Instalação e Cuidados Específicos"
  - "Placa Solar (DC)"
---

# Alternador (DC)

> [!abstract] Resumo técnico
> Alternador é a principal fonte de recarga DC em embarcações motorizadas, mas seu desempenho e sua sobrevivência dependem de correia, polias, regulador, temperatura, banco conectado e estratégia de proteção. Em sistemas com lítio e alta demanda, o alternador deixa de ser "peça simples" e vira ponto crítico de arquitetura.

> [!tip] Regra de decisão em 30 segundos
> 1. **Alternador em barco é sistema, não peça.** Correia, polias, regulador, temperatura, banco conectado, proteção e ventilação compõem o sistema — trocar só o "alternador" sem olhar o resto é reincidir na mesma falha.
> 2. **Marinização não é opcional** — ABYC H-24, SAE J1171, UL 1500, ISO 8846 tratam ignition protection como requisito em motor a gasolina. Alternador automotivo em motor a gasolina é fonte de ignição próxima a vapores de combustível.
> 3. **Nunca desconecte a bateria com o motor ligado.** O campo indutor do rotor, sem carga no B+, gera pico de tensão > 50 V que destrói a ponte de diodos em milissegundos. Mesmo com voltímetro a postos — não faça.
> 4. **Banco lítio + alternador original sem regulador externo = queima programada.** BMS desconecta o banco, alternador perde carga, pico indutor queima diodos. Regulador externo programável (Balmar MC-614, Wakespeed WS500) ou DC-DC charger (Victron Orion-Tr, Sterling BB) é mandatório.
> 5. **Regulador externo com sonda NTC na carcaça do alternador** é rotina em instalação séria. Limitação térmica protege o alternador em banco muito descarregado com longa navegação contínua.
> 6. **Fusível no cabo B+ ≤ 178 mm do banco, dimensionado para o cabo e com AIC compatível com a Isc do banco.** ABYC E-11 é explícita — cabo B+ sem proteção em curto é tocha.
> 7. **Ratio de polia define RPM mínimo útil.** Alternador precisa girar 4.000-6.000 RPM para entregar corrente nominal; em marcha lenta pode produzir menos de 30 % do nominal.
> 8. **Dois alternadores em paralelo não se somam magicamente.** Reguladores conflitam; bancos separados ou sincronização explícita via Wakespeed / Balmar dual-alternator setup.
> 9. **Documente: modelo, Ah gerados por hora em cruzeiro, temperatura em carga máxima, versão de firmware do regulador.** Sem essa linha base, diagnóstico futuro é chute.

> [!danger] Quando chamar um especialista
> - **Retrofit de banco AGM → lítio mantendo alternador original com regulador interno.** A arquitetura toda precisa ser repensada: regulador externo ou DC-DC charger, cabeamento, fusível com AIC compatível, comunicação com BMS, ventilação. Não é troca de peça; é reprojeto. ART/CREA obrigatório.
> - **Alternador queimado imediatamente após instalação de banco lítio.** Diagnóstico: pico indutor no momento de desconexão do BMS. Exige substituir alternador + instalar regulador externo + reavaliar todo o sistema de carga. Seguradora pode cobrir se houver projeto; não cobre "improviso".
> - **Dois alternadores em sistema bimotor ou com banco único grande.** Sincronização, divisão de carga, proteção coordenada, fusível em cada B+, alternador HO com Wakespeed dual-alternator setup. Projeto eletromecânico com responsável técnico.
> - **Motor a gasolina com alternador não marinizado** (automotivo sem ignition protection). ISO 8846 + ABYC H-24 + UL 1500 + SAE J1171 como base. Risco de ignição de vapores. Substituir por alternador marítimo com ignition protection.
> - **Superaquecimento recorrente do alternador** com casa de máquinas ventilada e correia correta. Causa pode ser banco com célula em falha puxando corrente indefinidamente, regulador travado em alta tensão, sonda NTC desconectada. Não operar até diagnóstico.
> - **Correia derretendo ou soltando repetidamente.** Desalinhamento de polia > 1 mm, tensor defeituoso, polia desgastada, correia sub-dimensionada para a potência do alternador HO. Ajuste com régua, torquímetro, catálogo do fabricante.
> - **Interferência elétrica generalizada no barco** (VHF, plotter, NMEA 2000) acompanhando RPM. Diodo retificador com falha parcial deixa AC vazar no DC. Osciloscópio confirma; substituição de ponte retificadora.
> - **Diagnóstico pós-sinistro** (incêndio em casa de máquinas, pane elétrica total após navegação). Responsável técnico com ART/CREA; preservar alternador, regulador, cabeamento, fusível para análise. Seguradora pede laudo.
> - **Eletropropulsão híbrida diesel + bancos lítio + alternador HO 300-500 A.** Domínio industrial; ISO 16315 + IEC 62619 + ABYC E-30 (draft) + especificação do fabricante como base. Projeto integrado com teste em bancada.

## O que é

O alternador é o componente eletromecânico que converte energia mecânica do motor de propulsão em corrente elétrica contínua. Apesar do nome, **internamente é um gerador AC:** produz corrente alternada trifásica no estator, que é convertida para DC por uma ponte de diodos retificadores antes de sair pelo terminal B+.

**Por que não é chamado de "dínamo":**

O dínamo (máquina DC pura, com comutador de carbonos) foi substituído pelo alternador na década de 1960. O alternador é mais eficiente, não tem desgaste por atrito de carbonos, e é mais confiável — mas o nome popular no Brasil ainda confunde os dois.

**Distinção com GERADOR DC neste material:**

A página GERADOR DC aborda o sistema completo de geração DC em navegação (alternador + regulação + cabeamento + integração). Esta página foca no componente alternador: sua construção, tipos, seleção e comportamento técnico.

## Função

Converter energia mecânica (rotação do motor) em corrente contínua para:

- Recarregar baterias de partida e de serviço durante a navegação
- Alimentar cargas DC ativas durante o cruzeiro
- Compensar consumo elétrico em tempo real para que as baterias não descarreguem durante o uso

Está ativo sempre que o motor está ligado. É a fonte de energia DC mais imediata da embarcação.

## Como aparece na prática

Em uma lancha de 28 pés com motor diesel inboard de 300HP, o alternador de 120A liga junto com o motor. Em marcha lenta gera ~50–70A. Em cruzeiro de 3.000 RPM, gera a corrente máxima até o banco atingir absorption, depois recua gradualmente.

**O problema clássico brasileiro:** banco descarregado (12 dias sem shore power, standby consumindo 3Ah/dia) + motor frio ligando na sexta-feira + alternador em máxima corrente por horas → superaquecimento → queima do alternador.

Com regulador externo (Balmar MC-614) e sonda de temperatura na carcaça do alternador, a corrente seria limitada automaticamente ao atingir ~80°C — mesmo com banco exigindo mais.

## Fundamentos mínimos

**Princípio de funcionamento (passo a passo):**

1. Correia aciona a polia do alternador → rotor gira dentro do estator
2. Tensão de excitação alimenta o enrolamento do rotor → campo magnético rotativo criado
3. Campo magnético rotativo induz tensão AC trifásica no estator (bobinas fixas)
4. Ponte retificadora (6 diodos) converte AC → DC pulsado
5. Regulador de tensão controla a corrente de excitação do rotor → tensão de saída estável em ~14,4V (12V sistema)

**RPM do alternador vs RPM do motor:**

O ratio da correia define quantas vezes o alternador gira para cada rotação do motor. Ratio típico 1:2 a 1:3 — em 2.000 RPM do motor, o alternador gira 4.000–6.000 RPM.

## Características técnicas

| Parâmetro | Valores típicos |
| --- | --- |
| Tensão nominal de saída | 14,2–14,7V (12V) / 28,4–29,4V (24V) |
| Corrente nominal | 50A / 70A / 90A / 120A / 150A / 200A |
| Potência | tensão × corrente (ex: 14,4V × 120A = 1,7kW) |
| Eficiência | 50–65% |
| Temperatura máxima carcaça | 80–100°C |
| RPM operação | 4.000–10.000 RPM (próprio) |

**Comparativo regulador interno vs externo:**

| Aspecto | Regulador Interno | Regulador Externo (Balmar/Wakespeed) |
| --- | --- | --- |
| Protocolo de carga | Fixo em 14,4V | Bulk/Absorption/Float configurável |
| Carregamento completo | ~70–80% do banco | ~95–100% |
| Proteção térmica | Não | Sim (sonda NTC no carcaça) |
| Compatível com lítio | Depende da estratégia de limitação e proteção | Muito mais favorável quando corretamente configurado |
| Custo adicional | Zero | R$800–3.000 |

**Por que regulador interno pode ser insuficiente em alguns cenários:**

Em bancos grandes, perfis cíclicos intensos ou químicas mais exigentes, o regulador interno pode não entregar a estratégia ideal de absorção, limitação térmica e coordenação com o banco. Em muitos barcos isso é aceitável; em outros, limita a recarga e acelera falhas.

## Tipos e configurações

**Por tipo de motor/embarcação (muito comum no Brasil):**

- **Motores de popa gasolina (Mercury, Yamaha, Suzuki):** alternadores automotivos de 35–75A, regulador interno, acoplamento por correia ou integrado ao volante magnético (alguns modelos 4T modernos sem correia externa)
- **Diesel inboard marinizado (Volvo Penta, Yanmar, Cummins):** Bosch, Leece-Neville ou Mitsubishi, 80–120A em 12V ou 24V. Maior robustez, marinizado de fábrica.

**Por nível de sistema (mais presente em embarcações maiores/premium):**

- **Alternador HO (High Output) com regulador externo:** Balmar 200A + MC-614. Curva de carga completa, sonda de temperatura. Para bancos AGM grandes com ciclos profundos frequentes.
- **Alternador de pólo externo + Wakespeed WS500 + lítio:** arranjo de alto nível para sistemas exigentes, com melhor controle térmico e coordenação com BMS quando suportado.

**Por número de alternadores:**

- **Um alternador:** universal em embarcações simples
- **Dois alternadores:** um para banco de partida + um HO para banco de serviço — comum em embarcações >40 pés com alta demanda
- **Bimotor com dois alternadores:** redundância total, cada alternador cuida de seu banco

## Marcas e referências

**Alternadores originais por motor (muito comum no Brasil):**

- **Mercury/MerCruiser:** Motorola/Delco, 50–75A, facilmente substituídos por automotivos
- **Yamaha:** integrado ao motor em modelos 4T modernos — substituição exige peça original
- **Volvo Penta:** Bosch ou Leece-Neville, 80–120A, 12V ou 24V
- **Yanmar:** Mitsubishi ou Hitachi, 80–100A, excelente confiabilidade
- **Cummins Marine:** Prestolite ou Leece-Neville, linha industrial robusta

**Alternadores de alta performance aftermarket (mais presente em embarcações maiores/premium):**

- **Balmar** (EUA) — série 6 (12V/24V), 100A a 200A, referência em upgrades náuticos; requer alternador de pólo externo
- **Leece-Neville** — série 4900, embarcações comerciais e iates de trabalho
- **Prestolite** — linha náutica durável, visto em motores Cummins Marine

**Reguladores externos:**

- **Balmar MC-614** — padrão náutico intermediário, AGM/GEL/Lítio (com cuidados)
- **Wakespeed WS500** — referência atual para lítio, CANBUS nativo com BMS Victron/Lithionics/REC
- **Victron Alternator Controller** — integração nativa com ecossistema Victron

## Componentes relacionados

- **Correia / tensor de correia:** transmissão mecânica — ponto de falha mais comum
- **Polia:** ratio define RPM do alternador e corrente mínima em marcha lenta
- **Ponte retificadora (6 diodos):** converte AC → DC; falha parcial gera interferência em VHF
- **Regulador de tensão (interno ou externo):** controla a excitação — "inteligência" do carregamento
- **Sonda de temperatura NTC:** proteção do carcaça com regulador externo
- **Terminal B+:** saída positiva de alta corrente — o circuito precisa de proteção coordenada com cabo, fonte e norma aplicável
- **Terminal D+ (ou FR):** sinal de excitação — ausência impede alternador de iniciar carga
- **Divisor de carga / FET isolator:** distribui corrente para bancos separados
- **BMS:** em lítio, autoriza ou bloqueia carregamento — deve comunicar com regulador externo

## Problemas mais frequentes

1. **Não carrega (luz de carga acesa no painel)** — correia solta/quebrada, fusível do B+ aberto, regulador com falha, diodo queimado, conexão B+ oxidada
2. **Superaquece e queima** — banco muito descarregado exige máxima corrente por horas + casa de máquinas quente + sem regulação de temperatura
3. **Correia solta ou quebra frequentemente** — tensão incorreta, correia envelhecida, desalinhamento de polias, ratio exigindo RPM excessivo
4. **Regulador travado no alto (>15,5V em 12V)** — bateria "borbulha", eletrólito evaporando — parar motor imediatamente
5. **Regulador travado no baixo (12,6V constante)** — banco não carrega — barco fica sem energia em navegação longa
6. **Interferência elétrica no VHF/plotter** — diodo retificador parcialmente em curto → harmônicos AC no barramento DC
7. **Queima ao usar lítio** — BMS desconecta banco com alternador em carga máxima → pico indutor destrói diodos — falha grave e cara

## Causas raiz

| Problema | Causa raiz real |
| --- | --- |
| Alternador queima com lítio | BMS desconecta banco sem aviso → campo indutor sem carga → pico de tensão > 50V destrói diodos |
| Alternador não carrega em marcha lenta | Ratio de polias exige RPM > limiar mínimo; em marcha lenta não atinge rotação suficiente |
| Correia quebrando repetidamente | Tensão incorreta OU desalinhamento de polias OU ratio exigindo RPM excessivo |
| Ruído VHF ao acelerar | Diodo retificador com falha parcial — conduz em ambas as direções, deixa AC vazar no DC |
| Banco estagna em 80% | Regulador interno "interpreta" subida rápida de tensão como banco cheio — carregamento incompleto estrutural |

## Diagnóstico prático

**Passo 1 — Tensão com motor em marcha lenta (~800–1000 RPM):**

- 13,8–14,2V: carregando normalmente
- <13,5V: fraco ou não está carregando — verificar correia e regulador
- 

    > 15,5V: regulador travado no alto → parar motor imediatamente → não ligar até reparar
    > 

**Passo 2 — Acelerando para 2.000 RPM:**

- Tensão deve chegar a 14,2–14,7V
- Se não sobe: correia deslizando ou alternador fraco

**Passo 3 — Corrente com alicate amperímetro no cabo B+:**

- Banco descarregado: deve atingir próximo ao nominal (ex: 80–90A em alternador de 90A)
- Banco cheio: deve cair para 5–15A (regulador limitando)

**Passo 4 — Temperatura após 30–45 min de navegação:**

- Com pistola térmica na carcaça
- <80°C: normal
- 80–100°C: atenção, verificar ventilação
- 

    > 100°C: crítico — reduzir carga ou parar
    > 

**Passo 5 — Interferência no VHF:**

- Canal de escuta ligado → ruído que acompanha RPM = diodo em curto parcial
- Confirmar: desligar alternador momentaneamente — se ruído some, diagnóstico confirmado

**Passo 6 — Verificação da correia:**

- Pressionar com dedo no trecho mais longo (força ~10N)
- Deflexão correta: 6–8mm
- Mais folgada: ajustar tensor
- Com rachaduras, desfazendo: trocar imediatamente

## Boas práticas profissionais

- Verificar correia e tensão dos terminais a cada 100 horas de operação ou na revisão anual
- **Nunca desconectar bateria com motor ligado** — pico de tensão destrói a ponte retificadora instantaneamente
- Avaliar cuidadosamente a estratégia de carga ao trabalhar com bancos de lítio; em muitos casos será necessário regulador externo, DC-DC charger ou limitação equivalente
- Instalar sonda de temperatura NTC no carcaça ao usar regulador externo
- Manter terminal B+ limpo e bem apertado — oxidação = resistência = calor localizado = falha do conector
- Instalar proteção do circuito B+ conforme a arquitetura, a ampacidade do cabo e a exigência normativa aplicável
- Projetar ventilação da casa de máquinas considerando o calor gerado pelo alternador em carga máxima
- Substituir correia preventivamente a cada 500h ou ao primeiro sinal de desgaste

## Cuidados de instalação

- Cabo B+ dimensionado pela corrente contínua esperada, ambiente térmico, percurso e queda de tensão admissível
- Proteção do B+ posicionada conforme o projeto e a topologia do circuito, não por hábito genérico
- Ratio de polias calculado para gerar corrente útil a partir de ~1.200 RPM do motor
- Alinhamento de polias verificado com régua — desalinhamento de 1–2mm já acelera desgaste da correia
- Regulador externo instalado longe do alternador (calor) em local ventilado
- Sonda NTC fixada no carcaça do alternador com pasta térmica (não apenas presa com fita)
- Para sistemas com dois bancos: instalar FET isolator preferível a diodo clássico (sem queda de tensão)

## Cuidados de uso

- Após longas paradas (>2 semanas), inspecionar visualmente a correia antes de ligar o motor
- Monitorar tensão de saída nos primeiros minutos após retornar de reforma ou manutenção no motor
- Em saídas longas de cruzeiro, verificar temperatura do alternador na primeira parada
- Evitar operar em máxima corrente elétrica (todas as cargas ligadas) em marcha lenta prolongada

## Erros comuns de instaladores

- **Instalar banco de lítio sem regulador externo compatível** — o erro mais perigoso e mais comum atualmente; quando o BMS desconecta, o pico de tensão queima os diodos do alternador em segundos
- **Cabo B+ sem fusível** — em curto-circuito, um cabo de 70–95mm² vira tocha antes de qualquer proteção atuar
- **Correia mal tensionada** — deslizamento gera calor na polia, carregamento inconsistente, desgaste acelerado
- **Usar alternador automotivo genérico** em ambiente marinho sem proteção adequada — falha precoce por corrosão
- **Não separar banco de partida do banco de serviço** — banco de serviço descarregado deixa motor sem partida
- **Conectar B+ direto no banco de serviço** sem isolador — banco de partida pode descarregar para serviço à noite pelos consumos

## Relação com outros sistemas

- **Motor de propulsão:** fonte mecânica — RPM e carga do motor definem a produção DC
- **Banco de Baterias:** receptor da corrente gerada — estado de carga define a corrente exigida
- **Divisor de Carga / FET Isolator:** distribui corrente gerada entre banco de partida e banco de serviço
- **BMS (lítio):** pode limitar ou bloquear o carregamento via alternador — a forma correta de integração depende do sistema
- **Regulador Externo (Balmar/Wakespeed):** inteligência do carregamento — sem ele, o alternador opera em modo primitivo
- **Monitor de Bateria (BMV/SmartShunt):** exibe corrente gerada em tempo real — principal ferramenta de diagnóstico remoto
- **Painel Solar + MPPT:** fonte DC complementar — trabalham juntos carregando o mesmo banco
- **Shore Power + Carregador:** fonte alternativa em porto — o alternador serve apenas quando em navegação

## Brasil x Internacional

| Aspecto | Brasil | Internacional (ABYC/Europa) |
| --- | --- | --- |
| Alternadores comuns | Automotivos 50–90A, regulador interno | Náuticos HO 100–200A com regulador externo |
| Fusível no cabo B+ | Frequentemente ausente | Obrigatório por ABYC E-11 (2023) |
| Uso com lítio | Crescendo — muitos erros de instalação | Bem estabelecido (Wakespeed + BMS) |
| Reguladores externos | Raros, exceto instalações premium | Comuns em barcos >35 pés |
| Manutenção preventiva | Reativa | Programada por horas de uso |
| Marinização | Frequentemente automotivo adaptado | Marinizado de fábrica com proteção IP e vedação |

**Ponto crítico no Brasil:** a transição para bancos de lítio está acelerada no mercado brasileiro (2023–2025), mas a maioria das instalações ainda não usa regulador externo compatível. Isso está gerando um volume crescente de queimas de alternadores — problema real de campo.

## Glossário rápido

- **Alternador** — máquina eletromecânica que converte energia mecânica do motor em corrente contínua (internamente gera AC trifásico retificado).
- **Gerador DC / dínamo** — máquina DC pura com comutador de carbonos; obsoleta, substituída pelo alternador na década de 1960.
- **Rotor** — parte girante que recebe corrente de excitação e cria o campo magnético.
- **Estator** — parte fixa com enrolamentos trifásicos onde é induzida a tensão AC.
- **Ponte retificadora (6 diodos)** — converte AC trifásico em DC pulsado na saída B+.
- **Regulador de tensão** — controla a excitação do rotor para manter tensão de saída estável.
- **Regulador interno** — integrado ao alternador; curva fixa (~14,4 V), sem compensação.
- **Regulador externo programável** — Balmar MC-614, Wakespeed WS500, Victron Alternator Controller; bulk/absorção/float configurável, sonda térmica.
- **Terminal B+** — saída positiva de alta corrente; vai ao banco via fusível.
- **Terminal D+ / FR / I** — sinal de excitação; sem ele, alternador não inicia carga (lâmpada "bateria" apaga).
- **Terminal W / STA** — sinal de rotação para tacômetro do motor.
- **Terminal L / IG** — alimentação do regulador via chave de ignição.
- **Correia / belt** — transmissão mecânica entre motor e alternador. Trapezoidal clássica ou poly-V moderna.
- **Polia / pulley** — define ratio de rotação alternador/motor; ratio típico 1:2-1:3.
- **Tensor / idler pulley** — mantém tensão correta na correia; automático em motores modernos.
- **Correia poly-V / serpentina** — multi-nervuras em V; padrão em motores modernos HP.
- **Ratio de polias** — proporção entre diâmetros; define RPM do alternador vs motor.
- **RPM útil mínimo** — rotação abaixo da qual o alternador não entrega corrente significativa.
- **Corrente nominal (A)** — corrente máxima contínua em cruzeiro (ex: 90 A, 120 A, 200 A).
- **HO (High Output)** — alternador aftermarket com corrente nominal elevada (Balmar 200 A+).
- **Alternador de pólo externo** — estator ligado externamente, permite regulador externo comandar excitação.
- **Marinização** — adaptação para ambiente marinho: proteção contra umidade, salinidade, ignição de gases.
- **Ignition protection (IP marine)** — certificação SAE J1171 / UL 1500 / ISO 8846 para não gerar faísca em vapores de combustível.
- **Curva de carga** — perfil de tensão/corrente ao longo do tempo de carga.
- **Bulk / absorção / float** — três estágios: corrente máxima, tensão constante, manutenção.
- **Sonda NTC / termistor** — sensor de temperatura na carcaça do alternador, conectado ao regulador externo.
- **Proteção térmica** — redução automática da corrente ao atingir temperatura limite (~80-100 °C).
- **Pico indutor (load dump)** — pico de tensão gerado quando o banco é desconectado com alternador em carga; pode ultrapassar 50 V.
- **Load dump transient** — padrão ISO 16750-2 / ISO 7637-2 que descreve este pico.
- **TVS diode (Transient Voltage Suppressor)** — diodo de supressão que protege eletrônicos contra load dump.
- **Divisor de carga** — diodo tradicional com queda de 0,6-1,0 V; divide corrente entre bancos.
- **FET isolator / ACR (Automatic Charging Relay)** — alternativa moderna sem queda de tensão.
- **VSR (Voltage Sensitive Relay)** — relé que fecha quando tensão ultrapassa limiar; divide bancos por proximidade.
- **DC-DC charger (B2B)** — conversor isolado que carrega banco de serviço a partir do banco de partida ou do alternador.
- **BMS (Battery Management System)** — em banco lítio, pode desconectar banco e expor alternador ao load dump.
- **NMEA 2000 / VE.Can / CAN bus** — protocolos de comunicação entre regulador externo moderno e BMS.
- **Field current** — corrente de excitação do rotor; controlada pelo regulador.
- **Excitation voltage** — tensão aplicada ao rotor para criar campo.
- **Tensão de absorção** — alvo do bulk/CV; 14,2-14,7 V chumbo, 14,2-14,6 V lítio em 12 V.
- **Tensão de float** — manutenção; 13,2-13,8 V chumbo; LFP pode dispensar float contínuo.
- **Amp-hour output** — Ah entregues por hora em condição de cruzeiro; base de dimensionamento.
- **Duty cycle** — percentual do tempo em máxima corrente; alternador aguenta se ventilado.
- **Slip ring / escovas de carbono** — contatos móveis entre campo fixo e rotor; desgaste comum.
- **Bearing (rolamento)** — mecânico; ruído metálico indica substituição iminente.

## Normas e referências técnicas

- **ABYC E-11 (2023)** — AC and DC Electrical Systems on Boats: fusível no cabo B+ ≤ 178 mm, bitolagem, proteção de cabeamento, separação de bancos.
- **ABYC E-13 (2023)** — Lithium Ion Batteries: interface alternador-BMS, requisitos de proteção contra load dump.
- **ABYC E-10 (2023)** — Storage Batteries: separação de bancos (start/house), ventilação, proteção.
- **ABYC H-25 (2023)** — Power feeds for engine-mounted accessories: cabeamento e proteção de circuitos do motor.
- **ISO 13297:2020** — Electrical systems on recreational craft AC e DC.
- **ISO 8846:2022** — Protection against ignition of surrounding flammable gases: ignition protection obrigatório em motor a gasolina.
- **SAE J1171** — Marine ignition protection for alternators and starters: requisito americano para alternador em motor a gasolina.
- **UL 1500** — Ignition-protected marine products: certificação equivalente.
- **ISO 16750-2 / ISO 7637-2** — Environmental conditions for electrical/electronic equipment: caracterização de load dump.
- **NMEA 2000 (IEC 61162-3)** — Comunicação de rede marítima; regulador externo moderno publica PGNs de carga.
- **ABNT NBR 5410 (2004 + emendas)** — Base brasileira para baixa tensão; aplicável ao circuito DC do barramento.
- **NORMAM-211/DPC** — Embarcações de esporte e recreio: exigências administrativas e de segurança brasileiras.
- **Compatibilidade com lítio** — não coberta explicitamente por normas antigas; é engenharia de sistema. Fabricantes de BMS (Victron, REC, Lithionics, Battle Born) e de regulador (Balmar, Wakespeed, Victron) publicam guias de instalação que integram os requisitos das normas acima.

## Como ensinar este tópico

**Progressão recomendada:**

1. Analogia: "alternador do carro" — mesma física, diferente contexto
2. Abrir um alternador queimado: identificar visualmente rotor, estator, ponte de diodos, regulador
3. Diagrama interno: motor → correia → rotor → campo → estator → AC trifásico → diodos → DC
4. Exercício: medir tensão e corrente em marcha lenta e em cruzeiro — ver diferença
5. Comparar: regulador interno (curva plana) vs externo (bulk/absorption/float) — gráfico de tensão × tempo
6. Caso de falha: "por que o alternador queimou quando instalaram lítio?" — explicar o pico sem carga

## Ideias de vídeos e aulas práticas

- **"Como funciona o alternador por dentro"** — desmontagem de alternador queimado, componentes identificados
- **"Diagnóstico de alternador com multímetro: 5 testes em 10 minutos"** — passo a passo de campo
- **"Lítio + alternador: o erro que destrói os dois"** — demonstração do pico de tensão com osciloscópio
- **"Regulador externo Wakespeed WS500: instalação e configuração"** — tutorial completo
- **"Por que meu banco nunca carrega 100% em navegação?"** — regulador interno vs externo explicado visualmente

## Diagramas sugeridos

- **Corte interno do alternador:** rotor, estator, ponte de diodos, regulador — com identificação de cada componente
- **Diagrama de blocos do sistema:** motor → correia → alternador → regulador → banco → divisor → banco de serviço
- **Circuito de proteção com lítio:** alternador (pólo externo) → Wakespeed WS500 → banco LFP → BMS → CANBUS
- **Gráfico de carregamento:** tensão × tempo com regulador interno (linha plana) vs externo (bulk/absorption/float)
- **Diagrama de temperatura:** fluxo de calor no alternador — rotor → estator → carcaça → dissipação

## FAQ

**O alternador do carro funciona no barco?**

Funciona em sistemas simples com chumbo-ácido, mas não é marinizado (sem proteção contra umidade, vibração e maresia). Vida útil reduzida. Incompatível com lítio sem regulador externo. Aceitável em emergência ou embarcações simples; não recomendado para instalação permanente.

**Posso usar dois alternadores em paralelo?**

Não diretamente — reguladores conflitam entre si. Dois alternadores devem alimentar bancos separados via divisor, ou ter reguladores sincronizados. Paralelo direto sem sincronização causa oscilação e falha prematura.

**Por que o alternador não carrega em marcha lenta?**

O ratio das polias pode exigir mais RPM do motor para o alternador atingir velocidade de produção útil. Solução: reduzir diâmetro da polia do alternador (aumenta RPM relativo) ou alternador HO com maior produção em baixa rotação.

**Quanto tempo para recarregar com alternador de 90A?**

Banco 200Ah a 50% (100Ah a repor): teoricamente 1,1h com 90A. Na prática, 2–3h porque a corrente cai na fase de absorção. Com lítio: mais rápido (aceita 100% da corrente até ~95% de carga).

**O alternador pode alimentar diretamente equipamentos AC?**

Não. O alternador produz DC. Para alimentar cargas AC (220V), é necessário um inversor DC→AC.

## Integração com outras notas

- [[Bancos de Bateria]]
- [[BMS — Battery Management System]]
- [[Arranque]]
- [[CAIS (Pier) (AC)]]
- [[Carregador Elétrico para Tender e Jet Ski]]
- [[Eólico (DC)]]
- [[Gerador (AC)]]
- [[Gerador (DC)]]
- [[Inversora (DC To AC)]]
- [[Lítio LiFePO4 — Instalação e Cuidados Específicos]]
- [[Placa Solar (DC)]]

## Perguntas que esta nota responde

- O que é Alternador (DC) em instalações elétricas náuticas?
- Qual é a função de Alternador (DC) na embarcação?
