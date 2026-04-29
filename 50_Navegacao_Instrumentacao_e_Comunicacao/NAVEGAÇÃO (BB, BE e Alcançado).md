---
title: "NAVEGAÇÃO (BB, BE e Alcançado)"
note_type: "technical-note"
domain: "50_Navegacao_Instrumentacao_e_Comunicacao"
source_file: "NAVEGAÇÃO (BB, BE e Alcançado) ff119734f7fb8264ba9b01e36f23d896.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "24"
tier_fase_6: "S"
reviewed_on: "2026-04-19"
review_jurisdiction:
  - "Brasil"
  - "internacional"
normas_citadas:
  - "COLREGs 72 — International Regulations for Preventing Collisions at Sea (Rules 20-31)"
  - "COLREGs Regra 20 — Application (aplicabilidade das luzes)"
  - "COLREGs Regra 21 — Definitions (definições fotométricas de masthead light, sidelights, sternlight, towing light, all-round light)"
  - "COLREGs Regra 22 — Visibility of lights (alcance mínimo por porte)"
  - "COLREGs Regra 23 — Power-driven vessels underway"
  - "COLREGs Regra 25 — Sailing vessels underway and vessels under oars"
  - "COLREGs Regra 30 — Anchored vessels and vessels aground"
  - "COLREGs Regra 38 — Exemptions (isenções legais)"
  - "COLREGs Annex I — Positioning and technical details of lights and shapes"
  - "ISO 16180:2011 — Small craft — Navigation lights — Installation, placement and visibility"
  - "ISO 19009:2015 — Small craft — Electric navigation lights — Performance requirements"
  - "IMO Resolution A.694(17) — General requirements for shipborne radio and electronic navigation aids"
  - "IEC 60945 — Maritime navigation and radiocommunication equipment — General requirements"
  - "IEC 61108-1 — GNSS receiver performance (quando integrado a luzes GPS)"
  - "USCG 33 CFR Part 183 — Boats and associated equipment"
  - "USCG 46 CFR Part 111 — Electrical engineering (grandes embarcações)"
  - "ABYC A-16 (2023) — Electric navigation lights"
  - "ABYC E-11 (2023) — AC and DC Electrical Systems on Boats"
  - "ABYC E-30 — Ignition protection for marine products (fiação sob coberta)"
  - "NORMAM-201/DPC — Tráfego e Permanência de Embarcações"
  - "NORMAM-211/DPC — Embarcações de esporte e recreio"
  - "Resoluções ANTAQ/DPC aplicáveis à Marinha Mercante"
  - "ABNT NBR 5410:2004 + emendas — Instalações elétricas de baixa tensão"
  - "CIE Publication 15:2004 — Colorimetry (coordenadas das cores das luzes)"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://www.nmea.org/standards.html"
  - "https://www.gov.br/anatel/pt-br/regulado/outorga/servico-movel-maritimo"
aliases:
  - "NAVEGAÇÃO (BB, BE e Alcançado)"
seo_title: "NAVEGAÇÃO (BB, BE e Alcançado)"
seo_description: "LUZES DE NAVEGAÇÃO (BB, BE e Alcançado) — Sistema de iluminação de navegação previsto em COLREGs para embarcações em movimento. Verde em BE/boreste, vermelho em BB/bombordo e branco de alcançado na popa."
seo_keywords:
  - "NAVEGAÇÃO"
  - "Alcançado"
  - "50 Navegacao Instrumentacao e Comunicacao"
geo_queries:
  - "O que é NAVEGAÇÃO (BB, BE e Alcançado) em instalações elétricas náuticas?"
  - "Qual é a função de NAVEGAÇÃO (BB, BE e Alcançado) na embarcação?"
related_notes:
  - "AIS (Automatic Identification System)"
  - "Buzina"
  - "Bússola Eletrônica (Compass / HDG Sensor)"
  - "Chartplotter / GPS / MFD"
  - "Dsc — Chamada Seletiva Digital"
  - "EPIRB / Beacon de Emergência"
  - "Estação de Vento / Anemômetro"
  - "Mob — Man Overboard — Sistema de Detecção"
---

# NAVEGAÇÃO (BB, BE e Alcançado)

> [!abstract] Resumo técnico
> LUZES DE NAVEGAÇÃO (BB, BE e Alcançado) — Sistema de iluminação de navegação previsto em COLREGs para embarcações em movimento. Vermelho em BB/bombordo, verde em BE/boreste e branco de alcançado na popa. O arranjo exato depende do tipo e do porte da embarcação.

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **As cores e arcos não são "costume náutico" — são direito internacional vinculante** — COLREGs Regra 21 define 112,5° vermelho (BB) + 112,5° verde (BE) + 135° branca (alcançado) + 225° branca (masthead) e Annex I especifica colorimetria CIE, alcance em milhas náuticas e posicionamento; qualquer desvio é violação.
> 2. **Alcance mínimo é função do comprimento** — embarcação < 12 m: sidelights 1 mn + sternlight 2 mn + masthead 2 mn; < 20 m: sidelights 2 mn; < 50 m: sidelights 2 mn + masthead 3 mn + sternlight 2 mn; > 50 m: sidelights 3 mn + masthead 6 mn. (COLREGs Reg 22)
> 3. **LED só pode substituir incandescente se for homologado ISO 19009:2015 (luzes de navegação elétricas) ou ABYC A-16** — LED de "loja de ferragem" ou LED automotivo tem coordenadas CIE fora da norma; a Capitania pode autuar em inspeção mesmo que "pareça" correto.
> 4. **BB vermelho e BE verde, sempre da perspectiva do tripulante olhando para a proa** — não da perspectiva de fora. Confusão na instalação inverte luzes e envia mensagem oposta a outros navegantes (rumo reverso).
> 5. **Veleiros: tricolor no topo do mastro OU luzes de bordo inferiores — nunca as duas simultâneas** — COLREGs Regra 25 permite tricolor APENAS em modo vela pura; a motor, obrigatório masthead light + sidelights inferiores. Chave seletora é projeto correto.
> 6. **Luz de alcançado (sternlight) é o que mais esquecem** — 135° branca ré, alcance 2 mn; em embarcação > 12 m a motor, é separada; em tricolor de veleiro, integrada. Ausência é infração grave.
> 7. **Dimmer em luz de navegação NÃO é permitido** — a luz deve operar em plena potência para atingir alcance fotométrico normativo; dimmer subdimensiona e viola o alcance mínimo.
> 8. **Sinais adicionais por tipo de embarcação** — rebocando (Rule 24), restrita (Rule 27), pescando (Rule 26): arranjos específicos com luzes adicionais (all-round vermelha/branca/verde) que o comandante deve conhecer por tipo de operação.
> 9. **Inspeção pré-saída checklist não-negociável** — BB vermelho? BE verde? Masthead branca 225°? Sternlight branca 135°? Todos acendem? Arco visível? Cabos e conectores sem oxidação? Se algo falhou, não saia.

> [!danger] Quando chamar um especialista (engenheiro/técnico com formação em COLREGs + eletrônica marinha)
> 1. **Homologação de embarcação nova e comissionamento Classe DPC** — instalação de sistema de luzes em embarcação comercial ou recreio de > 12 m requer plano de luzes aprovado pela Capitania, ensaio fotométrico documentado (ISO 16180/19009 ou USCG 33 CFR 183) e vistoria; escopo de projeto naval.
> 2. **Retrofit com tricolor mastro em veleiro importado (padrão EU)** — substituição de incandescente 25 W por tricolor LED no topo do mastro exige passagem de cabo pelo mastro, chave seletora Vela/Motor, proteção contra raio ABYC TE-4 e alinhamento com Annex I COLREGs; projeto elétrico.
> 3. **Embarcação restrita em sua capacidade de manobra (Rule 27)** — arranjo de luzes especial (all-round vermelha-branca-vermelha na vertical + mastro) para operação de draga, pesquisa, reboque, mergulho, cabo submarino etc.; licenciamento operacional com Capitania + DPC.
> 4. **Conflito entre homologação USCG e CE-RCD europeu** — embarcação importada dos EUA com luzes USCG e inspeção brasileira exigindo ISO: a equivalência nem sempre é automática; trânsito com plano de equivalência documentado ou substituição.
> 5. **Perícia pós-abalroamento com alegação "luzes apagadas/erradas"** — laudo forense requer leitura do switch panel, documentação fotográfica, exame de oxidação de conectores, teste de tensão em terminais das luminárias, certificação da luminária; escopo jurídico.
> 6. **Integração com IoT/automação de luzes (acendimento automático ao pôr-do-sol, sensor crepuscular)** — sistemas "smart" adicionados sem certificação podem gerar glitch de intermitência (não compliant com COLREGs que exige fluxo constante); análise de compatibilidade necessária.
> 7. **Instalação de luz em embarcação com fibra de carbono** — não há caminho de retorno de descargas; ABYC TE-4 + análise de aterramento específico; engenheiro elétrico naval.
> 8. **Navegação internacional com regras contrárias (inland rules USCG vs COLREGs internacionais)** — EUA tem Inland Navigation Rules diferentes (33 CFR 84-88); embarcação com masthead separate de sidelights para internacional e combinado para inland; projeto e chave seletora.
> 9. **Substituição de magnetron de luz de tope em navio comercial (sistema de arco elétrico)** — embarcação comercial com luz a arco (alcance > 6 mn, rara em recreio) requer técnico certificado pelo fabricante (Lalolux, AquaSignal industrial); nunca DIY.

> [!info] Glossário rápido (≈ 46 termos)
> - **BB (Bombordo)** — lado esquerdo visto da proa, luz VERMELHA.
> - **BE (Boreste)** — lado direito visto da proa, luz VERDE.
> - **Alcançado (Sternlight)** — luz BRANCA na popa, arco 135°.
> - **Masthead light** — luz branca no mastro/tope, arco 225° (COLREGs Reg 23).
> - **Sidelight** — luzes laterais coloridas, arco 112,5° cada.
> - **All-round light** — luz 360° (âncora, restrita, pescando).
> - **Luz de âncora** — all-round branca usada fundeado (Rule 30).
> - **Towing light** — all-round amarela (embarcações rebocando, Rule 24).
> - **Luz de tricolor** — combinada BB+BE+alcançado no topo do mastro (veleiros apenas).
> - **Bicolor light** — BB+BE combinados em uma luminária única (proa).
> - **Arco 112,5°** — sidelight (de proa até 22,5° atrás do través).
> - **Arco 135°** — sternlight (135° da popa, 67,5° cada lado).
> - **Arco 225°** — masthead light (cobre tudo à frente + lados 22,5° atrás do través).
> - **Arco 360°** — all-round light (âncora, restrita, pesca).
> - **CIE xy chromaticity** — coordenadas colorimétricas Internacional Commission on Illumination.
> - **Fotometria** — medição de intensidade luminosa por ângulo (cd, candela).
> - **Candela (cd)** — unidade de intensidade luminosa; sidelight 1 mn ≈ 0,9 cd.
> - **Intensidade mínima por ângulo** — definida em Annex I COLREGs.
> - **Alcance (mn)** — distância de visibilidade em milhas náuticas.
> - **Ano de emenda COLREGs** — 1972 original + emendas 1981, 1987, 1989, 2003, 2007, 2013.
> - **Annex I** — Positioning and technical details (posicionamento geométrico).
> - **Annex II** — Additional signals for fishing vessels.
> - **Annex III** — Technical details of sound signal appliances.
> - **Annex IV** — Distress signals.
> - **USCG 33 CFR 183** — Boats and associated equipment (padrão norte-americano).
> - **ABYC A-16** — Electric Navigation Lights (2023, padrão ABYC).
> - **ISO 16180:2011** — Navigation lights — Installation and visibility.
> - **ISO 19009:2015** — Electric navigation lights — Performance requirements.
> - **IEC 60945** — General requirements for marine electronic equipment.
> - **Inland Navigation Rules (USA)** — Rules 33 CFR 84-88, versão doméstica USCG.
> - **Certificado de homologação** — documento que atesta cumprimento normativo.
> - **Flux constant** — COLREGs exige fluxo constante (não strobing).
> - **Intensidade máxima** — limite superior em cd (ofuscamento).
> - **Redução diurna** — permitida em all-round de navio grande, nunca em recreio.
> - **Dimmer** — NÃO permitido em luzes de navegação.
> - **Fan beam / Sector cut-off** — transição entre setores deve ser < 6°.
> - **Temperatura de cor (vermelho/verde)** — definida por CIE, não pelo nome.
> - **LED marino homologado** — com certificação USCG/ISO 19009/ABYC A-16.
> - **LED automotivo não serve** — fora de colorimetria CIE náutica.
> - **Halogênio** — substituto do incandescente antes do LED (transição anos 2000-2010).
> - **Incandescente (filamento)** — tradicional, vida 500-2000 h, consumo 2-5 A.
> - **Fresnel lens** — lente escalonada, padrão em luminárias de longo alcance.
> - **Cut-off angle** — ângulo preciso onde a luz corta.
> - **IP-67/IP-68** — proteção ingress protection para ambiente marino.
> - **Marine-grade connector** — conectores vedados tipo Deutsch DT, Ancor, AMP Superseal.
> - **Bonding (aterramento)** — ligação de massa para proteção contra raio (ABYC TE-4).
> - **Hotline** — ligação direta ao banco DC (sempre ativa, bypass da chave geral).

## O que é

As luzes de navegação são o sistema de iluminação obrigatório definido pela Convenção COLREGS (Regulamento Internacional para Evitar Abalroamentos no Mar), adotado pelo Brasil via NORMAM. Elas identificam a posição, o rumo e o tipo de embarcação para outros navegantes, especialmente à noite e em baixa visibilidade.

Os três tipos básicos para embarcações de recreio a motor:

- **Luz de boreste (BE)** — verde, no lado de boreste da embarcação (direita de quem olha para a proa), arco de 112,5°
- **Luz de bombordo (BB)** — vermelha, no lado de bombordo da embarcação (esquerda de quem olha para a proa), arco de 112,5°
- **Luz de alcançado (popa)** — branca, ré, arco de 135°

> **Mnemônico prático:** "Verde-direita, vermelho-esquerda" — da perspectiva de quem está na embarcação olhando para frente.
>

## Função na embarcação

- Sinalizar a presença, posição e rumo da embarcação para outros navegantes
- Indicar o lado de aproximação segura (para onde a embarcação está virando)
- Diferenciar tipo de embarcação (a vela, a motor, rebocando, restrita)
- Cumprir obrigação legal — COLREGS / NORMAM-01 (edição a verificar)

Sem luzes de navegação corretas: risco de colisão + infração grave com autuação pela Capitania dos Portos.

## Como aparece na prática

**Muito comum no Brasil:**

- Lanchas e veleiros com conjunto de luzes LED combinadas (BB+BE) na proa
- Luz de alcançado (branca) na popa
- Alimentação por chave dedicada "NAVLIGHTS" no painel
- Conjuntos Hella, Perko, Aqua Signal

**Comum em barcos importados:**

- Conjunto tricolor no topo do mastro (veleiros) — uma única luz com três setores coloridos
- Luzes integradas ao costado (flush mount) em lanchas premium
- A intensidade luminosa não deve ser reduzida de forma a comprometer o alcance e a fotometria exigidos para a luz certificada

**Mais presente em embarcações maiores/premium:**

- Luzes de navegação separadas (BB e BE individuais, não combinadas)
- Maior ângulo de visibilidade e maior alcance (2 a 3 milhas náuticas)
- Integração ao sistema de automação — acendem automaticamente ao anoitecer

## Fundamentos mínimos

**COLREGS Regra 23 — embarcações a motor:**

- Luz de tope (mastro): branca, arco 225°, visível a 3 milhas (embarcação ≥ 50m) ou 2 milhas (< 50m)
- Luzes de bordo (BB vermelho, BE verde): arco 112,5°, com alcance conforme o porte e a regra aplicável
- Luz de alcançado (popa): branca, arco 135°, visível a 2 milhas

**Embarcações muito pequenas em condições específicas:** podem existir arranjos alternativos previstos na regra, mas isso deve ser lido diretamente nas COLREGs e na regulamentação aplicável ao tipo de navegação, sem simplificação indevida.

**Regra dos setores:** O arco de visibilidade das luzes define o ângulo de onde outro navegante consegue ver a luz — e, portanto, de onde vem a embarcação que está à sua frente. É a base do sistema de prioridade de rota.

**LED vs. incandescente:** LEDs modernos homologados consomem 80–90% menos energia. Mas devem ser certificados para uso marino com arco de visibilidade correto — não usar LED genérico de carro ou LED de iluminação residencial.

## Características principais

| Parâmetro | LED moderno | Incandescente |
| --- | --- | --- |
| Corrente típica | 0,3–0,8A por luz | 2–5A por luz |
| Vida útil | 20.000–50.000h | 500–2.000h |
| Temperatura de cor | 6000–7000K (branco) / filtros RGB | Amarelada |
| Homologação | USCG / ISO 16180:2011 / ABYC | ISO 16180:2011 |
| Vibração | Excelente (sem filamento) | Vulnerável |
| Custo inicial | Maior | Menor |

## Configurações e variações comuns

**Conjunto combinado de proa (< 12m, mais comum no Brasil)**

- Uma única luminária com dois setores: verde (112,5° boreste) e vermelho (112,5° bombordo)
- Montado na proa
- Luz de popa (alcançado) separada, na ré

**Luzes separadas (> 12m ou padrão premium)**

- Luz verde individual no costado de boreste
- Luz vermelha individual no costado de bombordo
- Maior alcance de visibilidade e maior ângulo

**Tricolor de mastro (veleiros)**

- Uma única luminária no topo do mastro com três setores: vermelho (BB) + verde (BE) + branco (popa)
- Mais eficiente — uma luz serve tudo
- Não pode ser usada simultaneamente com as luzes de bordo inferiores (apenas uma ou outra)

**Conjunto de 360° (âncora + tope)**

- Ver tópico LUZ DE ÂNCORA

## Principais marcas

- **Hella Marine** — referência de qualidade, homologação USCG, boa disponibilidade no Brasil
- **Aqua Signal** — alemã, presente em iates europeus, excelente durabilidade
- **Perko** — americana, boa reputação, muito em barcos americanos importados
- **Kahlenberg** — naval, mais robusta, embarcações maiores
- **Attwood** — acessível, boa qualidade, mercado americano

**No Brasil:** Hella e Perko são as mais encontradas. Existem cópias não homologadas no mercado — verificar sempre a certificação USCG ou ISO no produto.

## Componentes e sistemas relacionados

- **Chave de navlights** — chave dedicada no painel principal
- **Fusível ou disjuntor** — proteção do circuito
- **Cabo elétrico** — bitola mínima 1mm² (corrente baixa, mas distância pode ser significativa)
- **Conector vedado** — todo conector externo deve ser marinizado (IP67 mínimo)
- **Luz de tope (mastro)** — complemento obrigatório em embarcações > 12m a motor
- **Luz de âncora** — modo de fundeio (ver tópico dedicado)

## Onde costuma dar problema

| Problema | Sintoma | Causa |
| --- | --- | --- |
| Luz apagada | Não acende | Bulbo queimado, fusível, oxidação |
| Arco incorreto | Luz visível fora do setor | Luminária mal posicionada ou danificada |
| Cor errada | Verde onde deveria ser vermelho | Conexão invertida ou luminária trocada |
| Intermitência | Luz piscando sem ser strobo | Oxidação em conector |
| Condensação interna | LED embaçado, falha prematura | Vedação comprometida |
| Luz de popa apagada | Popa sem luz | Cabo rompido, conector oxidado |

## Causas raiz

**Luz apagada:**

- LED queimado (menos comum que incandescente)
- Oxidação em conectores externos expostos à maresia — a causa mais frequente
- Fusível queimado por curto em conector submerso na proa (spray constante)

**Cor errada:**

- Luminárias instaladas no lado errado (BB e BE invertidos)
- Comprador trocou a luminária sem observar marcação de bordo

**Causa raiz sistêmica:** Conectores e terminais sem vedação adequada em ambiente de maresia. A cada temporada sem manutenção, oxidação progressiva aumenta a resistência até a luz falhar.

## Diagnóstico prático

**Passo 1:** Luz não acende → verificar chave, fusível e tensão no terminal da luminária.

**Passo 2:** Tensão no terminal mas sem luz → LED com defeito ou oxidação no contato interno da luminária. Limpar contatos ou substituir.

**Passo 3:** Luz intermitente → resistência variável em algum conector. Inspecionar toda a linha com multímetro em modo continuidade.

**Passo 4:** Verificar o setor de visibilidade: colocar um bloqueador e circular ao redor da proa — luz deve aparecer somente no setor correto.

**Passo 5:** Verificar cor e bordo: BB/bombordo deve ser vermelho; BE/boreste deve ser verde. Registrar foto de frente para confirmar posicionamento e setor.

## Boas práticas

- Usar somente luminárias com homologação USCG ou certificação ISO 16180:2011
- Inspecionar e limpar conectores externos no início de cada temporada
- Testar todas as luzes de navegação no checklist pré-saída — sempre
- Carregar lanterna manual branca de reserva (obrigação legal para embarcações < 7m)
- Verificar visibilidade de cada setor com outra pessoa no cais
- Em veleiros: testar tricolor de mastro e luzes de bordo como sistemas separados

## Cuidados de instalação

- Luminárias posicionadas conforme o arco de visibilidade correto (não bloquear por anteparas ou estruturas)
- Cabos protegidos em eletrocalha ou condute — proa recebe muito spray
- Conectores vedados com terminal crimp-seal ou conector com gland de vedação
- Massa dedicada — não compartilhar com outros sistemas de corrente alta (evitar ruído em instrumentos)
- Verificar que nenhuma estrutura do barco bloqueia parcialmente o arco de visibilidade

## Cuidados de uso

- Não reduzir luminosidade nem alterar circuitos de modo que a luminária deixe de atender ao alcance e ao setor previstos em certificação
- Verificar funcionamento antes de cada saída noturna ou de baixa visibilidade
- Nunca navegar com luz apagada — buscar o problema antes de sair

## Erros comuns

❌ **Instalar LED genérico de carro** — cor, ângulo e fotometria incorretos — não é homologado

❌ **BB e BE invertidos** — vermelho no lado errado indica rumo oposto para outros navegantes

❌ **Usar luz de âncora como luz de navegação** — ângulo 360° não substitui as luzes direcionais

❌ **Sem verificação periódica** — luz queimada descoberta somente na noite de saída

❌ **Conector aberto exposto na proa** — oxida em duas temporadas

❌ **Luz de popa ignorada** — ausência cria risco de ser alcançado por embarcação mais rápida

## Relação com outros sistemas

- **Painel de distribuição DC** — chave de navlights dedicada
- **Banco de bateria** — consumo baixo (LED) mas circuito permanente durante navegação noturna
- **Hotline** — em algumas embarcações, navlights no hotline para manter acesas mesmo com chave geral desligada
- **Luz de âncora** — sistema complementar para fundeio (ver tópico)
- **VHF/AIS** — identificação eletrônica que complementa as luzes físicas

## Brasil x referências internacionais

**Prática comum no Brasil:** Luminárias genéricas sem homologação, LED de carro adaptado, verificação ausente no checklist. Muitas embarcações pequenas navegando sem luz de alcançado.

**Referência COLREGS / NORMAM-01 (edição a verificar):** Obrigação legal absoluta. Multa e responsabilidade civil em caso de abalroamento com luzes incorretas ou ausentes. NORMAM-01 (edição a verificar) define os requisitos para embarcações miúdas brasileiras.

**Ponto de conflito:** NORMAM-01 (edição a verificar) e COLREGS definem requisitos mínimos de alcance visual por comprimento de embarcação. Na prática, muitas lanchas pequenas no Brasil usam luminárias subdimensionadas para o porte.

**Leitura equilibrada:** Para embarcação ≤ 12m com uso diurno: conjunto combinado de proa + luz de popa LED homologado resolve. Para uso noturno frequente ou embarcações maiores: investir em sistema completo com alcance adequado é obrigação de segurança.

## Normas e referências aplicáveis

- **COLREGs 72 — Convention on the International Regulations for Preventing Collisions at Sea** — base legal internacional; Regras 20-31 especificam luzes e sinais.
- **COLREGs Regra 20** — Application (aplicabilidade das luzes em todas as embarcações).
- **COLREGs Regra 21** — Definitions (masthead light, sidelights, sternlight, towing light, all-round light; arcos e fotometria).
- **COLREGs Regra 22** — Visibility of lights (alcance mínimo em milhas náuticas por porte).
- **COLREGs Regra 23** — Power-driven vessels underway (masthead + sidelights + sternlight).
- **COLREGs Regra 25** — Sailing vessels underway (tricolor no topo OU luzes de bordo + sternlight; nunca simultâneas a motor).
- **COLREGs Regra 26** — Fishing vessels (all-round vermelha-branca + direcional).
- **COLREGs Regra 27** — Vessels not under command or restricted in their ability to maneuver.
- **COLREGs Regra 30** — Anchored vessels and vessels aground (all-round branca 360°).
- **COLREGs Regra 38** — Exemptions (embarcações antigas, período de transição).
- **COLREGs Annex I** — Positioning and technical details of lights and shapes (geometria precisa de instalação).
- **COLREGs Annex II** — Additional signals for fishing vessels.
- **ISO 16180:2011** — Small craft — Navigation lights — Installation, placement and visibility (requisitos de instalação em embarcações < 24 m).
- **ISO 19009:2015** — Small craft — Electric navigation lights — Performance requirements (homologação elétrica e fotométrica).
- **IMO Resolution A.694(17)** — General requirements for shipborne radio and electronic navigation aids (base técnica para equipamento embarcado).
- **IEC 60945** — Maritime navigation and radiocommunication equipment — General requirements (EMC, IP, ambiente marinho).
- **IEC 61108-1** — GNSS receiver performance (quando integrado a luzes com GPS automático).
- **USCG 33 CFR Part 183** — Boats and associated equipment (padrão norte-americano recreio).
- **USCG 46 CFR Part 111** — Electrical engineering (grandes embarcações comerciais, sistema de luzes).
- **ABYC A-16 (2023)** — Electric Navigation Lights (instalação, alcance, fiação em embarcações de recreio).
- **ABYC E-11 (2023)** — AC and DC Electrical Systems on Boats (fiação, fusíveis, bitolas do circuito de luzes).
- **ABYC E-30** — Ignition protection for marine products (fiação sob coberta em áreas de combustível).
- **NORMAM-201/DPC** — Tráfego e Permanência de Embarcações (aplicabilidade a comerciais brasileiras).
- **NORMAM-211/DPC** — Embarcações de esporte e recreio (obrigação de luzes em recreio brasileiro).
- **Resoluções ANTAQ/DPC** — aplicáveis à Marinha Mercante.
- **ABNT NBR 5410:2004 + emendas** — Instalações elétricas de baixa tensão (aplicável quando há parte AC).
- **CIE Publication 15:2004** — Colorimetry (coordenadas CIE xy das cores vermelho/verde/branco/amarelo exigidas pelas COLREGs).

## Destaques para ensino

- O sistema COLREGS: por que as cores e os arcos foram definidos assim (prevenção de colisão por identificação de rumo)
- Por que LED genérico não substitui LED homologado — fotometria e arco
- Mnemônico prático: vermelho = PERIGO (pare, cuidado), verde = VANTAGEM (pode passar)
- Verificação dos setores: como testar corretamente no cais
- Responsabilidade legal: navegar sem luzes é infração — e a responsabilidade em colisão recai sobre quem estava sem luz

## Ideias de vídeo, aula prática ou demonstração

- Demonstração noturna: como as luzes aparecem para outra embarcação
- Teste de setor: bloqueador na proa verificando arco de 112,5°
- Comparação: LED homologado vs. LED genérico (fotometria real)
- Troca de conjunto combinado Hella: instalação correta passo a passo
- Leitura das COLREGS: quem tem prioridade baseado nas luzes visíveis

## Ideias de diagramas, circuitos, simulações ou imagens

- Diagrama dos setores de visibilidade: vista de cima da embarcação com arcos
- Circuito elétrico: painel → fusível → chave navlights → BB/BE/popa → massa
- Ilustração da perspectiva de outra embarcação: o que vê dependendo do ângulo de abordagem
- Tabela COLREGS: tipo de embarcação × configuração de luzes exigida

## Observações técnicas avançadas

**Temperatura de cor e conformidade:** As COLREGS definem a cor pelas coordenadas CIE (Internacional Commission on Illumination) — não apenas "verde" ou "vermelho" genérico. LEDs homologados têm a cor dentro das coordenadas especificadas. LEDs genéricos frequentemente ficam fora da especificação.

**Luzes de navegação em veleiros:** Veleiros têm opções adicionais — tricolor no mastro (para vela) e luzes de bordo + tope separadas (para motor). Nunca ligar os dois sistemas simultaneamente (arcos se sobreporiam de forma incorreta).

**AIS e luzes:** Embarcações com AIS transmitem posição, mas AIS não substitui as luzes de navegação — sistemas complementares. Em baixa visibilidade, a luz é o que o olho nu enxerga; AIS é o que o radar/computador enxerga.

## FAQ

**Posso usar LED de carro nas luzes de navegação para economizar?**

Não. LED de automóvel não tem homologação marítima, o arco de emissão é diferente e a cor pode não estar dentro das coordenadas CIE exigidas pela COLREGS. Usar somente LED com certificação ISO 16180:2011 ou USCG.

**A lancha pequena (< 7m) é obrigada a ter luzes fixas?**

Sim — deve ter pelo menos luz de popa branca fixa. Em movimento, deve exibir as luzes de bordo. A COLREGS permite lanterna de mão branca como alternativa emergencial mas não como solução permanente.

**Qual a diferença entre luz de navegação e luz de âncora?**

Luz de navegação = embarcação em movimento, com setores direcionais. Luz de âncora = branca 360° usada quando fundeado. Nunca confundir — usar âncora em movimento ou navlights fundeado está errado.

**Posso ligar as luzes de navegação em dimmer?**

Absolutamente não. Devem operar sempre em plena potência para garantir o alcance especificado pelas COLREGS.

**O que acontece se eu colidir com luzes incorretas ou apagadas?**

Responsabilidade civil aumentada pelo descumprimento da norma. Autuação pela Capitania dos Portos. Em caso de vítima, agravante legal por negligência.

## Integração com outras notas

- [[AIS (Automatic Identification System)]]
- [[Buzina]]
- [[Bússola Eletrônica (Compass / HDG Sensor)]]
- [[Chartplotter / GPS / MFD]]
- [[Dsc — Chamada Seletiva Digital]]
- [[EPIRB / Beacon de Emergência]]
- [[Estação de Vento / Anemômetro]]
- [[Mob — Man Overboard — Sistema de Detecção]]

## Perguntas que esta nota responde

- O que é NAVEGAÇÃO (BB, BE e Alcançado) em instalações elétricas náuticas?
- Qual é a função de NAVEGAÇÃO (BB, BE e Alcançado) na embarcação?
