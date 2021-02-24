
"""Week1 Test Cases Topological Sort"""

from collections import deque
from week1.topologicalSort import topological_sort


def test_topological_sort1():
    graph = {
        's': ['v', 'w'],
        'v': ['t'],
        'w': ['t'],
        't': []
    }

    assert topological_sort(graph) == deque(['s', 'w', 'v', 't'])


def test_topological_sort2():
    graph = {
        1: [3],
        3: [5, 6],
        5: [4],
        4: [7],
        7: [],
        6: []}

    assert topological_sort(graph) == deque([1, 3, 6, 5, 4, 7])


def test_topological_sort_not_connected():
    graph = {
        's': ['v', 'w'],
        'v': ['t'],
        'w': ['t'],
        't': [],
        1: [3],
        3: [5, 6],
        5: [4],
        4: [7],
        7: [],
        6: []
    }

    assert topological_sort(graph) == deque(
        [1, 3, 6, 5, 4, 7, 's', 'w', 'v', 't'])
