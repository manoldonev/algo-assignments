"""Test cases for mergesort."""

from src.course1.week2.mergesort import sort as mergesort


def test_mergesort_empty():
    assert mergesort([]) == []


def test_mergesort_single():
    assert mergesort([1]) == [1]


def test_mergesort_single_negative():
    assert mergesort([-1]) == [-1]


def test_mergesort_even():
    assert mergesort([1, 2]) == [1, 2]


def test_mergesort_even2():
    assert mergesort([2, 1]) == [1, 2]


def test_mergesort_mixed():
    assert mergesort([2, -1]) == [-1, 2]


def test_mergesort_mixed2():
    assert mergesort([-1, 2]) == [-1, 2]


def test_mergesort_odd():
    assert mergesort([1, 2, 3]) == [1, 2, 3]


def test_mergesort_odd1():
    assert mergesort([1, 3, 2]) == [1, 2, 3]


def test_mergesort_odd2():
    assert mergesort([2, 1, 3]) == [1, 2, 3]


def test_mergesort_odd3():
    assert mergesort([3, 1, 2]) == [1, 2, 3]


def test_mergesort_odd4():
    assert mergesort([3, 2, 1]) == [1, 2, 3]


def test_mergesort_odd5():
    assert mergesort([2, 3, 1]) == [1, 2, 3]


def test_mergesort():
    assert mergesort([2, 4, 1, 3]) == [1, 2, 3, 4]


def test_mergesort2():
    assert mergesort([1, 2, 4, 3]) == [1, 2, 3, 4]


def test_mergesort3():
    assert mergesort([2, 1, 3, 4]) == [1, 2, 3, 4]
