---
title: "Matriz de Normativas Citadas — Verificação Oficial"
note_type: "inventory"
domain: "90_Revisao_Manual"
status: "active-curation"
reviewed_on: "2026-04-19"
review_jurisdiction: "Brasil"
aliases:
  - "Verificação Oficial de Normativas"
  - "Matriz de Normas Citadas"
related_notes:
  - "Banco de Marcas e Normas Citadas — Corpus Integral"
  - "Normas e Regulamentações — Abyc Iso e Brasil"
  - "MOC — Revisao Manual"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://abycinc.org/abyc-technical-committees/"
  - "https://abycinc.org/events/certification-courses/marine-electrical-certification/"
  - "https://abycinc.org/news/supplement65/"
  - "https://www.iso.org/standard/69551.html"
  - "https://www.iso.org/standard/83643.html"
  - "https://www.marinha.mil.br/dpc/normam-211"
  - "https://www.marinha.mil.br/sites/default/files/atos-normativos/dpc/portaria-200-normam-211.html"
  - "https://www.marinha.mil.br/dpc/normam-204"
  - "https://www.marinha.mil.br/sites/default/files/atos-normativos/dpc/portaria-194-normam-204_0.html"
  - "https://webstore.iec.ch/en/publication/709"
  - "https://webstore.iec.ch/en/publication/67980"
  - "https://webstore.iec.ch/en/publication/67981"
  - "https://abntcatalogo.com.br/"
---

# Matriz de Normativas Citadas — Verificação Oficial

> [!abstract] Resumo técnico
> Esta nota consolida a checagem oficial das normativas mais sensíveis que apareceram no `Banco de Marcas e Normas Citadas — Corpus Integral`. O objetivo aqui não é reproduzir norma paga, e sim travar `qual referência está viva`, `qual foi substituída` e `onde verificar a fonte primária`.

## Leitura operacional

- o banco Python mostrou presença forte de `ABYC`, `ISO`, `IEC`, `NORMAM` e `ABNT NBR` no corpus;
- as verificações abaixo foram conferidas em fonte primária pública até `2026-04-19`;
- quando a norma depende de compra ou catálogo fechado, a regra da base passa a ser:
  - citar o código;
  - citar a fonte oficial de verificação;
  - evitar afirmar edição/ano sem checagem.

## Referências prioritárias verificadas

| Família / norma | Situação verificada | Leitura prática | Fonte oficial |
| --- | --- | --- | --- |
| `ABYC Standards` | hub oficial ativo | continua sendo a porta de entrada institucional para a biblioteca ABYC | [ABYC Standards](https://abycinc.org/standards/) |
| `ABYC E-11`, `E-13`, `E-2`, `E-10`, `E-30` | confirmadas como linhas ativas no ecossistema ABYC | aparecem em comitês e trilhas de certificação, então seguem vivas no referencial técnico | [ABYC Technical Committees](https://abycinc.org/abyc-technical-committees/) |
| `ABYC A-28`, `A-31`, `A-32`, `A-27` | confirmadas em trilha oficial de certificação elétrica | úteis para galvanic isolators, chargers/inverters, power conversion e gensets | [Marine Electrical Certification](https://abycinc.org/events/certification-courses/marine-electrical-certification/) |
| `ABYC E-11` e `E-13` | explicitamente citadas como atualizadas no suplemento recente | importante para revisão futura da base quando houver mudança de requisitos | [Supplement 65 update](https://abycinc.org/news/supplement65/) |
| `ISO 13297:2020` | publicada, edição 5, com `Amd 1:2022` | continua sendo a referência ISO central para instalações elétricas AC/DC em small craft | [ISO 13297:2020](https://www.iso.org/standard/69551.html) / [Amd 1:2022](https://www.iso.org/standard/83643.html) |
| `ISO 10133:2012` | retirada | não deve mais ser tratada como referência viva isolada; aparece como predecessora da trilha atual | [ISO 13297 lifecycle](https://www.iso.org/standard/69551.html) |
| `NORMAM-211/DPC` | página oficial ativa, atualizada em `2026-03-09`; Portaria `200/2026` | segue sendo o eixo regulatório mais direto para esporte e recreio no Brasil | [NORMAM 211](https://www.marinha.mil.br/dpc/normam-211) / [Portaria 200/2026](https://www.marinha.mil.br/sites/default/files/atos-normativos/dpc/portaria-200-normam-211.html) |
| `NORMAM-204/DPC` | página oficial ativa; Portaria `194/2025` | aparece muito no corpus, mas deve ser lida como tráfego/permanência e não como norma-mestre de projeto elétrico de bordo | [NORMAM 204](https://www.marinha.mil.br/dpc/normam-204) / [Portaria 194/2025](https://www.marinha.mil.br/sites/default/files/atos-normativos/dpc/portaria-194-normam-204_0.html) |
| `IEC 60092-507:2014` | publicação oficial ativa; versão 2008 marcada como revisada | permanece importante como referência complementar para instalações elétricas em small vessels fora do recorte recreativo puro | [IEC 60092-507:2014](https://webstore.iec.ch/en/publication/709) |
| `IEC 61008-1:2024` | publicação atual | referência atual para RCCB no universo doméstico/similar que o corpus usa como apoio para DR | [IEC 61008-1:2024](https://webstore.iec.ch/en/publication/67980) |
| `IEC 61009-1:2024` | publicação atual | referência atual para RCBO no mesmo universo de apoio | [IEC 61009-1:2024](https://webstore.iec.ch/en/publication/67981) |
| `ABNT NBR 5410` | verificação deve ser feita pelo catálogo oficial ABNT | continua sendo a família-base brasileira de BT na linguagem da base, mas a edição precisa ser conferida antes de citação fechada | [ABNT Catálogo](https://abntcatalogo.com.br/) |

## O que isso muda na biblioteca

- `ISO 10133` continua podendo aparecer no corpus, mas agora fica marcada como `referência histórica / retirada`;
- `ISO 13297` sobe como referência ISO viva da base;
- `NORMAM-211` passa a ser tratada como referência regulatória brasileira prioritária para esporte e recreio com data oficial explícita;
- `NORMAM-204` deve continuar no banco porque aparece muito, mas com etiqueta de escopo correto;
- `IEC 61008` e `IEC 61009` deixam de ser citadas genericamente como família solta quando o assunto pedir edição atual;
- `ABNT NBR 5410` permanece na base como apoio de BT, mas com disciplina de checagem no catálogo antes de afirmar ano/edição.

## Regra editorial daqui para frente

1. Se a nota citar norma específica, preferir `código + função + fonte oficial de verificação`.
2. Se a norma for paga, não inventar edição.
3. Se a norma tiver sido retirada ou substituída, manter o código antigo só com marcação histórica.
4. Para temas náuticos de instalação, separar sempre:
   - `regulação brasileira`;
   - `engenharia náutica`;
   - `norma de produto`;
   - `manual do fabricante`.
