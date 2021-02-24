
"""Week2 Test Cases: Count Inversions"""

from course1.week2.count_inversions import sort_and_count as count_inversions


class TestCountInversions:
    """Test cases for count inversions challenge."""

    def test_count_inversions_empty(self):
        _, inversions = count_inversions([])
        assert inversions == 0

    def test_count_inversions_single(self):
        _, inversions = count_inversions([1])
        assert inversions == 0

    def test_count_inversions_even(self):
        _, inversions = count_inversions([1, 2])
        assert inversions == 0

    def test_count_inversions_even2(self):
        _, inversions = count_inversions([2, 1])
        assert inversions == 1

    def test_count_inversions_odd(self):
        _, inversions = count_inversions([1, 2, 3])
        assert inversions == 0

    def test_count_inversions_odd1(self):
        _, inversions = count_inversions([1, 3, 2])
        assert inversions == 1

    def test_count_inversions_odd2(self):
        _, inversions = count_inversions([2, 1, 3])
        assert inversions == 1

    def test_count_inversions_odd3(self):
        _, inversions = count_inversions([3, 1, 2])
        assert inversions == 2

    def test_count_inversions_odd4(self):
        _, inversions = count_inversions([3, 2, 1])
        assert inversions == 3

    def test_count_inversions_odd5(self):
        _, inversions = count_inversions([2, 3, 1])
        assert inversions == 2

    def test_count_inversions(self):
        _, inversions = count_inversions([2, 4, 1, 3])
        assert inversions == 3

    def test_count_inversions2(self):
        _, inversions = count_inversions([1, 2, 4, 3])
        assert inversions == 1

    def test_count_inversions3(self):
        _, inversions = count_inversions([4, 3, 2, 1])
        assert inversions == 6
