
"""Week1 Test Cases DFS"""

from collections.abc import Iterable, Mapping
import pytest

from src.course2.week1.dfs_recursive import dfs_recursive
from src.course2.week1.dfs import dfs


@pytest.fixture(name='graph')
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


def test_dfs_recursive(graph: Mapping[int, Iterable[int]]):
    path = dfs_recursive(graph, 0)
    assert path == [0, 1, 2, 6, 3, 4, 5]


def test_dfs(graph: Mapping[int, Iterable[int]]):
    path = dfs(graph, 0)
    assert path == [0, 4, 5, 3, 6, 2, 1]
