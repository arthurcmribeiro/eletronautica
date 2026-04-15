# 50 Hz vs 60 Hz

## Objetivo didático

Mostrar que 50 Hz e 60 Hz significam ritmos diferentes de alternancia, com impacto pratico em motores, temporizacao e equipamentos dependentes de frequencia.

## Formato recomendado

- Tipo: `grafico-comparativo`
- Prioridade: `alta`

## Como ler

- No mesmo intervalo de tempo, 60 Hz entrega mais ciclos do que 50 Hz.
- Frequencia errada pode alterar RPM, comportamento de motores e temporizacao de certos equipamentos.
- Transformador ou gerador nao corrigem frequencia sozinhos; isso exige arquitetura especifica.

## Cautelas

- O visual usa uma janela fixa de 100 ms para deixar a diferenca perceptivel. Em projeto real, compatibilidade depende do equipamento, da tensao e da topologia completa da alimentacao.

## Notas sugeridas para embedding

- `10_Fundamentos_e_Projeto/DC vs AC — Corrente Contínua e Alternada.md`
- `30_Energia_e_Conversao/CAIS (Pier) (AC).md`
- `30_Energia_e_Conversao/Gerador (AC).md`

## Arquivos gerados

- `50hz-vs-60hz.svg`
- `50hz-vs-60hz.png`
- `50hz-vs-60hz.md`
