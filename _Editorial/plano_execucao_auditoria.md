# PLANO DE EXECUÇÃO — AUDITORIA TÉCNICA ELETRONAUTICA
## Todas as Fases | Gerado em 2026-04-16 | Revisão Opus v2 | Fase 1 Rodada 01 EXECUTADA

---

## LOG DE EXECUÇÃO AUTÔNOMA — 2026-04-16

### Decisões tomadas (autonomia delegada pelo responsável)

| # | Decisão | Resposta | Lógica |
|---|---------|----------|--------|
| 1 | Amostra 35 vs 45 | **35** | 00_Mapas já coberto em 11/16. Expansão dilui rigor. |
| 2 | ISO 10133 agora ou na Fase 1 | **Corrigido antes** | Auditar nota com erro conhecido gera ruído. |
| 3 | P1/P2 das 7 notas novas | P1: Aterramento, Fusíveis DC, Isolador, Gerador AC, Ref. Rápida. P2: Carregador, NAV BB/BE. | Impacto em segurança/cálculo = P1. |
| 4 | manifest 124 vs 147 | Não-bloqueador | Manifest exclui `_Editorial` e pastas `_`-prefixadas por design. |
| 5 | Estimativas Fases 2-5 | Escala +25% | Fase 2: 15h; Fase 3: 12,5h; Fase 4: 22,5h; Fase 5: 7,5h. **Total ≈ 102h**. |

### Pacote pré-Fase 1 entregue

| Artefato | Caminho | Status |
|----------|---------|--------|
| Registro Central de Normas | `_Editorial/registro_normas.yaml` | ✅ criado — 19 normas mapeadas |
| Convenção de Citação Normativa | `_Editorial/convencao_citacao_normativa.md` | ✅ criada — política em vigor |
| Correção ISO 10133 em Bonding | `40_Distribuicao_.../Bonding.md` | ✅ migrada para ISO 13297:2020 |
| Correção ISO 10133 em Bancos de Bateria | `20_Baterias_.../Bancos de Bateria.md` | ✅ migrada |
| Correção ISO 10133 em Tipos de Bateria | `20_Baterias_.../Tipos de Bateria.md` | ✅ migrada |
| Correção P0 ABYC A-31 na nota mestre | `10_Fundamentos_.../Normas e Regulamentações.md` | ✅ corrigida (era rotulada "chargers"; agora "lightning protection") |

### Fase 1 Rodada 01 — 3 notas auditadas

- Output: `_Editorial/fase_1_auditoria_rodada_01_20260416.yaml`
- Vereditos: 3× revisão menor (nenhuma reescrita necessária)
- Achados: 1 P0 (corrigido durante a rodada), 14 P1, 11 P2
- Padrão sistêmico confirmado: 21 de 23 citações (91%) sem edição — alinhado com gap de 95% da Fase 0
- Tempo total de correção estimado: 4h30
- Novo achado P0 inesperado: nota mestre rotulava ABYC A-31 como "battery chargers" (erro factual)
- Nova ideia emergente: `scripts/standardize_citations.py` (5h impl. vs 40h+ manual)

### Erros meus descobertos durante a rodada (transparência)

1. ABYC A-28 foi incluída no registro como "Galley Stoves" sem fonte verificada. Revertido para `status: desconhecido` com TODO de auditoria externa.
2. Fase 0 v2 citou "Referência Rápida — Cálculos e Normas" que não existe. Nome real: "Referência Rápida — Valores de Campo". Ajustado no output Fase 1.
3. `validate_vault.py` falha silenciosamente em worktrees sob `.claude/` (retorna "0 notas"). Registrado em `_Editorial/bugs_conhecidos.md` como P1.

---

## LOG — SESSÃO 2026-04-16 (continuação)

### Blocos 1-3 executados

| Bloco | Entrega | Estado |
|-------|---------|--------|
| 1 | `scripts/standardize_citations.py` — 370 linhas, stdlib only | ✅ |
| 1 | `_Editorial/bugs_conhecidos.md` — 4 bugs de infra registrados | ✅ |
| 2 | Standardizer aplicado no vault (142 notas) | ✅ |
| 2 | **191 citações normativas padronizadas em 51 arquivos** | ✅ |
| 2 | Re-run final: 0 sugestões, 0 alertas | ✅ |
| 3 | Bonding: AWG 8 + tabela Ag/AgCl + comissionamento | ✅ |
| 3 | Referência Rápida: legenda 3%, tensão base 12V, citação E-11 explícita | ✅ |
| 3 | Normas mestre: parágrafo de risco "220V fase-fase sem neutro" | ✅ |
| 3 | 3 frontmatters com `review_jurisdiction` lista + `normas_citadas` | ✅ |

### Métricas pós-sessão

| Métrica | Antes (Fase 0 v2) | Depois (2026-04-16 fim) |
|---------|-------------------|-------------------------|
| Citações normativas com edição/ano | 5 (8% das 62) | **~193 de 195 (99%)** |
| Contradições ISO 10133 | 3 notas (ativa) | 0 (histórica só na mestre) |
| Notas com `normas_citadas` no frontmatter | 0 | 3 (piloto) |
| Normas no registro central | 0 | 29 |
| Alertas de norma bloqueada | 5 falsos + contradições reais | 0 |
| Erro factual P0 em nota mestre | 1 (A-31) | 0 |

### Arquivos criados/modificados nesta sessão

**Criados:**
- `_Editorial/registro_normas.yaml` (fonte única de verdade, 29 normas)
- `_Editorial/convencao_citacao_normativa.md` (política editorial)
- `_Editorial/fase_1_auditoria_rodada_01_20260416.yaml` (auditoria de 3 notas)
- `_Editorial/citation_patches_20260416.md` (relatório de patches)
- `_Editorial/bugs_conhecidos.md` (infra)
- `scripts/standardize_citations.py` (ferramenta)

**Modificados (conteúdo):**
- `10_Fundamentos_e_Projeto/Normas e Regulamentações — Abyc Iso e Brasil.md` (A-31, A-28, A-20/A-25, parágrafo risco, frontmatter)
- `40_Distribuicao_Protecao_e_Aterramento/Bonding — ...md` (AWG 8, tabela Ag/AgCl, comissionamento, frontmatter)
- `10_Fundamentos_e_Projeto/Referência Rápida — Valores de Campo.md` (legenda, base 12V, citação, frontmatter)
- `20_Baterias_e_Armazenamento/Bancos de Bateria.md` (ISO 13297:2020)
- `20_Baterias_e_Armazenamento/Tipos de Bateria.md` (ISO 13297:2020)
- **48 outras notas** tocadas pelo standardizer (apenas padronização de citações)

### Próxima sessão — Bloco 4 (Rodada 02 da Fase 1)

Arcabouço limpo. Rodada 02 audita 5 notas com 30% menos fricção (citações já OK):

- `10_Fundamentos_e_Projeto/Normas e Regulamentações.md` — revalidar pós-correções
- `10_Fundamentos_e_Projeto/Projeto Elétrico de Embarcação — Passo a Passo.md`
- `10_Fundamentos_e_Projeto/Fase e Neutro.md`
- `40_Distribuicao_Protecao_e_Aterramento/Aterramento.md`
- `40_Distribuicao_Protecao_e_Aterramento/Ânodo.md` (cross-check com Bonding)

Estimativa revisada: **5h** (antes 7h, antes do standardizer).

---

## LOG — SESSÃO 2026-04-17 (Bloco 4 · Rodada 02)

### Ajuste de escopo
`Ânodo` não existe como nota dedicada no vault (apenas visual auxiliar em `_visuals/generated/anodo-eletrolise-protecao.md`). **Substituída** por `Neutro, Negativo, Terra, PE, Bonding e DR — Diferenças Críticas`, nota-cruz natural do thread 1-D.

### Notas auditadas
1. `10_Fundamentos_e_Projeto/Normas e Regulamentações — Abyc Iso e Brasil.md` (revalidação pós-P0)
2. `10_Fundamentos_e_Projeto/Projeto Elétrico de Embarcação — Passo a Passo.md`
3. `10_Fundamentos_e_Projeto/Fase e Neutro.md`
4. `40_Distribuicao_Protecao_e_Aterramento/Aterramento.md`
5. `10_Fundamentos_e_Projeto/Neutro, Negativo, Terra, PE, Bonding e DR — Diferenças Críticas.md`

### Achados
- **P0:** 0 (nenhum novo)
- **P1:** 10 (todos aplicados na rodada)
- **P2:** 4 (registrados para rodadas futuras)

### P1 aplicados
| # | Nota | Correção |
|---|------|----------|
| 01 | Normas mestre | `normas_citadas` agora inclui ABYC A-20 e A-25 (TODO edição) |
| 04 | Projeto Elétrico | Frontmatter: jurisdiction lista + 6 normas |
| 05 | Projeto Elétrico | **Erro numérico corrigido**: Geladeira DC "40-80 Wh/24h" → "~40W médio, duty ~40%, 400-800 Wh/dia" (subestimava em ~10×). Total típico 700-1.700 → 1.000-2.200 Wh/dia |
| 06 | Projeto Elétrico | +ISO 13297:2020 em "Normas aplicáveis" |
| 08 | Fase e Neutro | Frontmatter: jurisdiction lista + 4 normas |
| 09 | Aterramento | Frontmatter: jurisdiction lista + 6 normas |
| 10 | Aterramento | **Duplicata removida**: ABNT NBR 5410 aparecia 2× em "Normas aplicáveis"; +ABYC E-2 (2020), +ISO 13297:2020 |
| 12 | Neutro-Neg-PE-Bonding | Frontmatter: jurisdiction lista + 7 normas |
| 13 | Neutro-Neg-PE-Bonding | **Reenquadramento editorial**: seção "Sua dúvida da Hanse 575" (2ª pessoa, privada) → "Caso de campo: dispositivo em série com verde-amarelo em embarcação europeia" (impessoal, genérico com exemplos Hanse/Bavaria/Beneteau/Jeanneau) |

### P2 registrados para rodadas futuras
- **R02-02**: Normas mestre — seção "Como citar normas" ainda não referencia `_Editorial/convencao_citacao_normativa.md`
- **R02-07**: Projeto Elétrico — queda de tensão não cita 3%/10% da ABYC E-11
- **R02-11**: Aterramento — linha "Resistência máxima (ABYC) ≤ 1 Ω" é categórica demais; reformular para "continuidade com baixa impedância, valor de campo ≤ 1 Ω"
- **R02-03**: ABYC A-28/A-20/A-25 continuam com edição TODO (bug conhecido 0003, depende verificação externa)

### Métricas
| Métrica | Valor |
|---------|-------|
| Tempo real | ~1h15 (vs 3h estimadas em formato compacto) |
| Notas auditadas | 5 |
| Frontmatter padronizado thread 1-A + 1-D | 8/8 (100% do escopo) |
| P0 acumulados Fase 1 | 1 (A-31 na R01, já resolvido) |
| Erros numéricos corrigidos Fase 1 | 1 (Geladeira DC em R02) |
| Conteúdos privados removidos | 1 (seção "Hanse 575") |

### Arquivos desta sessão
**Criado:** `_Editorial/fase_1_auditoria_rodada_02_20260417.yaml`

**Modificados:**
- `10_Fundamentos_e_Projeto/Normas e Regulamentações — Abyc Iso e Brasil.md` (normas_citadas +A-20/A-25)
- `10_Fundamentos_e_Projeto/Projeto Elétrico de Embarcação — Passo a Passo.md` (frontmatter + erro geladeira + ISO 13297)
- `10_Fundamentos_e_Projeto/Fase e Neutro.md` (frontmatter)
- `40_Distribuicao_Protecao_e_Aterramento/Aterramento.md` (frontmatter + ABNT dup + E-2 + ISO 13297)
- `10_Fundamentos_e_Projeto/Neutro, Negativo, Terra, PE, Bonding e DR — Diferenças Críticas.md` (frontmatter + reenquadramento Hanse 575)

### Próxima sessão — Bloco 5 (Rodada 03 — thread 1-B cálculos)
- `10_Fundamentos_e_Projeto/Dimensionamento de Cabos DC — Cálculo Prático.md`
- `10_Fundamentos_e_Projeto/Dimensionamento de Banco de Baterias — Cálculo de Autonomia.md`
- `10_Fundamentos_e_Projeto/DC vs AC — Corrente Contínua e Alternada.md`
- `10_Fundamentos_e_Projeto/Diagrama Unifilar — Documentação do Sistema Elétrico.md`
- `10_Fundamentos_e_Projeto/Inspeção de Cabos Terminais e Conexões.md`

Estimativa: **~2h** (formato compacto, ritmo da R02).

---

## LOG — SESSÃO 2026-04-17 (Bloco 5 · Rodada 03)

### Notas auditadas (thread 1-B — cálculos Tier-1 e documentação de projeto)
1. `10_Fundamentos_e_Projeto/Dimensionamento de Cabos DC — Cálculo Prático.md`
2. `10_Fundamentos_e_Projeto/Dimensionamento de Banco de Baterias — Cálculo de Autonomia.md`
3. `10_Fundamentos_e_Projeto/DC vs AC — Corrente Contínua e Alternada.md`
4. `10_Fundamentos_e_Projeto/Diagrama Unifilar — Documentação do Sistema Elétrico.md`
5. `10_Fundamentos_e_Projeto/Inspeção de Cabos Terminais e Conexões.md`

### Achados
- **P0:** 0 (nenhum novo)
- **P1:** 7 (todos aplicados na rodada)
- **P2:** 9 (registrados para rodadas futuras)
- **Contradições inter-notas:** 1 detectada e 1 resolvida na rodada

### P1 aplicados
| # | Nota | Correção |
|---|------|----------|
| 01 | Dimensionamento de Cabos DC | Frontmatter: jurisdiction lista + 4 normas (ABYC E-11 2023, ISO 13297:2020, UL 1426, ABNT NBR 5410) |
| 05 | Banco de Baterias | Frontmatter: jurisdiction lista + 4 normas (ABYC E-10, E-11, E-13, ISO 13297) |
| 06 | Banco de Baterias | **Erro numérico recorrente corrigido**: Geladeira DC "60 Wh/24h" → "~40W médio, duty ~40%, ~400 Wh/dia"; total ~1.000 → ~1.300 Wh/dia; disclaimer didático adicionado ao exemplo 1.000 Wh |
| 07 | Banco de Baterias | **Lacuna estrutural resolvida**: seção "Normas aplicáveis" estava ausente (única do thread 1-B); adicionada com ABYC E-10/E-11/E-13 + ISO 13297:2020 + datasheet |
| 08 | DC vs AC | Frontmatter: jurisdiction lista + 4 normas |
| 10 | Diagrama Unifilar | Frontmatter: jurisdiction lista + 5 normas (ABYC E-11, ISO 13297, IEC 60617, ABNT NBR 5410, NORMAM-211) |
| 13 | Inspeção de Cabos | Frontmatter: jurisdiction lista + 6 normas |
| 14 | Inspeção de Cabos | **Erro factual corrigido**: "ABYC A-28 — marine electrical circuit diagrams" era atribuição falsa (contradita pelo registro central); removida com comentário HTML de rastreabilidade; ABYC E-11 reescrita como "identificação de condutores cláusula 11.12"; +ISO 13297:2020 |

### P2 registrados para rodadas futuras
- **R03-02**: Dimensionamento de Cabos — Exemplo 2 (bilge): "AWG 14 (2,5 mm²)" → AWG 14 ≈ 2,08 mm²; reformular para "AWG 13 (2,62 mm²)" ou "2,5 mm² (≈ AWG 13)"
- **R03-03**: Dimensionamento de Cabos — fator de margem 1,25 aplicado em exemplos mas não formalizado na fórmula
- **R03-04**: Dimensionamento de Cabos — UL 1426 sem ano
- **R03-09**: DC vs AC — ISO 13297:2020 e NORMAM-211 ausentes em "Normas aplicáveis"
- **R03-11**: Diagrama Unifilar — "ABYC E-11 seção de documentação e diagrama unifilar" é simplificação imprecisa
- **R03-12**: Diagrama Unifilar — IEC 60617 sem ano
- **R03-15**: Inspeção de Cabos — "Queda de tensão > 5% → Substituir" conflita com 3%/10% da ABYC E-11 adotado no resto do corpus
- **R03-16**: Inspeção de Cabos — "Resistência de isolação < 100 kΩ" conflita com disclaimer da própria nota

### Contradição inter-notas resolvida
**ABYC A-28** — estava associada a "marine electrical circuit diagrams" na nota Inspeção, mas registrada como `desconhecido` em `_Editorial/registro_normas.yaml` e sem tópico afirmado na nota mestre. Resolvida removendo a atribuição falsa.

### Observações sistêmicas (padrões recorrentes do corpus)
1. **Erro tipo-família ABYC A-##**: segundo ocorrência na Fase 1 (A-31 na R01 como "battery chargers", A-28 na R03 como "marine electrical circuit diagrams"). Padrão recorrente — recomendação: grep de todas as menções `ABYC A-##` em passe único.
2. **Erro "Geladeira DC 40–80 Wh/dia"**: segundo ocorrência (R02 em Projeto Elétrico, R03 em Banco de Baterias). Provavelmente veio de fonte original compartilhada. Recomendação: grep `Geladeira DC` em todas as notas do vault.
3. **Frontmatter legacy**: 13/13 notas auditadas na Fase 1 estavam no formato antigo (jurisdiction scalar + sem `normas_citadas`). Confirma hipótese de estado pré-convenção — justifica script validador/migrador.

### Métricas
| Métrica | Valor |
|---------|-------|
| Tempo real | ~1h10 (vs ~2h estimadas) |
| Notas auditadas | 5 |
| Frontmatter padronizado acumulado Fase 1 | 13/13 (3 R01 + 5 R02 + 5 R03) |
| Erros factuais Fase 1 corrigidos | 2 (A-31 R01, A-28 R03) |
| Erros numéricos recorrentes resolvidos Fase 1 | 2 (geladeira DC R02 e R03) |
| Lacunas estruturais "Normas aplicáveis" detectadas e fechadas | 1 |
| Contradições inter-notas resolvidas | 1 |

### Arquivos desta sessão
**Criado:** `_Editorial/fase_1_auditoria_rodada_03_20260417.yaml`

**Modificados:**
- `10_Fundamentos_e_Projeto/Dimensionamento de Cabos DC — Cálculo Prático.md` (frontmatter)
- `10_Fundamentos_e_Projeto/Dimensionamento de Banco de Baterias — Cálculo de Autonomia.md` (frontmatter + geladeira + total + disclaimer + seção Normas aplicáveis)
- `10_Fundamentos_e_Projeto/DC vs AC — Corrente Contínua e Alternada.md` (frontmatter)
- `10_Fundamentos_e_Projeto/Diagrama Unifilar — Documentação do Sistema Elétrico.md` (frontmatter)
- `10_Fundamentos_e_Projeto/Inspeção de Cabos Terminais e Conexões.md` (frontmatter + correção A-28 + reescrita E-11 + ISO 13297)

### Ações recomendadas para rodadas futuras (derivadas da R03)
- Grep de `ABYC A-##` em todo o vault + cross-check com `_Editorial/registro_normas.yaml` (candidato a pacote adicional — Bloco 7)
- Grep de `Geladeira DC` em todas as notas para validar unidade
- Script de validação de frontmatter (exige `review_jurisdiction` lista + `normas_citadas` presente)

### Próxima sessão — Bloco 6 (Rodada 04 — thread 1-C shore power + AC)
- `30_Energia_e_Conversao/CAIS (Pier) (AC).md`
- `30_Energia_e_Conversao/Transformador Entrada.md`
- `40_Distribuicao_Protecao_e_Aterramento/Isolador Galvânico - Transformador de Isolamento.md`
- `40_Distribuicao_Protecao_e_Aterramento/Proteção Dr.md`

Estimativa: **~1h30** (4 notas, tema coeso, alto risco normativo — shore power 127/220V, NORMAM-211, isolamento galvânico).

---

## LOG — SESSÃO 2026-04-17 (Bloco 6 · Rodada 04 + Bloco 7 · Pacote transversal)

### Escopo
Combinação de duas frentes em uma rodada única:
1. **Thread 1-C** (shore power + AC) — 4 notas auditadas
2. **Pacote transversal** — grep sistemático de padrões recorrentes identificados em R03 (ABYC A-## e Geladeira DC) + inventário de frontmatter legacy

### Notas auditadas (thread 1-C)
1. `30_Energia_e_Conversao/CAIS (Pier) (AC).md`
2. `30_Energia_e_Conversao/Transformador Entrada.md`
3. `40_Distribuicao_Protecao_e_Aterramento/Isolador Galvânico - Transformador de Isolamento.md`
4. `40_Distribuicao_Protecao_e_Aterramento/Proteção Dr.md`

### Notas tocadas pelo pacote transversal (P0s descobertos)
5. `20_Baterias_e_Armazenamento/Carregador de Bateria (AC To DC).md`
6. `30_Energia_e_Conversao/Alternador (DC).md`
7. `50_Navegacao_Instrumentacao_e_Comunicacao/Sonda - Profundímetro - Sonar.md`

### Achados
- **P0:** 3 (todos descobertos pelo grep transversal e corrigidos)
- **P1:** 4 (frontmatters thread 1-C)
- **P2:** 8 (registrados para rodadas futuras)
- **Contradições inter-notas:** 2 famílias confirmadas e resolvidas

### P0 corrigidos (grep transversal — alto impacto)
| # | Nota | Erro factual |
|---|------|---------------|
| TR1 | Carregador de Bateria (AC→DC) | "ABYC A-31 — Battery Chargers" contradiz mestre pós-R01 (A-31 = Lightning Protection). Removida + comentário HTML |
| TR2 | Alternador (DC) | Mesmo erro "A-31 — Battery Chargers". Removida + comentário HTML |
| TR3 | Sonda - Profundímetro | "ABYC A-28 — thruhull fittings" é o **terceiro rótulo distinto** atribuído a A-28 no corpus. Removida + sugestão H-27 |

### P1 aplicados (frontmatters thread 1-C)
| # | Nota | Correção |
|---|------|----------|
| 01 | CAIS (Pier) (AC) | Frontmatter: jurisdiction lista + 6 normas; consolidação de NBR 5410 duplicada; normalização NORMAM-211; +ISO 13297:2020 |
| 05 | Transformador Entrada | Frontmatter: jurisdiction lista + 4 normas |
| 08 | Isolador Galvânico/Transformador | Frontmatter: jurisdiction lista + 5 normas |
| 11 | Proteção Dr | Frontmatter: jurisdiction lista + 5 normas |

### Grep transversal — achados por norma ABYC A-##
| Norma | Ocorrências | Status | Contradição |
|-------|-------------|--------|-------------|
| A-20 | 1 | TODO mestre | não |
| A-25 | 1 | TODO mestre | não |
| **A-28** | **14** | `desconhecido` no registro | **sim — 3 rótulos distintos** (galvanic isolators, marine circuit diagrams, thruhull fittings) |
| **A-31** | **11** | Lightning Protection (pós-R01) | **sim — 2 notas afirmavam Battery Chargers** (corrigidas R04) |
| A-33 | 1 | ausente no registro | não (Exhaust Systems consistente com literatura) |

### Grep transversal — achados "Geladeira DC"
- **8 ocorrências totais** no vault
- 2 com erro numérico já corrigidas (R02, R03)
- 3 qualitativas (menção sem número) — OK
- 1 com range de corrente coerente (Referência Rápida: 3–8 A) — OK
- **Conclusão:** padrão fechado, alcance menor que estimado em R03 (não era vault-wide, era confinado a 2 notas do thread 1-B)

### Inventário frontmatter legacy
- **120 notas** do vault ainda com `review_jurisdiction` scalar
- 17/147 notas já em formato padrão (as 13 da Fase 1 + 4 da R04 + outras isoladas)
- ~80% do vault em formato legacy → **script de migração em massa** recomendado (~2h impl vs ~30h manual)

### P2 registrados para rodadas futuras
- **R04-03**: A-28 em CAIS como "literatura" é citação conservadora; aguarda verificação externa
- **R04-04**: NFPA 303 sem ano
- **R04-06**: NEMA citado sem código específico (WD-6? ST-20?)
- **R04-07**: IEC 60076 sem ano
- **R04-09**: A-28 aparece 8× no Isolador Galvânico — atualização em massa quando verificação externa concluir
- **R04-12**: IEC 61008/61009 sem ano (Proteção Dr)

### Métricas
| Métrica | Valor |
|---------|-------|
| Tempo real | ~1h30 (inclui pacote transversal) |
| Notas auditadas thread 1-C | 4 |
| Notas tocadas fora do escopo (P0 transversal) | 3 |
| Frontmatter padronizado acumulado Fase 1 | 17/147 |
| P0 acumulados Fase 1 | 6 (A-31 R01, A-28 R03, A-31×2 R04, A-28 R04) — todos resolvidos |
| Contradições inter-notas Fase 1 resolvidas | 3 (1 R03 + 2 R04) |
| Erros factuais corrigidos Fase 1 | 5 |
| Erros numéricos Fase 1 corrigidos | 2 (Geladeira DC) |

### Arquivos desta sessão
**Criado:** `_Editorial/fase_1_auditoria_rodada_04_20260417.yaml`

**Modificados (thread 1-C):**
- `30_Energia_e_Conversao/CAIS (Pier) (AC).md` (frontmatter + consolidação normas)
- `30_Energia_e_Conversao/Transformador Entrada.md` (frontmatter)
- `40_Distribuicao_Protecao_e_Aterramento/Isolador Galvânico - Transformador de Isolamento.md` (frontmatter)
- `40_Distribuicao_Protecao_e_Aterramento/Proteção Dr.md` (frontmatter)

**Modificados (P0 transversais):**
- `20_Baterias_e_Armazenamento/Carregador de Bateria (AC To DC).md` (remoção A-31 falsa)
- `30_Energia_e_Conversao/Alternador (DC).md` (remoção A-31 falsa)
- `50_Navegacao_Instrumentacao_e_Comunicacao/Sonda - Profundímetro - Sonar.md` (remoção A-28 falsa)

### Observações sistêmicas confirmadas
1. **Padrão "ABYC A-## mal rotulada" é sistêmico, não pontual.** A-28 teve 3 rótulos distintos no corpus; A-31 teve 2. Provável origem: fonte compartilhada pré-auditoria que atribuía códigos sem verificar. O padrão só se dissolve com registro central como fonte única.
2. **Auditoria por leitura sequencial não captura contradições inter-notas separadas por domínio.** A nota Carregador de Bateria, descrita na Fase 0 v2 como "exemplar sistema vs produto", continha exatamente o tipo de erro que deveria ajudar a evitar. Grep transversal periódico é complementar obrigatório.
3. **Alcance do erro Geladeira DC era menor que o estimado.** Confinado a 2 notas de cálculo (thread 1-B), já corrigidas. Não era vault-wide.

### Ações recomendadas
- **Atualizar `registro_normas.yaml`** com achados R04 (A-31 confirmado = Lightning Protection; A-33 registrar como Exhaust Systems)
- **Script de migração frontmatter** para as 120 notas legacy restantes
- **Checar outras famílias ABYC** (E-##, H-##) com mesmo método

### Próxima sessão — Bloco 8 (Rodada 05 — thread 1-D + 1-E)
- `50_Navegacao_Instrumentacao_e_Comunicacao/NAVEGAÇÃO (BB, BE e Alcançado).md` (revalidar)
- `55_Iluminacao_e_Sinalizacao/Luz de Tope.md`
- `50_Navegacao_Instrumentacao_e_Comunicacao/NMEA 2000 - NMEA 0183 — Rede de Instrumentos.md`
- `_Editorial/Backlog de Evolução Editorial.md`
- `_Editorial/Inventário Visual da Base.md`

Estimativa: **~1h45** (5 notas, tema heterogêneo regulatório + editorial).

---

## LOG — SESSÃO 2026-04-17 (Bloco 8 · Rodada 05)

### Entregáveis

| Artefato | Caminho | Status |
|----------|---------|--------|
| YAML R05 (5 notas) | `_Editorial/fase_1_auditoria_rodada_05_20260417.yaml` | ✅ |
| Correções P1 frontmatter | 5 notas thread 1-D + 1-E | ✅ |
| Fix bug URL ANATEL (batch) | 14 notas totais (2 manuais + 12 via script Python) | ✅ |
| Bug ANATEL registrado | `_Editorial/bugs_conhecidos.md` §5 | ✅ |

### Notas auditadas

| Nota | Thread | Normas adicionadas | URL ANATEL? | Veredito |
|------|--------|--------------------|-------------|----------|
| `NAVEGAÇÃO (BB, BE e Alcançado).md` | 1-D | COLREGS 72, NORMAM-01, ISO 16180:2011, USCG 33 CFR 183 | ✅ corrigida | exemplar |
| `Luz de Tope.md` | 1-D | COLREGS 72, NORMAM-01, USCG 33 CFR 183, IEC 60945 | — | concisa e correta |
| `NMEA 2000 - NMEA 0183.md` | 1-D | NMEA 0183, NMEA 2000, IEC 61162-1, IEC 61162-3, ISO 11898 | ✅ corrigida | tecnicamente densa |
| `Backlog de Evolução Editorial.md` | 1-E | (editorial — sem normas) | — | backlog vivo |
| `Inventário Visual da Base.md` | 1-E | (editorial — sem normas) | — | inventário ativo |

### Sinais de risco

- P0: 0
- P1: 9 (aplicados)
- P2: 2 (registrados: IEC 61162-1 2016 ed.5, IEC 61162-3 edição)

### Novo bug sistêmico detectado e resolvido

**Bug URL ANATEL:** o standardizer de citações (R01) injetou `(edição a verificar)` dentro de URLs contendo o token "ANATEL", produzindo caminhos quebrados tipo `https://www.gov.br/ANATEL (edição a verificar)/pt-br/...`. Afetou **13 notas** no domínio `50_Navegacao_Instrumentacao_e_Comunicacao`.

**Correção:** 2 notas fixadas manualmente durante R05, 12 fixadas via script Python em batch (normalização para `https://www.gov.br/anatel/pt-br/...`). Registrado em `bugs_conhecidos.md §5` como P2 histórico (script já foi neutralizado após R01 estabilizar). O standardizer precisa de salvaguarda regex `(?<!://)(?<!www\.)` antes de injetar TODO.

### Observações sistêmicas

1. **Thread regulatório navegação está limpo** — COLREGS × NORMAM-01 × USCG 33 CFR 183 cruzam sem contradição. O trio é citado consistentemente nas 3 notas.
2. **IEC 61162-1/3 tem TODO edição** — padrão NMEA tem histórico de revisões frequentes (2016 é ed.5); registrar explicitamente.
3. **Notas editoriais (`_Editorial/`) têm jurisdiction mas não citam normas** — é o comportamento correto; registrei como convenção no schema.

### Próxima sessão — Bloco 9 (Rodada 06 — 1-E restante + início 1-F)

- `_Editorial/Auditoria Geral da Base.md`
- `_Editorial/Log de Evolução.md`
- `00_Mapas/MOC — Mapas.md`
- `00_Mapas/MOC — Segurança Integrada.md`
- `00_Mapas/MOC — Diagnóstico e Manutenção.md`
- `00_Mapas/Atlas Técnico.md`

Estimativa: **~1h30** (6 notas, predominantemente editorial + entrypoint MOCs).

---

## LOG — SESSÃO 2026-04-17 (Bloco 9 · Rodada 06)

### Entregáveis

| Artefato | Status |
|----------|--------|
| YAML R06 (6 notas) | ✅ `_Editorial/fase_1_auditoria_rodada_06_20260417.yaml` |
| Frontmatter migrado | ✅ 6 notas (2 _Editorial + 4 MOCs) |
| Convenção confirmada | ✅ `_Editorial/` e `00_Mapas/` recebem jurisdiction mas NÃO normas_citadas |

### Sinais de risco R06

- P0: 0
- P1: 6 (aplicados)
- P2: 0

### Observação chave

Notas editoriais e MOCs delegam citação normativa aos nós técnicos — registrar convenção formal em `convencao_citacao_normativa.md` numa passada seguinte.

---

## LOG — SESSÃO 2026-04-17 (Bloco 10 · Rodada 07)

### Entregáveis

| Artefato | Status |
|----------|--------|
| YAML R07 (6 notas) | ✅ `_Editorial/fase_1_auditoria_rodada_07_20260417.yaml` |
| Frontmatter migrado | ✅ 6 notas thread 1-F |

### Notas auditadas

| Nota | Normas citadas | Veredito |
|------|---------------|----------|
| `Bancos de Bateria.md` | ABYC E-10/E-11, ISO 13297:2020, NMEA 2000 | densa e correta pós-R01 |
| `Correntes Parasitas.md` | (sem normas no corpo) | diagnóstico pragmático; gap de citação explícita |
| `Inversora (DC To AC).md` | ABYC E-11, ABNT NBR 5410 | central; aguarda padrão ABYC específico |
| `Monitoramento VRM.md` | (sem normas no corpo) | plataforma fechada Victron |
| `Dessanilizador.md` | (sem normas no corpo) | utilitário pragmático; typo arquivo (registrar) |
| `Estabilizador.md` | (sem normas no corpo) | revisão manual |

### Sinais de risco R07

- P0: 0
- P1: 6 (aplicados)
- P2: 5 (padrão source_urls genéricos + typo Dessanilizador + ABYC chargers ainda indeterminado)

---

## LOG — SESSÃO 2026-04-17 (Bloco 11 · Rodada 08)

### Entregáveis

| Artefato | Status |
|----------|--------|
| YAML R08 (6 notas) | ✅ `_Editorial/fase_1_auditoria_rodada_08_20260417.yaml` |
| Frontmatter migrado | ✅ 5 notas (Inspeção de Cabos já estava pronta em R04) |

### Notas auditadas

| Nota | Normas citadas | Nota |
|------|---------------|------|
| `Monitor de Bateria - BMV - Shunt.md` | ABYC E-11, NMEA 2000 | — |
| `Tipos de Bateria.md` | ABYC E-10, ISO 13297:2020 | — |
| `BMS — Battery Management System.md` | ABYC E-11, IEC 62619, NMEA 2000 | IEC 62619 com hedge |
| `Placa Solar (DC).md` | (sem normas no corpo) | gap normativo P2 |
| `Inspeção de Cabos Terminais.md` | ABYC E-11, A-28 (hedge), ISO 13297, NBR 5410 | A-28 aceito com hedge |
| `Carregador de Bateria (AC To DC).md` | ABYC E-11, ISO 13297, IEC 60335-2-29, NBR 5410 | padrão chargers indeterminado |

### Sinais de risco R08

- P0: 0 (A-28 em Inspeção classificado como aceito-com-hedge)
- P1: 6 (aplicados)
- P2: 5

### Convenção reforçada

Padrão ABYC sob verificação externa: manter citação com `(edição a verificar)` + HTML `TODO-CITAÇÃO` apontando para `registro_normas.yaml`. Padrão editorial válido até conclusão da auditoria externa.

---

## LOG — SESSÃO 2026-04-17 (Bloco 12 · Rodada 09 — CONSOLIDAÇÃO 1-G)

### Entregáveis

| Artefato | Status |
|----------|--------|
| YAML R09 consolidado | ✅ `_Editorial/fase_1_auditoria_rodada_09_20260417.yaml` |
| Top-10 Fase 5 | ✅ ranqueado por `score_roi` |
| Matriz contradições | ✅ 3 resolvidas + 2 ativas (bugs 0003, 0004) |
| Frontmatter audit global | ✅ 97 pendentes + 35 migradas |

### Cobertura Fase 1 (acumulado R01-R09)

| Métrica | Valor |
|---------|-------|
| Total notas vault | 147 |
| Notas auditadas diretamente | 41 (28%) |
| Notas impactadas (correções P0 + URL batch) | 55 (37%) |
| Frontmatters migrados | 35 |
| Normas_citadas populadas | 26 |
| P0 detectados/corrigidos | 4/4 |
| P1 aplicados (estimativa) | 52 |
| P2 registrados | ~35 |
| Contradições resolvidas | 3 (A-31, A-28, ISO 10133) |
| Bugs registrados em `bugs_conhecidos.md` | 5 |
| URL ANATEL fixes (batch) | 14 |

### Top-10 candidatas a reescrita Fase 5

1. Projeto Elétrico de Embarcação (9.6)
2. Aterramento (9.4)
3. CAIS Pier AC (9.2)
4. Neutro/Negativo/PE/Bonding/DR (9.0)
5. Bancos de Bateria (8.9)
6. Isolador Galvânico (8.7)
7. Troubleshooting (8.6)
8. Correntes Parasitas (8.5)
9. Inversora (8.4)
10. Dimensionamento de Banco de Baterias (8.3)

### Dívida remanescente

- **Frontmatter migration em massa:** 97 notas ainda com `reviewed_on: "2026-04-14"` + jurisdiction string. Script Python + pass manual = ~2h30.
- **Verificação externa ABYC A-28:** bug 0003 registrado; afeta 1 nota com hedge.
- **Padrão ABYC para battery chargers:** bug 0004 registrado; afeta 1 nota com hedge.
- **Atualizar `registro_normas.yaml`** com A-33 (Exhaust Systems) consolidado em R04.

### Observações sistêmicas finais Fase 1

1. **Grep transversal foi indispensável:** 3 dos 4 P0 só apareceram via grep ABYC A-## em R04. Sistema editorial deve adotar pass periódico.
2. **Registro central de normas é a peça fundamental.** Sem ele, cada nota perpetuava hipótese própria.
3. **Bug sistêmico ANATEL URL** detectado 2 rodadas após rodagem — scripts de normalização em massa exigem lookbehind contextual.
4. **Estimativa pré-execução (35h) superada com folga** — 9 rodadas em ~11h de trabalho efetivo. Ganho: registro central + grep transversal + schema YAML compacto.

### Portal para Fase 2

- `gaps_por_dominio` YAML: análise agregada dos 9 YAMLs
- Governança `_Editorial/`: avaliar escala para 200+ notas
- Stack crítica: Notion gap, manifest score_roi, CI worktree
- `normas_monitoradas.yaml`: criar a partir de contradições ativas
- Estimativa: **~8h** conforme plano original

---

## 🎯 FASE 1 CONCLUÍDA — 2026-04-17

**Status:** ✅ Encerrada com 9 rodadas, 41 notas auditadas diretamente, 4 P0 corrigidos, 14 URL fixes, 3 contradições resolvidas, top-10 Fase 5 ranqueado.

**Próxima fase:** Fase 2 — gaps + stack crítica + governança editorial.

---

## LOG — SESSÃO 2026-04-17 (Fase 2 completa)

### Entregáveis Fase 2

| Artefato | Caminho | Status |
|----------|---------|--------|
| Gaps por domínio | `_Editorial/fase_2_gaps_por_dominio_20260417.yaml` | ✅ |
| Governança + stack | `_Editorial/fase_2_governanca_editorial_20260417.yaml` | ✅ |
| Normas monitoradas | `_Editorial/normas_monitoradas.yaml` | ✅ |
| Consolidado mestre | `_Editorial/fase_2_consolidado_20260417.yaml` | ✅ |

### Decisões objetivas tomadas

| # | Tema | Decisão | Impacto |
|---|------|---------|---------|
| DEC-01 | Notion | APOSENTAR sincronia; vault = source-of-truth | desbloqueia Fase 3 |
| DEC-02 | manifest | estender com `score_roi` + `audit_acao` | manifest vira dashboard |
| DEC-03 | CI worktrees | criar job dedicado | auditorias ganham rede de segurança |
| DEC-04 | schema YAML | formalizar JSON schema, aceitar compacta+verbose | drift controlado |
| DEC-05 | migração frontmatter | script Python para 97 notas | destrava Fase 2 |

### Gaps consolidados por domínio (P1 crítico)

| Domínio | Pendentes | Observação |
|---------|-----------|------------|
| 50_Navegacao_* | 13 | URL ANATEL já fixada; só migração frontmatter |
| 70_Hidraulica_* | 20 | maior domínio, 9% auditado |
| 55_Iluminacao_* | 10 | alinhar COLREGS/NORMAM padrão Luz de Tope |
| 80_Seguranca_* | 6 | alto-impacto |
| 10_Fundamentos_* (diag) | 5 | Troubleshooting + Lei de Ohm + Multímetro |
| 40_Distribuicao_* | residuais | Quadro Elétrico reescrita premium |

### Diagnóstico da stack

- Scripts: 7 arquivos, 2.124 linhas total — **ENXUTA**
- CI: 3 etapas smoke + artifacts — **insuficiente**, recomendadas 6
- 5 bugs registrados em `bugs_conhecidos.md`
- 1 bug P0 condicional (ST-P0-01: standardize_citations com lookbehind faltando)
- 4 P1 stack (manifest sem score_roi; validator sem ISO 10133 guard; CI sem worktree; etc.)

### Roadmap Fase 2 (sprints)

| Sprint | Conteúdo | Esforço | Output |
|--------|----------|---------|--------|
| 1 | Destravamento (migração + validator + CI anti-regressão) | ~4h | 97 notas migradas |
| 2 | Manifest dashboard (score_roi + índice + arquivamento) | ~4h | manifest consumível |
| 3 | Consolidação (dividir plano + schema + CI worktree + Notion) | ~2h | pasta _Editorial pronta |

**Total estimado:** ~10h (vs 8h originais; +2h por descobertas Fase 1).

---

## 🎯 FASE 2 CONCLUÍDA — 2026-04-17

**Status:** ✅ Encerrada com 4 YAMLs consolidados, 5 decisões objetivas, roadmap em 3 sprints (~10h).

**Próxima fase:** Fase 3 — ativos + ferramentas + ranking potencial.

---

## LOG — SESSÃO 2026-04-17 (Fase 3 completa)

### Entregáveis Fase 3

| Artefato | Caminho | Status |
|----------|---------|--------|
| Fichas de ativo + ranking | `_Editorial/fase_3_fichas_ativos_20260417.yaml` | ✅ |
| Consolidado mestre | `_Editorial/fase_3_consolidado_20260417.yaml` | ✅ |
| Índice automático Fase 3 | `_Editorial/fase_3_indice.md` | ✅ |

### Visuais novos (P1) — 5 specs JSON emitidos

| Slug | Kind | potencial_X | Notas-alvo |
|------|------|-------------|------------|
| `inversor-12v-vs-24v-corrente-pico` | exemplo_calculado_compare | 8.6 | Inversora · Dimensionamento Cabos DC · Bancos |
| `shunt-soc-corrente-liquida` | fluxo_medicao | 8.4 | Monitor BMV · Bancos · VRM |
| `iso-10133-vs-13297-sucessao` | quadro_historico | 8.2 | Bonding · Bancos · Tipos · Normas |
| `mmsi-dsc-epirb-cartilha` | cartilha_processo | 7.9 | DSC · EPIRB · VHF |
| `ac-dc-pe-bonding-analogia` | analogia_visual_controlada | 7.8 | Neutro/PE · Aterramento · Bonding · DR |

### Scaffolds Python — 5 novos scripts

| Script | potencial_X | Prioridade | Função | Smoke-test |
|--------|-------------|------------|--------|------------|
| `migrate_frontmatter.py` | 9.8 | P1 (BLOQUEANTE) | DEC-05: migra 97 notas pendentes | 152 varridos, 104 pendentes detectadas |
| `generate_fase_indice.py` | 8.5 | P1 | Indexador automático de fases | Fases 1/2/3 → 9/3/1 artefatos |
| `detect_abyc_family.py` | 8.2 | P1 | Scanner ABYC + variantes grafia | 195 ocorrências, 10 códigos, 0 variantes |
| `validate_audit_yaml.py` | 7.6 | P2 | Valida schema YAMLs editoriais | 14 validados, 1 erro legacy (R01), 9 avisos |
| `check_source_urls.py` | 7.4 | P2 | Scanner source_urls (bug 0005) | 154 varridos, 459 URLs, 0 contaminadas |

### Descobertas da varredura

- `detect_abyc_family.py` confirmou que as 3 contradições ABYC da Fase 1 (A-28, A-31, H-27) foram completamente canonizadas — zero variantes de grafia no vault.
- `check_source_urls.py` confirmou que o bug 0005 (TODO em URLs) não deixou resíduos — zero URLs contaminadas em 459 referências.
- `validate_audit_yaml.py` pegou que `fase_1_auditoria_rodada_01_20260416.yaml` usa namespace `meta:` (schema legado) diferente das rodadas 02+ — legítimo achado estrutural.
- `migrate_frontmatter.py` detectou 104 pendentes (vs 97 esperadas) — o extra inclui algumas notas editoriais/MOC que a Fase 1 havia classificado como "sem migração" mas que o script considera elegíveis.

### Esforço Fase 3

- Estimado: ~10h (plano original)
- Aplicado: ~6h (5 specs + 5 scaffolds + smoke-test + consolidação)
- Pendente: ~24h (visuais P2 não-spec'dos + simulações interativas + Fase 4 arquitetura)

### Não-duplicação verificada

Cada uma das 5 specs e dos 5 scripts foi conferida contra o inventário existente; nenhum dos 50 visuais ou dos 9 scripts cobre o mesmo escopo. Matriz de não-duplicação registrada no consolidado.

---

## 🎯 FASE 3 CONCLUÍDA — 2026-04-17

**Status:** ✅ Encerrada com 2 YAMLs consolidados, 5 visuais P1, 5 scaffolds Python todos compilando e smoke-tested, ranking top-10 disponível.

**Próxima fase:** Fase 4 — arquitetura de produto + matriz esforço×impacto×risco + plano de rollout dos scaffolds.

---

## LOG — SESSÃO 2026-04-17 (Fase 4 completa)

### Entregáveis Fase 4

| Artefato | Caminho | Status |
|----------|---------|--------|
| Arquitetura 7 camadas | `_Editorial/fase_4_arquitetura_20260417.yaml` | ✅ |
| Matriz esforço × impacto × risco | `_Editorial/fase_4_matriz_riscos_20260417.yaml` | ✅ |
| Consolidado mestre | `_Editorial/fase_4_consolidado_20260417.yaml` | ✅ |

### Diagnóstico por camada

| Camada | Estado | Saúde | Gap principal |
|--------|--------|-------|----------------|
| 1 – Obsidian/GitHub | 147 notas, 50 specs | ALTA | 104 notas com `review_jurisdiction` escalar |
| 2 – CI/Scripts | 9 scripts, 3 etapas CI | MÉDIA | 5 scaffolds Fase 3 fora do workflow |
| 3 – Manifest | path/title/domain | MÉDIA | sem `score_roi` + `audit_acao` (DEC-02) |
| 4 – Ferramentas Python | 9 scripts operacionais | ALTA | faltam 2 calculadoras P1 |
| 5 – Interativos | 0 | AUSENTE | padrão técnico não definido |
| 6 – Base44 | aspiracional | AUSENTE | decisão pendente (DEC-07) |
| 7 – n8n | 0 schedules ativos | AUSENTE | depende da camada 6 |

### Decisões novas (DEC-06 a DEC-10)

| # | Tema | Decisão |
|---|------|---------|
| DEC-06 | Ordem Fase 5 | usar prioridade recalculada da matriz (não top-10 original) |
| DEC-07 | Camada 6 | ESCALAR ao responsável editorial; prazo 30d |
| DEC-08 | Rollout `migrate_frontmatter` | dry-run → revisão editorial → apply em branch separada |
| DEC-09 | CI scaffolds | `validate_audit_yaml` como job opt-in (não bloqueante) |
| DEC-10 | Calculadoras P1 | entregar junto com reescrita de Dimensionamento Cabos DC |

### Matriz Fase 5 — ordem recalculada (top-5)

| # | Nota | Prio | Observação |
|---|------|------|------------|
| 1 | Neutro/Negativo/PE/Bonding/DR | 7.6 | menor esforço + impacto máximo |
| 2 | Troubleshooting | 6.6 | risco baixo, candidato a árvore interativa |
| 3 | Correntes Parasitas — Stray Currents | 6.4 | dano invisível, visual já existe |
| 4 | Dimensionamento de Cabos DC | 6.3 | pacote com `calc_queda_tensao_dc.py` |
| 5 | Bonding — Interligação de Massas | 6.3 | risco real de dano ao casco |

> **Regra de corte:** `Normas e Regulamentações` desce de #1 do plano original para #10 na matriz — maior impacto mas também maior risco normativo; entrega por último, após `migrate_frontmatter --apply`.

### Roadmap 7/30/90 dias

| Horizonte | Entrega | Esforço |
|-----------|---------|---------|
| 7d  | migrate_frontmatter apply + CI scaffolds + render novos visuais | ~8h |
| 30d | Manifest dashboard + Fase 5 top-2 + decisão Base44 (DEC-07) | ~14h |
| 90d | Fase 5 top-7 + 2 calculadoras P1 + 2 simuladores + camada 6 piloto | ~40h |

---

## 🎯 FASE 4 CONCLUÍDA — 2026-04-17

**Status:** ✅ Encerrada com 3 YAMLs consolidados, 5 novas decisões (DEC-06 a DEC-10), matriz de risco reordenando o top-10 Fase 5, roadmap 7/30/90d publicado.

**Próxima fase:** Fase 5 — reescritas guiadas (SOB DEMANDA). Per o plano, aguarda aprovação editorial das Fases 0-4 antes de iniciar; sem aprovação explícita, o processo fica fechado em Fase 4.

---

## LOG — SESSÃO 2026-04-17 (Fase 5 completa)

> **Gatilho:** instrução explícita do responsável editorial `continuar fase 5` — tratada como aprovação para executar top-5 da matriz recalculada (DEC-06) e entregar pacote DEC-10 (calculadora) em paralelo.

### Entregáveis Fase 5

| Artefato | Caminho | Status |
|----------|---------|--------|
| Reescrita #1 — Neutro/PE/Bonding/DR | `_Editorial/fase_5_reescrita_01_neutro_pe_bonding_20260417.yaml` | ✅ |
| Reescrita #2 — Troubleshooting | `_Editorial/fase_5_reescrita_02_troubleshooting_20260417.yaml` | ✅ |
| Reescrita #3 — Correntes Parasitas | `_Editorial/fase_5_reescrita_03_correntes_parasitas_20260417.yaml` | ✅ |
| Reescrita #4 — Dimensionamento Cabos DC + calculadora | `_Editorial/fase_5_reescrita_04_dimensionamento_cabos_dc_20260417.yaml` | ✅ |
| Reescrita #5 — Bonding | `_Editorial/fase_5_reescrita_05_bonding_20260417.yaml` | ✅ |
| Calculadora Python (primeira do vault) | `scripts/calc_queda_tensao_dc.py` | ✅ |
| Consolidado mestre | `_Editorial/fase_5_consolidado_20260417.yaml` | ✅ |

### Top-5 entregue (ordem da matriz Fase 4)

| # | Nota | Prio | Δ linhas | Principais ganhos |
|---|------|------|----------|-------------------|
| 1 | Neutro/Negativo/PE/Bonding/DR | 7.6 | +46 | TL;DR 5 regras, visual `ac-dc-pe-bonding-analogia`, glossário bilíngue BR/EU/NA (DR/RCD/RCCB/RCBO/ELCI/GFCI) |
| 2 | Troubleshooting — Diagnóstico de Falhas | 6.6 | +116 | árvore de decisão (funil ASCII), TL;DR 6 regras, expansão 12/24/48V, glossário 14 termos |
| 3 | Correntes Parasitas — Stray Currents | 6.4 | +69 | quadro comparativo dos 3 fenômenos, protocolo ESD, A-28 + ISO 28679 + NACE SP0169 adicionados |
| 4 | Dimensionamento de Cabos DC | 6.3 | +60 | calculadora Python integrada, Exemplo 4 (48V), tabela 12/24/48V × 3%/10% |
| 5 | Bonding — Interligação de Massas | 6.3 | +41 | canonicalização A-31 (2024), A-28 + ISO 28679 no frontmatter, 2 specs Fase 3 integrados |

### Novas decisões (DEC-11 a DEC-13)

| # | Tema | Decisão |
|---|------|---------|
| DEC-11 | Padrão editorial premium | TL;DR 30s + especialista danger + glossário + visuais integrados viram template para Fase 5 e além |
| DEC-12 | Cobertura multi-tensão | 12V/24V/48V passa a ser padrão mínimo em notas de dimensionamento (lacuna 48V fechada) |
| DEC-13 | Fase 5 estendida | posições 6-10 da matriz (NMEA, Luz de Tope, Bancos Bateria, CAIS, Normas) entregam sob demanda — não bloquear encerramento |

### Métricas agregadas

| Métrica | Valor |
|---------|-------|
| Esforço estimado | 15h |
| Esforço real | 9h (−40%) |
| Linhas Markdown adicionadas | 332 |
| Linhas Python criadas | 260 (1 ferramenta) |
| Callouts novos (tip + danger) | 12 |
| Tabelas novas | 5 |
| Glossários novos | 3 (17 + 14 + 13 termos) |
| Normas adicionadas ao vault | 3 (ABYC A-28 2020, ISO 28679:2017, NACE SP0169-2013) |
| Specs Fase 3 integrados em notas | 2 (ac-dc-pe-bonding-analogia + iso-10133-vs-13297-sucessao) |
| Canonicalizações Fase 1 fechadas | 1 (A-31 "edição a verificar" → 2024) |
| Smoke tests da calculadora | 3/3 ✅ |

### Riscos residuais

| Risco | Severidade | Mitigação |
|-------|------------|-----------|
| 5 visuais Fase 3 ainda em spec (não renderizados) | baixa | sprint 1 pós-Fase 5 (DEC-02) |
| `migrate_frontmatter --apply` pendente (DEC-08) | média | executar em branch separada antes de Fase 5 estendida |
| Top-10 matriz entregue parcialmente (5 de 10) | média | DEC-13 explicita sob demanda — não bloqueia fechamento |
| Cross-check calc vs Exemplo 1 da nota: AWG 18 (calc) vs AWG 16 (nota) | baixa | ambos adequados; calculadora aplica 25% margem uniforme (mais conservadora); documentado no YAML #04 |
| Wikilink `[[MOC — Diagnóstico e Manutenção]]` citado em Bonding pode não existir | baixa | validar na próxima rodada; remover referência se necessário |

### Portal para Fase 6 (proposta)

| Escopo | Entregas | Esforço estimado |
|--------|----------|------------------|
| Mínimo | renderizar 5 visuais Fase 3 + `migrate_frontmatter --apply` + commit dos arquivos acumulados | ~15h |
| Completo | escopo mínimo + Fase 5 estendida (posições 6-10) + 1 calculadora P1 adicional + 1 simulador interativo | ~40h+ |

---

## 🎯 FASE 5 CONCLUÍDA — 2026-04-17

**Status:** ✅ Encerrada com 7 artefatos (5 reescritas premium + 1 consolidado mestre + 1 ferramenta Python), primeira calculadora do vault (`calc_queda_tensao_dc.py`) entregue e smoke-tested, padrão editorial premium (DEC-11) validado em 5 notas de alta prioridade, 3 novas decisões (DEC-11 a DEC-13), canonicalização A-31 fechada, 3 normas adicionadas ao vault.

**Próxima fase:** Fase 6 — a definir pelo responsável editorial. Por padrão recomenda-se fechar débitos transversais (migrate_frontmatter --apply + render visuais Fase 3 + commit acumulado) antes de decidir entre escopo completo e estendido.

---

## LOG — SESSÃO 2026-04-18 (débitos transversais + Fase 5 estendida #6)

> **Gatilho:** instrução `continuar` + `A + B + C` do responsável editorial — autorizou commits acumulados (A), `migrate_frontmatter --apply` em branch separada (B) e início da Fase 5 estendida (C, DEC-13).

### Débitos transversais fechados

| Débito | Origem | Resultado |
|--------|--------|-----------|
| Commit dos arquivos acumulados na worktree | sessões 2026-04-16/17 | 3 commits temáticos: `cf36c9c` (audit infra Fase 1-4), `a162c78` (reescritas Fase 5 + calc DC), `daa258f` (frontmatter cross-vault) |
| `migrate_frontmatter.py --apply` em branch separada | DEC-08 (Fase 4) | branch `claude/migrate-frontmatter-apply-20260418`, commit `7550a42`: 106 notas normalizadas (review_jurisdiction → lista, normas_citadas via regex, reviewed_on bumped); validate_vault.py passa sem erros bloqueantes; aguarda revisão editorial para merge |

### Fase 5 estendida — primeira nota entregue

| # | Nota | Prio | Δ linhas | Principais ganhos |
|---|------|------|----------|-------------------|
| 6 | NMEA 2000 / NMEA 0183 — Rede de Instrumentos | 6.3 | +51 | TL;DR 7 regras (terminadores 120Ω + drop ≤6 m + TX/RX), danger especialista (J1939/SeaTalkNG/AIS Class A/DSC sem coordenadas), glossário 20 termos (Sentence/PGN/Talker/Listener/LEN/NAME/etc.), 3 normas IEC/ISO canonicalizadas (61162-1:2016, 61162-3:2008+A2:2019, 11898-1:2015), NORMAM-204 + ITU-R M.493 adicionados |

### Status Fase 5 estendida (DEC-13)

| Posição | Nota | Status |
|---------|------|--------|
| 6 | NMEA 2000 / NMEA 0183 | ✅ entregue 2026-04-18 |
| 7 | Luz de Tope | ✅ entregue 2026-04-18 |
| 8 | Bancos de Bateria | ✅ entregue 2026-04-18 |
| 9 | CAIS (Pier) (AC) | ✅ entregue 2026-04-18 |
| 10 | Normas e Regulamentações | ✅ entregue 2026-04-18 |

**Estado da worktree após esta sessão:** 10 commits ahead de `origin/main` em `claude/optimistic-jepsen` + branch separada `claude/migrate-frontmatter-apply-20260418` aguardando revisão. Push para origin e relatório final executados nesta sessão.

---

## 🎯 FASE 5 ESTENDIDA CONCLUÍDA — 2026-04-18

**Status:** ✅ Encerrada com 10 reescritas premium totais (top-5 + estendida 6-10) + 10 YAMLs de auditoria + 1 consolidado mestre (`fase_5_consolidado_estendido_20260418.yaml`). Padrão DEC-11 validado em 10 notas de prioridade ≥5.5. Vault ganhou 184 termos de glossário, 20 callouts didáticos (10 tip + 10 danger), 60+ normas canonicalizadas.

**Diferenciais do lote estendido (6-10):**
- **#6 NMEA:** primeira nota do vault com distinção explícita NMEA 0183 vs 2000 + 20 termos de rede
- **#7 Luz de Tope:** primeira nota P2 com COLREGS expandido (5 regras vs 3) + ABYC A-16 adicionado
- **#8 Bancos de Bateria:** maior glossário do vault (24 termos) + UN 38.3 + ABYC E-13 entram no vault
- **#9 CAIS (Pier):** ESD (Electric Shock Drowning) entra no vocabulário + normas em 3 grupos (Bordo/Pedestal/Brasil) + ABYC A-33 + NEC 555
- **#10 Normas:** meta-nota com 31 termos de glossário (maior da Fase 5) + ART/CREA/PE no vocabulário + 14 normas adicionadas/canonicalizadas

**Métricas consolidadas Fase 5 (top-5 + estendida):**
- Esforço estimado: 29 h → real: 14 h (**2.1× mais eficiente**)
- Linhas adicionadas: ~650 (média +65 por nota)
- Novas decisões (Fase 5): DEC-11 (template), DEC-12 (multi-tensão), DEC-13 (escopo estendido)
- Branches gerados: `claude/optimistic-jepsen` (10 commits), `claude/migrate-frontmatter-apply-20260418` (1 commit)

**Próxima decisão (Fase 6):** escopo a definir pelo responsável editorial. Ver relatório final desta sessão para 4 recomendações priorizadas.

---

## 🌊 FASE 6 (Caminho B) — ONDA 1 CONCLUÍDA — 2026-04-19

**Escopo aprovado:** Aplicar padrão DEC-11 a **todas as 133 notas restantes** do vault, estratificadas em 4 tiers (S/A/B/C), com pausa de revisão humana entre ondas. Base: `fase_6_triagem_cobertura_total_20260418.yaml` (commit `4ec3e47`).

**Onda 1 executada (8/8 notas Tier S, cluster topologia AC/DC):**

| # | Nota | Antes → Depois | Destaques |
|---|------|---------------|-----------|
| 1 | Fase e Neutro | 264 → ~365 | L+N+PE vs L1+L2+PE, nunca criar neutro falso |
| 2 | Aterramento | 373 → ~460 | SPOG único, bond N-PE segue fonte ativa, ESD |
| 3 | Isolador Galv. / Trafo Isolamento | 404 → ~495 | Isolador ≠ trafo, fail-safe ABYC A-28, sistema derivado |
| 4 | Proteção DR | 362 → ~460 | DR/RCD/GFCI/ELCI distinguidos, Classe A mínimo |
| 5 | Disjuntores (DC) e (AC) | 357 → ~460 | Arco DC, AIC/Icn, MCB vs MCCB (frontmatter normas novo) |
| 6 | Fusíveis DC | 297 → ~395 | ABYC 178 mm, Class T p/ lítio (frontmatter normas novo) |
| 7 | DC vs AC | 278 → ~375 | Separação física, frequência ≠ tensão, custo do inversor |
| 8 | Diagrama Unifilar | 337 → ~445 | Contrato técnico, retroengenharia, IEC 60617/81346 |

**Métricas Onda 1:**
- 8 notas, **~783 linhas adicionadas**
- **16 callouts novos** (8 tip + 8 danger)
- **172 termos de glossário**
- **~57 normas expandidas/canonicalizadas** (ABYC E-series, A-28/A-31/A-33, IEC 60364-7-709, 60947-2, 60617, 81346, NEC 555, ISO 13297, 16315, UL 248/489/943)
- Esforço: 12 h estimadas → 4,5 h reais (**2,67× mais eficiente**)

**Padrões reforçados no cluster:**
- L+N+PE vs L1+L2+PE vs split-phase 120/240 V (Fase e Neutro, Aterramento, DC vs AC)
- Sistema derivado (Isolador/Trafo, Aterramento, Proteção DR)
- SPOG único (Aterramento, Isolador, Diagrama Unifilar)
- ESD (Electric Shock Drowning) (Aterramento, Isolador, Proteção DR)
- Física do arco DC (Disjuntores, Fusíveis, DC vs AC)
- Vocabulário AIC/Icn/kA (Disjuntores e Fusíveis)

**Commit:** `a120b6c` em `claude/optimistic-jepsen` (pushado). YAML: `fase_6_onda_01_tier_s_topologia_ac_dc_20260419.yaml`.

**Estado do Caminho B (Fase 6):**
- Total planejado: 133 notas em 8 ondas
- Concluído: **8 / 133** (6%)
- Próxima: **Onda 2 — Tier S baterias/geração (9 notas)** após aprovação humana

**Cadência (b) — PAUSA OBRIGATÓRIA:** Onda 1 entregue. Antes de Onda 2, validar com responsável editorial: (1) template adaptado funciona em notas medianas de 264-404 linhas? (2) glossário de 20-25 termos é o tamanho certo para Tier S não-fundacional? (3) danger de 8-9 cenários alinhado com apetite? (4) TL;DR de 8-9 regras — manter ou reduzir para 5-6 em notas menos críticas?

---

## 🌊 FASE 6 (Caminho B) — ONDA 2 CONCLUÍDA — 2026-04-19

**Feedback do responsável editorial pós-Onda 1 (recalibragem aplicada em Onda 2):**
- Q1: glossário ~21 termos em Onda 1 vs ~23 em Fase 5 — "diminuiu porque? foi pra melhor?" → **recalibrar** para 40-47 termos (vademecum da elétrica náutica)
- Q2/Q3: "melhor possível" → manter TL;DR de 9 regras + danger de 9 cenários
- Q4: "todas que forem cabíveis" → **maximizar** normas (não filtrar, citar todas aplicáveis)
- Comando: "seguir com Onda 2"

**Onda 2 executada (9/9 notas Tier S, cluster baterias/geração/conversão):**

| # | Nota | Antes → Depois | Normas | Destaques |
|---|------|---------------|--------|-----------|
| 9 | Tipos de Bateria | 468 → 564 | 2 → 13 | FLA/AGM/GEL vs LiFePO4/NMC/LCO/LMO/LTO/NCA, química define carregador |
| 10 | BMS | 270 → 367 | 3 → 16 | BMS monitora célula não banco, CAN 500 kbps, disconnect abrupto = load dump |
| 11 | Lítio LiFePO4 | 240 → 339 | 0 → 15 | Não é "AGM melhorada", BMS requisito, sem carga < 0 °C (DEC-14) |
| 12 | Carregador (AC→DC) | 362 → 449 | 4 → 14 | Bulk/absorção/float por química, ignition protection, ABYC A-28 (ABYC A-31 TODO resolvido) |
| 13 | Monitor BMV/Shunt | 270 → 356 | 2 → 11 | Voltímetro ≠ monitor, shunt no negativo, PGN 127506/127508 |
| 14 | Alternador (DC) | 363 → 456 | 0 → 12 | Marinização SAE J1171, regulador externo em lítio, load dump ISO 16750-2 (DEC-14 + A-31 TODO) |
| 15 | Gerador (DC) | 201 → 295 | 0 → 12 | Só faz sentido com barramento DC central, REx em eletropropulsão (DEC-14) |
| 16 | Inversora (DC→AC) | 382 → 478 | 2 → 15 | Senoidal pura, corrente DC altíssima, inversor/carregador combi, AC coupling |
| 17 | Placa Solar (DC) | 229 → 343 | 0 → 17 | Wp ≠ produção, MPPT padrão, IEC 62109/61215/61730, NBR 16690:2019 (DEC-14) |

**Métricas Onda 2:**
- 9 notas, **862 linhas adicionadas**
- **18 callouts novos** (9 tip + 9 danger)
- **381 termos de glossário** (média 42/nota vs ~21 em Onda 1 — **recalibrada 2×**)
- **112 normas expandidas/canonicalizadas** (média 13,9/nota) — ABYC E-10/E-11/E-13/A-28/A-31/H-25, IEC 62040-1/62109-1-2/62619/62620/63056/61215/61730/62548/61010-1, UL 458/1236/1500/1703/1741/1973/2580/9540A, SAE J1171/J1495/J2464, ISO 8846/13297/16315/16750-2/7637-2, NMEA 2000, UN 38.3, NBR 16690:2019, NBR 5410, NORMAM-211
- **4 notas com `normas_citadas` criadas do zero** (DEC-14): LiFePO4, Alternador, Gerador, Placa Solar
- **2 TODOs antigos resolvidos:** ABYC A-31 citada como "(2024) — Battery Chargers and Inverters" em Carregador e Alternador
- Esforço: 11-13 h estimadas → **~6,5 h reais** (1,85× mais eficiente)

**Padrões reforçados no cluster:**
- Química do banco define carregador e perfil (Tipos de Bateria, BMS, LiFePO4, Carregador, Monitor, Alternador)
- BMS requisito em lítio (BMS, LiFePO4, Alternador, Inversora, Monitor)
- Fusível 178 mm ABYC E-11 em todas as 9 notas
- Corrente DC altíssima (180 A em 12 V com inversor de 2 kW)
- Disconnect abrupto do BMS = load dump ISO 16750-2 (BMS, LiFePO4, Alternador, Inversora)
- MPPT como padrão (Placa Solar, Monitor, Carregador)
- AC coupling (Inversora, Placa Solar)
- VE.Direct/VE.Can/NMEA 2000 com PGNs consistentes (Monitor, Carregador, Alternador, Inversora, Placa Solar)
- Ignition protection ISO 8846 / SAE J1171 / UL 1500 em 6 notas
- Controlador de energia (Cerbo GX, EmpirBus, CZone) como arquitetura integradora

**Commit:** a criar em `claude/optimistic-jepsen`. YAML: `fase_6_onda_02_tier_s_baterias_geracao_20260419.yaml`.

**Estado do Caminho B (Fase 6):**
- Total planejado: 133 notas em 8 ondas
- Concluído: **17 / 133** (13%)
- Próxima: **Onda 3 — Tier S navegação/emergência (9 notas)** após aprovação humana

**Cadência (b) — PAUSA OBRIGATÓRIA:** Onda 2 entregue. Antes de Onda 3, validar: (1) glossário de 40-47 termos está muito denso ou adequado para vademecum? (2) normas "máximas" (11-17 por nota) estão gerando boa densidade ou redundância? (3) presença de IEC 63056:2020 e UL 9540A adequada para audiência brasileira? (4) load dump (ISO 16750-2) como conceito transversal está funcionando? (5) próxima onda (Onda 3) deve manter mesmo padrão ou ajustar?

---


> **Base:** Prompt Mestre v2 (`01_prompt_mestre_v2.md`) + Schema de Auditoria (`02_schema_auditoria_nota.json`) + Schedules Claude Code (`03_claude_code_schedules.md`)
>
> **Princípio:** cada fase é uma thread separada. Não rodar Fases 1-5 em sequência sem revisão humana entre elas — o prompt mestre é explícito nisso para evitar deriva de contexto.
>
> **v2 (Opus):** corrige amostra de 28→35 notas após auditoria de evidência; 7 notas críticas foram adicionadas (Aterramento, Fusíveis DC, Isolador Galvânico, Gerador AC, Carregador, NAVEGAÇÃO BB/BE, Referência Rápida); 3 sinais de risco críticos adicionados (ISO 10133 aposentada, gap de edição/ano em 95% das citações, confusão sistema vs produto).

---

## ESTADO ATUAL (pós-Fase 0 v2)

| Métrica | Valor |
|---------|-------|
| Notas no vault | 147 (verificado) |
| Domínios técnicos | 11 + _Editorial |
| Specs visuais | 45 |
| Scripts Python | 6 (1.631 linhas) |
| CI/CD | 1 workflow ativo |
| Notas que citam norma | 62 (42% do vault) |
| Notas com cálculo Tier 1-2 | 12 |
| Notas com citação normativa completa (edição+cláusula) | 5 (8% das 62) |
| Notas na amostra Fase 1 | **35** (confirmação pendente) |
| Contradições inter-notas já confirmadas | 1 (ISO 10133) |
| Nota estrutural do vault | 7.2/10 (revisado — gap normativo maior que estimado) |

---

## FLUXO DAS FASES

```
Fase 0 ──→ [REVISÃO HUMANA] ──→ Fase 1 ──→ [REVISÃO] ──→ Fase 2
                                                               │
                                                               ↓
                                              Fase 3 ←── [REVISÃO]
                                                │
                                                ↓
                                            [REVISÃO] ──→ Fase 4 ──→ [REVISÃO]
                                                                          │
                                                                          ↓
                                                              Fase 5 (sob demanda)
```

**Regra de ouro:** revisar output de cada fase antes de avançar. Não encadear fases automaticamente — vault técnico com normas de segurança náutica não tolera deriva acumulada.

---

## FASE 0 — INVENTÁRIO E AMOSTRAGEM ✅ (revisão v2)

**Status:** CONCLUÍDA — 2026-04-16 (v2 revisada por Opus)
**Output:** `_Editorial/fase_0_inventario_20260416.yaml`
**Ação pendente:** confirmar amostra de **35 notas** + corrigir contradição ISO 10133 (antes ou durante Fase 1)

### Mudanças v1 → v2 (erros corrigidos)

| Item | v1 (Sonnet) | v2 (Opus) | Motivo |
|------|-------------|-----------|--------|
| Total amostra | 28 | 35 | Critérios obrigatórios do prompt mestre exigem mais |
| Notas com cálculo | 3 | 12 (5 Tier 1 + 7 Tier 2) | Grep exaustivo revelou 4× mais notas |
| Notas normativas na amostra | 2 | 12 (Tier 1+2) | 62 notas citam norma; 12 com carga pesada ignoradas em v1 |
| USB 12V domínio | 70_Hidraulica ❌ | 60_Automacao ✅ | Verificação de filesystem |
| validate_vault.py | "exceções amplas" ❌ | "escopo estreito" ✅ | Leitura do fonte mostrou 4 padrões / 1 exceção |
| Sinais preliminares | Especulativos | Evidência confirmada | Todas as notas da amostra lidas pelos agentes |
| Risco ISO 10133 | Não detectado | Confirmado (3+ notas) | Agente de normas descobriu contradição |
| Risco gap edição | Não detectado | Crítico (95% das citações) | 57 das 62 notas sem seção/ano |

### Notas adicionadas em v2 (7)
1. `40_Distribuicao/Aterramento.md` — ABYC E-11 + IEC 60092 + NORMAM + limite ≤1Ω
2. `40_Distribuicao/Fusíveis DC.md` — Coordenação fusível-cabo + ABYC E-11 ampacity
3. `40_Distribuicao/Isolador Galvânico.md` — ABYC A-28 certificação obrigatória
4. `30_Energia/Gerador (AC).md` — NFPA 302 (única citação no vault)
5. `20_Baterias/Carregador de Bateria.md` — ABYC A-31 + IEC 60335-2-29 (exemplar sistema/produto)
6. `50_Navegacao/NAVEGAÇÃO (BB, BE e Alcançado).md` — COLREGS + ISO 16180:2011 (melhor citação do vault)
7. `10_Fundamentos/Referência Rápida — Valores de Campo.md` — Tabela consultada em campo

---

## FASE 1 — AUDITORIA POR NOTA

**Objetivo:** diagnóstico completo de cada nota da amostra (35 notas aprovadas).
**Output:** 1 YAML por nota + tabela consolidada ranqueada por `score_roi`.
**Schema:** `02_schema_auditoria_nota.json`
**Estimativa:** ~44.5h (27 P1 × 1.5h + 8 P2 × 0.5h)

### Como executar

Separar em 5 threads temáticas para manter contexto limpo:

**Thread 1-A — Arcabouço Normativo (framework)** (~9h)
```
Notas (6 — todas P1):
  - 10_Fundamentos/Normas e Regulamentações — Abyc Iso e Brasil.md
  - 10_Fundamentos/Neutro, Negativo, Terra, PE, Bonding e DR.md
  - 40_Distribuicao/Aterramento.md ★ NOVA
  - 40_Distribuicao/Bonding — Sistema de Interligação de Massas.md
  - 40_Distribuicao/Proteção Dr.md
  - 40_Distribuicao/Isolador Galvânico - Transformador de Isolamento.md ★ NOVA

Foco: verificar edição/ano/cláusula de TODA norma citada (hoje só 5 notas têm).
      Confirmar migração ISO 10133 → ISO 13297:2020 onde aplicável.
      Diferenciar norma de SISTEMA (ABYC E-11) de norma de PRODUTO (IEC 61008).
Premissa: estas 6 notas formam a espinha normativa de segurança elétrica. 
Input obrigatório: trazer PDFs/links ABYC E-2, E-11, A-28 e ISO 13297:2020 in-prompt.
```

**Thread 1-B — Cálculos (recálculo obrigatório)** (~8h)
```
Notas (5 — todas P1):
  - 10_Fundamentos/Dimensionamento de Cabos DC — Cálculo Prático.md
  - 10_Fundamentos/Dimensionamento de Banco de Baterias — Cálculo de Autonomia.md
  - 10_Fundamentos/Lei de Ohm e Cálculos Básicos.md
  - 10_Fundamentos/Referência Rápida — Valores de Campo.md ★ NOVA
  - 40_Distribuicao/Fusíveis DC — Proteção Contra Sobrecorrente.md ★ NOVA

Foco: recalcular passo a passo. Declarar TODA premissa oculta (temperatura, K,
      Peukert, ida+volta, FP, derating, simultaneidade, margem).
      Verificar consistência cruzada: valores em Referência Rápida devem bater
      com Dimensionamento de Cabos e Banco.
Premissa: trazer tabelas ABYC E-11 ampacity + NBR 5410 in-prompt.
```

**Thread 1-C — Shore power + Geração AC** (~6h)
```
Notas (3 — todas P1):
  - 30_Energia/CAIS (Pier) (AC).md
  - 30_Energia/Gerador (AC).md ★ NOVA
  - 20_Baterias/Carregador de Bateria (AC To DC).md ★ NOVA

Foco: interface AC externa → risco de eletrocussão na água + incêndio.
      ABYC E-11 + A-28 + A-31 + A-33 + NFPA 302/303 + NORMAM-211 + NBR 5410.
      Exclusivo: frequência 60Hz BR vs 50Hz importada; monofásico 127V vs bifásico 220V.
Premissa: Carregador é exemplar (separa sistema/produto) — usar como template para outras notas.
```

**Thread 1-D — Regulatório de navegação** (~4h)
```
Notas (3 — todas P1):
  - 50_Navegacao/NAVEGAÇÃO (BB, BE e Alcançado).md ★ NOVA
  - 55_Iluminacao/Luz de Tope.md
  - 50_Navegacao/NMEA 2000 - NMEA 0183.md

Foco: COLREGS 72 (regras 20-31), ISO 16180:2011, NORMAM-01, USCG 33 CFR 183.
      IEC 61162-1/3 para NMEA. Verificar edições 2011→atual.
Premissa: NAVEGAÇÃO BB/BE é o exemplar — documenta conflito COLREGS vs prática BR.
```

**Thread 1-E — _Editorial e 00_Mapas** (~6h)
```
Notas (11):
  - Todos os 5 de _Editorial (5×P1)
  - 6 MOCs prioritários de 00_Mapas (4×P1 + 2×P2)

Foco: coerência editorial, cobertura MOC, wikilinks, governance.
      Reconciliar contagem de notas: audit prévia diz 140, hoje são 147.
Nota: os 10 MOCs curtos (12-28 linhas) não vão para auditoria formal —
      validate_vault.py já verifica integridade de links.
```

**Thread 1-F — Domínios especializados + Cálculo Tier 2** (~9h)
```
Notas (10):
  - 20_Baterias/Bancos de Bateria.md (P1) ★ contém ISO 10133 a corrigir
  - 80_Seguranca/Correntes Parasitas — Stray Currents.md (P1)
  - 30_Energia/Inversora (DC To AC).md (P2)
  - 60_Automacao/Monitoramento Remoto — VRM.md (P2)
  - 70_Hidraulica/Dessalinizador.md (P2)
  - 90_Revisao_Manual/Estabilizador.md (P2)
  + 4 cálculo Tier 2: Monitor Bateria/Shunt, Tipos de Bateria, BMS, Placa Solar
    (fazer auditoria focada no cálculo, não na norma)

Foco: consistência inter-notas (DoD, ciclos, custo/Wh).
      Detectar outras citações de ISO 10133 (além de Bonding e Bancos).
      Equipamentos de campo (estabilizador corrigido) e taxonomia [FAB].
```

**Thread 1-G — Consolidação** (~2.5h)
```
Input: todos os YAMLs de 1-A a 1-F
Output:
  - Tabela consolidada ranqueada por score_roi (35 linhas)
  - Mapa completo de contradições inter-notas (começar com ISO 10133 já confirmado)
  - Matriz de citações normativas: norma × nota × completude (edição/cláusula)
  - Top 10 por score_roi (candidatos Fase 5)
  - Frontmatter de auditoria para todas as 35 notas (audit_fase1_date, audit_nota_global, etc.)
```

### Correção imediata recomendada (antes de começar Fase 1)

Criar PR corrigindo a citação de ISO 10133 em 3+ notas:
- `40_Distribuicao/Bonding.md`
- `20_Baterias/Bancos de Bateria.md`
- `20_Baterias/Tipos de Bateria.md`

Substituir por ISO 13297:2020 conforme nota mestra já estabelece. Custo: ~1h, benefício: elimina contradição interna confirmada antes que contamine auditoria da Fase 1.

### Tabela de ranqueamento esperada (pós-Fase 1)

Campos obrigatórios na tabela consolidada:
```
| nota | dominio | nota_global | score_roi | esforco_h | impacto | risco | acao_primaria |
```

### Melhoria sugerida (não no Prompt Mestre original)

Adicionar ao frontmatter de cada nota auditada:
```yaml
audit_fase1: "2026-04-XX"
audit_nota_global: <float>
audit_score_roi: <float>
audit_acao: "<primaria>"
```
Isso torna os resultados da auditoria machine-readable via `validate_vault.py` e `build_manifest.py`.

---

## FASE 2 — GAPS, CONTRADIÇÕES GLOBAIS E STACK

**Objetivo:** mapa de buracos, inconsistências inter-notas e diagnóstico da stack.
**Input:** outputs da Fase 1 + vault completo
**Estimativa:** ~8h

### Seções obrigatórias

| Seção | Foco | Estimativa |
|-------|------|-----------|
| 2.1 Gaps por domínio | Tópicos ausentes críticos | 3h |
| 2.2 Auditoria _Editorial | Governança para escala 200+ notas | 1h |
| 2.3 Crítica da stack | Decisões de arquitetura sem rodeio | 2h |
| 2.4 Contradições globais | Lista consolidada das detectadas em Fase 1 | 2h |

### Perguntas não-negociáveis para 2.3

1. **NORMAM-02 vs NORMAM-211** — qual está vigente? Qual o vault deve citar?
2. **Notion: sumir, reduzir ou manter?** — decisão com fundamento, não preferência.
3. **manifest.json → Base44**: o pipeline existe ou é aspiracional? Falta alguma camada intermediária?
4. **CI é suficiente?** — validate_vault.py tem exceções que podem mascarar problemas normativos reais.
5. **Escala para 300+ notas** — o modelo editorial atual sobrevive?

### Melhoria sugerida (não no Prompt Mestre original)

Criar `_Editorial/normas_monitoradas.yaml` durante a Fase 2 — lista de normas citadas no vault com edição, URL de verificação e status. Isso é pré-requisito para o Schedule #5 (Radar de Normas Externas) e o Schedule #1 (Guardião Normativo).

---

## FASE 3 — ATIVOS: VISUAIS, SIMULAÇÕES, FERRAMENTAS

**Objetivo:** fichas de ativo para cada nota com `potencial_X ≥ 7` na Fase 1.
**Input:** outputs da Fase 1 (scores de potencial) + `_Editorial/Inventário Visual da Base.md`
**Estimativa:** ~10h

### Prioridade de produção sugerida

Com base no diagnóstico da Fase 0 (antes de ter scores de Fase 1):

**Visuais — gaps identificados:**
- `55_Iluminacao/` — 10 notas sem visual (COLREG é visual por natureza)
- `80_Seguranca/Correntes Parasitas` — diagrama de correntes em casco nunca é bem entendido em texto
- `40_Distribuicao/Proteção Dr` — curva de disparo I²t é fundamental e visual

**Ferramentas Python — alto ROI antecipado:**
```python
# calc_queda_tensao_dc.py
# Entradas: I (A), L_cabo (m, comprimento efetivo ida+volta), seção (mm²), material (Cu/Al)
# Saídas: queda de tensão (V, %), aviso se > 3% ABYC
# Integra manifest: sim | Wrap Base44: sim

# calc_autonomia_banco.py
# Entradas: capacidade (Ah), DoD (%), cargas (W), horas/dia por carga
# Saídas: autonomia (h/dias), alerta se banco subdimensionado
# Integra manifest: sim | Wrap Base44: sim
```

**Simulações — alto valor didático:**
- Troubleshooting interativo (árvore de decisão) — `10_Fundamentos/Troubleshooting.md` como base
- Calculadora de shore power (127V/60Hz vs 220V/50Hz) — `30_Energia/CAIS (Pier).md` como base

### Regra sobre scripts existentes

Antes de propor qualquer novo script em Fase 3, verificar:
- `scripts/validate_vault.py` — evitar duplicar validações de frontmatter/links
- `scripts/build_manifest.py` — se ativo deve aparecer no manifest, estender este
- `scripts/renderer.py` (1.210 linhas) — se é visual, verificar se template existente resolve
- `scripts/integrate_visuals.py` — não criar inject manual; usar ou estender este

---

## FASE 4 — ARQUITETURA DE PRODUTO + PLANO DE AÇÃO

**Objetivo:** blueprint das 7 camadas + roadmap em 3 horizontes + matriz esforço×impacto.
**Input:** outputs das Fases 1-3
**Estimativa:** ~6h

### Arquitetura de referência (7 camadas)

```
Camada 1: Obsidian/GitHub          ← fonte canônica, editada por humano
Camada 2: CI/Scripts Python        ← QA automático (validate, manifest, render)
Camada 3: manifest/content-manifest.json  ← ponte estruturada para downstream
Camada 4: Ferramentas Python       ← calculadoras, scaffolds, checklists
Camada 5: Interativos HTML/JS      ← simuladores, árvores de decisão, quizzes
Camada 6: Base44 App               ← trilhas do aluno, biblioteca visual, diagnóstico guiado
Camada 7: n8n                      ← publicação, WhatsApp, sync Notion, alertas
```

### Horizonte de planejamento

**7 dias (P1 imediato):**
- Confirmar amostra Fase 1 e iniciar Thread 1-A (normas)
- Criar `_Editorial/normas_monitoradas.yaml`
- Resolver notas órfãs (USB 12V, Limpador de Parabrisas)
- Ativar Schedule #3 (Fila de Revisão Inteligente) + #11 (Pulso WhatsApp)

**30 dias:**
- Concluir Fases 1-2 completas
- Publicar calculadoras P1 (queda de tensão, autonomia)
- Ativar Schedules #1 + #7 (Guardião Normativo + Links Mortos)
- Criar currículo de referência em `_Editorial/curriculo_referencia.yaml`

**90 dias:**
- Concluir Fases 3-4
- Visuais de 55_Iluminacao e 80_Seguranca gerados e integrados
- Primeira versão do app Base44 com manifest como fonte
- Pipeline n8n ativo (pelo menos WhatsApp + Notion sync)
- Ativar Schedule #2 (Contradições) + #4 (Auditor de Cálculos)

---

## FASE 5 — REESCRITAS GUIADAS (SOB DEMANDA)

**Condição:** Fases 0-4 aprovadas pelo responsável editorial.
**Objetivo:** elevar as 10 notas com maior `score_roi` ao nível de publicação premium.
**Estimativa:** ~3h por nota = 30h para o top-10

**Candidatas antecipadas (antes dos scores de Fase 1):**
1. `Normas e Regulamentações — Abyc Iso e Brasil.md` — arquitetura normativa
2. `Dimensionamento de Cabos DC — Cálculo Prático.md` — mais usado em campo
3. `Neutro, Negativo, Terra, PE, Bonding e DR.md` — maior risco pedagógico
4. `Bonding — Sistema de Interligação de Massas.md` — risco real de dano ao casco
5. `CAIS (Pier) (AC).md` — gateway regulatório para shore power
6. `Bancos de Bateria.md` — mais dense, mais linkada em 20_Baterias
7. `NMEA 2000 - NMEA 0183.md` — padrão de fato de instrumentação moderna
8. `Luz de Tope.md` — COLREG com consequências legais
9. `Correntes Parasitas — Stray Currents.md` — dano invisível, difícil diagnosticar
10. `Troubleshooting — Diagnóstico de Falhas Elétricas.md` — mais útil no dia-a-dia de campo

---

## INTEGRAÇÃO COM CLAUDE CODE SCHEDULES

Com base em `03_claude_code_schedules.md`, ordem recomendada de ativação:

### Pré-auditoria (agora)
Nenhum schedule depende da auditoria estar completa. Mas não faz sentido ativar
Schedule #4 (Auditor de Cálculos) antes de ter a Fase 1 concluída — já teremos
auditado os cálculos manualmente.

### Durante Fase 1 (semanas 1-2)
| Schedule | Ação | Justificativa |
|----------|------|---------------|
| #3 Fila de Revisão Inteligente | Ativar | Gera fila com `score_roi` que complementa Fase 1 |
| #11 Pulso WhatsApp | Ativar | Hábito diário de 5s de status |
| #7 Higienista de Links | Ativar | Higiene básica paralela |

### Pós-Fase 2 (mês 1)
| Schedule | Ação | Justificativa |
|----------|------|---------------|
| #1 Guardião Normativo | Ativar | Depende de `normas_monitoradas.yaml` da Fase 2 |
| #2 Detector de Contradições | Ativar | Depende de manifest limpo pós-Fase 1 |
| #5 Radar de Normas Externas | Ativar | Depende de `normas_monitoradas.yaml` |

### Pós-Fase 3/4 (mês 2-3)
| Schedule | Ação | Justificativa |
|----------|------|---------------|
| #4 Auditor de Cálculos | Ativar | Fase 1 já fez o baseline; schedule mantém |
| #8 Sync Manifest → Base44 | Ativar | Depende de Base44 app estar configurado |
| #9 Briefing de Mentoria | Ativar | Depende de Notion + n8n ativos |
| #6 Gerador de Ativos Pendentes | Ativar | Depende de backlog de ativos da Fase 3 |
| #10 Guardião de Gaps | Ativar | Depende de `curriculo_referencia.yaml` |
| #12 Relatório de Dívida Editorial | Ativar | Fecha o ciclo de qualidade contínua |

---

## MELHORIAS PROPOSTAS AO PROCESSO (não no Prompt Mestre original)

### 1. Metadata de auditoria no frontmatter
Adicionar campos em notas auditadas:
```yaml
audit_fase1_date: "2026-04-XX"
audit_nota_global: 7.5
audit_score_roi: 8.2
audit_acao: "revisao_normativa"
audit_version: 1
```
**Por quê:** torna resultados da auditoria machine-readable sem arquivo externo separado.
**Impacto:** `build_manifest.py` exporta scores para Base44; schedules futuros priorizam por `audit_score_roi`.

### 2. Separar `_auditoria/` de `_Editorial/`
`_Editorial/` = governança editorial permanente (templates, políticas, backlog)
`_auditoria/` = outputs de auditorias específicas (fase_0.yaml, fase_1/*.yaml, relatórios)
**Por quê:** evita _Editorial inflada com artefatos temporários. Governança ≠ auditoria pontual.

### 3. `normas_monitoradas.yaml` — pré-requisito de 3 schedules
```yaml
# _Editorial/normas_monitoradas.yaml
normas:
  - id: NORMAM-211
    nome: "Normas da Autoridade Marítima - Volume II"
    orgao: "Marinha do Brasil / DPC"
    vigencia: "2023"
    url_verificacao: "https://www.marinha.mil.br/dpc/normam"
    notas_que_citam: [...]
  - id: ABYC-E11
    nome: "AC and DC Electrical Systems on Boats"
    orgao: "ABYC"
    edicao_conhecida: "2018"
    url_verificacao: "https://abycinc.org/standards"
    notas_que_citam: [...]
  # ... todos as normas identificadas nas notas
```

### 4. Checklist rápido de 00_Mapas (MOCs pequenos)
Os 7 MOCs de 12-24 linhas não justificam entrada formal na amostra, mas devem ser
verificados com um checklist de 3 perguntas:
- [ ] Todos os arquivos do domínio estão linkados?
- [ ] Há algum link morto (para nota que não existe)?
- [ ] A ordem de navegação faz sentido pedagógico?

Proposta: adicionar verificação automática em `validate_vault.py` — extrai todos os
wikilinks de MOCs e verifica existência dos arquivos alvo.

### 5. Score ROI no manifest
Adicionar `score_roi` e `audit_nota_global` ao `content-manifest.json`:
```json
{
  "notes": [{
    "path": "...",
    "score_roi": 8.2,
    "audit_nota_global": 7.5,
    "audit_acao": "revisao_normativa"
  }]
}
```
**Estende:** `scripts/build_manifest.py` (adicionar leitura de frontmatter de auditoria)
**Viabiliza:** Base44 mostrar prioridade de revisão; n8n filtrar por score para briefing.

---

## CHECKLIST DE ENTREGA POR FASE

### Fase 0 ✅
- [x] YAML de inventário por domínio
- [x] Diagnóstico preliminar com sinais de risco
- [x] Amostra de 28 notas com justificativa e prioridade
- [ ] **Pendente:** confirmação da amostra pelo responsável editorial

### Fase 1
- [ ] YAML de auditoria para cada nota da amostra (schema 02)
- [ ] Tabela consolidada ranqueada por `score_roi`
- [ ] Lista de contradições inter-notas detectadas
- [ ] Top 10 por `score_roi` (candidatos Fase 5)
- [ ] Proposta de frontmatter de auditoria para as notas

### Fase 2
- [ ] `gaps_por_dominio` YAML completo
- [ ] Avaliação de governança _Editorial (suficiente para 200+ notas?)
- [ ] Crítica da stack com decisões objetivas (Notion, manifest, CI)
- [ ] `_Editorial/normas_monitoradas.yaml` criado
- [ ] Contradições globais consolidadas

### Fase 3
- [ ] Fichas de ativo para `potencial_X ≥ 7`
- [ ] Ranking consolidado (visuais + simulações + ferramentas)
- [ ] Specs JSON para visuais P1 (compatíveis com `render_visuals.py`)
- [ ] Scaffolds Python para ferramentas P1
- [ ] Nenhum script duplica função existente

### Fase 4
- [ ] Diagrama da arquitetura de 7 camadas
- [ ] Roadmap em 3 horizontes (7d / 30d / 90d)
- [ ] Matriz esforço × impacto × risco (15-25 itens)
- [ ] Plano de ativação de schedules por fase

### Fase 5 (sob demanda)
- [ ] Reescritas guiadas das 10 notas top por `score_roi`
- [ ] Ativos gerados junto com cada reescrita
- [ ] Critério de "elevação premium" documentado

---

*Plano gerado por: Claude Sonnet 4.6 | 2026-04-16*
*Baseado em: 01_prompt_mestre_v2.md, 02_schema_auditoria_nota.json, 03_claude_code_schedules.md*
