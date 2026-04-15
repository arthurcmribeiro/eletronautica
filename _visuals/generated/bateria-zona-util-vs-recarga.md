# Bateria: zona util vs recarga

## Objetivo didático

Ajudar iniciantes a interpretar tensao em repouso como faixa de conforto, atencao e necessidade de recarga, sem confundir isso com SoC preciso ou regra valida durante carga e descarga.

## Formato recomendado

- Tipo: `faixa-operacional`
- Prioridade: `alta`

## Como ler

- Use a tensao em repouso como triagem rapida, nao como medidor preciso de SoC.
- Durante carga ou descarga, a tensao fica distorcida pela condicao instantanea do sistema.
- Em LiFePO4, um voltimetro simples nao substitui monitor com shunt.

## Cautelas

- Os valores sao tipicos para chumbo-acido 12 V em repouso e servem como analogia didatica. Temperatura, quimica, envelhecimento e historico de carga alteram a leitura. Para LiFePO4, a curva de tensao e plana demais para esse uso.

## Notas sugeridas para embedding

- `20_Baterias_e_Armazenamento/Tipos de Bateria.md`
- `20_Baterias_e_Armazenamento/Monitor de Bateria - BMV - Shunt.md`
- `10_Fundamentos_e_Projeto/Voltímetro - Amperímetro (DC e AC).md`

## Arquivos gerados

- `bateria-zona-util-vs-recarga.svg`
- `bateria-zona-util-vs-recarga.png`
- `bateria-zona-util-vs-recarga.md`
