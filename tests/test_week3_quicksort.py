"""Week3 Test Cases: Quicksort"""

from week3 import sort as randomized_quicksort


def test_quicksort_empty():
    assert randomized_quicksort([]) == []


def test_quicksort_single():
    assert randomized_quicksort([1]) == [1]


def test_quicksort_single_negative():
    assert randomized_quicksort([-1]) == [-1]


def test_quicksort_even():
    assert randomized_quicksort([1, 2]) == [1, 2]


def test_quicksort_even2():
    assert randomized_quicksort([2, 1]) == [1, 2]


def test_quicksort_mixed():
    assert randomized_quicksort([2, -1]) == [-1, 2]


def test_quicksort_mixed2():
    assert randomized_quicksort([-1, 2]) == [-1, 2]


def test_quicksort_odd():
    assert randomized_quicksort([1, 2, 3]) == [1, 2, 3]


def test_quicksort_odd1():
    assert randomized_quicksort([1, 3, 2]) == [1, 2, 3]


def test_quicksort_odd2():
    assert randomized_quicksort([2, 1, 3]) == [1, 2, 3]


def test_quicksort_odd3():
    assert randomized_quicksort([3, 1, 2]) == [1, 2, 3]


def test_quicksort_odd4():
    assert randomized_quicksort([3, 2, 1]) == [1, 2, 3]


def test_quicksort_odd5():
    assert randomized_quicksort([2, 3, 1]) == [1, 2, 3]


def test_randomized_quicksort():
    assert randomized_quicksort([2, 4, 1, 3]) == [1, 2, 3, 4]


def test_quicksort2():
    assert randomized_quicksort([1, 2, 4, 3]) == [1, 2, 3, 4]


def test_quicksort3():
    assert randomized_quicksort([2, 1, 3, 4]) == [1, 2, 3, 4]
