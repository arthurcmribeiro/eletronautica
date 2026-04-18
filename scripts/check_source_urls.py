"""Scanner de URLs nos campos `source_urls` das notas do vault.

Objetivo: detectar URLs quebradas, duplicadas ou inconsistentes nas
referências externas declaradas no frontmatter. Funciona em dois modos:

1. **offline** (padrão): apenas análise estática.
   - URLs duplicadas entre notas diferentes.
   - URLs mal formadas (sem esquema, sem host, caracteres suspeitos).
   - URLs com marcador TODO acidentalmente injetado (bug 0005).
   - Contagem por domínio (detecta concentração excessiva em um host).

2. **online** (`--check-online`): HEAD request em cada URL única,
   reporta HTTP != 2xx/3xx e erros de rede. Usa urllib da stdlib.
   Timeout curto (5s) e rate-limit básico (0.5s entre requisições).

Saída: `_Editorial/source_urls_<data>.md` — relatório para revisão.

Uso:
    python scripts/check_source_urls.py
    python scripts/check_source_urls.py --check-online
    python scripts/check_source_urls.py --domain abycinc.org
    python scripts/check_source_urls.py --dup-only

Dependências: stdlib.

Referências:
- `_Editorial/bugs_conhecidos.md` §5 (bug 0005 — URLs contaminadas)
- Fase 2 GG-02 (cadeia de fontes externas sem verificação)
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "_Editorial"
EXCLUDED_PARTS = {".git", ".obsidian", ".claude", "_visuals", "scripts"}

FRONTMATTER_RE = re.compile(r"(?s)^---\r?\n(.*?)\r?\n---")
URL_LINE_RE = re.compile(r'^\s*-\s*"?(https?://[^\s"]+)"?')
TODO_CONTAMINACAO_RE = re.compile(r"<!--\s*TODO-CITA")


@dataclass
class OcorrenciaURL:
    arquivo: Path
    url: str
    linha_num: int


@dataclass
class ResultadoHTTP:
    url: str
    status: int
    erro: str = ""


@dataclass
class Relatorio:
    ocorrencias: list[OcorrenciaURL] = field(default_factory=list)
    arquivos_varridos: int = 0
    urls_unicas: set[str] = field(default_factory=set)
    malformadas: list[OcorrenciaURL] = field(default_factory=list)
    contaminadas: list[OcorrenciaURL] = field(default_factory=list)
    resultados_http: list[ResultadoHTTP] = field(default_factory=list)


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


def extrair_source_urls(arquivo: Path) -> list[OcorrenciaURL]:
    texto = arquivo.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(texto)
    if not match:
        return []
    frontmatter = match.group(1)
    resultado: list[OcorrenciaURL] = []
    dentro_bloco = False
    for num, linha in enumerate(frontmatter.splitlines(), start=2):
        if linha.startswith("source_urls:"):
            dentro_bloco = True
            continue
        if dentro_bloco and linha and not linha.startswith(" "):
            dentro_bloco = False
        if not dentro_bloco:
            continue
        m = URL_LINE_RE.match(linha)
        if m:
            resultado.append(
                OcorrenciaURL(arquivo=arquivo, url=m.group(1), linha_num=num)
            )
    return resultado


def url_malformada(url: str) -> bool:
    try:
        parsed = urlparse(url)
    except ValueError:
        return True
    if parsed.scheme not in {"http", "https"}:
        return True
    if not parsed.netloc:
        return True
    # fragmentos suspeitos
    if " " in url or "\t" in url:
        return True
    return False


def checar_url_http(url: str, timeout: float = 5.0) -> ResultadoHTTP:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "eletronautica-audit/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return ResultadoHTTP(url=url, status=resp.status)
    except urllib.error.HTTPError as e:
        return ResultadoHTTP(url=url, status=e.code, erro=str(e.reason))
    except urllib.error.URLError as e:
        return ResultadoHTTP(url=url, status=0, erro=str(e.reason))
    except TimeoutError:
        return ResultadoHTTP(url=url, status=0, erro="timeout")
    except Exception as e:  # noqa: BLE001 — stdlib + timeout edge cases
        return ResultadoHTTP(url=url, status=0, erro=f"{type(e).__name__}: {e}")


def gerar_relatorio(
    rel: Relatorio,
    dup_only: bool,
    domain_filter: str,
    output: Path,
) -> None:
    hoje = dt.date.today().isoformat()
    # contagem por domínio
    dominios = Counter()
    por_url: dict[str, list[OcorrenciaURL]] = defaultdict(list)
    for oc in rel.ocorrencias:
        try:
            parsed = urlparse(oc.url)
            if parsed.netloc:
                dominios[parsed.netloc] += 1
        except ValueError:
            pass
        por_url[oc.url].append(oc)

    duplicadas = {url: ocs for url, ocs in por_url.items() if len(ocs) > 1}

    # filtro de domínio
    if domain_filter:
        rel.ocorrencias = [o for o in rel.ocorrencias if domain_filter in o.url]
        por_url = {url: ocs for url, ocs in por_url.items() if domain_filter in url}
        duplicadas = {url: ocs for url, ocs in duplicadas.items() if domain_filter in url}

    linhas = [
        "---",
        f'title: "Source URLs — Scanner ({hoje})"',
        'note_type: "editorial-report"',
        f'reviewed_on: "{hoje}"',
        "---",
        "",
        f"# Source URLs — Scanner ({hoje})",
        "",
        "Gerado por `scripts/check_source_urls.py`.",
        "",
        f"- Arquivos varridos: **{rel.arquivos_varridos}**",
        f"- URLs totais no frontmatter: **{len(rel.ocorrencias)}**",
        f"- URLs únicas: **{len(rel.urls_unicas)}**",
        f"- URLs duplicadas entre notas: **{len(duplicadas)}**",
        f"- URLs malformadas: **{len(rel.malformadas)}**",
        f"- URLs contaminadas por TODO (bug 0005): **{len(rel.contaminadas)}**",
        f"- Verificações HTTP: **{len(rel.resultados_http)}**",
        "",
    ]

    if rel.contaminadas:
        linhas.extend(["## URLs contaminadas por TODO (P0 — bug 0005)", ""])
        for oc in rel.contaminadas:
            rel_path = oc.arquivo.relative_to(ROOT)
            linhas.append(f"- `{rel_path}` L{oc.linha_num}: `{oc.url}`")
        linhas.append("")

    if rel.malformadas:
        linhas.extend(["## URLs malformadas (P1)", ""])
        for oc in rel.malformadas:
            rel_path = oc.arquivo.relative_to(ROOT)
            linhas.append(f"- `{rel_path}` L{oc.linha_num}: `{oc.url}`")
        linhas.append("")

    if duplicadas:
        linhas.extend(["## URLs duplicadas entre notas diferentes", ""])
        for url, ocs in sorted(duplicadas.items()):
            linhas.append(f"### `{url}` ({len(ocs)} ocorrências)")
            for oc in ocs:
                linhas.append(f"- `{oc.arquivo.relative_to(ROOT)}` L{oc.linha_num}")
            linhas.append("")

    if rel.resultados_http:
        linhas.extend(["## Resultados HTTP", ""])
        quebradas = [r for r in rel.resultados_http if r.status == 0 or r.status >= 400]
        linhas.append(f"- URLs com falha (status 0 ou ≥400): **{len(quebradas)}**")
        linhas.append("")
        for r in rel.resultados_http:
            marca = "OK" if 200 <= r.status < 400 else "FAIL"
            detalhe = f" — {r.erro}" if r.erro else ""
            linhas.append(f"- `[{marca} {r.status}]` `{r.url}`{detalhe}")
        linhas.append("")

    if not dup_only:
        linhas.extend(["## Concentração por domínio", ""])
        for dominio, total in dominios.most_common():
            linhas.append(f"- `{dominio}`: {total}")
        linhas.append("")

    output.write_text("\n".join(linhas) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-online", action="store_true",
                        help="executa HEAD request em cada URL única (rate-limited)")
    parser.add_argument("--domain", help="filtrar por substring de domínio")
    parser.add_argument("--dup-only", action="store_true",
                        help="exibir apenas duplicadas e contaminadas")
    parser.add_argument("--max-urls", type=int, default=200,
                        help="limite de URLs a checar online (default: 200)")
    parser.add_argument("--output", help="arquivo de saída (padrão: _Editorial/source_urls_<data>.md)")
    args = parser.parse_args()

    rel = Relatorio()
    for arquivo in note_files():
        rel.arquivos_varridos += 1
        for oc in extrair_source_urls(arquivo):
            rel.ocorrencias.append(oc)
            rel.urls_unicas.add(oc.url)
            if url_malformada(oc.url):
                rel.malformadas.append(oc)
            if TODO_CONTAMINACAO_RE.search(oc.url):
                rel.contaminadas.append(oc)

    if args.check_online:
        alvos = sorted(rel.urls_unicas)[: args.max_urls]
        print(f"Checando {len(alvos)} URLs online (rate-limit 0.5s)...")
        for i, url in enumerate(alvos, start=1):
            resultado = checar_url_http(url)
            rel.resultados_http.append(resultado)
            tag = "OK" if 200 <= resultado.status < 400 else "FAIL"
            print(f"  [{i}/{len(alvos)}] [{tag} {resultado.status}] {url}")
            time.sleep(0.5)

    hoje_compact = dt.date.today().isoformat().replace("-", "")
    output = Path(args.output) if args.output else OUTPUT_DIR / f"source_urls_{hoje_compact}.md"
    gerar_relatorio(rel, args.dup_only, args.domain or "", output)

    print(f"\nArquivos varridos: {rel.arquivos_varridos}")
    print(f"URLs totais: {len(rel.ocorrencias)}")
    print(f"URLs únicas: {len(rel.urls_unicas)}")
    print(f"URLs contaminadas: {len(rel.contaminadas)}")
    print(f"Relatório: {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
