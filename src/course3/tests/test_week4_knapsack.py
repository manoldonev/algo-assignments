"""Week4 Test Cases Knapsack """

from week4.knapsack import knapsack, knapsack_recursive


def test_knapsack():
    items = [(60, 10), (100, 20), (120, 30)]
    knapsack_size = 50
    assert knapsack(items, knapsack_size) == 220


def test_knapsack_recursive():
    items = [(60, 10), (100, 20), (120, 30)]
    knapsack_size = 50
    assert knapsack_recursive(items, knapsack_size) == 220
