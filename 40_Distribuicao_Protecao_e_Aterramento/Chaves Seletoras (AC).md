---
title: "Chaves Seletoras (AC)"
note_type: "technical-note"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "CHAVES SELETORAS (AC) 2c919734f7fb83078ff601354dc25bca.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "59"
tier_fase_6: "A"
reviewed_on: "2026-04-21"
review_jurisdiction:
  - "Brasil"
  - "internacional"
review_level: "engineering-curated"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
  - "https://www.ul.com/services/ul-1008"
normas_citadas:
  - "ABYC E-11 (AC and DC Electrical Systems on Boats) — §11.7 entradas AC, §11.8 transfer switches, §11.10 paralelismo"
  - "ABYC A-31 (Battery Chargers and Inverters) — lógica de transferência interna"
  - "ABYC E-10 (Storage Batteries)"
  - "ISO 13297:2020 (Small craft — Electrical systems — AC installations) — §8 transferência de fonte"
  - "ISO 10133:2012 (Small craft — Electrical systems — Extra-low-voltage DC)"
  - "ISO 8846:1990 (Ignition protection)"
  - "IEC 60947-6-1 (Multiple function equipment — Automatic transfer switching equipment — ATSE)"
  - "IEC 60947-3 (Switches, disconnectors, switch-disconnectors) — intertravamento"
  - "IEC 60364-5-53 (Selection and erection — Isolation, switching and control)"
  - "IEC 61008/61009 (RCCB/RCBO — proteção diferencial)"
  - "IEC 60529 (IP Code)"
  - "IEC 60092-301 (Electrical installations in ships — Equipment — Generators and motors)"
  - "IEC 60092-401 (Installation and test of completed installation)"
  - "UL 1008 (Transfer Switch Equipment)"
  - "UL 508 (Industrial Control Equipment)"
  - "UL 1741 (Inverters, Converters, Controllers — Supply-side interconnection)"
  - "NFPA 70 (NEC) — art. 230.82 (disconnecting means — utility interconnection), art. 445 (geradores), art. 555 (marinas), art. 700 (emergency), art. 702 (optional standby)"
  - "NFPA 110 (Emergency and Standby Power Systems)"
  - "ABNT NBR 5410 (Instalações elétricas de baixa tensão) — §5.3 proteção, §5.7 seccionamento"
  - "ABNT NBR IEC 60947-6-1 (Equipamento de transferência automática)"
  - "ABNT NBR IEC 61008/61009 (DR)"
  - "NORMAM-05/DPC (Embarcações de esporte e recreio)"
  - "NORMAM-01/DPC (Embarcações em navegação marítima)"
  - "USCG 33 CFR 183.340 (Inlets of ventilation systems — shore power)"
  - "USCG 46 CFR 111.105 (Hazardous locations)"
  - "DNV-RU-SHIP Pt.4 Ch.8 §4 (Distribution systems)"
  - "ABS Rules for Building and Classing Steel Vessels — Part 4 Ch.8"
  - "IEEE 446 (Recommended Practice for Emergency and Standby Power Systems)"
family_clusters:
  - "ABYC-USCG (EUA)"
  - "ISO-IEC (internacional)"
  - "ABNT-NORMAM (Brasil)"
  - "UL-NFPA (EUA industrial)"
aliases:
  - "CHAVES SELETORAS (AC)"
  - "Transfer switch"
  - "ATS"
  - "Chave de transferência AC"
seo_title: "Chaves Seletoras (AC)"
seo_description: "CHAVES SELETORAS AC — Dispositivos de transferencia e selecao de fonte para shore power, gerador e inversor, com foco em intertravamento, topologia de neutro e seguranca da comutacao."
seo_keywords:
  - "Chave seletora AC"
  - "Transfer switch"
  - "Selecao de fonte"
  - "40 Distribuicao Protecao e Aterramento"
geo_queries:
  - "Como especificar chave seletora AC em embarcacao?"
  - "Como funciona a transferencia entre shore power, gerador e inversor?"
  - "Qual a diferenca entre break-before-make e make-before-break?"
related_notes:
  - "CAIS (Pier) (AC)"
  - "Gerador (AC)"
  - "Inversora (DC To AC)"
  - "Proteção Dr"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
  - "Transformador Entrada"
---

# Chaves Seletoras (AC)

> [!abstract] Resumo técnico
> Chave seletora AC, manual ou automática, é o elemento que escolhe qual fonte de corrente alternada alimenta o sistema da embarcação. Sua função crítica é impedir paralelismo indevido entre fontes não sincronizadas e preservar a coerência elétrica entre shore power, gerador, inversor e o painel AC. ABYC E-11.8 e ISO 13297 §8 exigem intertravamento físico ou elétrico entre fontes, tratamento correto de neutro/PE por topologia, e documentação de operação — paralelismo em embarcação de recreio sem sincronização é causa comum de incêndio em cais.

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **Break-before-make é o padrão** em recreio sem sincronização — a fonte anterior deve abrir antes da nova fechar; paralelismo momentâneo queima inversor/gerador em milissegundos.
> 2. **Intertravamento físico ou elétrico obrigatório** — não dependa do "operador lembrar"; use ATS, disjuntores intertravados mecanicamente ou inversor multiplus com lógica interna.
> 3. **Neutro e PE mudam por fonte** — shore power traz PE do cais; gerador tem PE gerado a bordo; inversor pode ter ground relay interno. Transferência errada cria loop de neutro + PE = ruído + corrente parasita pelo casco.
> 4. **Corrente de transferência ≥ 1,25× da corrente nominal** do sistema AC de bordo; capacidade de interrupção coordenada com proteção principal (Icu ≥ Icc presumida do cais).
> 5. **Tempo de transferência importa para cargas sensíveis** — eletrônica digital aceita 50-200 ms; motores de refrigeração/bombas pedem < 30 ms ou anti-short-cycle timer (> 3 min).
> 6. **ATS automático com temporização** — retardo de 10-30 s para partida do gerador evita "ligar-desligar" em flicker da rede; retardo de retorno (retransfer) de 5-15 min após estabilização da shore power.
> 7. **UL 1008 (EUA) ou IEC 60947-6-1 (internacional)** são os dois padrões principais para ATS certificado — não improvise com disjuntores comuns.
> 8. **Inversor multiplus (Victron, Mastervolt, Magnum, Xantrex)** já integra transfer switch interno (normalmente 30-50 A, 16-32 ms) — em sistemas > 50 A ou múltiplas fontes, ATS externo ainda é necessário.
> 9. **Documente cada posição** ("CAIS", "GERADOR", "INVERSOR", "OFF") com etiqueta permanente — retirar decalque colado com tempo cria ambiguidade perigosa.

> [!danger] Quando chamar um especialista
> Estes 9 cenários exigem engenheiro elétrico náutico ou certificador:
> 1. **Sistema paralelo permanente entre gerador e shore power** (paralel load sharing) — exige sincronizador de fase, relé de proteção 25/27/59/81, e esquema de proteção anti-islanding conforme UL 1741 ou IEC 61727.
> 2. **Embarcação com dois ou mais geradores em paralelo** — load share, anti-hunting, kW/kVAr balance; só integrador ou classificadora certifica.
> 3. **Shore power split-phase 240 V (EUA) ou trifásico 220/380 V** — neutro ausente em L-L, bonding do cais vs. bonding do barco, isolador galvânico, risco de ESD (electric shock drowning) em marina sem GFCI.
> 4. **Retrofit de inversor grid-tie (solar ou híbrido)** alimentando rede pública — anti-islanding UL 1741-SA / IEEE 1547 obrigatório; nunca liga em marina sem autorização do operador do cais.
> 5. **Navio comercial sob classificadora** — ATS IEC 60092-301/401 certificado, com classe DNV/Lloyd's/BV/ABS; transfer switch de uso terrestre não é aceito.
> 6. **Sistema CA 480 V ou trifásico industrial em embarcação grande** — estudo de curto-circuito, coordenação de proteção, análise de arc flash (NFPA 70E ou IEC 61641).
> 7. **Transferência com tempo < 16 ms (UPS-grade)** para carga crítica (hospital ship, yacht com servidor de automação) — exige bateria/capacitor ride-through e solid-state transfer switch.
> 8. **Marina com problema de corrente de fuga ou ESD histórico** — investigação eletrotécnica: pode exigir isolador galvânico, isolation transformer, ou intervenção na arquitetura de bonding da embarcação.
> 9. **Certificação CE/RCD, ABYC Certified Technician ou USCG inspection** — dossiê com diagrama unifilar, memorial de topologia de neutro, teste de intertravamento e verificação de proteção diferencial.

## O que é

É o dispositivo de transferência ou seleção de fonte entre:

- **energia de cais (shore power)** — 120/240 V @ 60 Hz (EUA, Caribe) ou 230 V @ 50 Hz (UE, Brasil);
- **gerador de bordo** — motor-gerador diesel/gasolina;
- **inversor/carregador** — converte DC (bateria) em AC;
- eventualmente **outras entradas AC** previstas no projeto (segundo cais, segundo gerador, doca seca).

Nem toda solução é uma "chave giratória simples". Dependendo da arquitetura, a seleção pode ocorrer por:

- **chave manual rotativa** (simples, barata, exige operador atento);
- **disjuntores intertravados mecanicamente** (interlock kit);
- **ATS externo** (Automatic Transfer Switch — lógica eletromecânica ou eletrônica);
- **lógica interna de inversor/carregador** (Victron Multiplus, Mastervolt Mass Combi, Magnum MS-PAE, Xantrex Freedom XC);
- **STS — Static Transfer Switch** (solid-state, < 4 ms, UPS-grade).

## Função na embarcação

- impedir que duas fontes incompatíveis alimentem o mesmo barramento simultaneamente (causa de incêndio);
- organizar a prioridade entre fontes (tipicamente: shore > gerador > inversor);
- permitir comutação controlada entre energia externa, geração local e inversão;
- sustentar segurança operacional e integridade dos equipamentos;
- preservar coerência de neutro/PE conforme a fonte ativa;
- proteger contra backfeed (energia de dentro do barco indo para o cabo do cais).

## Fundamentos mínimos

### Fonte AC não pode ser tratada como se fosse apenas "mais uma tomada"

Shore power, gerador e inversor têm comportamentos diferentes de tensão, frequência, neutro e aterramento. A comutação precisa preservar essa topologia:

- **Shore power**: PE e neutro já interligados no cais (sistema TN-C-S ou TN-S); o barco não deve criar segunda ligação;
- **Gerador**: PE criado a bordo (bonding), neutro gerado pelo enrolamento; relé de neutro-terra (N-G bonding switch) fecha apenas quando o gerador é a fonte;
- **Inversor**: pode ter ground relay interno que cria ligação N-G apenas em modo "invert" e abre em modo "pass-through".

### Paralelismo entre fontes não é manobra trivial

Duas fontes AC só podem operar em paralelo quando o sistema foi projetado para sincronização e compartilhamento:

- **relé de sincronismo (25)** compara tensão, frequência e ângulo de fase;
- **relés de proteção (27/59/81)** monitoram sub/sobretensão e sub/sobrefrequência;
- **anti-islanding** para inversor grid-tie.

Fora desse cenário, a regra é **seleção exclusiva com intertravamento**.

### Break-before-make é a lógica mais comum

Na maior parte das embarcações de recreio, a chave ou o sistema de transferência deve abrir uma fonte antes de fechar a outra. Isso evita:

- **backfeed** (energia do gerador/inversor voltando pelo cabo do cais → risco ao trabalhador da marina);
- **paralelismo indevido** (curto se fontes não sincronizadas);
- **loop de neutro** (N-G bonding duplicado);
- **arco de comutação** (capacitores de filtros descarregando).

Transferência típica: 16-200 ms; em sistemas UPS-grade solid-state: < 4 ms (raro em recreio).

### Neutro e PE exigem leitura arquitetural

A forma como neutro e proteção se relacionam depende da topologia da fonte selecionada e da arquitetura do barco. Uma chave seletora fisicamente simples pode induzir erro sério se a topologia de neutro não for entendida:

- **ABYC E-11.5.3** exige que o neutro de cada fonte seja chaveado junto com a fase no transfer switch (2-pole ou 3-pole conforme tensão);
- **Ground relay (N-G bonding switch)** deve fechar APENAS quando a fonte é gerador ou inversor em modo "invert"; em shore power deve abrir para evitar duplicação da ligação N-G do cais;
- **Isolation transformer** ou **isolador galvânico** quebram a ligação PE entre cais e barco para evitar corrente de fuga pelo casco (ABYC E-11.11).

## Tipos e arquiteturas comuns

### Chave manual rotativa (simples)

- 2 ou 3 posições: CAIS / OFF / GERADOR;
- baixo custo, dependente de operador atento;
- usada em embarcação de recreio pequena (< 50 A);
- exemplos: Blue Sea ML-series, Marinco Transfer Switch 30/50 A.

### Disjuntores intertravados (interlock kit)

- 2 disjuntores com kit mecânico que impede fechar ambos simultaneamente;
- aceito por NFPA 70 (NEC) como alternativa a ATS em sistemas simples;
- típico em embarcação média com shore + gerador;
- exemplos: Eaton BRN interlock, Square D Homeline interlock.

### ATS externo eletromecânico

- contatores em break-before-make com lógica de temporização;
- entrada para sensor de "shore available" e "generator ready";
- padrão UL 1008 (EUA) ou IEC 60947-6-1 (internacional);
- exemplos: ASCO 300/400, Kohler RXT, Onan RSS, Generac.

### ATS integrado em inversor multiplus

- transfer switch interno de 30-50 A (Victron Multiplus), 50-100 A (Magnum MS-PAE), até 200 A (Mastervolt Mass Combi XL);
- modos: pass-through (shore/gerador passa direto), charge, invert, power assist (somar inversor + shore);
- tempo de transferência típico 16-32 ms;
- exemplos: Victron Multiplus-II, Mastervolt Mass Combi Ultra, Magnum MS-PAE, Xantrex Freedom XC Pro.

### STS (Static Transfer Switch — solid-state)

- SCR/IGBT com comutação em < 4 ms;
- usado em UPS-grade (yacht com automação, hospital ship);
- alto custo; exemplos: ASCO 7000, Eaton PowerSwitch STS.

## Dimensionamento — tabela de referência

| Sistema AC | Corrente nominal | Fontes | Solução típica | Tempo transfer |
| --- | --- | --- | --- | --- |
| Single-phase 120 V 30 A | 30 A | shore + gerador | interlock manual ou ATS simples | 50-200 ms |
| Single-phase 120 V 50 A | 50 A | shore + gerador + inversor | inversor multiplus (Victron, Mastervolt) | 16-32 ms |
| Split-phase 120/240 V 50 A | 50 A (L-L) | shore + gerador | ATS UL 1008 2-pole | 50-200 ms |
| Split-phase 240 V 100 A | 100 A | shore + gerador grande | ATS automotive ASCO/Kohler | 200 ms |
| Single-phase 230 V 32 A (UE/BR) | 32 A | shore + gerador | ATS IEC 60947-6-1 | 50-200 ms |
| Single-phase 230 V 63 A | 63 A | shore + gerador + inversor | inversor multiplus 5 kVA | 20 ms |
| Trifásico 400 V até 125 A | até 125 A | shore + gerador trifásico | ATS IEC 3-pole | 50-200 ms |
| Trifásico > 125 A | > 125 A | shore + múltiplos geradores | projeto dedicado com sincronismo | varia |

## Projeto e instalação

### O que precisa ser definido

1. **quais fontes existem** e em que ordem de prioridade;
2. **se a comutação será manual, automática ou híbrida**;
3. **como neutro, PE e proteção diferencial se comportam** em cada fonte (diagrama unifilar obrigatório);
4. **qual é a corrente máxima** do sistema (com margem ≥ 25%);
5. **quais cargas podem tolerar a interrupção** de transferência (eletrônica digital, motores, refrigeração);
6. **como a operação será documentada** para o usuário e para manutenção;
7. **tempo máximo aceitável de interrupção** (16 ms UPS-grade / 30 ms cargas críticas / 200 ms geral);
8. **capacidade de interrupção** do ATS (Icu ≥ Icc presumida da shore power + gerador);
9. **sinalização e alarmes** (LED indicando fonte ativa, alarme sonoro de falha de transferência).

### Diretrizes práticas

- prever intertravamento real entre fontes (físico OU elétrico — nunca apenas "procedimento");
- identificar claramente entradas e saída (etiqueta gravada + diagrama unifilar ao lado do painel);
- não confiar em "memória do operador" como barreira de segurança;
- integrar a lógica de transferência com o painel AC e a proteção diferencial (DR/RCD conforme fonte);
- evitar gambiarras com tomadas, plugues e backfeed improvisado;
- instalar sinalização visual (LED) em cada posição da chave;
- testar funcionalmente a transferência a cada inspeção anual (ABYC A-31);
- manter memorial de topologia de neutro atualizado após qualquer retrofit.

## Onde costuma dar problema

| Problema | Causa provável | Correção |
| --- | --- | --- |
| fonte errada energizando o barramento | chave mal operada ou arquitetura confusa | redesenhar etiquetagem, treinar operador, adicionar sinalização visual |
| comutação falha ou intermitente | componente degradado, tensão fora da janela ou lógica ruim | substituir ATS, verificar sensor de presença de fonte, calibrar temporização |
| disparos ou comportamento estranho após troca de fonte | topologia de neutro/PE mal tratada | revisar bonding N-G por fonte; instalar isolador galvânico se necessário |
| dano em inversor, gerador ou entrada de cais | paralelismo indevido ou backfeed | substituir chave por ATS com intertravamento verificado |
| usuário não sabe qual fonte está ativa | painel e chave mal identificados | painel com LEDs por fonte, etiqueta permanente, checklist pré-operação |
| carga crítica reinicia em cada transferência | tempo de transferência > tempo de ride-through da carga | upgrade para STS solid-state ou UPS dedicada para essa carga |
| gerador "flerta" com shore intermitente | temporização de retransfer curta demais | aumentar retardo de retorno para 5-15 min |

## Diagnóstico prático

1. **Confirmar qual fonte deveria estar alimentando** o sistema (check de painel × diagrama).
2. **Verificar a posição ou o estado** do sistema de transferência (LED indicador, posição da chave).
3. **Medir presença de tensão** na entrada e na saída da seletora (multímetro AC, ponto a ponto).
4. **Conferir se a topologia elétrica** prevista para a fonte ativa está coerente com o restante do sistema (teste de continuidade N-G em shore vs. gerador).
5. **Em ATS ou lógica automática**, validar critérios de detecção, temporização e prioridade (check de parâmetros).
6. **Testar proteção diferencial** (DR/RCD) sob cada fonte — botão de teste deve disparar em < 40 ms.
7. **Inspecionar contatos** do ATS após operação intensiva (soldagem, pitting, oxidação).
8. **Medir tempo real de transferência** com osciloscópio se disponível (datasheet × realidade).

## Boas práticas profissionais

- usar transferência com intertravamento inequívoco (físico ou elétrico);
- documentar operação normal e operação de contingência (procedimento impresso no painel);
- tratar neutro, PE e DR em conjunto com a chave seletora (diagrama unifilar + memorial);
- prever manutenção e teste funcional do sistema de transferência (anual);
- desenhar a operação para minimizar erro humano (LEDs, etiquetas, checklist);
- em marina com histórico de ESD ou corrente de fuga, instalar isolador galvânico ou isolation transformer;
- manter contatos do ATS limpos e apertados (inspeção a cada 500 h ou anual);
- substituir preventivamente ATS a cada 10-15 anos em uso frequente;
- em embarcação comercial, considerar redundância N+1 (dois ATS em paralelo com interlock);
- treinar tripulação em procedimento de shore power → gerador em caso de queda da shore.

## Erros comuns

- assumir que qualquer chave "serve" para transferir fontes AC;
- ligar duas fontes no mesmo barramento sem estratégia de sincronização;
- ignorar implicações de neutro e aterramento ao trocar a fonte;
- deixar a transferência dependente de procedimento informal não documentado;
- achar que inversor com relé interno resolve sozinho uma arquitetura mal pensada;
- usar interlock de kit terrestre em embarcação sem verificar classificação marine;
- deixar backfeed "temporário" de gerador no cabo de cais (mortalmente perigoso para eletricista do cais);
- dimensionar ATS pela corrente média e não pelo pico (partida de compressor);
- ignorar temporização mínima entre transferências (anti-short-cycle para motores);
- conectar inversor grid-tie em marina sem autorização (anti-islanding obrigatório).

## Relação com outros sistemas

- **[[CAIS (Pier) (AC)]]** — fonte externa frequentemente priorizada.
- **[[Gerador (AC)]]** — fonte local com comportamento próprio.
- **[[Inversora (DC To AC)]]** — fonte alternativa e, muitas vezes, elemento de transferência.
- **[[Proteção Dr]]** — coerência da proteção diferencial conforme a fonte ativa.
- **[[Quadro Elétrico e Painel de Distribuição AC-DC]]** — ponto de distribuição a jusante.
- **[[Transformador Entrada]]** — influencia a topologia de entrada AC.
- **[[Chaves Gerais (DC)]]** — análogo em DC.

## Normas e referências

### Por família e jurisdição

| Família | Norma | Escopo |
| --- | --- | --- |
| **ABYC (EUA)** | E-11 §7, §8, §10 | entradas AC, transfer switches, paralelismo |
| ABYC | A-31 | inversores/carregadores com transferência interna |
| **USCG (EUA)** | 33 CFR 183.340 | entradas shore power |
| USCG | 46 CFR 111.105 | áreas classificadas |
| **UL (EUA)** | UL 1008 | Transfer Switch Equipment |
| UL | UL 508 | equipamento de controle industrial |
| UL | UL 1741 / UL 1741-SA | inversores grid-tie com anti-islanding |
| **NFPA (EUA)** | NFPA 70 art. 230.82 | disconnecting means |
| NFPA | NFPA 70 art. 445/555/700/702 | geradores / marinas / emergency / standby |
| NFPA | NFPA 110 | sistemas emergência/standby |
| **IEEE (EUA)** | IEEE 446 | práticas recomendadas para emergency/standby |
| **ISO (internacional)** | ISO 13297:2020 §8 | transferência de fonte AC em pequenas embarcações |
| ISO | ISO 10133:2012 | sistemas DC (referência cruzada) |
| **IEC (internacional)** | IEC 60947-6-1 | ATSE — Automatic Transfer Switching Equipment |
| IEC | IEC 60947-3 | intertravamento de switches |
| IEC | IEC 60364-5-53 | isolamento, chaveamento e controle |
| IEC | IEC 61008/61009 | DR (RCCB/RCBO) |
| IEC | IEC 60092-301/401 | instalações elétricas em navios |
| **ABNT (Brasil)** | NBR 5410 §5.3 / §5.7 | proteção e seccionamento |
| ABNT | NBR IEC 60947-6-1 | equipamento de transferência |
| ABNT | NBR IEC 61008/61009 | DR |
| **NORMAM (Brasil)** | NORMAM-05/DPC | embarcações de recreio |
| NORMAM | NORMAM-01/DPC | navegação marítima |
| **Classificadoras** | DNV-RU-SHIP Pt.4 Ch.8 §4 | sistemas de distribuição em navios |
| Classificadoras | ABS / Lloyd's / BV / RINA | regras de classe |

### Comparação prática entre jurisdições

- **EUA (ABYC + NEC + UL 1008)**: foco em intertravamento físico, chaveamento de neutro junto com fase (2-pole ou 3-pole por tensão), NFPA 110 para emergency/standby.
- **Internacional (ISO + IEC 60947-6-1)**: abordagem por ATSE classificado (PC/CB), tempos de transferência especificados (te ≤ 100 ms, to ≤ 50 ms tipicamente).
- **Brasil (ABNT + NORMAM)**: NBR 5410 predial aplica-se parcialmente; NORMAM-05 remete a ABYC/ISO; falta regulamento ABNT específico para transferência náutica.
- **Navio classificado**: IEC 60092-301/401 obrigatório; ATS de uso terrestre não é aceito sem certificação de classe.

## Glossário rápido

1. **Anti-islanding** — proteção que desliga inversor grid-tie ao detectar queda da rede pública (UL 1741 / IEEE 1547).
2. **Anti-short-cycle timer** — temporizador que impede religar motor/compressor antes de 3-5 min após corte.
3. **ATS (Automatic Transfer Switch)** — chave de transferência automática entre fontes AC.
4. **ATSE (Automatic Transfer Switching Equipment)** — terminologia IEC 60947-6-1 para ATS.
5. **Backfeed** — energia do barco retornando pelo cabo do cais (perigoso).
6. **Bonding N-G (neutral-ground)** — ligação intencional entre neutro e terra em fonte standalone (gerador/inversor).
7. **Break-before-make (BBM)** — lógica em que fonte anterior abre antes da nova fechar — padrão seguro.
8. **Bypass** — caminho alternativo que contorna o ATS para manutenção.
9. **Cloud power (em marina moderna)** — shore power gerenciado digitalmente.
10. **Contactor** — chave comandada eletricamente (bobina interna).
11. **CTTS (Closed Transition Transfer Switch)** — transfere com breve paralelismo (< 100 ms) — exige sincronismo.
12. **DR (Dispositivo Residual) / RCD / GFCI** — proteção diferencial (disparo 30 mA em 40 ms).
13. **ESD (Electric Shock Drowning)** — afogamento por choque em marina por corrente de fuga na água.
14. **Flicker** — variação rápida de tensão da rede.
15. **GFCI (Ground Fault Circuit Interrupter)** — DR americano; 5 mA pessoa / 30 mA equipamento.
16. **Grid-tie** — inversor que injeta em rede pública; exige anti-islanding.
17. **Ground relay** — relé que fecha N-G quando gerador/inversor é a fonte ativa.
18. **Hybrid inverter** — inversor que integra carregador + transfer switch + solar MPPT.
19. **Interlock kit** — kit de intertravamento mecânico entre disjuntores.
20. **Inversor multiplus** — inversor/carregador com transfer switch e power assist integrados.
21. **Island mode** — operação de gerador/inversor sem conexão à rede pública.
22. **Isolador galvânico (galvanic isolator)** — dispositivo que bloqueia corrente DC no PE entre cais e barco.
23. **Isolation transformer** — transformador de isolação que cria neutro/PE a bordo, independente do cais.
24. **Load shedding** — desligamento programado de cargas para evitar sobrecarga do gerador.
25. **Load sharing** — distribuição de carga entre geradores em paralelo.
26. **Make-before-break (MBB)** — lógica em que nova fonte fecha antes da antiga abrir — exige sincronismo.
27. **Neutral pole** — polo dedicado ao neutro no transfer switch (2-pole ou 3-pole).
28. **OTTS (Open Transition Transfer Switch)** — transferência aberta (BBM) — padrão para recreio.
29. **Parallel source** — operação em paralelo entre duas fontes.
30. **Pass-through** — modo do inversor em que shore/gerador passa direto pela saída AC sem conversão.
31. **Power assist (Victron)** — modo em que inversor soma inversão à shore/gerador para suportar pico.
32. **Pre-transfer timer** — retardo entre detecção de falha e ordem de partida do gerador.
33. **Re-transfer timer** — retardo para voltar à shore após estabilização.
34. **Relé de sincronismo (25)** — relé que confirma fase/freq/tensão antes de fechar paralelismo.
35. **Relés de proteção (27/59/81)** — subtensão / sobretensão / sub-sobrefrequência.
36. **RCBO** — DR + disjuntor integrado (IEC 61009).
37. **RCCB** — DR puro (IEC 61008).
38. **Shore power** — alimentação pelo cabo do cais.
39. **Soft-load transfer** — transferência com rampa de carga gradual (CTTS avançado).
40. **Split-phase** — sistema americano 120/240 V com neutro central.
41. **STS (Static Transfer Switch)** — transfer solid-state < 4 ms (SCR/IGBT).
42. **Sync-check relay** — ver relé de sincronismo.
43. **Tap change** — chave de alteração de tensão em transformador.
44. **TN-S / TN-C-S / IT-system** — classificações de aterramento (IEC 60364-1).
45. **Transfer switch (genérico)** — chave de transferência (manual, automática ou solid-state).
46. **UPS (Uninterruptible Power Supply)** — fonte contínua com bateria e transfer < 4 ms.
47. **Utility** — rede pública; em náutica, shore power.
48. **UV/OV (undervoltage/overvoltage)** — critérios de disparo para partida do gerador.
49. **Voltage window** — janela aceitável de tensão da fonte antes de transferir (ex.: 108-132 V em 120 V nominal).
50. **Zero-crossing detection** — detecção do zero da onda AC para comutação sincronizada solid-state.

## FAQ

**Posso transferir diretamente de uma fonte para outra sem passar por OFF?**

Depende do equipamento. ATS automáticos fazem break-before-make internamente em milissegundos. Chaves manuais sem intertravamento explícito precisam da posição OFF intermediária como segurança. Em sistemas synchronized (raro em recreio), existe closed-transition com paralelismo < 100 ms.

**Todo inversor já substitui chave seletora externa?**

Não. Inversor multiplus (Victron, Mastervolt, Magnum) integra transfer switch para UMA entrada shore/gerador. Se houver duas fontes externas (shore + gerador além do inversor), ATS externo ainda é necessário, ou inversor com entrada dupla (Victron Quattro).

**Se a tensão está presente, a transferência está correta?**

Não necessariamente. Pode haver presença de tensão com topologia incorreta, fonte errada ou risco de backfeed. Verifique: (1) qual fonte está alimentando, (2) se N-G bonding está coerente com a fonte ativa, (3) se não há paralelismo inadvertido.

**Qual a diferença entre transfer switch de uso terrestre e marine?**

Construção (materiais contra corrosão), IP classification (mínimo IP44 em casaria), certificação (UL 1008 marine variant ou ABYC compliance), e tratamento específico de N-G bonding conforme fonte ativa.

**Posso usar um inversor grid-tie residencial em embarcação atracada?**

Não sem autorização do operador da marina. Inversor grid-tie precisa de anti-islanding certificado e pode violar regras locais. Em embarcação com painel solar, use inversor off-grid ou híbrido com modo "feed-in" desabilitado.

**O isolador galvânico substitui ATS?**

Não. São funções diferentes: isolador galvânico bloqueia corrente DC no PE entre cais e barco (anti-corrosão, anti-ESD); ATS escolhe qual fonte AC alimenta o barramento. Ambos coexistem em instalação profissional.

## Integração com outras notas

- [[CAIS (Pier) (AC)]]
- [[Gerador (AC)]]
- [[Inversora (DC To AC)]]
- [[Proteção Dr]]
- [[Quadro Elétrico e Painel de Distribuição AC-DC]]
- [[Transformador Entrada]]
- [[Chaves Gerais (DC)]]
- [[Contatores (AC)]]

## Perguntas que esta nota responde

- Como selecionar fontes AC em embarcações com segurança?
- Qual a função real de uma chave seletora ou transfer switch?
- Quais erros de topologia e operação aparecem na comutação AC de bordo?
- Qual a diferença entre ATS manual, automático e inversor multiplus?
- Quando é obrigatório intertravamento físico e quando lógica eletrônica basta?
