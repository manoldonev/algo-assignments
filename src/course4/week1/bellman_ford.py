
import sys

from collections import defaultdict


def compute_single_source_shortest_paths(graph, source, reconstruct_shortest_paths=False):
    # vertex indexing in "graph" is 1-based but subproblem implementation is 0-based
    n = len(graph)

    subproblems = [[0 for x in range(n)] for y in range(n + 1)]
    in_degree_neighbors = _compute_in_degree_neighbors(graph)
    predecessors = {}

    # base cases
    for v in range(0, n):
        subproblems[0][v] = sys.maxsize

    subproblems[0][source - 1] = 0

    for i in range(1, n + 1):
        stable = True

        for v in range(0, n):
            case1 = subproblems[i - 1][v]

            if in_degree_neighbors[v + 1]:
                case2 = min(subproblems[i - 1][tail - 1] + edge_weight for tail,
                            edge_weight in in_degree_neighbors[v + 1])
                subproblems[i][v] = min(case1, case2)
            else:
                subproblems[i][v] = case1

            if subproblems[i][v] != subproblems[i - 1][v]:
                stable = False

        if stable:
            shortest_lengths = {
                v + 1: subproblems[i - 1][v] for v in range(0, n)}

            shortest_paths = None
            if reconstruct_shortest_paths:
                shortest_paths = _reconstruct_shortest_paths(
                    graph, source, in_degree_neighbors, subproblems, shortest_lengths)

            return shortest_lengths, shortest_paths

    return None, None  # negative cycle detected


def _reconstruct_shortest_paths(graph, source, in_degree_neighbors, subproblems, shortest_lengths):
    shortest_paths = defaultdict(list)

    for v_key in graph:
        key = v_key
        while key != source:
            if not in_degree_neighbors[key]:
                shortest_paths[v_key].append(None)
                break

            for tail, edge_weight in in_degree_neighbors[key]:
                if shortest_lengths[tail] + edge_weight == shortest_lengths[key]:
                    shortest_paths[v_key].append(tail)
                    key = tail
                    break

        shortest_paths[v_key].reverse()

    return shortest_paths


def _compute_in_degree_neighbors(graph):
    in_degree_neighbors = defaultdict(list)

    for v in graph:
        for head, edge_weight in graph[v]:
            in_degree_neighbors[head].append((v, edge_weight))

    return in_degree_neighbors
