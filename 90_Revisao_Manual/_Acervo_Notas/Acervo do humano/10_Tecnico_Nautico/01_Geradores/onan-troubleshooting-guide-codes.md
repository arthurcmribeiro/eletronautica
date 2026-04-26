---
title: "onan troubleshooting guide codes"
note_type: "acervo-companion"
domain: "90_Revisao_Manual"
status: "staging-human-curated"
acervo_origin: "humano-staging"
document_kind: "troubleshooting-guide"
curation_priority: "alta"
curation_stage: "curadoria-humana-parcial"
reviewed_on: "2026-04-26"
review_jurisdiction: "Brasil"
source_file: "01_Geradores/onan-troubleshooting-guide-codes.pdf"
source_sha256: "b69a70cf50514b325d71fbc59fb036b6e30e4a4fc80e51da2820fe8a54ae1aa3"
acervo_bucket: "Geradores"
acervo_system: "Geradores"
acervo_brand: "Cummins / Onan"
acervo_family: "CODES"
extraction_method: "pdftotext"
text_extractable: "sim"
extracted_text_chars: 7454
indexed_text_path: ""
duplicate_status: "unique"
duplicate_group_sha256: ""
duplicate_group_size: 1
duplicate_canonical_source: ""
duplicate_canonical_note: ""
aliases:
  - "onan-troubleshooting-guide-codes.pdf"
  - "onan-troubleshooting-guide-codes.pdf"
related_notes:
  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Indice Gerado"
  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Manifesto de Duplicatas"
  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Fila de Resolucao de Duplicatas"
---

# onan troubleshooting guide codes

> [!abstract] Resumo tecnico
> Nota companheira automatica do staging tecnico humano.
> Ela preserva trilha editorial, busca textual e prepara a futura promocao ao acervo principal.

## Fonte

- arquivo: [onan-troubleshooting-guide-codes.pdf](</C:/Users/User/Desktop/ELETRO NAUTICA OBSIDIAN/ELETRO NAUTICA/90_Revisao_Manual/_Acervo_Local/Acervo do humano/10_Tecnico_Nautico/01_Geradores/onan-troubleshooting-guide-codes.pdf>)
- nome original: `onan-troubleshooting-guide-codes.pdf`
- caminho original: `01_Geradores/onan-troubleshooting-guide-codes.pdf`
- caminho atual: `01_Geradores/onan-troubleshooting-guide-codes.pdf`
- nota companheira: `90_Revisao_Manual/_Acervo_Notas/Acervo do humano/10_Tecnico_Nautico/01_Geradores/onan-troubleshooting-guide-codes.md`
- extensao: `.pdf`
- tamanho do arquivo: `64.3 KB`
- texto extraivel detectado: `sim`
- metodo de extracao: `pdftotext`
- caracteres extraidos: `7454`
- texto integral auxiliar: `n/a`

## Sinais principais

- bucket tecnico: `Geradores`
- sistema-base: `Geradores`
- tipo documental detectado: `troubleshooting-guide`
- marcas detectadas: `Cummins / Onan`
- codigos/modelos detectados: `CODES`
- termos uteis detectados: `air, alternator, battery, control, diagnostic, engine, parts, service`

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
- guia compacto de troubleshooting da Onan centrado em `fault codes`, logica de `status indicator light` e acoes corretivas iniciais.
- o valor deste PDF nao esta em cobertura profunda de uma familia especifica, mas em servir como folha de consulta rapida para leitura de codigo e primeira resposta em campo.
- a propria linguagem mostra que ele nasceu para multiplos contextos, inclusive aplicacoes veiculares e modelos a gasolina/LPG; por isso deve ser usado como apoio, nao como referencia final de familia marinha diesel.

### Aplicacao tecnica / oficina
- ideal para a primeira triagem quando o operador so consegue relatar "pisca X vezes" e o tecnico ainda nao abriu o manual de servico da familia.
- muito util em atendimento remoto ou WhatsApp, porque transforma sequencia de piscadas em proxima acao objetiva.
- serve tambem como base para material de aula sobre diagnostico por codigo, desde que acompanhado do aviso de que o manual especifico da familia sempre prevalece.

### Modelos ou codigos prioritarios
- `fault codes Onan`
- `2 blinks`
- `3 blinks`
- `4 blinks`
- `Code 12`
- `Code 13`
- `Code 14`
- `Code 15`

### Pontos de atencao
- `2 blinks` = baixa pressao de oleo; `3 blinks` = `service fault` com codigo de segundo nivel; `4 blinks` = `overcrank`.
- para ver o codigo de segundo nivel, o proprio guia manda pressionar `STOP` uma vez; para restaurar a piscada depois de alguns minutos, pressionar `STOP` `3` vezes em `5 s`.
- o documento traz boas heuristicas de campo que valem para oficina nautica: manter nivel de oleo, conexoes de bateria limpas e apertadas, nao sobrecarregar o genset e marcar no medidor o ponto em que o tubo de captacao do gerador fica sem combustivel.
- cuidado: ha instrucoes que falam em `vehicle engine`, gasolina e `LPG`. Em gerador marinho diesel, essas partes servem so como analogia de diagnostico e nao como procedimento direto.

### Integracoes e trilha editorial
- bucket de origem: `Geradores`
- sistema-base: `Geradores`
- marca/familia: `Onan / guia transversal de codigos`
- notas relacionadas: `10_Fundamentos_e_Projeto/Troubleshooting - Diagnostico de Falhas Eletricas`, `30_Energia_e_Conversao/Gerador (AC)`, `90_Revisao_Manual/Matriz de Modelos e Versoes - Geradores`
- promocao ao acervo principal: apoio rapido, nao ancora documental unica

### Status de curadoria
- tipo documental detectado: `troubleshooting-guide`
- prioridade editorial: `alta`
- curadoria humana: parcial
- pronto para ensino/SEO: parcial
<!-- CURADORIA-HUMANA:END -->

## Trechos indexaveis

- `Troubleshooting`
- `fault shutdown, the indicator light will repeatedly`
- `blink 2, 3 or 4 blinks at a time.`
- `Hot engine parts can cause severe`
- `burns. Always allow the engine time to cool`
- `before performing any maintenance or service.`
- `• Two blinks indicates a low oil pressure fault.`
- `• Three blinks indicates a service fault. Press`
- `Stop once to cause the two-digit, secondlevel fault code to blink. (Pressing Stop again`
- `will stop the blinking.)The two-digit code consists of 1, 2, 3, 4 or 5 blinks, a brief pause, and`

## Observacoes

- esta nota foi gerada automaticamente a partir do arquivo fisico e ainda pede auditoria humana
- o nome padronizado privilegia rastreabilidade e busca; ajustes finos de semantica podem ser feitos caso a caso
