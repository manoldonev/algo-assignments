
"""Topological Sort Package"""


def topological_sort(graph):
    """Topological Sort"""
    explored = []
    sort_order = []

    for node in graph.keys():
        if node not in explored:
            dfs(graph, node, explored, sort_order)

    # nodes are sorted in reverse order
    sort_order.reverse()
    return sort_order


def dfs(graph, start, explored=None, sort_order=None):
    """Depth-First Search (Recursive)"""
    if explored is None:
        explored = []

    if sort_order is None:
        sort_order = []

    explored.append(start)

    for node in graph[start]:
        if node not in explored:
            dfs(graph, node, explored, sort_order)

    sort_order.append(start)
