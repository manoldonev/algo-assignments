
import sys
import math
from collections import defaultdict

from week1.johnson import compute_all_pairs_shortest_paths
from week2.tsp import traveling_salesman_problem, generate_complete_euclidean_distanace_graph, calculate_euclidean_distance


# def main():
#     graph = defaultdict(list)

#     # with open("tests/week1_g1.txt") as handle:
#     #     handle.readline()
#     #     for line in handle:
#     #         tail, head, cost = line.split()
#     #         graph[int(tail)].append((int(head), int(cost)))

#     # all_pairs_shortests_paths = compute_all_pairs_shortest_paths(graph)

#     # with open("tests/week1_g2.txt") as handle:
#     #     handle.readline()
#     #     for line in handle:
#     #         tail, head, cost = line.split()
#     #         graph[int(tail)].append((int(head), int(cost)))

#     # all_pairs_shortests_paths = compute_all_pairs_shortest_paths(graph)

#     # return all_pairs_shortests_paths

#     with open("tests/week1_g3.txt") as handle:
#         handle.readline()
#         for line in handle:
#             tail, head, cost = line.split()
#             graph[int(tail)].append((int(head), int(cost)))

#     all_pairs_shortests_paths = compute_all_pairs_shortest_paths(graph)

#     shortest_shortest_path = sys.maxsize
#     for v in all_pairs_shortests_paths:
#         shortest_shortest_path = min(shortest_shortest_path, min(
#             all_pairs_shortests_paths[v].values()))

#     return shortest_shortest_path  # -19

def main():

    points = []
    with open("tests/week2_tsp.txt") as handle:
        handle.readline()
        for line in handle:
            x, y = line.split()
            points.append((float(x), float(y)))

    points_0_12 = points[:13]
    points_11_24 = points[11:25]

    graph = generate_complete_euclidean_distanace_graph(points_0_12)
    graph2 = generate_complete_euclidean_distanace_graph(points_11_24)

    result1 = traveling_salesman_problem(graph)
    result2 = traveling_salesman_problem(graph2)

    result = result1 + result2 - 2 * \
        calculate_euclidean_distance(points[11], points[12])

    return math.floor(result)  # 26442


if __name__ == '__main__':
    print(main())
