"""Migra frontmatter das notas do vault para o padrão Fase 2 (DEC-05).

Transformações aplicadas:

1. `review_jurisdiction: "Brasil"` (escalar)
   -> lista YAML. Regra:
        "Brasil"        -> ["Brasil"]
        "internacional" -> ["internacional"]
        valor misto     -> lista com o valor original (revisao manual depois).

2. Acrescenta campo `normas_citadas` quando ausente, populado por varredura
   regex sobre o CORPO da nota (ignora frontmatter e URLs). Detecta:
        ABYC <LETRA>-<N>, ISO <N>, ABNT NBR <N>, NBR <N>, NORMAM-<N>,
        NORMAM <N>, IEC <N>, NFPA <N>, NMEA <N>, CFR <N>, COLREGS.
   A lista e registrada em ordem de primeira aparicao e dedup.

3. Atualiza `reviewed_on` para a data-alvo (padrao: hoje) APENAS quando
   alguma das mudancas acima for aplicada.

Comportamento:
- Padrao: dry-run. Emite relatorio em `_Editorial/frontmatter_migration_<data>.md`.
- `--apply`: escreve as mudancas em disco (um arquivo por vez).
- `--target YYYY-MM-DD`: sobrescreve data-alvo do reviewed_on.
- `--file <path>`: limita a um arquivo.

Design:
- Respeita bug 0005: regex nunca rasca URLs (filtra http/https/www.).
- Respeita normas retiradas: NAO popula ISO 10133 em `normas_citadas`
  (a menos que o CORPO cite claramente como "historico").
- Nao toca notas no diretorio excluido (scripts, _visuals, .claude).
- Nao mexe em aliases, seo_*, geo_* -- preserva ordem do frontmatter.

Uso:
    python scripts/migrate_frontmatter.py                       # dry-run
    python scripts/migrate_frontmatter.py --apply               # escreve
    python scripts/migrate_frontmatter.py --target 2026-04-17   # data custom
    python scripts/migrate_frontmatter.py --file "20_Baterias/Bancos de Bateria.md"

Dependencias: apenas stdlib.

Referencias:
- `_Editorial/fase_2_consolidado_20260417.yaml` (DEC-05)
- `_Editorial/fase_1_auditoria_rodada_09_20260417.yaml` (97 notas pendentes)
- `_Editorial/bugs_conhecidos.md` secao 5 (bug 0005, lookbehind em URLs)
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "_Editorial"
EXCLUDED_PARTS = {".git", ".obsidian", ".claude", "_visuals", "scripts"}

FRONTMATTER_RE = re.compile(r"(?s)^(---\r?\n)(.*?)(\r?\n---\r?\n?)(.*)$")

# Regex de normas — SEMPRE ancorada em boundary de palavra,
# e usada APENAS sobre linhas que não contêm URL (http/https/www.).
NORMAS_PATTERNS = [
    (re.compile(r"\bABYC\s+([A-Z])-(\d+)\b"), lambda m: f"ABYC {m.group(1)}-{m.group(2)}"),
    (re.compile(r"\bISO\s+(\d{3,5})(?::\s*(\d{4}))?"), lambda m: f"ISO {m.group(1)}" + (f":{m.group(2)}" if m.group(2) else "")),
    (re.compile(r"\bABNT\s+NBR\s+(\d{3,5})"), lambda m: f"ABNT NBR {m.group(1)}"),
    (re.compile(r"\bNBR\s+(\d{3,5})"), lambda m: f"NBR {m.group(1)}"),
    (re.compile(r"\bNORMAM[-\s](\d{2,4})"), lambda m: f"NORMAM-{m.group(1)}"),
    (re.compile(r"\bIEC\s+(\d{4,5})(?:-(\d+))?"), lambda m: f"IEC {m.group(1)}" + (f"-{m.group(2)}" if m.group(2) else "")),
    (re.compile(r"\bNFPA\s+(\d{2,4})"), lambda m: f"NFPA {m.group(1)}"),
    (re.compile(r"\bNMEA\s+(\d{3,5})"), lambda m: f"NMEA {m.group(1)}"),
    (re.compile(r"\b(\d{1,3})\s+CFR\s+(\d{1,4})"), lambda m: f"{m.group(1)} CFR {m.group(2)}"),
    (re.compile(r"\bCOLREGS\b"), lambda m: "COLREGS"),
]

# Normas retiradas — só podem aparecer em normas_citadas se o contexto for
# claramente histórico. Por padrão, migrate_frontmatter NÃO as inclui.
NORMAS_RETIRADAS = {"ISO 10133"}

URL_MARKERS = ("http://", "https://", "www.")


@dataclass
class MigrationPlan:
    arquivo: Path
    atual_jurisdiction: str = ""
    nova_jurisdiction: list[str] = field(default_factory=list)
    adicionar_normas_citadas: bool = False
    normas_detectadas: list[str] = field(default_factory=list)
    atual_reviewed_on: str = ""
    nova_reviewed_on: str = ""

    @property
    def precisa_migrar(self) -> bool:
        return bool(self.nova_jurisdiction) or self.adicionar_normas_citadas


@dataclass
class Relatorio:
    planos: list[MigrationPlan] = field(default_factory=list)
    arquivos_varridos: int = 0
    ja_migrados: int = 0

    @property
    def pendentes(self) -> list[MigrationPlan]:
        return [p for p in self.planos if p.precisa_migrar]


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


def split_frontmatter(texto: str) -> tuple[str, str, str, str] | None:
    """Retorna (abre, frontmatter_raw, fecha, body) ou None se não houver frontmatter."""
    texto = texto.lstrip("\ufeff")
    match = FRONTMATTER_RE.match(texto)
    if not match:
        return None
    return match.group(1), match.group(2), match.group(3), match.group(4)


def extrair_jurisdiction(frontmatter_raw: str) -> tuple[str, str]:
    """Detecta valor atual de review_jurisdiction.

    Retorna (forma_detectada, valor_texto):
        forma: "escalar" | "lista" | "ausente"
        valor: string para escalar, primeiro item para lista, "" para ausente.
    """
    linhas = frontmatter_raw.splitlines()
    for i, linha in enumerate(linhas):
        if not linha.startswith("review_jurisdiction:"):
            continue
        resto = linha.split(":", 1)[1].strip()
        if resto:
            # escalar direto na linha
            valor = resto
            if valor.startswith('"') and valor.endswith('"'):
                valor = valor[1:-1]
            return "escalar", valor
        # lista (próximas linhas começam com "  -")
        itens: list[str] = []
        for cont in linhas[i + 1:]:
            if cont.startswith("  - ") or cont.startswith("- "):
                v = cont.lstrip(" -").strip()
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                itens.append(v)
            elif cont and not cont.startswith(" "):
                break
        return "lista", itens[0] if itens else ""
    return "ausente", ""


def tem_normas_citadas(frontmatter_raw: str) -> bool:
    for linha in frontmatter_raw.splitlines():
        if linha.startswith("normas_citadas:"):
            return True
    return False


def extrair_reviewed_on(frontmatter_raw: str) -> str:
    for linha in frontmatter_raw.splitlines():
        if linha.startswith("reviewed_on:"):
            valor = linha.split(":", 1)[1].strip()
            if valor.startswith('"') and valor.endswith('"'):
                valor = valor[1:-1]
            return valor
    return ""


def detectar_normas(body: str) -> list[str]:
    """Varre body e retorna normas citadas, em ordem de primeira aparição, dedup.

    Ignora linhas que contêm URLs (bug 0005) e linhas dentro de blocos de código.
    """
    encontradas: list[str] = []
    vistas: set[str] = set()
    dentro_codeblock = False

    for linha in body.splitlines():
        stripped = linha.strip()
        if stripped.startswith("```"):
            dentro_codeblock = not dentro_codeblock
            continue
        if dentro_codeblock:
            continue
        if any(marcador in linha for marcador in URL_MARKERS):
            # pode ter citação fora da URL na mesma linha; tenta limpar URLs primeiro
            linha_limpa = re.sub(r"https?://\S+|www\.\S+", "", linha)
        else:
            linha_limpa = linha

        for regex, formatter in NORMAS_PATTERNS:
            for match in regex.finditer(linha_limpa):
                chave = formatter(match)
                if chave in NORMAS_RETIRADAS:
                    continue
                if chave not in vistas:
                    vistas.add(chave)
                    encontradas.append(chave)
    return encontradas


def planejar_migracao(arquivo: Path, target_date: str) -> MigrationPlan | None:
    """Constrói o plano de migração de uma nota. None se a nota for ignorada."""
    try:
        texto = arquivo.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None

    partes = split_frontmatter(texto)
    if partes is None:
        return None
    _, frontmatter_raw, _, body = partes

    plano = MigrationPlan(arquivo=arquivo)
    plano.atual_reviewed_on = extrair_reviewed_on(frontmatter_raw)

    # 1) Jurisdiction
    forma, valor = extrair_jurisdiction(frontmatter_raw)
    plano.atual_jurisdiction = f"{forma}:{valor}"
    if forma == "escalar" and valor:
        # heurística: se o valor é um par conhecido, expande; senão, lista unitária
        if valor.lower() == "brasil+internacional":
            plano.nova_jurisdiction = ["Brasil", "internacional"]
        else:
            plano.nova_jurisdiction = [valor]

    # 2) normas_citadas
    if not tem_normas_citadas(frontmatter_raw):
        normas = detectar_normas(body)
        if normas:
            plano.adicionar_normas_citadas = True
            plano.normas_detectadas = normas

    if plano.precisa_migrar:
        plano.nova_reviewed_on = target_date

    return plano


def aplicar_plano(plano: MigrationPlan) -> None:
    """Reescreve o frontmatter do arquivo conforme o plano."""
    texto = plano.arquivo.read_text(encoding="utf-8")
    partes = split_frontmatter(texto)
    if partes is None:
        return
    abre, frontmatter_raw, fecha, body = partes

    linhas = frontmatter_raw.splitlines()
    novas: list[str] = []
    i = 0
    inseriu_normas = False
    while i < len(linhas):
        linha = linhas[i]

        # reviewed_on
        if plano.nova_reviewed_on and linha.startswith("reviewed_on:"):
            novas.append(f'reviewed_on: "{plano.nova_reviewed_on}"')
            i += 1
            continue

        # review_jurisdiction
        if plano.nova_jurisdiction and linha.startswith("review_jurisdiction:"):
            novas.append("review_jurisdiction:")
            for v in plano.nova_jurisdiction:
                novas.append(f'  - "{v}"')
            # pular linhas subsequentes de lista antiga (indentadas ou "- ")
            j = i + 1
            while j < len(linhas) and (
                linhas[j].startswith("  - ")
                or linhas[j].startswith("- ")
                or (linhas[j].startswith(" ") and ":" not in linhas[j])
            ):
                j += 1
            # logo depois do bloco de jurisdiction, inserir normas_citadas se for o caso
            if plano.adicionar_normas_citadas and not inseriu_normas:
                novas.append("normas_citadas:")
                for n in plano.normas_detectadas:
                    novas.append(f'  - "{n}"')
                inseriu_normas = True
            i = j
            continue

        novas.append(linha)
        i += 1

    # se normas_citadas não foi inserida (ex: jurisdiction não mudou), insere antes de source_urls
    if plano.adicionar_normas_citadas and not inseriu_normas:
        inseridas_aqui: list[str] = []
        for linha in novas:
            if linha.startswith("source_urls:") or linha.startswith("aliases:"):
                inseridas_aqui.append("normas_citadas:")
                for n in plano.normas_detectadas:
                    inseridas_aqui.append(f'  - "{n}"')
                inseriu_normas = True
            inseridas_aqui.append(linha)
        if not inseriu_normas:
            # append ao final
            inseridas_aqui.append("normas_citadas:")
            for n in plano.normas_detectadas:
                inseridas_aqui.append(f'  - "{n}"')
        novas = inseridas_aqui

    novo_frontmatter = "\n".join(novas)
    novo_texto = abre + novo_frontmatter + fecha + body
    plano.arquivo.write_text(novo_texto, encoding="utf-8")


def gerar_relatorio(rel: Relatorio, target_date: str, output_path: Path) -> None:
    linhas = [
        "---",
        f'title: "Migração de Frontmatter — {target_date}"',
        'note_type: "editorial-report"',
        f'reviewed_on: "{target_date}"',
        "---",
        "",
        f"# Migração de Frontmatter — {target_date}",
        "",
        "Gerado por `scripts/migrate_frontmatter.py`.",
        "",
        f"- Arquivos varridos: **{rel.arquivos_varridos}**",
        f"- Já migrados (sem ação): **{rel.ja_migrados}**",
        f"- Pendentes de migração: **{len(rel.pendentes)}**",
        "",
        "## Escopo",
        "",
        "- `review_jurisdiction: \"escalar\"` -> lista YAML",
        "- Campo `normas_citadas` ausente -> populado via varredura regex do corpo",
        "- `reviewed_on` atualizado para a data-alvo quando alguma mudança for aplicada",
        "",
        "## Pendentes",
        "",
    ]

    if not rel.pendentes:
        linhas.append("_Nenhuma nota pendente. Vault alinhado ao padrão Fase 2._")
    else:
        for plano in rel.pendentes:
            rel_path = plano.arquivo.relative_to(ROOT)
            linhas.append(f"### `{rel_path}`")
            linhas.append("")
            if plano.nova_jurisdiction:
                linhas.append(
                    f"- `review_jurisdiction`: `{plano.atual_jurisdiction}` -> "
                    f"`{plano.nova_jurisdiction}`"
                )
            if plano.adicionar_normas_citadas:
                linhas.append(
                    f"- `normas_citadas`: adicionar **{len(plano.normas_detectadas)}** "
                    f"códigos: {', '.join('`' + n + '`' for n in plano.normas_detectadas)}"
                )
            if plano.nova_reviewed_on and plano.atual_reviewed_on != plano.nova_reviewed_on:
                linhas.append(
                    f"- `reviewed_on`: `{plano.atual_reviewed_on}` -> "
                    f"`{plano.nova_reviewed_on}`"
                )
            linhas.append("")

    output_path.write_text("\n".join(linhas) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply", action="store_true",
        help="aplica as mudanças em disco (padrão é dry-run)",
    )
    parser.add_argument(
        "--target", default=dt.date.today().isoformat(),
        help="data-alvo para reviewed_on (YYYY-MM-DD; padrão: hoje)",
    )
    parser.add_argument(
        "--file", help="limita a execução a um arquivo (caminho relativo ao vault)",
    )
    args = parser.parse_args()

    # validação da data
    try:
        dt.date.fromisoformat(args.target)
    except ValueError:
        print(f"ERRO: --target inválido (esperado YYYY-MM-DD): {args.target}")
        return 2

    arquivos = note_files()
    if args.file:
        arquivos = [ROOT / args.file]

    rel = Relatorio()
    for arquivo in arquivos:
        if not arquivo.exists():
            continue
        rel.arquivos_varridos += 1
        plano = planejar_migracao(arquivo, args.target)
        if plano is None:
            continue
        if plano.precisa_migrar:
            rel.planos.append(plano)
        else:
            rel.ja_migrados += 1
            rel.planos.append(plano)

    print(f"Arquivos varridos: {rel.arquivos_varridos}")
    print(f"Já migrados: {rel.ja_migrados}")
    print(f"Pendentes: {len(rel.pendentes)}")

    if args.apply:
        aplicados = 0
        for plano in rel.pendentes:
            aplicar_plano(plano)
            aplicados += 1
            print(f"  {plano.arquivo.relative_to(ROOT)}")
        print(f"\nAplicadas {aplicados} migrações.")
        return 0

    hoje_compact = args.target.replace("-", "")
    output = OUTPUT_DIR / f"frontmatter_migration_{hoje_compact}.md"
    gerar_relatorio(rel, args.target, output)
    print(f"\nRelatório: {output.relative_to(ROOT)}")
    print("Rodar com --apply para escrever as mudanças em disco.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
