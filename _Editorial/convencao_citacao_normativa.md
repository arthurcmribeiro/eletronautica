---
title: Convenção de Citação Normativa
note_type: editorial-policy
reviewed_on: 2026-04-16
review_jurisdiction: [Brasil, internacional]
source_urls: []
---

# Convenção de Citação Normativa — Eletronautica Vault

## Por que esta política existe

Na auditoria Fase 0 (2026-04-16), identificou-se que **95% das citações normativas** no vault não indicavam edição, ano ou cláusula — citavam apenas a sigla (ex.: "ABYC E-11", "ISO 13297"). Isso cria três riscos operacionais:

1. **Desatualização silenciosa:** ISO 10133 foi retirada e continuou sendo citada como ativa em 3 notas derivadas porque não havia ancoragem de edição/ano.
2. **Responsabilidade legal:** o vault é público e voltado a eletricistas de campo. Citação imprecisa vira recomendação imprecisa e pode resultar em instalação insegura.
3. **Não rastreabilidade:** sem cláusula/item, o leitor (aluno, mentee, auditor) não consegue verificar a origem da prescrição.

Esta convenção corrige esse padrão e se torna obrigatória para novas notas a partir de 2026-04-16. Notas legadas são corrigidas durante as auditorias Fase 1–4.

## Formato canônico

```
<ORGANISMO> <CÓDIGO> (<EDIÇÃO/ANO>), <CLÁUSULA>
```

### Exemplos corretos

```
ABYC E-11 (2023), §11.4.1.2
ISO 13297:2020, cláusula 5.3.2
NORMAM-211/DPC (2022), item 0207
IEC 60092-201 (2019), seção 5
ABNT NBR 5410 (2004, Emenda 1:2008), item 6.3.4
```

### Exemplos incorretos (NÃO usar)

```
❌  ABYC E-11                  (sem edição)
❌  "a norma ABYC diz..."       (sem sigla ou código)
❌  ISO 13297 cap. 5           (faltando edição e usando "cap." em vez de "cláusula")
❌  ISO 10133                   (norma aposentada; ver registro_normas.yaml)
```

## Quando a edição/cláusula ainda não é conhecida

Se você está capturando conhecimento em rascunho e **ainda** não tem acesso ao texto oficial:

1. Use o placeholder explícito: `ABYC E-11 (edição a verificar)`.
2. Adicione `TODO-CITAÇÃO` como tag na linha.
3. A nota **não sai de rascunho** até a citação estar completa.

Exemplo:

```
- **ABYC E-11 (edição a verificar)** — define bitolamento AC/DC. <!-- TODO-CITAÇÃO -->
```

## Regras de interação com o Registro Central

O arquivo `_Editorial/registro_normas.yaml` é a **fonte única de verdade**. Antes de citar qualquer norma:

1. Abrir o registro e verificar o campo `status`.
2. Se `status: substituida` ou `aposentada` → **não citar como viva**. Usar apenas em contexto histórico explícito.
3. Se `status: desconhecido` → auditar publicação oficial antes da primeira citação viva; atualizar o registro.
4. Se `status: vigente` → citar com edição conforme o campo `edicao_vigente` do registro.

Após citar, adicionar a nota ao campo `citada_em` da norma no registro, e atualizar `ultima_verificacao` da norma para a data.

## Lista de bloqueio (referências retiradas/substituídas)

| Norma | Status | Ação exigida |
|-------|--------|--------------|
| ISO 10133 | substituída por ISO 13297:2020 | Não citar como viva. Citação histórica só na nota mestre [[Normas e Regulamentações — Abyc Iso e Brasil]]. |
| NORMAM-02 (esporte/recreio) | substituída por NORMAM-211/DPC | Não citar. Exceção única: nota mestre de normas. |
| ABYC TE-13 | renomeada para ABYC E-13 (2022) | Usar ABYC E-13 (2022). |
| ABNT NBR 13885 | status desconhecido | Auditar antes de primeira citação. |
| ABNT NBR 16033 | status desconhecido | Auditar antes de primeira citação. |

Estas referências já são sinalizadas pelo `scripts/validate_vault.py` (padrões sensíveis). A validação no CI gera **warning**; meta é converter para **error** após as Fases 1–2 zerarem o backlog.

## Relação com o frontmatter

Notas de tipo `reference`, `technical-note`, `procedure` ou `system` devem ter:

```yaml
review_jurisdiction: [Brasil, internacional]   # ou apenas uma
source_urls: [https://... , https://...]       # pelo menos 1
reviewed_on: YYYY-MM-DD                        # data da última verificação normativa
normas_citadas:                                # NOVO CAMPO — proposto
  - "ABYC E-11 (2023)"
  - "ISO 13297:2020"
  - "NORMAM-211/DPC (2022)"
```

O campo `normas_citadas` torna a validação cruzada com `registro_normas.yaml` trivial em CI.

## Responsabilidade legal e limites de uso

Cita-se norma para **fundamentar**, não para **substituir**:

- O vault não substitui projeto assinado por profissional habilitado.
- Recomendações de dimensionamento e proteção devem explicitar que dependem de verificação in loco.
- Reprodução literal de norma paga (ABNT NBR, IEC) é proibida. **Parafrasear** e citar a cláusula.
- Para normas abertas (ABYC é parcialmente aberta, ISO via preview, DPC/NORMAM é pública), preferir link direto em `source_urls`.

## Histórico

| Data | Mudança |
|------|---------|
| 2026-04-16 | Criação. Política entra em vigor. |
| 2026-04-16 | Correção em Bonding, Bancos de Bateria, Tipos de Bateria (remoção de citação ativa de ISO 10133). |
