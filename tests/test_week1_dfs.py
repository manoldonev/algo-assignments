
"""Week1 Test Cases DFS"""

from week1.dfsRecursive import dfs_recursive
from week1.dfs import dfs
from week1.topologicalSort import topological_sort


def test_dfs_recursive():
    graph = {
        0: [1, 3, 4],
        1: [0, 2, 4],
        2: [1, 6],
        3: [0, 4, 6],
        4: [0, 1, 3, 5],
        5: [4],
        6: [2, 3]
    }

    path = dfs_recursive(graph, 0)
    assert path == [0, 1, 2, 6, 3, 4, 5]


def test_dfs():
    graph = {
        0: [1, 3, 4],
        1: [0, 2, 4],
        2: [1, 6],
        3: [0, 4, 6],
        4: [0, 1, 3, 5],
        5: [4],
        6: [2, 3]
    }

    path = dfs(graph, 0)
    assert path == [0, 4, 5, 3, 6, 2, 1]


def test_topological_sort1():
    graph = {
        's': ['v', 'w'],
        'v': ['t'],
        'w': ['t'],
        't': []
    }

    assert topological_sort(graph) == ['s', 'w', 'v', 't']


def test_topological_sort2():
    graph = {
        1: [3],
        3: [5, 6],
        5: [4],
        4: [7],
        7: [],
        6: []}

    assert topological_sort(graph) == [1, 3, 6, 5, 4, 7]


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

    assert topological_sort(graph) == ['s', 'w', 'v', 't', 1, 3, 6, 5, 4, 7]
