---
title: "Migração de Frontmatter — 2026-04-17"
note_type: "editorial-report"
reviewed_on: "2026-04-17"
---

# Migração de Frontmatter — 2026-04-17

Gerado por `scripts/migrate_frontmatter.py`.

- Arquivos varridos: **152**
- Já migrados (sem ação): **47**
- Pendentes de migração: **104**

## Escopo

- `review_jurisdiction: "escalar"` -> lista YAML
- Campo `normas_citadas` ausente -> populado via varredura regex do corpo
- `reviewed_on` atualizado para a data-alvo quando alguma mudança for aplicada

## Pendentes

### `00_Mapas\Fundamentos da Elétrica Náutica.md`

- `normas_citadas`: adicionar **2** códigos: `NMEA 2000`, `NMEA 0183`
- `reviewed_on`: `` -> `2026-04-17`

### `00_Mapas\Guia da Vault Curada.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `00_Mapas\MOC — Fundamentos e Projeto.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `00_Mapas\MOC — Navegacao Instrumentacao e Comunicacao.md`

- `normas_citadas`: adicionar **2** códigos: `NMEA 2000`, `NMEA 0183`
- `reviewed_on`: `` -> `2026-04-17`

### `10_Fundamentos_e_Projeto\Ferramentas do Eletricista Náutico.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **1** códigos: `NMEA 2000`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `10_Fundamentos_e_Projeto\Lei de Ohm e Cálculos Básicos.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `10_Fundamentos_e_Projeto\Leitura de Diagramas e Esquemas Elétricos.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `10_Fundamentos_e_Projeto\Manutenção Preventiva Elétrica — Checklist.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **2** códigos: `ABYC E-11`, `NORMAM-211`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `10_Fundamentos_e_Projeto\Multímetro e Instrumentos de Medição.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `10_Fundamentos_e_Projeto\Princípios Náuticos.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **1** códigos: `NORMAM-211`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `10_Fundamentos_e_Projeto\Simbologia Elétrica Náutica.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **1** códigos: `IEC 60617`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `10_Fundamentos_e_Projeto\Tipos de Embarcação.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `10_Fundamentos_e_Projeto\Troubleshooting — Diagnóstico de Falhas Elétricas.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **1** códigos: `ABYC E-11`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `10_Fundamentos_e_Projeto\Voltímetro - Amperímetro (DC e AC).md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **4** códigos: `ABYC E-11`, `ISO 13297:2020`, `ABNT NBR 5410`, `NBR 5410`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `20_Baterias_e_Armazenamento\Lítio LiFePO4 — Instalação e Cuidados Específicos.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **2** códigos: `IEC 62619`, `ABYC E-13`
- `reviewed_on`: `2026-04-13` -> `2026-04-17`

### `30_Energia_e_Conversao\Alternador (DC).md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **5** códigos: `ABYC E-11`, `ABYC A-31`, `ISO 13297:2020`, `ABNT NBR 5410`, `NBR 5410`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `30_Energia_e_Conversao\Arranque.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `30_Energia_e_Conversao\Carregador Elétrico para Tender e Jet Ski.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `30_Energia_e_Conversao\Eólico (DC).md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `30_Energia_e_Conversao\Gerador (AC).md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **6** códigos: `ABYC E-11`, `ABYC A-33`, `NFPA 302`, `ABNT NBR 5410`, `NBR 5410`, `NORMAM-211`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `30_Energia_e_Conversao\Gerador (DC).md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `30_Energia_e_Conversao\Transformador Bivolt.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `40_Distribuicao_Protecao_e_Aterramento\Barramento DC - Bus Bar - Distribuição DC.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `40_Distribuicao_Protecao_e_Aterramento\Cabeamento Náutico.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **2** códigos: `NMEA 2000`, `NMEA 0183`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `40_Distribuicao_Protecao_e_Aterramento\Chaves Gerais (DC).md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `40_Distribuicao_Protecao_e_Aterramento\Chaves Seletoras (AC).md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `40_Distribuicao_Protecao_e_Aterramento\Contatores (AC).md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **1** códigos: `IEC 60947-4`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `40_Distribuicao_Protecao_e_Aterramento\Disjuntores (DC) e (AC).md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **6** códigos: `ABYC E-11`, `ABYC E-10`, `ISO 13297:2020`, `IEC 60947-2`, `ABNT NBR 5410`, `NBR 5410`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `40_Distribuicao_Protecao_e_Aterramento\Divisores de Carga (DC).md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `40_Distribuicao_Protecao_e_Aterramento\Fusíveis DC — Proteção Contra Sobrecorrente.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **3** códigos: `ABYC E-11`, `ABNT NBR 5410`, `NBR 5410`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `40_Distribuicao_Protecao_e_Aterramento\Hotline (DC).md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `40_Distribuicao_Protecao_e_Aterramento\Linha Leve (AC).md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `40_Distribuicao_Protecao_e_Aterramento\Linha Pesada (AC).md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `40_Distribuicao_Protecao_e_Aterramento\Quadro Elétrico e Painel de Distribuição AC-DC.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `40_Distribuicao_Protecao_e_Aterramento\Relés e Relés de Estado Sólido.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `40_Distribuicao_Protecao_e_Aterramento\Terminais Conectores e Emendas.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `50_Navegacao_Instrumentacao_e_Comunicacao\AIS (Automatic Identification System).md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **3** códigos: `NMEA 2000`, `NMEA 0183`, `NORMAM-01`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `50_Navegacao_Instrumentacao_e_Comunicacao\Buzina.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **1** códigos: `COLREGS`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `50_Navegacao_Instrumentacao_e_Comunicacao\Bússola Eletrônica (Compass - HDG Sensor).md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **5** códigos: `NMEA 2000`, `ABYC E-11`, `IEC 60945`, `NMEA 0183`, `ISO 11606`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `50_Navegacao_Instrumentacao_e_Comunicacao\Chartplotter - GPS - MFD.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **4** códigos: `NMEA 2000`, `NMEA 0183`, `COLREGS`, `IEC 61162`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `50_Navegacao_Instrumentacao_e_Comunicacao\Dsc — Chamada Seletiva Digital.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **3** códigos: `NMEA 0183`, `NMEA 2000`, `NORMAM-01`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `50_Navegacao_Instrumentacao_e_Comunicacao\EPIRB - Beacon de Emergência.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **1** códigos: `IEC 61097-2`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `50_Navegacao_Instrumentacao_e_Comunicacao\Estação de Vento - Anemômetro.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **4** códigos: `NMEA 0183`, `NMEA 2000`, `ABYC E-11`, `IEC 60945`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `50_Navegacao_Instrumentacao_e_Comunicacao\Mob — Man Overboard — Sistema de Detecção.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **5** códigos: `COLREGS`, `ABYC A-7`, `ISO 15085`, `NORMAM-01`, `IEC 61097-14`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `50_Navegacao_Instrumentacao_e_Comunicacao\Piloto Automático.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **3** códigos: `NMEA 2000`, `COLREGS`, `ABYC E-11`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `50_Navegacao_Instrumentacao_e_Comunicacao\Radar.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **2** códigos: `NMEA 2000`, `COLREGS`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `50_Navegacao_Instrumentacao_e_Comunicacao\Sonda - Profundímetro - Sonar.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **2** códigos: `NMEA 2000`, `ABYC A-28`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `50_Navegacao_Instrumentacao_e_Comunicacao\VHF.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **2** códigos: `NMEA 0183`, `NMEA 2000`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `55_Iluminacao_e_Sinalizacao\Dimmer — Controle de Intensidade Luminosa.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **3** códigos: `NMEA 2000`, `ABYC E-11`, `IEC 61000`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `55_Iluminacao_e_Sinalizacao\Farol de Busca.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **2** códigos: `COLREGS`, `ABYC E-11`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `55_Iluminacao_e_Sinalizacao\Fitas Led - Iluminação Led.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **2** códigos: `ABYC E-11`, `IEC 60529`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `55_Iluminacao_e_Sinalizacao\Iluminação de Emergência a Bordo.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **4** códigos: `ISO 17631`, `ISO 3864`, `IEC 60598-2`, `NORMAM-01`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `55_Iluminacao_e_Sinalizacao\Luz de Cortesia.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **1** códigos: `ABYC E-11`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `55_Iluminacao_e_Sinalizacao\Luz de Âncora.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **3** códigos: `COLREGS`, `NORMAM-01`, `ISO 16180:2011`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `55_Iluminacao_e_Sinalizacao\Luz Subaquática.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `55_Iluminacao_e_Sinalizacao\Luzes Internas Teto.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **2** códigos: `ABYC E-11`, `IEC 60529`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `55_Iluminacao_e_Sinalizacao\Strobo.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `55_Iluminacao_e_Sinalizacao\Tipos de Lâmpadas e LEDs Náuticos.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **1** códigos: `IEC 60529`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `60_Automacao_Conectividade_e_Monitoramento\Atuador Linear.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `60_Automacao_Conectividade_e_Monitoramento\Automação de Bordo — Sistemas Domoticos.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **1** códigos: `NMEA 2000`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `60_Automacao_Conectividade_e_Monitoramento\Câmeras de Bordo - Sistema CFTV.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **1** códigos: `IEC 60529`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `60_Automacao_Conectividade_e_Monitoramento\Interfone - Intercomunicador de Bordo.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `60_Automacao_Conectividade_e_Monitoramento\Sensor de Nível Diesel.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `normas_citadas`: adicionar **2** códigos: `NMEA 2000`, `NMEA 0183`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `60_Automacao_Conectividade_e_Monitoramento\Sistema de Alarme Geral - Painel de Alarmes.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `60_Automacao_Conectividade_e_Monitoramento\Som.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `60_Automacao_Conectividade_e_Monitoramento\Starlink - Internet a Bordo.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `60_Automacao_Conectividade_e_Monitoramento\TV a Bordo - Entretenimento.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `60_Automacao_Conectividade_e_Monitoramento\USB 12V (Power).md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `60_Automacao_Conectividade_e_Monitoramento\Wi-Fi a Bordo — Roteador Marine e Conectividade.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Aquecedor de Bordo - Cabin Heater.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Ar-Condicionado Marine — Sistema Completo.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Blower.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Boiler.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Bomba Ar Condicionado.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Bomba de Banheiro.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Bomba de Porão.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Bomba de Água Pressurizada.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Bomba de Águas Negras.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Caixa de Água Cinza.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Casa de Máquinas e Paiol.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Catraca.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Davit - Munk - Guindaste de Bote - Tender Lift.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Flap.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Fogão - Cooktop Elétrico - Galley.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Geladeira - Freezer de Bordo.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Guincho.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Holding Tank - Y-Valve - Sistema de Esgoto.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Icemaker - Máquina de Gelo.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Limpador de Parabrisas.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Macerador - Bomba de Águas Negras.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Plataforma de Popa Elétrica - Hidráulica.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Sensor de Nível de Água.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `70_Hidraulica_Climatizacao_e_Utilidades\Thruster.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `80_Seguranca_e_Corrosao\Alarme de Alagamento - Sensor de Porão.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `80_Seguranca_e_Corrosao\Anôdo.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `80_Seguranca_e_Corrosao\Detector de CO — Monóxido de Carbono.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `80_Seguranca_e_Corrosao\Detector de Gás GLP - GN.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `80_Seguranca_e_Corrosao\Eletrólise.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `80_Seguranca_e_Corrosao\Extintor Automático — Combate a Incêndio na Casa de Máquinas.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `90_Revisao_Manual\Motor de Trim - Tilt.md`

- `review_jurisdiction`: `escalar:Brasil` -> `['Brasil']`
- `reviewed_on`: `2026-04-14` -> `2026-04-17`

### `_Editorial\Auditoria Geral da Base.md`

- `normas_citadas`: adicionar **2** códigos: `NMEA 2000`, `NMEA 0183`

### `_Editorial\bugs_conhecidos.md`

- `normas_citadas`: adicionar **4** códigos: `ABYC A-28`, `ABNT NBR 13885`, `NBR 13885`, `NMEA 2000`
- `reviewed_on`: `2026-04-16` -> `2026-04-17`

### `_Editorial\convencao_citacao_normativa.md`

- `review_jurisdiction`: `escalar:[Brasil, internacional]` -> `['[Brasil, internacional]']`
- `normas_citadas`: adicionar **10** códigos: `ABYC E-11`, `ISO 13297`, `ISO 13297:2020`, `NORMAM-02`, `NORMAM-211`, `ABYC E-13`, `ABNT NBR 13885`, `NBR 13885`, `ABNT NBR 16033`, `NBR 16033`
- `reviewed_on`: `2026-04-16` -> `2026-04-17`

### `_Editorial\Inventário Visual da Base.md`

- `normas_citadas`: adicionar **2** códigos: `NMEA 2000`, `NMEA 0183`

