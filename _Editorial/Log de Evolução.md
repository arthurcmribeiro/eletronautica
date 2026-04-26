---
title: "Log de Evolução"
note_type: "audit-report"
domain: "_Editorial"
status: "active-log"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
---

# Log de Evolução

## 2026-04-21 — Lote 24 — Promoção do staging para o acervo principal

- Promovidos `26` documentos do `Acervo do humano/10_Tecnico_Nautico` para o `_Acervo_Local` principal com nomes normalizados e pastas coerentes.
- Expandido o bloco `Geradores/Cummins-Onan/` com as famílias:
  - `MDKBH`;
  - `MDKDK`;
  - `MDKDL`;
  - `MDKDM-MDKDN`;
  - `MDKAD-MDKAE-MDKAF`;
  - `Legacy-MDKBK-MDKBN`;
  - `Legacy-MDKBP-MDKBS`;
  - `Legacy-MDKBT-MDKBV`.
- Reforçadas as famílias já abertas `MDKDP-MDKDR-MDKDV` e `MDKDS-MDKDT-MDKDU` com `service manual`.
- Aberta a pasta `Climatizacao/Dometic/Self-Contained` com pacote inicial de `installation/troubleshooting` e `price lists`.
- Criado o bloco `Complementar-Brasil/` no acervo principal para referências técnicas que não entram bem como família de fabricante:
  - `12 Volt Doctors`;
  - `corrosão / eletrólise`;
  - `Volvo Penta`.
- Criado o script `scripts/acervo/promote_human_archive_to_main.py` para repetir a promoção curada sem retrabalho manual.
- Ajustado `scripts/acervo/build_local_index.py` e o `README` do acervo para excluir `Acervo do humano/` do índice principal, preservando o staging bruto separado da biblioteca curada.

## 2026-04-21 — Lote 23 — Organização do Acervo do Humano

- Organizada a pasta `90_Revisao_Manual/_Acervo_Local/Acervo do humano`, limpando a raiz e redistribuindo `599` arquivos em subpastas operacionais.
- Isolado o material fora de escopo ou pessoal em `00_Fora_do_Escopo_ou_Pessoal/` com `204` arquivos.
- Concentrado o material profissional em `10_Tecnico_Nautico/` com `395` arquivos, incluindo:
  - `58` em `01_Geradores/`;
  - `27` em `03_Baterias_e_DC/`;
  - `20` em `05_Navegacao_e_Eletronicos/`;
  - `56` em `09_Propulsao_Motores_Estabilizacao_e_Atuacao/`;
  - `116` em `90_Triagem_Tecnica_por_Codigo/` para PDFs ainda ambíguos pelo nome.
- Preservados em pastas temáticas exemplos estratégicos do acervo humano:
  - `The 12 Volt Doctors Practical Handbook.pdf`;
  - `ELETRÓLISE ... .html`;
  - `CABOS E CONEXÃO RAYMARINE SEATALK.pdf`;
  - `Fundamentos_Eletrica_Nautica_ArthurRibeiro.pdf`.
- Criado o script `scripts/acervo/organize_human_archive.py` para reaplicar a organização em novas rodadas, incluindo correção para caminhos longos no Windows.

## 2026-04-19 — Lote 22 — Shore power, conversão AC e conectores

- Criada a nota `90_Revisao_Manual/Links Confirmados — Shore Power, Conversão AC e Conectores Marinhos`.
- Consolidada uma passada oficial para:
  - `Xantrex / Schneider Electric`;
  - `Charles Industries`;
  - `ProMariner`;
  - `Marinco`;
  - `Hubbell Marine`.
- Promovidas no backlog operacional as linhas:
  - `MAN-B01` para `manual localizado`;
  - `MAN-B03` para `manual localizado`;
  - `MAN-B04` para `manual localizado`;
  - `MAN-B02` para `portal mapeado`;
  - `MAN-B05` para `portal mapeado`.
- Expandida a `Tabela-Mestre do Acervo — Biblioteca de Referência` com o novo bloco:
  - `ACP-001` a `ACP-005`.
- Reforçado o `MOC — Revisao Manual` para incluir a nova nota de captação por bloco funcional.

## 2026-04-14 — Lote 0 — Higiene estrutural da automação

- Confirmado que `scripts/vault_tools.py` estava varrendo o espelho `.claude/worktrees/agitated-hugle`.
- Corrigido o escopo dos scanners para excluir `.claude` e `_visuals`.
- Revalidado o vault real: `140` notas, `0` erros, `0` avisos.
- Regenerado `manifest/content-manifest.json` com o corpus correto.

## 2026-04-14 — Lote 1 — Auditoria editorial da base

- Mapeada a estrutura por domínio, tipo de nota e entrypoints.
- Confirmado que o vault principal não possui notas órfãs reais.
- Identificadas notas pouco integradas:
  - `USB 12V (Power)`
  - `Limpador de Parabrisas`
- Identificados problemas críticos:
  - escopo incorreto dos scripts;
  - ausência de sistema visual versionável;
  - rascunhos úteis presos fora do vault principal.
- Criados:
  - `Auditoria Geral da Base`
  - `Backlog de Evolução Editorial`
  - `Log de Evolução`

## Próximo lote planejado

- Implantar a camada `_visuals/` com specs, gerador e outputs.
- Gerar os três primeiros visuais obrigatórios.
- Reforçar a camada de mapas com hubs transversais e nota de referência rápida.

## 2026-04-14 — Lote 2 — Camada visual inicial e reforço de navegação

- Implantada a estrutura `_visuals/specs/`, `_visuals/generated/` e `scripts/visuals/`.
- Gerados os três primeiros visuais obrigatórios:
  - `onda-pura-vs-onda-quadrada`
  - `50hz-vs-60hz`
  - `bateria-zona-util-vs-recarga`
- Integrados os visuais nas notas:
  - `DC vs AC — Corrente Contínua e Alternada`
  - `Inversora (DC To AC)`
  - `Tipos de Bateria`
- Reforçado `Fundamentos da Elétrica Náutica` com hubs transversais para diagnóstico, segurança e referência rápida.
- Documentada a camada visual no `README.md`.
- Ajustado `.gitignore` para manter `.claude/` e `.obsidian/graph.json` fora do versionamento.

## Próximo lote recomendado

- Revisar `USB 12V (Power)` e `Limpador de Parabrisas` para aumentar integração interna.
- Criar a segunda onda de visuais focada em `shore power`, `bonding`, `DR` e `NMEA`.
- Estender CI para validar geração mínima dos specs visuais.

## 2026-04-15 — Lote 3 — Varredura visual ampla

- Ajustado o template visual para reduzir desalinhamento em títulos longos, resumo e cards de fluxo.
- Acrescentados tipos reutilizáveis ao renderer:
  - `flow_diagram`
  - `comparison_cards`
  - `cause_effect`
- Criadas specs adicionais para cobrir os principais temas visuais da base.
- Renderizados `21` visuais versionados em `svg`, `png` e `md` no total.
- Criado `scripts/visuals/integrate_visuals.py` para inserir blocos visuais em notas-alvo sem duplicação.
- Integrados `18` novos visuais diretamente em notas técnicas.
- Criado `Inventário Visual da Base` com cobertura atual, candidatos por domínio e fila recomendada.

## Próximo lote recomendado

- Criar pacote de medição e diagnóstico: multímetro, shunt, troubleshooting e inspeção.
- Criar pacote de distribuição DC: fusíveis, disjuntores, barramento, quadro e chaves.
- Criar pacote de navegação/comunicação: AIS, VHF, radar, piloto automático e chartplotter.

## 2026-04-15 — Lote 4 — Cartilha visual e segunda onda

- Registrado feedback editorial: os visuais anteriores estavam informativos, mas excessivamente parecidos e com pouca leitura humana aplicada.
- Redesenhado o renderer para linguagem de cartilha/infográfico técnico:
  - `flow_diagram` agora usa mapa de processo com eixo visual, estações numeradas, faixa de aplicação e erros comuns;
  - `comparison_cards` agora usa mapa comparativo radial, painéis de uso prático e leitura rápida;
  - `cause_effect` agora usa raciocínio diagnóstico em faixas progressivas.
- Otimizado o rasterizador local:
  - retângulos passaram a usar escrita por linha em vez de pixel a pixel;
  - PNG passou a ser gerado em resolução lógica 2x para melhorar leitura quando ajustado à tela.
- Criadas e renderizadas `24` novas specs, elevando a cobertura para `45` visuais em `svg`, `png` e `md`.
- Integrados `24` novos visuais em notas-alvo, mantendo idempotência do integrador.
- Atualizados `Inventário Visual da Base`, `Backlog de Evolução Editorial` e este log.

## Próximo lote recomendado

- Fazer revisão visual fina dos SVGs mais estratégicos para curso/apostila.
- Criar exemplos calculados específicos com números de campo e cautela explícita.
- Criar versões verticais/compactas dos melhores infográficos para slide, aula e publicação futura.

## 2026-04-18 — Lote 5 — Higiene final de versionamento

- Revisado o estado pós-rodada com validação estrutural completa: `147` notas, `0` erros, `0` avisos.
- Regenerado `manifest/content-manifest.json` para confirmar consistência do corpus atual.
- Reexecutado o pipeline visual: `45` specs confirmadas, `45` integrações já presentes e `0` notas alteradas pelo integrador.
- Identificado que `.obsidian/graph.json` seguia rastreado apesar de já constar no `.gitignore`.
- Ajustado o versionamento para retirar `graph.json` do Git e evitar ruído local recorrente de layout/zoom do Obsidian.

## 2026-04-19 — Lote 6 — Mapa inicial do acervo de manuais

- Criada a nota `90_Revisao_Manual/Acervo de Manuais — Marcas e Modelos Prioritários` para consolidar marcas e famílias de modelos recorrentes na base.
- Estruturada a priorização por três frentes:
  - energia e gestão elétrica;
  - navegação, comunicação e segurança;
  - iluminação, sinalização e acessórios de casco.
- Mapeados portais oficiais de manuais e suporte para as marcas mais relevantes do corpus.
- Integrado o novo inventário ao `MOC — Revisao Manual`.
- Revalidada a vault após as edições: `148` notas, `0` erros, `0` avisos.
- Regenerado `manifest/content-manifest.json` para refletir o corpus atualizado.

## 2026-04-19 — Lote 7 — Varredura completa do corpus para marcas e modelos

- Confirmado que a rodada anterior era priorizada e não exaustiva; executada nova varredura integral do corpus versionado.
- Escopo consolidado da checagem:
  - `193` arquivos Markdown versionados no Git;
  - `148` notas reconhecidas pela validação estrutural da vault;
  - `22` notas com seção explícita de marcas/modelos, mais notas complementares fora dessas seções.
- Criada a nota `90_Revisao_Manual/Inventário Completo — Marcas e Modelos Citados no Corpus` com consolidação por domínio e por nota-fonte.
- Atualizada a nota priorizada para apontar explicitamente para o inventário completo.
- Reforçado o `MOC — Revisao Manual` com as duas camadas de navegação:
  - inventário completo do corpus;
  - fila priorizada de coleta de manuais.

## 2026-04-19 — Lote 8 — Backlog operacional de coleta de manuais

- Criada a nota `90_Revisao_Manual/Backlog Operacional — Coleta de Manuais` como camada executável para busca, download e curadoria.
- Estruturado backlog com:
  - `ID` por item;
  - prioridade por lote;
  - categoria;
  - marca;
  - modelos / famílias-alvo;
  - tipo de manual alvo;
  - `url oficial`;
  - `coleta`;
  - `curadoria`.
- Separadas as frentes em três níveis:
  - `Lote A` para coleta imediata;
  - `Lote B` para segunda rodada;
  - `Lote C` para long tail, apoio técnico e realidade Brasil-primeiro.
- Integrada a nova camada ao `MOC — Revisao Manual` e à nota `Acervo de Manuais — Marcas e Modelos Prioritários`.
- Deixada rotina operacional explícita para futura exportação da tabela para Notion ou Base44.
- Mapeados na própria fila operacional portais oficiais adicionais para itens de maior retorno:
  - `Actisense`, `Maretron`, `Standard Horizon` e `Starlink` no `Lote A`;
  - `Xantrex`, `Charles Industries`, `Battle Born`, `ACR`, `Ocean Signal`, `B&G`, `Lumitec`, `Navisafe` e `Quick` no `Lote B`.

## 2026-04-19 — Lote 9 — Links oficiais confirmados do Lote A

- Criada a nota `90_Revisao_Manual/Links Oficiais Confirmados — Lote A` para concentrar URLs oficiais específicas já confirmadas no primeiro lote.
- Consolidada uma camada prática de links para `22` linhas do `Lote A`, cobrindo:
  - energia e gestão elétrica;
  - navegação, comunicação e instrumentação;
  - iluminação e conectividade.
- Promovidas as linhas do `Lote A` de `portal mapeado` para `manual localizado` no backlog operacional.
- Registradas ressalvas explícitas onde a família está coberta, mas um submodelo legado ainda merece rodada própria:
  - `MaraTron` dentro do ecossistema Mastervolt;
  - `GHP 12 / GHP 12R / GMC 010` dentro da linha Garmin;
  - variações de locale para alguns materiais Garmin e Raymarine.
- Integradas as novas referências ao `MOC — Revisao Manual`, ao inventário completo e à nota priorizada.

## 2026-04-19 — Lote 10 — Camada source-first e matriz inicial de geradores

- Criada a nota `90_Revisao_Manual/Matriz de Fontes — Fabricantes e Repositórios` para mapear a camada `source-first` do acervo.
- Classificadas as fontes em:
  - `fonte oficial primária`;
  - `fonte oficial secundária`;
  - `espelho externo`.
- Normalizados aliases críticos de busca:
  - `Kohler Marine -> Rehlko Marine`;
  - `Onan -> Cummins / Cummins Onan`;
  - `Cruisair -> Dometic`;
  - `Marine Air -> Dometic`;
  - `Rule / Jabsco -> Xylem`.
- Criada a nota `90_Revisao_Manual/Matriz de Modelos e Versões — Geradores` para organizar a pesquisa de `Cummins Onan` e `Rehlko/Kohler`.
- Consolidada primeira camada de famílias e códigos úteis para geradores:
  - `MDKBH`, `MDKBJ`, `MDKBW`, `MDKDL`, `MDKDK`, `MDKDM`, `MDKDN`, `MDKDP`, `MDKDR`, `MDKDT`, `MDKDU`, `MDKDS`;
  - séries atuais `5EFKOD`, `6EKOD`, `7EFKOZD`, `13.5EFKOZD`, `17EFKOZD`, `20.5EFKOZD`, `28EFKOZD`, `35EFKOZD`, `EFOZDJ`.
- Expandido o backlog operacional com novas frentes para:
  - `Cummins / Onan`;
  - `Rehlko / Kohler Marine`;
  - `Dometic / Cruisair / Marine Air`;
  - `Jabsco / Rule`;
  - `VETUS`.
- Atualizadas as notas de acervo, inventário e o `MOC — Revisao Manual` para apontar para a nova camada de pesquisa por fonte e por versão.

## 2026-04-19 — Lote 11 — Dometic por subgrupos, marcas-matriz e catálogos

- Criada a nota `90_Revisao_Manual/Matriz Dometic — Subgrupos, Linhas e Documentos`.
- Formalizada a leitura correta de `Dometic` como marca-matriz e de `Cruisair`, `Condaria` e `Marine Air` como linhas históricas internas.
- Separados dentro da Dometic os subgrupos que realmente importam para o acervo:
  - climatização;
  - displays, controles e painéis;
  - bombas;
  - steering / marine control;
  - sanitário e holding;
  - conforto e galley.
- Criada a nota `90_Revisao_Manual/Matriz de Marcas Matriz — Ecossistemas e Subgrupos` para expor outros grupos com lógica parecida:
  - `Cummins / Onan`;
  - `Rehlko / Kohler`;
  - `Xylem / Rule / Jabsco`;
  - `VETUS`.
- Incorporada a camada de `catálogos`, `guides`, `brochures`, `portfolio` e `pocket guide` ao sistema de fontes e ao backlog.
- Reestruturado o backlog operacional para desdobrar a Dometic em frentes próprias:
  - `MAN-B33` climate;
  - `MAN-B36` marine control;
  - `MAN-B37` pumps and controls;
  - `MAN-B38` sanitation e conforto.
- Reforçado que `catálogo corporativo` também entra como ativo do acervo de referência, e não apenas `manual de instalação/operação`.

## 2026-04-19 — Lote 12 — Regra do pacote triplo para geradores

- Formalizada a regra de curadoria para geradores: a coleta mínima útil passa a exigir `manual de serviço + manual operacional + parts manual`.
- Atualizadas as linhas `MAN-B31` e `MAN-B32` para refletir explicitamente o pacote triplo como alvo principal.
- Ajustada a matriz de geradores para registrar:
  - quais documentos são obrigatórios;
  - quais documentos são complementares;
  - o campo operacional `pacote triplo conferido`.
- Reforçado no backlog que `installation manual`, `spec sheet`, `brochure` e `product guide` seguem importantes, mas não substituem o trio principal.

## 2026-04-19 — Lote 13 — Tabela-mestre da biblioteca e primeira carga de geradores

- Criada a nota `90_Revisao_Manual/Tabela-Mestre do Acervo — Biblioteca de Referência` como núcleo operacional da biblioteca.
- Definidos campos centrais para o acervo:
  - `grupo_matriz`;
  - `marca`;
  - `alias`;
  - `subgrupo`;
  - `familia_codigos`;
  - `spec_rev`;
  - `service`, `operacao`, `parts`, `installation`;
  - `catalogo_guide`;
  - `fonte_oficial`, `fonte_espelho`;
  - `pacote_triplo`;
  - `pasta_sugerida`.
- Carregada a primeira leva de geradores na tabela-mestre, cobrindo famílias de:
  - `Cummins / Onan`;
  - `Rehlko / Kohler Marine`.
- Registrados na tabela sinais já úteis de `espelho localizado` para alguns casos, sem confundir isso com fechamento oficial do pacote triplo.
- Integradas a nova tabela ao `MOC — Revisao Manual`, ao backlog operacional, à nota priorizada e à matriz de geradores.

## 2026-04-19 — Lote 14 — Refinamento de geradores: 6EKOD e quebra do bloco QD 40–110

- Refinada a linha `GEN-010` na `Tabela-Mestre do Acervo — Biblioteca de Referência` com leitura mais precisa de:
  - `service manual`;
  - `operation manual`;
  - `installation manual`;
  - trilha oficial de `parts`.
- Registrado que o `6EKOD` já tem base documental forte em espelho:
  - `TP-6774` para `service`;
  - `TP-6772` para `operation`;
  - instalação em espelho;
  - rota oficial de `parts` e `Pocket Guide` no ecossistema Rehlko.
- Substituída a antiga linha genérica `QD 40-110` por três subfamílias operacionais na tabela-mestre:
  - `QD 40/45/50/55/58 kW`;
  - `QD 65/80 kW`;
  - `QD 73/80/85/98/99/110 kW`.
- Atualizada a `Matriz de Modelos e Versões — Geradores` para refletir essa quebra mais útil para busca por código, potência, frequência e fase.
- Repriorizado o próximo passo operacional:
  - fechar `parts manual` do `6EKOD`;
  - trabalhar `Cummins Onan` por subfamília, e não mais pelo bloco genérico `40-110`.

## 2026-04-19 — Lote 15 — Escopo náutico estrito e avanço por blocos

- Formalizado nas notas centrais que a biblioteca deve priorizar somente `mercado náutico`.
- Registrado que linhas `RV`, `residenciais`, `standby` e `industriais terrestres` não entram como núcleo do acervo.
- Reescrita a estratégia operacional para `geradores`:
  - avançar por `blocos náuticos de família/plataforma`;
  - usar `modelo exato` só quando a separação documental realmente exigir.
- Atualizadas a `Tabela-Mestre do Acervo — Biblioteca de Referência`, a `Matriz de Modelos e Versões — Geradores` e o `Backlog Operacional — Coleta de Manuais` para refletir:
  - foco náutico estrito;
  - blocos `Cummins / Onan` pequeno, médio e grande;
  - blocos `Rehlko / Kohler Marine` pequeno, médio, médio-alto e grande.

## 2026-04-19 — Lote 16 — Onan por código de conjunto e camada de motor-base

- Reorientada a leitura de `Cummins / Onan` para `código de conjunto`, e não mais para o rótulo comercial `QD` como chave principal.
- Expandido o escopo operacional de `Onan` para cobrir:
  - todos os `MDK` marinhos possíveis nesta passada;
  - o bloco grande `MDDC*`;
  - o legado digital `MDKBK` até `MDKBV`.
- Atualizado o `MAN-B31` no backlog para tratar `MDK + MDDC` como universo náutico de coleta, com levantamento obrigatório de:
  - `motor-base / modelo do motor`;
  - `cilindros`.
- Refinada a `Matriz de Modelos e Versões — Geradores` para distinguir melhor:
  - famílias `MDK` pequenas e médias;
  - bloco grande `MDDC`;
  - literatura atual versus literatura marinha legada.
- Ajustada a `Tabela-Mestre do Acervo — Biblioteca de Referência` para deixar mais honesta a leitura do bloco grande `Onan`, registrando onde a literatura ainda mistura plataformas `4` e `6 cilindros` por `código`, `ano` e `spec`.

## 2026-04-19 — Lote 17 — Regra-mãe da biblioteca de referência

- Criada a nota `_Editorial/Padrão da Biblioteca de Referência Técnica` para congelar o padrão de construção do acervo.
- Formalizadas as regras permanentes de:
  - escopo náutico;
  - hierarquia de fontes;
  - camadas da biblioteca;
  - campos mínimos obrigatórios;
  - pacote documental por tipo;
  - critério de `pronto`;
  - estrutura de pasta e nomeação de arquivo;
  - fluxo operacional e validação final.
- Integrado o novo padrão ao `MOC — Revisao Manual`, à `Tabela-Mestre do Acervo — Biblioteca de Referência` e ao `Backlog Operacional — Coleta de Manuais`.
- Registrado explicitamente que futuras rodadas da biblioteca devem nascer já aderentes a esse padrão, para manter consistência técnica, curadoria funcional e preparo para automação.

## 2026-04-19 — Lote 18 — Checklist operacional de abertura de família

- Criada a nota `90_Revisao_Manual/Checklist Operacional — Abertura de Nova Família do Acervo` para transformar o padrão da biblioteca em rotina prática de execução.
- Estruturada a checklist com etapas de:
  - enquadramento correto;
  - normalização de nome;
  - camada de fontes;
  - estrutura técnica mínima;
  - pacote documental;
  - registro nas notas centrais;
  - estrutura local do acervo;
  - critério de fechamento.
- Integrada a checklist ao `Padrão da Biblioteca de Referência Técnica`, ao `MOC — Revisao Manual` e às notas centrais de matrizes, para que novas rodadas da biblioteca já comecem com regra e checklist lado a lado.

## 2026-04-19 — Lote 19 — Captação real de geradores pequenos e médios

- Integrada ao sistema a nota `90_Revisao_Manual/Links Confirmados — Geradores Pequenos (Onan e Rehlko)`, consolidando a primeira leva real de links exatos para:
  - `MDKBH`, `MDKBJ/BW`, `MDKDK/DL/DM/DN`;
  - `5EFKOD`, `6EKOD`, `7EFKOZD`.
- Criada a nota `90_Revisao_Manual/Links Confirmados — Geradores Médios (Onan MDKDP a MDKDU)` para abrir a segunda leva real de captação do bloco `MDKDP`, `MDKDR`, `MDKDV`, `MDKDS`, `MDKDT` e `MDKDU`.
- Atualizada a `Tabela-Mestre do Acervo — Biblioteca de Referência` para refletir:
  - `status documental` real por família;
  - fechamento do `pacote triplo` onde `service + operacao + parts` já foram localizados;
  - ajuste de `motor_base / cilindros` nos blocos médios `GEN-006` e `GEN-007`;
  - correção da leitura operacional dos blocos pequenos `GEN-001` a `GEN-005` e `GEN-012` a `GEN-014`.
- Reforçado no `MOC — Revisao Manual` o caminho prático da captação já aberta para geradores, para que a biblioteca continue avançando por blocos náuticos e não por PDFs soltos.

## 2026-04-19 — Lote 20 — Captação real de Dometic, Xylem e VETUS

- Criada a nota `90_Revisao_Manual/Links Confirmados — Dometic Marine (Climate, Controls e Sanitário)` para consolidar a primeira leva real de captura em:
  - `climate self-contained`;
  - `MagDrive`;
  - `Optimus displays/controls`;
  - `MasterFlush`.
- Criada a nota `90_Revisao_Manual/Links Confirmados — Xylem e VETUS (Bombas, Toilets, Searchlights e Thrusters)` para consolidar a primeira leva real de captura em:
  - `Rule bilge, dry bilge e float switches`;
  - `Jabsco toilets, cooling pumps e searchlights`;
  - `VETUS bow thrusters e thruster panels`.
- Atualizado o `Backlog Operacional — Coleta de Manuais` para promover as linhas `MAN-B28`, `MAN-B33`, `MAN-B34`, `MAN-B36`, `MAN-B37` e `MAN-B38` de `portal mapeado` para `manual localizado`.
- Expandida a `Tabela-Mestre do Acervo — Biblioteca de Referência` com a primeira camada operacional nao geradores, abrindo linhas para:
  - `Dometic`;
  - `Rule/Jabsco`;
  - `VETUS`.
- Reforçado o `MOC — Revisao Manual` com as novas notas de links confirmados, para que a biblioteca avance também em climatização, sanitário, bombas e thrusters.

## 2026-04-19 — Lote 21 — Captação real de segurança e iluminação

- Criada a nota `90_Revisao_Manual/Links Confirmados — Segurança e Iluminação Náutica` para consolidar a primeira leva real de captura em:
  - `ACR` para `EPIRB` e `PLB`;
  - `Ocean Signal` para `EPIRB`, `PLB` e `MOB`;
  - `Lumitec` para `underwater lights` e `lighting control`.
- Atualizado o `Backlog Operacional — Coleta de Manuais` para promover `MAN-B13`, `MAN-B15` e `MAN-B24` de `portal mapeado` para `manual localizado`.
- Expandida a `Tabela-Mestre do Acervo — Biblioteca de Referência` com a primeira camada operacional de:
  - `SAFE-001` para `ACR`;
  - `SAFE-002` para `Ocean Signal`;
  - `LIT-001` para `Lumitec`.
- Reforçado o `MOC — Revisao Manual` para que a biblioteca avance também em `segurança de emergência`, `MOB`, `EPIRB/PLB` e `controle de iluminação`.

## 2026-04-19 — Lote 23 — Fechamento de Hubbell e abertura de estabilização

- Refinada a nota `90_Revisao_Manual/Links Confirmados — Shore Power, Conversão AC e Conectores Marinhos`.
- Consolidada a trilha oficial da `Hubbell Marine` com:
  - `spec sheets` por `catalog ID`;
  - `installation instructions search`;
  - PDF oficial aberto para a linha internacional `16 A / 32 A`.
- Promovida a linha `MAN-B05` para `manual localizado`.
- Criada a nota `90_Revisao_Manual/Links Confirmados — Estabilização Náutica (Seakeeper Ride)`.
- Promovida a linha `MAN-B30` para `manual localizado`.
- Expandida a `Tabela-Mestre do Acervo — Biblioteca de Referência` com:
  - refinamento de `ACP-005`;
  - novo bloco `STAB-001`.
- Reforçado o `MOC — Revisao Manual` para incluir a nova frente de estabilização.

## 2026-04-19 — Lote 24 — Quick Marine Lighting e controles

- Criada a nota `90_Revisao_Manual/Links Confirmados — Quick Marine Lighting e Controles` para consolidar a trilha oficial de:
  - `QNN`;
  - `QNN Gateway`;
  - `QCC`;
  - `ZDIM 100`;
  - `HDIM 300 PLUS`;
  - `LDIM BUS`.
- Promovida a linha `MAN-B29` para `manual localizado`.
- Expandida a `Tabela-Mestre do Acervo — Biblioteca de Referência` com o bloco `LIT-002`.
- Reforçado o `MOC — Revisao Manual` para incluir a nova frente de `Quick Marine Lighting`.


## 2026-04-19 ? Lote 25 ? B&G vela, vento e instrumentacao

- Criada a nota `90_Revisao_Manual/Links Confirmados ? B&G Vela, Vento e Instrumentacao`.
- Consolidada a trilha oficial da `B&G` para:
  - `Triton2`;
  - `WS310`;
  - `Precision-9`;
  - `WTP3`.
- Promovida a linha `MAN-B20` para `manual localizado`.
- Atualizado o `Acervo de Manuais ? Marcas e Modelos Priorit?rios` para registrar `WTP1` como citado no corpus e `WTP3` como linha oficial atual.
- Expandida a `Tabela-Mestre do Acervo ? Biblioteca de Refer?ncia` com o bloco `NAV-001`.
- Refor?ado o `MOC ? Revisao Manual` para incluir a nova frente de instrumentacao de vela da `B&G`.


## 2026-04-19 ? Lote 26 ? Climatizacao marinha fora da Dometic

- Criada a nota `90_Revisao_Manual/Links Confirmados ? Climatizacao Marinha (Webasto, Mabru e FRIGOMAR)`.
- Expandido o backlog com `MAN-B39`, `MAN-B40` e `MAN-B41` para `Webasto`, `Mabru` e `FRIGOMAR`.
- Expandida a `Tabela-Mestre do Acervo ? Biblioteca de Refer?ncia` com `CLI-001`, `CLI-002` e `CLI-003`.
- Atualizado o `Acervo de Manuais ? Marcas e Modelos Priorit?rios` para incluir as novas frentes de climatiza??o marinha.
- Refor?ada a `Matriz de Fontes ? Fabricantes e Reposit?rios` para ampliar a camada `source-first` de climatiza??o al?m da `Dometic`.
- Refor?ado o `MOC ? Revisao Manual` com a nova frente de climatiza??o marinha.

## 2026-04-19 — Lote 27 — Portal do acervo e frente nacional de climatização

- Criada a nota `90_Revisao_Manual/Portal do Acervo — Biblioteca de Referência` como camada simples de acesso humano para a biblioteca.
- Criado o ponto físico `90_Revisao_Manual/_Acervo_Local/README.md` para separar `links confirmados` de `PDF baixado`.
- Criada a nota `90_Revisao_Manual/Links Confirmados — Climatização Náutica Nacional (H-Tec, Gelotec e Schutz)`.
- Expandido o backlog com:
  - `MAN-B42` para `H-Tec`;
  - `MAN-C15` para `Gelotec`;
  - `MAN-C16` para `Schutz` em validação.
- Expandida a `Tabela-Mestre do Acervo — Biblioteca de Referência` com `CLI-004` para `H-Tec`.
- Atualizados:
  - `Acervo de Manuais — Marcas e Modelos Prioritários`;
  - `Matriz de Fontes — Fabricantes e Repositórios`;
  - `Padrão da Biblioteca de Referência Técnica`;
  - `MOC — Revisao Manual`.
- Formalizada a distinção operacional entre:
  - `estrutura de consulta`;
  - `link confirmado`;
  - `manual localizado`;
  - `acervo local baixado`.

## 2026-04-19 — Lote 28 — Primeiros PDFs no acervo local

- Criadas as primeiras pastas físicas em `90_Revisao_Manual/_Acervo_Local/Climatizacao/` para:
  - `H-Tec/HFC-Acqua`;
  - `Mabru/Self-Contained-DC-VI`.
- Baixado o brochure institucional da `H-Tec` para o acervo local.
- Baixado o `Mabru Marine Air Conditioner Installation Manual 2025` para o acervo local.
- Criada a nota `90_Revisao_Manual/Acervo Local — Índice Inicial` para expor os primeiros arquivos já salvos.
- Atualizados:
  - `Portal do Acervo — Biblioteca de Referência`;
  - `Acervo Local — README`;
  - `Backlog Operacional — Coleta de Manuais`;
  - `Tabela-Mestre do Acervo — Biblioteca de Referência`;
  - `MOC — Revisao Manual`.

## 2026-04-19 — Lote 29 — Primeiros manuais de gerador no acervo local

- Criadas as pastas físicas:
  - `90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDP-MDKDR-MDKDV`;
  - `90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDS-MDKDT-MDKDU`.
- Baixados para o acervo local:
  - `parts manual A046L892` da família `MDKDP-MDKDR-MDKDV`;
  - `parts manual A046J604` da família `MDKDS-MDKDT-MDKDU`;
  - `installation manual A046J598` para as duas famílias.
- Criada a nota `90_Revisao_Manual/Acervo Local — Geradores Iniciais (Cummins Onan)` para expor a primeira vitrine de geradores.
- Atualizados:
  - `Acervo Local — Índice Inicial`;
  - `Portal do Acervo — Biblioteca de Referência`;
  - `Tabela-Mestre do Acervo — Biblioteca de Referência`;
  - `MOC — Revisao Manual`.
- Mantida a leitura honesta:
  - `parts` e `installation` já baixados;
  - `service` e `operator` ainda pendentes de captura limpa no terminal.

## 2026-04-19 — Lote 30 — Camada Python operacional do acervo

- Criados os scripts:
  - `scripts/acervo/download_queue.py`;
  - `scripts/acervo/build_local_index.py`.
- Formalizada a fila estruturada em `90_Revisao_Manual/_Acervo_Local/acervo-download-queue.json`.
- Gerado o relatório automático `90_Revisao_Manual/_Acervo_Local/acervo-download-report.json`.
- Gerado o índice de disco:
  - `90_Revisao_Manual/_Acervo_Local/acervo-local-index.json`;
  - `90_Revisao_Manual/Acervo Local — Índice Gerado.md`.
- Integrados os novos artefatos operacionais em:
  - `Portal do Acervo — Biblioteca de Referência`;
  - `Acervo Local — README`;
  - `Acervo Local — Índice Inicial`;
  - `MOC — Revisao Manual`;
  - `Padrão da Biblioteca de Referência Técnica`.
- Primeira rodada Python concluída sem erro:
  - `6` itens processados na fila;
  - `6` arquivos válidos já reconhecidos como existentes;
  - `0` erros.

## 2026-04-19 — Lote 31 — Banco integral de marcas, normas e fila source-first

- Criada a taxonomia editável `scripts/acervo/acervo_taxonomy.json` com:
  - `marcas`;
  - `submarcas`;
  - `produtos/famílias`;
  - `domínios`;
  - `seed URLs`.
- Criados os scripts:
  - `scripts/acervo/build_brand_norm_bank.py`;
  - `scripts/acervo/build_manual_resolution_queue.py`;
  - `scripts/acervo/resolve_manual_links.py`.
- Gerado o banco integral em:
  - `90_Revisao_Manual/_Dados_Acervo/brand-norm-bank.json`;
  - `90_Revisao_Manual/Banco de Marcas e Normas Citadas — Corpus Integral.md`.
- Gerada a fila `source-first` em:
  - `90_Revisao_Manual/_Dados_Acervo/manual-resolution-queue.json`;
  - `90_Revisao_Manual/Preparação Source-First — Resolver de Links Oficiais.md`.
- Executado `dry-run` do resolvedor sem acesso à rede para validar a estrutura futura:
  - `90_Revisao_Manual/_Dados_Acervo/manual-resolution-results.json`.
- Registrada a camada de verificação normativa oficial em:
  - `90_Revisao_Manual/Matriz de Normativas Citadas — Verificação Oficial.md`.
- Resultados centrais desta rodada:
  - `174` notas analisadas;
  - `52` marcas/submarcas operacionais na taxonomia;
  - `53` produtos/famílias na taxonomia;
  - `44` normas específicas detectadas no corpus;
  - `52` itens prontos na fila de resolução futura.

## 2026-04-20 — Lote 32 — Piloto source-first aplicado em Onan

- Reforçada a taxonomia `scripts/acervo/acervo_taxonomy.json` para `Onan` com:
  - `source_layers.official`;
  - `source_layers.secondary`;
  - `source_layers.mirror`;
  - `curated_candidates` por família e tipo documental.
- Reescrito `scripts/acervo/build_manual_resolution_queue.py` para:
  - carregar camadas de fonte;
  - separar `seed_urls` por prioridade;
  - expor `curated_candidates` na fila;
  - atualizar a nota `Preparação Source-First — Resolver de Links Oficiais`.
- Reescrito `scripts/acervo/resolve_manual_links.py` para:
  - registrar `source_tier`;
  - ordenar resultados por `official -> secondary -> mirror`;
  - normalizar URLs de espelho;
  - reconhecer `PDF direto` sem baixar arquivo;
  - incorporar candidatos curados quando o site oficial bloquear o crawler.
- Executado o piloto `Onan` sem download em:
  - `90_Revisao_Manual/_Dados_Acervo/manual-resolution-results-onan.json`.
- Criada a nota humana do piloto:
  - `90_Revisao_Manual/Aplicação Piloto — Onan (Resolver Source-First).md`.
- Integrados os acessos no:
  - `90_Revisao_Manual/Portal do Acervo — Biblioteca de Referência`;
  - `00_Mapas/MOC — Revisao Manual`.
- Resultado prático do piloto:
  - `26` candidatos úteis;
  - `13` oficiais;
  - `9` secundários;
  - `4` espelhos;
  - `0` desconhecidos.
- Mantida a premissa desta etapa:
  - `nenhum PDF baixado`.

## 2026-04-21 â€” Lote 33 â€” Renomeação do acervo principal para busca

- Ajustado o padrão de nomes dos PDFs promovidos do `Acervo do humano` para melhorar busca local por:
  - `família/código`;
  - `tipo documental`;
  - `contexto técnico`.
- Criado o script reaplicável:
  - `scripts/acervo/rename_acervo_files_for_search.py`.
- Atualizado `scripts/acervo/promote_human_archive_to_main.py` para que os próximos lotes já entrem com nomes revisados.
- Normalizados os nomes mais frágeis do acervo principal, com foco em:
  - `Cummins Onan` legado;
  - documentos marcados apenas como `mirror`;
  - referências complementares de `12 V`, `corrosão/eletrolise` e `Dometic`.
- Mantida a estrutura oficial `Sistema/Marca/Família`, sem reabrir a triagem do staging bruto.

## 2026-04-21 — Lote 34 — Fechamento operacional da etapa do acervo

- Organizado o fluxo desta etapa no `README` do acervo local com a sequência:
  - `staging bruto`;
  - `promoção`;
  - `renomeação`;
  - `índice`;
  - `manifesto`;
  - `validação`.
- Registrada a convenção complementar de nome para o sufixo `legacy-espelho`.
- Criado o verificador reaplicável `scripts/check_python_scripts.py` para compilar todos os scripts Python da pasta `scripts/` sem executar rotinas destrutivas.

## 2026-04-21 — Lote 35 — Promoção de navegação e eletrônicos

- Promovido novo lote técnico do staging para o acervo principal com foco em `Navegacao/`.
- Estruturados blocos claros por marca e família:
  - `Raymarine/SeaTalk`;
  - `Raymarine/Quantum`;
  - `Raymarine/SmartPilot-ST6002`;
  - `Furuno/FI-5002`;
  - `Furuno/CAN-Bus`;
  - `Garmin/GPS-17x-HVS`;
  - `Garmin/GPSMAP-4000-5000`;
  - `Garmin/GHC-50`;
  - `Standard-Horizon/GX2000-GX2150`.
- Mantido o padrão de nome forte para busca por:
  - marca;
  - família/modelo;
  - tipo documental;
  - contexto técnico.

## 2026-04-21 — Lote 36 — Governança do bloco de navegação promovido

- Expandida a `Tabela-Mestre do Acervo` para refletir o que ja entrou no acervo principal em:
  - `Raymarine/SeaTalk`;
  - `Raymarine/Quantum`;
  - `Raymarine/SmartPilot-ST6002`;
  - `Furuno/FI-5002`;
  - `Furuno/CAN-Bus`;
  - `Garmin/GPSMAP-4000-5000`;
  - `Garmin/GPS-17x-HVS`;
  - `Garmin/GHC-50`;
  - `Standard-Horizon/GX2000-GX2150`.
- Atualizado o backlog operacional para marcar esse material como `parcial em acervo local`, mantendo visivel o que ainda falta fechar por familia.
- Preservado o criterio desta etapa:
  - primeiro consolidar o que ja foi promovido;
  - depois aprofundar por `operacao`, `instalacao`, `parts` e variantes oficiais.

## 2026-04-21 — Lote 37 — Primeira passada Kohler / Rehlko no acervo principal

- Promovido para o acervo principal o `service manual` compartilhado `TP-6774 (2/14a)` da linha `Kohler / Rehlko`, a partir do staging tecnico por codigo.
- O manual foi encaixado nas familias que ja estavam mapeadas na governanca:
  - `5EFKOD`;
  - `6EKOD`;
  - `7EFKOZD`;
  - `9-13.5-EKOZD-EFKOZD` como cobertura parcial do subconjunto `9-11EKOZD` / `7-9EFKOZD`.
- Atualizada a `Tabela-Mestre` para refletir o novo status de `service` nesse bloco e movido `MAN-B32` para `parcial em acervo local`.
- Mantida separada, por enquanto, a ficha tecnica `9EOZD / 7EFOZD`:
  - o documento e util;
  - mas pede governanca propria antes de entrar no acervo principal curado.

## 2026-04-22 - Lote 38 - Camada companheira dos PDFs e drenagem da triagem tecnica

- Criada a camada espelhada `90_Revisao_Manual/_Acervo_Notas/` para funcionar como trilha rastreavel dos PDFs do acervo principal, com `46` notas companheiras em Markdown.
- Refeito `scripts/acervo/build_pdf_companion_notes.py` para extrair texto com `pdftotext` quando houver texto real no PDF, cair para `pdf-stream-strings` apenas como fallback e montar nota padrao com:
  - fonte;
  - sinais principais;
  - trechos indexaveis;
  - acoes sugeridas.
- Adicionado `scripts/acervo/pdf_text_tools.py` como base reaproveitavel da leitura textual dos PDFs.
- Atualizado `scripts/acervo/promote_human_archive_to_main.py` para que novas promocoes do staging possam disparar automaticamente a geracao das notas companheiras.
- Organizada em lote a raiz de `90_Triagem_Tecnica_por_Codigo`, que saiu de `116` arquivos soltos para subpastas tematicas:
  - `01_Geradores_e_Motores_Base`: `7`;
  - `02_Navegacao_Comunicacao_e_Instrumentos`: `5`;
  - `03_Propulsao_Motores_e_Turbo`: `22`;
  - `04_DC_Componentes_e_Controle`: `5`;
  - `05_Bombas_Utilidades_e_Acessorios`: `8`;
  - `06_Artigos_Normas_e_Referencia_Tecnica`: `8`;
  - `07_Imagens_e_Recortes_Tecnicos`: `10`;
  - `99_Fora_do_Escopo_ou_Pessoal`: `11`;
  - `ZZ_Residual_Manual`: `32`;
  - `98_Duplicatas`: `8`.
- Mantido o principio de seguranca desta passada:
  - o acervo principal ficou intocado na sua estrutura curada;
  - a organizacao em lote aconteceu apenas no staging tecnico, preservando reprocessamento futuro.

## 2026-04-22 - Lote 39 - Curadoria preservavel e painel do Acervo Notas

- Evoluida a camada companheira dos PDFs para um formato de curadoria reaplicavel, sem perder o carater automatico.
- Atualizado `scripts/acervo/build_pdf_companion_notes.py` para:
  - adicionar campos de frontmatter como `document_kind`, `curation_priority`, `curation_stage` e `text_extractable`;
  - criar secoes fixas de `Aplicacao e integracoes sugeridas`, `Links internos sugeridos` e `Perguntas de curadoria`;
  - reservar um bloco `CURADORIA-HUMANA:START/END` que pode ser editado manualmente e preservado em futuras regeneracoes.
- Gerado o painel [Acervo Notas - Indice Gerado.md](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/Acervo%20Notas%20-%20Indice%20Gerado.md>) com:
  - distribuicao por sistema;
  - distribuicao por tipo documental;
  - distribuicao por prioridade de curadoria;
  - navegacao rapida por marca/familia da camada `_Acervo_Notas`.
- Atualizados os `READMEs` de `_Acervo_Local` e `_Acervo_Notas` para formalizar:
  - a separacao PDF fisico vs. nota companheira;
  - a preservacao do bloco de curadoria humana;
  - o uso do painel geral como porta de entrada da camada textual.

## 2026-04-22 - Lote 40 - Restauracao de contexto persistente no vault

- Criada a nota `_Editorial/Restauração de Contexto — Acervo e Conteúdo` para registrar, dentro da base, o estado operacional da frente de `acervo + conteúdo`.
- Integrado o ponto de retomada ao `MOC — Revisao Manual` para que a volta ao trabalho não dependa do histórico visível do chat.
- Consolidado nessa nota o caminho prático para reabrir a frente:
  - `Log de Evolução`;
  - `MOC — Revisao Manual`;
  - `Portal do Acervo`;
  - `Acervo Notas - Indice Gerado`.
- Registrado explicitamente que o problema percebido foi de memória conversacional do Codex, e não de perda do conteúdo técnico já produzido no vault.

## 2026-04-22 - Lote 41 - Recuperacao das threads do Codex por arquivo de sessao

- Confirmado que as conversas antigas da base continuam presentes em `C:\Users\User\.codex\session_index.jsonl` e em `C:\Users\User\.codex\sessions\2026\04\`.
- Validado dentro dos arquivos `rollout-*.jsonl` que as threads de abril tinham `cwd` apontando para:
  - `C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA`.
- Criada a nota `_Editorial/Recuperação de Threads do Codex — Eletro Nautica` com:
  - lista das threads recuperadas;
  - caminhos exatos dos arquivos `.jsonl`;
  - distinção entre `workspace original` e `sessao projectless`;
  - procedimento curto para nova recuperação futura.
- Vinculada essa trilha ao ponto de retomada `_Editorial/Restauração de Contexto — Acervo e Conteúdo`.

## 2026-04-22 - Lote 42 - Congelamento do ponto exato de retomada da curadoria

- Reaberta a sessao `019daf6e-51eb-70d0-9345-e2fb8424caa5` para identificar o ultimo ponto real de trabalho da frente `acervo + notas companheiras`.
- Confirmado que a instrucao central do usuario era:
  - manter os PDFs;
  - criar uma camada em Markdown por item;
  - extrair resumo, trechos, links uteis e integracoes;
  - deixar o fluxo pronto para futuros PDFs seguirem o mesmo conceito.
- Confirmado que a sessao parou logo apos um ajuste no parser de `codigos/modelos`, antes de rerodar a camada e as validacoes finais daquela passada.
- Criada a nota `_Editorial/Ponto de Retomada — Acervo Notas e Curadoria` com:
  - instrucao exata;
  - ponto de interrupcao;
  - pendencias reais;
  - ordem curta de continuacao.

## 2026-04-22 - Lote 43 - Endurecimento da pipeline do acervo companheiro

- Endurecido `scripts/acervo/pdf_text_tools.py` para separar tres estados de leitura:
  - `pdftotext` com texto util;
  - `pdf-stream-strings` com texto util;
  - `pdf-stream-strings-low-confidence` ou `no-text-detected` quando a extração nao merece ser tratada como texto confiavel.
- Endurecido `scripts/acervo/build_pdf_companion_notes.py` para:
  - reduzir ruído em `codigos/modelos detectados`;
  - priorizar codigos vindos de familia, slug tecnico e codigos realmente plausiveis;
  - parar de aceitar bloco automatico velho como se fosse curadoria humana;
  - reconstruir blocos `triagem-automatica` quando o conteudo preservado era apenas placeholder;
  - sinalizar explicitamente notas com extração textual de baixa confianca.
- Atualizado `scripts/acervo/organize_technical_triage_bulk.py` para o novo contrato de extração textual.
- Expandido `scripts/validate_vault.py` com verificacoes semanticas da camada `acervo-companion`, para evitar regressao de:
  - extração fraca marcada como `texto extraivel`;
  - `codigos/modelos` com ruído evidente;
  - bloco de curadoria com numeros espurios.
- Regeneradas as `46` notas companheiras e o painel `Acervo Notas - Indice Gerado`.
- Resultado pratico desta passada:
  - notas como `SeaTalk` passaram a cair corretamente em `pdf-stream-strings-low-confidence` com `texto extraivel: nao`;
  - a lista `codigos/modelos detectados` foi limpa nos PDFs principais de geradores, navegacao e acervo complementar;
  - blocos absurdos preservados por historico automatico foram resetados quando nao havia curadoria humana real.

## 2026-04-24 - Lote 44 - Curadoria premium piloto do Onan MDKBH

- Elevada a nota companheira `Geradores/Cummins-Onan/MDKBH/cummins-onan__mdkbh__service-manual__legacy-espelho.md` de `triagem-automatica` para `curadoria-humana-parcial`.
- Reescrito o bloco preservavel de curadoria com foco de oficina e diagnostico, incluindo:
  - identidade documental do manual `981-0542 (Issue 7)` e cobertura `MDKBH (Spec A-E)`;
  - caracterizacao tecnica do conjunto com `Kubota Z482`, `2 cilindros`, `0,479 L`, `2900/2400 rpm`;
  - mapa rapido por capitulos;
  - fault codes e sinais mais valiosos para atalho mental de bancada;
  - procedimentos premium como `fuel prime`, teste rapido da bomba, ajuste de `high-idle`, mudanca `50/60 Hz` e ajuste de tensao AC;
  - riscos nauticos criticos: `CO`, pecas `ignition protected`, retorno de armazenagem e contaminacao por vedacao errada em linha de diesel.
- Amarradas integracoes internas com notas-base de `Gerador (AC)`, `Troubleshooting`, `Aterramento`, `Detector de CO` e notas centrais do acervo de geradores.
- Este `MDKBH` passa a servir como referencia piloto de nivel premium para a proxima leva de notas `Cummins-Onan`.

## 2026-04-24 - Lote 45 - Empacotamento do Acervo Humano Tecnico

- Criado `scripts/acervo/package_human_technical_archive.py` para processar em lote o staging tecnico humano em `90_Revisao_Manual/_Acervo_Local/Acervo do humano/10_Tecnico_Nautico`.
- O script passou a:
  - abrir os arquivos do staging tecnico;
  - renomear os itens com padrao pesquisavel e seguro para Windows;
  - preservar nomes canonicos ja bons;
  - encurtar slugs extremos com hash curto para evitar falhas de caminho longo;
  - gerar notas-companheiras basicas em espelho dentro de `_Acervo_Notas/Acervo do humano/10_Tecnico_Nautico`;
  - resolver colisao de notas quando dois arquivos compartilham o mesmo stem em extensoes diferentes, usando sufixos como `__html` e `__pdf`.
- Resultado do lote:
  - `356` arquivos tecnicos processados;
  - `356` notas-companheiras geradas;
  - `0` arquivos temporarios remanescentes;
  - painel gerado em `90_Revisao_Manual/Acervo Humano Tecnico - Indice Gerado.md`.
- A passada precisou recuperar uma falha intermediaria de caminho longo no Windows durante a renomeacao; o algoritmo foi endurecido e a recuperacao foi concluida sem perda do lote.
- Validacao final desta passada:
  - `python scripts/check_python_scripts.py`;
  - `python scripts/build_manifest.py`;
  - `python scripts/validate_vault.py`.
- Estado final apos a rodada:
  - `19` scripts Python compilando;
  - `586` notas analisadas;
  - `0` erros;
  - `0` avisos.

## 2026-04-24 - Lote 46 - Hardening do staging tecnico humano e manifesto de duplicatas

- Endurecido `scripts/acervo/package_human_technical_archive.py` para:
  - limpar restos de nomes temporarios como `tmp-renomear-*`;
  - estabilizar a renomeacao para nao entrar em churn de hash curto;
  - tratar nomes com hash contextual como fallback estavel, e nao como lixo infinito;
  - reduzir falsos positivos em `codigos/modelos detectados` na camada do staging;
  - gerar automaticamente o manifesto de duplicatas do staging tecnico.
- Criados e atualizados os artefatos:
  - `90_Revisao_Manual/Acervo Humano Tecnico - Manifesto de Duplicatas.md`;
  - `manifest/acervo-humano-duplicates.json`.
- O manifesto passou a consolidar duplicatas fisicas por `sha256`, com:
  - grupo;
  - arquivo canonico sugerido;
  - bucket canonico;
  - lista completa de membros por grupo.
- Endurecido `scripts/validate_vault.py` para reconhecer nomes temporarios herdados no staging humano como problema semantico, evitando regressao silenciosa dessa sujeira.
- Resultado pratico da rodada:
  - `0` arquivos `tmp-renomear-*` remanescentes;
  - `20` grupos de duplicatas mapeados;
  - `51` arquivos envolvidos em duplicidade;
  - `31` excedentes sobre o canonico sugerido.
- Validacao final desta passada:
  - `python scripts/check_python_scripts.py`;
  - `python scripts/build_manifest.py`;
  - `python scripts/validate_vault.py`.
- Estado final apos o hardening:
  - `19` scripts Python compilando;
  - `587` notas analisadas;
  - `0` erros;
  - `0` avisos.

## 2026-04-24 - Lote 47 - Governanca operacional de duplicatas no staging humano

- Expandido `scripts/acervo/package_human_technical_archive.py` para anotar governanca de duplicatas diretamente nas notas-companheiras do staging tecnico humano.
- Cada nota do lote passou a registrar em frontmatter e corpo:
  - `duplicate_status` como `unique`, `canonical-suggested` ou `duplicate`;
  - `duplicate_group_sha256`;
  - tamanho do grupo;
  - arquivo e nota companheira canonicos sugeridos.
- Criada a fila operacional `90_Revisao_Manual/Acervo Humano Tecnico - Fila de Resolucao de Duplicatas.md`, ordenada por prioridade de resolucao para facilitar saneamento manual antes da proxima curadoria pesada.
- O painel `Acervo Humano Tecnico - Indice Gerado` e o `Manifesto de Duplicatas` passaram a apontar explicitamente para essa fila.
- O manifesto JSON `manifest/acervo-humano-duplicates.json` foi enriquecido com:
  - prioridade de resolucao;
  - acao recomendada;
  - contagem de buckets por grupo.
- Resultado pratico desta rodada:
  - `20` grupos de duplicatas continuam mapeados;
  - `31` arquivos excedentes seguem explicitados como fila de decisao;
  - as `356` notas-companheiras do staging agora carregam rastreabilidade fisica local sem depender apenas do painel central.
- Validacao final desta passada:
  - `python scripts/check_python_scripts.py`;
  - `python scripts/acervo/package_human_technical_archive.py`;
  - `python scripts/build_manifest.py`;
  - `python scripts/validate_vault.py`.

## 2026-04-26 - Lote 63 - Automacao completa dos proximos passos do acervo PDF

- Criado checkpoint Git antes das novas automacoes:
  - commit `f39e86b` (`Checkpoint organized PDF archive`).
- Ativado `git config core.longpaths true` no repositorio para permitir versionamento de caminhos longos do acervo sem renomear documentos tecnicos.
- Rodada completa da pipeline PDF executada com auditoria e OCR prioritario:
  - `678` PDFs auditados;
  - `2.8 GB` de acervo auditado;
  - `33305` paginas conhecidas;
  - `420` PDFs com `qpdf ok`;
  - `258` PDFs com `qpdf warning`;
  - `639` PDFs com texto pesquisavel;
  - `39` PDFs sem texto pesquisavel direto;
  - `8` PDFs selecionados para OCR prioritario;
  - OCR finalizado com `6` completos e `4` parciais no historico acumulado.
- Criado `scripts/acervo/build_curation_dashboard.py` como etapa automatica para:
  - separar `acervo-principal`, `humano-staging-tecnico`, `humano-fora-do-escopo` e `humano-arquivado-duplicata`;
  - gerar manifesto `manifest/acervo-curation-dashboard.json`;
  - gerar painel `90_Revisao_Manual/10_Indices_e_Paineis/Painel de Curadoria do Acervo.md`;
  - priorizar fila de curadoria por sistema, tipo documental, OCR, texto pesquisavel, paginas, `qpdf` e prioridade editorial;
  - enriquecer notas prioritarias com curadoria assistida por automacao sem sobrescrever curadoria humana existente.
- Resultado da separacao automatica:
  - `248` PDFs no acervo principal;
  - `230` PDFs no staging tecnico humano;
  - `176` PDFs fora de escopo/pessoais;
  - `24` PDFs em duplicatas arquivadas;
  - `478` PDFs classificados como tecnico operacional (`acervo-principal` + `humano-staging-tecnico`).
- Enriquecimento automatico aplicado:
  - `21` notas companheiras receberam bloco de `curadoria-assistida-automatica`;
  - `100` alvos tecnicos ficaram priorizados no manifesto/painel;
  - a rotina preserva blocos humanos ja editados e evita rebaixar curadoria existente.
- Propagacao para PDFs novos:
  - `run_pdf_pipeline.py` passou a chamar `build_curation_dashboard.py` antes da validacao e do manifesto final;
  - `README.md`, `AGENTS.md`, `CLAUDE.md` e `scripts/acervo/README.md` foram atualizados para documentar o novo passo.
- Validacao final desta passada:
  - `python scripts/acervo/run_pdf_pipeline.py --keep-going`;
  - `python scripts/acervo/run_pdf_pipeline.py --skip-audit --skip-ocr`;
  - `python scripts/check_python_scripts.py`;
  - `python scripts/validate_vault.py`;
  - `python scripts/build_manifest.py`.
- Estado final:
  - `26` scripts Python compilando;
  - `754` notas analisadas;
  - `0` erros;
  - `0` avisos.

## 2026-04-26 - Lote 62 - Limpeza reversivel e reestruturação final do 90_Revisao_Manual

- Reestruturada a raiz de `90_Revisao_Manual/` para reduzir ruído operacional sem apagar rastreabilidade.
- A raiz passou a manter apenas `README.md`; os arquivos soltos foram redistribuídos em:
  - `00_Entrada_e_Controle/` para portal, tabela-mestre, backlog e checklist;
  - `10_Indices_e_Paineis/` para índices e painéis gerados por script;
  - `20_Matrizes_Fontes_e_Links/` para matrizes, links confirmados e notas source-first;
  - `30_Notas_Tecnicas/` para notas técnicas pontuais;
  - `90_Arquivo_Historico/` para notas substituídas ou históricas.
- Nenhum PDF ou documento útil foi excluído; a limpeza foi reversível, com arquivamento lógico em vez de remoção.
- Atualizados `AGENTS.md`, `CLAUDE.md`, `README.md`, `00_Mapas/MOC — Revisao Manual.md` e `90_Revisao_Manual/_Acervo_Local/README.md` para apontarem ao novo padrão.
- Atualizados os scripts do acervo para que os relatórios gerados não retornem à raiz:
  - `build_local_index.py`;
  - `build_pdf_companion_notes.py`;
  - `package_human_technical_archive.py`;
  - `archive_human_duplicate_groups.py`;
  - `build_manual_resolution_queue.py`;
  - `build_brand_norm_bank.py`;
  - `run_pdf_pipeline.py`;
  - `audit_pdf_toolchain.py`;
  - `ocr_priority_pdfs.py`;
  - `promote_all_human_pdfs_to_main.py`;
  - `consolidate_human_triage_buckets.py`.
- Criado `scripts/acervo/README.md` para separar scripts ativos, utilitários de fonte/link e ferramentas históricas de migração; os `.py` não foram removidos por idade porque ainda há dependências e valor de rerun reversível.
- Resultado estrutural após a limpeza:
  - raiz de `90_Revisao_Manual/`: `1` arquivo (`README.md`);
  - `00_Entrada_e_Controle/`: `5` notas;
  - `10_Indices_e_Paineis/`: `7` notas;
  - `20_Matrizes_Fontes_e_Links/`: `21` notas;
  - `30_Notas_Tecnicas/`: `2` notas;
  - `90_Arquivo_Historico/`: `2` notas;
  - `_Acervo_Notas/`: `546` notas companheiras.
- Validacao final desta passada:
  - `python scripts/acervo/build_brand_norm_bank.py`;
  - `python scripts/acervo/build_manual_resolution_queue.py`;
  - `python scripts/check_python_scripts.py`;
  - `python scripts/validate_vault.py`;
  - `python scripts/acervo/run_pdf_pipeline.py --skip-audit --skip-ocr`.
- Estado final:
  - `25` scripts Python compilando;
  - `745` notas analisadas;
  - `0` erros;
  - `0` avisos.

## 2026-04-26 - Lote 60 - Promocao integral PDF do acervo humano tecnico

- Criado `scripts/acervo/promote_all_human_pdfs_to_main.py` para promover em massa, por hash, todos os PDFs tecnicos do staging humano para o acervo principal.
- A promocao foi feita por copia, nao por movimento, preservando os originais em `90_Revisao_Manual/_Acervo_Local/Acervo do humano/10_Tecnico_Nautico` para rastreabilidade e rollback.
- O script foi blindado para caminho longo no Windows via varredura `\\?\`, o que permitiu incluir o PDF longo de bomba pressurizadora que a varredura normal do Python nao enxergava.
- Resultado da promocao:
  - `230` PDFs tecnicos avaliados;
  - `202` PDFs copiados agora para o acervo principal;
  - `28` PDFs ja presentes por hash no acervo principal;
  - `67` arquivos nao-PDF mantidos no staging como fila de conversao/normalizacao (`60` HTML, `5` JPG, `1` JPEG, `1` PNG).
- O acervo principal passou a ter `248` PDFs indexados e `248` notas companheiras geradas em Markdown.
- Ampliado `scripts/acervo/build_pdf_companion_notes.py` para reconhecer os novos sistemas promovidos:
  - `Campo-Clientes`;
  - `Energia-DC`;
  - `Shore-Power-AC`;
  - `Bombas-Utilidades`;
  - `Iluminacao-Acessorios`;
  - `Corrosao-Seguranca`;
  - `Propulsao-Motores`;
  - `Materiais-Internos`;
  - `HTML-Tecnico-Exportado`.
- Atualizada a filtragem de modelos detectados para remover ruido de nomes genericos de documentos, como `DIAGRAMA`, `INSTALACAO`, `RAPHAEL`, `ELECTRICAL`, `MOTORES` e similares.
- Artefatos gerados/atualizados:
  - `_Editorial/Promocao Integral do Acervo Humano Tecnico.md`;
  - `manifest/acervo-humano-promoted-all-pdfs.json`;
  - `90_Revisao_Manual/Acervo Local - Indice Gerado.md`;
  - `90_Revisao_Manual/Acervo Notas - Indice Gerado.md`;
  - `90_Revisao_Manual/_Acervo_Local/acervo-local-index.json`;
  - `manifest/acervo-pdf-toolchain-audit.json`;
  - `_Editorial/Auditoria Operacional PDF - Toolchain.md`;
  - `manifest/content-manifest.json`.
- Auditoria operacional PDF apos promocao:
  - `248` PDFs no acervo principal;
  - `1.2 GB` auditados;
  - `14.834` paginas conhecidas;
  - `236` PDFs com texto extraivel;
  - `12` PDFs sem texto extraivel confiavel;
  - `8` PDFs em prioridade OCR alta;
  - `2` PDFs com OCR auxiliar concluido;
  - `2` PDFs bloqueados para OCR/reparo;
  - `0` notas companheiras faltantes.
- Duplicatas por hash no acervo principal permanecem intencionais em `7` grupos, principalmente manuais compartilhados entre familias/modelos Onan e Kohler.
- Validacao final desta passada:
  - `python scripts/check_python_scripts.py` -> `25` scripts, `0` falhas;
  - `python scripts/acervo/promote_all_human_pdfs_to_main.py --apply`;
  - `python scripts/acervo/build_local_index.py`;
  - `python scripts/acervo/audit_pdf_toolchain.py --scope main --max-text-pages 2 --ocr-sample-limit 0`;
  - `python scripts/acervo/build_pdf_companion_notes.py`;
  - `python scripts/build_manifest.py`;
  - `python scripts/validate_vault.py` -> `740` notas, `0` erros, `0` avisos.

## 2026-04-26 - Lote 61 - Normalizacao dos nao-PDF do acervo humano tecnico

- Expandido `scripts/acervo/package_human_technical_archive.py` para tambem tratar a fila nao-PDF do staging humano como camada operacional de busca, sem misturar HTML/imagens ao acervo principal PDF-first.
- Endurecido o pacote com varredura longa via `\\?\`, corrigindo o ponto cego que deixava um PDF de caminho longo fora da contagem normal.
- Resultado pratico da nova rodada:
  - `297` itens tecnicos encontrados no staging humano;
  - `1` renomeacao aplicada para encurtar caminho longo;
  - `297` notas companheiras geradas;
  - `0` renomeacoes pendentes no rerun de conferencia;
  - `67` nao-PDF catalogados em indice proprio.
- Criada camada dedicada para nao-PDF:
  - `90_Revisao_Manual/Acervo Humano Tecnico - Nao PDF - Indice Gerado.md`;
  - `_Editorial/Normalizacao Nao PDF - Acervo Humano Tecnico.md`;
  - `manifest/acervo-humano-non-pdf-support.json`;
  - `90_Revisao_Manual/_Dados_Acervo/non_pdf_texts/`.
- Resultado da extracao nao-PDF:
  - `60` HTML;
  - `5` JPG;
  - `1` JPEG;
  - `1` PNG;
  - `66` itens com texto bruto indexavel em Markdown/sidecar;
  - `24` itens com texto tecnicamente util o bastante para marcar `text_extractable: sim`;
  - `7` imagens processadas com Tesseract OCR.
- Atualizado `scripts/acervo/pdf_text_tools.py` para aceitar caminhos longos ao chamar `pdftotext` e ao ler fallback por streams.
- Decisao operacional preservada:
  - HTML e imagens continuam fora do acervo principal PDF-first;
  - ficam rastreados, pesquisaveis e prontos para conversao posterior em PDF arquivavel, nota autoral ou descarte justificado.
- Validacao final desta passada:
  - `python scripts/check_python_scripts.py` -> `25` scripts, `0` falhas;
  - `python scripts/acervo/package_human_technical_archive.py --dry-run` -> `297` itens, `0` renomeacoes pendentes apos aplicacao;
  - `python scripts/acervo/package_human_technical_archive.py`;
  - `python scripts/build_manifest.py`;
  - `python scripts/validate_vault.py` -> `743` notas, `0` erros, `0` avisos.

## 2026-04-25 - Lote 51 - Auditoria de conteudo com ferramentas do sistema

- Executada auditoria programatica da base usando:
  - `scripts/check_python_scripts.py`;
  - `scripts/validate_vault.py`;
  - `scripts/build_manifest.py`;
  - consultas adicionais sobre manifesto, backlinks e metadados.
- Snapshot confirmado nesta rodada:
  - `559` notas analisadas;
  - `20` scripts Python compilando;
  - `0` erros;
  - `0` avisos.
- Confirmado que o nucleo principal fora de `90_Revisao_Manual/` e `_Editorial/` segue forte:
  - `140` notas;
  - `0` orfas reais;
  - backlog de backlinks baixos continua concentrado em `MOC - Mapas`, `USB 12V (Power)` e `Limpador de Parabrisas`.
- Identificado o principal risco desta rodada como problema de observabilidade:
  - a camada de acervo usa bastante link Markdown local para notas `.md`;
  - isso deixa parte relevante da navegacao invisivel para analises baseadas apenas em links wiki do Obsidian.
- Confirmada a necessidade de um proximo lote focado em:
  - auditoria programatica que enxergue links Markdown locais;
  - padronizacao de frontmatter nos MOCs de `00_Mapas`;
  - triagem dos casos `acervo-companion` com extracao textual fraca.
- Registrado o relatorio desta passada em:
  - `'_Editorial/Auditoria de Conteúdo — Ferramentas do Sistema.md'`.

## 2026-04-25 - Lote 52 - Organizacao do 90_Revisao_Manual com o padrao recuperado do historico

- Recuperado do historico da frente `Organizar acervo local` e das notas de contexto o contrato operacional que segue valendo para a biblioteca:
  - manter os PDFs;
  - espelhar o acervo principal em `Markdown`;
  - preservar bloco de `curadoria humana`;
  - deixar o fluxo pronto para que cada PDF novo siga o mesmo conceito automaticamente.
- Confirmado nas ferramentas novas que o staging humano ja estava estruturalmente estabilizado:
  - `organize_human_archive.py` sem movimentos pendentes;
  - `package_human_technical_archive.py --dry-run` com `325` itens e `0` renomeacoes planejadas.
- Identificado um desvio no acervo principal:
  - `Arthur Ribeiro CV.pdf` estava solto na raiz de `_Acervo_Local`;
  - esse arquivo gerou indevidamente uma nota companheira no acervo principal e inflou a camada de `46` para `47` notas.
- Corrigida a organizacao:
  - o PDF foi movido para `90_Revisao_Manual/_Acervo_Local/Acervo do humano/00_Fora_do_Escopo_ou_Pessoal/`;
  - a nota companheira automatica indevida foi retirada do acervo principal;
  - a raiz de `_Acervo_Local` voltou a conter apenas `README` e artefatos operacionais.
- Reexecutada a pipeline do acervo:
  - `python scripts/acervo/package_human_technical_archive.py`;
  - `python scripts/acervo/build_local_index.py`;
  - `python scripts/acervo/build_pdf_companion_notes.py`.
- Estado final desta passada:
  - `325` itens tecnicos ativos no staging humano;
  - `0` renomeacoes novas no staging;
  - `0` acoes previstas de arquivamento de duplicatas;
  - `46` notas companheiras no acervo principal, de volta ao padrao esperado;
  - `_Acervo_Local` principal sem PDF pessoal solto na raiz.

## 2026-04-25 - Lote 53 - Auditoria pos-organizacao do 90_Revisao_Manual

- Reexecutada auditoria apos a organizacao fisica dos PDFs do `90_Revisao_Manual`.
- Validacoes finais:
  - `python scripts/check_python_scripts.py`;
  - `python scripts/validate_vault.py`;
  - `python scripts/build_manifest.py`;
  - `python scripts/acervo/package_human_technical_archive.py --dry-run`;
  - `python scripts/acervo/archive_human_duplicate_groups.py --dry-run --priority alta --priority media --priority baixa`.
- Snapshot confirmado:
  - `560` notas analisadas;
  - `20` scripts Python compilando;
  - `0` erros;
  - `0` avisos;
  - `0` PDFs soltos na raiz de `_Acervo_Local`;
  - `0` renomeacoes pendentes no staging tecnico;
  - `0` acoes pendentes de duplicatas.
- Achados principais:
  - nucleo principal segue com `140` notas e `0` orfas reais;
  - `_Acervo_Notas` segue com `371` notas companheiras no total;
  - o acervo principal curado segue com `46` notas companheiras;
  - as `46` notas companheiras do acervo principal ainda precisam de convencao explicita de `acervo_origin`.
- Registrado o relatorio desta passada em:
  - `'_Editorial/Auditoria Pós-Organização do 90_Revisao_Manual.md'`.

## 2026-04-25 - Lote 54 - Propagacao de instrucoes para Codex, Claude e PDFs novos

- Criados arquivos persistentes de governanca para agentes na raiz do repositorio:
  - `AGENTS.md`;
  - `CLAUDE.md`.
- O `AGENTS.md` passou a consolidar:
  - estilo editorial;
  - contexto operacional do usuario;
  - stack preferida;
  - fluxo obrigatorio para PDFs novos;
  - comandos de validacao;
  - regras do acervo e da camada companheira.
- O `CLAUDE.md` passou a funcionar como rotina curta para o Claude:
  - ler `AGENTS.md`;
  - validar antes e depois;
  - respeitar staging versus acervo principal;
  - preservar `CURADORIA-HUMANA:START/END`.
- Endurecido `scripts/acervo/build_pdf_companion_notes.py` para:
  - ignorar PDFs do acervo principal fora do padrao `Sistema/Marca/Familia`;
  - gravar `acervo_origin: "acervo-principal"` nas notas companheiras do acervo curado.
- Endurecido `scripts/validate_vault.py` para:
  - bloquear PDF solto ou fora do padrao no acervo principal;
  - exigir nota companheira para cada PDF curado;
  - exigir `acervo_origin: "acervo-principal"` nas notas companheiras do acervo principal.
- Atualizado o `README.md` para apontar para os arquivos de agentes e para a rotina de acervo.
- Regeradas as `46` notas companheiras do acervo principal com a nova origem explicita.

## 2026-04-25 - Lote 59 - Consolidacao da triagem tecnica do acervo humano

- Criado `scripts/acervo/consolidate_human_triage_buckets.py` para esvaziar a pasta intermediaria `90_Triagem_Tecnica_por_Codigo` com regras rastreaveis.
- Consolidados `102` arquivos fisicos que ainda estavam em subpastas intermediarias:
  - `70` foram movidos para buckets tecnicos finais;
  - `32` foram movidos para `00_Fora_do_Escopo_ou_Pessoal/_Triagem_Tecnica_Resolvida`;
  - `0` arquivos ficaram em `90_Triagem_Tecnica_por_Codigo`.
- Resultado apos empacotamento do staging humano:
  - `296` itens tecnicos ativos;
  - `12` buckets tecnicos finais;
  - `296` notas companheiras geradas;
  - `0` grupos de duplicatas no staging tecnico.
- Endurecido o consolidador para:
  - lidar com caminhos longos no Windows via prefixo `\\?\`;
  - ignorar erro de permissao ao tentar remover apenas diretorios vazios.
- Criado/atualizado o relatorio `_Editorial/Consolidacao do Acervo Humano Tecnico.md`.
- Executado `python scripts/acervo/run_pdf_pipeline.py --skip-audit --skip-ocr`:
  - `24` scripts analisados, `0` falhas;
  - `537` notas analisadas, `0` erros, `0` avisos;
  - manifesto geral reconstruido.

## 2026-04-25 - Lote 58 - Orquestrador unico da pipeline PDF

- Criado `scripts/acervo/run_pdf_pipeline.py` como entrada unica para a operacao de PDFs.
- O orquestrador cobre, em sequencia:
  - empacotamento/atualizacao do staging humano tecnico;
  - reconstrucao do indice local;
  - auditoria PDF com toolchain externo;
  - OCR auxiliar prioritario;
  - regeneracao de notas companheiras;
  - checagem de scripts Python;
  - validacao do vault;
  - reconstrucao do manifesto geral.
- Criados artefatos de rastreio da ultima execucao:
  - `manifest/pdf-pipeline-last-run.json`;
  - `_Editorial/Pipeline PDF - Ultima Execucao.md`.
- Adicionados modos operacionais:
  - `--dry-run` para conferir a sequencia sem executar;
  - `--skip-audit` e `--skip-ocr` para janelas curtas;
  - `--fast-audit` para auditoria mais rapida;
  - `--force-ocr`, `--max-ocr-pages` e `--ocr-only-contains` para controlar OCR pesado.
- Atualizados `README.md`, `AGENTS.md` e `CLAUDE.md` para preferirem `run_pdf_pipeline.py` quando um PDF novo entrar ou quando o acervo precisar ser reprocessado.
- Testes executados:
  - `python scripts/check_python_scripts.py`: `23` scripts, `0` falhas;
  - `python scripts/acervo/run_pdf_pipeline.py --dry-run`: sequencia completa verificada;
  - `python scripts/acervo/run_pdf_pipeline.py --skip-package --skip-audit --skip-ocr`: execucao real leve com `5` passos `ok` e `3` passos `skipped`;
  - validacao interna do wrapper: `565` notas, `0` erros, `0` avisos.

## 2026-04-25 - Lote 57 - OCR controlado dos PDFs prioridade alta

- Criado `scripts/acervo/ocr_priority_pdfs.py` para gerar OCR auxiliar sem sobrescrever PDFs originais.
- Gerados artefatos operacionais em:
  - `90_Revisao_Manual/_Dados_Acervo/ocr-results.json`;
  - `90_Revisao_Manual/_Dados_Acervo/ocr_texts/`;
  - `90_Revisao_Manual/_Dados_Acervo/ocr_notes/`;
  - `_Editorial/OCR Controlado - Acervo Principal.md`.
- Processados os `2` PDFs de prioridade `alta` do acervo principal:
  - Raymarine SeaTalk: `completed`, `3/3` paginas uteis, `3767` caracteres OCR;
  - Dometic Marine Air Conditioners Price List 2024: `partial`, `95/98` paginas uteis, `213175` caracteres OCR.
- Total gerado nesta rodada: `216942` caracteres OCR auxiliares.
- Enriquecido `build_pdf_companion_notes.py` para:
  - ler `ocr-results.json`;
  - marcar OCR `completed`/`partial` como `ocr_priority: "concluido"`;
  - inserir caminhos de TXT/MD OCR, status e contagem de caracteres no frontmatter das notas companheiras;
  - usar texto OCR como fonte de analise quando o PDF original nao tiver texto confiavel.
- Atualizados `README.md`, `AGENTS.md` e `CLAUDE.md` para propagar a rotina `ocr_priority_pdfs.py --priority alta`.
- Validacao final:
  - `python scripts/check_python_scripts.py`: `22` scripts, `0` falhas;
  - `python scripts/validate_vault.py`: `564` notas, `0` erros, `0` avisos;
  - `python scripts/build_manifest.py`: manifesto geral reconstruido.

## 2026-04-25 - Lote 56 - Auditoria operacional PDF com toolchain externo

- Criado `scripts/acervo/audit_pdf_toolchain.py` para auditar PDFs com Poppler, qpdf, ExifTool, Tesseract, MuPDF, ImageMagick, Ghostscript e 7-Zip.
- Gerados os artefatos:
  - `manifest/acervo-pdf-toolchain-audit.json`;
  - `_Editorial/Auditoria Operacional PDF - Toolchain.md`.
- A auditoria final varreu `472` PDFs (`1.8 GB`, `22061` paginas conhecidas):
  - `46` no acervo principal;
  - `258` no staging tecnico humano;
  - `144` fora de escopo/pessoal;
  - `24` arquivados como duplicatas.
- Resultado operacional:
  - `444` PDFs com texto pesquisavel;
  - `28` sem texto confiavel;
  - `2` candidatos `alta` para OCR no acervo principal;
  - `9` candidatos `media` no staging tecnico;
  - `53` grupos de duplicatas fisicas por SHA-256;
  - `0` notas companheiras faltantes no acervo principal.
- Enriquecido `build_pdf_companion_notes.py` para incorporar `pdf_pages`, `pdf_version`, `pdf_encrypted`, `qpdf_status` e `ocr_priority` nas notas companheiras.
- Atualizados `README.md`, `AGENTS.md` e `CLAUDE.md` para propagar a nova rotina de auditoria a agentes futuros.

## 2026-04-25 - Lote 55 - Instalacao de ferramentas externas para auditoria PDF/OCR

- Instalado e validado o conjunto externo principal para auditoria, OCR e saneamento de PDFs:
  - Tesseract OCR `5.5.0.20241111`;
  - qpdf `12.3.2`;
  - ExifTool `13.57`;
  - ImageMagick `7.1.2-21 Q16`;
  - MuPDF/mutool `1.23.0`;
  - Poppler `25.07.0` (`pdfinfo` e `pdftotext`);
  - 7-Zip `26.00`;
  - Ghostscript `10.07.0`.
- O Ghostscript nao estava disponivel no catalogo `winget`; foi instalado a partir do release oficial da Artifex/GitHub com SHA-256 verificado antes da execucao.
- Corrigido o `PATH` do usuario para expor:
  - `tesseract`;
  - `qpdf`;
  - `7z`;
  - `gswin64c`.
- Criado tessdata de usuario em `%LOCALAPPDATA%/Tesseract-OCR/tessdata` e configurado `TESSDATA_PREFIX` para habilitar OCR em:
  - `eng`;
  - `osd`;
  - `por`.
- Observacao operacional:
  - no Windows, o comando validado do Ghostscript e `gswin64c`, nao `gs`.

## 2026-04-24 - Lote 48 - Arquivamento reversivel e limpeza total das duplicatas do staging humano

- Criado `scripts/acervo/archive_human_duplicate_groups.py` para arquivar excedentes fisicos por prioridade fora do staging ativo, sem apagar arquivos e sem perder rastreabilidade.
- Definido o arquivo governado de resolvidas em:
  - `90_Revisao_Manual/_Acervo_Local/Acervo do humano/_Arquivados_Duplicatas_Resolvidas/10_Tecnico_Nautico`.
- Criados os artefatos de trilha desta limpeza:
  - `90_Revisao_Manual/Acervo Humano Tecnico - Arquivo de Duplicatas Resolvidas.md`;
  - `manifest/acervo-humano-duplicates-archived.json`.
- Primeira passada arquivou os `18` excedentes de prioridade alta.
- Segunda passada arquivou os `13` excedentes restantes de prioridade media/baixa, incluindo casos herdados de `98_Duplicatas`.
- O script de arquivamento foi endurecido com suporte a caminho longo no Windows, para resolver falhas em destinos acima de `MAX_PATH`.
- `scripts/acervo/package_human_technical_archive.py` tambem foi endurecido para nao falhar ao tentar remover diretorios vazios bloqueados pelo atributo `ReadOnly` do Windows.
- Resultado pratico apos regeneracao do lote:
  - staging tecnico humano caiu de `356` para `325` arquivos ativos;
  - `31` excedentes fisicos foram retirados do staging ativo e preservados no arquivo reversivel;
  - `0` grupos de duplicatas restantes;
  - `0` excedentes restantes;
  - `325` arquivos fisicamente unicos no staging.
- Validacao final desta passada:
  - `python scripts/check_python_scripts.py`;
  - `python scripts/acervo/archive_human_duplicate_groups.py --priority alta`;
  - `python scripts/acervo/archive_human_duplicate_groups.py --priority media --priority baixa`;
  - `python scripts/acervo/package_human_technical_archive.py`;
  - `python scripts/build_manifest.py`;
  - `python scripts/validate_vault.py`.
- Estado final apos a limpeza:
  - `20` scripts Python compilando;
  - `558` notas analisadas;
  - `0` erros;
  - `0` avisos.

## 2026-04-24 - Lote 49 - Blindagem de curadoria no staging e primeira leva premium de geradores

- Endurecido `scripts/acervo/package_human_technical_archive.py` para preservar em reruns:
  - bloco `CURADORIA-HUMANA`;
  - `curation_stage`;
  - `curation_priority`;
  - `status` das notas ja trabalhadas manualmente.
- Com isso, o staging humano deixou de ser apenas regeneravel e passou a ser tambem curavel sem risco de perder a camada humana na proxima rodada do pacote.
- Curadas manualmente as seguintes notas do bucket `01_Geradores`, elevadas para `staging-human-curated` com `curadoria-humana-parcial`:
  - `cummins-onan__mdkad-mdkae-mdkaf__service-manual__legacy-espelho.md`;
  - `cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__service-manual__legacy-espelho.md`;
  - `cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__operator-manual__a052j727.md`;
  - `934-0602-onan-mdl3-mdl4-mdl6-marine-genset-installation-manual-01-1991.md`;
  - `onan-troubleshooting-guide-codes.md`.
- A curadoria desta leva foi orientada por valor de oficina e ensino:
  - manual-base de servico para diagnostico e protecoes;
  - manual operacional para handoff e comissionamento;
  - manual de instalacao para retrofit e auditoria fisica;
  - guia curto de codigos como apoio de campo e atendimento remoto.
- O rerun de `package_human_technical_archive.py` foi executado logo depois das edicoes para provar que o pacote preserva a curadoria humana escrita nas notas.
- Resultado pratico desta passada:
  - bucket `01_Geradores` segue limpo, sem duplicatas fisicas ativas;
  - `5` notas do staging passaram de triagem bruta para fila editorial com valor tecnico real;
  - a pipeline do staging humano agora esta segura para continuar curadoria por lotes sem regressao de conteudo humano.
- Validacao final desta passada:
  - `python scripts/check_python_scripts.py`;
  - `python scripts/acervo/package_human_technical_archive.py`;
  - `python scripts/build_manifest.py`;
  - `python scripts/validate_vault.py`.

## 2026-04-24 - Lote 50 - Segunda leva de Onan no staging humano com preservacao semantica

- Expandido `scripts/acervo/package_human_technical_archive.py` para preservar em notas humanas, alem do bloco de curadoria:
  - `title`;
  - `document_kind`;
  - `acervo_brand`;
  - `acervo_family`.
- Esse endurecimento resolveu a perda de semantica em reruns para casos como:
  - familia `MDKBK-MDKBV` resumida no nome de arquivo como `MDKBX`;
  - `acervo_brand` ainda marcado como `A revisar` em familias Onan com stem menos explicito.
- Curadas manualmente mais `3` notas do bucket `01_Geradores`, elevadas para `staging-human-curated` com `curadoria-humana-parcial`:
  - `981-0181-onan-mdkbx-marine-genset-operator-manual-03-2008.md`;
  - `mdkbk-bl-bm-bn-bp-br-bs-bt-bu-bv-service-manual.md`;
  - `mdkdp-dr-ds-dt-du-dv-service-manual.md`.
- Esta leva fechou um conjunto mais coerente de familias `Cummins-Onan` no staging humano:
  - operacao de familias legadas `MDKBK-MDKBV`;
  - servico da familia legada `MDKBK-MDKBV`;
  - servico da familia media `MDKDP-MDKDV`.
- O rerun de `package_human_technical_archive.py` foi executado apos as edicoes para provar que as correcoes semanticas de frontmatter tambem sobrevivem a regeneracao.
- Resultado pratico desta passada:
  - o staging continua com `325` itens ativos e `0` duplicatas fisicas;
  - o bucket `01_Geradores` ganhou mais `3` notas com valor real de oficina;
  - a camada humana do staging agora preserva tanto narrativa editorial quanto metadado semantico corrigido.
- Validacao final desta passada:
  - `python scripts/check_python_scripts.py`;
  - `python scripts/acervo/package_human_technical_archive.py`;
  - `python scripts/build_manifest.py`;
  - `python scripts/validate_vault.py`.
