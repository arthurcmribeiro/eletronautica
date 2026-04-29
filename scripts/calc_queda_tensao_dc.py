"""Calculadora de dimensionamento de cabos DC para embarcacoes.

Aplica os dois criterios classicos de dimensionamento e retorna o AWG minimo
vencedor, com warnings de contexto:

1. Queda de tensao: delta_V = I * R_cabo; R_cabo = rho * L / A_secao
   Limite tipico ABYC E-11 (2023): 3% circuitos criticos, 10% nao-criticos.

2. Ampacidade: capacidade de corrente do cabo sem superaquecer.
   Valores tabela ABYC E-11 a 30C, com fator de temperatura para
   casa de maquinas tipica (ate 60C) e fator de agrupamento.

O AWG recomendado e o MAIOR (mais grosso) dos dois criterios.

Uso basico:
    python scripts/calc_queda_tensao_dc.py \\
        --potencia 3000 --tensao 24 --comprimento 6

Com temperatura e agrupamento:
    python scripts/calc_queda_tensao_dc.py \\
        --potencia 3000 --tensao 24 --comprimento 6 \\
        --queda-pct 3 --temperatura 50 --cabos-agrupados 3

Dependencias: stdlib.

Referencias:
- 10_Fundamentos_e_Projeto/Dimensionamento de Cabos DC - Calculo Pratico.md
- ABYC E-11 (2023): AC and DC Electrical Systems on Boats
- ISO 13297:2020: Small craft - Electrical systems - AC/DC installations
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from typing import Optional

# Resistividade do cobre a 20C, em Ohm * mm^2 / m.
# (O valor sobe ligeiramente com a temperatura, mas a ABYC usa 0.0175 como
# referencia de projeto para simplificar.)
RHO_COBRE = 0.0175

# Tabela AWG -> (secao_mm2, ampacidade_30C_A).
# Valores aproximados ABYC E-11 Table 6 (2023), cabo no interior da
# embarcacao, temperatura ambiente 30C, nao em feixe.
# Para projetos reais consultar tabela completa da norma.
AWG_TABLE = [
    # (awg, secao_mm2, ampacidade_30C)
    ("18", 0.82, 10),
    ("16", 1.31, 15),
    ("14", 2.08, 20),
    ("12", 3.31, 25),
    ("10", 5.26, 40),
    ("8",  8.37, 55),
    ("6", 13.30, 80),
    ("4", 21.15, 105),
    ("2", 33.62, 140),
    ("1", 42.41, 165),
    ("1/0", 53.48, 195),
    ("2/0", 67.42, 225),
    ("3/0", 85.02, 260),
    ("4/0", 107.22, 300),
]

# Fator de temperatura: multiplicador da ampacidade tabelada (30C).
# ABYC E-11 2023 Table 6A (valores aproximados, isolacao 105C).
TEMP_DERATING = {
    30: 1.00,
    40: 0.91,
    50: 0.82,
    60: 0.71,
    70: 0.58,
    80: 0.41,
}

# Fator de agrupamento (multiplicador) - numero de condutores carregados.
# Aproximacao simplificada do metodo de de-rating por feixe.
GROUPING_DERATING = {
    1: 1.00,
    2: 1.00,
    3: 0.70,
    4: 0.70,
    6: 0.60,
    9: 0.50,
}


@dataclass
class Resultado:
    awg_recomendado: str
    secao_mm2: float
    criterio_vencedor: str   # "queda_tensao" | "ampacidade"
    queda_calculada_V: float
    queda_calculada_pct: float
    ampacidade_efetiva_A: float
    avisos: list[str]


def fator_temperatura(temperatura: int) -> float:
    """Interpolacao linear em TEMP_DERATING. Clamped em 30..80."""
    if temperatura <= 30:
        return 1.0
    if temperatura >= 80:
        return TEMP_DERATING[80]
    # interpolacao linear entre pontos
    chaves = sorted(TEMP_DERATING.keys())
    for i in range(len(chaves) - 1):
        t0, t1 = chaves[i], chaves[i + 1]
        if t0 <= temperatura <= t1:
            f0, f1 = TEMP_DERATING[t0], TEMP_DERATING[t1]
            return f0 + (f1 - f0) * (temperatura - t0) / (t1 - t0)
    return 1.0


def fator_agrupamento(cabos_agrupados: int) -> float:
    if cabos_agrupados <= 2:
        return GROUPING_DERATING[1]
    if cabos_agrupados in GROUPING_DERATING:
        return GROUPING_DERATING[cabos_agrupados]
    # Para valores intermediarios, aproximar para o menor fator conhecido
    chaves = sorted(GROUPING_DERATING.keys())
    fator = 1.0
    for k in chaves:
        if cabos_agrupados >= k:
            fator = GROUPING_DERATING[k]
    return fator


def queda_tensao(corrente_A: float, comprimento_total_m: float, secao_mm2: float) -> float:
    """Retorna queda de tensao em Volts sobre um cabo de dado comprimento.

    comprimento_total_m e o RUN COMPLETO (ida + volta).
    """
    resistencia_cabo = RHO_COBRE * comprimento_total_m / secao_mm2
    return corrente_A * resistencia_cabo


def dimensionar(
    potencia_W: float,
    tensao_V: float,
    comprimento_fisico_m: float,
    queda_pct: float,
    temperatura: int,
    cabos_agrupados: int,
    margem_corrente: float,
) -> Resultado:
    corrente = potencia_W / tensao_V
    corrente_projeto = corrente * (1 + margem_corrente)
    comprimento_total = 2 * comprimento_fisico_m   # ida + volta
    queda_max_V = tensao_V * (queda_pct / 100.0)

    f_temp = fator_temperatura(temperatura)
    f_agrup = fator_agrupamento(cabos_agrupados)

    avisos: list[str] = []
    if temperatura >= 50:
        avisos.append(
            f"Temperatura {temperatura}C aplica de-rating {f_temp:.2f}x na ampacidade"
        )
    if cabos_agrupados >= 3:
        avisos.append(
            f"Agrupamento de {cabos_agrupados} cabos aplica de-rating {f_agrup:.2f}x"
        )

    # Criterio 1: queda de tensao
    awg_queda = None
    queda_final_V = 0.0
    for awg, secao, _ in AWG_TABLE:
        dv = queda_tensao(corrente_projeto, comprimento_total, secao)
        if dv <= queda_max_V:
            awg_queda = (awg, secao)
            queda_final_V = dv
            break

    # Criterio 2: ampacidade
    awg_amp = None
    amp_efetiva = 0.0
    for awg, secao, amp_tab in AWG_TABLE:
        amp_eff = amp_tab * f_temp * f_agrup
        if amp_eff >= corrente_projeto:
            awg_amp = (awg, secao)
            amp_efetiva = amp_eff
            break

    if awg_queda is None and awg_amp is None:
        avisos.append(
            "Nenhum AWG na tabela atende; considerar paralelismo de condutores "
            "ou sistema de maior tensao"
        )
        return Resultado(
            awg_recomendado="N/A",
            secao_mm2=0.0,
            criterio_vencedor="nenhum",
            queda_calculada_V=0.0,
            queda_calculada_pct=0.0,
            ampacidade_efetiva_A=0.0,
            avisos=avisos,
        )

    # AWG recomendado = o mais grosso (maior secao) dos dois criterios
    if awg_queda is None:
        assert awg_amp is not None
        escolhido = awg_amp
        criterio = "ampacidade"
    elif awg_amp is None:
        escolhido = awg_queda
        criterio = "queda_tensao"
    else:
        if awg_queda[1] >= awg_amp[1]:
            escolhido = awg_queda
            criterio = "queda_tensao"
        else:
            escolhido = awg_amp
            criterio = "ampacidade"

    # Recalcular numeros finais para o AWG escolhido
    awg_final, secao_final = escolhido
    queda_final_V = queda_tensao(corrente_projeto, comprimento_total, secao_final)
    queda_final_pct = (queda_final_V / tensao_V) * 100

    # Encontrar ampacidade efetiva do escolhido
    amp_efetiva = 0.0
    for awg, _, amp_tab in AWG_TABLE:
        if awg == awg_final:
            amp_efetiva = amp_tab * f_temp * f_agrup
            break

    if queda_final_pct > queda_pct + 0.5:
        avisos.append(
            f"Queda final {queda_final_pct:.1f}% supera alvo {queda_pct}% "
            "por limite da tabela AWG"
        )

    return Resultado(
        awg_recomendado=awg_final,
        secao_mm2=secao_final,
        criterio_vencedor=criterio,
        queda_calculada_V=queda_final_V,
        queda_calculada_pct=queda_final_pct,
        ampacidade_efetiva_A=amp_efetiva,
        avisos=avisos,
    )


def imprimir_relatorio(
    potencia: float, tensao: float, comprimento: float,
    queda_pct: float, temperatura: int, cabos_agrupados: int,
    margem: float, res: Resultado,
) -> None:
    corrente = potencia / tensao
    corrente_projeto = corrente * (1 + margem)
    comp_total = 2 * comprimento
    queda_max = tensao * (queda_pct / 100)

    print("=" * 80)
    print("DIMENSIONAMENTO DC - calc_queda_tensao_dc.py")
    print("=" * 80)
    print(f"Potencia:         {potencia:.0f} W")
    print(f"Tensao sistema:   {tensao:.0f} V")
    print(f"Corrente:         {corrente:.1f} A  "
          f"(com margem {margem*100:.0f}%: {corrente_projeto:.1f} A)")
    print(f"Run total:        {comp_total:.1f} m  (ida + volta)")
    print(f"Queda maxima:     {queda_pct}% -> {queda_max:.3f} V")
    print(f"Temperatura:      {temperatura}C "
          f"(fator: {fator_temperatura(temperatura):.2f})")
    if cabos_agrupados >= 3:
        print(f"Agrupamento:      {cabos_agrupados} cabos "
              f"(fator: {fator_agrupamento(cabos_agrupados):.2f})")
    print("-" * 80)
    if res.awg_recomendado == "N/A":
        print("RESULTADO: nenhum AWG na tabela atende - rever projeto")
    else:
        print(f"AWG recomendado:     {res.awg_recomendado}  "
              f"({res.secao_mm2:.1f} mm^2)")
        print(f"Criterio vencedor:   {res.criterio_vencedor}")
        print(f"Queda final:         {res.queda_calculada_V:.2f} V  "
              f"({res.queda_calculada_pct:.1f}%)")
        print(f"Ampacidade efetiva:  {res.ampacidade_efetiva_A:.0f} A")
    print("-" * 80)
    if res.avisos:
        print("Avisos:")
        for aviso in res.avisos:
            print(f"  - {aviso}")
    else:
        print("Sem avisos.")
    print("=" * 80)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Calculadora de dimensionamento de cabos DC para embarcacoes",
    )
    parser.add_argument("--potencia", type=float, required=True,
                        help="potencia do equipamento em Watts")
    parser.add_argument("--tensao", type=float, required=True,
                        help="tensao do sistema em Volts (12, 24 ou 48)")
    parser.add_argument("--comprimento", type=float, required=True,
                        help="comprimento fisico do cabo em metros (um sentido)")
    parser.add_argument("--queda-pct", type=float, default=3.0,
                        help="queda maxima admitida em %% (padrao 3%% - critico)")
    parser.add_argument("--temperatura", type=int, default=30,
                        help="temperatura ambiente em C (padrao 30C)")
    parser.add_argument("--cabos-agrupados", type=int, default=1,
                        help="numero de cabos carregados no mesmo feixe (padrao 1)")
    parser.add_argument("--margem", type=float, default=0.25,
                        help="margem de corrente sobre a nominal (padrao 25%%)")
    parser.add_argument("--quiet", action="store_true",
                        help="imprime apenas o AWG recomendado (para scripts)")
    args = parser.parse_args()

    if args.tensao not in (12, 24, 36, 48):
        print(f"AVISO: tensao {args.tensao}V nao usual em embarcacoes; "
              "valores suportados tipicos: 12, 24, 48", file=sys.stderr)

    res = dimensionar(
        potencia_W=args.potencia,
        tensao_V=args.tensao,
        comprimento_fisico_m=args.comprimento,
        queda_pct=args.queda_pct,
        temperatura=args.temperatura,
        cabos_agrupados=args.cabos_agrupados,
        margem_corrente=args.margem,
    )

    if args.quiet:
        print(res.awg_recomendado)
    else:
        imprimir_relatorio(
            args.potencia, args.tensao, args.comprimento,
            args.queda_pct, args.temperatura, args.cabos_agrupados,
            args.margem, res,
        )

    if res.awg_recomendado == "N/A":
        return 2
    if any("supera" in a for a in res.avisos):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
