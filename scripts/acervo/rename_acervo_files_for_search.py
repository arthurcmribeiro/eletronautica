from __future__ import annotations

import argparse
import hashlib
import sys
import unicodedata
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent

if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.append(str(SCRIPTS_ROOT))

from vault_tools import ROOT  # noqa: E402


MAIN_ROOT = ROOT / "90_Revisao_Manual" / "_Acervo_Local"

RENAMES: tuple[tuple[str, str], ...] = (
    (
        "Climatizacao/Dometic/Self-Contained/dometic-cruisair__dx-remote-self-contained__installation-manual__mirror.pdf",
        "Climatizacao/Dometic/Self-Contained/dometic-cruisair__self-contained-air-conditioner__installation-manual__dx-remote-legacy-espelho.pdf",
    ),
    (
        "Climatizacao/Dometic/Self-Contained/dometic-cruisair__self-contained__troubleshooting-guide__mirror.pdf",
        "Climatizacao/Dometic/Self-Contained/dometic-cruisair__self-contained-air-conditioner__troubleshooting-guide__legacy-espelho.pdf",
    ),
    (
        "Complementar-Brasil/Corrosao/DPH-DPR-IPS/referencia-tecnica__corrosao-dph-dpr-ips__medicoes.pdf",
        "Complementar-Brasil/Corrosao/DPH-DPR-IPS/referencia-tecnica__corrosao-eletrolise-dph-dpr-ips__medicoes.pdf",
    ),
    (
        "Complementar-Brasil/Referencias-Gerais/12V/referencia-geral__12-volt-doctors__handbook__practical.pdf",
        "Complementar-Brasil/Referencias-Gerais/12V/referencia-geral__12-volt-doctors__handbook__practical-12v-systems.pdf",
    ),
    (
        "Geradores/Cummins-Onan/Legacy-MDKBK-MDKBN/cummins-onan__mdkbk-mdkbv__service-manual__mirror.pdf",
        "Geradores/Cummins-Onan/Legacy-MDKBK-MDKBN/cummins-onan__mdkbk-mdkbl-mdkbm-mdkbn__service-manual__legacy-espelho.pdf",
    ),
    (
        "Geradores/Cummins-Onan/Legacy-MDKBK-MDKBN/cummins-onan__mdkbx__operator-manual__981-0181-2008-03.pdf",
        "Geradores/Cummins-Onan/Legacy-MDKBK-MDKBN/cummins-onan__mdkbk-mdkbl-mdkbm-mdkbn__operator-manual__981-0181-2008-03.pdf",
    ),
    (
        "Geradores/Cummins-Onan/Legacy-MDKBP-MDKBS/cummins-onan__mdkbk-mdkbv__service-manual__mirror.pdf",
        "Geradores/Cummins-Onan/Legacy-MDKBP-MDKBS/cummins-onan__mdkbp-mdkbr-mdkbs__service-manual__legacy-espelho.pdf",
    ),
    (
        "Geradores/Cummins-Onan/Legacy-MDKBP-MDKBS/cummins-onan__mdkbp-mdkbr-mdkbs__parts-manual__mirror.pdf",
        "Geradores/Cummins-Onan/Legacy-MDKBP-MDKBS/cummins-onan__mdkbp-mdkbr-mdkbs__parts-manual__legacy-espelho.pdf",
    ),
    (
        "Geradores/Cummins-Onan/Legacy-MDKBP-MDKBS/cummins-onan__mdkbx__operator-manual__981-0181-2008-03.pdf",
        "Geradores/Cummins-Onan/Legacy-MDKBP-MDKBS/cummins-onan__mdkbp-mdkbr-mdkbs__operator-manual__981-0181-2008-03.pdf",
    ),
    (
        "Geradores/Cummins-Onan/Legacy-MDKBT-MDKBV/cummins-onan__mdkbk-mdkbv__service-manual__mirror.pdf",
        "Geradores/Cummins-Onan/Legacy-MDKBT-MDKBV/cummins-onan__mdkbt-mdkbu-mdkbv__service-manual__legacy-espelho.pdf",
    ),
    (
        "Geradores/Cummins-Onan/Legacy-MDKBT-MDKBV/cummins-onan__mdkbx__operator-manual__981-0181-2008-03.pdf",
        "Geradores/Cummins-Onan/Legacy-MDKBT-MDKBV/cummins-onan__mdkbt-mdkbu-mdkbv__operator-manual__981-0181-2008-03.pdf",
    ),
    (
        "Geradores/Cummins-Onan/MDKAD-MDKAE-MDKAF/cummins-onan__mdkad-mdkae-mdkaf__service-manual__mirror.pdf",
        "Geradores/Cummins-Onan/MDKAD-MDKAE-MDKAF/cummins-onan__mdkad-mdkae-mdkaf__service-manual__legacy-espelho.pdf",
    ),
    (
        "Geradores/Cummins-Onan/MDKBH/cummins-onan__mdkbh__service-manual__mirror.pdf",
        "Geradores/Cummins-Onan/MDKBH/cummins-onan__mdkbh__service-manual__legacy-espelho.pdf",
    ),
    (
        "Geradores/Cummins-Onan/MDKDK/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__service-manual__mirror.pdf",
        "Geradores/Cummins-Onan/MDKDK/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__service-manual__legacy-espelho.pdf",
    ),
    (
        "Geradores/Cummins-Onan/MDKDL/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__service-manual__mirror.pdf",
        "Geradores/Cummins-Onan/MDKDL/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__service-manual__legacy-espelho.pdf",
    ),
    (
        "Geradores/Cummins-Onan/MDKDM-MDKDN/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__service-manual__mirror.pdf",
        "Geradores/Cummins-Onan/MDKDM-MDKDN/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__service-manual__legacy-espelho.pdf",
    ),
    (
        "Geradores/Cummins-Onan/MDKDP-MDKDR-MDKDV/cummins-onan__mdkdp-mdkdr-mkdv__parts-manual__a046l892.pdf",
        "Geradores/Cummins-Onan/MDKDP-MDKDR-MDKDV/cummins-onan__mdkdp-mdkdr-mdkdv__parts-manual__a046l892.pdf",
    ),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_text(value: str) -> str:
    normalized = unicodedata.normalize("NFC", value)
    return normalized.encode("cp1252", errors="replace").decode("cp1252")


def rename_file(old_rel: str, new_rel: str, apply_changes: bool) -> str:
    old_path = MAIN_ROOT / old_rel
    new_path = MAIN_ROOT / new_rel

    if not old_path.exists():
        if new_path.exists():
            return "already-renamed"
        return "missing"

    if new_path.exists():
        if sha256(old_path) == sha256(new_path):
            raise FileExistsError(
                f"Antigo e novo existem ao mesmo tempo com o mesmo conteúdo: {old_path} -> {new_path}"
            )
        raise FileExistsError(f"Destino já existe com conteúdo diferente: {new_path}")

    if not apply_changes:
        return "planned"

    new_path.parent.mkdir(parents=True, exist_ok=True)
    old_path.rename(new_path)
    return "renamed"


def rename_all(apply_changes: bool) -> dict[str, int]:
    counters = {
        "planned": 0,
        "renamed": 0,
        "already-renamed": 0,
        "missing": 0,
    }

    for old_rel, new_rel in RENAMES:
        result = rename_file(old_rel, new_rel, apply_changes)
        counters[result] += 1
        print(safe_text(f"{result.upper()}: {old_rel} -> {new_rel}"))

    return counters


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Renomeia arquivos do acervo principal para melhorar busca e consistência."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Aplica os renomes. Sem esta flag, apenas mostra o plano.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    counters = rename_all(apply_changes=args.apply)
    mode = "APLICADO" if args.apply else "DRY-RUN"
    print("")
    print(f"Modo: {mode}")
    print(f"Arquivos planejados: {counters['planned']}")
    print(f"Arquivos renomeados: {counters['renamed']}")
    print(f"Arquivos já renomeados: {counters['already-renamed']}")
    print(f"Arquivos ausentes: {counters['missing']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
