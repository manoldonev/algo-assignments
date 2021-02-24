
"""Depth-First Search (Recursive) Package"""


def dfs_recursive(graph, start, path=None):
    """Depth-First Search (Recursive)"""
    if path is None:
        path = []

    path.append(start)

    for node in graph[start]:
        if node not in path:
            dfs_recursive(graph, node, path)

    return path
