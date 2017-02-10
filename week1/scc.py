
"""Strongly Connected Components Package"""

from collections import deque
from collections import defaultdict


class Tracker(object):

    def __init__(self):
        self.current_source = None
        self.sccs_by_leader = defaultdict(list)
        self.finish_times_reversed = deque()

        """Sets are implemented using hash tables thus membership test does not depend
        on the size of the set. For lists, in contrast, the whole list needs to be searched,
        which will become slower as the list grows."""
        self.explored = set()


def scc(graph):
    """Strongly Connected Components"""
    graph_reversed = reverse_graph(graph)

    tracker1 = Tracker()
    dfs_loop(graph_reversed, graph_reversed.keys(), tracker1)

    tracker2 = Tracker()
    dfs_loop(graph, tracker1.finish_times_reversed, tracker2)

    return tracker2.sccs_by_leader


def dfs_loop(graph, nodes, tracker):
    """Depth First Search Loop"""
    for node in nodes:
        if node not in tracker.explored:
            tracker.current_source = node
            dfs(graph, node, tracker)


def dfs(graph, start, tracker):
    """Depth First Search"""
    tracker.explored.add(start)
    tracker.sccs_by_leader[tracker.current_source].append(start)

    for node in graph[start]:
        if node not in tracker.explored:
            dfs(graph, node, tracker)

    tracker.finish_times_reversed.appendleft(start)


def reverse_graph(graph):
    """Reverse edges in a directed graph"""
    reversed_graph = defaultdict(list)

    for tail, head_list in graph.iteritems():
        if not head_list and not reversed_graph.has_key(tail):
            reversed_graph[tail] = []
            continue

        for head in head_list:
            reversed_graph[head].append(tail)

    return reversed_graph
