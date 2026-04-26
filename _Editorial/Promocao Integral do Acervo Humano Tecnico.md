---
title: "Promocao Integral do Acervo Humano Tecnico"
note_type: "audit"
domain: "90_Revisao_Manual"
status: "active-curation"
reviewed_on: "2026-04-25"
review_jurisdiction: "Brasil"
aliases:
  - "Promocao Integral PDF do Acervo Humano"
  - "Promocao em Massa do Acervo Humano Tecnico"
related_notes:
  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Local - Indice Gerado"
  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado"
  - "90_Revisao_Manual/Acervo Humano Tecnico - Indice Gerado"
---

# Promocao Integral do Acervo Humano Tecnico

> [!abstract] Resumo tecnico
> Esta auditoria registra a promocao em massa dos PDFs tecnicos do staging humano para o acervo principal PDF-first.
> Os originais foram preservados no staging para rastreabilidade; arquivos HTML e imagens ficam em fila separada de conversao/normalizacao.

## Escopo

- modo: `aplicado`
- gerado em UTC: `2026-04-26T02:53:42.484865+00:00`
- PDFs tecnicos avaliados: `230`
- PDFs copiados agora: `202`
- PDFs ja presentes por hash no acervo principal: `28`
- PDFs planejados em dry-run: `0`
- arquivos nao-PDF mantidos no staging: `67`

## Distribuicao por sistema de destino

- `Bombas-Utilidades`: `12` PDFs
- `Campo-Clientes`: `15` PDFs
- `Climatizacao`: `9` PDFs
- `Corrosao-Seguranca`: `5` PDFs
- `Energia-DC`: `25` PDFs
- `Geradores`: `53` PDFs
- `Iluminacao-Acessorios`: `3` PDFs
- `Materiais-Internos`: `11` PDFs
- `Navegacao`: `21` PDFs
- `Propulsao-Motores`: `69` PDFs
- `Shore-Power-AC`: `7` PDFs

## Distribuicao por bucket de origem

- `00_Documentacao_de_Campo_e_Clientes`: `15` PDFs
- `01_Geradores`: `53` PDFs
- `02_Climatizacao`: `9` PDFs
- `03_Baterias_e_DC`: `25` PDFs
- `04_Shore_Power_e_AC`: `7` PDFs
- `05_Navegacao_e_Eletronicos`: `21` PDFs
- `06_Bombas_Hidraulica_e_Utilidades`: `12` PDFs
- `07_Iluminacao_Sinalizacao_e_Acessorios`: `3` PDFs
- `08_Corrosao_Bonding_e_Seguranca`: `5` PDFs
- `09_Propulsao_Motores_Estabilizacao_e_Atuacao`: `69` PDFs
- `10_Materiais_Internos_e_Cursos`: `11` PDFs

## Arquivos nao-PDF pendentes

- `.html`: `60` arquivos
- `.jpeg`: `1` arquivos
- `.jpg`: `5` arquivos
- `.png`: `1` arquivos

## Regra operacional

- PDFs sao promovidos para `Sistema/Marca/Familia/arquivo.pdf`, que e o padrao exigido pelo acervo principal e pela camada de notas companheiras.
- O script evita duplicacao por hash: se o PDF ja existe no acervo principal, ele registra `already-present` em vez de copiar outra vez.
- HTML, JPG, JPEG e PNG nao foram misturados ao acervo principal porque ainda precisam de conversao para PDF, captura limpa ou nota tecnica curada.

## Promocoes registradas

- `copied` | `00_Documentacao_de_Campo_e_Clientes/a-c-raphael.pdf` -> `Campo-Clientes/Referencia-Campo/A-C-RAPHAEL/referencia-campo__a-c-raphael__techref__h-aa444c6c1c41.pdf` | `aa444c6c1c41`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/analise-para-instalacao-dos-transducers-ga-a573969e.pdf` -> `Campo-Clientes/Referencia-Campo/analise-para-instalacao/referencia-campo__analise-para-instala__techref__h-7e33a63e0684.pdf` | `7e33a63e0684`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/diagrama-esquematico-de-ligacao-dos-equipa-f4d827e7.pdf` -> `Campo-Clientes/Referencia-Campo/diagrama-esquematico-lig/referencia-campo__diagrama-esquematico__doc__h-c36426e5182f.pdf` | `c36426e5182f`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/diagrama-victron-invert-raphael-c-rj.pdf` -> `Campo-Clientes/Victron/Geral/victron__geral__doc__h-3fe450185b8e.pdf` | `3fe450185b8e`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/diagramas-som-fusion-jl-audio-raphael-c-rj.pdf` -> `Campo-Clientes/Referencia-Campo/diagramas-som-fusion-aud/referencia-campo__diagramas-som-fusion__doc__h-64d239534599.pdf` | `64d239534599`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/esboco-instalacao-camera-farol-radar-raphael-c-rj.pdf` -> `Campo-Clientes/Referencia-Campo/esboco-instalacao-camera/referencia-campo__esboco-instalacao-ca__techref__h-5e99575ddd2c.pdf` | `5e99575ddd2c`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/estudo-e-diagramas-do-sistema-hidraulico-d-932ba9b7.pdf` -> `Campo-Clientes/Referencia-Campo/estudo-diagramas-sistema/referencia-campo__estudo-diagramas-sis__doc__h-fa7ae235245d.pdf` | `fa7ae235245d`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/estudo-painel-garnet-300ht-raphael-c-rj.pdf` -> `Campo-Clientes/Referencia-Campo/estudo-painel-garnet-300/referencia-campo__estudo-painel-garnet__techref__h-d26d1828a491.pdf` | `d26d1828a491`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/Imagens_e_Recortes_Tecnicos/00206bf595ae240412115759.pdf` -> `Campo-Clientes/Referencia-Campo/00206BF595AE240412115759/referencia-campo__00206bf595ae24041211__techref__h-4f030a8a2591.pdf` | `4f030a8a2591`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/Imagens_e_Recortes_Tecnicos/c-users-nalmeida-appdata-local-temp-26-46885c42.pdf` -> `Campo-Clientes/Referencia-Campo/Imagens-e-Recortes-Tecni/referencia-campo__imagens-e-recortes-t__techref__h-aa138d8c8774.pdf` | `aa138d8c8774`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/Imagens_e_Recortes_Tecnicos/DOC-20180206-WA0045.pdf` -> `Campo-Clientes/Referencia-Campo/DOC-20180206-WA0045/referencia-campo__doc-20180206-wa0045__techref__h-8d05a269d0b0.pdf` | `8d05a269d0b0`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/Imagens_e_Recortes_Tecnicos/foto-de-p-303-241gina-inteira.pdf` -> `Campo-Clientes/Referencia-Campo/Imagens-e-Recortes-Tecni/referencia-campo__imagens-e-recortes-t__techref__h-7be021d8f385.pdf` | `7be021d8f385`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/Imagens_e_Recortes_Tecnicos/IMG-20230614-WA0001.pdf` -> `Campo-Clientes/Referencia-Campo/IMG-20230614-WA0001/referencia-campo__img-20230614-wa0001__techref__h-db8f43f124b2.pdf` | `db8f43f124b2`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/Imagens_e_Recortes_Tecnicos/P753.pdf` -> `Campo-Clientes/Referencia-Campo/Imagens-e-Recortes-Tecni/referencia-campo__imagens-e-recortes-t__techref__h-6af763337b2b.pdf` | `6af763337b2b`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/Imagens_e_Recortes_Tecnicos/q-q-q-q-q-q-q-q-q-q-q-q-q-q-q-q-q-q-q-q-49ec4234.pdf` -> `Campo-Clientes/Referencia-Campo/Imagens-e-Recortes-Tecni/referencia-campo__imagens-e-recortes-t__techref__h-01f752e602ba.pdf` | `01f752e602ba`
- `copied` | `01_Geradores/0981-0181-Issue-7-English.pdf` -> `Geradores/Referencia-Geradores/0981-0181-ISSUE-7-ENGLIS/referencia-gerad__0981-0181-issue-7-en__techref__h-438ff8dbb60a.pdf` | `438ff8dbb60a`
- `copied` | `01_Geradores/10850OM.pdf` -> `Geradores/Referencia-Geradores/10850OM/referencia-gerad__10850om__techref__h-08e9f6fecc42.pdf` | `08e9f6fecc42`
- `copied` | `01_Geradores/17-5mdkae.pdf` -> `Geradores/Cummins-Onan/17-5MDKAE/cummins-onan__17-5mdkae__techref__h-448b5df582c7.pdf` | `448b5df582c7`
- `copied` | `01_Geradores/32002OM.pdf` -> `Geradores/Referencia-Geradores/32002OM/referencia-gerad__32002om__techref__h-0c4ab74fef53.pdf` | `0c4ab74fef53`
- `copied` | `01_Geradores/40457-rev2-7-6btd-operator-manual.pdf` -> `Geradores/Referencia-Geradores/40457-rev2-6btd/referencia-gerad__40457-rev2-6btd__operation__h-9f154dfb466d.pdf` | `9f154dfb466d`
- `already-present` | `01_Geradores/5EFKOZD-service-manual.pdf` -> `Geradores/Rehlko-Kohler/5EFKOD/rehlko-kohler__5efkod-6ekod-9-11ekozd-7-9efkozd__service-manual__tp-6774-2014-02a.pdf` | `25c5a7676eea`
- `copied` | `01_Geradores/70384OM.pdf` -> `Geradores/Referencia-Geradores/70384OM/referencia-gerad__70384om__techref__h-20746e490d48.pdf` | `20746e490d48`
- `copied` | `01_Geradores/7953-hdkah-spec-a-n-operator-manual-2015.pdf` -> `Geradores/Cummins-Onan/Geral/cummins-onan__geral__operation__h-2f3b12f95110.pdf` | `2f3b12f95110`
- `copied` | `01_Geradores/8731-marine-electrical-products.pdf` -> `Geradores/Referencia-Geradores/8731-electrical-products/referencia-gerad__8731-electrical-prod__techref__h-f96263ee33f8.pdf` | `f96263ee33f8`
- `copied` | `01_Geradores/8732-marine-electrical-products.pdf` -> `Geradores/Referencia-Geradores/8732-electrical-products/referencia-gerad__8732-electrical-prod__techref__h-b58c6e93ee1b.pdf` | `b58c6e93ee1b`
- `copied` | `01_Geradores/900-0541b-energy-command-operation-manual.pdf` -> `Geradores/Cummins-Onan/Geral/cummins-onan__geral__operation__h-ce7111298b99.pdf` | `ce7111298b99`
- `copied` | `01_Geradores/934-0602-onan-mdl3-mdl4-mdl6-marine-genset-installation-manual-01-1991.pdf` -> `Geradores/Cummins-Onan/Geral/cummins-onan__geral__install__h-3e546f83ffea.pdf` | `3e546f83ffea`
- `already-present` | `01_Geradores/981-0181-onan-mdkbx-marine-genset-operator-manual-03-2008.pdf` -> `Geradores/Cummins-Onan/Legacy-MDKBK-MDKBN/cummins-onan__mdkbk-mdkbl-mdkbm-mdkbn__operator-manual__981-0181-2008-03.pdf` | `5f97f11c68dc`
- `copied` | `01_Geradores/avr-a-opt-01-regulador-de-tensao-analogico.pdf` -> `Geradores/Referencia-Geradores/avr-opt-regulador-tensao/referencia-gerad__avr-opt-regulador-te__techref__h-7d410be8f0a8.pdf` | `7d410be8f0a8`
- `copied` | `01_Geradores/california-proposition-65.pdf` -> `Geradores/Referencia-Geradores/CALIFORNIA-PROPOSITION-6/referencia-gerad__california-propositi__techref__h-df8e3cab395e.pdf` | `df8e3cab395e`
- `already-present` | `01_Geradores/cummins-onan__mdkad-mdkae-mdkaf__operator-manual__981-0140-1996-02.pdf` -> `Geradores/Cummins-Onan/MDKAD-MDKAE-MDKAF/cummins-onan__mdkad-mdkae-mdkaf__operator-manual__981-0140-1996-02.pdf` | `1a79566b0e5a`
- `already-present` | `01_Geradores/cummins-onan__mdkad-mdkae-mdkaf__service-manual__legacy-espelho.pdf` -> `Geradores/Cummins-Onan/MDKAD-MDKAE-MDKAF/cummins-onan__mdkad-mdkae-mdkaf__service-manual__legacy-espelho.pdf` | `437245942da1`
- `already-present` | `01_Geradores/cummins-onan__mdkad-mdkae__parts-manual__981-0264-1999-01.pdf` -> `Geradores/Cummins-Onan/MDKAD-MDKAE-MDKAF/cummins-onan__mdkad-mdkae__parts-manual__981-0264-1999-01.pdf` | `9ca5a7ef8170`
- `already-present` | `01_Geradores/cummins-onan__mdkbh__service-manual__legacy-espelho.pdf` -> `Geradores/Cummins-Onan/MDKBH/cummins-onan__mdkbh__service-manual__legacy-espelho.pdf` | `a791141a566b`
- `already-present` | `01_Geradores/cummins-onan__mdkbp-mdkbr-mdkbs__parts-manual__legacy-espelho.pdf` -> `Geradores/Cummins-Onan/Legacy-MDKBP-MDKBS/cummins-onan__mdkbp-mdkbr-mdkbs__parts-manual__legacy-espelho.pdf` | `b0df461c94d3`
- `already-present` | `01_Geradores/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__operator-manual__a052j727.pdf` -> `Geradores/Cummins-Onan/MDKDK/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__operator-manual__a052j727.pdf` | `54a3d0cea3e2`
- `already-present` | `01_Geradores/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__service-manual__legacy-espelho.pdf` -> `Geradores/Cummins-Onan/MDKDK/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__service-manual__legacy-espelho.pdf` | `21b643a8b1b7`
- `copied` | `01_Geradores/Fischer-Panda-4200-ECO-Operation-manual.pdf` -> `Geradores/Fischer-Panda/Geral/fischer-panda__geral__operation__h-41fb6a309ac3.pdf` | `41fb6a309ac3`
- `copied` | `01_Geradores/fischer-panda-4200.pdf` -> `Geradores/Fischer-Panda/FISCHER-PANDA-4200/fischer-panda__fischer-panda-4200__techref__h-e5385ebc8e0d.pdf` | `e5385ebc8e0d`
- `copied` | `01_Geradores/Fischer-Panda-7Mini.pdf` -> `Geradores/Fischer-Panda/FISCHER-PANDA-7MINI/fischer-panda__fischer-panda-7mini__techref__h-a6d160ed41d2.pdf` | `a6d160ed41d2`
- `copied` | `01_Geradores/folheto-gerador-panda-7-mini.pdf` -> `Geradores/Fischer-Panda/FOLHETO-GERADOR-PANDA-7/fischer-panda__folheto-gerador-pand__techref__h-e0643ebc72b8.pdf` | `e0643ebc72b8`
- `copied` | `01_Geradores/folheto-gerador-panda-9-dp-digital-panel-ingles.pdf` -> `Geradores/Fischer-Panda/Geral/fischer-panda__geral__techref__h-42b1f74e5c85.pdf` | `42b1f74e5c85`
- `copied` | `01_Geradores/Generator-Northern-Lights-Manual.pdf` -> `Geradores/Northern-Lights/Geral/northern-lights__geral__techref__h-ae0d5335b800.pdf` | `ae0d5335b800`
- `copied` | `01_Geradores/hdkah-hdkaj-hdkak-hdkau-hdkav-service-manual.pdf` -> `Geradores/Cummins-Onan/Geral/cummins-onan__geral__service__h-a3ae73c9a3ef.pdf` | `a3ae73c9a3ef`
- `copied` | `01_Geradores/kohler-manual-instalacao-gmg.pdf` -> `Geradores/Rehlko-Kohler/KOHLER-MANUAL-INSTALACAO/rehlko-kohler__kohler-manual-instal__techref__h-6c3aa0ac7a9f.pdf` | `6c3aa0ac7a9f`
- `copied` | `01_Geradores/machine-translated-by-google.pdf` -> `Geradores/Referencia-Geradores/MACHINE-TRANSLATED-BY-GO/referencia-gerad__machine-translated-b__techref__h-77cfe2f0c71c.pdf` | `77cfe2f0c71c`
- `copied` | `01_Geradores/manual-de-produto-126-108.pdf` -> `Geradores/Referencia-Geradores/MANUAL-DE-PRODUTO-126-10/referencia-gerad__manual-de-produto-12__techref__h-157ce2010aaa.pdf` | `157ce2010aaa`
- `copied` | `01_Geradores/manual-egc-automatic-rev02.pdf` -> `Geradores/Referencia-Geradores/MANUAL-EGC-AUTOMATIC-REV/referencia-gerad__manual-egc-automatic__techref__h-f86036e87bfc.pdf` | `f86036e87bfc`
- `copied` | `01_Geradores/manual-egc.pdf` -> `Geradores/Referencia-Geradores/MANUAL-EGC/referencia-gerad__manual-egc__techref__h-c891f41ad0f9.pdf` | `c891f41ad0f9`
- `copied` | `01_Geradores/Manual-Gerador-20-kva-com-Tramontini.pdf` -> `Geradores/Referencia-Geradores/Gerador-kva-com-Tramonti/referencia-gerad__gerador-kva-com-tram__techref__h-1f2426c552d9.pdf` | `1f2426c552d9`
- `copied` | `01_Geradores/manual-gerador-parts-e-pecas.pdf` -> `Geradores/Referencia-Geradores/MANUAL-GERADOR-PARTS-E-P/referencia-gerad__manual-gerador-parts__techref__h-ad6f5e06da71.pdf` | `ad6f5e06da71`
- `already-present` | `01_Geradores/MDKBK-BL-BM-BN-BP-BR-BS-BT-BU-BV-Service-Manual.pdf` -> `Geradores/Cummins-Onan/Legacy-MDKBK-MDKBN/cummins-onan__mdkbk-mdkbl-mdkbm-mdkbn__service-manual__legacy-espelho.pdf` | `1a505c22df00`
- `copied` | `01_Geradores/mdkbk.pdf` -> `Geradores/Cummins-Onan/Geral/cummins-onan__geral__techref__h-5015b93e504c.pdf` | `5015b93e504c`
- `already-present` | `01_Geradores/mdkdp-dr-ds-dt-du-dv-service-manual.pdf` -> `Geradores/Cummins-Onan/MDKDP-MDKDR-MDKDV/cummins-onan__mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv__service-manual__a046j602.pdf` | `3e936560c78c`
- `copied` | `01_Geradores/model-9eozd-60-hz-7efozd-50-hz.pdf` -> `Geradores/Referencia-Geradores/9eozd-7efozd/referencia-gerad__9eozd-7efozd__techref__h-ed09239a8d50.pdf` | `ed09239a8d50`
- `copied` | `01_Geradores/modulo1-geradores-ca-1-a-21-2007.pdf` -> `Geradores/Referencia-Geradores/modulo1-geradores-2007/referencia-gerad__modulo1-geradores-20__techref__h-d2a13fccc230.pdf` | `d2a13fccc230`
- `copied` | `01_Geradores/northen-lights-generator-om844w3.pdf` -> `Geradores/Northern-Lights/Geral/northern-lights__geral__techref__h-e7a61856413f.pdf` | `e7a61856413f`
- `copied` | `01_Geradores/onan-mcck-marine-genset-manual.pdf` -> `Geradores/Cummins-Onan/Geral/cummins-onan__geral__techref__h-d61fcf04667d.pdf` | `d61fcf04667d`
- `copied` | `01_Geradores/onan-troubleshooting-guide-codes.pdf` -> `Geradores/Cummins-Onan/Geral/cummins-onan__geral__trouble__h-b69a70cf5051.pdf` | `b69a70cf5051`
- `copied` | `01_Geradores/operator-manual-marine-diesel-generators.pdf` -> `Geradores/Referencia-Geradores/diesel-generators/referencia-gerad__diesel-generators__operation__h-6aa974905459.pdf` | `6aa974905459`
- `copied` | `01_Geradores/panda-15mini-pms-digital-vcs183-eng-r03.pdf` -> `Geradores/Fischer-Panda/Geral/fischer-panda__geral__techref__h-11d07a48e60e.pdf` | `11d07a48e60e`
- `copied` | `01_Geradores/panda-4200-4500eco-r01.pdf` -> `Geradores/Fischer-Panda/PANDA-4200-4500ECO-R01/fischer-panda__panda-4200-4500eco-r__techref__h-6cdfb70a12f6.pdf` | `6cdfb70a12f6`
- `copied` | `01_Geradores/Panda-4K-5K-7K-manual.pdf` -> `Geradores/Fischer-Panda/PANDA-4K-5K-7K-MANUAL/fischer-panda__panda-4k-5k-7k-manua__techref__h-01fb383084e6.pdf` | `01fb383084e6`
- `copied` | `01_Geradores/panda-4k-pms-eng-r01.pdf` -> `Geradores/Fischer-Panda/PANDA-4K-PMS-ENG-R01/fischer-panda__panda-4k-pms-eng-r01__techref__h-8f734f18a72c.pdf` | `8f734f18a72c`
- `copied` | `01_Geradores/Panda-7K-PMS.pdf` -> `Geradores/Fischer-Panda/PANDA-7K-PMS/fischer-panda__panda-7k-pms__techref__h-c8025edb30d6.pdf` | `c8025edb30d6`
- `copied` | `01_Geradores/reguladores-de-tensao-digitais.pdf` -> `Geradores/Referencia-Geradores/reguladores-tensao-digit/referencia-gerad__reguladores-tensao-d__techref__h-50e847969261.pdf` | `50e847969261`
- `copied` | `01_Geradores/service-manual.pdf` -> `Geradores/Referencia-Geradores/SERVICE-MANUAL/referencia-gerad__service-manual__service__h-6ee62475cc8c.pdf` | `6ee62475cc8c`
- `copied` | `01_Geradores/universidade-federal-do-amapa-departamento-de-ciencias-exatas-e-t-35c52013.pdf` -> `Geradores/Referencia-Geradores/universidade-federal-ama/referencia-gerad__universidade-federal__techref__h-5ca233e3515f.pdf` | `5ca233e3515f`
- `copied` | `02_Climatizacao/chilled-water-air-conditioning.pdf` -> `Climatizacao/Referencia-Climatizacao/chilled-water-conditioni/referencia-clima__chilled-water-condit__techref__h-192a095558b2.pdf` | `192a095558b2`
- `already-present` | `02_Climatizacao/cruisair-marine-a-c-systems-troubleshooting-guide.pdf` -> `Climatizacao/Dometic/Self-Contained/dometic-cruisair__self-contained-air-conditioner__troubleshooting-guide__legacy-espelho.pdf` | `0b38d83d6d12`
- `copied` | `02_Climatizacao/cruisair-tempered-water-system.pdf` -> `Climatizacao/Dometic/Geral/dometic__geral__techref__h-ce30568e795f.pdf` | `ce30568e795f`
- `copied` | `02_Climatizacao/dometic-chilled-water-operating-manual.pdf` -> `Climatizacao/Dometic/Geral/dometic__geral__techref__h-c0ad0cafc451.pdf` | `c0ad0cafc451`
- `already-present` | `02_Climatizacao/dometic-cruisair__marine-air-conditioners__price-list__2015.pdf` -> `Climatizacao/Dometic/Self-Contained/dometic-cruisair__marine-air-conditioners__price-list__2015.pdf` | `cc259fa0437f`
- `copied` | `02_Climatizacao/dometic-mtcg-9108893793-75371.pdf` -> `Climatizacao/Dometic/Geral/dometic__geral__techref__h-2fc37685edf5.pdf` | `2fc37685edf5`
- `already-present` | `02_Climatizacao/dometic__marine-air-conditioners__price-list__2024.pdf` -> `Climatizacao/Dometic/Self-Contained/dometic__marine-air-conditioners__price-list__2024.pdf` | `6a5287a55b9b`
- `already-present` | `02_Climatizacao/dx-remote-and-self-contained-a-c-v-installation-operation-manual.pdf` -> `Climatizacao/Dometic/Self-Contained/dometic-cruisair__self-contained-air-conditioner__installation-manual__dx-remote-legacy-espelho.pdf` | `0ca46dcdba29`
- `copied` | `02_Climatizacao/manual-ar-condicionado.pdf` -> `Climatizacao/Referencia-Climatizacao/MANUAL-AR-CONDICIONADO/referencia-clima__manual-ar-condiciona__techref__h-08991e8e30fa.pdf` | `08991e8e30fa`
- `copied` | `03_Baterias_e_DC/19-informativo-tecnico-no.pdf` -> `Energia-DC/Referencia-Energia-DC/19-INFORMATIVO-TECNICO-N/referencia-energ__19-informativo-tecni__techref__h-7abdcbd8eb77.pdf` | `7abdcbd8eb77`
- `copied` | `03_Baterias_e_DC/722-NE.pdf` -> `Energia-DC/Referencia-Energia-DC/722-NE/referencia-energ__722-ne__techref__h-707b3fb0f560.pdf` | `707b3fb0f560`
- `copied` | `03_Baterias_e_DC/AB12210.pdf` -> `Energia-DC/Referencia-Energia-DC/AB12210/referencia-energ__ab12210__techref__h-24b7a5c72622.pdf` | `24b7a5c72622`
- `copied` | `03_Baterias_e_DC/abso-charger.pdf` -> `Energia-DC/Referencia-Energia-DC/ABSO-CHARGER/referencia-energ__abso-charger__techref__h-1593c97dadc4.pdf` | `1593c97dadc4`
- `copied` | `03_Baterias_e_DC/atlas-eolico-rs.pdf` -> `Energia-DC/Referencia-Energia-DC/ATLAS-EOLICO-RS/referencia-energ__atlas-eolico-rs__techref__h-32aaad151d9e.pdf` | `32aaad151d9e`
- `copied` | `03_Baterias_e_DC/bch-opt-41-bivolt.pdf` -> `Energia-DC/Referencia-Energia-DC/BCH-OPT-41-BIVOLT/referencia-energ__bch-opt-41-bivolt__techref__h-916f50c87c38.pdf` | `916f50c87c38`
- `copied` | `03_Baterias_e_DC/catalogo-inversor-2023-digital.pdf` -> `Energia-DC/Referencia-Energia-DC/inversor-2023-digital/referencia-energ__inversor-2023-digita__catalog__h-dc95ed231199.pdf` | `dc95ed231199`
- `copied` | `03_Baterias_e_DC/catalogo-usina-impresso-2022.pdf` -> `Energia-DC/Usina/CATALOGO-USINA-IMPRESSO/usina__catalogo-usina-impre__catalog__h-e962a9637eb9.pdf` | `e962a9637eb9`
- `copied` | `03_Baterias_e_DC/conceptual-diagram-dc-overview.pdf` -> `Energia-DC/Referencia-Energia-DC/conceptual-overview/referencia-energ__conceptual-overview__doc__h-1308555afbe0.pdf` | `1308555afbe0`
- `copied` | `03_Baterias_e_DC/industrial-and-marine-engines.pdf` -> `Energia-DC/Referencia-Energia-DC/industrial-engines/referencia-energ__industrial-engines__techref__h-12fb7a4e0d38.pdf` | `12fb7a4e0d38`
- `copied` | `03_Baterias_e_DC/irfz48npbf.pdf` -> `Energia-DC/Referencia-Energia-DC/IRFZ48NPBF/referencia-energ__irfz48npbf__techref__h-737bb8cabd25.pdf` | `737bb8cabd25`
- `copied` | `03_Baterias_e_DC/Manual-BPP2-PT.pdf` -> `Energia-DC/Referencia-Energia-DC/MANUAL-BPP2-PT/referencia-energ__manual-bpp2-pt__techref__h-732424d4c60c.pdf` | `732424d4c60c`
- `copied` | `03_Baterias_e_DC/Manual-Digital-Multi-Control-GX-Panel-EN-NL-FR-DE-ES.pdf` -> `Energia-DC/Referencia-Energia-DC/Digital-Multi-Panel/referencia-energ__digital-multi-panel__techref__h-a25f30d8271c.pdf` | `a25f30d8271c`
- `copied` | `03_Baterias_e_DC/manual-do-produto.pdf` -> `Energia-DC/Referencia-Energia-DC/MANUAL-DO-PRODUTO/referencia-energ__manual-do-produto__techref__h-d5d6dc1cdb8b.pdf` | `d5d6dc1cdb8b`
- `copied` | `03_Baterias_e_DC/more-user-manuals-on.pdf` -> `Energia-DC/Referencia-Energia-DC/MORE-USER-MANUALS-ON/referencia-energ__more-user-manuals-on__operation__h-62ad6d381a18.pdf` | `62ad6d381a18`
- `copied` | `03_Baterias_e_DC/motive-power-dup-2.pdf` -> `Energia-DC/Referencia-Energia-DC/MOTIVE-POWER-DUP-2/referencia-energ__motive-power-dup-2__techref__h-94413f9df153.pdf` | `94413f9df153`
- `copied` | `03_Baterias_e_DC/motive-power.pdf` -> `Energia-DC/Referencia-Energia-DC/MOTIVE-POWER/referencia-energ__motive-power__techref__h-7331909288a7.pdf` | `7331909288a7`
- `copied` | `03_Baterias_e_DC/nautical-equipment-evolution.pdf` -> `Energia-DC/Referencia-Energia-DC/NAUTICAL-EQUIPMENT-EVOLU/referencia-energ__nautical-equipment-e__techref__h-87ed2f565544.pdf` | `87ed2f565544`
- `copied` | `03_Baterias_e_DC/owner-s-manual.pdf` -> `Energia-DC/Referencia-Energia-DC/OWNER-S-MANUAL/referencia-energ__owner-s-manual__techref__h-009988c7277b.pdf` | `009988c7277b`
- `copied` | `03_Baterias_e_DC/pcwmvar.pdf` -> `Energia-DC/Referencia-Energia-DC/pcwmvar/referencia-energ__pcwmvar__techref__h-c3d93df4459e.pdf` | `c3d93df4459e`
- `copied` | `03_Baterias_e_DC/rev-2-04-17.pdf` -> `Energia-DC/Referencia-Energia-DC/REV-2-04-17/referencia-energ__rev-2-04-17__techref__h-1604851083fa.pdf` | `1604851083fa`
- `already-present` | `03_Baterias_e_DC/the-12-volt-doctors-practical-handbook.pdf` -> `Complementar-Brasil/Referencias-Gerais/12V/referencia-geral__12-volt-doctors__handbook__practical-12v-systems.pdf` | `59ed52a6fe64`
- `copied` | `03_Baterias_e_DC/user-manual-for-interbus-s.pdf` -> `Energia-DC/Referencia-Energia-DC/USER-MANUAL-FOR-INTERBUS/referencia-energ__user-manual-for-inte__operation__h-5b62a14729bf.pdf` | `5b62a14729bf`
- `copied` | `03_Baterias_e_DC/users-manual.pdf` -> `Energia-DC/Referencia-Energia-DC/USERS-MANUAL/referencia-energ__users-manual__techref__h-f533f12bb49d.pdf` | `f533f12bb49d`
- `copied` | `03_Baterias_e_DC/www-sparkpower-com-br.pdf` -> `Energia-DC/Referencia-Energia-DC/WWW-SPARKPOWER-COM-BR/referencia-energ__www-sparkpower-com-b__techref__h-fbe645bcabe8.pdf` | `fbe645bcabe8`
- `copied` | `04_Shore_Power_e_AC/baixa-tensao.pdf` -> `Shore-Power-AC/Referencia-Shore-Power/BAIXA-TENSAO/referencia-shore__baixa-tensao__techref__h-76ea282b86f8.pdf` | `76ea282b86f8`
- `copied` | `04_Shore_Power_e_AC/catalogo-chave-rotativa-lw26-rev-set-18.pdf` -> `Shore-Power-AC/Referencia-Shore-Power/chave-rotativa-lw26-rev/referencia-shore__chave-rotativa-lw26__catalog__h-d27ee4babe8c.pdf` | `d27ee4babe8c`
- `copied` | `04_Shore_Power_e_AC/co-004-15-folder-linha-automotiva-21x29-7cm-ok.pdf` -> `Shore-Power-AC/Referencia-Shore-Power/004-folder-linha-automot/referencia-shore__004-folder-linha-aut__techref__h-f1c574a9604f.pdf` | `f1c574a9604f`
- `copied` | `04_Shore_Power_e_AC/licenca-de-uso-exclusivo-para-target-engenharia-e-consulto-572b6510.pdf` -> `Shore-Power-AC/Referencia-Shore-Power/licenca-uso-exclusivo-pa/referencia-shore__licenca-uso-exclusiv__techref__h-610e30c82eec.pdf` | `610e30c82eec`
- `copied` | `04_Shore_Power_e_AC/LUMISHORE-2024-SYBROCHURE.pdf` -> `Shore-Power-AC/Lumishore/LUMISHORE-2024-SYBROCHUR/lumishore__lumishore-2024-sybro__techref__h-48d3ef482a88.pdf` | `48d3ef482a88`
- `copied` | `04_Shore_Power_e_AC/stop-0-start.pdf` -> `Shore-Power-AC/Referencia-Shore-Power/STOP-0-START/referencia-shore__stop-0-start__techref__h-5b5043777b35.pdf` | `5b5043777b35`
- `copied` | `04_Shore_Power_e_AC/technical-data-sheet.pdf` -> `Shore-Power-AC/Referencia-Shore-Power/TECHNICAL-DATA-SHEET/referencia-shore__technical-data-sheet__techref__h-fbc265150af8.pdf` | `fbc265150af8`
- `already-present` | `05_Navegacao_e_Eletronicos/0-75-6-5-6.pdf` -> `Navegacao/Standard-Horizon/GX2000-GX2150/standard-horizon__gx2000-gx2150__operation-manual__em044n160-5292013.pdf` | `b10aa04e9fed`
- `already-present` | `05_Navegacao_e_Eletronicos/116-mm-4-9-16-in.pdf` -> `Navegacao/Garmin/GHC-50/garmin__ghc-50__display-cutout-template__legacy-espelho.pdf` | `a3ef36f782be`
- `already-present` | `05_Navegacao_e_Eletronicos/fi-5002-junction-box-installation-instructions.pdf` -> `Navegacao/Furuno/FI-5002/furuno__fi-5002__installation-manual__rev-a.pdf` | `b2baab940a87`
- `already-present` | `05_Navegacao_e_Eletronicos/furuno-can-bus-network-design-guide.pdf` -> `Navegacao/Furuno/CAN-Bus/furuno__can-bus__network-design-guide__legacy-espelho.pdf` | `4d757d2c1a7d`
- `already-present` | `05_Navegacao_e_Eletronicos/gps-17x-hvs-technical-specifications.pdf` -> `Navegacao/Garmin/GPS-17x-HVS/garmin__gps-17x-hvs__technical-specifications__legacy-espelho.pdf` | `bc429e98748d`
- `already-present` | `05_Navegacao_e_Eletronicos/gpsmap-4000-5000-series-installation-instructions.pdf` -> `Navegacao/Garmin/GPSMAP-4000-5000/garmin__gpsmap-4000-5000__installation-manual__en.pdf` | `f8a3c18f958b`
- `copied` | `05_Navegacao_e_Eletronicos/installation-and-wire-connection-manual.pdf` -> `Navegacao/Referencia-Navegacao/wire-connection/referencia-naveg__wire-connection__techref__h-1ea33ab0b704.pdf` | `1ea33ab0b704`
- `copied` | `05_Navegacao_e_Eletronicos/intellian-i3-i4-i4p-i6-i6p-i6pe-i6w-qui-fa98cb0e.pdf` -> `Navegacao/Intellian/Geral/intellian__geral__techref__h-012502f49cf7.pdf` | `012502f49cf7`
- `copied` | `05_Navegacao_e_Eletronicos/Interbus.pdf` -> `Navegacao/Referencia-Navegacao/Interbus/referencia-naveg__interbus__techref__h-03d72ce8f84e.pdf` | `03d72ce8f84e`
- `copied` | `05_Navegacao_e_Eletronicos/manual-2019-12-19-08-26-08-rs40-rs40-b-and-hs40.pdf` -> `Navegacao/Referencia-Navegacao/2019-rs40-rs40-hs40/referencia-naveg__2019-rs40-rs40-hs40__techref__h-82a849d86a53.pdf` | `82a849d86a53`
- `copied` | `05_Navegacao_e_Eletronicos/network-expansion-port-2-nep-2.pdf` -> `Navegacao/Referencia-Navegacao/network-expansion-port-n/referencia-naveg__network-expansion-po__techref__h-625e93f09380.pdf` | `625e93f09380`
- `copied` | `05_Navegacao_e_Eletronicos/NRX300.pdf` -> `Navegacao/Referencia-Navegacao/NRX300/referencia-naveg__nrx300__techref__h-beb3139454cf.pdf` | `beb3139454cf`
- `copied` | `05_Navegacao_e_Eletronicos/nx403a.pdf` -> `Navegacao/Referencia-Navegacao/NX403A/referencia-naveg__nx403a__techref__h-ebee10527d4f.pdf` | `ebee10527d4f`
- `copied` | `05_Navegacao_e_Eletronicos/owner-s-guide-and-installation-instructions.pdf` -> `Navegacao/Referencia-Navegacao/owner/referencia-naveg__owner__techref__h-96a97cf2327d.pdf` | `96a97cf2327d`
- `already-present` | `05_Navegacao_e_Eletronicos/quantumtm-instrucoes-de.pdf` -> `Navegacao/Raymarine/Quantum/raymarine__quantum-radar__manual__portugues-legacy-espelho.pdf` | `323f97e95983`
- `copied` | `05_Navegacao_e_Eletronicos/quick-start-guide-and-installation-manual-guide-de-4ec49ee6.pdf` -> `Navegacao/Quick/Geral/quick__geral__install__h-a92e0cb1f37d.pdf` | `a92e0cb1f37d`
- `already-present` | `05_Navegacao_e_Eletronicos/seatalk-refrence-manual.pdf` -> `Navegacao/Raymarine/SeaTalk/raymarine__seatalk__cabling-and-connections__legacy-espelho.pdf` | `4bcd9af75d0d`
- `already-present` | `05_Navegacao_e_Eletronicos/st6002-smartpilot-controller-operating-guide.pdf` -> `Navegacao/Raymarine/SmartPilot-ST6002/raymarine__smartpilot-st6002__operation-manual__legacy-espelho.pdf` | `af5bab3a75f9`
- `already-present` | `05_Navegacao_e_Eletronicos/supplemental-instructions.pdf` -> `Navegacao/Furuno/FI-5002/furuno__fi-5002__supplemental-instructions__legacy-espelho.pdf` | `97663dc66b1a`
- `copied` | `05_Navegacao_e_Eletronicos/technical-manual.pdf` -> `Navegacao/Referencia-Navegacao/TECHNICAL-MANUAL/referencia-naveg__technical-manual__techref__h-555b0f8483b8.pdf` | `555b0f8483b8`
- `copied` | `05_Navegacao_e_Eletronicos/voce-conhece-voce-confia.pdf` -> `Navegacao/Referencia-Navegacao/VOCE-CONHECE-VOCE-CONFIA/referencia-naveg__voce-conhece-voce-co__techref__h-75ac1c0ece8d.pdf` | `75ac1c0ece8d`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/60020-0024.pdf` -> `Bombas-Utilidades/Referencia-Bombas-Utilidades/60020-0024/referencia-bomba__60020-0024__techref__h-dbaaa72ddf4f.pdf` | `dbaaa72ddf4f`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/capdf21.pdf` -> `Bombas-Utilidades/Referencia-Bombas-Utilidades/CAPDF21/referencia-bomba__capdf21__techref__h-70879e17812f.pdf` | `70879e17812f`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/dockapreto.pdf` -> `Bombas-Utilidades/Referencia-Bombas-Utilidades/dockapreto/referencia-bomba__dockapreto__techref__h-dd03a80cc29c.pdf` | `dd03a80cc29c`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/dockavermelho.pdf` -> `Bombas-Utilidades/Referencia-Bombas-Utilidades/dockavermelho/referencia-bomba__dockavermelho__techref__h-45bd6abdd316.pdf` | `45bd6abdd316`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/document-91095466-installation-guide-mini-pressurizador-com-pressostato-eletronico-externo-agua-quente-350w-220v-syllent.pdf` -> `Bombas-Utilidades/Referencia-Bombas-Utilidades/91095466-mini-pressuriza/referencia-bomba__91095466-mini-pressu__techref__h-b6d3ca86776f.pdf` | `b6d3ca86776f`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/electric-motor-ct165.pdf` -> `Bombas-Utilidades/Referencia-Bombas-Utilidades/ELECTRIC-MOTOR-CT165/referencia-bomba__electric-motor-ct165__techref__h-38b83326b8ec.pdf` | `38b83326b8ec`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/experience-our-innovation.pdf` -> `Bombas-Utilidades/Referencia-Bombas-Utilidades/EXPERIENCE-OUR-INNOVATIO/referencia-bomba__experience-our-innov__techref__h-b98aba78ee2c.pdf` | `b98aba78ee2c`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/johnson-pump-marine-aquat-marine-toilet-stan-1154108b.pdf` -> `Bombas-Utilidades/Johnson-Pump/Geral/johnson-pump__geral__techref__h-12d03a0cae41.pdf` | `12d03a0cae41`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/manual-de-instrucoes-para-bomba-de-aguas-cin-d98d4d4c.pdf` -> `Bombas-Utilidades/Referencia-Bombas-Utilidades/instrucoes-para-bomba-ag/referencia-bomba__instrucoes-para-bomb__techref__h-37d247ffbe3a.pdf` | `37d247ffbe3a`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/seelevel-ii-tm.pdf` -> `Bombas-Utilidades/Referencia-Bombas-Utilidades/SEELEVEL-II-TM/referencia-bomba__seelevel-ii-tm__techref__h-9e532fc28c6f.pdf` | `9e532fc28c6f`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/verhroicrizeolnlitaol-wriinzdzlaossnetsale-m-8fa8750d.pdf` -> `Bombas-Utilidades/Referencia-Bombas-Utilidades/verhroicrizeolnlitaol-wr/referencia-bomba__verhroicrizeolnlitao__techref__h-43de0e5e640b.pdf` | `43de0e5e640b`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/whale-2023.pdf` -> `Bombas-Utilidades/Whale/WHALE-2023/whale__whale-2023__techref__h-b0b5ae3b5e45.pdf` | `b0b5ae3b5e45`
- `copied` | `07_Iluminacao_Sinalizacao_e_Acessorios/officine-comercial-ltda.pdf` -> `Iluminacao-Acessorios/Referencia-Iluminacao/OFFICINE-COMERCIAL-LTDA/referencia-ilumi__officine-comercial-l__techref__h-12190342ffa2.pdf` | `12190342ffa2`
- `copied` | `07_Iluminacao_Sinalizacao_e_Acessorios/owner-s-manual.pdf` -> `Iluminacao-Acessorios/Referencia-Iluminacao/OWNER-S-MANUAL/referencia-ilumi__owner-s-manual__techref__h-bf7c64ed69bf.pdf` | `bf7c64ed69bf`
- `copied` | `07_Iluminacao_Sinalizacao_e_Acessorios/SPL.pdf` -> `Iluminacao-Acessorios/Referencia-Iluminacao/SPL/referencia-ilumi__spl__techref__h-c82ae584ac5b.pdf` | `c82ae584ac5b`
- `copied` | `08_Corrosao_Bonding_e_Seguranca/aluminio.pdf` -> `Corrosao-Seguranca/Referencia-Corrosao-Seguranc/aluminio/referencia-corro__aluminio__techref__h-00255db22e9b.pdf` | `00255db22e9b`
- `copied` | `08_Corrosao_Bonding_e_Seguranca/caro-cliente.pdf` -> `Corrosao-Seguranca/Referencia-Corrosao-Seguranc/CARO-CLIENTE/referencia-corro__caro-cliente__techref__h-b9e5f60a342e.pdf` | `b9e5f60a342e`
- `already-present` | `08_Corrosao_Bonding_e_Seguranca/corrosion-measurement.pdf` -> `Complementar-Brasil/Corrosao/DPH-DPR-IPS/referencia-tecnica__corrosao-eletrolise-dph-dpr-ips__medicoes.pdf` | `6868a575a33a`
- `copied` | `08_Corrosao_Bonding_e_Seguranca/m-y-des-amis-b.pdf` -> `Corrosao-Seguranca/Referencia-Corrosao-Seguranc/M-Y-DES-AMIS-B/referencia-corro__m-y-des-amis-b__techref__h-3b095991edf8.pdf` | `3b095991edf8`
- `copied` | `08_Corrosao_Bonding_e_Seguranca/VERNIZ-SCHOONER.pdf` -> `Corrosao-Seguranca/Referencia-Corrosao-Seguranc/VERNIZ-SCHOONER/referencia-corro__verniz-schooner__techref__h-94080eb5ac89.pdf` | `94080eb5ac89`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/235-east-airway-boulevard-livermore-cal-c772a288.pdf` -> `Propulsao-Motores/Referencia-Propulsao/235-east-airway-boulevar/referencia-propu__235-east-airway-boul__techref__h-5c998713766c.pdf` | `5c998713766c`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/235-east-airway-boulevard-livermore-cal-fc96c680.pdf` -> `Propulsao-Motores/Referencia-Propulsao/235-east-airway-boulevar/referencia-propu__235-east-airway-boul__techref__h-b9e0bbe77119.pdf` | `b9e0bbe77119`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/31200346-fevereiro-2-2007.pdf` -> `Propulsao-Motores/Referencia-Propulsao/31200346-FEVEREIRO-2-200/referencia-propu__31200346-fevereiro-2__techref__h-3a0fb0162411.pdf` | `3a0fb0162411`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/3TNC78L-RTBA.pdf` -> `Propulsao-Motores/Referencia-Propulsao/3TNC78L-RTBA/referencia-propu__3tnc78l-rtba__techref__h-54e8de048706.pdf` | `54e8de048706`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/5648ffb8-6efb-48bb-aa5d-270a51b18862por-d75c11ad.pdf` -> `Propulsao-Motores/Referencia-Propulsao/5648ffb8-6efb-48bb-aa5d/referencia-propu__5648ffb8-6efb-48bb-a__techref__h-5431892c0da0.pdf` | `5431892c0da0`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/67AUTOMATION.pdf` -> `Propulsao-Motores/Referencia-Propulsao/67AUTOMATION/referencia-propu__67automation__techref__h-22d9863132c1.pdf` | `22d9863132c1`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/6eod.pdf` -> `Propulsao-Motores/Referencia-Propulsao/6EOD/referencia-propu__6eod__techref__h-73ddbba37508.pdf` | `73ddbba37508`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/8m0128973-517-eng.pdf` -> `Propulsao-Motores/Referencia-Propulsao/8M0128973-517-ENG/referencia-propu__8m0128973-517-eng__techref__h-b9d69997d025.pdf` | `b9d69997d025`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/accessories-catalog.pdf` -> `Propulsao-Motores/Referencia-Propulsao/ACCESSORIES-CATALOG/referencia-propu__accessories-catalog__catalog__h-473a8a90425f.pdf` | `473a8a90425f`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/B185-M843NW3G-1.pdf` -> `Propulsao-Motores/Referencia-Propulsao/B185-M843NW3G-1/referencia-propu__b185-m843nw3g-1__techref__h-5e5b9a630f22.pdf` | `5e5b9a630f22`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/bow-thrusters.pdf` -> `Propulsao-Motores/Referencia-Propulsao/BOW-THRUSTERS/referencia-propu__bow-thrusters__techref__h-dec935cbfc2e.pdf` | `dec935cbfc2e`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/capdf18.pdf` -> `Propulsao-Motores/Referencia-Propulsao/CAPDF18/referencia-propu__capdf18__techref__h-7755cbd5ac12.pdf` | `7755cbd5ac12`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/capdf19.pdf` -> `Propulsao-Motores/Referencia-Propulsao/CAPDF19/referencia-propu__capdf19__techref__h-95956834c517.pdf` | `95956834c517`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/capdf22.pdf` -> `Propulsao-Motores/Referencia-Propulsao/CAPDF22/referencia-propu__capdf22__techref__h-ffca6b759159.pdf` | `ffca6b759159`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/catalogo-motori.pdf` -> `Propulsao-Motores/Referencia-Propulsao/CATALOGO-MOTORI/referencia-propu__catalogo-motori__catalog__h-f9e41dfc285b.pdf` | `f9e41dfc285b`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/cnpj-07-884-277-0001-73-inscricaoestadu-f0c649c5.pdf` -> `Propulsao-Motores/Referencia-Propulsao/cnpj-884-277-0001-inscri/referencia-propu__cnpj-884-277-0001-in__techref__h-af597e096e04.pdf` | `af597e096e04`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/co-buu-and-nv-j.pdf` -> `Propulsao-Motores/Referencia-Propulsao/CO-BUU-AND-NV-J/referencia-propu__co-buu-and-nv-j__techref__h-014f05a12ada.pdf` | `014f05a12ada`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/e8c8da.pdf` -> `Propulsao-Motores/Referencia-Propulsao/E8C8DA/referencia-propu__e8c8da__techref__h-aeeb6fe6d7c8.pdf` | `aeeb6fe6d7c8`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/ed-luglio-2022.pdf` -> `Propulsao-Motores/Referencia-Propulsao/ED-LUGLIO-2022/referencia-propu__ed-luglio-2022__techref__h-ee5dfb566a5d.pdf` | `ee5dfb566a5d`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/edizione-2001.pdf` -> `Propulsao-Motores/Referencia-Propulsao/EDIZIONE-2001/referencia-propu__edizione-2001__techref__h-fe3fdb81d9d1.pdf` | `fe3fdb81d9d1`
- `already-present` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/gp-boats-2023.pdf` -> `Complementar-Brasil/Volvo-Penta/Catalogo-GP-Boats/referencia-comercial__volvo-penta__catalogo-pecas-gp-boats.pdf` | `19234b42fdf9`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/GRT7-TH4.pdf` -> `Propulsao-Motores/Referencia-Propulsao/GRT7-TH4/referencia-propu__grt7-th4__techref__h-6a37269dbfc9.pdf` | `6a37269dbfc9`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/h-y-d-r-a-u-l-i-c.pdf` -> `Propulsao-Motores/Referencia-Propulsao/H-Y-D-R-A-U-L-I-C/referencia-propu__h-y-d-r-a-u-l-i-c__techref__h-20ee6db154d4.pdf` | `20ee6db154d4`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/industrial-and-marine-engines-dup-2.pdf` -> `Propulsao-Motores/Referencia-Propulsao/industrial-engines-dup/referencia-propu__industrial-engines-d__techref__h-3238c6d6d088.pdf` | `3238c6d6d088`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/industrial-and-marine-engines-dup-3.pdf` -> `Propulsao-Motores/Referencia-Propulsao/industrial-engines-dup/referencia-propu__industrial-engines-d__techref__h-f1dda7f77ea5.pdf` | `f1dda7f77ea5`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/industrial-and-marine-engines.pdf` -> `Propulsao-Motores/Referencia-Propulsao/industrial-engines/referencia-propu__industrial-engines__techref__h-663d6a160079.pdf` | `663d6a160079`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/instruction-book.pdf` -> `Propulsao-Motores/Referencia-Propulsao/INSTRUCTION-BOOK/referencia-propu__instruction-book__techref__h-4bd33ea30282.pdf` | `4bd33ea30282`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/lewmar-cpx-vertical-windlass-66300104-iss-9.pdf` -> `Propulsao-Motores/Referencia-Propulsao/lewmar-cpx-vertical-wind/referencia-propu__lewmar-cpx-vertical__techref__h-d4a1a80638ed.pdf` | `d4a1a80638ed`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/lewmar-v1-6-windlass-65001201-issue-11.pdf` -> `Propulsao-Motores/Referencia-Propulsao/lewmar-windlass-65001201/referencia-propu__lewmar-windlass-6500__techref__h-d15ecf7a6158.pdf` | `d15ecf7a6158`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/lighthouse-tm-multifunction-display-ope-5507d454.pdf` -> `Propulsao-Motores/Referencia-Propulsao/lighthouse-multifunction/referencia-propu__lighthouse-multifunc__techref__h-100896827809.pdf` | `100896827809`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/MACS.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MACS/referencia-propu__macs__techref__h-df8a266135f1.pdf` | `df8a266135f1`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/man-mc2-x10-en-rev002a.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MAN-MC2-X10-EN-REV002A/referencia-propu__man-mc2-x10-en-rev00__techref__h-96fbc304fedd.pdf` | `96fbc304fedd`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/manual-grta-4-multilinguas.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MANUAL-GRTA-4-MULTILINGU/referencia-propu__manual-grta-4-multil__techref__h-b686563edd87.pdf` | `b686563edd87`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/Manual-GRTA-4.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MANUAL-GRTA-4/referencia-propu__manual-grta-4__techref__h-c4cb4e4fe262.pdf` | `c4cb4e4fe262`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/Manual-telecomandos.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MANUAL-TELECOMANDOS/referencia-propu__manual-telecomandos__techref__h-87450d33d671.pdf` | `87450d33d671`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/MANUAL-ZEN150-230V-TRASD-ENG.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MANUAL-ZEN150-230V-TRASD/referencia-propu__manual-zen150-230v-t__techref__h-eefe957b4adb.pdf` | `eefe957b4adb`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/MANUAL-ZEN150-24V-TRASD-ENG.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MANUAL-ZEN150-24V-TRASD/referencia-propu__manual-zen150-24v-tr__techref__h-fbdbab1dadba.pdf` | `fbdbab1dadba`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/MANUAL-ZEN30-12-24V.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MANUAL-ZEN30-12-24V/referencia-propu__manual-zen30-12-24v__techref__h-fbc840032aed.pdf` | `fbc840032aed`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/manuel-d-atelier-d.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MANUEL-D-ATELIER-D/referencia-propu__manuel-d-atelier-d__techref__h-9db9737de95f.pdf` | `9db9737de95f`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/marine-equipment-guide.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MARINE-EQUIPMENT-GUIDE/referencia-propu__marine-equipment-gui__techref__h-25922a5c437a.pdf` | `25922a5c437a`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/marine-generator-sets-dup-6.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MARINE-GENERATOR-SETS-DU/referencia-propu__marine-generator-set__techref__h-8ac52873aba0.pdf` | `8ac52873aba0`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/marine-generator-sets.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MARINE-GENERATOR-SETS/referencia-propu__marine-generator-set__techref__h-a51f69d703e8.pdf` | `a51f69d703e8`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/MN700.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MN700/referencia-propu__mn700__techref__h-9a354150909a.pdf` | `9a354150909a`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/MN900.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MN900/referencia-propu__mn900__techref__h-18fe39053408.pdf` | `18fe39053408`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/models-1204m-05m-09m-21m-dup-2.pdf` -> `Propulsao-Motores/Referencia-Propulsao/1204m-05m-09m-21m-dup/referencia-propu__1204m-05m-09m-21m-du__techref__h-2877cec21a17.pdf` | `2877cec21a17`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/models-1204m-05m-09m-21m.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MODELS-1204M-05M-09M-21M/referencia-propu__models-1204m-05m-09m__techref__h-7432e6e0b827.pdf` | `7432e6e0b827`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/motores-industriais-e-maritimos.pdf` -> `Propulsao-Motores/Referencia-Propulsao/motores-industriais-mari/referencia-propu__motores-industriais__techref__h-08672e089fef.pdf` | `08672e089fef`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/OM843NW3.pdf` -> `Propulsao-Motores/Referencia-Propulsao/OM843NW3/referencia-propu__om843nw3__techref__h-7571cd41af6f.pdf` | `7571cd41af6f`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/operator-s-manual-p.pdf` -> `Propulsao-Motores/Referencia-Propulsao/OPERATOR-S-MANUAL-P/referencia-propu__operator-s-manual-p__techref__h-50ec814d24c5.pdf` | `50ec814d24c5`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/operator-s-manual.pdf` -> `Propulsao-Motores/Referencia-Propulsao/OPERATOR-S-MANUAL/referencia-propu__operator-s-manual__techref__h-a9d2a4d1dd60.pdf` | `a9d2a4d1dd60`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/P843-3.pdf` -> `Propulsao-Motores/Referencia-Propulsao/P843/referencia-propu__p843__techref__h-e6a6d675fd6c.pdf` | `e6a6d675fd6c`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/propulsao-motores-e-turbo-547726ed.pdf` -> `Propulsao-Motores/Referencia-Propulsao/propulsao-motores-turbo/referencia-propu__propulsao-motores-tu__techref__h-547726ed710b.pdf` | `547726ed710b`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/service-manual.pdf` -> `Propulsao-Motores/Referencia-Propulsao/SERVICE-MANUAL/referencia-propu__service-manual__service__h-f47deffcc87c.pdf` | `f47deffcc87c`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/service-parts-dup-2.pdf` -> `Propulsao-Motores/Referencia-Propulsao/SERVICE-PARTS-DUP-2/referencia-propu__service-parts-dup-2__techref__h-4d243514a427.pdf` | `4d243514a427`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/service-parts.pdf` -> `Propulsao-Motores/Referencia-Propulsao/SERVICE-PARTS/referencia-propu__service-parts__techref__h-07c0ac116ec6.pdf` | `07c0ac116ec6`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/servicemanualtneseries1ocr.pdf` -> `Propulsao-Motores/Referencia-Propulsao/SERVICEMANUALTNESERIES1O/referencia-propu__servicemanualtneseri__techref__h-04e64f519519.pdf` | `04e64f519519`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/smart-compact-design-easy-installation.pdf` -> `Propulsao-Motores/Referencia-Propulsao/smart-compact-design-eas/referencia-propu__smart-compact-design__techref__h-980d0e6696c5.pdf` | `980d0e6696c5`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/superior-technology.pdf` -> `Propulsao-Motores/Referencia-Propulsao/SUPERIOR-TECHNOLOGY/referencia-propu__superior-technology__techref__h-66bfdab15f7e.pdf` | `66bfdab15f7e`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/thruster-systems.pdf` -> `Propulsao-Motores/Referencia-Propulsao/THRUSTER-SYSTEMS/referencia-propu__thruster-systems__techref__h-75fc0836cbcb.pdf` | `75fc0836cbcb`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/tp6252.pdf` -> `Propulsao-Motores/Referencia-Propulsao/TP6252/referencia-propu__tp6252__techref__h-c0003ffef8fe.pdf` | `c0003ffef8fe`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/tp6255.pdf` -> `Propulsao-Motores/Referencia-Propulsao/TP6255/referencia-propu__tp6255__techref__h-516bbd3d42fd.pdf` | `516bbd3d42fd`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/tp6772.pdf` -> `Propulsao-Motores/Referencia-Propulsao/TP6772/referencia-propu__tp6772__techref__h-dc279056e42e.pdf` | `dc279056e42e`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/tp6775.pdf` -> `Propulsao-Motores/Referencia-Propulsao/TP6775/referencia-propu__tp6775__techref__h-8470d3e3b1ea.pdf` | `8470d3e3b1ea`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/ultraflex-control-systems-s-r-l.pdf` -> `Propulsao-Motores/Ultraflex/Geral/ultraflex__geral__techref__h-1f9dd0022270.pdf` | `1f9dd0022270`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/valves-and-electronics.pdf` -> `Propulsao-Motores/Referencia-Propulsao/VALVES-AND-ELECTRONICS/referencia-propu__valves-and-electroni__techref__h-07ac6d782756.pdf` | `07ac6d782756`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/vw5cylinderoperatingmanual.pdf` -> `Propulsao-Motores/Referencia-Propulsao/VW5CYLINDEROPERATINGMANU/referencia-propu__vw5cylinderoperating__techref__h-6649fa0aa113.pdf` | `6649fa0aa113`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/workshop-manual-vw-marine-boat-engine.pdf` -> `Propulsao-Motores/Referencia-Propulsao/workshop-boat-engine/referencia-propu__workshop-boat-engine__techref__h-b9276254cab6.pdf` | `b9276254cab6`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/ydes04.pdf` -> `Propulsao-Motores/Referencia-Propulsao/YDES04/referencia-propu__ydes04__techref__h-8666504a0fbb.pdf` | `8666504a0fbb`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/ZEN150-12-24V-TOUCH.pdf` -> `Propulsao-Motores/Referencia-Propulsao/ZEN150-12-24V-TOUCH/referencia-propu__zen150-12-24v-touch__techref__h-b127103bddb1.pdf` | `b127103bddb1`
- `copied` | `10_Materiais_Internos_e_Cursos/dni-0409-dni-0413.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/DNI-0409-DNI-0413/referencia-mater__dni-0409-dni-0413__techref__h-953968223fb1.pdf` | `953968223fb1`
- `copied` | `10_Materiais_Internos_e_Cursos/fundamentos-da-eletrica-nautica.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/fundamentos-eletrica-nau/referencia-mater__fundamentos-eletrica__techref__h-4f4e79bf1f2b.pdf` | `4f4e79bf1f2b`
- `copied` | `10_Materiais_Internos_e_Cursos/i-publico-alvo-eletricista-auxiliar-de-eletrici-65f4cb48.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/publico-alvo-eletricista/referencia-mater__publico-alvo-eletric__techref__h-3ffa0e29f616.pdf` | `3ffa0e29f616`
- `copied` | `10_Materiais_Internos_e_Cursos/i-publico-alvo-gerentes-administrativo-de-marin-1cdd16fe.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/publico-alvo-gerentes-ad/referencia-mater__publico-alvo-gerente__techref__h-819e350fd832.pdf` | `819e350fd832`
- `copied` | `10_Materiais_Internos_e_Cursos/i-publico-alvo-mecanicos-as-e-auxiliares-de-mec-c8479237.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/publico-alvo-mecanicos-a/referencia-mater__publico-alvo-mecanic__techref__h-7893fbfe91cc.pdf` | `7893fbfe91cc`
- `copied` | `10_Materiais_Internos_e_Cursos/Manual0305.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/MANUAL0305/referencia-mater__manual0305__techref__h-992f869e9002.pdf` | `992f869e9002`
- `copied` | `10_Materiais_Internos_e_Cursos/Manual0409-0413.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/MANUAL0409-0413/referencia-mater__manual0409-0413__techref__h-361675976967.pdf` | `361675976967`
- `copied` | `10_Materiais_Internos_e_Cursos/motores-eletricos.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/MOTORES-ELETRICOS/referencia-mater__motores-eletricos__techref__h-f5acdfc1f53a.pdf` | `f5acdfc1f53a`
- `copied` | `10_Materiais_Internos_e_Cursos/Referencias_Tecnicas/2015-msc-pemm-gustavo-henrique-senna-de-64db7732.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/Referencias-Tecnicas/referencia-mater__referencias-tecnicas__techref__h-21f8717aa694.pdf` | `21f8717aa694`
- `copied` | `10_Materiais_Internos_e_Cursos/Referencias_Tecnicas/a-confraria-europeia-da-vela.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/A-CONFRARIA-EUROPEIA-DA/referencia-mater__a-confraria-europeia__techref__h-7a2b74af48ff.pdf` | `7a2b74af48ff`
- `copied` | `10_Materiais_Internos_e_Cursos/Referencias_Tecnicas/Non-Metallic-Materials-Brochure.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/Referencias-Tecnicas/referencia-mater__referencias-tecnicas__techref__h-fb258876ba1d.pdf` | `fb258876ba1d`

## Proxima fila sugerida

- converter HTML tecnico exportado para PDF arquivado e/ou nota Markdown curada quando o conteudo for fonte primaria util
- transformar imagens avulsas em anexos documentados ou descartar duplicatas visuais sem valor tecnico
- rodar novamente a pipeline de OCR para os PDFs promovidos com baixa extracao textual
