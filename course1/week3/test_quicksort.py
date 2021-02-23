"""Week3 Test Cases: Quicksort"""

import unittest

from course1.week3.quicksort import sort as randomized_quicksort


class QuicksortTests(unittest.TestCase):
    """Test cases for quicksort."""

    def test_quicksort_empty(self):
        self.assertEqual(randomized_quicksort([]), [])

    def test_quicksort_single(self):
        self.assertEqual(randomized_quicksort([1]), [1])

    def test_quicksort_single_negative(self):
        self.assertEqual(randomized_quicksort([-1]), [-1])

    def test_quicksort_even(self):
        self.assertEqual(randomized_quicksort([1, 2]), [1, 2])

    def test_quicksort_even2(self):
        self.assertEqual(randomized_quicksort([2, 1]), [1, 2])

    def test_quicksort_mixed(self):
        self.assertEqual(randomized_quicksort([2, -1]), [-1, 2])

    def test_quicksort_mixed2(self):
        self.assertEqual(randomized_quicksort([-1, 2]), [-1, 2])

    def test_quicksort_odd(self):
        self.assertEqual(randomized_quicksort([1, 2, 3]), [1, 2, 3])

    def test_quicksort_odd1(self):
        self.assertEqual(randomized_quicksort([1, 3, 2]), [1, 2, 3])

    def test_quicksort_odd2(self):
        self.assertEqual(randomized_quicksort([2, 1, 3]), [1, 2, 3])

    def test_quicksort_odd3(self):
        self.assertEqual(randomized_quicksort([3, 1, 2]), [1, 2, 3])

    def test_quicksort_odd4(self):
        self.assertEqual(randomized_quicksort([3, 2, 1]), [1, 2, 3])

    def test_quicksort_odd5(self):
        self.assertEqual(randomized_quicksort([2, 3, 1]), [1, 2, 3])

    def test_randomized_quicksort(self):
        self.assertEqual(randomized_quicksort([2, 4, 1, 3]), [1, 2, 3, 4])

    def test_quicksort2(self):
        self.assertEqual(randomized_quicksort([1, 2, 4, 3]), [1, 2, 3, 4])

    def test_quicksort3(self):
        self.assertEqual(randomized_quicksort([2, 1, 3, 4]), [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main(verbosity=2)
