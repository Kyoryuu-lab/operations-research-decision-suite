"""
==============================================================================
Module:      decision_analysis.py
Description: Decision theory under risk and uncertainty: Expected Monetary
             Value (EMV), EVPI, SymPy sensitivity analysis, and Analytic
             Hierarchy Process (AHP) priority calculation.
==============================================================================
"""

import numpy as np
from sympy import symbols, solve
from typing import Dict, List, Tuple


def calculate_emv_and_evpi(profits: Dict[str, List[float]], probabilities: List[float]) -> Tuple[Dict[str, float], float, float]:
    """
    Berechnet den Expected Monetary Value (EMV) jeder Alternative sowie
    den Erwarteten Wert vollkommener Information (EVPI).
    """
    p_large, p_avg, p_small = probabilities

    emv = {
        alt: p_large * vals[0] + p_avg * vals[1] + p_small * vals[2]
        for alt, vals in profits.items()
    }

    # Bestmoeglicher Gewinn je Umweltzustand
    max_state_large = max(vals[0] for vals in profits.values())
    max_state_avg = max(vals[1] for vals in profits.values())
    max_state_small = max(vals[2] for vals in profits.values())

    expected_perfect_info = (
        p_large * max_state_large +
        p_avg * max_state_avg +
        p_small * max_state_small
    )

    evpi = expected_perfect_info - max(emv.values())
    return emv, expected_perfect_info, evpi


def analyze_probability_sensitivity(profits: Dict[str, List[float]], fixed_p_large: float = 0.3):
    """
    Ermittelt mittels SymPy das Wahrscheinlichkeitsintervall fuer P_S,
    bei dem Alternative A3 einen hoeheren EMV als A1 erzielt.
    """
    p_s = symbols('P_S')
    p_l = fixed_p_large
    p_m = (1.0 - p_l) - p_s  # P_M = 0.7 - P_S

    emv_a1 = p_l * profits["A1"][0] + p_m * profits["A1"][1] + p_s * profits["A1"][2]
    emv_a3 = p_l * profits["A3"][0] + p_m * profits["A3"][1] + p_s * profits["A3"][2]

    condition = emv_a3 - emv_a1 > 0
    solution_interval = solve(condition, p_s)
    return solution_interval


def calculate_ahp_local_priorities(comparison_matrix: np.ndarray) -> np.ndarray:
    """
    Ermittelt den normierten Prioritaetsvektor einer Saaty-Paarvergleichsmatrix
    ueber Spaltennormierung und Zeilenmittelung.
    """
    matrix = np.asarray(comparison_matrix, dtype=float)
    col_sums = matrix.sum(axis=0)
    normalized = matrix / col_sums
    priorities = normalized.mean(axis=1)
    return priorities


if __name__ == "__main__":
    profit_data = {
        "A1": [20000, 10000, -2000],
        "A2": [15000, 12000, 6000],
        "A3": [9000, 6000, 5000],
    }
    emv_res, exp_perf, evpi_res = calculate_emv_and_evpi(profit_data, [0.3, 0.5, 0.2])
    print("EMV-Ergebnisse:", emv_res)
    print(f"EVPI: {evpi_res:.2f}")
