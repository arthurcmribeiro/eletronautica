"""Gera o índice consolidado de uma Fase de auditoria do vault Eletronautica.

Varre os YAMLs de uma fase específica em `_Editorial/` e produz um índice em
markdown que agrega:

- Rodadas executadas (com data, escopo e resumo).
- Contagem de notas por prioridade detectada (P0/P1/P2).
- Contradições abertas vs. resolvidas no fim da fase.
- Links cruzados para os artefatos individuais.

Saída: `_Editorial/fase_<N>_indice.md`.

Uso:
    python scripts/generate_fase_indice.py --fase 1
    python scripts/generate_fase_indice.py --fase 2 --output _Editorial/outro_indice.md

Dependências: apenas stdlib (parser YAML minimal, compatível com o estilo
dos artefatos da auditoria — 2 espaços, chave: valor, listas com `-`).

Referências:
- `_Editorial/plano_execucao_auditoria.md`
- `_Editorial/fase_1_auditoria_rodada_09_20260417.yaml` (exemplo consolidado)
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EDITORIAL = ROOT / "_Editorial"

FILENAME_RE = re.compile(
    r"^fase_(?P<fase>\d+)_(?P<tipo>auditoria_rodada|gaps|governanca|fichas|consolidado|arquitetura|matriz_riscos|inventario)"
    r"(?:_(?P<rodada>\d{2}))?"
    r"(?:_[a-z_]+)?"        # sufixo arbitrario (ex: "_por_dominio", "_editorial")
    r"(?:_(?P<data>\d{8}))?"
    r"\.yaml$"
)

PRIORIDADE_RE = re.compile(r"\bprioridade:\s*[\"']?(P[012])\b", re.IGNORECASE)
SINAL_RE = re.compile(r"\btipo_sinal:\s*[\"']?(P[012])\b", re.IGNORECASE)
CONTRADICAO_RE = re.compile(r"contradic", re.IGNORECASE)


def artefatos_da_fase(fase: int) -> list[Path]:
    if not EDITORIAL.exists():
        return []
    return sorted(
        p for p in EDITORIAL.glob(f"fase_{fase}_*.yaml")
        if FILENAME_RE.match(p.name)
    )


def parse_data(data_compact: str) -> str:
    if not data_compact or len(data_compact) != 8:
        return ""
    try:
        return dt.date(
            int(data_compact[:4]),
            int(data_compact[4:6]),
            int(data_compact[6:]),
        ).isoformat()
    except ValueError:
        return ""


def extrair_top_level(yaml_texto: str, chave: str) -> str:
    """Extrai o valor escalar de uma chave top-level. '' se ausente."""
    padrao = re.compile(rf"^{re.escape(chave)}:\s*(.*)$", re.MULTILINE)
    match = padrao.search(yaml_texto)
    if not match:
        return ""
    valor = match.group(1).strip()
    if valor.startswith('"') and valor.endswith('"'):
        valor = valor[1:-1]
    return valor


def contar_prioridades(yaml_texto: str) -> dict[str, int]:
    contagem = {"P0": 0, "P1": 0, "P2": 0}
    for regex in (PRIORIDADE_RE, SINAL_RE):
        for match in regex.finditer(yaml_texto):
            chave = match.group(1).upper()
            contagem[chave] = contagem.get(chave, 0) + 1
    return contagem


def contar_contradicoes(yaml_texto: str) -> int:
    return len(CONTRADICAO_RE.findall(yaml_texto))


def resumo_rodada(arquivo: Path) -> dict[str, object]:
    texto = arquivo.read_text(encoding="utf-8")
    match = FILENAME_RE.match(arquivo.name)
    info: dict[str, object] = {
        "arquivo": arquivo.relative_to(ROOT).as_posix(),
        "nome": arquivo.name,
        "tipo": match.group("tipo") if match else "?",
        "rodada": match.group("rodada") if match else "",
        "data": parse_data(match.group("data") or ""),
        "titulo": extrair_top_level(texto, "titulo") or extrair_top_level(texto, "title"),
        "escopo": extrair_top_level(texto, "escopo"),
        "prioridades": contar_prioridades(texto),
        "contradicoes": contar_contradicoes(texto),
    }
    return info


def gerar_markdown(fase: int, resumos: list[dict[str, object]], output: Path) -> None:
    hoje = dt.date.today().isoformat()
    total_prio = {"P0": 0, "P1": 0, "P2": 0}
    total_contradicoes = 0
    for r in resumos:
        pr = r["prioridades"]
        assert isinstance(pr, dict)
        for k, v in pr.items():
            total_prio[k] = total_prio.get(k, 0) + int(v)
        total_contradicoes += int(r["contradicoes"])  # type: ignore[arg-type]

    linhas = [
        "---",
        f'title: "Fase {fase} — Índice Consolidado"',
        'note_type: "editorial-report"',
        f'reviewed_on: "{hoje}"',
        "---",
        "",
        f"# Fase {fase} — Índice Consolidado",
        "",
        f"Gerado por `scripts/generate_fase_indice.py` em {hoje}.",
        "",
        "## Totais agregados",
        "",
        f"- Artefatos da fase: **{len(resumos)}**",
        f"- Ocorrências P0: **{total_prio.get('P0', 0)}**",
        f"- Ocorrências P1: **{total_prio.get('P1', 0)}**",
        f"- Ocorrências P2: **{total_prio.get('P2', 0)}**",
        f"- Menções a contradições: **{total_contradicoes}**",
        "",
        "## Artefatos",
        "",
    ]

    for r in resumos:
        pr = r["prioridades"]
        assert isinstance(pr, dict)
        linhas.append(f"### `{r['arquivo']}`")
        linhas.append("")
        if r.get("titulo"):
            linhas.append(f"- **Título:** {r['titulo']}")
        if r.get("data"):
            linhas.append(f"- **Data:** {r['data']}")
        if r.get("rodada"):
            linhas.append(f"- **Rodada:** {r['rodada']}")
        if r.get("escopo"):
            linhas.append(f"- **Escopo:** {r['escopo']}")
        linhas.append(
            f"- **Prioridades:** P0={pr.get('P0', 0)}, "
            f"P1={pr.get('P1', 0)}, P2={pr.get('P2', 0)}"
        )
        linhas.append(f"- **Menções contradição:** {r['contradicoes']}")
        linhas.append("")

    output.write_text("\n".join(linhas) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fase", type=int, required=True, help="número da fase (1..5)")
    parser.add_argument("--output", help="arquivo de saída (padrão: _Editorial/fase_<N>_indice.md)")
    args = parser.parse_args()

    arquivos = artefatos_da_fase(args.fase)
    if not arquivos:
        print(f"Nenhum artefato encontrado para Fase {args.fase} em {EDITORIAL.relative_to(ROOT)}")
        return 1

    resumos = [resumo_rodada(a) for a in arquivos]

    output = Path(args.output) if args.output else EDITORIAL / f"fase_{args.fase}_indice.md"
    gerar_markdown(args.fase, resumos, output)
    print(f"Índice gerado: {output.relative_to(ROOT)}")
    print(f"  Artefatos processados: {len(resumos)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
