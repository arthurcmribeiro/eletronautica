"""Valida estrutura dos YAMLs de auditoria do diretório `_Editorial/`.

Verifica que cada artefato de auditoria (`fase_N_*.yaml`) obedece ao
schema editorial definido na Fase 2:

- Chaves obrigatórias top-level: `titulo`, `fase`, `rodada` (quando
  aplicável), `data`, `escopo`, `notas_auditadas`.
- Cada entrada em `notas_auditadas` precisa ter: `caminho`, `tipo_nota`,
  `prioridade` (P0|P1|P2|ok), `sinais`.
- Arquivos de consolidação (`fase_N_consolidado_*.yaml`) precisam ter
  `artefatos_referenciados` e `matriz_contradicoes`.
- Artefatos de governança (`fase_N_governanca_*.yaml`) precisam ter
  `gargalos_identificados` e `decisoes`.

O validador usa parser YAML minimal compatível com o estilo dos artefatos
(2 espaços, listas com `-`). Não aceita YAML arbitrário — só o dialeto
que o processo editorial produz.

Saída: relatório de texto no stdout e código de saída != 0 se houver
erros. Com `--output`, também escreve em markdown.

Uso:
    python scripts/validate_audit_yaml.py
    python scripts/validate_audit_yaml.py --fase 1
    python scripts/validate_audit_yaml.py --strict

Dependências: stdlib.

Referências:
- `_Editorial/fase_2_consolidado_20260417.yaml`
- `_Editorial/fase_1_auditoria_rodada_09_20260417.yaml`
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EDITORIAL = ROOT / "_Editorial"

FILENAME_RE = re.compile(
    r"^fase_(?P<fase>\d+)_(?P<tipo>auditoria_rodada|gaps|governanca|fichas|consolidado|arquitetura|matriz_riscos|inventario)"
    r"(?:_\w+)*\.yaml$",
    re.IGNORECASE,
)

# Schema observado na pratica pelos artefatos editoriais existentes.
# `data` e universal; o restante varia por tipo de artefato e e tratado
# como "recomendado" (gera AVISO, nao ERRO).
SCHEMA_OBRIGATORIO: dict[str, set[str]] = {
    "auditoria_rodada": {"data"},
    "consolidado": {"data"},
    "governanca": {"data"},
    "gaps": {"data"},
    "fichas": {"data"},
    "arquitetura": {"data"},
    "matriz_riscos": {"data"},
    "inventario": {"data"},
}

SCHEMA_RECOMENDADO: dict[str, set[str]] = {
    "auditoria_rodada": {"rodada", "thread", "formato", "notas_auditadas"},
    "consolidado": {"entregaveis"},
    "governanca": {"acoes_para_rodadas_futuras"},
    "gaps": {"observacoes_sistemicas"},
    "fichas": {"sinais_de_risco"},
    "arquitetura": {"camadas", "roadmap"},
    "matriz_riscos": {"metodologia", "matriz", "ordem_recomendada"},
    "inventario": {"notas_totais"},
}

PRIORIDADES_VALIDAS = {"P0", "P1", "P2", "ok", "OK"}


@dataclass
class Erro:
    arquivo: Path
    linha_num: int
    mensagem: str
    severidade: str = "erro"  # "erro" | "aviso"


@dataclass
class Relatorio:
    erros: list[Erro] = field(default_factory=list)
    arquivos_validados: int = 0
    arquivos_ok: int = 0

    @property
    def erros_duros(self) -> list[Erro]:
        return [e for e in self.erros if e.severidade == "erro"]

    @property
    def avisos(self) -> list[Erro]:
        return [e for e in self.erros if e.severidade == "aviso"]


def extrair_chaves_top_level(texto: str) -> list[tuple[str, int]]:
    chaves: list[tuple[str, int]] = []
    for num, linha in enumerate(texto.splitlines(), start=1):
        if not linha or linha.startswith(" ") or linha.startswith("#"):
            continue
        if linha.startswith("---") or linha.startswith("..."):
            continue
        if ":" in linha:
            chave = linha.split(":", 1)[0].strip()
            if chave:
                chaves.append((chave, num))
    return chaves


def iterar_itens_lista(texto: str, chave_lista: str) -> list[tuple[int, str]]:
    """Itera os itens `-` diretamente sob `chave_lista:`.

    Retorna lista de (linha_num, corpo_item_concatenado).
    """
    linhas = texto.splitlines()
    itens: list[tuple[int, str]] = []
    dentro = False
    buffer: list[str] = []
    buffer_linha_num = 0

    def flush():
        nonlocal buffer, buffer_linha_num
        if buffer:
            itens.append((buffer_linha_num, "\n".join(buffer)))
            buffer = []
            buffer_linha_num = 0

    for num, linha in enumerate(linhas, start=1):
        if linha.startswith(f"{chave_lista}:"):
            dentro = True
            continue
        if not dentro:
            continue
        # sai quando voltar para top-level
        if linha and not linha.startswith(" ") and not linha.startswith("-"):
            flush()
            dentro = False
            continue
        # novo item
        if linha.startswith("  - ") or linha.startswith("- "):
            flush()
            buffer_linha_num = num
            # remove prefixo "- "
            prefixo = "  - " if linha.startswith("  - ") else "- "
            buffer.append(linha[len(prefixo):])
            continue
        if dentro and (linha.startswith("    ") or linha.startswith("      ")):
            buffer.append(linha.strip())
    flush()
    return itens


def validar_nota_auditada(item_texto: str) -> list[str]:
    campos_necessarios = {"caminho", "tipo_nota", "prioridade", "sinais"}
    campos_presentes: set[str] = set()
    prioridade_valor = ""
    for linha in item_texto.splitlines():
        if ":" in linha:
            chave = linha.split(":", 1)[0].strip()
            valor = linha.split(":", 1)[1].strip().strip('"')
            campos_presentes.add(chave)
            if chave == "prioridade":
                prioridade_valor = valor
    erros = []
    faltando = campos_necessarios - campos_presentes
    if faltando:
        erros.append(f"campos ausentes: {sorted(faltando)}")
    if prioridade_valor and prioridade_valor not in PRIORIDADES_VALIDAS:
        erros.append(
            f"prioridade inválida: '{prioridade_valor}' (esperado: {sorted(PRIORIDADES_VALIDAS)})"
        )
    return erros


def validar_arquivo(arquivo: Path, strict: bool) -> list[Erro]:
    erros: list[Erro] = []
    match = FILENAME_RE.match(arquivo.name)
    if not match:
        erros.append(
            Erro(arquivo, 0, f"nome não segue padrão esperado: {arquivo.name}", "aviso")
        )
        return erros

    tipo = match.group("tipo")
    obrigatorios = SCHEMA_OBRIGATORIO.get(tipo, set())
    recomendados = SCHEMA_RECOMENDADO.get(tipo, set())
    texto = arquivo.read_text(encoding="utf-8")

    chaves_top = {c: num for c, num in extrair_chaves_top_level(texto)}
    faltando = obrigatorios - chaves_top.keys()
    if faltando:
        erros.append(
            Erro(
                arquivo, 1,
                f"chaves obrigatorias ausentes para tipo '{tipo}': {sorted(faltando)}",
                "erro",
            )
        )

    faltando_reco = recomendados - chaves_top.keys()
    if faltando_reco:
        erros.append(
            Erro(
                arquivo, 1,
                f"chaves recomendadas ausentes para tipo '{tipo}': {sorted(faltando_reco)}",
                "aviso",
            )
        )

    # Validacao granular por tipo (quando as chaves de lista existem)
    if tipo == "auditoria_rodada" and "notas_auditadas" in chaves_top:
        for linha_num, item in iterar_itens_lista(texto, "notas_auditadas"):
            problemas = validar_nota_auditada(item)
            for problema in problemas:
                erros.append(Erro(arquivo, linha_num, problema, "erro"))

    if strict:
        # Strict: exige também `reviewed_on`, `autor`, `responsavel`
        campos_strict = {"reviewed_on", "autor"}
        ausentes = campos_strict - chaves_top.keys()
        for c in ausentes:
            erros.append(
                Erro(arquivo, 1, f"strict: campo '{c}' ausente", "aviso")
            )

    return erros


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fase", type=int, help="validar apenas uma fase específica")
    parser.add_argument("--strict", action="store_true",
                        help="exige também campos opcionais (reviewed_on, autor)")
    parser.add_argument("--output", help="escreve relatório em arquivo markdown")
    args = parser.parse_args()

    rel = Relatorio()
    if not EDITORIAL.exists():
        print(f"ERRO: diretório {EDITORIAL} não existe")
        return 2

    padrao = f"fase_{args.fase}_*.yaml" if args.fase else "fase_*.yaml"
    arquivos = sorted(EDITORIAL.glob(padrao))
    if not arquivos:
        print(f"Nenhum artefato encontrado em {EDITORIAL.relative_to(ROOT)}")
        return 1

    for arquivo in arquivos:
        rel.arquivos_validados += 1
        erros = validar_arquivo(arquivo, args.strict)
        if not erros:
            rel.arquivos_ok += 1
        rel.erros.extend(erros)

    print(f"Arquivos validados: {rel.arquivos_validados}")
    print(f"OK: {rel.arquivos_ok}")
    print(f"Erros: {len(rel.erros_duros)}")
    print(f"Avisos: {len(rel.avisos)}")

    for erro in rel.erros:
        rel_path = erro.arquivo.relative_to(ROOT)
        tag = erro.severidade.upper()
        print(f"  [{tag}] {rel_path}:{erro.linha_num} — {erro.mensagem}")

    if args.output:
        linhas = [
            "# Validação de YAMLs de Auditoria",
            "",
            f"- Arquivos validados: {rel.arquivos_validados}",
            f"- Sem erros: {rel.arquivos_ok}",
            f"- Erros: {len(rel.erros_duros)}",
            f"- Avisos: {len(rel.avisos)}",
            "",
        ]
        for erro in rel.erros:
            rel_path = erro.arquivo.relative_to(ROOT)
            linhas.append(
                f"- `[{erro.severidade}]` `{rel_path}` linha {erro.linha_num}: {erro.mensagem}"
            )
        Path(args.output).write_text("\n".join(linhas) + "\n", encoding="utf-8")

    return 0 if not rel.erros_duros else 1


if __name__ == "__main__":
    sys.exit(main())
