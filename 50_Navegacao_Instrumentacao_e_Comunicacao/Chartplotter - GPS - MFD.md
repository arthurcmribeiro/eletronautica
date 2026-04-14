---
title: "Chartplotter / GPS / MFD"
note_type: "technical-note"
domain: "50_Navegacao_Instrumentacao_e_Comunicacao"
source_file: "CHARTPLOTTER GPS MFD 33a19734f7fb8115a2f3e1a2bef2f5e6.md"
status: "technical-review-l1"
aliases:
  - "CHARTPLOTTER GPS MFD"
  - "CHARTPLOTTER / GPS / MFD"
seo_title: "Chartplotter / GPS / MFD"
seo_description: "CHARTPLOTTER / GPS / MFD — Sistema central de navegação eletrônica. GPS fornece posição; chartplotter exibe em carta náutica; MFD (Multifunction Display) integra rad."
seo_keywords:
  - "Chartplotter"
  - "GPS"
  - "MFD"
  - "50 Navegacao Instrumentacao e Comunicacao"
geo_queries:
  - "O que é Chartplotter / GPS / MFD em instalações elétricas náuticas?"
  - "Qual é a função de Chartplotter / GPS / MFD na embarcação?"
related_notes:
  - "AIS (Automatic Identification System)"
  - "Buzina"
  - "Bússola Eletrônica (Compass / HDG Sensor)"
  - "Dsc — Chamada Seletiva Digital"
  - "EPIRB / Beacon de Emergência"
  - "Estação de Vento / Anemômetro"
  - "Mob — Man Overboard — Sistema de Detecção"
  - "NAVEGAÇÃO (BB, BE e Alcançado)"
---

# Chartplotter / GPS / MFD

> [!abstract] Resumo técnico
> CHARTPLOTTER / GPS / MFD — Sistema central de navegação eletrônica. GPS fornece posição; chartplotter exibe em carta náutica; MFD (Multifunction Display) integra radar, sonda, AIS, câmera e NMEA 2000 em uma única tela. Corrente: 1–5A em 12V.

## O que é

O chartplotter é o computador de navegação que combina receptor GPS (posição, velocidade, rumo) com banco de dados de cartas náuticas digitais, exibindo em tempo real a posição da embarcação sobre a carta. O MFD (Multifunction Display) é o chartplotter evoluído que integra múltiplos sistemas de navegação em uma única tela touchscreen.

A evolução foi: GPS portátil → chartplotter dedicado → MFD com integração NMEA 2000 → sistema de navegação integrado com radar, sonda, AIS, câmera, piloto automático e instrumentos de bordo.

## Função na embarcação

- Exibir a posição da embarcação em cartas náuticas em tempo real
- Calcular rumo, distância e ETA para waypoints e destinos
- Integrar dados de radar, sonda, AIS, instrumentos de vento e motor
- Planejar rotas e tracks de navegação
- Registrar o trajeto percorrido (track log)
- Servir como interface central do sistema NMEA 2000

## Como aparece na prática

**Muito comum no Brasil:**

- Garmin GPSMAP 742/942/1042 em lanchas de 25–40 pés
- Simrad NSS ou GO em veleiros de cruzeiro
- Instalado na console de comando com antena GPS no T-top ou mastro
- Cartografia Navionics ou C-MAP no cartão SD

**Comum em barcos importados:**

- MFD de 12–16" com touchscreen integrado ao helm station
- Rede NMEA 2000 com múltiplos instrumentos integrados
- Raymarine Axiom ou Garmin GPSMAP 8600 como display principal

**Mais presente em embarcações maiores/premium:**

- Sistema com múltiplos MFDs (helm + fly bridge + saloon)
- Integração com Radar, AIS, piloto automático e câmera via NMEA 2000 / Ethernet
- Furuno NavNet TZtouch3 ou Garmin GPSMAP 8617 como sistema principal

## Fundamentos mínimos

**GPS:** Receptor de satélite que calcula posição (lat/lon), velocidade (SOG — Speed Over Ground) e rumo sobre o fundo (COG — Course Over Ground). A precisão real depende da constelação disponível, geometria dos satélites, interferências locais, ambiente de instalação, correções aplicadas e qualidade da antena/receptor.

**NMEA 0183 vs. NMEA 2000:**

- NMEA 0183: protocolo antigo, comunicação serial ponto-a-ponto (um emissor, um receptor)
- NMEA 2000 (N2K): protocolo moderno em rede (CAN bus) — múltiplos dispositivos na mesma rede, dados compartilhados

**Cartografia:** Muitos equipamentos saem de fábrica com mapa-base ou cartografia simplificada, mas a navegação séria depende da carta náutica adequada, atualizada e compatível com a região de operação. A qualidade e a atualização das cartas são tão importantes quanto o hardware.

**Atualização de cartas:** Cartas desatualizadas são risco de navegação. A Marinha do Brasil publica cartas náuticas oficiais. Navionics e C-MAP oferecem assinaturas de atualização anual.

## Características principais

| Parâmetro | Valor típico |
| --- | --- |
| Tensão | 12V DC (alguns modelos: 12–24V) |
| Corrente | 1–5A (dependendo do tamanho do display) |
| Tamanho de tela | 7" a 24" |
| Precisão GPS | depende do receptor, ambiente, constelação e correções disponíveis |
| Protocolos | NMEA 0183, NMEA 2000, Ethernet, CAN bus |
| IP | IPX6 ou IPX7 (frente d'água) |
| Temperatura de operação | -15°C a +70°C |

## Configurações e variações comuns

**Chartplotter standalone**

- Display + GPS integrado
- Sem rede NMEA 2000
- Mais simples e barato
- Garmin GPSMAP 742/942, Simrad GO5/GO7

**MFD com NMEA 2000 (mais comum em embarcações médias)**

- Display central integrando radar, sonda, AIS, instrumentos
- Rede N2K com múltiplos sensores e display
- Garmin GPSMAP 8400/8600, Raymarine Axiom Pro, Simrad NSS

**Sistema multi-display**

- MFD principal + display secundário no fly bridge ou nav station
- Sincronização de dados em tempo real via Ethernet
- Furuno NavNet, Garmin OneHelm, Raymarine Lighthouse

**Tablet como chartplotter (solução alternativa)**

- iPad com Navionics ou iNavX
- Receptor GPS externo Bluetooth (Bad Elf, Garmin GLO)
- Menor custo, boa cartografia, sem integração NMEA 2000
- Limitações: IP (chuva), temperatura, suporte de montagem

## Principais marcas

- **Garmin** — mais popular no Brasil, suporte local, cartografia BlueChart/Navionics
- **Simrad** — popular em veleiros e embarcações profissionais
- **Raymarine** — forte presença em veleiros europeus, interface Lighthouse
- **Furuno** — referência profissional, alta durabilidade, presente em embarcações de trabalho
- **Lowrance** — acessível, popular em pesca esportiva
- **Cartografia:** Navionics (melhor cobertura Brasil), C-MAP (boa qualidade global), Garmin BlueChart

## Componentes e sistemas relacionados

- **Antena GPS** — posicionada no ponto mais alto e desobstruído
- **Transdutor de sonda** — sensor integrado ao sistema MFD
- **Radar** — integrado via Ethernet ou NMEA 2000
- **Transponder AIS** — recepção e envio de dados de tráfego
- **Piloto automático** — recebe dados de rumo e destino do chartplotter
- **Instrumentos NMEA 2000** — velocidade, vento, profundidade, temperatura
- **Câmera de bordo** — exibida no MFD via IP ou cabo analógico
- **VHF com DSC** — integração para chamada de emergência com posição GPS

## Onde costuma dar problema

| Problema | Sintoma | Causa |
| --- | --- | --- |
| GPS sem fix | "Procurando satélites" permanente | Antena bloqueada, cabo danificado, antena antiga |
| Display apagando | Desligamento intermitente | Queda de tensão, cabo de alimentação fino |
| Carta desatualizada | Posição em terra ou em local incorreto | Cartografia não atualizada |
| Interferência de ruído | Display com ruído/artefatos | Aterramento ruim, EMI de outros sistemas |
| Display "embaçado" | Umidade interna | Vedação comprometida (borracha de vedação envelhecida) |
| NMEA 2000 sem dados | Instrumento sem comunicação | Terminador ausente, conector solto, backbone interrompido |

## Causas raiz

**GPS sem fix:**

- Antena com linha de visada bloqueada (dentro da cabine, próxima à VHF)
- Cabo de antena danificado ou conector oxidado
- Antena envelhecida (componentes internos degradados)

**Display apagando:**

- Queda de tensão: cabo de alimentação fino para a distância + corrente do display
- Banco de bateria descarregado causando instabilidade

**Sem dados NMEA 2000:**

- Rede N2K requer terminadores (120Ω) nos dois extremos do backbone
- Um conector T com má vedação interrompe a rede inteira

## Diagnóstico prático

**Passo 1:** GPS sem fix → verificar visibilidade do céu pela antena. Mover a embarcação para área aberta e aguardar 5 minutos.

**Passo 2:** Display apagando → medir tensão nos terminais do display em operação. Se < 11,5V em 12V: queda de tensão.

**Passo 3:** Sem dados de instrumento na rede N2K → verificar terminadores nos extremos do backbone, testar cada conector T.

**Passo 4:** Display com ruído → verificar alimentação, roteamento de cabos, fontes de EMI próximas e práticas de aterramento/equipotencialização conforme o fabricante e a arquitetura da embarcação.

**Passo 5:** Carta errada → verificar data de atualização do cartão SD e comparar com versão disponível no site do fabricante.

## Boas práticas

- Antena GPS no ponto mais alto e desobstruído, a pelo menos 1m de antenas VHF
- Cabo de alimentação dedicado com disjuntor próprio e bitola para a corrente + distância
- Considerar condicionamento de alimentação, segregação de circuitos e proteção contra ripple/picos quando o ambiente elétrico da embarcação for ruidoso
- Atualizar cartografia anualmente — especialmente para navegação em áreas novas
- Seguir a recomendação do fabricante para ligação de blindagens, drenos e eventuais pontos de equipotencialização do equipamento
- Backup: sempre ter chartplotter portátil ou app em tablet com GPS externo

## Erros comuns

❌ **Antena GPS perto da antena VHF** — interferência recíproca, GPS sem fix intermitente

❌ **Cabo de alimentação fino** — queda de tensão em displays de > 3A

❌ **Cartografia nunca atualizada** — erro grave em áreas com mudanças de balizamento

❌ **Sem aterramento do chassi** — ruído, comportamentos erráticos

❌ **Sem backup** — único chartplotter falhou em alto-mar sem backup de posição

❌ **Rede N2K sem terminadores** — toda a rede falha

## Relação com outros sistemas

- **Radar** — integração MFD: overlay de radar sobre carta
- **Sonda** — profundidade exibida no MFD
- **AIS** — alvos AIS exibidos na carta em tempo real
- **Piloto automático** — recebe waypoints e rotas do chartplotter
- **VHF com DSC** — posição GPS enviada ao VHF para chamadas de emergência
- **NMEA 2000** — backbone de integração de todos os instrumentos

## Brasil x referências internacionais

### Prática comum no Brasil

Garmin simples sem NMEA 2000, cartografia Navionics em cartão nunca atualizado, antena GPS perto da VHF, sem aterramento.

### Referência internacional

Sistema MFD com rede N2K completa, cartografia atualizada anualmente, aterramento correto, backup com tablet e GPS externo.

### Ponto de conflito

A cobertura cartográfica do Brasil no Navionics e C-MAP varia muito por região. Áreas como o Nordeste e o Pantanal têm cartas com menos detalhes que o Sudeste. A Marinha do Brasil publica cartas oficiais em formato impresso — complemento essencial.

## Normas e referências aplicáveis

- **COLREGS** — chartplotter é ferramenta de auxílio, não substitui a vigília náutica
- **NMEA 2000 Standard** — protocolo de rede de instrumentos
- **IEC 61162** — interface de equipamentos náuticos (NMEA)
- **Manual do fabricante** — instalação e configuração

## Destaques para ensino

- GPS x chartplotter x MFD: a evolução e a diferença entre eles
- NMEA 0183 vs. NMEA 2000: por que a rede é a diferença que transforma o sistema
- Qualidade da cartografia: tão importante quanto o hardware
- Antena GPS: posicionamento correto e separação de VHF
- O chartplotter não é o responsável pela navegação — é uma ferramenta de auxílio

## Ideias de vídeo, aula prática ou demonstração

- Instalação de rede NMEA 2000 básica: backbone, conectores T e terminadores
- Separação correta de antenas: GPS vs. VHF — distância e posicionamento
- Atualização de cartografia Navionics: passo a passo
- Integração chartplotter + piloto automático: criar rota e ativar piloto

## FAQ

**Posso usar o telefone celular como chartplotter?**

Com app de qualidade (Navionics, iBoating) e GPS externo (Bad Elf ou Garmin GLO): sim, como backup. Como sistema primário: limitações de IP, temperatura e suporte de fixação. Para uso recreativo casual: viável.

**Qual a diferença entre GPS e chartplotter?**

GPS = receptor de satélite que fornece posição. Chartplotter = computador que exibe essa posição em uma carta náutica digital. O GPS portátil de trilha mostra posição mas não tem carta náutica náutica detalhada.

**Preciso atualizar a cartografia?**

Sim, sempre que houver atualização relevante para a área de operação ou alteração de balizamento, profundidade publicada, infraestrutura costeira ou banco cartográfico. Em embarcações que navegam com frequência em áreas dinâmicas, revisão periódica da cartografia é medida de segurança básica.

**O que é WAAS/SBAS?**

SBAS é uma família de sistemas de aumento por satélite que pode melhorar integridade e, em certos cenários, a precisão da solução GNSS. O benefício real depende da cobertura regional, do receptor utilizado e das correções efetivamente suportadas. Não convém tratar um valor fixo de erro como garantia operacional.

## Integração com outras notas

- [[AIS (Automatic Identification System)]]
- [[Buzina]]
- [[Bússola Eletrônica (Compass / HDG Sensor)]]
- [[Dsc — Chamada Seletiva Digital]]
- [[EPIRB / Beacon de Emergência]]
- [[Estação de Vento / Anemômetro]]
- [[Mob — Man Overboard — Sistema de Detecção]]
- [[NAVEGAÇÃO (BB, BE e Alcançado)]]

## Perguntas que esta nota responde

- O que é Chartplotter / GPS / MFD em instalações elétricas náuticas?
- Qual é a função de Chartplotter / GPS / MFD na embarcação?
