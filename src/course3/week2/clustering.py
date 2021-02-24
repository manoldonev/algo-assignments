
from collections import defaultdict

from src.course3.week2.union_find import UnionFind


def clusterize(graph, edge_list, cluster_count):
    union_find = UnionFind(len(graph))

    t_edges = {i: defaultdict(int) for i in range(len(graph))}

    edge_list.sort()
    for cost, v1, v2 in edge_list:
        if union_find.find(v1) != union_find.find(v2):
            if len(union_find) == cluster_count:
                # TODO: compute connected components
                return t_edges, cost

            t_edges[v1][v2] = cost
            t_edges[v2][v1] = cost
            union_find.union(v1, v2)

    return None, -1
