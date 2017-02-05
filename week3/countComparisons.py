
"""Quicksort Implementation"""


def sort_and_count(array):
    """Quicksort public method"""

    comparisons = _sort_and_count(array, 0, len(array) - 1)

    return array, comparisons


def _sort_and_count(array, l, r):
    """Divide and conquer step"""

    if l >= r:
        return 0

    pivot_index = partition(array, l, r)

    comparisons_left = _sort_and_count(array, l, pivot_index - 1)
    comparisions_right = _sort_and_count(array, pivot_index + 1, r)

    return r - l + comparisons_left + comparisions_right


def partition(array, l, r):
    """Partition around pivot"""
    pivot_index = choose_pivot_median(array, l, r)
    pivot = array[pivot_index]

    i = l + 1
    j = l + 1
    while j <= r:
        if array[j] < pivot:
            swap(array, i, j)
            i += 1

        j += 1

    swap(array, l, i - 1)

    return i - 1


def choose_pivot_first(array, l, r):
    """Choose first element as pivot"""

    return l


def choose_pivot_last(array, l, r):
    """Choose last element as pivot"""

    swap(array, l, r)
    return l


def choose_pivot_median(array, l, r):
    """Choose median element as pivot"""

    first = array[l]
    last = array[r]

    n = r - l + 1

    middle_index = n / 2 + n % 2 - 1
    middle = array[l + middle_index]

    median = find_median(first, middle, last)
    median_index = array.index(median)

    swap(array, l, median_index)

    return l


def find_median(a, b, c):
    """Find median of three elements"""
    x = a - b
    y = b - c
    z = a - c

    if x * y > 0:
        return b

    if x * z > 0:
        return c

    return a


def swap(array, i, j):
    """Swap routine"""
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
