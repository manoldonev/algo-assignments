
import sys
from collections import defaultdict

from week1.johnson import compute_all_pairs_shortest_paths


def main():
    graph = defaultdict(list)

    # with open("tests/week1_g1.txt") as handle:
    #     handle.readline()
    #     for line in handle:
    #         tail, head, cost = line.split()
    #         graph[int(tail)].append((int(head), int(cost)))

    # all_pairs_shortests_paths = compute_all_pairs_shortest_paths(graph)

    # with open("tests/week1_g2.txt") as handle:
    #     handle.readline()
    #     for line in handle:
    #         tail, head, cost = line.split()
    #         graph[int(tail)].append((int(head), int(cost)))

    # all_pairs_shortests_paths = compute_all_pairs_shortest_paths(graph)

    # return all_pairs_shortests_paths

    with open("tests/week1_g3.txt") as handle:
        handle.readline()
        for line in handle:
            tail, head, cost = line.split()
            graph[int(tail)].append((int(head), int(cost)))

    all_pairs_shortests_paths = compute_all_pairs_shortest_paths(graph)

    shortest_shortest_path = sys.maxsize
    for v in all_pairs_shortests_paths:
        shortest_shortest_path = min(shortest_shortest_path, min(
            all_pairs_shortests_paths[v].values()))

    return shortest_shortest_path  # -19


if __name__ == '__main__':
    print(main())
