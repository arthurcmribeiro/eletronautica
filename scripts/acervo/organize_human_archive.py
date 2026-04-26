from __future__ import annotations

import argparse
import os
import shutil
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent

if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.append(str(SCRIPTS_ROOT))

from vault_tools import ROOT  # noqa: E402


ARCHIVE_ROOT = ROOT / "90_Revisao_Manual" / "_Acervo_Local" / "Acervo do humano"
TECH_ROOT = ARCHIVE_ROOT / "10_Tecnico_Nautico"

NON_TECH_DOC_EXTENSIONS = {
    ".csv",
    ".doc",
    ".docx",
    ".html",
    ".md",
    ".txt",
    ".xlsx",
    ".xml",
    ".zip",
}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}

GENERIC_TECH_DOC_MARKERS = (
    "brochure",
    "catalog",
    "catalogo",
    "catalogue",
    "diagram",
    "guide",
    "installation",
    "instructions",
    "manual",
    "operator",
    "operation",
    "opm",
    "owner",
    "owners",
    "parts",
    "qsg",
    "schema",
    "service",
    "spec",
    "technical",
    "troubleshooting",
    "wiring",
)


def normalize(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    without_accents = "".join(
        character for character in normalized if not unicodedata.combining(character)
    )
    return without_accents.casefold()


def has_any(text: str, keywords: tuple[str, ...]) -> bool:
    return any(keyword in text for keyword in keywords)


def io_path(path: Path) -> str:
    resolved = str(path.resolve())
    if os.name != "nt" or resolved.startswith("\\\\?\\"):
        return resolved
    return f"\\\\?\\{resolved}"


@dataclass(frozen=True)
class Rule:
    destination: str
    keywords: tuple[str, ...]


RULES: tuple[Rule, ...] = (
    Rule(
        "00_Fora_do_Escopo_ou_Pessoal",
        (
            "#poupatempotaon",
            "adesionelb",
            "analise_trafego_pago",
            "apertura_conto",
            "arthurribeiro-postecert",
            "arthurribeiro postecert",
            "arthur ribeiro cv",
            "auberge-de-cendrillon",
            "aula-",
            "aula_",
            "autorizacao_viagem",
            "banca_multicanale",
            "banco_posta",
            "boleto",
            "budesonida",
            "calendario_estrategico",
            "cartao de embarque",
            "cartao embarque",
            "cartilha_para_aprovacao_de_projetos",
            "certificado_nacional_de_covid",
            "certidao_casamento",
            "civp",
            "classificacao_provisoria",
            "classificacao-definitiva",
            "classificacao_definitiva",
            "compra ubatuba",
            "comprovantesantander",
            "condizioni_contrattuali",
            "confermaprenotazione",
            "contrato_de_prestacao_de_servios",
            "contratto",
            "copia de kcombo7",
            "covid",
            "cronograma-6-meses",
            "curriculo",
            "cv arthur",
            "danfe",
            "das-pgmei",
            "declaracao explicativa",
            "diploma",
            "docmil-",
            "documentacao necessaria",
            "documento motor portugal arthur",
            "do brasil a bora bora",
            "edital",
            "eua - loteria americana",
            "ementa semanal",
            "enrollment form",
            "fap55_installation_and_set_up",
            "fatura_",
            "fatura-",
            "fattura",
            "ficha de candidatura",
            "ficha consular",
            "fi_cbp",
            "fi_sp_sa_cbp",
            "fid_cbp",
            "fpo1-",
            "fp1-",
            "funil_vendas",
            "gmail - arthur, seu volks",
            "historico escolar",
            "historico arthur",
            "historicoescolardigital",
            "horarios_publicacao",
            "im-ams",
            "info_privacy",
            "irpf",
            "istr_operative_banca_multicanale",
            "lavora_con_noi",
            "lettera clt",
            "lista-de-classificacao-definitiva",
            "loteria americana",
            "maconha",
            "malformacao-da-veia-de-galeno",
            "malformacao_da_veia_de_galeno",
            "marcos_desenvolvimento",
            "matricula ribeira",
            "metricas_monetizacao",
            "metrexato",
            "mi_electric_scooter",
            "mod_contratto",
            "modulo_richiesta_intervento",
            "nascimento_alice",
            "notafiscalvitrine",
            "ocean engineering, ph_d_ - florida tech",
            "onde_a_maconha",
            "orc 6640_mg - arthur ribeiro",
            "orientador",
            "organizacao_tarefas",
            "paciornik_perfil",
            "passaporto_arthur",
            "paises que exigem o certificado internacional",
            "planejamento_semanal",
            "plano+do+milhao",
            "plano do milhao",
            "plano_manus_organizacao",
            "pmusa brco- moodboard",
            "pmusa_es_100",
            "pmusa_escopo marcenaria",
            "poupatempo",
            "postepay",
            "postecert",
            "precario _ fees",
            "preçario _ fees",
            "prenotazione",
            "privacy",
            "prohibited_list",
            "protocolos de parceria cbr",
            "proposta transporte internacional de carga",
            "proposta 04_07_2025",
            "qav-2932019",
            "ra_checkout",
            "registro-online",
            "resultado_semanal_completo",
            "richiesta",
            "roteiro de atividade pratica",
            "roteiro(",
            "saude",
            "sicoob",
            "shorts",
            "tempos-verbais-presente",
            "termo_assinado",
            "termos_cursos_mentorias",
            "titulos_shorts",
            "titulos_videos_longos",
            "trabalho_ev161",
            "trafego_pago",
            "ugrhi03",
            "umweltzone",
            "vacin",
            "videos_longos",
        ),
    ),
    Rule(
        "10_Tecnico_Nautico/00_Documentacao_de_Campo_e_Clientes",
        (
            "analise_instalacao",
            "análise_instalação",
            "checklist_embarcacao",
            "declaracao_desembaraco_gerador",
            "declaracao_gerador_seco",
            "diagramas_",
            "diagrama_victron",
            "esboco_instalacao",
            "estudo_painel_garnet",
            "estudos_diagrama",
            "exigencias gerador dhl",
            "fornecimento de balsa",
            "gladiolo_descricao",
            "nota bomba combustivel",
            "nota usina",
            "orcamento n.",
            "ordem de servico n.",
            "ordem de serviço n.",
            "plano_preventivo_yanmar",
            "ptc 239_2024",
            "raphael_c_rj",
            "relatorio de avaliacao tecnica",
            "relatório de avaliação técnica",
            "relatorio e orcamento apos visita",
            "relatório e orçamento após visita",
            "relatorio tres marias",
            "relatório três marias",
            "suporte_radar",
            "veleiro seven",
        ),
    ),
    Rule(
        "10_Tecnico_Nautico/01_Geradores",
        (
            "0981-",
            "10850om",
            "17.5mdkae",
            "32002om",
            "40457_rev",
            "70384om",
            "7953_hdkah",
            "8731",
            "8732",
            "900-0541b-energy-command-operation",
            "934-0602",
            "981-",
            "a029z105",
            "a050g574",
            "a052j727",
            "egc",
            "fischer panda",
            "folheto gerador",
            "generator",
            "genset",
            "gerador",
            "geradores ca",
            "hdk",
            "kohler",
            "manual-gerador",
            "manual gerador",
            "manual_egc",
            "mcck",
            "mdk",
            "modulo1_geradores",
            "northen lights",
            "northern lights",
            "onan",
            "panda_",
            "panda-",
            "panda_15mini",
            "panda_4200",
            "panda_4k",
            "panda_7k",
            "panda_7mini",
            "qd 4-5",
            "qd 6-8",
            "qd 7-9",
            "qd 9-13",
        ),
    ),
    Rule(
        "10_Tecnico_Nautico/02_Climatizacao",
        (
            "a-c",
            "air-condition",
            "air conditioner",
            "ar-condicionado",
            "blower",
            "chilled",
            "climatizacao",
            "cruisair",
            "dometic",
            "frigo",
            "hfc-acqua",
            "mabru",
            "marine-air",
            "mtcg",
            "self-contained",
        ),
    ),
    Rule(
        "10_Tecnico_Nautico/03_Baterias_e_DC",
        (
            "12 volt",
            "12v",
            "alternador",
            "bateria",
            "battery",
            "bch-opt-41",
            "carregador",
            "charger",
            "digital-multi-control",
            "divisores de carga",
            "energy command",
            "eolico",
            "freedom hf",
            "freedom_combie",
            "ind_12_en",
            "inversora",
            "inversor",
            "inverter",
            "kisae",
            "manual-bpp2",
            "manual fonte usina",
            "manual kisae",
            "manual mastervolts",
            "manual quick sbc",
            "manual smart volt amp",
            "mastervolt",
            "pys_dc_overview",
            "quick sbc",
            "qb_export_neutral_12lc-150",
            "qb_neutral_12lc-150",
            "solar",
            "tipos de bateria",
            "usb (power 12v)",
            "usina",
            "victron",
            "voltimetro amperimetro",
        ),
    ),
    Rule(
        "10_Tecnico_Nautico/04_Shore_Power_e_AC",
        (
            "acti9",
            "cais (pier)",
            "catalogo-chave-rotativa",
            "chaves seletoras",
            "conimel",
            "contatores (ac)",
            "cps18_xsa_60hz",
            "diagrama 220v ac",
            "disjuntores (dc) e (ac)",
            "fase e neutro",
            "linha leve (ac)",
            "linha pesada (ac)",
            "nbr 05410",
            "nbr 5410",
            "protecao dr",
            "protection dr",
            "shore",
            "transformador entrada",
        ),
    ),
    Rule(
        "10_Tecnico_Nautico/05_Navegacao_e_Eletronicos",
        (
            "arquivocorte display ghc50",
            "cabos e conexao raymarine seatalk",
            "camera_farol_radar",
            "can bus",
            "fi5002",
            "furuno",
            "fusion",
            "fx503",
            "garmin",
            "gps",
            "gpsmap",
            "gx2000",
            "interbus",
            "jl audio",
            "network_expansion_port",
            "nrx300",
            "nx403",
            "nx404",
            "piloto automatico",
            "piloto automático",
            "por_raymarine_manu_quantum",
            "quantum",
            "radar",
            "raymarine",
            "seatalk",
            "smartpilot",
            "som ",
            "som_",
            "transducer",
            "vhf",
        ),
    ),
    Rule(
        "10_Tecnico_Nautico/06_Bombas_Hidraulica_e_Utilidades",
        (
            "agua pressurizada",
            "bomba",
            "boiler",
            "caixa de agua cinza",
            "caixa de agua",
            "dessanilizador",
            "document-91095466-installation-guide-mini-pressurizador",
            "gulper",
            "hotline",
            "installation and user's manual _ titan horizontal",
            "johnson-pump",
            "manual_bomba_pulmao",
            "pump",
            "pressur",
            "syllent",
            "toilet",
            "whale-2023",
        ),
    ),
    Rule(
        "10_Tecnico_Nautico/07_Iluminacao_Sinalizacao_e_Acessorios",
        (
            "buzina",
            "farol de busca",
            "lumishore",
            "luz de cortesia",
            "luz subaquatica",
            "luzes internas teto",
            "programacao do controle remoto",
            "programação do controle remoto",
            "strobo",
        ),
    ),
    Rule(
        "10_Tecnico_Nautico/08_Corrosao_Bonding_e_Seguranca",
        (
            "aluminio",
            "anodo",
            "aterramento",
            "corrosao",
            "eletrolise",
            "meggertest",
            "schooner",
            "seguranca",
        ),
    ),
    Rule(
        "10_Tecnico_Nautico/09_Propulsao_Motores_Estabilizacao_e_Atuacao",
        (
            "3tnc",
            "5eoz",
            "6eod",
            "a65",
            "atuador linear",
            "b185-m843",
            "bow-thruster",
            "cat marine",
            "engines_for_planing_boats",
            "engines for planing boats",
            "flap",
            "grt7-th4",
            "grta-4",
            "guincho",
            "jh_series",
            "jh series",
            "lewmar",
            "macs",
            "man-mc2-x10",
            "manual telecomandos",
            "manual-telecomandos",
            "manual-zen",
            "mc2_x",
            "mn700",
            "mn900",
            "new2015_twd_bow-thruster",
            "om843",
            "operators_manual_d124x",
            "operators_manual_tad",
            "p843-3",
            "scania",
            "servicemanualtneseries",
            "sp30s2i-sp40s2i-sp55s2i",
            "th220b",
            "th330b",
            "thruster",
            "tp6053",
            "tp6252",
            "tp6255",
            "tp6270",
            "tp6772",
            "tp6775",
            "twd_bcshydraulicsteeringsystems",
            "v1-v6 windlass",
            "volvo",
            "vw150",
            "vw5cylinder",
            "yanmar",
            "ydes04",
            "zen150",
            "zen30",
        ),
    ),
    Rule(
        "10_Tecnico_Nautico/10_Materiais_Internos_e_Cursos",
        (
            "folder eletricista",
            "folder gestor de marinas",
            "folder mecanica de motores de popa",
            "folder_yata_motores",
            "fundamentos da eletrica nautica",
            "fundamentos_eletrica_nautica",
            "logo eletro nautica",
            "manual0305",
            "manual0409-0413",
            "manual dni 0409-0413",
            "zen.png",
        ),
    ),
)

TECH_EXPORT_KEYWORDS = (
    "ac)",
    "alternador",
    "anodo",
    "arranque",
    "aterramento",
    "atuador",
    "bancos de bateria",
    "blower",
    "boiler",
    "bomba",
    "buzina",
    "carregador",
    "casa de maquinas",
    "chaves gerais",
    "chaves seletoras",
    "contatores",
    "corrosao",
    "dessanilizador",
    "disjuntores",
    "divisores de carga",
    "eletrolise",
    "eolico",
    "estabilizador",
    "fase e neutro",
    "farol de busca",
    "fundamentos da eletrica nautica",
    "gerador",
    "guincho",
    "hotline",
    "ilumin",
    "inversora",
    "limpador de parabrisas",
    "linha leve",
    "linha pesada",
    "luz",
    "navegacao",
    "piloto automatico",
    "placa solar",
    "principios nauticos",
    "protecao dr",
    "radar",
    "sensor de nivel",
    "som",
    "strob",
    "thruster",
    "tipos de bateria",
    "tipos de embarcacao",
    "top ",
    "transformador entrada",
    "usb (power 12v)",
    "vhf",
)


def classify(path: Path) -> str:
    name = normalize(path.name)
    extension = path.suffix.lower()

    for rule in RULES:
        if has_any(name, rule.keywords):
            return rule.destination

    if extension in {".html", ".md"} and has_any(name, TECH_EXPORT_KEYWORDS):
        return "10_Tecnico_Nautico/11_HTML_Tecnico_Exportado"

    if extension in NON_TECH_DOC_EXTENSIONS:
        return "00_Fora_do_Escopo_ou_Pessoal"

    if extension in IMAGE_EXTENSIONS and any(
        token in name for token in ("logo eletro nautica", "zen", "display ghc50")
    ):
        return "10_Tecnico_Nautico/10_Materiais_Internos_e_Cursos"

    if has_any(name, GENERIC_TECH_DOC_MARKERS):
        return "10_Tecnico_Nautico/90_Triagem_Tecnica_por_Codigo"

    if extension == ".pdf" or extension in IMAGE_EXTENSIONS:
        return "10_Tecnico_Nautico/90_Triagem_Tecnica_por_Codigo"

    return "00_Fora_do_Escopo_ou_Pessoal"


def source_files() -> list[Path]:
    return sorted(path for path in ARCHIVE_ROOT.iterdir() if path.is_file())


def organize(apply_changes: bool) -> tuple[Counter[str], list[tuple[str, str]]]:
    counts: Counter[str] = Counter()
    moves: list[tuple[str, str]] = []

    for source in source_files():
        destination = ARCHIVE_ROOT / classify(source)
        target = destination / source.name
        counts[destination.relative_to(ARCHIVE_ROOT).as_posix()] += 1
        moves.append((source.name, target.relative_to(ARCHIVE_ROOT).as_posix()))

        if not apply_changes:
            continue

        destination.mkdir(parents=True, exist_ok=True)
        if target.exists():
            if target.samefile(source):
                continue
            raise FileExistsError(f"Destino já existe: {target}")
        shutil.move(io_path(source), io_path(target))

    return counts, moves


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Organiza o conteúdo bruto de 'Acervo do humano' em subpastas temáticas."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Move os arquivos de fato. Sem esta flag, apenas mostra o plano.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Quantidade de movimentos exibidos na prévia.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    counts, moves = organize(apply_changes=args.apply)

    mode = "APLICADO" if args.apply else "DRY-RUN"
    print(f"Modo: {mode}")
    print(f"Arquivos avaliados: {len(moves)}")
    print("")
    print("Resumo por destino:")
    for destination, count in sorted(counts.items()):
        print(f"- {destination}: {count}")

    preview = moves[: max(args.limit, 0)]
    if preview:
        print("")
        print("Prévia de movimentos:")
        for source_name, relative_target in preview:
            print(f"- {source_name} -> {relative_target}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
