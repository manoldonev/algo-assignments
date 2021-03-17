
"""Topological Sort Package"""

from collections import deque
from collections.abc import Iterable, Mapping


class Tracker():
    def __init__(self):
        self.explored = set()
        self.sort_order = deque()


def topological_sort(graph: Mapping[int, Iterable[int]]):
    """Topological Sort"""
    tracker = Tracker()

    for node in graph:
        if node not in tracker.explored:
            dfs(graph, node, tracker)

    return tracker.sort_order


def dfs(graph: Mapping[int, Iterable[int]], start: int, tracker: Tracker):
    """Depth-First Search (Recursive)"""
    tracker.explored.add(start)

    for node in graph[start]:
        if node not in tracker.explored:
            dfs(graph, node, tracker)

    tracker.sort_order.appendleft(start)
