# Radar, AIS e chartplotter: fusao de situacao

## Objetivo didático

Mostrar que cada sensor enxerga uma parte diferente do ambiente e o MFD ajuda a integrar, mas nao substitui julgamento.

## Formato recomendado

- Tipo: `fluxo-de-dados`
- Prioridade: `alta`

## Como ler

- Radar detecta eco, inclusive alvo sem AIS.
- AIS informa dados transmitidos por outra embarcacao.
- GPS localiza a propria embarcacao no sistema.
- MFD integra camadas, alarmes e apresentacao.

## Cautelas

- Fusao de dados depende de calibracao, antenas, rede, configuracao e interpretacao correta pelo operador.

## Notas sugeridas para embedding

- `50_Navegacao_Instrumentacao_e_Comunicacao/Chartplotter - GPS - MFD.md`
- `50_Navegacao_Instrumentacao_e_Comunicacao/Radar.md`
- `50_Navegacao_Instrumentacao_e_Comunicacao/AIS (Automatic Identification System).md`

## Arquivos gerados

- `radar-ais-chartplotter-fusao.svg`
- `radar-ais-chartplotter-fusao.png`
- `radar-ais-chartplotter-fusao.md`
