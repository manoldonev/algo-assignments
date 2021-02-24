
"""Dijkstra's Shortest Paths Algorithm (heapq) Package"""

import sys

from src.common.priority_queue import PriorityQueue


def dijkstra(graph, source):
    """Dijkstra's Shortest Paths Algorithm (heapq) - O(m*log(n)) Complexity"""
    explored = set([source])
    shortest_paths = {source: 0}
    min_heap = initialize_heap(graph, source)
    n = len(graph)

    while n > 1:
        min_item = min_heap.pop_task()
        min_key = min_item[1]
        min_dijkstra_criterion = min_item[0]

        explored.add(min_key)
        shortest_paths[min_key] = min_dijkstra_criterion

        for head in graph[min_key]:
            head_key = head[0]
            if head_key in explored:
                continue

            old_min_value = min_heap.remove_task(head_key)
            new_value = shortest_paths[min_key] + head[1]
            min_value = min(old_min_value, new_value)
            min_heap.add_task(head_key, min_value)

        n -= 1

    return shortest_paths


def initialize_heap(graph, source):
    """Initialize Min-Heap"""
    dijkstra_criterion = {key: sys.maxsize for key in graph}
    for node in graph[source]:
        dijkstra_criterion[node[0]] = node[1]

    return PriorityQueue(list([value, key] for key, value in dijkstra_criterion.items()))
