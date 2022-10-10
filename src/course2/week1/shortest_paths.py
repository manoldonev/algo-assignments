"""Shortest Path Package"""

from collections import deque
from collections.abc import Iterable, Mapping


def shortest_paths(graph: Mapping[int, Iterable[int]], start: int):
    """Shortest Paths"""
    explored = set([start])
    queue = deque([start])
    dist = {start: 0}

    while queue:
        vertex = queue.pop()

        for node in graph[vertex]:
            if node not in explored:
                explored.add(node)
                queue.appendleft(node)
                dist[node] = dist[vertex] + 1

    return dist
