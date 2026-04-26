---
title: "Checklist Operacional — Abertura de Nova Família do Acervo"
note_type: "guide"
domain: "90_Revisao_Manual"
status: "active-curation"
reviewed_on: "2026-04-19"
review_jurisdiction: "Brasil"
aliases:
  - "Checklist de Abertura de Família"
  - "Checklist do Acervo"
  - "Template de Abertura de Família"
related_notes:
  - "Padrão da Biblioteca de Referência Técnica"
  - "MOC — Revisao Manual"
  - "Tabela-Mestre do Acervo — Biblioteca de Referência"
  - "Backlog Operacional — Coleta de Manuais"
  - "Matriz de Fontes — Fabricantes e Repositórios"
  - "Matriz de Modelos e Versões — Geradores"
  - "Log de Evolução"
---

# Checklist Operacional — Abertura de Nova Família do Acervo

> [!abstract] Resumo técnico
> Esta nota transforma o padrão da biblioteca em rotina prática. Sempre que uma nova família, marca, subgrupo ou bloco técnico for aberto no acervo, usar esta checklist para evitar lacunas de rastreabilidade, curadoria e busca futura.

Para a regra-mãe, ver [[_Editorial/Padrão da Biblioteca de Referência Técnica|Padrão da Biblioteca de Referência Técnica]].

## Quando usar

- ao abrir uma nova marca ou família no backlog;
- ao desdobrar uma submarca ou linha histórica;
- ao transformar uma família ampla em blocos menores;
- ao começar a coleta real de documentos de uma família já mapeada.

## Etapa 1 — Enquadramento correto

- [ ] confirmar que a família pertence ao `mercado náutico`;
- [ ] verificar se a família deve entrar como `linha principal` ou apenas `apoio`;
- [ ] definir se o avanço será por `bloco de família/plataforma` ou por `modelo exato`;
- [ ] confirmar a categoria técnica principal:
  - energia;
  - geração;
  - climatização;
  - bombas;
  - navegação;
  - segurança;
  - utilidades;
  - outra.

## Etapa 2 — Normalização de nome

- [ ] registrar `grupo_matriz`;
- [ ] registrar `marca operacional`;
- [ ] registrar `aliases` e marcas legadas;
- [ ] definir o nome que será usado como padrão de busca;
- [ ] verificar se a marca precisa de nota-matriz ou matriz de versões.

## Etapa 3 — Camada de fontes

- [ ] localizar `fonte oficial primária`;
- [ ] localizar `fonte oficial secundária`, se existir;
- [ ] verificar se há `espelho externo` útil;
- [ ] registrar limitação prática da fonte oficial:
  - exige serial;
  - exige dealer;
  - exige login;
  - só mostra literature;
  - outra.

## Etapa 4 — Estrutura técnica mínima

- [ ] registrar `familia_codigos`;
- [ ] registrar `spec`, revisão ou variante, quando aplicável;
- [ ] registrar `Hz`, `fase_tensao` e `controlador`, quando aplicável;
- [ ] em geradores e motorizados:
  - [ ] registrar `motor_base`;
  - [ ] registrar `cilindros`;
- [ ] registrar observação operacional curta e útil para oficina.

## Etapa 5 — Pacote documental

- [ ] identificar quais documentos existem:
  - [ ] `service`
  - [ ] `operacao`
  - [ ] `parts`
  - [ ] `installation`
  - [ ] `wiring`
  - [ ] `troubleshooting`
  - [ ] `spec sheet`
  - [ ] `catalogo_guide`
- [ ] distinguir claramente:
  - [ ] documento oficial localizado;
  - [ ] documento sustentado só por espelho;
  - [ ] documento apenas inferido por literature;
- [ ] em geradores, conferir se o `pacote triplo` foi realmente identificado.

## Etapa 6 — Registro nas notas certas

- [ ] atualizar a `Matriz de Fontes`, quando a fonte ainda não estiver formalizada;
- [ ] atualizar a `Matriz de Modelos e Versões`, quando houver muita variação de família;
- [ ] abrir ou atualizar a linha correspondente no `Backlog Operacional`;
- [ ] abrir ou atualizar a linha da `Tabela-Mestre do Acervo`;
- [ ] se a mudança alterar a governança da biblioteca, registrar no `Log de Evolução`.

## Etapa 7 — Estrutura local do acervo

- [ ] definir `pasta_sugerida`;
- [ ] padronizar nome de arquivo:
  `marca__familia-modelo__tipo-documento__spec-rev-ano`;
- [ ] separar `manual técnico` de `catálogo`, `brochure` e `guide`;
- [ ] evitar arquivos duplicados com nomes vagos.

## Etapa 8 — Critério de fechamento

- [ ] a família está com fonte principal clara;
- [ ] os nomes foram normalizados;
- [ ] os campos mínimos foram preenchidos;
- [ ] os documentos-chave foram localizados;
- [ ] a linha está coerente no backlog e na tabela-mestre;
- [ ] a curadoria não deixou ambiguidade grave de modelo, spec ou geração.

## Regra rápida por tipo

### Geradores

- obrigatório:
  `service + operacao + parts`;
- complementar forte:
  `installation + spec + literature + parts portal`;
- campos técnicos obrigatórios:
  `motor_base + cilindros + Hz + fase_tensao + controlador`.

### Equipamentos técnicos gerais

- obrigatório:
  `instalacao + operacao`;
- complementar:
  `service + parts + wiring + troubleshooting + spec`.

### Catálogos e guides

- não fecham família sozinhos;
- servem para:
  abrir linha, mapear subgrupos, localizar alias e acelerar a coleta certa.

## Mini-template de abertura

```md
marca:
grupo_matriz:
alias:
subgrupo:
familia_codigos:
spec_rev:
motor_base:
cilindros:
hz:
fase_tensao:
controlador:
fonte_oficial:
fonte_secundaria:
fonte_espelho:
documentos_localizados:
pacote_triplo:
pasta_sugerida:
observacoes:
```

## Sinais de erro que devem travar a curadoria

- família aberta só com nome comercial genérico e sem código;
- mistura de documentos de famílias diferentes no mesmo bloco;
- `service` de uma revisão e `parts` de outra, sem anotação;
- uso de espelho como se fosse fonte oficial;
- motor-base ou cilindros inferidos sem base mínima;
- família marcada como fechada sem documento suficiente.

## Saída mínima esperada ao final

- linha coerente no `Backlog Operacional`;
- linha coerente na `Tabela-Mestre do Acervo`;
- fontes rastreadas;
- nomenclatura normalizada;
- pacote documental classificado;
- pasta sugerida pronta para a coleta física.
