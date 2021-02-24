
import sys
from collections import defaultdict

from src.course4.week1.bellman_ford import compute_single_source_shortest_paths as bellman_ford_shortest_paths
from src.course2.week2.dijkstra_heapq import dijkstra as dijkstra_shortest_paths


def compute_all_pairs_shortest_paths(graph):
    graph, augmented_source = _augment_graph(graph)
    shortest_paths, _ = bellman_ford_shortest_paths(graph, augmented_source)
    del graph[augmented_source]

    if (shortest_paths is None):
        return None  # negative cycle detected

    graph_non_negative_edges = _reweigh_graph(graph, shortest_paths)

    all_pairs_shortest_paths = {}
    for v in graph_non_negative_edges:
        all_pairs_shortest_paths[v] = dijkstra_shortest_paths(
            graph_non_negative_edges, v)

    for v1 in all_pairs_shortest_paths:
        for v2 in all_pairs_shortest_paths[v1]:
            if all_pairs_shortest_paths[v1][v2] == sys.maxsize:
                continue

            all_pairs_shortest_paths[v1][v2] = all_pairs_shortest_paths[v1][v2] - \
                shortest_paths[v1] + shortest_paths[v2]

    return all_pairs_shortest_paths


def _augment_graph(graph):
    n = len(graph)
    augmented_source = n + 1

    zero_weight_edges = []
    for v in graph:
        zero_weight_edges.append((v, 0))

    graph[augmented_source] = zero_weight_edges

    return graph, augmented_source


def _reweigh_graph(graph, shortest_paths):
    graph_non_negative_edges = defaultdict(list)
    for tail in graph:
        for head, weight in graph[tail]:
            graph_non_negative_edges[tail].append(
                (head, weight + shortest_paths[tail] - shortest_paths[head]))

        if not graph[tail]:
            graph_non_negative_edges[tail] = []

    return graph_non_negative_edges
