"""Week2 Test Cases Traveling Salesman Problem"""

import math

from week2.tsp import generate_complete_euclidean_distanace_graph, traveling_salesman_problem


def test_tsp1():
    points = [(1, 1), (4, 1), (1, 4), (4, 4)]
    graph = generate_complete_euclidean_distanace_graph(points)
    result = traveling_salesman_problem(graph)
    assert result == 12


def test_tsp2():
    points = [(0, 0), (0, 3), (3, 3)]
    graph = generate_complete_euclidean_distanace_graph(points)
    result = traveling_salesman_problem(graph)
    assert math.floor(result) == 10


def test_tsp3():
    points = [(0, 0), (4, 3), (4, 0), (0, 3)]
    graph = generate_complete_euclidean_distanace_graph(points)
    result = traveling_salesman_problem(graph)
    assert result == 14


def test_tsp4():
    points = [
        (1.000, 1.00),
        (1.125, 1.00),
        (1.250, 1.00),
        (1.500, 1.00),
        (1.750, 1.00),
        (2.000, 1.00),
        (1.000, 2.00),
        (1.125, 2.00),
        (1.250, 2.00),
        (1.500, 2.00),
        (1.750, 2.00),
        (2.000, 2.00)
    ]
    graph = generate_complete_euclidean_distanace_graph(points)
    result = traveling_salesman_problem(graph)
    assert result == 4


def test_tsp5():
    points = [
        (0.549963E-07,  0.985808E-08),
        (-28.8733,    -0.797739E-07),
        (-79.2916,     -21.4033),
        (-14.6577,    -43.3896),
        (-64.7473,     21.8982),
        (-29.0585,     -43.2167),
        (-72.0785,     0.181581),
        (-36.0366,    -21.6135),
        (-50.4808,     7.37447),
        (-50.5859,     -21.5882),
        (-0.135819,    -28.7293),
        (-65.0866,    -36.0625),
        (-21.4983,      7.31942),
        (-57.5687,    -43.2506),
        (-43.0700,     14.5548)
    ]
    graph = generate_complete_euclidean_distanace_graph(points)
    result = traveling_salesman_problem(graph)
    assert math.floor(result) == 284


def test_tsp6():
    points = [(0, 2.05), (3.414213562373095, 3.4642135623730947),
              (0.5857864376269049, 0.6357864376269047),
              (0.5857864376269049, 3.4642135623730947),
              (2, 0),
              (4.05, 2.05),
              (2, 4.10),
              (3.414213562373095, 0.6357864376269047)]
    graph = generate_complete_euclidean_distanace_graph(points)
    result = traveling_salesman_problem(graph)
    assert math.floor(result) == 12
