"""Week1 Test Cases Prim's MST"""

import sys

from week1.johnson import compute_all_pairs_shortest_paths


def test_mixed_costs_no_negative_cycle():
    graph = {
        1: [(2, 1), (3, -1)],
        2: [(3, -2), (4, -1)],
        3: [(1, 3), (4, 4)],
        4: [(3, -3)]
    }

    shortest_paths = compute_all_pairs_shortest_paths(graph)

    assert shortest_paths == {
        1: {1: 0, 2: 1, 3: -3, 4: 0},
        2: {1: -1, 2: 0, 3: -4, 4: -1},
        3: {1: 3, 2: 4, 3: 0, 4: 3},
        4: {1: 0, 2: 1, 3: -3, 4: 0}
    }


def test_positive_costs_only():
    graph = {
        1: [(2, 1), (3, 1)],
        2: [(3, 2), (4, 1)],
        3: [(1, 1), (4, 4)],
        4: [(3, 3)]
    }

    shortest_paths = compute_all_pairs_shortest_paths(graph)

    assert shortest_paths == {
        1: {1: 0, 2: 1, 3: 1, 4: 2},
        2: {1: 3, 2: 0, 3: 2, 4: 1},
        3: {1: 1, 2: 2, 3: 0, 4: 3},
        4: {1: 4, 2: 5, 3: 3, 4: 0}
    }


def test_mixed_costs_negative_cycle():
    graph = {
        1: [(2, 1), (3, -1)],
        2: [(3, -2), (4, -1)],
        3: [(1, 2), (4, 4)],
        4: [(3, -3)]
    }

    shortest_paths = compute_all_pairs_shortest_paths(graph)

    assert shortest_paths is None  # negative cycle detected


def test_negative_costs_negative_cycle():
    graph = {
        1: [(2, -1), (3, -1)],
        2: [(3, -2), (4, -1)],
        3: [(1, -2), (4, -4)],
        4: [(3, -3)]
    }

    shortest_paths = compute_all_pairs_shortest_paths(graph)

    assert shortest_paths is None  # negative cycle detected


def test_negative_costs_no_negative_cycle():
    graph = {
        1: [(2, -4), (3, -1), (4, -2)],
        2: [(3, -1), (4, -6)],
        3: [(4, -3)],
        4: []
    }

    shortest_paths = compute_all_pairs_shortest_paths(graph)

    assert shortest_paths == {
        1: {1: 0, 2: -4, 3: -5, 4: -10},
        2: {1: sys.maxsize, 2: 0, 3: -1, 4: -6},
        3: {1: sys.maxsize, 2: sys.maxsize, 3: 0, 4: -3},
        4: {1: sys.maxsize, 2: sys.maxsize, 3: sys.maxsize, 4: 0}
    }
