
"""Shortest Path Package"""

from collections import deque


def shortest_paths(graph, start):
    """Shortest Path"""
    explored = set([start])
    queue = deque([start])
    dist = {start: 0}

    while queue:
        vertex = queue.popleft()

        # TODO: Can this be done with queue.extend(...) + inline
        # generator/yield?
        for node in graph[vertex]:
            if node not in explored:
                explored.add(node)
                queue.append(node)
                dist[node] = dist[vertex] + 1

    return dist
