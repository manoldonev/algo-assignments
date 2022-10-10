"""Week2 Test Cases Max Spacing for K-order Cluster"""

from collections import defaultdict

from src.course3.week2.clustering import clusterize


def test_clusterize():
    graph = defaultdict(list)
    edge_list = []
    with open("src/course3/week2_clustering_test.txt") as handle:
        handle.readline()
        for line in handle:
            vertex1, vertex2, cost = line.split()
            graph[int(vertex1)].append((int(vertex2), int(cost)))
            graph[int(vertex2)].append((int(vertex1), int(cost)))

            edge_list.append((int(cost), int(vertex1), int(vertex2)))

        _, max_spacing = clusterize(graph, edge_list, 4)

        assert max_spacing == 7
