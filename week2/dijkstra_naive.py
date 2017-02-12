
"""Dijkstra's Shortest Paths Algorithm (Naive) Package"""

import sys


def dijkstra(graph, source):
    """Dijkstra's Shortest Paths Algorithm (Naive) - O(mn) Complexity"""
    explored = set([source])
    shortest_paths = {
        source: 0
    }

    n = len(graph)
    while n > 1:
        min_key = None
        min_value = sys.maxint

        for tail in explored:
            for head in graph[tail]:
                if head[0] not in explored:
                    temp_value = shortest_paths[tail] + head[1]
                    if temp_value < min_value:
                        min_key = head[0]
                        min_value = temp_value

        explored.add(min_key)
        shortest_paths[min_key] = min_value
        n -= 1

    return shortest_paths
