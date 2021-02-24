"""Week4 Test Cases: Randomized Selection"""

from src.course1.week4.rselect import rselect


class TestRselect:
    """Test cases for rselect."""

    def test_rselect_basic(self):
        assert rselect([4], 1) == 4

    def test_rselect(self):
        for order_stat in range(0, 10):
            result = rselect([5, 2, 7, 1, 9, 6, 0, 8, 4, 3], order_stat)
            assert result == order_stat
