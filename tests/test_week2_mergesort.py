"""Week2 Test Cases: Mergesort"""

from week2 import mergesort

def test_mergesort_empty():
    assert mergesort.sort([]) == []

def test_mergesort_single():
    assert mergesort.sort([1]) == [1]

def test_mergesort_single_negative():
    assert mergesort.sort([-1]) == [-1]

def test_mergesort_even():
    assert mergesort.sort([1, 2]) == [1, 2]

def test_mergesort_even2():
    assert mergesort.sort([2, 1]) == [1, 2]

def test_mergesort_mixed():
    assert mergesort.sort([2, -1]) == [-1, 2]

def test_mergesort_mixed2():
    assert mergesort.sort([-1, 2]) == [-1, 2]

def test_mergesort_odd():
    assert mergesort.sort([1, 2, 3]) == [1, 2, 3]

def test_mergesort_odd1():
    assert mergesort.sort([1, 3, 2]) == [1, 2, 3]

def test_mergesort_odd2():
    assert mergesort.sort([2, 1, 3]) == [1, 2, 3]

def test_mergesort_odd3():
    assert mergesort.sort([3, 1, 2]) == [1, 2, 3]

def test_mergesort_odd4():
    assert mergesort.sort([3, 2, 1]) == [1, 2, 3]

def test_mergesort_odd5():
    assert mergesort.sort([2, 3, 1]) == [1, 2, 3]

def test_mergesort():
    assert mergesort.sort([2, 4, 1, 3]) == [1, 2, 3, 4]

def test_mergesort2():
    assert mergesort.sort([1, 2, 4, 3]) == [1, 2, 3, 4]

def test_mergesort3():
    assert mergesort.sort([2, 1, 3, 4]) == [1, 2, 3, 4]
