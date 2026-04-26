---
title: "cummins-onan - mdkad-mdkae-mdkaf - service-manual - legacy-espelho"
note_type: "acervo-companion"
domain: "90_Revisao_Manual"
status: "staging-human-curated"
acervo_origin: "humano-staging"
document_kind: "service-manual"
curation_priority: "alta"
curation_stage: "curadoria-humana-parcial"
reviewed_on: "2026-04-26"
review_jurisdiction: "Brasil"
source_file: "01_Geradores/cummins-onan__mdkad-mdkae-mdkaf__service-manual__legacy-espelho.pdf"
source_sha256: "437245942da150426c095a0fd90cd1889b3cbbb359470a7c8b06a5547ebdae29"
acervo_bucket: "Geradores"
acervo_system: "Geradores"
acervo_brand: "Cummins / Onan"
acervo_family: "MDKAE"
extraction_method: "pdftotext"
text_extractable: "sim"
extracted_text_chars: 688
indexed_text_path: ""
duplicate_status: "unique"
duplicate_group_sha256: ""
duplicate_group_size: 1
duplicate_canonical_source: ""
duplicate_canonical_note: ""
aliases:
  - "cummins-onan__mdkad-mdkae-mdkaf__service-manual__legacy-espelho.pdf"
  - "cummins-onan__mdkad-mdkae-mdkaf__service-manual__legacy-espelho.pdf"
related_notes:
  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Indice Gerado"
  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Manifesto de Duplicatas"
  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Fila de Resolucao de Duplicatas"
---

# cummins-onan - mdkad-mdkae-mdkaf - service-manual - legacy-espelho

> [!abstract] Resumo tecnico
> Nota companheira automatica do staging tecnico humano.
> Ela preserva trilha editorial, busca textual e prepara a futura promocao ao acervo principal.

## Fonte

- arquivo: [cummins-onan__mdkad-mdkae-mdkaf__service-manual__legacy-espelho.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Acervo do humano/10_Tecnico_Nautico/01_Geradores/cummins-onan__mdkad-mdkae-mdkaf__service-manual__legacy-espelho.pdf>)
- nome original: `cummins-onan__mdkad-mdkae-mdkaf__service-manual__legacy-espelho.pdf`
- caminho original: `01_Geradores/cummins-onan__mdkad-mdkae-mdkaf__service-manual__legacy-espelho.pdf`
- caminho atual: `01_Geradores/cummins-onan__mdkad-mdkae-mdkaf__service-manual__legacy-espelho.pdf`
- nota companheira: `90_Revisao_Manual/_Acervo_Notas/Acervo do humano/10_Tecnico_Nautico/01_Geradores/cummins-onan__mdkad-mdkae-mdkaf__service-manual__legacy-espelho.md`
- extensao: `.pdf`
- tamanho do arquivo: `1.7 MB`
- texto extraivel detectado: `sim`
- metodo de extracao: `pdftotext`
- caracteres extraidos: `688`
- texto integral auxiliar: `n/a`

## Sinais principais

- bucket tecnico: `Geradores`
- sistema-base: `Geradores`
- tipo documental detectado: `service-manual`
- marcas detectadas: `Cummins / Onan`
- codigos/modelos detectados: `MDKAE, MDKAD, MDKAF`
- termos uteis detectados: `engine, manual, service`

## Uso sugerido

- usar esta nota para localizar o arquivo sem depender do nome bruto original
- confirmar se o item deve ficar no staging, ser promovido ao acervo principal ou ir para trilha complementar
- revisar manualmente os modelos/codigos antes de transformar o conteudo em resumo definitivo

## Governanca de duplicatas

- status no lote: `unique`
- este arquivo ficou fisicamente unico no staging desta rodada
- manifesto geral: [Acervo Humano Tecnico - Manifesto de Duplicatas.md](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Manifesto de Duplicatas.md>)
- fila de resolucao: [Acervo Humano Tecnico - Fila de Resolucao de Duplicatas.md](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Fila de Resolucao de Duplicatas.md>)

<!-- CURADORIA-HUMANA:START -->
## Curadoria humana

### Resumo humano
- manual de servico de bancada para `Cummins Onan MDKAD, MDKAE e MDKAF`, com foco em `engine controls`, regulacao de tensao, troubleshooting de geracao, arrefecimento, exaustao e esquemas `12 VDC` e `24 VDC`.
- a estrutura e mais eletromecanica que "eletronica de display": o valor forte deste PDF esta em entender a logica de relays, breakers de falha e sensores do conjunto, sem depender de tentativa e erro a bordo.
- o manual deixa claro que informacao de modulo eletronico e limitada e que, em campo, costuma ser mais eficiente substituir placas do que tentar reparo em nivel de componente.

### Aplicacao tecnica / oficina
- usar como manual-base quando o defeito mistura `nao parte`, `parte e cai`, `sem AC`, `falha de combustivel`, `falha de arrefecimento` e suspeita de desligamento por protecao.
- e especialmente util para rastrear a cadeia de comando do genset: `S1 Start-Stop/Preheat`, `K1/K2/K3`, `K5 glow plug`, `K7 fuel shutoff`, `E5 fuel pump`, `AVR1`, `CB1`, `CB2`, `CB4` e `CB5`.
- em oficina, este PDF ajuda muito quando o operador descreve sintoma "ele gira mas nao segura" ou "gera mas cai com aquecimento", porque a documentacao separa bem controle, bomba de combustivel, regulador e falhas de sensores.

### Modelos ou codigos prioritarios
- `MDKAE`
- `MDKAD`
- `MDKAF`

### Mapa de uso rapido
- `Secao 2`: arquitetura do controle, relays, breakers de falha, regulador e sensores de protecao.
- `Secao 3`: servico do controle do motor e `fuel pump test`.
- `Secao 4 a 6`: gerador, regulador de tensao, troubleshooting e testes do conjunto gerador.
- `Secao 8`: sistema de arrefecimento, pontos de drenagem e componentes do circuito.
- `Secao 9`: diagramas e esquemas `12/24 VDC`, essenciais para campo e retrofit.

### Pontos de atencao
- o proprio manual diferencia `Spec A` de `MDKAD/MDKAE` e configuracoes posteriores, alem de trazer figura separada para `MDKAF`; confirmar sempre a `Spec letter` antes de seguir circuito ou disposicao fisica.
- `S1` energiza glow plugs e roda a bomba de combustivel quando mantido em `Stop`, ou seja, esta familia usa a propria chave de parada como `preheat/prime`; isso precisa entrar no ritual de diagnostico.
- `CB2` e `CB5` sao protecoes criticas de falha; muita gente procura "fault code digital" quando, nesta familia, o caminho rapido e verificar breaker de falha, sensores e alimentacoes do controle.
- o manual e forte em seguranca nautica: CO, tensao de gerador, exaustao quente, combustivel, `coolant` sob pressao e risco de curto em ambiente umido.

### Integracoes e trilha editorial
- bucket de origem: `Geradores`
- sistema-base: `Geradores`
- marca/familia: `Cummins-Onan / MDKAD-MDKAE-MDKAF`
- notas relacionadas: `30_Energia_e_Conversao/Gerador (AC)`, `10_Fundamentos_e_Projeto/Troubleshooting - Diagnostico de Falhas Eletricas`, `40_Distribuicao_Protecao_e_Aterramento/Aterramento`, `80_Seguranca_e_Corrosao/Detector de CO - Monoxido de Carbono`, `90_Revisao_Manual/Matriz de Modelos e Versoes - Geradores`
- promocao ao acervo principal: candidato forte se vier acompanhado do operator manual da mesma familia

### Status de curadoria
- tipo documental detectado: `service-manual`
- prioridade editorial: `alta`
- curadoria humana: parcial
- pronto para ensino/SEO: parcial
<!-- CURADORIA-HUMANA:END -->

## Trechos indexaveis

- `Caution: This document contains mixed page sizes (8.5 x 11 or 11 x`
- `17), which may affect printing. Please adjust your printer settings`
- `according to the size of each page you wishRedistribution`
- `or publication of this document`
- `by any means, is strictly prohibited.`
- `Service Manual`
- `MDKAD, MDKAE, MDKAF`
- `Printed in U.S.A.`
- `Redistribution or publication of this document`
- `Proposition 65 Warning`

## Observacoes

- esta nota foi gerada automaticamente a partir do arquivo fisico e ainda pede auditoria humana
- o nome padronizado privilegia rastreabilidade e busca; ajustes finos de semantica podem ser feitos caso a caso
