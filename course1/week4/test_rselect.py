"""Week4 Test Cases: Randomized Selection"""

import unittest

from course1.week4.rselect import rselect


class RselectTests(unittest.TestCase):
    """Test cases for rselect."""

    def test_rselect_basic(self):
        self.assertEqual(rselect([4], 1), 4)

    def test_rselect(self):
        for order_stat in range(0, 10):
            self.assertEqual(
                rselect([5, 2, 7, 1, 9, 6, 0, 8, 4, 3], order_stat),
                order_stat)


if __name__ == "__main__":
    unittest.main(verbosity=2)
