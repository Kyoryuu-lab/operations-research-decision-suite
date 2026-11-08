"""
==============================================================================
Module:      linear_programming.py
Description: Linear Programming (LP) numerical optimization and 2D feasible
             region graphical rendering.
==============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
from typing import Tuple, Optional


def solve_lp_problem() -> Tuple[bool, np.ndarray, float]:
    """
    Minimiert die Zielfunktion 2*x1 + 3*x2 unter linearen Ungleichungen:
      x1 + 2*x2 >= 18
      4*x1 + 3*x2 >= 48
      x1 >= 3, x2 >= 0
    """
    # Minimierung: 2*x1 + 3*x2
    c = [2, 3]

    # Umwandlung von >= b in <= -b fuer linprog
    a_ub = [
        [-1, -2],   # -x1 - 2*x2 <= -18
        [-4, -3],   # -4*x1 - 3*x2 <= -48
        [-1, 0],    # -x1 <= -3
    ]
    b_ub = [-18, -48, -3]

    x_bounds = (0, None)
    y_bounds = (0, None)

    res = linprog(c, A_ub=a_ub, b_ub=b_ub, bounds=[x_bounds, y_bounds], method='highs')
    return res.success, res.x, res.fun


def plot_feasible_region(save_path: Optional[str] = None):
    """Visualisiert und schattiert den zulaessigen Bereich des Optimierungsproblems."""
    x1 = np.linspace(0, 25, 500)

    # Randgeraden der Restriktionen
    x2_1 = (18 - x1) / 2.0        # x1 + 2*x2 >= 18
    x2_2 = (48 - 4 * x1) / 3.0    # 4*x1 + 3*x2 >= 48

    x2_1 = np.maximum(0, x2_1)
    x2_2 = np.maximum(0, x2_2)

    plt.figure(figsize=(8, 6))
    plt.plot(x1, x2_1, label=r'$x_1 + 2x_2 \geq 18$', color='blue')
    plt.plot(x1, x2_2, label=r'$4x_1 + 3x_2 \geq 48$', color='green')
    plt.axvline(3, label=r'$x_1 \geq 3$', color='red', linestyle='--')

    # Schattierung des zulaessigen Loesungsraums
    y_lower = np.maximum(x2_1, x2_2)
    plt.fill_between(x1, y_lower, 20, where=(x1 >= 3), color='gray', alpha=0.35, label='Zulaessiger Bereich (Feasible Region)')

    plt.xlim(0, 20)
    plt.ylim(0, 20)
    plt.xlabel(r'$x_1$')
    plt.ylabel(r'$x_2$')
    plt.title('Lineare Programmierung: Zulaessiger Bereich und Restriktionen')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
    else:
        plt.show()


if __name__ == "__main__":
    success, opt_x, opt_val = solve_lp_problem()
    print(f"LP geloest: {success} | Optimum x: {opt_x} | Minimaler Zielfunktionswert: {opt_val}")
