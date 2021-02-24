
"""Randomized Selection Implementation"""

from random import randint


def rselect(array, i):
    """Rselect public method"""
    return _rselect(array, 0, len(array) - 1, i)


def _rselect(array, l, r, i):
    """Divide and conquer step"""

    if l >= r:
        return array[r]

    pivot_index = partition(array, l, r)

    if pivot_index == i:
        return array[i]
    elif pivot_index > i:
        return _rselect(array, l, pivot_index - 1, i)
    else:
        return _rselect(array, pivot_index + 1, r, i)


def partition(array, l, r):
    """Partition around pivot"""
    pivot_index = choose_pivot(array, l, r)
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


def choose_pivot(array, l, r):
    """Choose pivot"""

    # Choose random pivot
    pivot_index = randint(l, r)

    # Make sure chosen pivot is on first slot (relative)
    swap(array, l, pivot_index)

    return l


def swap(array, i, j):
    """Swap routine"""
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
