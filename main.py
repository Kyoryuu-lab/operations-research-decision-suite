"""
==============================================================================
Project:     Operations Research & Decision Intelligence Suite
File:        main.py
Author:      Yevhen Biezhyn
Description: Unified CLI orchestrator executing Linear Programming, Graph
             Routing (TSP & Dijkstra), Decision Theory (EMV, EVPI, AHP),
             and Time-Series Forecasting.
==============================================================================
"""

import argparse
import numpy as np

from modules.linear_programming import solve_lp_problem, plot_feasible_region
from modules.network_routing import (
    solve_tsp_bruteforce,
    find_shortest_path_dijkstra,
    find_multistage_waypoint_path
)
from modules.decision_analysis import (
    calculate_emv_and_evpi,
    analyze_probability_sensitivity,
    calculate_ahp_local_priorities
)
from modules.time_series_analysis import (
    evaluate_forecast_methods,
    plot_registration_forecasts
)


def print_banner(title: str):
    print("\n" + "=" * 78)
    print(f"  {title.upper()}")
    print("=" * 78)


def run_linear_programming_suite(save_plots: bool = False):
    print_banner("1. Modul: Lineare Programmierung & Zulaessiger Bereich")
    success, opt_solution, opt_val = solve_lp_problem()
    print(f"[*] HiGHS Solver Konvergenz : {success}")
    print(f"[*] Optimale Variablenbelegung: x1 = {opt_solution[0]:.4f}, x2 = {opt_solution[1]:.4f}")
    print(f"[*] Minimaler Zielfunktionswert: {opt_val:.4f}")

    plot_path = "lp_feasible_region.png" if save_plots else None
    plot_feasible_region(save_path=plot_path)
    if save_plots:
        print(f"[+] LP-Diagramm gespeichert unter: {plot_path}")


def run_network_routing_suite():
    print_banner("2. Modul: Graphentheorie & Netzwerk-Routing")

    # 2.1 TSP Brute-Force
    dist_matrix = [
        [0, 250, 300, 400, 350],
        [250, 0, 450, 500, 550],
        [300, 450, 0, 200, 250],
        [400, 500, 200, 0, 150],
        [350, 550, 250, 150, 0]
    ]
    best_path, min_dist = solve_tsp_bruteforce(dist_matrix, start_city=0)
    city_names = [f"B{i}" for i in best_path]
    print(f"[*] TSP Kuerzeste Rundreise : {' -> '.join(city_names)}")
    print(f"[*] Minimale Gesamtstrecke  : {min_dist} km")

    # 2.2 Kürzester Weg nach Dijkstra (Knoten 1 -> 11)
    dijkstra_edges = [
        (1, 2, 7), (1, 4, 5), (2, 3, 2), (2, 5, 4), (3, 6, 5),
        (4, 5, 4), (4, 7, 6), (5, 6, 4), (5, 8, 8), (6, 9, 3),
        (7, 8, 5), (7, 10, 9), (8, 9, 2), (9, 11, 6), (10, 11, 1)
    ]
    path_dijkstra, cost_dijkstra = find_shortest_path_dijkstra(dijkstra_edges, source=1, target=11)
    print(f"[*] Kuerzester Pfad (1 -> 11) : {' -> '.join(map(str, path_dijkstra))}")
    print(f"[*] Minimale Pfadkosten       : {cost_dijkstra}")

    # 2.3 Mehrstufige Wegpunkt-Route (1 -> A(4) -> B(7) -> C(10) -> 11)
    multistage_edges = [
        (1, 2, 7), (1, 3, 6), (1, 4, 5),
        (2, 5, 5), (2, 6, 8), (2, 8, 4),
        (3, 5, 7), (3, 6, 10), (3, 7, 4),
        (4, 6, 7), (4, 7, 2), (4, 10, 2),
        (5, 8, 8), (5, 9, 7),
        (6, 8, 7), (6, 9, 6),
        (7, 9, 8), (7, 10, 2),
        (8, 11, 10), (9, 11, 6), (10, 11, 18)
    ]
    waypoints = [1, 4, 7, 10, 11]
    ms_path, ms_cost = find_multistage_waypoint_path(multistage_edges, waypoints)
    print(f"[*] Meilenstein-Pfad (1->4->7->10->11): {' -> '.join(map(str, ms_path))}")
    print(f"[*] Gesamtlaenge Meilenstein-Route   : {ms_cost}")


def run_decision_analysis_suite():
    print_banner("3. Modul: Entscheidungstheorie & AHP")

    # 3.1 EMV & EVPI
    profits = {
        "A1": [20000, 10000, -2000],
        "A2": [15000, 12000, 6000],
        "A3": [9000, 6000, 5000],
    }
    probs = [0.3, 0.5, 0.2]
    emv_dict, exp_perf_info, evpi_val = calculate_emv_and_evpi(profits, probs)

    print("[*] Erwartete Geldwerte (EMV):")
    for alt, val in emv_dict.items():
        print(f"    - {alt}: {val:10.2f} EUR")
    print(f"[*] Erwartungswert bei vollkommener Information: {exp_perf_info:.2f} EUR")
    print(f"[*] Wert vollkommener Information (EVPI)        : {evpi_val:.2f} EUR")

    # 3.2 Symbolische Sensitivitätsanalyse (SymPy)
    p_s_range = analyze_probability_sensitivity(profits, fixed_p_large=0.3)
    print(f"[*] Sensitivitaetsschwelle: Alternative A3 dominiert A1 fuer P_S in: {p_s_range}")

    # 3.3 AHP Saaty Paarvergleiche
    c1_mat = np.array([[1, 1/3, 1/7], [3, 1, 1/5], [7, 5, 1]])
    c2_mat = np.array([[1, 7, 5], [1/7, 1, 1/3], [1/5, 3, 1]])
    c3_mat = np.array([[1, 1/3, 1], [3, 1, 3], [1, 1/3, 1]])

    p1 = calculate_ahp_local_priorities(c1_mat)
    p2 = calculate_ahp_local_priorities(c2_mat)
    p3 = calculate_ahp_local_priorities(c3_mat)

    print("\n[*] AHP Lokale Prioritaetsvektoren (A1, A2, A3):")
    print(f"    - Kriterium 1: [{', '.join(f'{v:.4f}' for v in p1)}]")
    print(f"    - Kriterium 2: [{', '.join(f'{v:.4f}' for v in p2)}]")
    print(f"    - Kriterium 3: [{', '.join(f'{v:.4f}' for v in p3)}]")


def run_time_series_suite(save_plots: bool = False):
    print_banner("4. Modul: Zeitreihenprognose & Modell-Validierung")
    weeks = np.arange(1, 11)
    registrations = np.array([22, 21, 25, 27, 35, 29, 33, 37, 41, 37])

    forecasts, mse_scores = evaluate_forecast_methods(weeks, registrations)
    print("[*] Mittlere quadratische Fehler (MSE):")
    for name, score in mse_scores.items():
        print(f"    - {name:<12} : MSE = {score:.4f}")

    best_method = min(mse_scores, key=mse_scores.get)
    print(f"[+] Genauestes Prognosemodell: {best_method}")

    plot_path = "forecast_comparison.png" if save_plots else None
    plot_registration_forecasts(weeks, registrations, forecasts, save_path=plot_path)
    if save_plots:
        print(f"[+] Prognose-Diagramm gespeichert unter: {plot_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Operations Research & Decision Intelligence Suite",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "--module",
        choices=["all", "lp", "routing", "decision", "forecasting"],
        default="all",
        help=(
            "all         : Fuehrt die gesamte Suite aus (Standard)\n"
            "lp          : Lineare Programmierung (HiGHS Solver & Plot)\n"
            "routing     : TSP & Kuerzeste-Wege-Routing (NetworkX)\n"
            "decision    : EMV, EVPI, SymPy Sensitivitaet & Saaty-AHP\n"
            "forecasting : Zeitreihenprognosen und MSE-Vergleich"
        )
    )
    parser.add_argument("--save-plots", action="store_true", help="Speichert Matplotlib-Diagramme als PNG-Dateien")
    args = parser.parse_args()

    dispatch = {
        "lp": lambda: run_linear_programming_suite(args.save_plots),
        "routing": run_network_routing_suite,
        "decision": run_decision_analysis_suite,
        "forecasting": lambda: run_time_series_suite(args.save_plots),
    }

    if args.module == "all":
        for fn in dispatch.values():
            fn()
    else:
        dispatch[args.module]()

    print("\n" + "=" * 78)
    print("  AUSFUEHRUNG ERFOLGREICH ABGESCHLOSSEN.")
    print("=" * 78 + "\n")


if __name__ == "__main__":
    main()
