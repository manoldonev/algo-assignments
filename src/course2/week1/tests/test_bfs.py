
"""Week1 Test Cases BFS"""

from collections.abc import Iterable, Mapping
import pytest

from src.course2.week1.bfs import bfs
from src.course2.week1.shortest_paths import shortest_paths


@pytest.fixture(name="graph")
def fixture_graph():
    return {
        0: [1, 3, 4],
        1: [0, 2, 4],
        2: [1, 6],
        3: [0, 4, 6],
        4: [0, 1, 3, 5],
        5: [4],
        6: [2, 3]
    }


def test_bfs(graph: Mapping[int, Iterable[int]]):
    path = bfs(graph, 0)
    assert path == [0, 1, 3, 4, 2, 6, 5]


def test_shortestPaths(graph: Mapping[int, Iterable[int]]):
    paths = shortest_paths(graph, 0)
    assert paths == {0: 0, 1: 1, 2: 2, 3: 1, 4: 1, 5: 2, 6: 2}
