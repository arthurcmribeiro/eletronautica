from __future__ import annotations

import argparse
import hashlib
import shutil
import subprocess
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent

if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.append(str(SCRIPTS_ROOT))

from vault_tools import ROOT  # noqa: E402


STAGING_ROOT = (
    ROOT
    / "90_Revisao_Manual"
    / "_Acervo_Local"
    / "Acervo do humano"
    / "10_Tecnico_Nautico"
)
MAIN_ROOT = ROOT / "90_Revisao_Manual" / "_Acervo_Local"


@dataclass(frozen=True)
class Promotion:
    source_rel: str
    targets: tuple[str, ...]


PROMOTIONS: tuple[Promotion, ...] = (
    Promotion(
        "01_Geradores/MDKBH-Service-Manual.pdf",
        (
            "Geradores/Cummins-Onan/MDKBH/cummins-onan__mdkbh__service-manual__legacy-espelho.pdf",
        ),
    ),
    Promotion(
        "01_Geradores/MDKDK-DL-DM-DN-Service-Manual.pdf",
        (
            "Geradores/Cummins-Onan/MDKDK/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__service-manual__legacy-espelho.pdf",
            "Geradores/Cummins-Onan/MDKDL/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__service-manual__legacy-espelho.pdf",
            "Geradores/Cummins-Onan/MDKDM-MDKDN/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__service-manual__legacy-espelho.pdf",
        ),
    ),
    Promotion(
        "01_Geradores/A052J727-Issue-1-English.pdf",
        (
            "Geradores/Cummins-Onan/MDKDK/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__operator-manual__a052j727.pdf",
            "Geradores/Cummins-Onan/MDKDL/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__operator-manual__a052j727.pdf",
            "Geradores/Cummins-Onan/MDKDM-MDKDN/cummins-onan__mdkdk-mdkdl-mdkdm-mdkdn__operator-manual__a052j727.pdf",
        ),
    ),
    Promotion(
        "01_Geradores/MDKDP-DR-DS-DT-DU-DV-Service-Manual.pdf",
        (
            "Geradores/Cummins-Onan/MDKDP-MDKDR-MDKDV/cummins-onan__mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv__service-manual__a046j602.pdf",
            "Geradores/Cummins-Onan/MDKDS-MDKDT-MDKDU/cummins-onan__mdkdp-mdkdr-mdkds-mdkdt-mdkdu-mdkdv__service-manual__a046j602.pdf",
        ),
    ),
    Promotion(
        "01_Geradores/MDKAD-AE-AF-Service-Manual.pdf",
        (
            "Geradores/Cummins-Onan/MDKAD-MDKAE-MDKAF/cummins-onan__mdkad-mdkae-mdkaf__service-manual__legacy-espelho.pdf",
        ),
    ),
    Promotion(
        "01_Geradores/981-0140 Onan MDKAD MDKAE MDKAF Operator's Manual (2-1996).pdf",
        (
            "Geradores/Cummins-Onan/MDKAD-MDKAE-MDKAF/cummins-onan__mdkad-mdkae-mdkaf__operator-manual__981-0140-1996-02.pdf",
        ),
    ),
    Promotion(
        "01_Geradores/981-0264 Onan MDKAD MDKAE (spec A-C) Marine Diesel Genset Parts manual (01-1999).pdf",
        (
            "Geradores/Cummins-Onan/MDKAD-MDKAE-MDKAF/cummins-onan__mdkad-mdkae__parts-manual__981-0264-1999-01.pdf",
        ),
    ),
    Promotion(
        "01_Geradores/MDKBK-BL-BM-BN-BP-BR-BS-BT-BU-BV-Service-Manual.pdf",
        (
            "Geradores/Cummins-Onan/Legacy-MDKBK-MDKBN/cummins-onan__mdkbk-mdkbl-mdkbm-mdkbn__service-manual__legacy-espelho.pdf",
            "Geradores/Cummins-Onan/Legacy-MDKBP-MDKBS/cummins-onan__mdkbp-mdkbr-mdkbs__service-manual__legacy-espelho.pdf",
            "Geradores/Cummins-Onan/Legacy-MDKBT-MDKBV/cummins-onan__mdkbt-mdkbu-mdkbv__service-manual__legacy-espelho.pdf",
        ),
    ),
    Promotion(
        "01_Geradores/981-0181 Onan MDKBx Marine Genset Operator manual (03-2008).pdf",
        (
            "Geradores/Cummins-Onan/Legacy-MDKBK-MDKBN/cummins-onan__mdkbk-mdkbl-mdkbm-mdkbn__operator-manual__981-0181-2008-03.pdf",
            "Geradores/Cummins-Onan/Legacy-MDKBP-MDKBS/cummins-onan__mdkbp-mdkbr-mdkbs__operator-manual__981-0181-2008-03.pdf",
            "Geradores/Cummins-Onan/Legacy-MDKBT-MDKBV/cummins-onan__mdkbt-mdkbu-mdkbv__operator-manual__981-0181-2008-03.pdf",
        ),
    ),
    Promotion(
        "01_Geradores/MDKBPA-C-BRA-C-BS-Parts-Manual.pdf",
        (
            "Geradores/Cummins-Onan/Legacy-MDKBP-MDKBS/cummins-onan__mdkbp-mdkbr-mdkbs__parts-manual__legacy-espelho.pdf",
        ),
    ),
    Promotion(
        "90_Triagem_Tecnica_por_Codigo/5EFKOZD-service-manual.pdf",
        (
            "Geradores/Rehlko-Kohler/5EFKOD/rehlko-kohler__5efkod-6ekod-9-11ekozd-7-9efkozd__service-manual__tp-6774-2014-02a.pdf",
            "Geradores/Rehlko-Kohler/6EKOD/rehlko-kohler__5efkod-6ekod-9-11ekozd-7-9efkozd__service-manual__tp-6774-2014-02a.pdf",
            "Geradores/Rehlko-Kohler/7EFKOZD/rehlko-kohler__5efkod-6ekod-9-11ekozd-7-9efkozd__service-manual__tp-6774-2014-02a.pdf",
            "Geradores/Rehlko-Kohler/9-13.5-EKOZD-EFKOZD/rehlko-kohler__5efkod-6ekod-9-11ekozd-7-9efkozd__service-manual__tp-6774-2014-02a.pdf",
        ),
    ),
    Promotion(
        "02_Climatizacao/cruisair_-_dx_remote_self-contained_a-c.pdf",
        (
            "Climatizacao/Dometic/Self-Contained/dometic-cruisair__self-contained-air-conditioner__installation-manual__dx-remote-legacy-espelho.pdf",
        ),
    ),
    Promotion(
        "02_Climatizacao/cruisair-troubleshooting-guide.pdf",
        (
            "Climatizacao/Dometic/Self-Contained/dometic-cruisair__self-contained-air-conditioner__troubleshooting-guide__legacy-espelho.pdf",
        ),
    ),
    Promotion(
        "02_Climatizacao/2015-Price-list-CRUISAIR-Dometic-Air-Conditioner.pdf",
        (
            "Climatizacao/Dometic/Self-Contained/dometic-cruisair__marine-air-conditioners__price-list__2015.pdf",
        ),
    ),
    Promotion(
        "02_Climatizacao/Dometic-Marine-Air-Conditioner-2024-Price-List.pdf",
        (
            "Climatizacao/Dometic/Self-Contained/dometic__marine-air-conditioners__price-list__2024.pdf",
        ),
    ),
    Promotion(
        "03_Baterias_e_DC/The 12 Volt Doctors Practical Handbook.pdf",
        (
            "Complementar-Brasil/Referencias-Gerais/12V/referencia-geral__12-volt-doctors__handbook__practical-12v-systems.pdf",
        ),
    ),
    Promotion(
        "08_Corrosao_Bonding_e_Seguranca/corrosao DPH DPR IPS medicoes.pdf",
        (
            "Complementar-Brasil/Corrosao/DPH-DPR-IPS/referencia-tecnica__corrosao-eletrolise-dph-dpr-ips__medicoes.pdf",
        ),
    ),
    Promotion(
        "05_Navegacao_e_Eletronicos/CABOS E CONEXÃO RAYMARINE SEATALK.pdf",
        (
            "Navegacao/Raymarine/SeaTalk/raymarine__seatalk__cabling-and-connections__legacy-espelho.pdf",
        ),
    ),
    Promotion(
        "05_Navegacao_e_Eletronicos/por_raymarine_manu_quantum.pdf",
        (
            "Navegacao/Raymarine/Quantum/raymarine__quantum-radar__manual__portugues-legacy-espelho.pdf",
        ),
    ),
    Promotion(
        "05_Navegacao_e_Eletronicos/SMARTPILOT ST6002.pdf",
        (
            "Navegacao/Raymarine/SmartPilot-ST6002/raymarine__smartpilot-st6002__operation-manual__legacy-espelho.pdf",
        ),
    ),
    Promotion(
        "05_Navegacao_e_Eletronicos/fi5002_installation_manual_a.pdf",
        (
            "Navegacao/Furuno/FI-5002/furuno__fi-5002__installation-manual__rev-a.pdf",
        ),
    ),
    Promotion(
        "05_Navegacao_e_Eletronicos/fi5002_supplemental_instructions.pdf",
        (
            "Navegacao/Furuno/FI-5002/furuno__fi-5002__supplemental-instructions__legacy-espelho.pdf",
        ),
    ),
    Promotion(
        "05_Navegacao_e_Eletronicos/furuno_can_bus_network_design.pdf",
        (
            "Navegacao/Furuno/CAN-Bus/furuno__can-bus__network-design-guide__legacy-espelho.pdf",
        ),
    ),
    Promotion(
        "05_Navegacao_e_Eletronicos/GPS_17x_HVS_Tech_Specs.pdf",
        (
            "Navegacao/Garmin/GPS-17x-HVS/garmin__gps-17x-hvs__technical-specifications__legacy-espelho.pdf",
        ),
    ),
    Promotion(
        "05_Navegacao_e_Eletronicos/GPSMAP_4000-5000_Install_EN.pdf",
        (
            "Navegacao/Garmin/GPSMAP-4000-5000/garmin__gpsmap-4000-5000__installation-manual__en.pdf",
        ),
    ),
    Promotion(
        "05_Navegacao_e_Eletronicos/GX2000_GX2150_OM_USA_EM044N160_5292013.pdf",
        (
            "Navegacao/Standard-Horizon/GX2000-GX2150/standard-horizon__gx2000-gx2150__operation-manual__em044n160-5292013.pdf",
        ),
    ),
    Promotion(
        "90_Triagem_Tecnica_por_Codigo/ARQUIVO_CORTE_DISPLAY_GHC50.pdf",
        (
            "Navegacao/Garmin/GHC-50/garmin__ghc-50__display-cutout-template__legacy-espelho.pdf",
        ),
    ),
    Promotion(
        "09_Propulsao_Motores_Estabilizacao_e_Atuacao/Catálogo GP BOATS Peças Volvo Penta.pdf",
        (
            "Complementar-Brasil/Volvo-Penta/Catalogo-GP-Boats/referencia-comercial__volvo-penta__catalogo-pecas-gp-boats.pdf",
        ),
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


def resolve_source(source_rel: str) -> Path:
    direct = STAGING_ROOT / source_rel
    if direct.exists():
        return direct

    name = Path(source_rel).name
    matches = sorted(path for path in STAGING_ROOT.rglob(name) if path.is_file())
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise FileNotFoundError(f"Fonte nÃ£o encontrada: {direct}")
    raise FileNotFoundError(
        f"Fonte ambÃ­gua para {source_rel}: "
        + ", ".join(str(path.relative_to(STAGING_ROOT).as_posix()) for path in matches)
    )


def ensure_same_or_copy(source: Path, target: Path, apply_changes: bool) -> str:
    if target.exists():
        if sha256(source) == sha256(target):
            return "unchanged"
        raise FileExistsError(f"Destino existente com conteúdo diferente: {target}")

    if not apply_changes:
        return "planned"

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    return "copied"


def promote(apply_changes: bool) -> dict[str, int]:
    counters = {"planned": 0, "copied": 0, "unchanged": 0}

    for promotion in PROMOTIONS:
        source = resolve_source(promotion.source_rel)

        for target_rel in promotion.targets:
            target = MAIN_ROOT / target_rel
            result = ensure_same_or_copy(source, target, apply_changes)
            counters[result] += 1
            print(
                safe_text(
                    f"{result.upper()}: {promotion.source_rel} -> {target.relative_to(MAIN_ROOT).as_posix()}"
                )
            )

    return counters


def run_companion_note_pipeline() -> None:
    script = SCRIPT_DIR / "build_pdf_companion_notes.py"
    subprocess.run([sys.executable, str(script)], check=True)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Promove documentos técnicos curados do Acervo do humano para o acervo principal."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Copia os arquivos para o acervo principal. Sem esta flag, apenas mostra o plano.",
    )
    parser.add_argument(
        "--skip-notes",
        action="store_true",
        help="Nao gera notas companheiras apos a promocao aplicada.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    counters = promote(apply_changes=args.apply)
    if args.apply and not args.skip_notes:
        print("")
        print("Gerando notas companheiras para o acervo principal...")
        run_companion_note_pipeline()
    mode = "APLICADO" if args.apply else "DRY-RUN"
    print("")
    print(f"Modo: {mode}")
    print(f"Arquivos planejados: {counters['planned']}")
    print(f"Arquivos copiados: {counters['copied']}")
    print(f"Arquivos já presentes: {counters['unchanged']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
