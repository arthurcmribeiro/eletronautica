# Eletro Nautica

Vault curada de eletrica nautica com foco em Obsidian, governanca editorial e revisao Brasil-primeiro.

## O que este repositorio contem

- base tecnica em Markdown organizada por dominios;
- MOCs para navegacao no Obsidian;
- frontmatter editorial para SEO e GEO;
- scripts para validar links internos, metadados e referencias sensiveis;
- geracao de manifesto JSON para integracoes futuras.
- camada versionavel de visuais didaticos em SVG, PNG e Markdown de apoio.

## Estrutura

- `00_Mapas/` mapas e MOCs da base
- `10_Fundamentos_e_Projeto/` fundamentos, projeto e normas
- `20_Baterias_e_Armazenamento/` bancos, BMS e litio
- `30_Energia_e_Conversao/` shore power, alternador, inversor e geracao
- `40_Distribuicao_Protecao_e_Aterramento/` distribuicao, DR, bonding e aterramento
- `50_` a `80_` dominios aplicados
- `_Editorial/` auditoria, lacunas e governanca editorial
- `_visuals/specs/` especificacoes declarativas dos visuais
- `_visuals/generated/` assets gerados e markdowns de apoio
- `scripts/` automacao local e validacoes
- `scripts/visuals/` pipeline local de geracao visual
- `manifest/` saidas geradas para integracoes

## Validacao local

```powershell
python scripts/validate_vault.py
python scripts/build_manifest.py
python scripts/visuals/render_visuals.py
python scripts/visuals/integrate_visuals.py
```

## O que a validacao verifica

- links `[[wikilinks]]` sem destino;
- ausencia de `title` e `note_type`;
- padroes normativos marcados como obsoletos ou divergentes;
- avisos para notas tecnicas sem data de revisao, jurisdicao ou fontes.

## Camada visual

Os visuais sao definidos em `_visuals/specs/*.json` e gerados localmente por `python scripts/visuals/render_visuals.py`.

Cada spec gera:

- `arquivo.svg` para embedding em notas, GitHub e futura publicacao web;
- `arquivo.png` para reaproveitamento rapido em apostila, slide ou mensageria;
- `arquivo.md` com objetivo didatico, cautelas e notas recomendadas para embedding.

O script `scripts/visuals/integrate_visuals.py` insere blocos de "Visual didatico" nas notas-alvo sem duplicar visuais ja integrados.

## GitHub Actions

O workflow em `.github/workflows/vault-check.yml` roda a validacao em `push`, `pull_request` e `workflow_dispatch`, gera `manifest/content-manifest.json`, renderiza `_visuals/generated/` e publica ambos como artefatos.

## Diretriz editorial atual

- Brasil primeiro para enquadramento regulatorio;
- ABYC e ISO como referencia de engenharia;
- fonte primaria obrigatoria em notas normativas e sensiveis;
- datas de revisao explicitas nas notas criticas.
