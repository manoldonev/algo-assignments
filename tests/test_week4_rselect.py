"""Week4 Test Cases: Randomized Selection"""

from week4 import rselect


def test_rselect_basic():
    assert rselect([4], 1) == 4


def test_rselect():
    for order_stat in range(0, 10):
        assert rselect([5, 2, 7, 1, 9, 6, 0, 8, 4, 3],
                       order_stat) == order_stat
