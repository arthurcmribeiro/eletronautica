---
title: "Acervo Notas - README"
note_type: "index"
domain: "90_Revisao_Manual"
status: "active-curation"
reviewed_on: "2026-04-22"
review_jurisdiction: "Brasil"
aliases:
  - "README do Acervo Notas"
  - "Camada Companheira dos PDFs"
related_notes:
  - "90_Revisao_Manual/Acervo Local - Indice Gerado"
  - "Tabela-Mestre do Acervo - Biblioteca de Referencia"
---

# Acervo Notas - README

> [!abstract] Resumo tecnico
> Esta pasta espelha o `acervo local principal`, mas em `Markdown`.
> Cada PDF importante pode ganhar uma nota companheira para busca, rastreio rapido, curadoria editorial e futuras integracoes.

## Funcao desta pasta

- manter uma camada textual pesquisavel sem mexer no PDF original;
- guardar sinais principais, trechos indexaveis e contexto minimo por documento;
- reservar um bloco fixo de `curadoria humana` que a automacao preserva nas reexecucoes;
- preparar terreno para notas humanas curadas, SEO, apostila, aulas e automacoes.

## Regra estrutural

- espelhar a mesma estrutura de `Sistema/Marca/Familia` do `_Acervo_Local`;
- usar o mesmo nome-base do PDF, trocando apenas a extensao para `.md`;
- manter esta camada separada do PDF fisico para evitar pasta poluida e facilitar automacao.

## Fluxo esperado

- PDF entra no acervo principal;
- a nota companheira nasce em `_Acervo_Notas/`;
- o bloco entre `CURADORIA-HUMANA:START/END` pode ser editado manualmente sem ser sobrescrito;
- depois, quando fizer sentido, essa nota automatica pode evoluir para curadoria humana.

## Automacao atual

- geracao em lote: `python scripts/acervo/build_pdf_companion_notes.py`
- promocao do staging para o acervo principal: `python scripts/acervo/promote_human_archive_to_main.py --apply`
- a promocao aplicada ja pode disparar a atualizacao das notas companheiras automaticamente.
- o painel geral da camada fica em `90_Revisao_Manual/Acervo Notas - Indice Gerado.md`.

## Limite desta camada

- ela nao substitui leitura tecnica humana;
- quando o PDF for escaneado, grafico demais ou ambiguuo, a nota pode sair incompleta;
- nesses casos, usar a nota como ponte de triagem, nao como verdade final.
