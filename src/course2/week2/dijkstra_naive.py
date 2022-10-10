"""Dijkstra's Shortest Paths Algorithm (Naive) Package"""

from collections.abc import Mapping
import sys


def dijkstra(graph: Mapping[str, list[tuple[str, int]]], source: str):
    """Dijkstra's Shortest Paths Algorithm (Naive) - O(m*n) Complexity"""

    explored = set([source])
    shortest_paths = {source: 0}
    n = len(graph)

    while n > 1:
        min_key = None
        min_value = sys.maxsize

        for tail in explored:
            for head, value in graph[tail]:
                if head not in explored:
                    temp_value = shortest_paths[tail] + value
                    if temp_value < min_value:
                        min_key = head
                        min_value = temp_value

        if min_key:
            explored.add(min_key)
            shortest_paths[min_key] = min_value

        n -= 1

    return shortest_paths
