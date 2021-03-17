
import sys
import math
import itertools

from collections import defaultdict


def traveling_salesman_problem(points):
    graph = generate_complete_euclidean_distanace_graph(points)
    n = len(graph)
    edge_dict = _get_edges(graph)

    subproblems = {}

    # base case
    subproblems[(0,)] = [0]

    for m in range(2, n + 1):
        for c in itertools.combinations(range(1, n), m - 1):
            # subset s of size m that contains 0
            subset = (0, ) + c

            # includes the 'otherwise' base case (+infinity for any subset != {0} and subproblem size = 1)
            subproblems[subset] = [sys.maxsize] * n

            for j in subset:
                if j == 0:
                    continue

                subset_minus_j = tuple(
                    filter(lambda element: element != j, subset))
                subproblems[subset][j] = min(
                    subproblems[subset_minus_j][k] + edge_dict[k][j] for k in subset if k != j)

    n_tuple = tuple(range(n))
    return min(subproblems[n_tuple][j] + edge_dict[j][0] for j in range(1, n))


def generate_complete_euclidean_distanace_graph(points):
    points_with_ids = [(index, point[0], point[1])
                       for index, point in enumerate(points)]

    graph = defaultdict(list)
    for point1, point2 in itertools.combinations(points_with_ids, 2):
        id1, x1, y1 = point1
        id2, x2, y2 = point2
        distance = calculate_euclidean_distance((x1, y1), (x2, y2))
        graph[id1].append((distance, id2))
        graph[id2].append((distance, id1))

    return graph


def calculate_euclidean_distance(point1, point2):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(point1, point2)]))


def _get_edges(graph):
    edge_dict = defaultdict(lambda: defaultdict(list))

    for v in graph:
        for cost, v2 in graph[v]:
            edge_dict[v][v2] = cost
            edge_dict[v2][v] = cost

    return edge_dict
