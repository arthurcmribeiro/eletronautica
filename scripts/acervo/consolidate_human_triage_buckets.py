from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent

if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.append(str(SCRIPTS_ROOT))

from vault_tools import ROOT, write_json  # noqa: E402


ARCHIVE_ROOT = ROOT / "90_Revisao_Manual" / "_Acervo_Local" / "Acervo do humano"
TECH_ROOT = ARCHIVE_ROOT / "10_Tecnico_Nautico"
TRIAGE_ROOT = TECH_ROOT / "90_Triagem_Tecnica_por_Codigo"
OUT_OF_SCOPE_ROOT = ARCHIVE_ROOT / "00_Fora_do_Escopo_ou_Pessoal"
MANIFEST_PATH = ROOT / "manifest" / "acervo-humano-triage-consolidation.json"
REPORT_PATH = ROOT / "_Editorial" / "Consolidacao do Acervo Humano Tecnico.md"


DEFAULT_FOLDER_TARGETS = {
    "01_Geradores_e_Motores_Base": "TECH:01_Geradores",
    "02_Navegacao_Comunicacao_e_Instrumentos": "TECH:05_Navegacao_e_Eletronicos",
    "03_Propulsao_Motores_e_Turbo": "TECH:09_Propulsao_Motores_Estabilizacao_e_Atuacao",
    "04_DC_Componentes_e_Controle": "TECH:03_Baterias_e_DC",
    "05_Bombas_Utilidades_e_Acessorios": "TECH:06_Bombas_Hidraulica_e_Utilidades",
    "06_Artigos_Normas_e_Referencia_Tecnica": "TECH:10_Materiais_Internos_e_Cursos/Referencias_Tecnicas",
    "07_Imagens_e_Recortes_Tecnicos": "TECH:00_Documentacao_de_Campo_e_Clientes/Imagens_e_Recortes_Tecnicos",
    "99_Fora_do_Escopo_ou_Pessoal": "OUT:_Triagem_Tecnica_Resolvida",
}

FILE_TARGET_OVERRIDES = {
    "03_Propulsao_Motores_e_Turbo/AB12210.pdf": "TECH:03_Baterias_e_DC",
    "03_Propulsao_Motores_e_Turbo/chilled-water-air-conditioning.pdf": "TECH:02_Climatizacao",
    "03_Propulsao_Motores_e_Turbo/Non-Metallic-Materials-Brochure.pdf": "TECH:10_Materiais_Internos_e_Cursos/Referencias_Tecnicas",
    "04_DC_Componentes_e_Controle/tribunal-maritimo.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "05_Bombas_Utilidades_e_Acessorios/cruisair-tempered-water-system.pdf": "TECH:02_Climatizacao",
    "05_Bombas_Utilidades_e_Acessorios/foto-de-p-303-241gina-inteira.pdf": "TECH:00_Documentacao_de_Campo_e_Clientes/Imagens_e_Recortes_Tecnicos",
    "06_Artigos_Normas_e_Referencia_Tecnica/SPL.pdf": "TECH:07_Iluminacao_Sinalizacao_e_Acessorios",
    "06_Artigos_Normas_e_Referencia_Tecnica/comando-da-aeronautica.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "06_Artigos_Normas_e_Referencia_Tecnica/disponivel-em-http-www-desafioonline-uf-0fb0e9fe.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "06_Artigos_Normas_e_Referencia_Tecnica/doi-10-32385-rpmgf-v37i3-12845.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "06_Artigos_Normas_e_Referencia_Tecnica/informac-oesgerais-normasdeconduta.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "06_Artigos_Normas_e_Referencia_Tecnica/sofia-furtado1-2-luis-reis2.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "07_Imagens_e_Recortes_Tecnicos/301-022-schema-toerenteller-tot-10000RPM-VDO.jpg": "TECH:05_Navegacao_e_Eletronicos",
    "99_Fora_do_Escopo_ou_Pessoal/avr-a-opt-01-regulador-de-tensao-analogico.pdf": "TECH:01_Geradores",
    "ZZ_Residual_Manual/00206bf595ae240412115759.pdf": "TECH:00_Documentacao_de_Campo_e_Clientes/Imagens_e_Recortes_Tecnicos",
    "ZZ_Residual_Manual/19-informativo-tecnico-no.pdf": "TECH:03_Baterias_e_DC",
    "ZZ_Residual_Manual/235-east-airway-boulevard-livermore-cal-c772a288.pdf": "TECH:09_Propulsao_Motores_Estabilizacao_e_Atuacao",
    "ZZ_Residual_Manual/235-east-airway-boulevard-livermore-cal-fc96c680.pdf": "TECH:09_Propulsao_Motores_Estabilizacao_e_Atuacao",
    "ZZ_Residual_Manual/722-NE.pdf": "TECH:03_Baterias_e_DC",
    "ZZ_Residual_Manual/arieltek-industria-e-comercio-ltda.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "ZZ_Residual_Manual/arthur-carlos-marques-ribeiro-em-21edeo-2e2a3fab.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "ZZ_Residual_Manual/c-users-nalmeida-appdata-local-temp-26-46885c42.pdf": "TECH:00_Documentacao_de_Campo_e_Clientes/Imagens_e_Recortes_Tecnicos",
    "ZZ_Residual_Manual/caro-cliente.pdf": "TECH:08_Corrosao_Bonding_e_Seguranca",
    "ZZ_Residual_Manual/catalogo-motori.pdf": "TECH:09_Propulsao_Motores_Estabilizacao_e_Atuacao",
    "ZZ_Residual_Manual/historico-escolar.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "ZZ_Residual_Manual/instructions-for-the-2024-diversity-imm-0ddbf97e.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "ZZ_Residual_Manual/instructions-for-the-2024-diversity-imm-1f475f72.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "ZZ_Residual_Manual/instructions-for-the-2024-diversity-imm-a53c49ac.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "ZZ_Residual_Manual/kamellcomercio.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "ZZ_Residual_Manual/models-1204m-05m-09m-21m-dup-2.pdf": "TECH:09_Propulsao_Motores_Estabilizacao_e_Atuacao",
    "ZZ_Residual_Manual/models-1204m-05m-09m-21m.pdf": "TECH:09_Propulsao_Motores_Estabilizacao_e_Atuacao",
    "ZZ_Residual_Manual/mpdf.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "ZZ_Residual_Manual/op-10377-par.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "ZZ_Residual_Manual/owner-s-manual.pdf": "TECH:07_Iluminacao_Sinalizacao_e_Acessorios",
    "ZZ_Residual_Manual/P753.pdf": "TECH:00_Documentacao_de_Campo_e_Clientes/Imagens_e_Recortes_Tecnicos",
    "ZZ_Residual_Manual/pagador-arthur-carlos-marques-ribeiro.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "ZZ_Residual_Manual/presentazione-standard-di-powerpoint.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "ZZ_Residual_Manual/recebemos-de-48-907-420-marlene-apareci-5ea063b8.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "ZZ_Residual_Manual/reguladores-de-tensao-digitais.pdf": "TECH:01_Geradores",
    "ZZ_Residual_Manual/relogio.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "ZZ_Residual_Manual/rev-2-04-17.pdf": "TECH:03_Baterias_e_DC",
    "ZZ_Residual_Manual/secretaria-de-governo-departamento-esta-f24aeecf.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "ZZ_Residual_Manual/seelevel-ii-tm.pdf": "TECH:06_Bombas_Hidraulica_e_Utilidades",
    "ZZ_Residual_Manual/ServletSolicitarPID.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "ZZ_Residual_Manual/tabela-chaves.pdf": "OUT:_Triagem_Tecnica_Resolvida",
    "ZZ_Residual_Manual/ultraflex-control-systems-s-r-l.pdf": "TECH:09_Propulsao_Motores_Estabilizacao_e_Atuacao",
}


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def io_path(path: Path) -> str:
    resolved = str(path.resolve())
    if os.name != "nt" or resolved.startswith("\\\\?\\"):
        return resolved
    return f"\\\\?\\{resolved}"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with open(io_path(path), "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def decode_target(target_spec: str) -> tuple[str, Path]:
    prefix, relative_target = target_spec.split(":", 1)
    if prefix == "TECH":
        return prefix, TECH_ROOT / relative_target
    if prefix == "OUT":
        return prefix, OUT_OF_SCOPE_ROOT / relative_target
    raise ValueError(f"Destino invalido: {target_spec}")


def target_for(source: Path) -> tuple[str, Path] | None:
    relative_source = source.relative_to(TRIAGE_ROOT).as_posix()
    target_spec = FILE_TARGET_OVERRIDES.get(relative_source)
    if not target_spec:
        parts = source.relative_to(TRIAGE_ROOT).parts
        target_spec = DEFAULT_FOLDER_TARGETS.get(parts[0] if parts else "")
    if not target_spec:
        return None
    scope, folder = decode_target(target_spec)
    return scope, folder / source.name


def unique_target(target: Path) -> Path:
    if not target.exists():
        return target
    stem = target.stem
    suffix = target.suffix
    for index in range(2, 1000):
        candidate = target.with_name(f"{stem}__triagem-{index}{suffix}")
        if not candidate.exists():
            return candidate
    raise FileExistsError(f"Nao foi possivel criar destino unico para {target}")


def source_files() -> list[Path]:
    if not TRIAGE_ROOT.exists():
        return []
    return sorted(path for path in TRIAGE_ROOT.rglob("*") if os.path.isfile(io_path(path)))


def clean_empty_dirs() -> list[str]:
    removed: list[str] = []
    for directory in sorted(
        (path for path in TRIAGE_ROOT.rglob("*") if path.is_dir()),
        key=lambda item: len(item.parts),
        reverse=True,
    ):
        if directory == TRIAGE_ROOT:
            continue
        try:
            next(directory.iterdir())
        except StopIteration:
            try:
                directory.rmdir()
                removed.append(relative(directory))
            except OSError:
                pass
    return removed


def build_plan() -> list[dict[str, Any]]:
    plan: list[dict[str, Any]] = []
    for source in source_files():
        target_data = target_for(source)
        if target_data is None:
            plan.append(
                {
                    "status": "needs-manual-review",
                    "source": relative(source),
                    "target": "",
                    "scope": "",
                    "sha256": sha256(source),
                }
            )
            continue
        scope, target = target_data
        final_target = unique_target(target)
        plan.append(
            {
                "status": "planned",
                "source": relative(source),
                "target": relative(final_target),
                "scope": "technical" if scope == "TECH" else "out-of-scope",
                "sha256": sha256(source),
            }
        )
    return plan


def apply_plan(plan: list[dict[str, Any]]) -> None:
    for item in plan:
        if item["status"] != "planned":
            continue
        source = ROOT / str(item["source"])
        target = ROOT / str(item["target"])
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(io_path(source), io_path(target))
        item["status"] = "moved"


def render_report(payload: dict[str, Any]) -> str:
    reviewed_on = datetime.now().date().isoformat()
    plan = payload["items"]
    status_counts = Counter(item["status"] for item in plan)
    scope_counts = Counter(item["scope"] for item in plan if item.get("scope"))
    target_parent_counts = Counter(
        Path(str(item["target"])).parent.as_posix()
        for item in plan
        if item.get("target")
    )

    lines = [
        "---",
        'title: "Consolidacao do Acervo Humano Tecnico"',
        'note_type: "audit"',
        'domain: "90_Revisao_Manual"',
        'status: "auto-generated"',
        f'reviewed_on: "{reviewed_on}"',
        'review_jurisdiction: "Brasil"',
        "related_notes:",
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Indice Gerado"',
        '  - "90_Revisao_Manual/10_Indices_e_Paineis/Acervo Humano Tecnico - Manifesto de Duplicatas"',
        "---",
        "",
        "# Consolidacao do Acervo Humano Tecnico",
        "",
        "> [!abstract] Resumo tecnico",
        "> Consolidacao dos itens que estavam em `90_Triagem_Tecnica_por_Codigo`, movendo material tecnico para buckets finais e material nao tecnico para fora de escopo.",
        "",
        "## Resultado",
        "",
        f"- modo aplicado: `{payload['applied']}`",
        f"- arquivos avaliados: `{len(plan)}`",
        f"- manifesto: `{relative(MANIFEST_PATH)}`",
        "",
        "## Status",
        "",
    ]
    for status, count in sorted(status_counts.items()):
        lines.append(f"- `{status}`: `{count}`")

    lines.extend(["", "## Escopo", ""])
    for scope, count in sorted(scope_counts.items()):
        lines.append(f"- `{scope}`: `{count}`")

    lines.extend(["", "## Destinos", ""])
    for target_parent, count in target_parent_counts.most_common():
        lines.append(f"- `{target_parent}`: `{count}`")

    if payload.get("removed_empty_dirs"):
        lines.extend(["", "## Diretorios vazios removidos", ""])
        for directory in payload["removed_empty_dirs"]:
            lines.append(f"- `{directory}`")

    lines.extend(["", "## Movimentacoes", ""])
    for item in plan:
        lines.append(
            f"- `{item['status']}` - `{item['scope']}` - `{item['source']}` -> `{item['target']}`"
        )

    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Consolida subpastas de triagem do acervo humano tecnico."
    )
    parser.add_argument("--apply", action="store_true", help="Move os arquivos.")
    parser.add_argument(
        "--clean-empty-dirs",
        action="store_true",
        help="Remove apenas diretorios vazios dentro da raiz de triagem.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    plan = build_plan()
    if args.apply:
        apply_plan(plan)
    removed_empty_dirs = clean_empty_dirs() if args.apply and args.clean_empty_dirs else []

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "applied": args.apply,
        "triage_root": relative(TRIAGE_ROOT),
        "items": plan,
        "removed_empty_dirs": removed_empty_dirs,
    }
    write_json(MANIFEST_PATH, payload)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(render_report(payload), encoding="utf-8", newline="\n")

    counts = Counter(item["status"] for item in plan)
    scopes = Counter(item["scope"] for item in plan if item.get("scope"))
    mode = "APLICADO" if args.apply else "DRY-RUN"
    print(f"Modo: {mode}")
    print(f"Arquivos avaliados: {len(plan)}")
    for status, count in sorted(counts.items()):
        print(f"{status}: {count}")
    for scope, count in sorted(scopes.items()):
        print(f"{scope}: {count}")
    print(f"Manifesto: {relative(MANIFEST_PATH)}")
    print(f"Relatorio: {relative(REPORT_PATH)}")
    return 0 if not counts.get("needs-manual-review") else 1


if __name__ == "__main__":
    raise SystemExit(main())
