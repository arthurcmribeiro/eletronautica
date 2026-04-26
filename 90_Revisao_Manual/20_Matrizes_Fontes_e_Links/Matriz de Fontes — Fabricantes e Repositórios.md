---
title: "Matriz de Fontes — Fabricantes e Repositórios"
note_type: "inventory"
domain: "90_Revisao_Manual"
status: "active-curation"
reviewed_on: "2026-04-19"
review_jurisdiction: "Brasil"
aliases:
  - "Matriz de Fontes"
  - "Fontes de Manuais e Repositórios"
related_notes:
  - "Padrão da Biblioteca de Referência Técnica"
  - "Checklist Operacional — Abertura de Nova Família do Acervo"
  - "MOC — Revisao Manual"
  - "Backlog Operacional — Coleta de Manuais"
  - "Acervo de Manuais — Marcas e Modelos Prioritários"
  - "Inventário Completo — Marcas e Modelos Citados no Corpus"
  - "Matriz de Marcas Matriz — Ecossistemas e Subgrupos"
  - "Matriz Dometic — Subgrupos, Linhas e Documentos"
  - "Matriz de Modelos e Versões — Geradores"
  - "Gerador (AC)"
---

# Matriz de Fontes — Fabricantes e Repositórios

> [!abstract] Resumo técnico
> Esta nota inaugura a camada `source-first` do acervo. Em vez de depender só do que já foi citado no corpus, ela mapeia os portais que de fato concentram manuais, fichas técnicas, literatura e documentos de suporte para pesquisa estruturada.

Usar esta nota junto com [[_Editorial/Padrão da Biblioteca de Referência Técnica|Padrão da Biblioteca de Referência Técnica]] e [[Checklist Operacional — Abertura de Nova Família do Acervo]].

## Regra de uso desta matriz

- `fonte oficial primária`: fabricante ou portal oficial com maior prioridade para manual válido;
- `fonte oficial secundária`: portal oficial útil, mas normalmente dependente de busca por serial, login, dealer ou família;
- `espelho externo`: repositório não oficial, útil para legado e lacuna, mas nunca deve substituir a confirmação por fonte oficial quando ela existir;
- quando houver conflito entre manual oficial e espelho externo, prevalece o oficial;
- quando a marca mudou de nome, registrar sempre `marca atual + alias legado`.

## Matriz principal de fontes

| Fonte | Tipo | Cobertura útil | Uso recomendado | Limitação prática | URL |
| --- | --- | --- | --- | --- | --- |
| Victron Energy Manuals | fonte oficial primária | energia, monitoramento, carregadores, inversores, GX, baterias | localizar manual por família e revisão | muitas famílias dividem manual por linha de produto | [Victron](https://www.victronenergy.com/support-and-downloads/manuals) |
| Mastervolt Downloads | fonte oficial primária | carregadores, inversores/carregadores, shore power, baterias | baixar manuais e literatura por produto | alguns SKUs legados exigem navegação adicional | [Mastervolt](https://www.mastervolt.com/downloads/) |
| Blue Sea Resources | fonte oficial primária | proteção, chaves, barramentos, fusíveis | localizar datasheet, instruções e application notes | catálogo é muito orientado a família, não a instalação completa | [Blue Sea Systems](https://www.bluesea.com/resources) |
| Cummins Marine Resources | fonte oficial primária | Onan Marine atual, spec sheets, brochures, documentos técnicos | pesquisa por família atual de geradores e manutenção | nem todo documento é exposto como manual aberto por SKU | [Cummins Marine Resources](https://www.cummins.com/generators/marine/resources) |
| Cummins Support Manuals / QuickServe | fonte oficial secundária | manuais, parts e docs por serial/spec | usar quando o modelo exige `ESN`, `spec` ou serial number | pode exigir registro e busca mais precisa | [Cummins Manuals](https://www.cummins.com/support/manuals?locset=US) |
| Rehlko Marine | fonte oficial primária | Kohler Marine atual, pleasure craft, commercial, technical documents | localizar modelos atuais e docs por página de produto | rebranding Kohler -> Rehlko exige atenção a alias históricos | [Rehlko Marine](https://www.marine.rehlko.com/) |
| Dometic Marine Partner Resources | fonte oficial primária | climatização, sanitário, refrigeração, água, steering e controles | abrir camada `Dometic/Cruisair/Marine Air` com manuais e literature | parte do material é distribuída por categoria ou dealer flow | [Dometic Marine Partner Resources](https://www.dometic.com/en-us/lp/marinelp-dometic-marine) |
| Webasto Cooling | fonte oficial prim?ria | climatiza??o marinha self-contained, chillers e controles | abrir por `BlueCool`, `FCF` e `MyTouch`, separando o que ? manual do que ? apenas datasheet/catalog | camada p?blica ? forte em p?ginas t?cnicas e downloads, mas parece menos aberta em manuais completos | [Webasto Cooling](https://www.webasto.com/en-us/cooling.html) |
| Mabru Marine | fonte oficial prim?ria | climatiza??o marinha DC/AC, rooftop e documenta??o de instala??o | excelente para `retrofit sem gerador`, `12 V DC` e pesquisa por fam?lia `SC/VI` | j? exp?e manual oficial 2025, specs e camada ?til de pump/wiring | [Mabru Marine](https://www.mabrumarine.com/) |
| FRIGOMAR Download | fonte oficial prim?ria | self-contained, chillers, fancoils, termostatos e brochures | abrir por `SCU`, `CU`, `AH` e `APDS`, mantendo distin??o entre datasheet e manual | camada p?blica muito boa para cat?logo t?cnico e source-first por fam?lia | [FRIGOMAR Download](https://www.frigomar.com/en/download/) |
| H-Tec Náutica | fonte oficial secundária | climatização náutica, dessalinizadores e painéis digitais | usar `site + brochure + revenda autorizada`, com viés `Brasil-primeiro` | a camada pública indexável ainda é fraca em manuais técnicos abertos | [H-Tec Náutica](https://www.htecnautica.com.br/) |
| Gelotec Refrigeração | fonte oficial secundária | refrigeração comercial/industrial, boiler, inox e gelo | usar só como apoio `Brasil-primeiro` e adjacência técnica, não como núcleo náutico | nesta passada não apareceu linha náutica robusta | [Gelotec Refrigeração](https://gelotecrefrigeracao.com.br/) |
| VETUS Manuals | fonte oficial primária | thrusters, powerpacks, chargers, utilidades, catálogos de peças | excelente para pesquisa por modelo exato e parts catalogue | cobertura muito extensa; exige recorte por família | [VETUS Manuals](https://vetus.com/service-support/manuals/) |
| Xylem Rule Documents | fonte oficial primária | bilge, float switch, shower drain, livewell, utility pumps | muito forte para `Rule` por família funcional | algumas páginas indexadas aparecem em locales europeus | [Rule Documents](https://www.xylem.com/de-de/brands/rule/documents/) |
| Xylem Jabsco | fonte oficial primária | sanitário, bombas, impellers, searchlights, cooling pumps | usar marca + página de produto + PDF oficial | a página genérica de documentos tem busca fraca; muitas vezes compensa entrar pelo produto | [Jabsco](https://www.xylem.com/en-us/brand/jabsco/) |
| Garmin Marine Support | fonte oficial primária | MFD, radar, transdutor, piloto, sensores | localizar manuals e software por SKU | modelos legados e locales variam bastante | [Garmin Marine](https://support.garmin.com/marine/) |
| Raymarine Document Library | fonte oficial primária | MFD, radar, piloto, instrumentos | família + document library | muitos documentos por geração, o que pede filtro fino | [Raymarine](https://www.raymarine.com/en-us/support/document-library) |
| Simrad Support | fonte oficial primária | MFD, radar, piloto, vento | usar páginas de produto/suporte por geração | linhas antigas e B&G compartilham tecnologia mas não portal único | [Simrad](https://www.simrad-yachting.com/help--support/service-and-support/) |
| Furuno Manuals | fonte oficial primária | radar, MFD, GPS compass, fishfinder | muito bom para SKU profissional exato | menos amigável para busca por uso leigo | [Furuno](https://furunousa.com/en/knowledge_base/general/manuals_for_furuno_products) |
| Icom Manual Download | fonte oficial primária | VHF fixo e portátil | simples para baixar manual por modelo | algumas variantes regionais exigem código completo | [Icom](https://www.icomamerica.com/support/manual/) |
| ManualsLib | espelho externo | legado, séries fora de linha, acervos dispersos | usar como camada 3 para confirmar existência de modelo e documento | não é fonte oficial; revisar revisão e compatibilidade antes de adotar | [ManualsLib](https://www.manualslib.com/) |

## Aliases de marca que precisam ser normalizados

| Nome encontrado no texto ou no mercado | Marca / portal atual para busca | Observação operacional |
| --- | --- | --- |
| Kohler Marine | Rehlko Marine | o fabricante atual expõe os produtos em `marine.rehlko.com`, mas o mercado ainda fala `Kohler` |
| Onan | Cummins / Cummins Onan | muitos barcos citam `Onan` sem dizer `Cummins`; convém pesquisar ambos |
| Cruisair | Dometic | a própria Dometic informa que `Cruisair is now Dometic` |
| Condaria | Dometic | a própria Dometic informa que `Condaria is now Dometic`; tratar como linha histórica, não como marca-matriz |
| Marine Air | Dometic | também reabsorvido no guarda-chuva Dometic |
| Rule | Xylem / Rule | a marca é `Rule`, mas o host e documentação vivem em `xylem.com` |
| Jabsco | Xylem / Jabsco | o mercado usa `Jabsco`, mas o suporte está sob Xylem |

## Marcas-matriz que merecem nota própria

- usar [[Matriz Dometic — Subgrupos, Linhas e Documentos]] para `Dometic`, `Cruisair`, `Condaria` e `Marine Air`;
- usar [[Matriz de Modelos e Versões — Geradores]] para `Cummins/Onan` e `Rehlko/Kohler`;
- usar [[Matriz de Marcas Matriz — Ecossistemas e Subgrupos]] para visão transversal de grupos com sublinhas e catálogos corporativos.

## Como usar o espelho externo sem contaminar o acervo

1. Confirmar primeiro se existe portal oficial ou PDF oficial.
2. Se o modelo for legado ou o oficial estiver opaco, usar o espelho para descobrir nome, família, revisão e tipo de documento.
3. Registrar a origem na curadoria:
   - `fonte_oficial`;
   - `fonte_oficial_secundaria`;
   - `espelho_externo`.
4. Quando o acervo local nascer, marcar claramente se o arquivo veio de espelho e se já foi confirmado por fabricante.

## Espelhos externos que valem monitoramento

| Repositório | Valor prático | Risco principal | Exemplo útil |
| --- | --- | --- | --- |
| ManualsLib | enorme cobertura de legado, especialmente em geração, bombas e sanitário | revisão errada, documento incompleto ou classificação ruim | [Onan brand index](https://www.manualslib.com/brand/onan/) |
| ManualsLib | útil para marcas que mudaram de nome ou sumiram do portal atual | nomenclatura inconsistente | [Kohler 6EKOD](https://www.manualslib.com/products/Kohler-6ekod-3799386.html) |
| ManualsLib | bom para mapear famílias recorrentes antes da coleta manual | não substitui validação por fabricante | [JABSCO brand index](https://www.manualslib.com/brand/jabsco/) |

## Catálogos e guias corporativos que valem a coleta

| Marca / grupo | Documento | Tipo | URL |
| --- | --- | --- | --- |
| Cummins | Marine Products Guide 2025 | product guide | [PDF](https://mart.cummins.com/imagelibrary/data/assetfiles/0032264.pdf) |
| Rehlko Marine | Literature hub | brochures, specification sheets, pocket guide | [Literature](https://www.marine.rehlko.com/brochures-literature) |
| Dometic | Marine AC Guide | buying guide / catálogo técnico | [PDF](https://www.dometic.com/globalassets/1-outdoor/out-category-pages/climate--comfort/air-conditioners/dometic-marine-ac-guide-2023.pdf) |
| Dometic | Marine Sanitation Guide | buying guide / catálogo técnico | [PDF](https://www.dometic.com/globalassets/1-outdoor/out-buying-guides/boat-toilets/dometic-marine-sanitation-guide-202363.pdf?ref=ACB369A871) |
| Webasto | Cooling overview / Marine catalog | cat?logo corporativo + entrada de downloads | [Cooling](https://www.webasto.com/en-us/cooling.html) |
| Mabru | Marine Air Conditioner Installation Manual 2025 | manual de instala??o e troubleshooting | [PDF](https://mabrupowersystems.com/wp-content/uploads/2025/04/Mabru-Marine-Air-Conditioner-Installation-Manual-2025.pdf) |
| FRIGOMAR | Download hub | datasheets, brochures e material t?cnico por fam?lia | [Download](https://www.frigomar.com/en/download/) |
| H-Tec | On Board / catálogo institucional | brochure corporativo e mapa de linhas | [PDF](https://cdnc.heyzine.com/files/uploaded/cd9e129d3571f2a543bcf1092cba927781018aa8.pdf) |
| VETUS | Catalogue 2026–2027 | catálogo corporativo | [VETUS Catalogue](https://vetus.com/usa/vetus-catalogue/) |
| Xylem / Rule | Rule Quick Reference Flyer | sales flyer / minicatálogo | [Rule Documents](https://www.xylem.com/de-de/brands/rule/documents/) |
| Xylem / Jabsco | Jabsco Marine Toilets Portfolio | portfolio guide | [PDF](https://www.xylem.com/siteassets/brand/jabsco/campaigns/jabsco-toilet-portfolio-f100-480-rev-a.pdf) |
| Xylem / Jabsco | Engine Cooling Pump Database | database / cross-reference | [PDF](https://www.xylem.com/siteassets/brand/jabsco/resources/specification/jabsco-engine-cooling-pump-database-f100-468-web.pdf) |

## Onda recomendada de abertura `source-first`

1. Geradores: `Cummins Onan` e `Rehlko/Kohler`.
2. Climatiza??o e conforto: `Dometic / Cruisair / Marine Air`, `Webasto`, `Mabru`, `FRIGOMAR` e `H-Tec`.
3. Bombas, bilge e sanitário: `Jabsco / Rule`.
4. Thrusters e utilidades: `VETUS`, depois `Lewmar` e `Sleipner`.
5. Só depois expandir o long tail por categoria.

## Entrega operacional que esta nota destrava

- criar backlog por `fonte` e não só por `marca`;
- abrir tabela `marca do texto x marca atual x portal correto`;
- reduzir perda de tempo com busca rasa em Google;
- separar desde já o que é `acervo oficial` do que é `acervo de espelho`.
