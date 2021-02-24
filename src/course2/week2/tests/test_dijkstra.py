
"""Week2 Test Cases"""

import pytest

from src.course2.week2.dijkstra_naive import dijkstra as dijkstra_naive
from src.course2.week2.dijkstra_heapq import dijkstra as dijkstra_heapq


@pytest.fixture(name="graph")
def fixture_graph():
    return {
        'a': [['b', 1], ['c', 4]],
        'b': [['a', 1], ['c', 2], ['d', 6]],
        'c': [['a', 4], ['b', 2], ['d', 3]],
        'd': [['b', 6], ['c', 3]]
    }


def test_dijkstra_naive(graph):
    assert dijkstra_naive(graph, 'a') == {'a': 0, 'c': 3, 'b': 1, 'd': 6}


def test_dijkstra_heapq(graph):
    assert dijkstra_heapq(graph, 'a') == {'a': 0, 'c': 3, 'b': 1, 'd': 6}