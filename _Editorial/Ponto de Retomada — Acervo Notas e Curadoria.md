---
title: "Ponto de Retomada — Acervo Notas e Curadoria"
note_type: "editorial"
domain: "_Editorial"
status: "active"
reviewed_on: "2026-04-22"
review_jurisdiction: "Brasil"
aliases:
  - "Parou Aqui - Acervo Notas"
  - "Retomada da Curadoria do Acervo"
related_notes:
  - "_Editorial/Restauração de Contexto — Acervo e Conteúdo"
  - "_Editorial/Recuperação de Threads do Codex — Eletro Nautica"
  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado"
  - "90_Revisao_Manual/_Acervo_Notas/README"
  - "MOC — Revisao Manual"
---

# Ponto de Retomada — Acervo Notas e Curadoria

> [!abstract] Resumo tecnico
> Esta nota congela o ponto exato em que a frente de `acervo + notas companheiras` ficou quando a sessao do Codex foi interrompida na UI.

## Atualizacao apos a recuperacao

- em `2026-04-22`, a pendencia do parser foi efetivamente resolvida no `Lote 43`;
- a pipeline de notas companheiras foi endurecida para separar `texto util` de `texto fraco` e evitar lixo em `codigos/modelos detectados`;
- a camada foi regenerada de novo com `46` notas;
- as validacoes fecharam com:
  - `229` notas;
  - `0` erros;
  - `0` avisos.

## Thread e momento exato

- thread principal: `019daf6e-51eb-70d0-9345-e2fb8424caa5`
- sessao: `C:\Users\User\.codex\sessions\2026\04\21\rollout-2026-04-21T06-45-36-019daf6e-51eb-70d0-9345-e2fb8424caa5.jsonl`
- ultimo ponto claro de trabalho da frente editorial: `2026-04-22 13:10`

## Instrucoes exatas do usuario que guiavam essa etapa

Em `2026-04-22 09:31`, a orientacao registrada foi:

- manter os `PDFs`;
- criar uma camada mais rastreavel em `Markdown` para cada item;
- extrair `informacoes principais`, `pequenos trechos`, `resumo`, `links uteis`, `integracoes` e contexto relevante;
- decidir se a camada ficaria junto do PDF ou em pasta separada, escolhendo a melhor estrutura;
- preparar o fluxo para que `cada PDF novo` adicionado no futuro ja siga esse conceito automaticamente.

## Solucao escolhida durante a sessao

- criar a pasta separada `90_Revisao_Manual/_Acervo_Notas/` como espelho do `_Acervo_Local`;
- manter o PDF fisico intacto;
- gerar uma nota companheira `.md` por PDF;
- preservar um bloco `CURADORIA-HUMANA:START/END` para enriquecer sem perder a automacao;
- gerar tambem o painel `90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado.md`.

## Ponto exato em que parou

- a camada automatica ja tinha sido gerada e reexecutada com `46` notas atualizadas;
- cinco notas de maior valor tecnico ja estavam com `curadoria humana parcial` preenchida:
  - `Geradores/Rehlko-Kohler/5EFKOD/...tp-6774-2014-02a.md`
  - `Geradores/Cummins-Onan/MDKDP-MDKDR-MDKDV/...a046j602.md`
  - `Climatizacao/Dometic/Self-Contained/...dx-remote-legacy-espelho.md`
  - `Complementar-Brasil/Corrosao/DPH-DPR-IPS/...medicoes.md`
  - `Complementar-Brasil/Referencias-Gerais/12V/...practical-12v-systems.md`
- em seguida o trabalho entrou numa passada de `acabamento do parser de codigos/modelos`, porque a extracao automatica ainda trazia falsos positivos por prefixos curtos demais;
- a ultima intencao explicitada pelo agente foi:
  - ajustar o parser;
  - `refazer a camada`;
  - `rodar as validacoes finais`.

## Evidencia tecnica da interrupcao

- a ultima mensagem operacional da sessao foi:
  - `Vou dar um acabamento no parser de codigos porque ele melhorou a captura, mas ainda trouxe alguns falsos positivos por prefixos curtos demais. Depois disso eu refaço a camada e rodo as validacoes finais.`
- imediatamente depois houve apenas o patch no script;
- nao aparecem novas execucoes de regeneracao nem validacoes dentro daquela sessao apos esse patch.

## O que ja estava pronto

- espelho `_Acervo_Notas/` montado;
- `README` da camada atualizado;
- painel geral `Acervo Notas - Indice Gerado` gerado;
- bloco de curadoria humana preservavel;
- primeira leva forte de curadoria manual iniciada em geradores, climatizacao e referencias complementares.

## O que ainda e pendencia real

- sair da etapa de endurecimento da automacao e entrar em `curadoria editorial humana`;
- consolidar as `5` notas ja parcialmente curadas para nivel pronto de uso;
- revisar a proxima leva de maior retorno tecnico sem abrir novos PDFs antes da hora;
- usar a camada `_Acervo_Notas` como fila editorial viva, e nao apenas como espelho tecnico.

## Como continuar a partir daqui

1. Abrir o painel [Acervo Notas - Indice Gerado](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado.md>) para usar a camada como fila de trabalho.
2. Manter o script [build_pdf_companion_notes.py](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/scripts/acervo/build_pdf_companion_notes.py>) como base estavel; so mexer nele se um caso novo realmente quebrar a qualidade da camada.
3. Reexecutar quando houver nova entrada no acervo principal ou mudanca relevante na heuristica:
   `python scripts/acervo/build_pdf_companion_notes.py`
4. Validar em seguida:
   `python scripts/check_python_scripts.py`
   `python scripts/build_manifest.py`
   `python scripts/validate_vault.py`
5. Revisar primeiro as cinco notas ja parcialmente curadas e decidir se cada uma sobe de `parcial` para `pronta para ensino/SEO` ou se fica como apoio tecnico de oficina.
6. Avancar para a proxima leva de maior retorno, nesta ordem:
   - `Geradores/Cummins-Onan`
   - `Geradores/Rehlko-Kohler`
   - `Climatizacao/Dometic`
   - `Climatizacao/Mabru`
   - `Navegacao/Garmin e Raymarine`
7. A cada nota prioritaria, preencher apenas o bloco `Curadoria humana` com:
   - resumo humano;
   - aplicacao de oficina;
   - modelos cobertos confirmados;
   - pontos de atencao;
   - integracoes e links internos;
   - status de curadoria.
8. Sempre que uma nota ganhar curadoria que mude uso real da biblioteca, refletir isso nas notas centrais:
   - `Tabela-Mestre do Acervo — Biblioteca de Referência`
   - `Backlog Operacional — Coleta de Manuais`
   - `Log de Evolução`

## Recomendacao pratica de retomada

- nao abrir novas familias do staging antes de amadurecer a camada `_Acervo_Notas/` dos PDFs que ja estao no acervo principal;
- primeiro consolidar a trilha `PDF fisico -> nota companheira -> curadoria humana -> integracao editorial`;
- depois voltar a promover novos lotes do `Acervo do humano`.

## Ordem curta para retomar sem pensar muito

1. abrir esta nota
2. abrir `Acervo Notas - Indice Gerado`
3. curar a proxima nota de maior valor tecnico
4. rodar o script se mexer na camada automatica ou entrar PDF novo
5. validar
6. registrar no `Log de Evolução`
