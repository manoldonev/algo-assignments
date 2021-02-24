"""Week1 Test Cases Prim's MST"""

from src.course3.week1.prim_mst import prim


def test_prim_mst():
    graph = {
        1: [(2, -1), (3, 2), (4, 6), (6, 7)],
        2: [(1, -1), (4, -2), (6, 1)],
        3: [(1, 2), (4, 3), ],
        4: [(1, 6), (2, -2), (3, 3), (5, 21), (6, 5)],
        5: [(4, 21)],
        6: [(1, 7), (2, 1), (4, 5)]
    }

    mst = prim(graph)

    total_cost = 0
    for cost, _, _ in mst:
        total_cost += cost

    assert total_cost == 21
