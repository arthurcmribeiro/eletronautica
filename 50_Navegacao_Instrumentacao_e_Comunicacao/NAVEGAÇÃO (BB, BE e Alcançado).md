---
title: "NAVEGAÇÃO (BB, BE e Alcançado)"
note_type: "technical-note"
domain: "50_Navegacao_Instrumentacao_e_Comunicacao"
source_file: "NAVEGAÇÃO (BB, BE e Alcançado) ff119734f7fb8264ba9b01e36f23d896.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://www.nmea.org/standards.html"
  - "https://www.gov.br/ANATEL (edição a verificar)/pt-br/regulado/outorga/servico-movel-maritimo"
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

- **COLREGS 72** — Convenção Internacional para Evitar Abalroamentos (Regras 20–31)
- **NORMAM-01 (edição a verificar) (DPC/Marinha do Brasil)** — regulamentação nacional de luzes de navegação
- **ISO 16180:2011** — Requisitos fotométricos para luzes de navegação
- **USCG 33 CFR (edição a verificar) 183** — padrão americano de homologação

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
