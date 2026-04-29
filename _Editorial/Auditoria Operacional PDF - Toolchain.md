---
title: "Auditoria Operacional PDF - Toolchain"
note_type: "audit"
domain: "90_Revisao_Manual"
status: "auto-generated"
reviewed_on: "2026-04-28"
review_jurisdiction: "Brasil"
related_notes:
  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Local - Indice Gerado"
  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado"
---

# Auditoria Operacional PDF - Toolchain

> [!abstract] Resumo tecnico
> Relatorio gerado com Poppler, qpdf, ExifTool, Tesseract, MuPDF, ImageMagick, Ghostscript e 7-Zip instalados no ambiente.
> Objetivo: transformar os PDFs em acervo auditavel, pesquisavel e pronto para filas de OCR/curadoria.

> [!info] Geracao
> Comando: `python scripts/acervo/audit_pdf_toolchain.py --scope all`.
> Escopo desta execucao: `main`.
> Gerado em `2026-04-29T01:22:06.674892+00:00`.

## Resultado executivo

- PDFs auditados: `248`
- tamanho total auditado: `1.2 GB`
- paginas conhecidas somadas: `14834`
- PDFs criptografados: `36`
- grupos de duplicatas fisicas por SHA-256: `7`
- arquivos envolvidos em duplicatas: `20`
- notas companheiras faltantes no acervo principal: `0`
- OCR amostral executado em: `0` candidato(s)

## Ferramentas detectadas

- `pdftotext`: `pdftotext version 25.07.0` - `C:\Users\User\AppData\Local\Microsoft\WinGet\Packages\oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe\poppler-25.07.0\Library\bin\pdftotext.EXE`
- `pdfinfo`: `pdfinfo version 25.07.0` - `C:\Users\User\AppData\Local\Microsoft\WinGet\Packages\oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe\poppler-25.07.0\Library\bin\pdfinfo.EXE`
- `pdftoppm`: `pdftoppm version 25.07.0` - `C:\Users\User\AppData\Local\Microsoft\WinGet\Packages\oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe\poppler-25.07.0\Library\bin\pdftoppm.EXE`
- `qpdf`: `qpdf.EXE version 12.3.2` - `C:\Program Files\qpdf 12.3.2\bin\qpdf.EXE`
- `exiftool`: `13.57` - `C:\Users\User\AppData\Local\Programs\ExifTool\exiftool.EXE`
- `tesseract`: `tesseract v5.5.0.20241111` - `C:\Program Files\Tesseract-OCR\tesseract.EXE`
- `mutool`: `mutool version 1.23.0` - `C:\Users\User\AppData\Local\Microsoft\WinGet\Packages\ArtifexSoftware.mutool_Microsoft.Winget.Source_8wekyb3d8bbwe\mupdf-1.23.0-windows\mutool.EXE`
- `magick`: `Version: ImageMagick 7.1.2-21 Q16 x64 c86de04:20260421 https://imagemagick.org` - `C:\Users\User\AppData\Local\Microsoft\WindowsApps\magick.EXE`
- `gswin64c`: `GPL Ghostscript 10.07.0 (2026-03-16)` - `C:\Program Files\gs\gs10.07.0\bin\gswin64c.EXE`
- `7z`: `7-Zip 26.00 (x64) : Copyright (c) 1999-2026 Igor Pavlov : 2026-02-12` - `C:\Program Files\7-Zip\7z.EXE`

## Recorte do acervo principal

- PDFs curados: `248`
- paginas conhecidas: `14834`
- qpdf: `ok:144, warning:104`
- texto pesquisavel: `nao:12, sim:236`
- OCR: `bloqueado:2, concluido:10, nao:236`

## Distribuicao por colecao

- `acervo-principal`: `248`

## Status estrutural qpdf

- `ok`: `144`
- `warning`: `104`

## Texto pesquisavel

- `nao`: `12`
- `sim`: `236`

## Metodos de texto

- `no-text-detected`: `3`
- `pdf-stream-strings`: `18`
- `pdf-stream-strings-low-confidence`: `9`
- `pdftotext`: `218`

## Prioridade de OCR

- `bloqueado`: `2`
- `concluido`: `10`
- `nao`: `236`

## Fila operacional de OCR

- `bloqueado` - [900-0541b-energy-command-operation-manual.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/Geral/900-0541b-energy-command-operation-manual.pdf>) - `acervo-principal` - `29` pag. - PDF com restricao interna; resolver permissao antes de OCR
- `bloqueado` - [manual-gerador-parts-e-pecas.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Referencia-Geradores/MANUAL-GERADOR-PARTS-E-P/manual-gerador-parts-e-pecas.pdf>) - `acervo-principal` - `96` pag. - PDF com restricao interna; resolver permissao antes de OCR

## Problemas estruturais ou de leitura

- `warning` - [60020-0024.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Bombas-Utilidades/Referencia-Bombas-Utilidades/60020-0024/60020-0024.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Bombas-Utilidades\Referencia-Bombas-Utilidades\60020-0024\60020-0024.pdf: part 8 is empty but nshared_total > nshared_first_page; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Bombas-Utilidades\Referencia-Bombas-Utilidades\60020-0024\60020-0024.pdf: page 0 has shared identifier entries`
- `warning` - [91095466-mini-pressurizador-pressostato-eletronico.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Bombas-Utilidades/Referencia-Bombas-Utilidades/91095466-mini-pressuriza/91095466-mini-pressurizador-pressostato-eletronico.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Bombas-Utilidades\Referencia-Bombas-Utilidades\91095466-mini-pressuriza\91095466-mini-pressurizador-pressostato-eletronico.pdf: shared object hint table: ntotal < nfirst_page; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Bombas-Utilidades\Referencia-Bombas-Utilidades\91095466-mini-pressuriza\91095466-mini-pressurizador-pressostato-eletronico.pdf: object count mismatch for page 1: hint table = 7; computed = 6`
- `warning` - [electric-motor-ct165.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Bombas-Utilidades/Referencia-Bombas-Utilidades/ELECTRIC-MOTOR-CT165/electric-motor-ct165.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Bombas-Utilidades\Referencia-Bombas-Utilidades\ELECTRIC-MOTOR-CT165\electric-motor-ct165.pdf: linearized file contains an uncompressed object after a compressed one in a cross-reference stream; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Bombas-Utilidades\Referencia-Bombas-Utilidades\ELECTRIC-MOTOR-CT165\electric-motor-ct165.pdf: part 8 is empty but nshared_total > nshared_first_page`
- `warning` - [seelevel-ii-tm.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Bombas-Utilidades/Referencia-Bombas-Utilidades/SEELEVEL-II-TM/seelevel-ii-tm.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Bombas-Utilidades\Referencia-Bombas-Utilidades\SEELEVEL-II-TM\seelevel-ii-tm.pdf: shared object 0 length mismatch: hint table = 36; computed = 1295; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Bombas-Utilidades\Referencia-Bombas-Utilidades\SEELEVEL-II-TM\seelevel-ii-tm.pdf: shared object 1 length mismatch: hint table = 1295; computed = 547`
- `warning` - [cruisair-tempered-water-system.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Climatizacao/Dometic/Geral/cruisair-tempered-water-system.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Climatizacao\Dometic\Geral\cruisair-tempered-water-system.pdf: page 0 has shared identifier entries; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Climatizacao\Dometic\Geral\cruisair-tempered-water-system.pdf: page 0: shared object 155: in hint table but not computed list`
- `warning` - [dometic-chilled-water-operating-manual.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Climatizacao/Dometic/Geral/dometic-chilled-water-operating-manual.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Climatizacao\Dometic\Geral\dometic-chilled-water-operating-manual.pdf: page 0 has shared identifier entries; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Climatizacao\Dometic\Geral\dometic-chilled-water-operating-manual.pdf: page 0: shared object 139: in hint table but not computed list`
- `warning` - [dometic-mtcg-9108893793-75371.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Climatizacao/Dometic/Geral/dometic-mtcg-9108893793-75371.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Climatizacao\Dometic\Geral\dometic-mtcg-9108893793-75371.pdf: linearized file contains an uncompressed object after a compressed one in a cross-reference stream; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Climatizacao\Dometic\Geral\dometic-mtcg-9108893793-75371.pdf: object count mismatch for page 0: hint table = 16; computed = 19`
- `warning` - [dometic-cruisair-marine-air-conditioners-price-list-2015.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Climatizacao/Dometic/Self-Contained/dometic-cruisair-marine-air-conditioners-price-list-2015.pdf>) - `WARNING: page object 302 0 stream 4002 0, stream 1818 0, stream 303 0, stream 1820 0, stream 2346 0, stream 4004 0, stream 4465 0 (content, offset 2755637): treating unexpected brace token as null; WARNING: page object 302 0 stream 4002 0, stream 1818 0, stream 303 0, stream 1820 0, stream 2346 0, stream 4004 0, stream 4465 0 (content, offset 2755638): treating unexpected brace token as null`
- `warning` - [dometic-cruisair-self-contained-air-conditioner-installation-manual-dx-remote-804-746.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Climatizacao/Dometic/Self-Contained/dometic-cruisair-self-contained-air-conditioner-installation-manual-dx-remote-804-746.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Climatizacao\Dometic\Self-Contained\dometic-cruisair-self-contained-air-conditioner-installation-manual-dx-remote-804-746.pdf: linearized file contains an uncompressed object after a compressed one in a cross-reference stream; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Climatizacao\Dometic\Self-Contained\dometic-cruisair-self-contained-air-conditioner-installation-manual-dx-remote-804-746.pdf: first shared object number mismatch: hint table = 153; computed = 155`
- `warning` - [dometic-cruisair-self-contained-air-conditioner-troubleshooting-guide.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Climatizacao/Dometic/Self-Contained/dometic-cruisair-self-contained-air-conditioner-troubleshooting-guide.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Climatizacao\Dometic\Self-Contained\dometic-cruisair-self-contained-air-conditioner-troubleshooting-guide.pdf: part 8 is empty but nshared_total > nshared_first_page; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Climatizacao\Dometic\Self-Contained\dometic-cruisair-self-contained-air-conditioner-troubleshooting-guide.pdf: first shared object offset mismatch: hint table = 697786; computed = 697432`
- `warning` - [dometic-marine-air-conditioners-price-list-2024.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Climatizacao/Dometic/Self-Contained/dometic-marine-air-conditioners-price-list-2024.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Climatizacao\Dometic\Self-Contained\dometic-marine-air-conditioners-price-list-2024.pdf: shared object 0 length mismatch: hint table = 36; computed = 1064; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Climatizacao\Dometic\Self-Contained\dometic-marine-air-conditioners-price-list-2024.pdf: shared object 1 length mismatch: hint table = 1064; computed = 413`
- `warning` - [h-tec-hfc-acqua-catalogo-on-board.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Climatizacao/H-Tec/HFC-Acqua/h-tec-hfc-acqua-catalogo-on-board.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Climatizacao\H-Tec\HFC-Acqua\h-tec-hfc-acqua-catalogo-on-board.pdf (offset 13803482): input stream is complete but output may still be valid; qpdf.EXE: operation succeeded with warnings`
- `warning` - [chilled-water-air-conditioning.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Climatizacao/Referencia-Climatizacao/chilled-water-conditioni/chilled-water-air-conditioning.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Climatizacao\Referencia-Climatizacao\chilled-water-conditioni\chilled-water-air-conditioning.pdf: part 8 is empty but nshared_total > nshared_first_page; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Climatizacao\Referencia-Climatizacao\chilled-water-conditioni\chilled-water-air-conditioning.pdf: page 0 has shared identifier entries`
- `warning` - [manual-ar-condicionado.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Climatizacao/Referencia-Climatizacao/MANUAL-AR-CONDICIONADO/manual-ar-condicionado.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Climatizacao\Referencia-Climatizacao\MANUAL-AR-CONDICIONADO\manual-ar-condicionado.pdf: linearized file contains an uncompressed object after a compressed one in a cross-reference stream; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Climatizacao\Referencia-Climatizacao\MANUAL-AR-CONDICIONADO\manual-ar-condicionado.pdf: first shared object offset mismatch: hint table = 784952; computed = 735257`
- `warning` - [corrosao-eletrolise-dph-dpr-ips-medicoes.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Complementar-Brasil/Corrosao/DPH-DPR-IPS/corrosao-eletrolise-dph-dpr-ips-medicoes.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Complementar-Brasil\Corrosao\DPH-DPR-IPS\corrosao-eletrolise-dph-dpr-ips-medicoes.pdf: page 0 has shared identifier entries; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Complementar-Brasil\Corrosao\DPH-DPR-IPS\corrosao-eletrolise-dph-dpr-ips-medicoes.pdf: page 0: shared object 4528: in hint table but not computed list`
- `warning` - [aluminio.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Corrosao-Seguranca/Referencia-Corrosao-Seguranc/aluminio/aluminio.pdf>) - `checking C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Corrosao-Seguranca\Referencia-Corrosao-Seguranc\aluminio\aluminio.pdf; PDF Version: 1.2`
- `warning` - [19-informativo-tecnico-no.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Energia-DC/Referencia-Energia-DC/19-INFORMATIVO-TECNICO-N/19-informativo-tecnico-no.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Energia-DC\Referencia-Energia-DC\19-INFORMATIVO-TECNICO-N\19-informativo-tecnico-no.pdf: page 0 has shared identifier entries; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Energia-DC\Referencia-Energia-DC\19-INFORMATIVO-TECNICO-N\19-informativo-tecnico-no.pdf: page 0: shared object 24: in hint table but not computed list`
- `warning` - [722-ne.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Energia-DC/Referencia-Energia-DC/722-NE/722-ne.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Energia-DC\Referencia-Energia-DC\722-NE\722-ne.pdf: linearized file contains an uncompressed object after a compressed one in a cross-reference stream; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Energia-DC\Referencia-Energia-DC\722-NE\722-ne.pdf: first shared object offset mismatch: hint table = 479336; computed = 339138`
- `warning` - [bch-opt-41-bivolt.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Energia-DC/Referencia-Energia-DC/BCH-OPT-41-BIVOLT/bch-opt-41-bivolt.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Energia-DC\Referencia-Energia-DC\BCH-OPT-41-BIVOLT\bch-opt-41-bivolt.pdf: page 0 has shared identifier entries; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Energia-DC\Referencia-Energia-DC\BCH-OPT-41-BIVOLT\bch-opt-41-bivolt.pdf: page 0: shared object 157: in hint table but not computed list`
- `warning` - [nautical-equipment-evolution.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Energia-DC/Referencia-Energia-DC/NAUTICAL-EQUIPMENT-EVOLU/nautical-equipment-evolution.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Energia-DC\Referencia-Energia-DC\NAUTICAL-EQUIPMENT-EVOLU\nautical-equipment-evolution.pdf: page 0 has shared identifier entries; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Energia-DC\Referencia-Energia-DC\NAUTICAL-EQUIPMENT-EVOLU\nautical-equipment-evolution.pdf: page 0: shared object 450: in hint table but not computed list`
- `warning` - [17-5mdkae.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/17-5MDKAE/17-5mdkae.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\17-5MDKAE\17-5mdkae.pdf: end of first page section (/E) mismatch: /E = 230559; computed = 230407..230408; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\17-5MDKAE\17-5mdkae.pdf: part 8 is empty but nshared_total > nshared_first_page`
- `warning` - [7953-hdkah-spec-a-n-operator-manual-2015.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/Geral/7953-hdkah-spec-a-n-operator-manual-2015.pdf>) - `checking C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\Geral\7953-hdkah-spec-a-n-operator-manual-2015.pdf; PDF Version: 1.6`
- `warning` - [900-0541b-energy-command-operation-manual.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/Geral/900-0541b-energy-command-operation-manual.pdf>) - `checking C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\Geral\900-0541b-energy-command-operation-manual.pdf; PDF Version: 1.4`
- `warning` - [934-0602-onan-mdl3-mdl4-mdl6-marine-genset-installation-manual-01-1991.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/Geral/934-0602-onan-mdl3-mdl4-mdl6-marine-genset-installation-manual-01-1991.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\Geral\934-0602-onan-mdl3-mdl4-mdl6-marine-genset-installation-manual-01-1991.pdf (offset 1989434): input stream is complete but output may still be valid; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\Geral\934-0602-onan-mdl3-mdl4-mdl6-marine-genset-installation-manual-01-1991.pdf (offset 1989517): input stream is complete but output may still be valid`
- `warning` - [hdkah-hdkaj-hdkak-hdkau-hdkav-service-manual.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/Geral/hdkah-hdkaj-hdkak-hdkau-hdkav-service-manual.pdf>) - `checking C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\Geral\hdkah-hdkaj-hdkak-hdkau-hdkav-service-manual.pdf; PDF Version: 1.6`
- `warning` - [onan-mcck-marine-genset-manual.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/Geral/onan-mcck-marine-genset-manual.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\Geral\onan-mcck-marine-genset-manual.pdf: shared object 0 length mismatch: hint table = 135; computed = 328; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\Geral\onan-mcck-marine-genset-manual.pdf: shared object 1 length mismatch: hint table = 328; computed = 1181`
- `warning` - [onan-troubleshooting-guide-codes.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/Geral/onan-troubleshooting-guide-codes.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\Geral\onan-troubleshooting-guide-codes.pdf: linearized file contains an uncompressed object after a compressed one in a cross-reference stream; WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\Geral\onan-troubleshooting-guide-codes.pdf: part 8 is empty but nshared_total > nshared_first_page`
- `warning` - [cummins-onan-mdkad-mdkae-mdkaf-operator-manual-981-0140-1996-02.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKAD-MDKAE-MDKAF/cummins-onan-mdkad-mdkae-mdkaf-operator-manual-981-0140-1996-02.pdf>) - `checking C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\MDKAD-MDKAE-MDKAF\cummins-onan-mdkad-mdkae-mdkaf-operator-manual-981-0140-1996-02.pdf; PDF Version: 1.6`
- `warning` - [cummins-onan-mdkad-mdkae-mdkaf-service-manual-981-0520b.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKAD-MDKAE-MDKAF/cummins-onan-mdkad-mdkae-mdkaf-service-manual-981-0520b.pdf>) - `checking C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\MDKAD-MDKAE-MDKAF\cummins-onan-mdkad-mdkae-mdkaf-service-manual-981-0520b.pdf; PDF Version: 1.6`
- `warning` - [cummins-onan-mdkbh-service-manual-981-0542.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKBH/cummins-onan-mdkbh-service-manual-981-0542.pdf>) - `checking C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\MDKBH\cummins-onan-mdkbh-service-manual-981-0542.pdf; PDF Version: 1.6`
- `warning` - [cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-operator-manual-a052j727.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDK/cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-operator-manual-a052j727.pdf>) - `checking C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\MDKDK\cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-operator-manual-a052j727.pdf; PDF Version: 1.6`
- `warning` - [cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-service-manual-a052j731.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDK/cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-service-manual-a052j731.pdf>) - `checking C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\MDKDK\cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-service-manual-a052j731.pdf; PDF Version: 1.6`
- `warning` - [cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-operator-manual-a052j727.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDL/cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-operator-manual-a052j727.pdf>) - `checking C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\MDKDL\cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-operator-manual-a052j727.pdf; PDF Version: 1.6`
- `warning` - [cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-service-manual-a052j731.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDL/cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-service-manual-a052j731.pdf>) - `checking C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\MDKDL\cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-service-manual-a052j731.pdf; PDF Version: 1.6`
- `warning` - [cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-operator-manual-a052j727.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDM-MDKDN/cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-operator-manual-a052j727.pdf>) - `checking C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\MDKDM-MDKDN\cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-operator-manual-a052j727.pdf; PDF Version: 1.6`
- `warning` - [cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-service-manual-a052j731.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDM-MDKDN/cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-service-manual-a052j731.pdf>) - `checking C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\MDKDM-MDKDN\cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-service-manual-a052j731.pdf; PDF Version: 1.6`
- `warning` - [cummins-onan-mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv-installation-manual-a046j598.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDP-MDKDR-MDKDV/cummins-onan-mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv-installation-manual-a046j598.pdf>) - `WARNING: C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\MDKDP-MDKDR-MDKDV\cummins-onan-mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv-installation-manual-a046j598.pdf: end of first page section (/E) mismatch: /E = 11549; computed = 31705..31707; qpdf.EXE: operation succeeded with warnings`
- `warning` - [cummins-onan-mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv-service-manual-a046j602.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDP-MDKDR-MDKDV/cummins-onan-mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv-service-manual-a046j602.pdf>) - `checking C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\MDKDP-MDKDR-MDKDV\cummins-onan-mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv-service-manual-a046j602.pdf; PDF Version: 1.6`
- `warning` - [cummins-onan-mdkdp-mdkdr-mdkdv-parts-manual-a046l892.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDP-MDKDR-MDKDV/cummins-onan-mdkdp-mdkdr-mdkdv-parts-manual-a046l892.pdf>) - `checking C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\MDKDP-MDKDR-MDKDV\cummins-onan-mdkdp-mdkdr-mdkdv-parts-manual-a046l892.pdf; PDF Version: 1.6`
- `warning` - [cummins-onan-mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv-service-manual-a046j602.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDS-MDKDT-MDKDU/cummins-onan-mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv-service-manual-a046j602.pdf>) - `checking C:\Users\User\Desktop\ELETRO NAUTICA OBSIDIAN\ELETRO NAUTICA\90_Revisao_Manual\_Acervo_Local\Geradores\Cummins-Onan\MDKDS-MDKDT-MDKDU\cummins-onan-mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv-service-manual-a046j602.pdf; PDF Version: 1.6`

## Maiores PDFs

- [marine-equipment-guide.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Propulsao-Motores/Referencia-Propulsao/MARINE-EQUIPMENT-GUIDE/marine-equipment-guide.pdf>) - `89.1 MB` - `412` pag. - `acervo-principal`
- [p753.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Campo-Clientes/Referencia-Campo/Imagens-e-Recortes-Tecni/p753.pdf>) - `53.8 MB` - `68` pag. - `acervo-principal`
- [67automation.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Propulsao-Motores/Referencia-Propulsao/67AUTOMATION/67automation.pdf>) - `46.9 MB` - `331` pag. - `acervo-principal`
- [lighthouse-tm-multifunction-display-ope-5507d454.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Propulsao-Motores/Referencia-Propulsao/lighthouse-multifunction/lighthouse-tm-multifunction-display-ope-5507d454.pdf>) - `42.9 MB` - `390` pag. - `acervo-principal`
- [workshop-manual-vw-marine-boat-engine.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Propulsao-Motores/Referencia-Propulsao/workshop-boat-engine/workshop-manual-vw-marine-boat-engine.pdf>) - `39.0 MB` - `453` pag. - `acervo-principal`
- [baixa-tensao.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Shore-Power-AC/Referencia-Shore-Power/BAIXA-TENSAO/baixa-tensao.pdf>) - `38.5 MB` - `358` pag. - `acervo-principal`
- [atlas-eolico-rs.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Energia-DC/Referencia-Energia-DC/ATLAS-EOLICO-RS/atlas-eolico-rs.pdf>) - `32.4 MB` - `65` pag. - `acervo-principal`
- [cummins-onan-mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv-service-manual-a046j602.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDP-MDKDR-MDKDV/cummins-onan-mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv-service-manual-a046j602.pdf>) - `25.2 MB` - `142` pag. - `acervo-principal`
- [cummins-onan-mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv-service-manual-a046j602.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDS-MDKDT-MDKDU/cummins-onan-mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv-service-manual-a046j602.pdf>) - `25.2 MB` - `142` pag. - `acervo-principal`
- [cummins-onan-mdkbh-service-manual-981-0542.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKBH/cummins-onan-mdkbh-service-manual-981-0542.pdf>) - `21.8 MB` - `138` pag. - `acervo-principal`
- [whale-2023.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Bombas-Utilidades/Whale/WHALE-2023/whale-2023.pdf>) - `18.9 MB` - `128` pag. - `acervo-principal`
- [5648ffb8-6efb-48bb-aa5d-270a51b18862por-d75c11ad.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Propulsao-Motores/Referencia-Propulsao/5648ffb8-6efb-48bb-aa5d/5648ffb8-6efb-48bb-aa5d-270a51b18862por-d75c11ad.pdf>) - `18.6 MB` - `216` pag. - `acervo-principal`
- [h-tec-hfc-acqua-catalogo-on-board.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Climatizacao/H-Tec/HFC-Acqua/h-tec-hfc-acqua-catalogo-on-board.pdf>) - `18.5 MB` - `184` pag. - `acervo-principal`
- [analise-para-instalacao-dos-transducers-ga-a573969e.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Campo-Clientes/Referencia-Campo/analise-para-instalacao/analise-para-instalacao-dos-transducers-ga-a573969e.pdf>) - `17.6 MB` - `22` pag. - `acervo-principal`
- [catalogo-inversor-2023-digital.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Energia-DC/Referencia-Energia-DC/inversor-2023-digital/catalogo-inversor-2023-digital.pdf>) - `16.6 MB` - `15` pag. - `acervo-principal`
- [manual-egc-automatic-rev02.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Geradores/Referencia-Geradores/MANUAL-EGC-AUTOMATIC-REV/manual-egc-automatic-rev02.pdf>) - `15.4 MB` - `23` pag. - `acervo-principal`
- [interbus.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Navegacao/Referencia-Navegacao/Interbus/interbus.pdf>) - `14.7 MB` - `274` pag. - `acervo-principal`
- [accessories-catalog.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Propulsao-Motores/Referencia-Propulsao/ACCESSORIES-CATALOG/accessories-catalog.pdf>) - `14.7 MB` - `92` pag. - `acervo-principal`
- [31200346-fevereiro-2-2007.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Propulsao-Motores/Referencia-Propulsao/31200346-FEVEREIRO-2-200/31200346-fevereiro-2-2007.pdf>) - `14.1 MB` - `204` pag. - `acervo-principal`
- [2015-msc-pemm-gustavo-henrique-senna-de-64db7732.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Materiais-Internos/Referencia-Materiais-Interno/Referencias-Tecnicas/2015-msc-pemm-gustavo-henrique-senna-de-64db7732.pdf>) - `13.5 MB` - `129` pag. - `acervo-principal`

## Duplicatas fisicas

- `sha256 5f97f11c68dc` - `3` arquivos
- `90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/Legacy-MDKBK-MDKBN/cummins-onan-mdkbk-mdkbl-mdkbm-mdkbn-operator-manual-981-0181-2008-03.pdf`
- `90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/Legacy-MDKBP-MDKBS/cummins-onan-mdkbp-mdkbr-mdkbs-operator-manual-981-0181-2008-03.pdf`
- `90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/Legacy-MDKBT-MDKBV/cummins-onan-mdkbt-mdkbu-mdkbv-operator-manual-981-0181-2008-03.pdf`
- `sha256 1a505c22df00` - `3` arquivos
- `90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/Legacy-MDKBK-MDKBN/cummins-onan-mdkbk-mdkbl-mdkbm-mdkbn-service-manual-981-0543.pdf`
- `90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/Legacy-MDKBP-MDKBS/cummins-onan-mdkbp-mdkbr-mdkbs-service-manual-981-0543.pdf`
- `90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/Legacy-MDKBT-MDKBV/cummins-onan-mdkbt-mdkbu-mdkbv-service-manual-981-0543.pdf`
- `sha256 54a3d0cea3e2` - `3` arquivos
- `90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDK/cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-operator-manual-a052j727.pdf`
- `90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDL/cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-operator-manual-a052j727.pdf`
- `90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDM-MDKDN/cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-operator-manual-a052j727.pdf`
- `sha256 21b643a8b1b7` - `3` arquivos
- `90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDK/cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-service-manual-a052j731.pdf`
- `90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDL/cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-service-manual-a052j731.pdf`
- `90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDM-MDKDN/cummins-onan-mdkdk-mdkdl-mdkdm-mdkdn-service-manual-a052j731.pdf`
- `sha256 3feca22ec4e2` - `2` arquivos
- `90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDP-MDKDR-MDKDV/cummins-onan-mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv-installation-manual-a046j598.pdf`
- `90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDS-MDKDT-MDKDU/cummins-onan-mdkds-mdkdt-mdkdu-installation-manual-a046j598.pdf`
- `sha256 3e936560c78c` - `2` arquivos
- `90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDP-MDKDR-MDKDV/cummins-onan-mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv-service-manual-a046j602.pdf`
- `90_Revisao_Manual/_Acervo_Local/Geradores/Cummins-Onan/MDKDS-MDKDT-MDKDU/cummins-onan-mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv-service-manual-a046j602.pdf`
- `sha256 25c5a7676eea` - `4` arquivos
- `90_Revisao_Manual/_Acervo_Local/Geradores/Rehlko-Kohler/5EFKOD/rehlko-kohler-5efkod-6ekod-9-11ekozd-7-9efkozd-service-manual-tp-6774-2014-02a.pdf`
- `90_Revisao_Manual/_Acervo_Local/Geradores/Rehlko-Kohler/6EKOD/rehlko-kohler-5efkod-6ekod-9-11ekozd-7-9efkozd-service-manual-tp-6774-2014-02a.pdf`
- `90_Revisao_Manual/_Acervo_Local/Geradores/Rehlko-Kohler/7EFKOZD/rehlko-kohler-5efkod-6ekod-9-11ekozd-7-9efkozd-service-manual-tp-6774-2014-02a.pdf`
- `90_Revisao_Manual/_Acervo_Local/Geradores/Rehlko-Kohler/9-13.5-EKOZD-EFKOZD/rehlko-kohler-5efkod-6ekod-9-11ekozd-7-9efkozd-service-manual-tp-6774-2014-02a.pdf`

## Pendencias de nota companheira

- nenhuma pendencia no acervo principal

## Rotina recomendada

- Rodar esta auditoria sempre que PDF novo entrar no acervo ou staging.
- Rodar `build_pdf_companion_notes.py` depois da auditoria para as notas principais herdarem paginas, qpdf e prioridade de OCR.
- Usar OCR pesado apenas nos itens `alta` e `media`, evitando gastar tempo em duplicata, fora de escopo ou material pessoal.
- Nao compactar ou regravar PDFs originais sem copia reversivel; usar qpdf/Ghostscript primeiro em modo diagnostico.
