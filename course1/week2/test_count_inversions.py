
"""Week2 Test Cases: Count Inversions"""

import unittest

from course1.week2.count_inversions import sort_and_count as count_inversions


class CountInversionsTests(unittest.TestCase):
    """Test cases for count inversions challenge."""

    def test_count_inversions_empty(self):
        _, inversions = count_inversions([])
        self.assertEqual(inversions, 0)

    def test_count_inversions_single(self):
        _, inversions = count_inversions([1])
        self.assertEqual(inversions, 0)

    def test_count_inversions_even(self):
        _, inversions = count_inversions([1, 2])
        self.assertEqual(inversions, 0)

    def test_count_inversions_even2(self):
        _, inversions = count_inversions([2, 1])
        self.assertEqual(inversions, 1)

    def test_count_inversions_odd(self):
        _, inversions = count_inversions([1, 2, 3])
        self.assertEqual(inversions, 0)

    def test_count_inversions_odd1(self):
        _, inversions = count_inversions([1, 3, 2])
        self.assertEqual(inversions, 1)

    def test_count_inversions_odd2(self):
        _, inversions = count_inversions([2, 1, 3])
        self.assertEqual(inversions, 1)

    def test_count_inversions_odd3(self):
        _, inversions = count_inversions([3, 1, 2])
        self.assertEqual(inversions, 2)

    def test_count_inversions_odd4(self):
        _, inversions = count_inversions([3, 2, 1])
        self.assertEqual(inversions, 3)

    def test_count_inversions_odd5(self):
        _, inversions = count_inversions([2, 3, 1])
        self.assertEqual(inversions, 2)

    def test_count_inversions(self):
        _, inversions = count_inversions([2, 4, 1, 3])
        self.assertEqual(inversions, 3)

    def test_count_inversions2(self):
        _, inversions = count_inversions([1, 2, 4, 3])
        self.assertEqual(inversions, 1)

    def test_count_inversions3(self):
        _, inversions = count_inversions([4, 3, 2, 1])
        self.assertEqual(inversions, 6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
