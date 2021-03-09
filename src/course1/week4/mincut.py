
"""Karger's Min Cut Algorithm Implementation"""

from random import randint
from copy import deepcopy
from typing import List, MutableMapping


def min_cut(graph: MutableMapping[int, List[int]]):
    """Min Cut Public Method"""

    graph = deepcopy(graph)
    n = len(graph)

    while n > 2:
        u, v = choose_edge(graph, n)
        contract(graph, u, v)

        n -= 1

    return graph


def choose_edge(graph: MutableMapping[int, List[int]], n: int):
    """Choose edge (u, v) uniformly at random"""

    u = list(graph.keys())[randint(0, n - 1)]
    u_edge_list = graph[u]
    v = u_edge_list[randint(0, len(u_edge_list) - 1)]

    return u, v


def contract(graph: MutableMapping[int, List[int]], u: int, v: int):
    """Contract u and v into a single vertex"""

    degree_u = len(graph[u])
    degree_v = len(graph[v])

    # Always extend with the shorter edge list
    if degree_v > degree_u:
        u, v = v, u

    graph[u].extend(graph[v])

    for element in graph[v]:
        element_list = graph[element]

        for i, _ in enumerate(element_list):
            if element_list[i] == v:
                element_list[i] = u

    # Remove self loops (can be multiple)
    while u in graph[u]:
        graph[u].remove(u)

    del graph[v]
