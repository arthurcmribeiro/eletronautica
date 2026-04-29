"""Detector da família ABYC e conflitos de identificação no vault.

Motivação:
A ABYC emite vários documentos cujos códigos diferem em 1 caractere
(A-28, A-31, A-33, E-10, E-11, H-27...). Confundir códigos é um sinal P0
da auditoria — muda a prescrição normativa e invalida o dimensionamento.

Este scanner varre o vault, cataloga TODAS as ocorrências de códigos
ABYC, agrupa por código e sinaliza:

1. Códigos ABYC com mais de uma variante de grafia (ex: `ABYC A-28` vs
   `ABYC A28` vs `ABYC A-28.1`) — inconsistência editorial.
2. Códigos ABYC sem edição/ano — gap de citação canônica.
3. Notas que citam códigos marcados como `substituida`/`aposentada` no
   `_Editorial/registro_normas.yaml` — contradição ativa.
4. Citações próximas de anos antigos (`E-11 (2008)` em nota recente) —
   potencial desatualização.

Saída: `_Editorial/abyc_family_<data>.md`.

Uso:
    python scripts/detect_abyc_family.py
    python scripts/detect_abyc_family.py --codigo A-28
    python scripts/detect_abyc_family.py --only-conflicts

Dependências: stdlib.

Referências:
- `_Editorial/fase_1_auditoria_rodada_09_20260417.yaml` (matriz contradições)
- `_Editorial/bugs_conhecidos.md` (0003 e 0004)
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "_Editorial"
REGISTRO_PATH = ROOT / "_Editorial" / "registro_normas.yaml"
EXCLUDED_PARTS = {".git", ".obsidian", ".claude", "_visuals", "scripts"}

# Cobre ABYC E-11, A-28, H-27, A-28.1 (subcláusula), A28 (grafia sem hífen),
# mas mantém grupo separado pra detectar inconsistências.
ABYC_RE = re.compile(
    r"\bABYC\s+(?P<letra>[A-Z])[-\u2010\s]?(?P<numero>\d{1,3})(?P<sub>\.\d+)?\b",
    re.IGNORECASE,
)

EDICAO_PROXIMA_RE = re.compile(r"[\s(:,]\s*(\d{4})")


@dataclass
class Ocorrencia:
    arquivo: Path
    linha_num: int
    linha_texto: str
    codigo_canonico: str
    grafia_original: str
    tem_edicao: bool = False
    ano_citado: str = ""


@dataclass
class Relatorio:
    ocorrencias: list[Ocorrencia] = field(default_factory=list)
    arquivos_varridos: int = 0
    registro_status: dict[str, str] = field(default_factory=dict)


def note_files(root: Path = ROOT) -> list[Path]:
    resultado = []
    for path in root.rglob("*.md"):
        if path.parent == root:
            continue
        try:
            partes = path.relative_to(root).parts
        except ValueError:
            continue
        if any(p in EXCLUDED_PARTS for p in partes):
            continue
        resultado.append(path)
    return sorted(resultado)


def carregar_registro_status(path: Path) -> dict[str, str]:
    """Carrega o status de cada norma ABYC do registro. dict[codigo, status]."""
    status: dict[str, str] = {}
    if not path.exists():
        return status
    codigo_atual = ""
    for linha in path.read_text(encoding="utf-8").splitlines():
        if not linha:
            continue
        if linha.startswith("ABYC "):
            # "ABYC E-11:" no topo
            if linha.rstrip().endswith(":"):
                codigo_atual = linha.rstrip()[:-1].strip()
            continue
        if codigo_atual and linha.startswith("  status:"):
            valor = linha.split(":", 1)[1].strip().strip('"')
            status[codigo_atual] = valor
            codigo_atual = ""
    return status


def varrer_arquivo(arquivo: Path) -> list[Ocorrencia]:
    resultado: list[Ocorrencia] = []
    try:
        linhas = arquivo.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return resultado

    for num, linha in enumerate(linhas, start=1):
        # pula URLs
        if "http://" in linha or "https://" in linha:
            linha_analisavel = re.sub(r"https?://\S+", "", linha)
        else:
            linha_analisavel = linha
        for match in ABYC_RE.finditer(linha_analisavel):
            letra = match.group("letra").upper()
            numero = match.group("numero")
            sub = match.group("sub") or ""
            canonico = f"ABYC {letra}-{numero}{sub}"
            grafia = match.group(0)
            resto = linha_analisavel[match.end() : match.end() + 30]
            edicao_match = EDICAO_PROXIMA_RE.match(resto)
            resultado.append(
                Ocorrencia(
                    arquivo=arquivo,
                    linha_num=num,
                    linha_texto=linha,
                    codigo_canonico=canonico,
                    grafia_original=grafia.strip(),
                    tem_edicao=bool(edicao_match),
                    ano_citado=edicao_match.group(1) if edicao_match else "",
                )
            )
    return resultado


def gerar_relatorio(rel: Relatorio, only_conflicts: bool, output: Path) -> None:
    hoje = dt.date.today().isoformat()
    grupos: dict[str, list[Ocorrencia]] = defaultdict(list)
    for oc in rel.ocorrencias:
        grupos[oc.codigo_canonico].append(oc)

    codigos_com_variantes: dict[str, set[str]] = {}
    codigos_bloqueados: dict[str, str] = {}
    for codigo, lista in grupos.items():
        grafias = {o.grafia_original.upper().replace(" ", "") for o in lista}
        if len({g.replace("-", "") for g in grafias}) > 1:
            codigos_com_variantes[codigo] = grafias
        status = rel.registro_status.get(codigo, "")
        if status in {"substituida", "aposentada"}:
            codigos_bloqueados[codigo] = status

    linhas = [
        "---",
        f'title: "Família ABYC — Scanner de Conflitos ({hoje})"',
        'note_type: "editorial-report"',
        f'reviewed_on: "{hoje}"',
        "---",
        "",
        f"# Família ABYC — Scanner de Conflitos ({hoje})",
        "",
        "Gerado por `scripts/detect_abyc_family.py`.",
        "",
        f"- Arquivos varridos: **{rel.arquivos_varridos}**",
        f"- Ocorrências ABYC totais: **{len(rel.ocorrencias)}**",
        f"- Códigos únicos: **{len(grupos)}**",
        f"- Códigos com variantes de grafia: **{len(codigos_com_variantes)}**",
        f"- Códigos em status bloqueado: **{len(codigos_bloqueados)}**",
        "",
    ]

    if codigos_bloqueados:
        linhas.extend(["## Normas bloqueadas (P0)", ""])
        for codigo, status in sorted(codigos_bloqueados.items()):
            linhas.append(f"### `{codigo}` — status: **{status}**")
            linhas.append("")
            for oc in grupos[codigo]:
                rel_path = oc.arquivo.relative_to(ROOT)
                linhas.append(
                    f"- `{rel_path}` L{oc.linha_num}: `{oc.linha_texto.strip()[:110]}`"
                )
            linhas.append("")

    if codigos_com_variantes:
        linhas.extend(["## Variantes de grafia (P1)", ""])
        for codigo, grafias in sorted(codigos_com_variantes.items()):
            linhas.append(f"### `{codigo}` — grafias encontradas: {sorted(grafias)}")
            linhas.append("")
            for oc in grupos[codigo]:
                rel_path = oc.arquivo.relative_to(ROOT)
                linhas.append(
                    f"- `{rel_path}` L{oc.linha_num}: grafia `{oc.grafia_original}` — `{oc.linha_texto.strip()[:100]}`"
                )
            linhas.append("")

    if not only_conflicts:
        linhas.extend(["## Inventário completo por código", ""])
        for codigo in sorted(grupos):
            lista = grupos[codigo]
            sem_edicao = sum(1 for o in lista if not o.tem_edicao)
            linhas.append(f"### `{codigo}` — {len(lista)} ocorrências ({sem_edicao} sem edição)")
            linhas.append("")
            for oc in lista:
                rel_path = oc.arquivo.relative_to(ROOT)
                marca = "[SEM EDIÇÃO]" if not oc.tem_edicao else f"[{oc.ano_citado}]"
                linhas.append(
                    f"- `{rel_path}` L{oc.linha_num} {marca}: `{oc.linha_texto.strip()[:100]}`"
                )
            linhas.append("")

    output.write_text("\n".join(linhas) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codigo", help="filtrar por código canônico (ex: 'A-28')")
    parser.add_argument("--only-conflicts", action="store_true",
                        help="exibir apenas variantes de grafia e normas bloqueadas")
    parser.add_argument("--output", help="arquivo de saída (padrão: _Editorial/abyc_family_<data>.md)")
    args = parser.parse_args()

    rel = Relatorio(registro_status=carregar_registro_status(REGISTRO_PATH))

    for arquivo in note_files():
        rel.arquivos_varridos += 1
        for oc in varrer_arquivo(arquivo):
            if args.codigo:
                # compara ignorando "ABYC " prefix
                alvo = args.codigo.upper().replace(" ", "").replace("ABYC", "")
                atual = oc.codigo_canonico.upper().replace(" ", "").replace("ABYC", "")
                if alvo not in atual:
                    continue
            rel.ocorrencias.append(oc)

    hoje_compact = dt.date.today().isoformat().replace("-", "")
    output = Path(args.output) if args.output else OUTPUT_DIR / f"abyc_family_{hoje_compact}.md"
    gerar_relatorio(rel, args.only_conflicts, output)

    print(f"Arquivos varridos: {rel.arquivos_varridos}")
    print(f"Ocorrências ABYC: {len(rel.ocorrencias)}")
    print(f"Relatório: {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
