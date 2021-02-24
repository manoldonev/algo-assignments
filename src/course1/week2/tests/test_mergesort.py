"""Week2 Test Cases: Mergesort"""

from src.course1.week2.mergesort import sort as mergesort


class TestMergesort:
    """Test cases for mergesort."""

    def test_mergesort_empty(self):
        assert mergesort([]) == []

    def test_mergesort_single(self):
        assert mergesort([1]) == [1]

    def test_mergesort_single_negative(self):
        assert mergesort([-1]) == [-1]

    def test_mergesort_even(self):
        assert mergesort([1, 2]) == [1, 2]

    def test_mergesort_even2(self):
        assert mergesort([2, 1]) == [1, 2]

    def test_mergesort_mixed(self):
        assert mergesort([2, -1]) == [-1, 2]

    def test_mergesort_mixed2(self):
        assert mergesort([-1, 2]) == [-1, 2]

    def test_mergesort_odd(self):
        assert mergesort([1, 2, 3]) == [1, 2, 3]

    def test_mergesort_odd1(self):
        assert mergesort([1, 3, 2]) == [1, 2, 3]

    def test_mergesort_odd2(self):
        assert mergesort([2, 1, 3]) == [1, 2, 3]

    def test_mergesort_odd3(self):
        assert mergesort([3, 1, 2]) == [1, 2, 3]

    def test_mergesort_odd4(self):
        assert mergesort([3, 2, 1]) == [1, 2, 3]

    def test_mergesort_odd5(self):
        assert mergesort([2, 3, 1]) == [1, 2, 3]

    def test_mergesort(self):
        assert mergesort([2, 4, 1, 3]) == [1, 2, 3, 4]

    def test_mergesort2(self):
        assert mergesort([1, 2, 4, 3]) == [1, 2, 3, 4]

    def test_mergesort3(self):
        assert mergesort([2, 1, 3, 4]) == [1, 2, 3, 4]
