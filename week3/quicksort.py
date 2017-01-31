
"""Randomized Quicksort Implementation"""

from random import randint

def sort(array):
    """Quicksort public method"""
    __sort(array, 0, len(array) - 1)

    return array

def __sort(array, l, r):
    """Divide and conquer step"""

    if r <= l:
        return

    pivot_index = partition(array, l, r)

    __sort(array, l, pivot_index - 1)
    __sort(array, pivot_index + 1, r)

def choose_pivot(array, l, r):
    """Choose pivot"""

    # Choose random pivot
    pivot_index = randint(l, r)

    # Make sure chosen pivot is on first slot (relative)
    swap(array, l, pivot_index)

    return l

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

def swap(array, i, j):
    """Swap routine"""
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
