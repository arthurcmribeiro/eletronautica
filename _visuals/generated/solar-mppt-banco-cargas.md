# Solar DC: painel, MPPT, banco e cargas

## Objetivo didático

Mostrar que painel solar nao alimenta o barco sozinho; ele passa por controlador, banco e estrategia de consumo.

## Formato recomendado

- Tipo: `fluxo-de-energia`
- Prioridade: `alta`

## Como ler

- O controlador MPPT adapta energia do painel para carregar o banco.
- O banco absorve variacao de sol, sombra e consumo.
- Cargas AC via inversor aumentam demanda sobre o banco.
- Dimensionamento precisa considerar consumo diario e geracao real.

## Cautelas

- Geracao solar real depende de area, orientacao, sombra, temperatura, eficiencia e perfil de uso.

## Notas sugeridas para embedding

- `30_Energia_e_Conversao/Placa Solar (DC).md`
- `20_Baterias_e_Armazenamento/Carregador de Bateria (AC To DC).md`

## Arquivos gerados

- `solar-mppt-banco-cargas.svg`
- `solar-mppt-banco-cargas.png`
- `solar-mppt-banco-cargas.md`
