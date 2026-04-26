---
title: "Portal do Acervo — Biblioteca de Referência"
note_type: "moc"
domain: "90_Revisao_Manual"
status: "active-curation"
reviewed_on: "2026-04-19"
review_jurisdiction: "Brasil"
aliases:
  - "Portal do Acervo"
  - "Entrada da Biblioteca de Manuais"
  - "Guia de Acesso ao Acervo"
related_notes:
  - "MOC — Revisao Manual"
  - "Banco de Marcas e Normas Citadas — Corpus Integral"
  - "Preparação Source-First — Resolver de Links Oficiais"
  - "Tabela-Mestre do Acervo — Biblioteca de Referência"
  - "Backlog Operacional — Coleta de Manuais"
  - "Matriz de Fontes — Fabricantes e Repositórios"
  - "Matriz de Modelos e Versões — Geradores"
  - "Matriz de Normativas Citadas — Verificação Oficial"
  - "Acervo Local — Índice Gerado"
  - "Acervo de Manuais — Marcas e Modelos Prioritários"
  - "Links Confirmados — Climatização Náutica Nacional (H-Tec, Gelotec e Schutz)"
---

# Portal do Acervo — Biblioteca de Referência

> [!abstract] Resumo técnico
> Esta nota é a porta de entrada simples da biblioteca. Ela existe para uma pessoa encontrar rápido `onde procurar`, `onde estão os links`, `qual o status do material` e `onde os PDFs devem ficar` sem precisar abrir toda a engrenagem editorial do acervo.

## Comece por aqui

- para visão geral da frente editorial: [[MOC — Revisao Manual]]
- para busca por `marca`, `família`, `modelo` e `status documental`: [[Tabela-Mestre do Acervo — Biblioteca de Referência]]
- para o banco integral de `marcas + submarcas + produtos + normas`: [[Banco de Marcas e Normas Citadas — Corpus Integral]]
- para a fila preparada de resolução oficial sem download: [[Preparação Source-First — Resolver de Links Oficiais]]
- para ver a aplicação real do resolvedor em `Onan`: [[Aplicação Piloto — Onan (Resolver Source-First)]]
- para saber o que ainda está faltando coletar: [[Backlog Operacional — Coleta de Manuais]]
- para descobrir `portal oficial`, `fonte secundária` e `espelho`: [[Matriz de Fontes — Fabricantes e Repositórios]]
- para geradores com muitas variantes: [[Matriz de Modelos e Versões — Geradores]]
- para checagem normativa oficial: [[Matriz de Normativas Citadas — Verificação Oficial]]
- para ver o recorte de prioridade: [[Acervo de Manuais — Marcas e Modelos Prioritários]]

## Atalhos rápidos por tema

- climatização importada: [[Links Confirmados — Climatizacao Marinha (Webasto, Mabru e FRIGOMAR)]]
- climatização Dometic: [[Links Confirmados — Dometic Marine (Climate, Controls e Sanitário)]]
- climatização Brasil-primeiro: [[Links Confirmados — Climatização Náutica Nacional (H-Tec, Gelotec e Schutz)]]
- bombas, toilets e thrusters: [[Links Confirmados — Xylem e VETUS (Bombas, Toilets, Searchlights e Thrusters)]]
- geradores pequenos: [[Links Confirmados — Geradores Pequenos (Onan e Rehlko)]]
- geradores médios: [[Links Confirmados — Geradores Médios (Onan MDKDP a MDKDU)]]
- piloto de resolução `source-first` em geradores: [[Aplicação Piloto — Onan (Resolver Source-First)]]
- geradores já baixados para teste de biblioteca: [[Acervo Local — Geradores Iniciais (Cummins Onan)]]
- shore power e conectores: [[Links Confirmados — Shore Power, Conversão AC e Conectores Marinhos]]
- segurança e iluminação: [[Links Confirmados — Segurança e Iluminação Náutica]]
- vela, vento e instrumentação: [[Links Confirmados — B&G Vela, Vento e Instrumentacao]]
- estabilização: [[Links Confirmados — Estabilização Náutica (Seakeeper Ride)]]

## Onde ficam os links e os PDFs

- os `links confirmados` ficam organizados nas notas `Links Confirmados — ...`;
- a visão central por `marca/família/status` fica na [[Tabela-Mestre do Acervo — Biblioteca de Referência]];
- a fila operacional de captura fica no [[Backlog Operacional — Coleta de Manuais]];
- o ponto físico previsto para os `PDFs baixados` fica em [[90_Revisao_Manual/_Acervo_Local/README|_Acervo_Local/README]].
- os primeiros arquivos já baixados ficam visíveis em [[Acervo Local — Índice Inicial]].
- o inventário automático do que já está salvo fica em [[Acervo Local — Índice Gerado]].
- o primeiro bloco real de geradores baixados fica em [[Acervo Local — Geradores Iniciais (Cummins Onan)]].

## Estado atual do acervo

- a estrutura de consulta já está organizada;
- o acervo local agora já tem `fila JSON`, `relatório de captura` e `índice gerado` por Python;
- a biblioteca agora também tem `banco integral de marcas e normas` e `fila source-first de resolução oficial`;
- a biblioteca agora também tem `piloto aplicado` em `Onan`, com `curated_candidates` e separação por `official / secondary / mirror`;
- boa parte do material ainda está em `portal mapeado` ou `manual localizado`;
- isso significa que muitos documentos já foram identificados, mas ainda não viraram `PDF baixado + nome padronizado + curadoria concluída`;
- em outras palavras:
  - `link confirmado` não é a mesma coisa que `arquivo já guardado`;
  - `manual localizado` não é a mesma coisa que `acervo local fechado`.

## Legenda rápida

- `pendente`: ainda sem fonte útil confirmada
- `portal mapeado`: a fonte principal já foi encontrada
- `manual localizado`: o manual relevante já apareceu
- `baixado`: o arquivo já entrou no acervo local
- `curado`: o material já foi triado, nomeado e ficou pronto para uso

## Regra prática para consulta

1. Se você já sabe a `marca` ou `modelo`, comece pela [[Tabela-Mestre do Acervo — Biblioteca de Referência]].
2. Se você quer `baixar` ou `abrir a fonte`, vá para a nota `Links Confirmados` do tema.
3. Se você quer saber `o que falta`, abra o [[Backlog Operacional — Coleta de Manuais]].
4. Se houver dúvida de `portal correto`, volte na [[Matriz de Fontes — Fabricantes e Repositórios]].
