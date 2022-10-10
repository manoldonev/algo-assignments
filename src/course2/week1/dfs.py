"""Depth-First Search Package"""

from collections.abc import Iterable, Mapping


def dfs(graph: Mapping[int, Iterable[int]], start: int):
    """Depth-First Search"""
    # Similar to breadth-first search but differs from it in two ways:
    # 1. it uses a stack (LIFO) instead of a queue, and
    # 2. it delays checking whether a vertex has been discovered until the vertex is popped from
    # the stack rather than making this check before pushing the vertex.
    path: list[int] = []
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in path:
            path.append(vertex)
            stack.extend(graph[vertex])

    return path
