"""
==============================================================================
Module:      time_series_analysis.py
Description: Moving average and naive time-series forecasting models with Mean
             Squared Error (MSE) accuracy evaluation and plotting.
==============================================================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, Tuple, Optional


def evaluate_forecast_methods(weeks: np.ndarray, registrations: np.ndarray) -> Tuple[Dict[str, np.ndarray], Dict[str, float]]:
    """
    Fuehrt Naive-, 2-Wochen- und 4-Wochen-Glaettungen durch und misst den MSE.
    """
    # 1. Naive Prognose (um 1 Periode versetzt)
    naive = np.append([np.nan], registrations[:-1])

    # 2. Gleitender Durchschnitt (2 Wochen)
    ma_2 = np.append([np.nan, np.nan], pd.Series(registrations).rolling(2).mean().iloc[2:].values)

    # 3. Gleitender Durchschnitt (4 Wochen)
    ma_4 = np.append([np.nan, np.nan, np.nan, np.nan], pd.Series(registrations).rolling(4).mean().iloc[4:].values)

    def calc_mse(actual, pred):
        return float(np.nanmean((actual - pred) ** 2))

    mse_scores = {
        "Naive": calc_mse(registrations[1:], naive[1:]),
        "2-Week MA": calc_mse(registrations[2:], ma_2[2:]),
        "4-Week MA": calc_mse(registrations[4:], ma_4[4:]),
    }

    forecasts = {
        "Naive": naive,
        "2-Week MA": ma_2,
        "4-Week MA": ma_4,
    }

    return forecasts, mse_scores


def plot_registration_forecasts(weeks: np.ndarray, registrations: np.ndarray,
                                forecasts: Dict[str, np.ndarray], save_path: Optional[str] = None):
    """Erzeugt ein Vergleichsdiagramm der Prognoseverfahren."""
    plt.figure(figsize=(10, 6))
    plt.plot(weeks, registrations, label="Tatsaechliche Registrierungen", marker='o', color='black', linewidth=2)
    plt.plot(weeks, forecasts["Naive"], label="Naive Prognose", marker='x', linestyle='--')
    plt.plot(weeks, forecasts["2-Week MA"], label="2-Wochen MA Prognose", marker='s', linestyle=':')
    plt.plot(weeks, forecasts["4-Week MA"], label="4-Wochen MA Prognose", marker='d', linestyle='-.')

    plt.xlabel("Woche", fontsize=11)
    plt.ylabel("Registrierungen", fontsize=11)
    plt.title("Vergleich quantitativer Zeitreihenprognosen", fontsize=13)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
    else:
        plt.show()


if __name__ == "__main__":
    w = np.arange(1, 11)
    r = np.array([22, 21, 25, 27, 35, 29, 33, 37, 41, 37])
    fc, mse = evaluate_forecast_methods(w, r)
    print("MSE Fehlermetriken:", mse)
