---
title: "Inventário Visual da Base"
note_type: "audit-report"
domain: "_Editorial"
status: "active-inventory"
reviewed_on: "2026-04-17"
review_jurisdiction:
  - "Brasil"
---

# Inventário Visual da Base

## Objetivo

Este inventário organiza a camada visual da base de elétrica náutica. A regra editorial é simples: criar visual quando ele melhora entendimento técnico, diagnóstico, comparação, arquitetura, cálculo ou decisão prática. Não criar imagem decorativa.

## Critérios de seleção

Uma nota é candidata a visual quando contém pelo menos um destes padrões:

- comparação entre conceitos;
- fluxo de energia, dados, água ou comando;
- topologia elétrica ou rede;
- relação causa/efeito;
- exemplo calculado;
- zona operacional;
- erro comum de campo;
- distinção entre papéis que iniciantes confundem.

## Cobertura atual

- Visuais versionados no repositório: `45`.
- Visuais integrados diretamente em notas técnicas: `45` integrações no total, considerando os 21 visuais da rodada anterior e os 24 novos desta rodada.
- Formatos disponíveis: `svg`, `png` e `md`.
- Pipeline local: `python scripts/visuals/render_visuals.py`.
- Integração em notas: `python scripts/visuals/integrate_visuals.py`.
- Linguagem visual atual: cartilha/infográfico técnico, com mapa de processo, mapa comparativo, raciocínio causa/efeito, painéis de aplicação e cautela.

## Visuais gerados

| Visual | Tipo | Prioridade | Nota principal |
| --- | --- | --- | --- |
| `onda-pura-vs-onda-quadrada` | gráfico comparativo | alta | `Inversora (DC To AC)` |
| `50hz-vs-60hz` | gráfico comparativo | alta | `DC vs AC` |
| `bateria-zona-util-vs-recarga` | faixa operacional | alta | `Tipos de Bateria` |
| `projeto-eletrico-fluxo-entregaveis` | fluxo de projeto | alta | `Projeto Elétrico de Embarcação` |
| `diagrama-unifilar-camadas` | fluxo de leitura | alta | `Diagrama Unifilar` |
| `queda-tensao-cabos-dc` | causa/efeito | alta | `Dimensionamento de Cabos DC` |
| `autonomia-banco-energia-dia` | exemplo calculado | alta | `Dimensionamento de Banco de Baterias` |
| `bancos-bateria-separacao-funcional` | quadro comparativo | alta | `Bancos de Bateria` |
| `bms-camadas-protecao` | arquitetura de controle | alta | `BMS` |
| `shore-power-topologias` | topologia comparativa | alta | `CAIS (Pier) (AC)` |
| `neutro-negativo-pe-bonding` | quadro comparativo | alta | `Neutro, Negativo, Terra, PE, Bonding e DR` |
| `dr-desequilibrio-corrente` | causa/efeito | alta | `Proteção DR` |
| `isolador-galvanico-vs-transformador-isolamento` | quadro comparativo | alta | `Isolador Galvânico - Transformador de Isolamento` |
| `nmea-backbone-drops` | arquitetura de rede | alta | `NMEA 2000 - NMEA 0183` |
| `monitoramento-remoto-vrm-fluxo` | fluxo de dados | média | `Monitoramento Remoto — VRM` |
| `bomba-porao-fluxo-alarme` | fluxo de segurança | alta | `Bomba de Porão` |
| `corrosao-stray-current-causa-efeito` | causa/efeito | alta | `Correntes Parasitas` |
| `usb-12v-queda-ruido-carga` | causa/efeito | média | `USB 12V (Power)` |
| `solar-mppt-banco-cargas` | fluxo de energia | alta | `Placa Solar (DC)` |
| `gerador-ac-rpm-frequencia` | causa/efeito | alta | `Gerador (AC)` |
| `ar-condicionado-marine-fluxo` | fluxo de sistema | média | `Ar-Condicionado Marine` |
| `agua-pressurizada-bomba-acumulador` | fluxo de sistema | média | `Bomba de Água Pressurizada` |
| `ais-vhf-dsc-epirb-camadas` | quadro comparativo | alta | `VHF` |
| `alarme-geral-sensores-acao` | fluxo de segurança | alta | `Sistema de Alarme Geral` |
| `anodo-eletrolise-protecao` | causa/efeito | alta | `Anôdo` |
| `barramento-dc-distribuicao-protecao` | fluxo de distribuição | alta | `Barramento DC` |
| `chaves-gerais-seletoras-isolamento` | fluxo de isolamento | alta | `Chaves Gerais (DC)` |
| `dessalinizador-fluxo-energia-agua` | fluxo energia/água | média | `Dessanilizador` |
| `detectores-co-gas-camadas` | quadro comparativo | alta | `Detector de CO` |
| `disjuntores-dc-ac-diferencas` | quadro comparativo | alta | `Disjuntores (DC) e (AC)` |
| `extintor-automatico-casa-maquinas` | fluxo de segurança | alta | `Extintor Automático` |
| `flap-trim-atuadores-posicao` | fluxo de comando | média | `Flap` |
| `fusivel-protege-cabo` | causa/efeito | alta | `Fusíveis DC` |
| `holding-tank-y-valve-macerador` | fluxo de sistema | média | `Holding Tank` |
| `iluminacao-navegacao-emergencia-camadas` | quadro comparativo | média | `Luz de Tope` |
| `inspecao-cabos-terminais-falhas` | causa/efeito | alta | `Inspeção de Cabos Terminais e Conexões` |
| `lei-ohm-potencia-relacoes` | quadro conceitual | alta | `Lei de Ohm e Cálculos Básicos` |
| `monitor-bateria-shunt-fluxo` | fluxo de medição | alta | `Monitor de Bateria - BMV - Shunt` |
| `multimetro-sequencia-medicao` | fluxo de diagnóstico | alta | `Multímetro e Instrumentos de Medição` |
| `piloto-automatico-sensores-atuador` | fluxo de controle | média | `Piloto Automático` |
| `quadro-ac-dc-camadas` | arquitetura de painel | alta | `Quadro Elétrico e Painel de Distribuição AC-DC` |
| `radar-ais-chartplotter-fusao` | fusão de informação | média | `Chartplotter - GPS - MFD` |
| `sonda-transdutor-eco-leitura` | fluxo de leitura | média | `Sonda - Profundímetro - Sonar` |
| `thruster-guincho-cargas-alta-corrente` | fluxo de alta corrente | alta | `Thruster` |
| `troubleshooting-funil-diagnostico` | funil de diagnóstico | alta | `Troubleshooting` |

## Candidatos por domínio

### `10_Fundamentos_e_Projeto`

- Já cobertos: `DC vs AC`, `Projeto Elétrico`, `Diagrama Unifilar`, `Dimensionamento de Cabos DC`, `Dimensionamento de Banco de Baterias`, `Neutro/Negativo/PE/Bonding/DR`, `Lei de Ohm`, `Multímetro`, `Troubleshooting`, `Inspeção de Cabos Terminais e Conexões`.
- Próximos candidatos: `Simbologia Elétrica Náutica`, exemplos calculados mais específicos de inversor 12V/24V e uma cartilha curta de sequência de comissionamento.

### `20_Baterias_e_Armazenamento`

- Já cobertos: `Tipos de Bateria`, `Bancos de Bateria`, `BMS`, `Monitor de Bateria - BMV - Shunt`.
- Próximos candidatos: `Lítio LiFePO4`, `Carregador de Bateria`, curva simplificada de carga/absorção/flutuação.

### `30_Energia_e_Conversao`

- Já cobertos: `CAIS (Pier) (AC)`, `Inversora`, `Gerador (AC)`, `Placa Solar (DC)`.
- Próximos candidatos: `Alternador (DC)`, `Transformador Entrada`, `Transformador Bivolt`, `Gerador (DC)`, `Eólico (DC)`.

### `40_Distribuicao_Protecao_e_Aterramento`

- Já cobertos: `Proteção DR`, `Isolador Galvânico`, ligação conceitual de `Aterramento/Bonding`, `Barramento DC`, `Fusíveis DC`, `Disjuntores DC/AC`, `Chaves Gerais`, `Quadro Elétrico`.
- Próximos candidatos: cartilha de aterramento/bonding por caso de uso e exemplo visual de seletividade básica.

### `50_Navegacao_Instrumentacao_e_Comunicacao`

- Já cobertos: `NMEA 2000 - NMEA 0183`, `AIS/VHF/DSC/EPIRB`, `Radar/AIS/Chartplotter`, `Piloto Automático`, `Sonda`.
- Próximos candidatos: cartilhas específicas de MMSI/DSC, EPIRB e limites de integração NMEA.

### `55_Iluminacao_e_Sinalizacao`

- Já cobertos: camada geral de `Iluminação de Navegação e Emergência`, integrada inicialmente em `Luz de Tope`.
- Próximos candidatos: `Luz de Âncora`, `Iluminação de Emergência`, `Dimmer`, `Fitas LED` e quadro de setores de visibilidade.

### `60_Automacao_Conectividade_e_Monitoramento`

- Já cobertos: `Monitoramento Remoto — VRM`, `USB 12V (Power)`, `Sistema de Alarme Geral`.
- Próximos candidatos: `Wi-Fi a Bordo`, `Starlink`, `Automação de Bordo`, `Sensor de Nível Diesel`.

### `70_Hidraulica_Climatizacao_e_Utilidades`

- Já cobertos: `Ar-Condicionado Marine`, `Bomba de Porão`, `Bomba de Água Pressurizada`, `Holding Tank`, `Dessalinizador`, `Thruster/Guincho`, `Flap`.
- Próximos candidatos: macerador em detalhe, pressostato/acumulador com exemplo de falha e ciclo de carga de guincho.

### `80_Seguranca_e_Corrosao`

- Já cobertos: `Correntes Parasitas`, `Anôdo`, `Detector de CO`, camada `CO/Gás`, `Extintor Automático`.
- Próximos candidatos: `Detector de Gás GLP/GN` em detalhe, `Alarme de Alagamento`, cartilha de inspeção de corrosão por sintomas.

### `90_Revisao_Manual`

- Ainda sem visual gerado nesta rodada.
- Próximos candidatos: `Estabilizador`, `Motor de Trim - Tilt`.

## Recomendações para a próxima onda

1. Refinar o PNG com renderização tipográfica nativa quando houver dependência local disponível, mantendo SVG como master principal.
2. Criar exemplos calculados específicos: inversor 12V/24V, queda de tensão, autonomia e carregamento.
3. Criar cartilhas visuais de normas e cautelas Brasil-primeiro sem inventar exigência normativa.
4. Criar pacote de publicação: thumbnails, versão vertical para aula/slide e versão compacta para apostila.
5. Revisar visual por visual em lote editorial fino, priorizando os que serão usados em curso/material premium.
