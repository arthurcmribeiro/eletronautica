# Monitor de bateria: shunt e calculo de SoC

## Objetivo didático

Mostrar por que shunt mede corrente real e entrega SoC melhor que voltimetro isolado.

## Formato recomendado

- Tipo: `fluxo-de-medicao`
- Prioridade: `alta`

## Como ler

- Toda corrente do banco deve passar pelo shunt.
- O monitor integra entrada e saida de Ah.
- Tensao sozinha nao mostra bem SoC, especialmente em LiFePO4.
- Instalacao errada faz o monitor mentir com precisao.

## Cautelas

- A posicao do shunt, referencia negativa e configuracao de capacidade/eficiencia devem seguir o fabricante.

## Notas sugeridas para embedding

- `20_Baterias_e_Armazenamento/Monitor de Bateria - BMV - Shunt.md`
- `20_Baterias_e_Armazenamento/Bancos de Bateria.md`

## Arquivos gerados

- `monitor-bateria-shunt-fluxo.svg`
- `monitor-bateria-shunt-fluxo.png`
- `monitor-bateria-shunt-fluxo.md`
