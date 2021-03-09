
"""Randomized Quicksort Implementation"""

from random import randint
from typing import List


def sort(numbers: List[int]) -> List[int]:
    """Quicksort public method"""
    _sort(numbers, 0, len(numbers) - 1)

    return numbers


def _sort(numbers: List[int], left: int, right: int):
    """Divide and conquer step"""

    if left >= right:
        return

    pivot_index = _partition(numbers, left, right)

    _sort(numbers, left, pivot_index - 1)
    _sort(numbers, pivot_index + 1, right)


def _partition(numbers: List[int], left: int, right: int) -> int:
    """Partition around pivot"""

    pivot_index = _choose_pivot_index(left, right)

    # Make sure chosen pivot is on first slot (relative to subarray)
    numbers[left], numbers[pivot_index] = numbers[pivot_index], numbers[left]
    pivot = numbers[left]

    # i denotes boundary b/n elements less than / greater than pivot.
    # j denotes boundary b/n processed / non-processed elements
    i = j = left + 1
    while j <= right:
        if numbers[j] < pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i += 1

        j += 1

    numbers[left], numbers[i - 1] = numbers[i - 1], numbers[left]

    return i - 1


def _choose_pivot_index(left: int, right: int):
    """Choose pivot"""

    # Choose random pivot
    return randint(left, right)
