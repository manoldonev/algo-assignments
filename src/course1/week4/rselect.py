
"""Randomized Selection Implementation"""

from random import randint


def rselect(numbers: list[int], i: int) -> int:
    """Rselect public method"""
    return _rselect(numbers, 0, len(numbers) - 1, i)


def _rselect(numbers: list[int], left: int, right: int, i: int) -> int:
    """Divide and conquer step"""

    if left >= right:
        return numbers[right]

    pivot_index = _partition(numbers, left, right)

    if pivot_index == i:
        return numbers[i]

    if pivot_index > i:
        return _rselect(numbers, left, pivot_index - 1, i)

    return _rselect(numbers, pivot_index + 1, right, i)


def _partition(numbers: list[int], left: int, right: int) -> int:
    """Partition around pivot"""

    pivot_index = _choose_pivot(numbers, left, right)

    # Make sure chosen pivot is on first slot (relative to subarray)
    numbers[left], numbers[pivot_index] = numbers[pivot_index], numbers[left]
    pivot = numbers[left]

    i = left + 1
    j = left + 1
    while j <= right:
        if numbers[j] < pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i += 1

        j += 1

    numbers[left], numbers[i - 1] = numbers[i - 1], numbers[left]

    return i - 1


def _choose_pivot(_: list[int], left: int, right: int) -> int:
    """Choose pivot"""

    # Choose random pivot
    return randint(left, right)
