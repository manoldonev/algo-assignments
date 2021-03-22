
"""Dijkstra's Shortest Paths Algorithm (heapq) Package"""

from collections.abc import Mapping
import sys

from src.common.priority_queue import PriorityQueue, PrioritizedItem


def dijkstra(graph: Mapping[str, list[tuple[str, int]]], source: str):
    """Dijkstra's Shortest Paths Algorithm (heapq) - O(m*log(n)) Complexity"""
    explored = set([source])
    shortest_paths = {source: 0}
    min_heap = initialize_heap(graph, source)
    n = len(graph)

    while n > 1:
        min_item = min_heap.pop_task()
        min_key = min_item[1]
        min_dijkstra_score = min_item[0]

        explored.add(min_key)
        shortest_paths[min_key] = min_dijkstra_score

        for head_key, value in graph[min_key]:
            if head_key in explored:
                continue

            old_min_value = min_heap.remove_task(head_key)
            candidate_min_value = shortest_paths[min_key] + value
            min_value = min(old_min_value, candidate_min_value)
            min_heap.add_task(head_key, min_value)

        n -= 1

    return shortest_paths


def initialize_heap(graph: Mapping[str, list[tuple[str, int]]], source: str):
    """Initialize Min-Heap"""

    dijkstra_score = {key: sys.maxsize for key in graph if key != source}
    for node in graph[source]:
        dijkstra_score[node[0]] = node[1]

    items = [PrioritizedItem(value, key)
             for key, value in dijkstra_score.items()]
    return PriorityQueue(items)
