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

- `copied` | `00_Documentacao_de_Campo_e_Clientes/a-c-raphael.pdf` -> `Campo-Clientes/Referencia-Campo/A-C-RAPHAEL/a-c-raphael.pdf` | `aa444c6c1c41`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/analise-para-instalacao-dos-transducers-ga-a573969e.pdf` -> `Campo-Clientes/Referencia-Campo/analise-para-instalacao/analise-para-instalacao-dos-transducers-ga-a573969e.pdf` | `7e33a63e0684`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/diagrama-esquematico-de-ligacao-dos-equipa-f4d827e7.pdf` -> `Campo-Clientes/Referencia-Campo/diagrama-esquematico-lig/diagrama-esquematico-de-ligacao-dos-equipa-f4d827e7.pdf` | `c36426e5182f`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/diagrama-victron-invert-raphael-c-rj.pdf` -> `Campo-Clientes/Victron/Geral/diagrama-victron-invert-raphael-c-rj.pdf` | `3fe450185b8e`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/diagramas-som-fusion-jl-audio-raphael-c-rj.pdf` -> `Campo-Clientes/Referencia-Campo/diagramas-som-fusion-aud/diagramas-som-fusion-jl-audio-raphael-c-rj.pdf` | `64d239534599`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/esboco-instalacao-camera-farol-radar-raphael-c-rj.pdf` -> `Campo-Clientes/Referencia-Campo/esboco-instalacao-camera/esboco-instalacao-camera-farol-radar-raphael-c-rj.pdf` | `5e99575ddd2c`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/estudo-e-diagramas-do-sistema-hidraulico-d-932ba9b7.pdf` -> `Campo-Clientes/Referencia-Campo/estudo-diagramas-sistema/estudo-e-diagramas-do-sistema-hidraulico-d-932ba9b7.pdf` | `fa7ae235245d`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/estudo-painel-garnet-300ht-raphael-c-rj.pdf` -> `Campo-Clientes/Referencia-Campo/estudo-painel-garnet-300/estudo-painel-garnet-300ht-raphael-c-rj.pdf` | `d26d1828a491`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/Imagens_e_Recortes_Tecnicos/00206bf595ae240412115759.pdf` -> `Campo-Clientes/Referencia-Campo/00206BF595AE240412115759/00206bf595ae240412115759.pdf` | `4f030a8a2591`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/Imagens_e_Recortes_Tecnicos/c-users-nalmeida-appdata-local-temp-26-46885c42.pdf` -> `Campo-Clientes/Referencia-Campo/Imagens-e-Recortes-Tecni/c-users-nalmeida-appdata-local-temp-26-46885c42.pdf` | `aa138d8c8774`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/Imagens_e_Recortes_Tecnicos/DOC-20180206-WA0045.pdf` -> `Campo-Clientes/Referencia-Campo/DOC-20180206-WA0045/doc-20180206-wa0045.pdf` | `8d05a269d0b0`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/Imagens_e_Recortes_Tecnicos/foto-de-p-303-241gina-inteira.pdf` -> `Campo-Clientes/Referencia-Campo/Imagens-e-Recortes-Tecni/foto-de-p-303-241gina-inteira.pdf` | `7be021d8f385`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/Imagens_e_Recortes_Tecnicos/IMG-20230614-WA0001.pdf` -> `Campo-Clientes/Referencia-Campo/IMG-20230614-WA0001/img-20230614-wa0001.pdf` | `db8f43f124b2`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/Imagens_e_Recortes_Tecnicos/P753.pdf` -> `Campo-Clientes/Referencia-Campo/Imagens-e-Recortes-Tecni/p753.pdf` | `6af763337b2b`
- `copied` | `00_Documentacao_de_Campo_e_Clientes/Imagens_e_Recortes_Tecnicos/q-q-q-q-q-q-q-q-q-q-q-q-q-q-q-q-q-q-q-q-49ec4234.pdf` -> `Campo-Clientes/Referencia-Campo/Imagens-e-Recortes-Tecni/q-q-q-q-q-q-q-q-q-q-q-q-q-q-q-q-q-q-q-q-49ec4234.pdf` | `01f752e602ba`
- `copied` | `01_Geradores/0981-0181-Issue-7-English.pdf` -> `Geradores/Referencia-Geradores/0981-0181-ISSUE-7-ENGLIS/0981-0181-issue-7-english.pdf` | `438ff8dbb60a`
- `copied` | `01_Geradores/10850OM.pdf` -> `Geradores/Referencia-Geradores/10850OM/10850om.pdf` | `08e9f6fecc42`
- `copied` | `01_Geradores/17-5mdkae.pdf` -> `Geradores/Cummins-Onan/17-5MDKAE/17-5mdkae.pdf` | `448b5df582c7`
- `copied` | `01_Geradores/32002OM.pdf` -> `Geradores/Referencia-Geradores/32002OM/32002om.pdf` | `0c4ab74fef53`
- `copied` | `01_Geradores/40457-rev2-7-6btd-operator-manual.pdf` -> `Geradores/Referencia-Geradores/40457-rev2-6btd/40457-rev2-7-6btd-operator-manual.pdf` | `9f154dfb466d`
- `already-present` | `01_Geradores/5EFKOZD-service-manual.pdf` -> `Geradores/Rehlko-Kohler/5EFKOD/rehlko-kohler-5efkod-6ekod-9-11ekozd-7-9efkozd-service-manual-tp-6774-2014-02a.pdf` | `25c5a7676eea`
- `copied` | `01_Geradores/70384OM.pdf` -> `Geradores/Referencia-Geradores/70384OM/70384om.pdf` | `20746e490d48`
- `copied` | `01_Geradores/7953-hdkah-spec-a-n-operator-manual-2015.pdf` -> `Geradores/Cummins-Onan/Geral/7953-hdkah-spec-a-n-operator-manual-2015.pdf` | `2f3b12f95110`
- `copied` | `01_Geradores/8731-marine-electrical-products.pdf` -> `Geradores/Referencia-Geradores/8731-electrical-products/8731-marine-electrical-products.pdf` | `f96263ee33f8`
- `copied` | `01_Geradores/8732-marine-electrical-products.pdf` -> `Geradores/Referencia-Geradores/8732-electrical-products/8732-marine-electrical-products.pdf` | `b58c6e93ee1b`
- `copied` | `01_Geradores/900-0541b-energy-command-operation-manual.pdf` -> `Geradores/Cummins-Onan/Geral/900-0541b-energy-command-operation-manual.pdf` | `ce7111298b99`
- `copied` | `01_Geradores/934-0602-onan-mdl3-mdl4-mdl6-marine-genset-installation-manual-01-1991.pdf` -> `Geradores/Cummins-Onan/Geral/934-0602-onan-mdl3-mdl4-mdl6-marine-genset-installation-manual-01-1991.pdf` | `3e546f83ffea`
- `already-present` | `01_Geradores/981-0181-onan-mdkbx-marine-genset-operator-manual-03-2008.pdf` -> `Geradores/Cummins-Onan/Legacy-MDKBK-MDKBN/cummins-onan-mdkbk-mdkbl-mdkbm-mdkbn-operator-manual-981-0181-2008-03.pdf` | `5f97f11c68dc`
- `copied` | `01_Geradores/avr-a-opt-01-regulador-de-tensao-analogico.pdf` -> `Geradores/Referencia-Geradores/avr-opt-regulador-tensao/avr-a-opt-01-regulador-de-tensao-analogico.pdf` | `7d410be8f0a8`
- `copied` | `01_Geradores/california-proposition-65.pdf` -> `Geradores/Referencia-Geradores/CALIFORNIA-PROPOSITION-6/california-proposition-65.pdf` | `df8e3cab395e`
- `already-present` | `01_Geradores/cummins-onan-mdkad-mdkae-mdkaf-operator-manual-981-0140-1996-02.pdf` -> `Geradores/Cummins-Onan/MDKAD-MDKAE-MDKAF/cummins-onan-mdkad-mdkae-mdkaf-operator-manual-981-0140-1996-02.pdf` | `1a79566b0e5a`
- `already-present` | `01_Geradores/cummins-onan-mdkad-mdkae-mdkaf-service-manual-981-0520b.pdf` -> `Geradores/Cummins-Onan/MDKAD-MDKAE-MDKAF/cummins-onan-mdkad-mdkae-mdkaf-service-manual-981-0520b.pdf` | `437245942da1`
- `already-present` | `01_Geradores/cummins-onan-mdkad-mdkae-parts-manual-981-0264-1999-01.pdf` -> `Geradores/Cummins-Onan/MDKAD-MDKAE-MDKAF/cummins-onan-mdkad-mdkae-parts-manual-981-0264-1999-01.pdf` | `9ca5a7ef8170`
- `already-present` | `01_Geradores/cummins-onan-mdkbh-service-manual-981-0542.pdf` -> `Geradores/Cummins-Onan/MDKBH/cummins-onan-mdkbh-service-manual-981-0542.pdf` | `a791141a566b`
- `already-present` | `01_Geradores/cummins-onan-mdkbp-mdkbr-mdkbs-parts-manual-0981-0281.pdf` -> `Geradores/Cummins-Onan/Legacy-MDKBP-MDKBS/cummins-onan-mdkbp-mdkbr-mdkbs-parts-manual-0981-0281.pdf` | `b0df461c94d3`
- `already-present` | `01_Geradores/cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-operator-manual-a052j727.pdf` -> `Geradores/Cummins-Onan/MDKDK/cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-operator-manual-a052j727.pdf` | `54a3d0cea3e2`
- `already-present` | `01_Geradores/cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-service-manual-a052j731.pdf` -> `Geradores/Cummins-Onan/MDKDK/cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-service-manual-a052j731.pdf` | `21b643a8b1b7`
- `copied` | `01_Geradores/Fischer-Panda-4200-ECO-Operation-manual.pdf` -> `Geradores/Fischer-Panda/Geral/fischer-panda-4200-eco-operation-manual.pdf` | `41fb6a309ac3`
- `copied` | `01_Geradores/fischer-panda-4200.pdf` -> `Geradores/Fischer-Panda/FISCHER-PANDA-4200/fischer-panda-4200.pdf` | `e5385ebc8e0d`
- `copied` | `01_Geradores/Fischer-Panda-7Mini.pdf` -> `Geradores/Fischer-Panda/FISCHER-PANDA-7MINI/fischer-panda-7mini.pdf` | `a6d160ed41d2`
- `copied` | `01_Geradores/folheto-gerador-panda-7-mini.pdf` -> `Geradores/Fischer-Panda/FOLHETO-GERADOR-PANDA-7/folheto-gerador-panda-7-mini.pdf` | `e0643ebc72b8`
- `copied` | `01_Geradores/folheto-gerador-panda-9-dp-digital-panel-ingles.pdf` -> `Geradores/Fischer-Panda/Geral/folheto-gerador-panda-9-dp-digital-panel-ingles.pdf` | `42b1f74e5c85`
- `copied` | `01_Geradores/Generator-Northern-Lights-Manual.pdf` -> `Geradores/Northern-Lights/Geral/generator-northern-lights-manual.pdf` | `ae0d5335b800`
- `copied` | `01_Geradores/hdkah-hdkaj-hdkak-hdkau-hdkav-service-manual.pdf` -> `Geradores/Cummins-Onan/Geral/hdkah-hdkaj-hdkak-hdkau-hdkav-service-manual.pdf` | `a3ae73c9a3ef`
- `copied` | `01_Geradores/kohler-manual-instalacao-gmg.pdf` -> `Geradores/Rehlko-Kohler/KOHLER-MANUAL-INSTALACAO/kohler-manual-instalacao-gmg.pdf` | `6c3aa0ac7a9f`
- `copied` | `01_Geradores/machine-translated-by-google.pdf` -> `Geradores/Referencia-Geradores/MACHINE-TRANSLATED-BY-GO/machine-translated-by-google.pdf` | `77cfe2f0c71c`
- `copied` | `01_Geradores/manual-de-produto-126-108.pdf` -> `Geradores/Referencia-Geradores/MANUAL-DE-PRODUTO-126-10/manual-de-produto-126-108.pdf` | `157ce2010aaa`
- `copied` | `01_Geradores/manual-egc-automatic-rev02.pdf` -> `Geradores/Referencia-Geradores/MANUAL-EGC-AUTOMATIC-REV/manual-egc-automatic-rev02.pdf` | `f86036e87bfc`
- `copied` | `01_Geradores/manual-egc.pdf` -> `Geradores/Referencia-Geradores/MANUAL-EGC/manual-egc.pdf` | `c891f41ad0f9`
- `copied` | `01_Geradores/Manual-Gerador-20-kva-com-Tramontini.pdf` -> `Geradores/Referencia-Geradores/Gerador-kva-com-Tramonti/manual-gerador-20-kva-com-tramontini.pdf` | `1f2426c552d9`
- `copied` | `01_Geradores/manual-gerador-parts-e-pecas.pdf` -> `Geradores/Referencia-Geradores/MANUAL-GERADOR-PARTS-E-P/manual-gerador-parts-e-pecas.pdf` | `ad6f5e06da71`
- `already-present` | `01_Geradores/MDKBK-BL-BM-BN-BP-BR-BS-BT-BU-BV-Service-Manual.pdf` -> `Geradores/Cummins-Onan/Legacy-MDKBK-MDKBN/cummins-onan-mdkbk-mdkbl-mdkbm-mdkbn-service-manual-981-0543.pdf` | `1a505c22df00`
- `copied` | `01_Geradores/mdkbk.pdf` -> `Geradores/Cummins-Onan/Geral/mdkbk.pdf` | `5015b93e504c`
- `already-present` | `01_Geradores/mdkdp-dr-ds-dt-du-dv-service-manual.pdf` -> `Geradores/Cummins-Onan/MDKDP-MDKDR-MDKDV/cummins-onan-mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv-service-manual-a046j602.pdf` | `3e936560c78c`
- `copied` | `01_Geradores/model-9eozd-60-hz-7efozd-50-hz.pdf` -> `Geradores/Referencia-Geradores/9eozd-7efozd/model-9eozd-60-hz-7efozd-50-hz.pdf` | `ed09239a8d50`
- `copied` | `01_Geradores/modulo1-geradores-ca-1-a-21-2007.pdf` -> `Geradores/Referencia-Geradores/modulo1-geradores-2007/modulo1-geradores-ca-1-a-21-2007.pdf` | `d2a13fccc230`
- `copied` | `01_Geradores/northen-lights-generator-om844w3.pdf` -> `Geradores/Northern-Lights/Geral/northen-lights-generator-om844w3.pdf` | `e7a61856413f`
- `copied` | `01_Geradores/onan-mcck-marine-genset-manual.pdf` -> `Geradores/Cummins-Onan/Geral/onan-mcck-marine-genset-manual.pdf` | `d61fcf04667d`
- `copied` | `01_Geradores/onan-troubleshooting-guide-codes.pdf` -> `Geradores/Cummins-Onan/Geral/onan-troubleshooting-guide-codes.pdf` | `b69a70cf5051`
- `copied` | `01_Geradores/operator-manual-marine-diesel-generators.pdf` -> `Geradores/Referencia-Geradores/diesel-generators/operator-manual-marine-diesel-generators.pdf` | `6aa974905459`
- `copied` | `01_Geradores/panda-15mini-pms-digital-vcs183-eng-r03.pdf` -> `Geradores/Fischer-Panda/Geral/panda-15mini-pms-digital-vcs183-eng-r03.pdf` | `11d07a48e60e`
- `copied` | `01_Geradores/panda-4200-4500eco-r01.pdf` -> `Geradores/Fischer-Panda/PANDA-4200-4500ECO-R01/panda-4200-4500eco-r01.pdf` | `6cdfb70a12f6`
- `copied` | `01_Geradores/Panda-4K-5K-7K-manual.pdf` -> `Geradores/Fischer-Panda/PANDA-4K-5K-7K-MANUAL/panda-4k-5k-7k-manual.pdf` | `01fb383084e6`
- `copied` | `01_Geradores/panda-4k-pms-eng-r01.pdf` -> `Geradores/Fischer-Panda/PANDA-4K-PMS-ENG-R01/panda-4k-pms-eng-r01.pdf` | `8f734f18a72c`
- `copied` | `01_Geradores/Panda-7K-PMS.pdf` -> `Geradores/Fischer-Panda/PANDA-7K-PMS/panda-7k-pms.pdf` | `c8025edb30d6`
- `copied` | `01_Geradores/reguladores-de-tensao-digitais.pdf` -> `Geradores/Referencia-Geradores/reguladores-tensao-digit/reguladores-de-tensao-digitais.pdf` | `50e847969261`
- `copied` | `01_Geradores/service-manual.pdf` -> `Geradores/Referencia-Geradores/SERVICE-MANUAL/service-manual.pdf` | `6ee62475cc8c`
- `copied` | `01_Geradores/universidade-federal-do-amapa-departamento-de-ciencias-exatas-e-t-35c52013.pdf` -> `Geradores/Referencia-Geradores/universidade-federal-ama/universidade-federal-do-amapa-departamento-de-ciencias-exatas-e-t-35c52013.pdf` | `5ca233e3515f`
- `copied` | `02_Climatizacao/chilled-water-air-conditioning.pdf` -> `Climatizacao/Referencia-Climatizacao/chilled-water-conditioni/chilled-water-air-conditioning.pdf` | `192a095558b2`
- `already-present` | `02_Climatizacao/cruisair-marine-a-c-systems-troubleshooting-guide.pdf` -> `Climatizacao/Dometic/Self-Contained/dometic-cruisair-self-contained-air-conditioner-troubleshooting-guide.pdf` | `0b38d83d6d12`
- `copied` | `02_Climatizacao/cruisair-tempered-water-system.pdf` -> `Climatizacao/Dometic/Geral/cruisair-tempered-water-system.pdf` | `ce30568e795f`
- `copied` | `02_Climatizacao/dometic-chilled-water-operating-manual.pdf` -> `Climatizacao/Dometic/Geral/dometic-chilled-water-operating-manual.pdf` | `c0ad0cafc451`
- `already-present` | `02_Climatizacao/dometic-cruisair-marine-air-conditioners-price-list-2015.pdf` -> `Climatizacao/Dometic/Self-Contained/dometic-cruisair-marine-air-conditioners-price-list-2015.pdf` | `cc259fa0437f`
- `copied` | `02_Climatizacao/dometic-mtcg-9108893793-75371.pdf` -> `Climatizacao/Dometic/Geral/dometic-mtcg-9108893793-75371.pdf` | `2fc37685edf5`
- `already-present` | `02_Climatizacao/dometic-marine-air-conditioners-price-list-2024.pdf` -> `Climatizacao/Dometic/Self-Contained/dometic-marine-air-conditioners-price-list-2024.pdf` | `6a5287a55b9b`
- `already-present` | `02_Climatizacao/dx-remote-and-self-contained-a-c-v-installation-operation-manual.pdf` -> `Climatizacao/Dometic/Self-Contained/dometic-cruisair-self-contained-air-conditioner-installation-manual-dx-remote-804-746.pdf` | `0ca46dcdba29`
- `copied` | `02_Climatizacao/manual-ar-condicionado.pdf` -> `Climatizacao/Referencia-Climatizacao/MANUAL-AR-CONDICIONADO/manual-ar-condicionado.pdf` | `08991e8e30fa`
- `copied` | `03_Baterias_e_DC/19-informativo-tecnico-no.pdf` -> `Energia-DC/Referencia-Energia-DC/19-INFORMATIVO-TECNICO-N/19-informativo-tecnico-no.pdf` | `7abdcbd8eb77`
- `copied` | `03_Baterias_e_DC/722-NE.pdf` -> `Energia-DC/Referencia-Energia-DC/722-NE/722-ne.pdf` | `707b3fb0f560`
- `copied` | `03_Baterias_e_DC/AB12210.pdf` -> `Energia-DC/Referencia-Energia-DC/AB12210/ab12210.pdf` | `24b7a5c72622`
- `copied` | `03_Baterias_e_DC/abso-charger.pdf` -> `Energia-DC/Referencia-Energia-DC/ABSO-CHARGER/abso-charger.pdf` | `1593c97dadc4`
- `copied` | `03_Baterias_e_DC/atlas-eolico-rs.pdf` -> `Energia-DC/Referencia-Energia-DC/ATLAS-EOLICO-RS/atlas-eolico-rs.pdf` | `32aaad151d9e`
- `copied` | `03_Baterias_e_DC/bch-opt-41-bivolt.pdf` -> `Energia-DC/Referencia-Energia-DC/BCH-OPT-41-BIVOLT/bch-opt-41-bivolt.pdf` | `916f50c87c38`
- `copied` | `03_Baterias_e_DC/catalogo-inversor-2023-digital.pdf` -> `Energia-DC/Referencia-Energia-DC/inversor-2023-digital/catalogo-inversor-2023-digital.pdf` | `dc95ed231199`
- `copied` | `03_Baterias_e_DC/catalogo-usina-impresso-2022.pdf` -> `Energia-DC/Usina/CATALOGO-USINA-IMPRESSO/catalogo-usina-impresso-2022.pdf` | `e962a9637eb9`
- `copied` | `03_Baterias_e_DC/conceptual-diagram-dc-overview.pdf` -> `Energia-DC/Referencia-Energia-DC/conceptual-overview/conceptual-diagram-dc-overview.pdf` | `1308555afbe0`
- `copied` | `03_Baterias_e_DC/industrial-and-marine-engines.pdf` -> `Energia-DC/Referencia-Energia-DC/industrial-engines/industrial-and-marine-engines.pdf` | `12fb7a4e0d38`
- `copied` | `03_Baterias_e_DC/irfz48npbf.pdf` -> `Energia-DC/Referencia-Energia-DC/IRFZ48NPBF/irfz48npbf.pdf` | `737bb8cabd25`
- `copied` | `03_Baterias_e_DC/Manual-BPP2-PT.pdf` -> `Energia-DC/Referencia-Energia-DC/MANUAL-BPP2-PT/manual-bpp2-pt.pdf` | `732424d4c60c`
- `copied` | `03_Baterias_e_DC/Manual-Digital-Multi-Control-GX-Panel-EN-NL-FR-DE-ES.pdf` -> `Energia-DC/Referencia-Energia-DC/Digital-Multi-Panel/manual-digital-multi-control-gx-panel-en-nl-fr-de-es.pdf` | `a25f30d8271c`
- `copied` | `03_Baterias_e_DC/manual-do-produto.pdf` -> `Energia-DC/Referencia-Energia-DC/MANUAL-DO-PRODUTO/manual-do-produto.pdf` | `d5d6dc1cdb8b`
- `copied` | `03_Baterias_e_DC/more-user-manuals-on.pdf` -> `Energia-DC/Referencia-Energia-DC/MORE-USER-MANUALS-ON/more-user-manuals-on.pdf` | `62ad6d381a18`
- `copied` | `03_Baterias_e_DC/motive-power-dup-2.pdf` -> `Energia-DC/Referencia-Energia-DC/MOTIVE-POWER-DUP-2/motive-power-dup-2.pdf` | `94413f9df153`
- `copied` | `03_Baterias_e_DC/motive-power.pdf` -> `Energia-DC/Referencia-Energia-DC/MOTIVE-POWER/motive-power.pdf` | `7331909288a7`
- `copied` | `03_Baterias_e_DC/nautical-equipment-evolution.pdf` -> `Energia-DC/Referencia-Energia-DC/NAUTICAL-EQUIPMENT-EVOLU/nautical-equipment-evolution.pdf` | `87ed2f565544`
- `copied` | `03_Baterias_e_DC/owner-s-manual.pdf` -> `Energia-DC/Referencia-Energia-DC/OWNER-S-MANUAL/owner-s-manual.pdf` | `009988c7277b`
- `copied` | `03_Baterias_e_DC/pcwmvar.pdf` -> `Energia-DC/Referencia-Energia-DC/pcwmvar/pcwmvar.pdf` | `c3d93df4459e`
- `copied` | `03_Baterias_e_DC/rev-2-04-17.pdf` -> `Energia-DC/Referencia-Energia-DC/REV-2-04-17/rev-2-04-17.pdf` | `1604851083fa`
- `already-present` | `03_Baterias_e_DC/the-12-volt-doctors-practical-handbook.pdf` -> `Complementar-Brasil/Referencias-Gerais/12V/12-volt-doctors-handbook-practical-12v-systems.pdf` | `59ed52a6fe64`
- `copied` | `03_Baterias_e_DC/user-manual-for-interbus-s.pdf` -> `Energia-DC/Referencia-Energia-DC/USER-MANUAL-FOR-INTERBUS/user-manual-for-interbus-s.pdf` | `5b62a14729bf`
- `copied` | `03_Baterias_e_DC/users-manual.pdf` -> `Energia-DC/Referencia-Energia-DC/USERS-MANUAL/users-manual.pdf` | `f533f12bb49d`
- `copied` | `03_Baterias_e_DC/www-sparkpower-com-br.pdf` -> `Energia-DC/Referencia-Energia-DC/WWW-SPARKPOWER-COM-BR/www-sparkpower-com-br.pdf` | `fbe645bcabe8`
- `copied` | `04_Shore_Power_e_AC/baixa-tensao.pdf` -> `Shore-Power-AC/Referencia-Shore-Power/BAIXA-TENSAO/baixa-tensao.pdf` | `76ea282b86f8`
- `copied` | `04_Shore_Power_e_AC/catalogo-chave-rotativa-lw26-rev-set-18.pdf` -> `Shore-Power-AC/Referencia-Shore-Power/chave-rotativa-lw26-rev/catalogo-chave-rotativa-lw26-rev-set-18.pdf` | `d27ee4babe8c`
- `copied` | `04_Shore_Power_e_AC/co-004-15-folder-linha-automotiva-21x29-7cm-ok.pdf` -> `Shore-Power-AC/Referencia-Shore-Power/004-folder-linha-automot/co-004-15-folder-linha-automotiva-21x29-7cm-ok.pdf` | `f1c574a9604f`
- `copied` | `04_Shore_Power_e_AC/licenca-de-uso-exclusivo-para-target-engenharia-e-consulto-572b6510.pdf` -> `Shore-Power-AC/Referencia-Shore-Power/licenca-uso-exclusivo-pa/licenca-de-uso-exclusivo-para-target-engenharia-e-consulto-572b6510.pdf` | `610e30c82eec`
- `copied` | `04_Shore_Power_e_AC/LUMISHORE-2024-SYBROCHURE.pdf` -> `Shore-Power-AC/Lumishore/LUMISHORE-2024-SYBROCHUR/lumishore-2024-sybrochure.pdf` | `48d3ef482a88`
- `copied` | `04_Shore_Power_e_AC/stop-0-start.pdf` -> `Shore-Power-AC/Referencia-Shore-Power/STOP-0-START/stop-0-start.pdf` | `5b5043777b35`
- `copied` | `04_Shore_Power_e_AC/technical-data-sheet.pdf` -> `Shore-Power-AC/Referencia-Shore-Power/TECHNICAL-DATA-SHEET/technical-data-sheet.pdf` | `fbc265150af8`
- `already-present` | `05_Navegacao_e_Eletronicos/0-75-6-5-6.pdf` -> `Navegacao/Standard-Horizon/GX2000-GX2150/standard-horizon-gx2000-gx2150-operation-manual-em044n160-5292013.pdf` | `b10aa04e9fed`
- `already-present` | `05_Navegacao_e_Eletronicos/116-mm-4-9-16-in.pdf` -> `Navegacao/Garmin/GHC-50/garmin-ghc-50-display-cutout-template.pdf` | `a3ef36f782be`
- `already-present` | `05_Navegacao_e_Eletronicos/fi-5002-junction-box-installation-instructions.pdf` -> `Navegacao/Furuno/FI-5002/furuno-fi-5002-installation-manual-rev-a.pdf` | `b2baab940a87`
- `already-present` | `05_Navegacao_e_Eletronicos/furuno-can-bus-network-design-guide.pdf` -> `Navegacao/Furuno/CAN-Bus/furuno-can-bus-network-design-guide-000-167.pdf` | `4d757d2c1a7d`
- `already-present` | `05_Navegacao_e_Eletronicos/gps-17x-hvs-technical-specifications.pdf` -> `Navegacao/Garmin/GPS-17x-HVS/garmin-gps-17x-hvs-technical-specifications.pdf` | `bc429e98748d`
- `already-present` | `05_Navegacao_e_Eletronicos/gpsmap-4000-5000-series-installation-instructions.pdf` -> `Navegacao/Garmin/GPSMAP-4000-5000/garmin-gpsmap-4000-5000-installation-manual-en.pdf` | `f8a3c18f958b`
- `copied` | `05_Navegacao_e_Eletronicos/installation-and-wire-connection-manual.pdf` -> `Navegacao/Referencia-Navegacao/wire-connection/installation-and-wire-connection-manual.pdf` | `1ea33ab0b704`
- `copied` | `05_Navegacao_e_Eletronicos/intellian-i3-i4-i4p-i6-i6p-i6pe-i6w-qui-fa98cb0e.pdf` -> `Navegacao/Intellian/Geral/intellian-i3-i4-i4p-i6-i6p-i6pe-i6w-qui-fa98cb0e.pdf` | `012502f49cf7`
- `copied` | `05_Navegacao_e_Eletronicos/Interbus.pdf` -> `Navegacao/Referencia-Navegacao/Interbus/interbus.pdf` | `03d72ce8f84e`
- `copied` | `05_Navegacao_e_Eletronicos/manual-2019-12-19-08-26-08-rs40-rs40-b-and-hs40.pdf` -> `Navegacao/Referencia-Navegacao/2019-rs40-rs40-hs40/manual-2019-12-19-08-26-08-rs40-rs40-b-and-hs40.pdf` | `82a849d86a53`
- `copied` | `05_Navegacao_e_Eletronicos/network-expansion-port-2-nep-2.pdf` -> `Navegacao/Referencia-Navegacao/network-expansion-port-n/network-expansion-port-2-nep-2.pdf` | `625e93f09380`
- `copied` | `05_Navegacao_e_Eletronicos/NRX300.pdf` -> `Navegacao/Referencia-Navegacao/NRX300/nrx300.pdf` | `beb3139454cf`
- `copied` | `05_Navegacao_e_Eletronicos/nx403a.pdf` -> `Navegacao/Referencia-Navegacao/NX403A/nx403a.pdf` | `ebee10527d4f`
- `copied` | `05_Navegacao_e_Eletronicos/owner-s-guide-and-installation-instructions.pdf` -> `Navegacao/Referencia-Navegacao/owner/owner-s-guide-and-installation-instructions.pdf` | `96a97cf2327d`
- `already-present` | `05_Navegacao_e_Eletronicos/quantumtm-instrucoes-de.pdf` -> `Navegacao/Raymarine/Quantum/raymarine-quantum-radar-manual-portugues.pdf` | `323f97e95983`
- `copied` | `05_Navegacao_e_Eletronicos/quick-start-guide-and-installation-manual-guide-de-4ec49ee6.pdf` -> `Navegacao/Quick/Geral/quick-start-guide-and-installation-manual-guide-de-4ec49ee6.pdf` | `a92e0cb1f37d`
- `already-present` | `05_Navegacao_e_Eletronicos/seatalk-refrence-manual.pdf` -> `Navegacao/Raymarine/SeaTalk/raymarine-seatalk-cabling-and-connections-a06033.pdf` | `4bcd9af75d0d`
- `already-present` | `05_Navegacao_e_Eletronicos/st6002-smartpilot-controller-operating-guide.pdf` -> `Navegacao/Raymarine/SmartPilot-ST6002/raymarine-smartpilot-st6002-operation-manual.pdf` | `af5bab3a75f9`
- `already-present` | `05_Navegacao_e_Eletronicos/supplemental-instructions.pdf` -> `Navegacao/Furuno/FI-5002/furuno-fi-5002-supplemental-instructions-410-479.pdf` | `97663dc66b1a`
- `copied` | `05_Navegacao_e_Eletronicos/technical-manual.pdf` -> `Navegacao/Referencia-Navegacao/TECHNICAL-MANUAL/technical-manual.pdf` | `555b0f8483b8`
- `copied` | `05_Navegacao_e_Eletronicos/voce-conhece-voce-confia.pdf` -> `Navegacao/Referencia-Navegacao/VOCE-CONHECE-VOCE-CONFIA/voce-conhece-voce-confia.pdf` | `75ac1c0ece8d`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/60020-0024.pdf` -> `Bombas-Utilidades/Referencia-Bombas-Utilidades/60020-0024/60020-0024.pdf` | `dbaaa72ddf4f`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/capdf21.pdf` -> `Bombas-Utilidades/Referencia-Bombas-Utilidades/CAPDF21/capdf21.pdf` | `70879e17812f`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/dockapreto.pdf` -> `Bombas-Utilidades/Referencia-Bombas-Utilidades/dockapreto/dockapreto.pdf` | `dd03a80cc29c`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/dockavermelho.pdf` -> `Bombas-Utilidades/Referencia-Bombas-Utilidades/dockavermelho/dockavermelho.pdf` | `45bd6abdd316`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/document-91095466-installation-guide-mini-pressurizador-com-pressostato-eletronico-externo-agua-quente-350w-220v-syllent.pdf` -> `Bombas-Utilidades/Referencia-Bombas-Utilidades/91095466-mini-pressuriza/91095466-mini-pressurizador-pressostato-eletronico.pdf` | `b6d3ca86776f`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/electric-motor-ct165.pdf` -> `Bombas-Utilidades/Referencia-Bombas-Utilidades/ELECTRIC-MOTOR-CT165/electric-motor-ct165.pdf` | `38b83326b8ec`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/experience-our-innovation.pdf` -> `Bombas-Utilidades/Referencia-Bombas-Utilidades/EXPERIENCE-OUR-INNOVATIO/experience-our-innovation.pdf` | `b98aba78ee2c`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/johnson-pump-marine-aquat-marine-toilet-stan-1154108b.pdf` -> `Bombas-Utilidades/Johnson-Pump/Geral/johnson-pump-marine-aquat-marine-toilet-stan-1154108b.pdf` | `12d03a0cae41`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/manual-de-instrucoes-para-bomba-de-aguas-cin-d98d4d4c.pdf` -> `Bombas-Utilidades/Referencia-Bombas-Utilidades/instrucoes-para-bomba-ag/manual-de-instrucoes-para-bomba-de-aguas-cin-d98d4d4c.pdf` | `37d247ffbe3a`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/seelevel-ii-tm.pdf` -> `Bombas-Utilidades/Referencia-Bombas-Utilidades/SEELEVEL-II-TM/seelevel-ii-tm.pdf` | `9e532fc28c6f`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/verhroicrizeolnlitaol-wriinzdzlaossnetsale-m-8fa8750d.pdf` -> `Bombas-Utilidades/Referencia-Bombas-Utilidades/verhroicrizeolnlitaol-wr/verhroicrizeolnlitaol-wriinzdzlaossnetsale-m-8fa8750d.pdf` | `43de0e5e640b`
- `copied` | `06_Bombas_Hidraulica_e_Utilidades/whale-2023.pdf` -> `Bombas-Utilidades/Whale/WHALE-2023/whale-2023.pdf` | `b0b5ae3b5e45`
- `copied` | `07_Iluminacao_Sinalizacao_e_Acessorios/officine-comercial-ltda.pdf` -> `Iluminacao-Acessorios/Referencia-Iluminacao/OFFICINE-COMERCIAL-LTDA/officine-comercial-ltda.pdf` | `12190342ffa2`
- `copied` | `07_Iluminacao_Sinalizacao_e_Acessorios/owner-s-manual.pdf` -> `Iluminacao-Acessorios/Referencia-Iluminacao/OWNER-S-MANUAL/owner-s-manual.pdf` | `bf7c64ed69bf`
- `copied` | `07_Iluminacao_Sinalizacao_e_Acessorios/SPL.pdf` -> `Iluminacao-Acessorios/Referencia-Iluminacao/SPL/spl.pdf` | `c82ae584ac5b`
- `copied` | `08_Corrosao_Bonding_e_Seguranca/aluminio.pdf` -> `Corrosao-Seguranca/Referencia-Corrosao-Seguranc/aluminio/aluminio.pdf` | `00255db22e9b`
- `copied` | `08_Corrosao_Bonding_e_Seguranca/caro-cliente.pdf` -> `Corrosao-Seguranca/Referencia-Corrosao-Seguranc/CARO-CLIENTE/caro-cliente.pdf` | `b9e5f60a342e`
- `already-present` | `08_Corrosao_Bonding_e_Seguranca/corrosion-measurement.pdf` -> `Complementar-Brasil/Corrosao/DPH-DPR-IPS/corrosao-eletrolise-dph-dpr-ips-medicoes.pdf` | `6868a575a33a`
- `copied` | `08_Corrosao_Bonding_e_Seguranca/m-y-des-amis-b.pdf` -> `Corrosao-Seguranca/Referencia-Corrosao-Seguranc/M-Y-DES-AMIS-B/m-y-des-amis-b.pdf` | `3b095991edf8`
- `copied` | `08_Corrosao_Bonding_e_Seguranca/VERNIZ-SCHOONER.pdf` -> `Corrosao-Seguranca/Referencia-Corrosao-Seguranc/VERNIZ-SCHOONER/verniz-schooner.pdf` | `94080eb5ac89`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/235-east-airway-boulevard-livermore-cal-c772a288.pdf` -> `Propulsao-Motores/Referencia-Propulsao/235-east-airway-boulevar/235-east-airway-boulevard-livermore-cal-c772a288.pdf` | `5c998713766c`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/235-east-airway-boulevard-livermore-cal-fc96c680.pdf` -> `Propulsao-Motores/Referencia-Propulsao/235-east-airway-boulevar/235-east-airway-boulevard-livermore-cal-fc96c680.pdf` | `b9e0bbe77119`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/31200346-fevereiro-2-2007.pdf` -> `Propulsao-Motores/Referencia-Propulsao/31200346-FEVEREIRO-2-200/31200346-fevereiro-2-2007.pdf` | `3a0fb0162411`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/3TNC78L-RTBA.pdf` -> `Propulsao-Motores/Referencia-Propulsao/3TNC78L-RTBA/3tnc78l-rtba.pdf` | `54e8de048706`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/5648ffb8-6efb-48bb-aa5d-270a51b18862por-d75c11ad.pdf` -> `Propulsao-Motores/Referencia-Propulsao/5648ffb8-6efb-48bb-aa5d/5648ffb8-6efb-48bb-aa5d-270a51b18862por-d75c11ad.pdf` | `5431892c0da0`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/67AUTOMATION.pdf` -> `Propulsao-Motores/Referencia-Propulsao/67AUTOMATION/67automation.pdf` | `22d9863132c1`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/6eod.pdf` -> `Propulsao-Motores/Referencia-Propulsao/6EOD/6eod.pdf` | `73ddbba37508`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/8m0128973-517-eng.pdf` -> `Propulsao-Motores/Referencia-Propulsao/8M0128973-517-ENG/8m0128973-517-eng.pdf` | `b9d69997d025`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/accessories-catalog.pdf` -> `Propulsao-Motores/Referencia-Propulsao/ACCESSORIES-CATALOG/accessories-catalog.pdf` | `473a8a90425f`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/B185-M843NW3G-1.pdf` -> `Propulsao-Motores/Referencia-Propulsao/B185-M843NW3G-1/b185-m843nw3g-1.pdf` | `5e5b9a630f22`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/bow-thrusters.pdf` -> `Propulsao-Motores/Referencia-Propulsao/BOW-THRUSTERS/bow-thrusters.pdf` | `dec935cbfc2e`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/capdf18.pdf` -> `Propulsao-Motores/Referencia-Propulsao/CAPDF18/capdf18.pdf` | `7755cbd5ac12`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/capdf19.pdf` -> `Propulsao-Motores/Referencia-Propulsao/CAPDF19/capdf19.pdf` | `95956834c517`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/capdf22.pdf` -> `Propulsao-Motores/Referencia-Propulsao/CAPDF22/capdf22.pdf` | `ffca6b759159`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/catalogo-motori.pdf` -> `Propulsao-Motores/Referencia-Propulsao/CATALOGO-MOTORI/catalogo-motori.pdf` | `f9e41dfc285b`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/cnpj-07-884-277-0001-73-inscricaoestadu-f0c649c5.pdf` -> `Propulsao-Motores/Referencia-Propulsao/cnpj-884-277-0001-inscri/cnpj-07-884-277-0001-73-inscricaoestadu-f0c649c5.pdf` | `af597e096e04`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/co-buu-and-nv-j.pdf` -> `Propulsao-Motores/Referencia-Propulsao/CO-BUU-AND-NV-J/co-buu-and-nv-j.pdf` | `014f05a12ada`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/e8c8da.pdf` -> `Propulsao-Motores/Referencia-Propulsao/E8C8DA/e8c8da.pdf` | `aeeb6fe6d7c8`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/ed-luglio-2022.pdf` -> `Propulsao-Motores/Referencia-Propulsao/ED-LUGLIO-2022/ed-luglio-2022.pdf` | `ee5dfb566a5d`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/edizione-2001.pdf` -> `Propulsao-Motores/Referencia-Propulsao/EDIZIONE-2001/edizione-2001.pdf` | `fe3fdb81d9d1`
- `already-present` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/gp-boats-2023.pdf` -> `Complementar-Brasil/Volvo-Penta/Catalogo-GP-Boats/volvo-penta-catalogo-pecas-gp-boats.pdf` | `19234b42fdf9`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/GRT7-TH4.pdf` -> `Propulsao-Motores/Referencia-Propulsao/GRT7-TH4/grt7-th4.pdf` | `6a37269dbfc9`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/h-y-d-r-a-u-l-i-c.pdf` -> `Propulsao-Motores/Referencia-Propulsao/H-Y-D-R-A-U-L-I-C/h-y-d-r-a-u-l-i-c.pdf` | `20ee6db154d4`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/industrial-and-marine-engines-dup-2.pdf` -> `Propulsao-Motores/Referencia-Propulsao/industrial-engines-dup/industrial-and-marine-engines-dup-2.pdf` | `3238c6d6d088`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/industrial-and-marine-engines-dup-3.pdf` -> `Propulsao-Motores/Referencia-Propulsao/industrial-engines-dup/industrial-and-marine-engines-dup-3.pdf` | `f1dda7f77ea5`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/industrial-and-marine-engines.pdf` -> `Propulsao-Motores/Referencia-Propulsao/industrial-engines/industrial-and-marine-engines.pdf` | `663d6a160079`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/instruction-book.pdf` -> `Propulsao-Motores/Referencia-Propulsao/INSTRUCTION-BOOK/instruction-book.pdf` | `4bd33ea30282`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/lewmar-cpx-vertical-windlass-66300104-iss-9.pdf` -> `Propulsao-Motores/Referencia-Propulsao/lewmar-cpx-vertical-wind/lewmar-cpx-vertical-windlass-66300104-iss-9.pdf` | `d4a1a80638ed`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/lewmar-v1-6-windlass-65001201-issue-11.pdf` -> `Propulsao-Motores/Referencia-Propulsao/lewmar-windlass-65001201/lewmar-v1-6-windlass-65001201-issue-11.pdf` | `d15ecf7a6158`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/lighthouse-tm-multifunction-display-ope-5507d454.pdf` -> `Propulsao-Motores/Referencia-Propulsao/lighthouse-multifunction/lighthouse-tm-multifunction-display-ope-5507d454.pdf` | `100896827809`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/MACS.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MACS/macs.pdf` | `df8a266135f1`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/man-mc2-x10-en-rev002a.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MAN-MC2-X10-EN-REV002A/man-mc2-x10-en-rev002a.pdf` | `96fbc304fedd`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/manual-grta-4-multilinguas.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MANUAL-GRTA-4-MULTILINGU/manual-grta-4-multilinguas.pdf` | `b686563edd87`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/Manual-GRTA-4.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MANUAL-GRTA-4/manual-grta-4.pdf` | `c4cb4e4fe262`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/Manual-telecomandos.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MANUAL-TELECOMANDOS/manual-telecomandos.pdf` | `87450d33d671`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/MANUAL-ZEN150-230V-TRASD-ENG.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MANUAL-ZEN150-230V-TRASD/manual-zen150-230v-trasd-eng.pdf` | `eefe957b4adb`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/MANUAL-ZEN150-24V-TRASD-ENG.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MANUAL-ZEN150-24V-TRASD/manual-zen150-24v-trasd-eng.pdf` | `fbdbab1dadba`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/MANUAL-ZEN30-12-24V.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MANUAL-ZEN30-12-24V/manual-zen30-12-24v.pdf` | `fbc840032aed`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/manuel-d-atelier-d.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MANUEL-D-ATELIER-D/manuel-d-atelier-d.pdf` | `9db9737de95f`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/marine-equipment-guide.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MARINE-EQUIPMENT-GUIDE/marine-equipment-guide.pdf` | `25922a5c437a`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/marine-generator-sets-dup-6.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MARINE-GENERATOR-SETS-DU/marine-generator-sets-dup-6.pdf` | `8ac52873aba0`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/marine-generator-sets.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MARINE-GENERATOR-SETS/marine-generator-sets.pdf` | `a51f69d703e8`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/MN700.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MN700/mn700.pdf` | `9a354150909a`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/MN900.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MN900/mn900.pdf` | `18fe39053408`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/models-1204m-05m-09m-21m-dup-2.pdf` -> `Propulsao-Motores/Referencia-Propulsao/1204m-05m-09m-21m-dup/models-1204m-05m-09m-21m-dup-2.pdf` | `2877cec21a17`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/models-1204m-05m-09m-21m.pdf` -> `Propulsao-Motores/Referencia-Propulsao/MODELS-1204M-05M-09M-21M/models-1204m-05m-09m-21m.pdf` | `7432e6e0b827`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/motores-industriais-e-maritimos.pdf` -> `Propulsao-Motores/Referencia-Propulsao/motores-industriais-mari/motores-industriais-e-maritimos.pdf` | `08672e089fef`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/OM843NW3.pdf` -> `Propulsao-Motores/Referencia-Propulsao/OM843NW3/om843nw3.pdf` | `7571cd41af6f`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/operator-s-manual-p.pdf` -> `Propulsao-Motores/Referencia-Propulsao/OPERATOR-S-MANUAL-P/operator-s-manual-p.pdf` | `50ec814d24c5`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/operator-s-manual.pdf` -> `Propulsao-Motores/Referencia-Propulsao/OPERATOR-S-MANUAL/operator-s-manual.pdf` | `a9d2a4d1dd60`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/P843-3.pdf` -> `Propulsao-Motores/Referencia-Propulsao/P843/p843-3.pdf` | `e6a6d675fd6c`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/propulsao-motores-e-turbo-547726ed.pdf` -> `Propulsao-Motores/Referencia-Propulsao/propulsao-motores-turbo/propulsao-motores-e-turbo-547726ed.pdf` | `547726ed710b`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/service-manual.pdf` -> `Propulsao-Motores/Referencia-Propulsao/SERVICE-MANUAL/service-manual.pdf` | `f47deffcc87c`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/service-parts-dup-2.pdf` -> `Propulsao-Motores/Referencia-Propulsao/SERVICE-PARTS-DUP-2/service-parts-dup-2.pdf` | `4d243514a427`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/service-parts.pdf` -> `Propulsao-Motores/Referencia-Propulsao/SERVICE-PARTS/service-parts.pdf` | `07c0ac116ec6`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/servicemanualtneseries1ocr.pdf` -> `Propulsao-Motores/Referencia-Propulsao/SERVICEMANUALTNESERIES1O/servicemanualtneseries1ocr.pdf` | `04e64f519519`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/smart-compact-design-easy-installation.pdf` -> `Propulsao-Motores/Referencia-Propulsao/smart-compact-design-eas/smart-compact-design-easy-installation.pdf` | `980d0e6696c5`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/superior-technology.pdf` -> `Propulsao-Motores/Referencia-Propulsao/SUPERIOR-TECHNOLOGY/superior-technology.pdf` | `66bfdab15f7e`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/thruster-systems.pdf` -> `Propulsao-Motores/Referencia-Propulsao/THRUSTER-SYSTEMS/thruster-systems.pdf` | `75fc0836cbcb`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/tp6252.pdf` -> `Propulsao-Motores/Referencia-Propulsao/TP6252/tp6252.pdf` | `c0003ffef8fe`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/tp6255.pdf` -> `Propulsao-Motores/Referencia-Propulsao/TP6255/tp6255.pdf` | `516bbd3d42fd`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/tp6772.pdf` -> `Propulsao-Motores/Referencia-Propulsao/TP6772/tp6772.pdf` | `dc279056e42e`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/tp6775.pdf` -> `Propulsao-Motores/Referencia-Propulsao/TP6775/tp6775.pdf` | `8470d3e3b1ea`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/ultraflex-control-systems-s-r-l.pdf` -> `Propulsao-Motores/Ultraflex/Geral/ultraflex-control-systems-s-r-l.pdf` | `1f9dd0022270`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/valves-and-electronics.pdf` -> `Propulsao-Motores/Referencia-Propulsao/VALVES-AND-ELECTRONICS/valves-and-electronics.pdf` | `07ac6d782756`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/vw5cylinderoperatingmanual.pdf` -> `Propulsao-Motores/Referencia-Propulsao/VW5CYLINDEROPERATINGMANU/vw5cylinderoperatingmanual.pdf` | `6649fa0aa113`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/workshop-manual-vw-marine-boat-engine.pdf` -> `Propulsao-Motores/Referencia-Propulsao/workshop-boat-engine/workshop-manual-vw-marine-boat-engine.pdf` | `b9276254cab6`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/ydes04.pdf` -> `Propulsao-Motores/Referencia-Propulsao/YDES04/ydes04.pdf` | `8666504a0fbb`
- `copied` | `09_Propulsao_Motores_Estabilizacao_e_Atuacao/ZEN150-12-24V-TOUCH.pdf` -> `Propulsao-Motores/Referencia-Propulsao/ZEN150-12-24V-TOUCH/zen150-12-24v-touch.pdf` | `b127103bddb1`
- `copied` | `10_Materiais_Internos_e_Cursos/dni-0409-dni-0413.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/DNI-0409-DNI-0413/dni-0409-dni-0413.pdf` | `953968223fb1`
- `copied` | `10_Materiais_Internos_e_Cursos/fundamentos-da-eletrica-nautica.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/fundamentos-eletrica-nau/fundamentos-da-eletrica-nautica.pdf` | `4f4e79bf1f2b`
- `copied` | `10_Materiais_Internos_e_Cursos/i-publico-alvo-eletricista-auxiliar-de-eletrici-65f4cb48.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/publico-alvo-eletricista/i-publico-alvo-eletricista-auxiliar-de-eletrici-65f4cb48.pdf` | `3ffa0e29f616`
- `copied` | `10_Materiais_Internos_e_Cursos/i-publico-alvo-gerentes-administrativo-de-marin-1cdd16fe.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/publico-alvo-gerentes-ad/i-publico-alvo-gerentes-administrativo-de-marin-1cdd16fe.pdf` | `819e350fd832`
- `copied` | `10_Materiais_Internos_e_Cursos/i-publico-alvo-mecanicos-as-e-auxiliares-de-mec-c8479237.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/publico-alvo-mecanicos-a/i-publico-alvo-mecanicos-as-e-auxiliares-de-mec-c8479237.pdf` | `7893fbfe91cc`
- `copied` | `10_Materiais_Internos_e_Cursos/Manual0305.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/MANUAL0305/manual0305.pdf` | `992f869e9002`
- `copied` | `10_Materiais_Internos_e_Cursos/Manual0409-0413.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/MANUAL0409-0413/manual0409-0413.pdf` | `361675976967`
- `copied` | `10_Materiais_Internos_e_Cursos/motores-eletricos.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/MOTORES-ELETRICOS/motores-eletricos.pdf` | `f5acdfc1f53a`
- `copied` | `10_Materiais_Internos_e_Cursos/Referencias_Tecnicas/2015-msc-pemm-gustavo-henrique-senna-de-64db7732.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/Referencias-Tecnicas/2015-msc-pemm-gustavo-henrique-senna-de-64db7732.pdf` | `21f8717aa694`
- `copied` | `10_Materiais_Internos_e_Cursos/Referencias_Tecnicas/a-confraria-europeia-da-vela.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/A-CONFRARIA-EUROPEIA-DA/a-confraria-europeia-da-vela.pdf` | `7a2b74af48ff`
- `copied` | `10_Materiais_Internos_e_Cursos/Referencias_Tecnicas/Non-Metallic-Materials-Brochure.pdf` -> `Materiais-Internos/Referencia-Materiais-Interno/Referencias-Tecnicas/non-metallic-materials-brochure.pdf` | `fb258876ba1d`

## Proxima fila sugerida

- converter HTML tecnico exportado para PDF arquivado e/ou nota Markdown curada quando o conteudo for fonte primaria util
- transformar imagens avulsas em anexos documentados ou descartar duplicatas visuais sem valor tecnico
- rodar novamente a pipeline de OCR para os PDFs promovidos com baixa extracao textual
