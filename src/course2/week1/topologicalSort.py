
"""Topological Sort Package"""

from collections import deque


class Tracker(object):

    def __init__(self):
        self.explored = set()
        self.sort_order = deque()


def topological_sort(graph):
    """Topological Sort"""
    tracker = Tracker()

    for node in graph:
        if node not in tracker.explored:
            dfs(graph, node, tracker)

    return tracker.sort_order


def dfs(graph, start, tracker):
    """Depth-First Search (Recursive)"""
    tracker.explored.add(start)

    for node in graph[start]:
        if node not in tracker.explored:
            dfs(graph, node, tracker)

    tracker.sort_order.appendleft(start)
