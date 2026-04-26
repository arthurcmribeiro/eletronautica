---
title: "Painel de Curadoria do Acervo"
note_type: "dashboard"
domain: "90_Revisao_Manual"
status: "auto-generated"
reviewed_on: "2026-04-26"
review_jurisdiction: "Brasil"
related_notes:
  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Local - Indice Gerado"
  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Notas - Indice Gerado"
  - "Auditoria Operacional PDF - Toolchain"
  - "OCR Controlado - Acervo Principal"
---

# Painel de Curadoria do Acervo

> [!abstract] Resumo tecnico
> Painel gerado automaticamente para separar acervo principal, staging tecnico, fora de escopo, OCR pendente e fila de curadoria das notas companheiras.

## Saude operacional

- pipeline: `ok`
- ultima execucao: `2026-04-26T08:59:20.270227+00:00`
- PDFs auditados: `678`
- tamanho auditado: `2.8 GB`
- paginas conhecidas: `33305`
- qpdf ok/warning: `420` / `258`
- texto pesquisavel sim/nao: `639` / `39`
- notas companheiras: `545`
- notas com curadoria assistida: `21`
- notas enriquecidas nesta rodada: `0`

## Separacao humano vs tecnico

- tecnico operacional: `478` PDFs (`acervo-principal` + `humano-staging-tecnico`).
- fora de escopo/pessoal: `176` PDFs.
- duplicatas arquivadas: `24` PDFs.

| Bucket                     | PDFs |
| -------------------------- | ---- |
| acervo-principal           | 248  |
| humano-arquivado-duplicata | 24   |
| humano-fora-do-escopo      | 176  |
| humano-staging-tecnico     | 230  |

## OCR

- OCR executado nesta base: `10` registros.
- OCR pendente por auditoria: `33` PDFs (`alta`, `media` ou `baixa`).

| Status    | Arquivos |
| --------- | -------- |
| completed | 6        |
| partial   | 4        |

## Fila de curadoria tecnica

Prioridade calculada por sistema, tipo documental, OCR, texto pesquisavel, paginas, `qpdf` e prioridade editorial.

| Score | Nota                                                                                                                                                                             | PDF                                                                                                 | Motivo                                                                         |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| 122   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Cummins-Onan/MDKBH/cummins-onan__mdkbh__service-manual__legacy-espelho|nota]]                                                        | cummins-onan__mdkbh__service-manual__legacy-espelho.pdf                                             | sistema Geradores; tipo service-manual; prioridade editorial alta              |
| 122   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Cummins-Onan/MDKDK/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__service-manual__legacy-espelho|nota]]                                      | cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__service-manual__legacy-espelho.pdf                           | sistema Geradores; tipo service-manual; prioridade editorial alta              |
| 122   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Cummins-Onan/MDKDL/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__service-manual__legacy-espelho|nota]]                                      | cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__service-manual__legacy-espelho.pdf                           | sistema Geradores; tipo service-manual; prioridade editorial alta              |
| 122   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Cummins-Onan/MDKDM-MDKDN/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__service-manual__legacy-espelho|nota]]                                | cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__service-manual__legacy-espelho.pdf                           | sistema Geradores; tipo service-manual; prioridade editorial alta              |
| 122   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Cummins-Onan/MDKDP-MDKDR-MDKDV/cummins-onan__mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv__service-manual__a046j602|nota]]                    | cummins-onan__mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv__service-manual__a046j602.pdf                     | sistema Geradores; tipo service-manual; prioridade editorial alta              |
| 122   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Cummins-Onan/MDKDS-MDKDT-MDKDU/cummins-onan__mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv__service-manual__a046j602|nota]]                    | cummins-onan__mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv__service-manual__a046j602.pdf                     | sistema Geradores; tipo service-manual; prioridade editorial alta              |
| 117   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Rehlko-Kohler/5EFKOD/rehlko-kohler__5efkod-6ekod-9-11ekozd-7-9efkozd__service-manual__tp-6774-2014-02a|nota]]                        | rehlko-kohler__5efkod-6ekod-9-11ekozd-7-9efkozd__service-manual__tp-6774-2014-02a.pdf               | sistema Geradores; tipo service-manual; prioridade editorial alta              |
| 117   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Rehlko-Kohler/6EKOD/rehlko-kohler__5efkod-6ekod-9-11ekozd-7-9efkozd__service-manual__tp-6774-2014-02a|nota]]                         | rehlko-kohler__5efkod-6ekod-9-11ekozd-7-9efkozd__service-manual__tp-6774-2014-02a.pdf               | sistema Geradores; tipo service-manual; prioridade editorial alta              |
| 117   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Rehlko-Kohler/7EFKOZD/rehlko-kohler__5efkod-6ekod-9-11ekozd-7-9efkozd__service-manual__tp-6774-2014-02a|nota]]                       | rehlko-kohler__5efkod-6ekod-9-11ekozd-7-9efkozd__service-manual__tp-6774-2014-02a.pdf               | sistema Geradores; tipo service-manual; prioridade editorial alta              |
| 117   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Rehlko-Kohler/9-13.5-EKOZD-EFKOZD/rehlko-kohler__5efkod-6ekod-9-11ekozd-7-9efkozd__service-manual__tp-6774-2014-02a|nota]]           | rehlko-kohler__5efkod-6ekod-9-11ekozd-7-9efkozd__service-manual__tp-6774-2014-02a.pdf               | sistema Geradores; tipo service-manual; prioridade editorial alta              |
| 116   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Cummins-Onan/Legacy-MDKBK-MDKBN/cummins-onan__mdkbk-mdkbl-mdkbm-mdkbn__service-manual__legacy-espelho|nota]]                         | cummins-onan__mdkbk-mdkbl-mdkbm-mdkbn__service-manual__legacy-espelho.pdf                           | sistema Geradores; tipo service-manual; prioridade editorial alta              |
| 116   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Cummins-Onan/Legacy-MDKBP-MDKBS/cummins-onan__mdkbp-mdkbr-mdkbs__service-manual__legacy-espelho|nota]]                               | cummins-onan__mdkbp-mdkbr-mdkbs__service-manual__legacy-espelho.pdf                                 | sistema Geradores; tipo service-manual; prioridade editorial alta              |
| 116   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Cummins-Onan/Legacy-MDKBT-MDKBV/cummins-onan__mdkbt-mdkbu-mdkbv__service-manual__legacy-espelho|nota]]                               | cummins-onan__mdkbt-mdkbu-mdkbv__service-manual__legacy-espelho.pdf                                 | sistema Geradores; tipo service-manual; prioridade editorial alta              |
| 116   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Cummins-Onan/MDKAD-MDKAE-MDKAF/cummins-onan__mdkad-mdkae-mdkaf__service-manual__legacy-espelho|nota]]                                | cummins-onan__mdkad-mdkae-mdkaf__service-manual__legacy-espelho.pdf                                 | sistema Geradores; tipo service-manual; prioridade editorial alta              |
| 108   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Cummins-Onan/MDKDP-MDKDR-MDKDV/cummins-onan__mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv__installation-manual__a046j598|nota]]               | cummins-onan__mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv__installation-manual__a046j598.pdf                | sistema Geradores; tipo installation-manual; prioridade editorial alta         |
| 108   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Cummins-Onan/MDKDS-MDKDT-MDKDU/cummins-onan__mdkds-mdkdt-mdkdu__installation-manual__a046j598|nota]]                                 | cummins-onan__mdkds-mdkdt-mdkdu__installation-manual__a046j598.pdf                                  | sistema Geradores; tipo installation-manual; prioridade editorial alta         |
| 105   | [[90_Revisao_Manual/_Acervo_Notas/Bombas-Utilidades/Referencia-Bombas-Utilidades/91095466-mini-pressuriza/referencia-bomba__91095466-mini-pressu__techref__h-b6d3ca86776f|nota]] | referencia-bomba__91095466-mini-pressu__techref__h-b6d3ca86776f.pdf                                 | sistema Bombas-Utilidades; tipo technical-reference; prioridade editorial alta |
| 105   | [[90_Revisao_Manual/_Acervo_Notas/Bombas-Utilidades/Whale/WHALE-2023/whale__whale-2023__techref__h-b0b5ae3b5e45|nota]]                                                           | whale__whale-2023__techref__h-b0b5ae3b5e45.pdf                                                      | sistema Bombas-Utilidades; tipo technical-reference; prioridade editorial alta |
| 105   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Cummins-Onan/Geral/cummins-onan__geral__service__h-a3ae73c9a3ef|nota]]                                                               | cummins-onan__geral__service__h-a3ae73c9a3ef.pdf                                                    | sistema Geradores; tipo technical-reference; prioridade editorial alta         |
| 105   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Cummins-Onan/MDKAD-MDKAE-MDKAF/cummins-onan__mdkad-mdkae-mdkaf__operator-manual__981-0140-1996-02|nota]]                             | cummins-onan__mdkad-mdkae-mdkaf__operator-manual__981-0140-1996-02.pdf                              | sistema Geradores; tipo operation-manual; prioridade editorial alta            |
| 105   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Cummins-Onan/MDKDK/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__operator-manual__a052j727|nota]]                                           | cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__operator-manual__a052j727.pdf                                | sistema Geradores; tipo operation-manual; prioridade editorial alta            |
| 105   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Cummins-Onan/MDKDL/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__operator-manual__a052j727|nota]]                                           | cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__operator-manual__a052j727.pdf                                | sistema Geradores; tipo operation-manual; prioridade editorial alta            |
| 105   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Cummins-Onan/MDKDM-MDKDN/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__operator-manual__a052j727|nota]]                                     | cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__operator-manual__a052j727.pdf                                | sistema Geradores; tipo operation-manual; prioridade editorial alta            |
| 105   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Referencia-Geradores/SERVICE-MANUAL/referencia-gerad__service-manual__service__h-6ee62475cc8c|nota]]                                 | referencia-gerad__service-manual__service__h-6ee62475cc8c.pdf                                       | sistema Geradores; tipo service-manual; prioridade editorial alta              |
| 102   | [[90_Revisao_Manual/_Acervo_Notas/Shore-Power-AC/Referencia-Shore-Power/licenca-uso-exclusivo-pa/referencia-shore__licenca-uso-exclusiv__techref__h-610e30c82eec|nota]]          | referencia-shore__licenca-uso-exclusiv__techref__h-610e30c82eec.pdf                                 | sistema Shore-Power-AC; tipo technical-reference; prioridade editorial alta    |
| 101   | [[90_Revisao_Manual/_Acervo_Notas/Climatizacao/Dometic/Self-Contained/dometic-cruisair__self-contained-air-conditioner__installation-manual__dx-remote-legacy-espelho|nota]]     | dometic-cruisair__self-contained-air-conditioner__installation-manual__dx-remote-legacy-espelho.pdf | sistema Climatizacao; tipo installation-manual; prioridade editorial alta      |
| 101   | [[90_Revisao_Manual/_Acervo_Notas/Navegacao/Referencia-Navegacao/Interbus/referencia-naveg__interbus__techref__h-03d72ce8f84e|nota]]                                             | referencia-naveg__interbus__techref__h-03d72ce8f84e.pdf                                             | sistema Navegacao; tipo technical-reference; prioridade editorial alta         |
| 100   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Fischer-Panda/Geral/fischer-panda__geral__operation__h-41fb6a309ac3|nota]]                                                           | fischer-panda__geral__operation__h-41fb6a309ac3.pdf                                                 | sistema Geradores; tipo technical-reference; prioridade editorial alta         |
| 100   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Fischer-Panda/PANDA-4200-4500ECO-R01/fischer-panda__panda-4200-4500eco-r__techref__h-6cdfb70a12f6|nota]]                             | fischer-panda__panda-4200-4500eco-r__techref__h-6cdfb70a12f6.pdf                                    | sistema Geradores; tipo technical-reference; prioridade editorial alta         |
| 100   | [[90_Revisao_Manual/_Acervo_Notas/Geradores/Fischer-Panda/PANDA-4K-5K-7K-MANUAL/fischer-panda__panda-4k-5k-7k-manua__techref__h-01fb383084e6|nota]]                              | fischer-panda__panda-4k-5k-7k-manua__techref__h-01fb383084e6.pdf                                    | sistema Geradores; tipo technical-reference; prioridade editorial alta         |

## Possiveis tecnicos no fora de escopo

Fila conservadora: nao move arquivo automaticamente, apenas aponta nomes com sinais tecnicos para revisao humana.

| Caminho                                                                                                                   | Sinais       |
| ------------------------------------------------------------------------------------------------------------------------- | ------------ |
| 90_Revisao_Manual/_Acervo_Local/Acervo do humano/00_Fora_do_Escopo_ou_Pessoal/DOCUMENTO MOTOR PORTUGAL ARTHUR.pdf         | motor        |
| 90_Revisao_Manual/_Acervo_Local/Acervo do humano/00_Fora_do_Escopo_ou_Pessoal/fap55_installation_and_set_up__3-12-91.pdf  | installation |
| 90_Revisao_Manual/_Acervo_Local/Acervo do humano/00_Fora_do_Escopo_ou_Pessoal/Ocean Engineering, Ph_D_ - Florida Tech.pdf | engine       |

## Rotina para PDF novo

```powershell
python scripts/acervo/run_pdf_pipeline.py
```

A pipeline atualiza auditoria, OCR prioritario, notas companheiras, este painel, validacao e manifesto.
