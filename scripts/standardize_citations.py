"""Standardizer de citações normativas para o vault Eletronautica.

Lê `_Editorial/registro_normas.yaml` (fonte única de verdade) e varre
todas as notas do vault procurando citações de normas SEM edição/ano.
Gera um relatório de sugestões em `_Editorial/citation_patches_<data>.md`
para revisão humana.

NÃO aplica mudanças automaticamente. O relatório é a fonte de trabalho;
após revisão, o responsável aplica os patches manualmente ou com
`--apply` (modo interativo, confirmação arquivo-por-arquivo).

Uso:
    python scripts/standardize_citations.py                 # dry-run, gera relatório
    python scripts/standardize_citations.py --apply         # interativo
    python scripts/standardize_citations.py --norm "ABYC E-11"  # só uma norma
    python scripts/standardize_citations.py --file <path>   # só um arquivo

Dependências: apenas stdlib (sem PyYAML).

Design:
- Não augmenta validate_vault.py — é script independente.
- Convenção de citação: ver _Editorial/convencao_citacao_normativa.md
- Bloqueia normas com status `substituida` ou `aposentada` (reporta
  como erro, não como sugestão).
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRO_PATH = ROOT / "_Editorial" / "registro_normas.yaml"
OUTPUT_DIR = ROOT / "_Editorial"
EXCLUDED_PARTS = {".git", ".obsidian", ".claude", "_visuals", "_Editorial", "scripts"}

# Padrões reconhecidos como "citação já com edição":
#   ABYC E-11 (2023)
#   ABYC E-11 (2023), §11.4
#   ISO 13297:2020
#   NORMAM-211/DPC (2022)
#   ABNT NBR 5410 (2004, Emenda 1:2008)
EDICAO_RE = re.compile(
    r"""
    \s*                                  # espaço opcional
    (?:
        \(\s*\d{4}[^)]*\)                # (2023) ou (2004, Emenda 1:2008)
        |
        :\s*\d{4}                        # :2020
        |
        ,\s*\d{4}                        # , 2023  (forma plana dentro de parênteses)
        |
        ,\s*edi[cç][aã]o\s+a\s+verificar # , edição a verificar
        |
        \(\s*edi[cç][aã]o\s+a\s+verificar\s*\)   # (edição a verificar)
        |
        <!--\s*TODO-CITA                 # marcador TODO explícito
    )
    """,
    re.VERBOSE | re.IGNORECASE,
)

# Marcador explícito de "edição a verificar" — aceita com ou sem parênteses
PLACEHOLDER_RE = re.compile(r"[,\s(]*edi[cç][aã]o\s+a\s+verificar", re.IGNORECASE)


@dataclass
class Norma:
    codigo: str
    titulo_completo: str = ""
    edicao_vigente: str = ""
    status: str = "desconhecido"
    substituida_por: str = ""
    observacao: str = ""

    @property
    def citacao_canonica(self) -> str:
        """Formato canônico conforme convencao_citacao_normativa.md."""
        if not self.edicao_vigente:
            return f"{self.codigo} (edição a verificar)"
        # Evita parênteses aninhados
        edicao_limpa = self.edicao_vigente.replace("(", "").replace(")", "").strip()
        # ISO: dois-pontos; resto: parênteses
        if self.codigo.startswith("ISO "):
            return f"{self.codigo}:{edicao_limpa}"
        return f"{self.codigo} ({edicao_limpa})"

    @property
    def bloqueada(self) -> bool:
        return self.status in {"substituida", "aposentada"}


@dataclass
class Sugestao:
    arquivo: Path
    linha_num: int
    linha_texto: str
    norma: Norma
    tipo: str  # "falta_edicao" | "bloqueada"
    sugestao_texto: str = ""


@dataclass
class Relatorio:
    sugestoes_falta_edicao: list[Sugestao] = field(default_factory=list)
    sugestoes_bloqueadas: list[Sugestao] = field(default_factory=list)
    arquivos_varridos: int = 0
    normas_carregadas: int = 0


def parse_registro_minimal(path: Path) -> dict[str, Norma]:
    """Parser mínimo de registro_normas.yaml.

    Suporta apenas a estrutura esperada:
        CODIGO DA NORMA:
          campo: "valor"
          campo2: valor_sem_aspas
    """
    if not path.exists():
        sys.exit(f"ERRO: registro não encontrado em {path}")

    normas: dict[str, Norma] = {}
    current_codigo: str | None = None
    current_campos: dict[str, str] = {}

    def flush():
        nonlocal current_codigo, current_campos
        if current_codigo and not current_codigo.startswith(("_", "meta")):
            normas[current_codigo] = Norma(
                codigo=current_codigo,
                titulo_completo=current_campos.get("titulo_completo", ""),
                edicao_vigente=current_campos.get("edicao_vigente", ""),
                status=current_campos.get("status", "desconhecido"),
                substituida_por=current_campos.get("substituida_por", ""),
                observacao=current_campos.get("observacao", ""),
            )
        current_codigo = None
        current_campos = {}

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        # Comentário ou vazio
        stripped = raw_line.rstrip()
        if not stripped or stripped.lstrip().startswith("#"):
            continue

        # Linha de bloco pipe `|` (multiline) — ignoramos valor multiline neste parser minimal
        if stripped.endswith("|") or stripped.endswith(">"):
            continue

        # Top-level key (não indentado): começa norma nova
        if not raw_line.startswith(" "):
            if stripped.endswith(":"):
                flush()
                current_codigo = stripped[:-1].strip()
            continue

        # Campo indentado (2 espaços)
        match = re.match(r"^  ([a-z_][a-z0-9_]*):\s*(.*)$", raw_line)
        if match and current_codigo:
            campo, valor = match.group(1), match.group(2).strip()
            # Remove aspas
            if valor.startswith('"') and valor.endswith('"'):
                valor = valor[1:-1]
            current_campos[campo] = valor

    flush()
    return normas


def note_files(root: Path = ROOT) -> list[Path]:
    resultado = []
    for path in root.rglob("*.md"):
        if path.parent == root:
            continue
        try:
            partes_relativas = path.relative_to(root).parts
        except ValueError:
            continue
        if any(p in EXCLUDED_PARTS for p in partes_relativas):
            continue
        resultado.append(path)
    return sorted(resultado)


def build_regex_para_norma(codigo: str) -> re.Pattern[str]:
    """Regex que casa o código da norma como palavra.

    Usa lookahead negativo para evitar casar quando já há edição adjacente.
    Casa:
        'ABYC E-11'          → sim (sugere edição)
        'ABYC E-11 (2023)'   → não casa (já tem edição)
        'ABYC E-110'         → não casa (seguido de dígito)
    """
    codigo_escaped = re.escape(codigo)
    # (?![-\w]): próximo char não é letra/dígito/hífen
    # Depois captura espaço + conteúdo até fim da citação, para decidir
    return re.compile(rf"\b{codigo_escaped}(?![-\w])", re.IGNORECASE)


def varrer_arquivo(
    arquivo: Path,
    normas: dict[str, Norma],
    filtro_norma: str | None = None,
) -> list[Sugestao]:
    sugestoes: list[Sugestao] = []
    try:
        linhas = arquivo.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return sugestoes

    for num, linha in enumerate(linhas, start=1):
        for codigo, norma in normas.items():
            if filtro_norma and codigo != filtro_norma:
                continue
            regex = build_regex_para_norma(codigo)
            for match in regex.finditer(linha):
                # O que vem depois do código?
                resto = linha[match.end() :]
                tem_edicao = bool(EDICAO_RE.match(resto) or PLACEHOLDER_RE.match(resto.strip()))

                if norma.bloqueada:
                    # Exceção: nota mestre pode citar como histórico
                    if "_Editorial" in str(arquivo) or "Normas e Regulamentações" in str(arquivo):
                        continue
                    # Contexto histórico autorizado: linha já explica a transição
                    linha_lower = linha.lower()
                    contexto_historico = any(
                        marcador in linha_lower
                        for marcador in (
                            "retirada", "retirado", "aposentada", "aposentado",
                            "substitui", "sucede", "sucedeu", "hist\u00f3ric",
                            "não citar", "nao citar", "n\u00e3o citar",
                            "migr", "foi retirada",
                        )
                    )
                    if contexto_historico:
                        continue
                    sugestoes.append(
                        Sugestao(
                            arquivo=arquivo,
                            linha_num=num,
                            linha_texto=linha,
                            norma=norma,
                            tipo="bloqueada",
                            sugestao_texto=(
                                f"NORMA BLOQUEADA ({norma.status}). "
                                f"Substituir por: {norma.substituida_por or '(ver registro)'}."
                            ),
                        )
                    )
                elif not tem_edicao:
                    sugestoes.append(
                        Sugestao(
                            arquivo=arquivo,
                            linha_num=num,
                            linha_texto=linha,
                            norma=norma,
                            tipo="falta_edicao",
                            sugestao_texto=(
                                f"Substituir '{codigo}' por '{norma.citacao_canonica}' "
                                f"(status: {norma.status})"
                            ),
                        )
                    )
    return sugestoes


def gerar_relatorio_markdown(rel: Relatorio, output_path: Path) -> None:
    hoje = dt.date.today().isoformat()
    linhas = [
        "---",
        f"title: \"Patches de Citação Normativa — {hoje}\"",
        "note_type: \"editorial-report\"",
        f"reviewed_on: \"{hoje}\"",
        "---",
        "",
        f"# Patches de Citação Normativa — {hoje}",
        "",
        f"Gerado por `scripts/standardize_citations.py` a partir de `_Editorial/registro_normas.yaml`.",
        "",
        f"- Arquivos varridos: **{rel.arquivos_varridos}**",
        f"- Normas carregadas do registro: **{rel.normas_carregadas}**",
        f"- Sugestões de edição faltante: **{len(rel.sugestoes_falta_edicao)}**",
        f"- Alertas de norma bloqueada (retirada/substituída): **{len(rel.sugestoes_bloqueadas)}**",
        "",
        "## Convenção",
        "",
        "Ver `_Editorial/convencao_citacao_normativa.md`. Formato canônico:",
        "",
        "```",
        "ORGANISMO CÓDIGO (EDIÇÃO/ANO), cláusula",
        "```",
        "",
        "## Normas bloqueadas (prioridade P0/P1)",
        "",
    ]

    if not rel.sugestoes_bloqueadas:
        linhas.append("_Nenhuma ocorrência. Limpo._")
    else:
        agrupado: dict[Path, list[Sugestao]] = {}
        for s in rel.sugestoes_bloqueadas:
            agrupado.setdefault(s.arquivo, []).append(s)
        for arq, sugs in sorted(agrupado.items()):
            rel_path = arq.relative_to(ROOT)
            linhas.append(f"### `{rel_path}`")
            linhas.append("")
            for s in sugs:
                linhas.append(f"- **L{s.linha_num}** — norma `{s.norma.codigo}` ({s.norma.status})")
                linhas.append(f"  - Linha: `{s.linha_texto.strip()[:120]}`")
                linhas.append(f"  - Ação: {s.sugestao_texto}")
                linhas.append("")

    linhas.extend(["", "## Falta edição/ano", ""])

    if not rel.sugestoes_falta_edicao:
        linhas.append("_Nenhuma ocorrência. Todas as citações têm edição._")
    else:
        agrupado = {}
        for s in rel.sugestoes_falta_edicao:
            agrupado.setdefault(s.arquivo, []).append(s)
        for arq, sugs in sorted(agrupado.items()):
            rel_path = arq.relative_to(ROOT)
            linhas.append(f"### `{rel_path}` ({len(sugs)} sugestões)")
            linhas.append("")
            for s in sugs:
                trecho = s.linha_texto.strip()
                if len(trecho) > 100:
                    trecho = trecho[:100] + "…"
                linhas.append(f"- **L{s.linha_num}** — `{s.norma.codigo}` → `{s.norma.citacao_canonica}`")
                linhas.append(f"  - `{trecho}`")
            linhas.append("")

    output_path.write_text("\n".join(linhas), encoding="utf-8")


def _aplicar_em_arquivo(arquivo: Path, sugestoes_arquivo: list[Sugestao]) -> int:
    """Aplica substituições em um arquivo. Retorna número de substituições."""
    texto = arquivo.read_text(encoding="utf-8")
    aplicados = 0

    # Agrupa por norma (mesmo código pode aparecer N vezes no arquivo)
    por_norma: dict[str, Norma] = {s.norma.codigo: s.norma for s in sugestoes_arquivo}

    for codigo, norma in por_norma.items():
        regex = build_regex_para_norma(codigo)

        linhas = texto.splitlines(keepends=True)
        novas = []
        for linha in linhas:
            def _replace_linha(match: re.Match[str]) -> str:
                nonlocal aplicados
                pos_start = match.start()
                pos_end = match.end()
                resto = linha[pos_end : pos_end + 40]
                # Já tem edição depois (ex: "ABYC E-11 (2023)") — pula
                if EDICAO_RE.match(resto) or PLACEHOLDER_RE.match(resto.strip()):
                    return match.group(0)
                # Norma bloqueada em contexto histórico — pula
                if norma.bloqueada:
                    linha_lower = linha.lower()
                    if any(m in linha_lower for m in (
                        "retirada", "aposentada", "substitui", "sucede",
                        "histórico", "historic", "não citar", "nao citar",
                        "migr",
                    )):
                        return match.group(0)

                # Código já está entre parênteses: aplica formato plano para evitar aninhamento
                # Ex: "## Tabela (ABYC E-11)" → "## Tabela (ABYC E-11, 2023)"
                char_antes = linha[pos_start - 1] if pos_start > 0 else ""
                # olha para o próximo `)` depois do código
                resto_ate_fim = linha[pos_end:]
                idx_paren_fecha = resto_ate_fim.find(")")
                idx_nova_abre = resto_ate_fim.find("(")
                dentro_de_parenteses = (
                    char_antes == "("
                    and idx_paren_fecha != -1
                    and (idx_nova_abre == -1 or idx_paren_fecha < idx_nova_abre)
                )

                aplicados += 1
                if dentro_de_parenteses:
                    # formato plano: "ABYC E-11, 2023" ou "ISO 13297, 2020"
                    if norma.edicao_vigente:
                        edicao = norma.edicao_vigente.replace("(", "").replace(")", "").strip()
                        return f"{codigo}, {edicao}"
                    return f"{codigo}, edição a verificar"
                return norma.citacao_canonica

            nova = regex.sub(_replace_linha, linha)
            novas.append(nova)
        texto = "".join(novas)

    if aplicados:
        arquivo.write_text(texto, encoding="utf-8")
    return aplicados


def aplicar_interativo(rel: Relatorio) -> int:
    aplicados_total = 0
    agrupado: dict[Path, list[Sugestao]] = {}
    for s in rel.sugestoes_falta_edicao:
        agrupado.setdefault(s.arquivo, []).append(s)

    for arq, sugs in sorted(agrupado.items()):
        rel_path = arq.relative_to(ROOT)
        print(f"\n=== {rel_path} ({len(sugs)} sugestões) ===")
        for s in sugs[:5]:
            print(f"  L{s.linha_num}: {s.norma.codigo} → {s.norma.citacao_canonica}")
        if len(sugs) > 5:
            print(f"  ... e mais {len(sugs) - 5}")
        resp = input("Aplicar todas desta nota? [s/n/q] ").strip().lower()
        if resp == "q":
            break
        if resp != "s":
            continue
        n = _aplicar_em_arquivo(arq, sugs)
        aplicados_total += n
        print(f"  → {n} substituições aplicadas")
    return aplicados_total


def aplicar_em_massa(rel: Relatorio) -> int:
    """Aplica TODAS as sugestões sem prompt. Usar após revisão do relatório."""
    aplicados_total = 0
    agrupado: dict[Path, list[Sugestao]] = {}
    for s in rel.sugestoes_falta_edicao:
        agrupado.setdefault(s.arquivo, []).append(s)

    for arq, sugs in sorted(agrupado.items()):
        n = _aplicar_em_arquivo(arq, sugs)
        aplicados_total += n
        if n:
            print(f"  {arq.relative_to(ROOT)}: {n}")
    return aplicados_total


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="modo interativo de aplicação")
    parser.add_argument("--apply-all", action="store_true", help="aplica TODAS as sugestões sem perguntar (use com cuidado)")
    parser.add_argument("--norm", help="filtrar por código de norma (ex: 'ABYC E-11')")
    parser.add_argument("--file", help="filtrar por arquivo (caminho relativo ao vault)")
    args = parser.parse_args()

    normas = parse_registro_minimal(REGISTRO_PATH)
    rel = Relatorio(normas_carregadas=len(normas))

    arquivos = note_files()
    if args.file:
        arquivos = [ROOT / args.file]

    for arq in arquivos:
        if not arq.exists():
            continue
        rel.arquivos_varridos += 1
        for s in varrer_arquivo(arq, normas, filtro_norma=args.norm):
            if s.tipo == "bloqueada":
                rel.sugestoes_bloqueadas.append(s)
            else:
                rel.sugestoes_falta_edicao.append(s)

    print(f"Arquivos varridos: {rel.arquivos_varridos}")
    print(f"Normas carregadas: {rel.normas_carregadas}")
    print(f"Sugestões falta-edição: {len(rel.sugestoes_falta_edicao)}")
    print(f"Alertas norma bloqueada: {len(rel.sugestoes_bloqueadas)}")

    if args.apply:
        aplicados = aplicar_interativo(rel)
        print(f"\nAplicados: {aplicados} substituições")
        return 0

    if args.apply_all:
        print("\n--apply-all: aplicando TODAS as sugestões...")
        aplicados = aplicar_em_massa(rel)
        print(f"\nAplicados: {aplicados} substituições em {rel.arquivos_varridos} arquivos")
        return 0

    hoje = dt.date.today().isoformat().replace("-", "")
    output = OUTPUT_DIR / f"citation_patches_{hoje}.md"
    gerar_relatorio_markdown(rel, output)
    rel_path = output.relative_to(ROOT)
    print(f"\nRelatório: {rel_path}")
    print("Revisar e rodar com --apply (interativo) ou --apply-all (em massa).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
