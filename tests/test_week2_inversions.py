
"""Week2 Test Cases: Count Inversions"""

from week2.countInversions import sort_and_count as count_inversions

def test_count_inversions_empty():
    [array, inversions] = count_inversions([])
    assert inversions == 0

def test_count_inversions_single():
    [array, inversions] = count_inversions([1])
    assert inversions == 0

def test_count_inversions_even():
    [array, inversions] = count_inversions([1, 2])
    assert inversions == 0

def test_count_inversions_even2():
    [array, inversions] = count_inversions([2, 1])
    assert inversions == 1

def test_count_inversions_odd():
    [array, inversions] = count_inversions([1, 2, 3])
    assert inversions == 0

def test_count_inversions_odd1():
    [array, inversions] = count_inversions([1, 3, 2])
    assert inversions == 1

def test_count_inversions_odd2():
    [array, inversions] = count_inversions([2, 1, 3])
    assert inversions == 1

def test_count_inversions_odd3():
    [array, inversions] = count_inversions([3, 1, 2])
    assert inversions == 2

def test_count_inversions_odd4():
    [array, inversions] = count_inversions([3, 2, 1])
    assert inversions == 3

def test_count_inversions_odd5():
    [array, inversions] = count_inversions([2, 3, 1])
    assert inversions == 2

def test_count_inversions():
    [array, inversions] = count_inversions([2, 4, 1, 3])
    assert inversions == 3

def test_count_inversions2():
    [array, inversions] = count_inversions([1, 2, 4, 3])
    assert inversions == 1

def test_count_inversions3():
    [array, inversions] = count_inversions([4, 3, 2, 1])
    assert inversions == 6
