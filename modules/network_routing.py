"""
==============================================================================
Module:      network_routing.py
Description: Traveling Salesperson Problem (TSP) brute-force solver and
             graph-based shortest-path routing using NetworkX.
==============================================================================
"""

import itertools
import networkx as nx
from typing import List, Tuple, Optional


def solve_tsp_bruteforce(distance_matrix: List[List[int]], start_city: int = 0) -> Tuple[List[int], float]:
    """
    Loest das Traveling Salesperson Problem (TSP) ueber vollstaendige Enumeration aller Rundreisen.
    """
    n = len(distance_matrix)
    other_cities = [i for i in range(n) if i != start_city]

    min_distance = float('inf')
    best_path = None

    for perm in itertools.permutations(other_cities):
        current_path = [start_city] + list(perm) + [start_city]
        current_distance = sum(
            distance_matrix[current_path[i]][current_path[i + 1]]
            for i in range(len(current_path) - 1)
        )
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = current_path

    return best_path, min_distance


def find_shortest_path_dijkstra(edges: List[Tuple[int, int, int]], source: int, target: int) -> Tuple[List[int], int]:
    """Findet den kuerzesten Weg zwischen Start- und Zielknoten in einem gerichteten Graphen."""
    graph = nx.DiGraph()
    for u, v, w in edges:
        graph.add_edge(u, v, weight=w)

    path = nx.shortest_path(graph, source=source, target=target, weight='weight')
    cost = nx.shortest_path_length(graph, source=source, target=target, weight='weight')
    return path, cost


def find_multistage_waypoint_path(edges: List[Tuple[int, int, int]], waypoints: List[int]) -> Tuple[List[int], int]:
    """Berechnet einen kuerzesten Pfad ueber eine Kette aufeinanderfolgender Pflichtknoten (Meilensteine)."""
    graph = nx.DiGraph()
    graph.add_weighted_edges_from(edges)

    total_path = []
    total_cost = 0

    for i in range(len(waypoints) - 1):
        u = waypoints[i]
        v = waypoints[i + 1]
        sub_path = nx.shortest_path(graph, source=u, target=v, weight='weight')
        sub_cost = nx.shortest_path_length(graph, source=u, target=v, weight='weight')

        if i == 0:
            total_path.extend(sub_path)
        else:
            total_path.extend(sub_path[1:])
        total_cost += sub_cost

    return total_path, total_cost


if __name__ == "__main__":
    matrix = [
        [0, 250, 300, 400, 350],
        [250, 0, 450, 500, 550],
        [300, 450, 0, 200, 250],
        [400, 500, 200, 0, 150],
        [350, 550, 250, 150, 0]
    ]
    path, dist = solve_tsp_bruteforce(matrix, start_city=0)
    print(f"TSP Kuerzester Pfad: {path} | Distanz: {dist} km")
