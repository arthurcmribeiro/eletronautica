---
title: "Bugs conhecidos — infraestrutura de validação"
note_type: "editorial-report"
reviewed_on: "2026-04-16"
---

# Bugs conhecidos — infraestrutura de validação

Lista curta de pontos que precisam ser atacados fora do ciclo de auditoria editorial.

## 1. `validate_vault.py` falha silenciosamente em worktree sob `.claude/`

**Sintoma:** rodar `python scripts/validate_vault.py` dentro de `.claude/worktrees/<branch>/` retorna "Notas analisadas: 0" e sai com exit 0.

**Causa:** a exclusão de pastas faz `any(part in EXCLUDED_PARTS for part in path.parts)` em `path.parts` absolutos. Como o caminho inteiro contém `.claude` como um dos componentes, TUDO é excluído.

**Correção recomendada:** checar partes RELATIVAS a `ROOT` (`path.relative_to(root).parts`), não partes absolutas. Padrão já aplicado em `scripts/standardize_citations.py`.

**Arquivo afetado:** `scripts/vault_tools.py` função `note_files()` (linhas 15–21).

**Impacto:** CI no branch principal funciona porque roda do root do repo; mas qualquer worktree branch criado pela equipe Claude Code para auditoria dá falso-verde. A auditoria de 2026-04-16 pegou isso porque o standardizer apareceu com o mesmo bug e foi corrigido lá.

**Prioridade:** P1 — é mecanismo de silenciamento de falhas em todos os worktrees.

## 2. Parse minimal de YAML não suporta blocos `|` multiline

**Sintoma:** `registro_normas.yaml` usa blocos `|` para observações longas; o parser minimal do standardizer ignora o conteúdo multiline (aceita a chave mas descarta o valor).

**Impacto:** baixo — o campo `observacao` não é usado no processamento de citações.

**Correção:** aceitar blocos `|` se o registro crescer e o campo virar canônico.

## 3. ABYC A-28 no registro_normas.yaml

**Status atual:** `desconhecido` com TODO de verificação externa.

**Ação:** consultar catálogo oficial ABYC (https://abycinc.org/page/Standards) para confirmar se A-28 é "Galvanic Isolators" (minha hipótese inicial sem fonte) ou outro padrão. Atualizar registro.

**Prioridade:** P1 — qualquer citação viva de A-28 depende disso.

## 4. ABNT NBR 13885 e 16033 não verificadas

**Status atual:** `desconhecido` no registro. `validate_vault.py` já sinaliza como padrão sensível.

**Ação:** consulta ao catálogo ABNT para confirmar título, número e status.

**Prioridade:** P2 — não é citada ativamente no vault hoje.

## 5. `standardize_citations.py` injetou TODO dentro de URLs com token "ANATEL"

**Sintoma:** URLs no campo `source_urls` contendo o token `ANATEL` receberam a injeção `(edição a verificar)` no meio do caminho, produzindo URLs quebradas como:

```
https://www.gov.br/ANATEL (edição a verificar)/pt-br/regulado/outorga/servico-movel-maritimo
```

**Causa:** o matcher de normas do standardizer detectou "ANATEL" como nome de autoridade e anexou o TODO sem filtrar contexto — a substituição ocorreu até mesmo quando a string estava dentro de uma URL.

**Alcance:** **13 notas** afetadas, todas no domínio `50_Navegacao_Instrumentacao_e_Comunicacao` (Sonda, Piloto Automático, Radar, VHF, Estação de Vento, MOB, DSC, EPIRB, AIS, Bússola Eletrônica, Buzina, Chartplotter, NMEA 2000).

**Correção aplicada (2026-04-17, R05):** 2 notas fixadas manualmente + 12 via script Python em batch. Todas normalizadas para `https://www.gov.br/anatel/pt-br/regulado/outorga/servico-movel-maritimo` (lowercase, sem TODO inline).

**Correção pendente no script:** `scripts/standardize_citations.py` precisa de lookbehind regex `(?<!://)(?<!www\.)` — ou, melhor, aplicar a substituição somente fora de spans de URL (detectados por regex prévio `https?://\S+`). Como o script já rodou e foi neutralizado após R01, esta é uma salvaguarda para reativação futura.

**Prioridade:** P2 histórico, P1 se o script for reativado.
