
"""Depth-First Search Package"""


def dfs(graph, start):
    """Depth-First Search"""
    """Similar to breadth-first search but differs from it in two ways:
    1. it uses a stack (LIFO) instead of a queue, and
    2. it delays checking whether a vertex has been discovered until the vertex is popped from
    the stack rather than making this check before pushing the vertex."""
    path = []
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in path:
            path.append(vertex)
            stack.extend(graph[vertex])

    return path
