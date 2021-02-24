"""Week3 Test Cases: Quicksort"""

from course1.week3.quicksort import sort as randomized_quicksort


class TestQuicksort:
    """Test cases for quicksort."""

    def test_quicksort_empty(self):
        assert randomized_quicksort([]) == []

    def test_quicksort_single(self):
        assert randomized_quicksort([1]) == [1]

    def test_quicksort_single_negative(self):
        assert randomized_quicksort([-1]) == [-1]

    def test_quicksort_even(self):
        assert randomized_quicksort([1, 2]) == [1, 2]

    def test_quicksort_even2(self):
        assert randomized_quicksort([2, 1]) == [1, 2]

    def test_quicksort_mixed(self):
        assert randomized_quicksort([2, -1]) == [-1, 2]

    def test_quicksort_mixed2(self):
        assert randomized_quicksort([-1, 2]) == [-1, 2]

    def test_quicksort_odd(self):
        assert randomized_quicksort([1, 2, 3]) == [1, 2, 3]

    def test_quicksort_odd1(self):
        assert randomized_quicksort([1, 3, 2]) == [1, 2, 3]

    def test_quicksort_odd2(self):
        assert randomized_quicksort([2, 1, 3]) == [1, 2, 3]

    def test_quicksort_odd3(self):
        assert randomized_quicksort([3, 1, 2]) == [1, 2, 3]

    def test_quicksort_odd4(self):
        assert randomized_quicksort([3, 2, 1]) == [1, 2, 3]

    def test_quicksort_odd5(self):
        assert randomized_quicksort([2, 3, 1]) == [1, 2, 3]

    def test_randomized_quicksort(self):
        assert randomized_quicksort([2, 4, 1, 3]) == [1, 2, 3, 4]

    def test_quicksort2(self):
        assert randomized_quicksort([1, 2, 4, 3]) == [1, 2, 3, 4]

    def test_quicksort3(self):
        assert randomized_quicksort([2, 1, 3, 4]) == [1, 2, 3, 4]
