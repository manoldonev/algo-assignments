
"""Karger's Min Cut Algorithm Implementation"""

from random import randint
from copy import deepcopy


def min_cut(g):
    """Min Cut Public Method"""
    g = deepcopy(g)
    n = len(g)

    while n > 2:
        u, v = choose_edge(g, n)
        contract(g, u, v)

        n -= 1

    return g


def choose_edge(g, n):
    """Choose edge (u, v) uniformly at random"""
    u = list(g.keys())[randint(0, n - 1)]
    u_edge_list = g[u]
    v = u_edge_list[randint(0, len(u_edge_list) - 1)]

    return u, v


def contract(g, u, v):
    """Contract u and v into a single vertex"""
    degree_u = len(g[u])
    degree_v = len(g[v])

    # Always extend with the shorter edge list
    if degree_v > degree_u:
        temp = u
        u = v
        v = temp

    g[u].extend(g[v])

    for element in g[v]:
        element_list = g[element]

        for i, _ in enumerate(element_list):
            if element_list[i] == v:
                element_list[i] = u

    # Remove self loops (can be multiple)
    while u in g[u]:
        g[u].remove(u)

    del g[v]
