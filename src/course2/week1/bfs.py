
"""Breadth-First Search Package"""

from collections import deque
from collections.abc import Iterable, Mapping


def bfs(graph: Mapping[int, Iterable[int]], start: int):
    """Breadth-First Search"""
    # Similar to iterative depth-first search, but differs from it in two ways:
    # 1. it uses a queue (FIFO) instead of a stack and
    # 2. it checks whether a vertex has been discovered before enqueueing it rather than
    # delaying this check until the vertex is dequeued from the queue.
    path = [start]
    queue = deque([start])

    while queue:
        vertex = queue.pop()

        for node in graph[vertex]:
            if node not in path:
                path.append(node)
                queue.appendleft(node)

    return path
