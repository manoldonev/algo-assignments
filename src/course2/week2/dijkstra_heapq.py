
"""Dijkstra's Shortest Paths Algorithm (heapq) Package"""

import sys

from heapq import heappush, heappop, heapify


class PriorityQueue:
    """Priority queue implementation based on heapq
    See https://docs.python.org/2/library/heapq.html#priority-queue-implementation-notes"""

    REMOVED = sys.maxsize

    def __init__(self, heap=None):
        if heap is None:
            heap = []
        else:
            heapify(heap)

        self.heap = heap
        self.entry_finder = {i[-1]: i for i in heap}

    def add_task(self, task, priority=0):
        """Add new priority task."""
        if task in self.entry_finder:
            self.remove_task(task)

        entry = [priority, task]
        self.entry_finder[task] = entry
        heappush(self.heap, entry)

    def remove_task(self, task):
        """Mark an existing task as REMOVED.  Raise KeyError if not found."""
        entry = self.entry_finder.pop(task)
        entry[-1] = PriorityQueue.REMOVED

        return entry[0]

    def pop_task(self):
        """Remove and return the lowest priority task. Raise KeyError if empty."""
        while self.heap:
            priority, task = heappop(self.heap)
            if task is not PriorityQueue.REMOVED:
                del self.entry_finder[task]
                return priority, task

        raise KeyError('pop from an empty priority queue')


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
