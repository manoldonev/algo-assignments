
import sys

from src.course4.week1.bellman_ford import compute_single_source_shortest_paths


def test_mixed_costs_no_negative_cycle():
    graph = {
        1: [(2, 1), (3, -1)],
        2: [(3, -2), (4, -1)],
        3: [(1, 3), (4, 4)],
        4: [(3, -3)]
    }

    shortest_lengths, shortest_paths = compute_single_source_shortest_paths(
        graph, 2, reconstruct_shortest_paths=True)

    assert shortest_lengths == {1: -1, 2: 0, 3: -4, 4: -1}
    assert shortest_paths == {
        1: [2, 4, 3],
        2: [],
        3: [2, 4],
        4: [2]}


def test_positive_costs_only():
    graph = {
        1: [(2, 1), (3, 1)],
        2: [(3, 2), (4, 1)],
        3: [(1, 1), (4, 4)],
        4: [(3, 3)]
    }

    shortest_lengths, shortest_paths = compute_single_source_shortest_paths(
        graph, 2, reconstruct_shortest_paths=True)

    assert shortest_lengths == {1: 3, 2: 0, 3: 2, 4: 1}
    assert shortest_paths == {
        1: [2, 3],
        2: [],
        3: [2],
        4: [2]
    }


def test_mixed_costs_negative_cycle():
    graph = {
        1: [(2, 1), (3, -1)],
        2: [(3, -2), (4, -1)],
        3: [(1, 2), (4, 4)],
        4: [(3, -3)]
    }

    shortest_lengths, shortest_paths = compute_single_source_shortest_paths(
        graph, 2, reconstruct_shortest_paths=True)

    assert shortest_lengths is None  # negative cycle detected
    assert shortest_paths is None


def test_negative_costs_negative_cycle():
    graph = {
        1: [(2, -1), (3, -1)],
        2: [(3, -2), (4, -1)],
        3: [(1, -2), (4, -4)],
        4: [(3, -3)]
    }

    shortest_lengths, shortest_paths = compute_single_source_shortest_paths(
        graph, 2, reconstruct_shortest_paths=True)

    assert shortest_lengths is None  # negative cycle detected
    assert shortest_paths is None


def test_negative_costs_no_negative_cycle():
    graph = {
        1: [(2, -4), (3, -1), (4, -2)],
        2: [(3, -1), (4, -6)],
        3: [(4, -3)],
        4: []
    }

    shortest_lengths, shortest_paths = compute_single_source_shortest_paths(
        graph, 2, reconstruct_shortest_paths=True)

    assert shortest_lengths == {1: sys.maxsize, 2: 0, 3: -1, 4: -6}
    assert shortest_paths == {1: [None], 2: [], 3: [2], 4: [2]}
