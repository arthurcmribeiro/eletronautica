---
title: "Consolidacao do Acervo Humano Tecnico"
note_type: "audit"
domain: "90_Revisao_Manual"
status: "auto-generated"
reviewed_on: "2026-04-25"
review_jurisdiction: "Brasil"
related_notes:
  - "90_Revisao_Manual/Acervo Humano Tecnico - Indice Gerado"
  - "90_Revisao_Manual/Acervo Humano Tecnico - Manifesto de Duplicatas"
---

# Consolidacao do Acervo Humano Tecnico

> [!abstract] Resumo tecnico
> Consolidacao dos itens que estavam em `90_Triagem_Tecnica_por_Codigo`, movendo material tecnico para buckets finais e material nao tecnico para fora de escopo.

## Resultado

- modo aplicado: `True`
- arquivos fisicos retirados da triagem intermediaria: `102`
- itens tecnicos absorvidos por buckets finais: `70`
- itens movidos para fora de escopo: `32`
- arquivos restantes em `90_Triagem_Tecnica_por_Codigo`: `0`
- itens tecnicos ativos apos consolidacao: `296`
- buckets tecnicos finais apos consolidacao: `12`
- manifesto: `manifest/acervo-humano-triage-consolidation.json`

> [!info] Nota de execucao
> A primeira passada aplicou a consolidacao principal, mas o Windows bloqueou a remocao de uma pasta vazia por permissao. A segunda passada concluiu `3` arquivos de caminho longo que o `Path.is_file()` do Python nao reconhecia sem tratamento especifico. O script foi endurecido para caminho longo e permissoes de pasta vazia.

## Status

- `moved`: `102`

## Escopo

- `technical`: `70`
- `out-of-scope`: `32`

## Destinos

- `90_Revisao_Manual/_Acervo_Local/Acervo do humano/10_Tecnico_Nautico/09_Propulsao_Motores_Estabilizacao_e_Atuacao`: consolidado como maior bucket tecnico final.
- `90_Revisao_Manual/_Acervo_Local/Acervo do humano/10_Tecnico_Nautico/01_Geradores`: absorveu geradores, AVRs e reguladores de gerador.
- `90_Revisao_Manual/_Acervo_Local/Acervo do humano/10_Tecnico_Nautico/03_Baterias_e_DC`: absorveu carregadores, chaves de bateria, reguladores e componentes DC.
- `90_Revisao_Manual/_Acervo_Local/Acervo do humano/10_Tecnico_Nautico/05_Navegacao_e_Eletronicos`: absorveu instrumentos, VDO, Intellian e manuais tecnicos de interface.
- `90_Revisao_Manual/_Acervo_Local/Acervo do humano/10_Tecnico_Nautico/00_Documentacao_de_Campo_e_Clientes/Imagens_e_Recortes_Tecnicos`: absorveu recortes e imagens tecnicas.
- `90_Revisao_Manual/_Acervo_Local/Acervo do humano/00_Fora_do_Escopo_ou_Pessoal/_Triagem_Tecnica_Resolvida`: recebeu `32` itens nao tecnicos, pessoais, comerciais ou academicos fora do foco do acervo tecnico.

## Movimentacoes detalhadas da segunda passada

- `moved` - `technical` - `90_Revisao_Manual/_Acervo_Local/Acervo do humano/10_Tecnico_Nautico/90_Triagem_Tecnica_por_Codigo/02_Navegacao_Comunicacao_e_Instrumentos/manual_2019-12-19_08-26-08_437f82db9d3ec913309ffa0b7b52f11f.pdf` -> `90_Revisao_Manual/_Acervo_Local/Acervo do humano/10_Tecnico_Nautico/05_Navegacao_e_Eletronicos/manual_2019-12-19_08-26-08_437f82db9d3ec913309ffa0b7b52f11f.pdf`
- `moved` - `technical` - `90_Revisao_Manual/_Acervo_Local/Acervo do humano/10_Tecnico_Nautico/90_Triagem_Tecnica_por_Codigo/03_Propulsao_Motores_e_Turbo/5648FFB8-6EFB-48BB-AA5D-270A51B18862PORTUGUESE_TH360B_31200294-A_OMM.pdf` -> `90_Revisao_Manual/_Acervo_Local/Acervo do humano/10_Tecnico_Nautico/09_Propulsao_Motores_Estabilizacao_e_Atuacao/5648FFB8-6EFB-48BB-AA5D-270A51B18862PORTUGUESE_TH360B_31200294-A_OMM.pdf`
- `moved` - `technical` - `90_Revisao_Manual/_Acervo_Local/Acervo do humano/10_Tecnico_Nautico/90_Triagem_Tecnica_por_Codigo/06_Artigos_Normas_e_Referencia_Tecnica/2015-MSc-PEMM-Gustavo_Henrique_Senna_de_Freitas_Ligeiro_de_Carvalho.pdf` -> `90_Revisao_Manual/_Acervo_Local/Acervo do humano/10_Tecnico_Nautico/10_Materiais_Internos_e_Cursos/Referencias_Tecnicas/2015-MSc-PEMM-Gustavo_Henrique_Senna_de_Freitas_Ligeiro_de_Carvalho.pdf`

## Resultado operacional apos regeneracao

- `python scripts/acervo/run_pdf_pipeline.py --skip-audit --skip-ocr` concluiu com status `ok`.
- `package_human_technical_archive.py` processou `296` itens tecnicos e gerou `296` notas companheiras.
- `validate_vault.py` analisou `537` notas com `0` erros e `0` avisos.
