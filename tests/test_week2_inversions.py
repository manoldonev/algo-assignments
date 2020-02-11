
"""Week2 Test Cases: Count Inversions"""

from week2 import sort_and_count as count_inversions


def test_count_inversions_empty():
    _, inversions = count_inversions([])
    assert inversions == 0


def test_count_inversions_single():
    _, inversions = count_inversions([1])
    assert inversions == 0


def test_count_inversions_even():
    _, inversions = count_inversions([1, 2])
    assert inversions == 0


def test_count_inversions_even2():
    _, inversions = count_inversions([2, 1])
    assert inversions == 1


def test_count_inversions_odd():
    _, inversions = count_inversions([1, 2, 3])
    assert inversions == 0


def test_count_inversions_odd1():
    _, inversions = count_inversions([1, 3, 2])
    assert inversions == 1


def test_count_inversions_odd2():
    _, inversions = count_inversions([2, 1, 3])
    assert inversions == 1


def test_count_inversions_odd3():
    _, inversions = count_inversions([3, 1, 2])
    assert inversions == 2


def test_count_inversions_odd4():
    _, inversions = count_inversions([3, 2, 1])
    assert inversions == 3


def test_count_inversions_odd5():
    _, inversions = count_inversions([2, 3, 1])
    assert inversions == 2


def test_count_inversions():
    _, inversions = count_inversions([2, 4, 1, 3])
    assert inversions == 3


def test_count_inversions2():
    _, inversions = count_inversions([1, 2, 4, 3])
    assert inversions == 1


def test_count_inversions3():
    _, inversions = count_inversions([4, 3, 2, 1])
    assert inversions == 6
