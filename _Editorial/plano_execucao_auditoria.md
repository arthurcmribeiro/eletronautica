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
