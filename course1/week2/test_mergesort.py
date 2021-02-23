"""Week2 Test Cases: Mergesort"""

import unittest

from course1.week2.mergesort import sort as mergesort


class MergesortTests(unittest.TestCase):
    """Test cases for mergesort."""

    def test_mergesort_empty(self):
        self.assertEqual(mergesort([]), [])

    def test_mergesort_single(self):
        self.assertEqual(mergesort([1]), [1])

    def test_mergesort_single_negative(self):
        self.assertEqual(mergesort([-1]), [-1])

    def test_mergesort_even(self):
        self.assertEqual(mergesort([1, 2]), [1, 2])

    def test_mergesort_even2(self):
        self.assertEqual(mergesort([2, 1]), [1, 2])

    def test_mergesort_mixed(self):
        self.assertEqual(mergesort([2, -1]), [-1, 2])

    def test_mergesort_mixed2(self):
        self.assertEqual(mergesort([-1, 2]), [-1, 2])

    def test_mergesort_odd(self):
        self.assertEqual(mergesort([1, 2, 3]), [1, 2, 3])

    def test_mergesort_odd1(self):
        self.assertEqual(mergesort([1, 3, 2]), [1, 2, 3])

    def test_mergesort_odd2(self):
        self.assertEqual(mergesort([2, 1, 3]), [1, 2, 3])

    def test_mergesort_odd3(self):
        self.assertEqual(mergesort([3, 1, 2]), [1, 2, 3])

    def test_mergesort_odd4(self):
        self.assertEqual(mergesort([3, 2, 1]), [1, 2, 3])

    def test_mergesort_odd5(self):
        self.assertEqual(mergesort([2, 3, 1]), [1, 2, 3])

    def test_mergesort(self):
        self.assertEqual(mergesort([2, 4, 1, 3]), [1, 2, 3, 4])

    def test_mergesort2(self):
        self.assertEqual(mergesort([1, 2, 4, 3]), [1, 2, 3, 4])

    def test_mergesort3(self):
        self.assertEqual(mergesort([2, 1, 3, 4]), [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main(verbosity=2)
