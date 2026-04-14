# Eletro Nautica

Vault curada de eletrica nautica com foco em Obsidian, governanca editorial e revisao Brasil-primeiro.

## O que este repositorio contem

- base tecnica em Markdown organizada por dominios;
- MOCs para navegacao no Obsidian;
- frontmatter editorial para SEO e GEO;
- scripts para validar links internos, metadados e referencias sensiveis;
- geracao de manifesto JSON para integracoes futuras.

## Estrutura

- `00_Mapas/` mapas e MOCs da base
- `10_Fundamentos_e_Projeto/` fundamentos, projeto e normas
- `20_Baterias_e_Armazenamento/` bancos, BMS e litio
- `30_Energia_e_Conversao/` shore power, alternador, inversor e geracao
- `40_Distribuicao_Protecao_e_Aterramento/` distribuicao, DR, bonding e aterramento
- `50_` a `80_` dominios aplicados
- `_Editorial/` auditoria, lacunas e governanca editorial
- `scripts/` automacao local e validacoes
- `manifest/` saidas geradas para integracoes

## Validacao local

```powershell
python scripts/validate_vault.py
python scripts/build_manifest.py
```

## O que a validacao verifica

- links `[[wikilinks]]` sem destino;
- ausencia de `title` e `note_type`;
- padroes normativos marcados como obsoletos ou divergentes;
- avisos para notas tecnicas sem data de revisao, jurisdicao ou fontes.

## GitHub Actions

O workflow em `.github/workflows/vault-check.yml` roda a validacao em `push`, `pull_request` e `workflow_dispatch`, depois gera `manifest/content-manifest.json` como artefato.

## Diretriz editorial atual

- Brasil primeiro para enquadramento regulatorio;
- ABYC e ISO como referencia de engenharia;
- fonte primaria obrigatoria em notas normativas e sensiveis;
- datas de revisao explicitas nas notas criticas.
