---
title: "Inventário Visual da Base"
note_type: "audit-report"
domain: "_Editorial"
status: "active-inventory"
reviewed_on: "2026-04-15"
review_jurisdiction: "Brasil"
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

- Visuais versionados no repositório: `21`.
- Visuais integrados diretamente em notas técnicas: `21` integrações no total, considerando os 3 visuais da rodada anterior e os 18 novos desta rodada.
- Formatos disponíveis: `svg`, `png` e `md`.
- Pipeline local: `python scripts/visuals/render_visuals.py`.
- Integração em notas: `python scripts/visuals/integrate_visuals.py`.

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

## Candidatos por domínio

### `10_Fundamentos_e_Projeto`

- Já cobertos: `DC vs AC`, `Projeto Elétrico`, `Diagrama Unifilar`, `Dimensionamento de Cabos DC`, `Dimensionamento de Banco de Baterias`, `Neutro/Negativo/PE/Bonding/DR`.
- Próximos candidatos: `Lei de Ohm e Cálculos Básicos`, `Multímetro e Instrumentos de Medição`, `Troubleshooting`, `Inspeção de Cabos Terminais e Conexões`, `Simbologia Elétrica Náutica`.

### `20_Baterias_e_Armazenamento`

- Já cobertos: `Tipos de Bateria`, `Bancos de Bateria`, `BMS`.
- Próximos candidatos: `Monitor de Bateria - BMV - Shunt`, `Lítio LiFePO4`, `Carregador de Bateria`.

### `30_Energia_e_Conversao`

- Já cobertos: `CAIS (Pier) (AC)`, `Inversora`, `Gerador (AC)`, `Placa Solar (DC)`.
- Próximos candidatos: `Alternador (DC)`, `Transformador Entrada`, `Transformador Bivolt`, `Gerador (DC)`, `Eólico (DC)`.

### `40_Distribuicao_Protecao_e_Aterramento`

- Já cobertos: `Proteção DR`, `Isolador Galvânico`, ligação conceitual de `Aterramento/Bonding` via visual de papéis.
- Próximos candidatos: `Aterramento`, `Bonding`, `Barramento DC`, `Fusíveis DC`, `Disjuntores DC/AC`, `Chaves Gerais`, `Quadro Elétrico`.

### `50_Navegacao_Instrumentacao_e_Comunicacao`

- Já coberto: `NMEA 2000 - NMEA 0183`.
- Próximos candidatos: `AIS`, `VHF`, `Radar`, `Piloto Automático`, `Chartplotter`, `Sonda`, `EPIRB/DSC`.

### `55_Iluminacao_e_Sinalizacao`

- Ainda sem visual gerado nesta rodada.
- Próximos candidatos: `Luzes de Navegação`, `Luz de Âncora`, `Iluminação de Emergência`, `Dimmer`, `Fitas LED`.

### `60_Automacao_Conectividade_e_Monitoramento`

- Já cobertos: `Monitoramento Remoto — VRM`, `USB 12V (Power)`.
- Próximos candidatos: `Wi-Fi a Bordo`, `Starlink`, `Automação de Bordo`, `Sistema de Alarme Geral`, `Sensor de Nível Diesel`.

### `70_Hidraulica_Climatizacao_e_Utilidades`

- Já cobertos: `Ar-Condicionado Marine`, `Bomba de Porão`.
- Próximos candidatos: `Bomba de Água Pressurizada`, `Holding Tank`, `Macerador`, `Dessalinizador`, `Thruster`, `Guincho`, `Flap`.

### `80_Seguranca_e_Corrosao`

- Já cobertos: `Correntes Parasitas`.
- Próximos candidatos: `Eletrólise`, `Anôdo`, `Detector de CO`, `Detector de Gás GLP/GN`, `Extintor Automático`, `Alarme de Alagamento`.

### `90_Revisao_Manual`

- Ainda sem visual gerado nesta rodada.
- Próximos candidatos: `Estabilizador`, `Motor de Trim - Tilt`.

## Recomendações para a próxima onda

1. Criar pacote de medição e diagnóstico: multímetro, troubleshooting, inspeção de cabos e shunt.
2. Criar pacote de distribuição DC: barramento, fusíveis, disjuntores, chaves gerais e quadro AC/DC.
3. Criar pacote de navegação/comunicação: AIS, VHF, radar, piloto automático e chartplotter.
4. Criar pacote de segurança: CO, gás, alagamento, extintor e corrosão.
5. Criar pacote de utilidades eletromecânicas: bombas, thruster, guincho, flap e dessalinizador.
