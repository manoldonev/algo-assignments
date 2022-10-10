"""Quicksort Implementation"""


def sort_and_count(numbers: list[int]) -> tuple[list[int], int]:
    """Quicksort public method"""

    comparisons = _sort_and_count(numbers, 0, len(numbers) - 1)

    return numbers, comparisons


def _sort_and_count(numbers: list[int], left: int, right: int) -> int:
    """Divide and conquer step"""

    if left >= right:
        return 0

    pivot_index = partition(numbers, left, right)

    comparisons_left = _sort_and_count(numbers, left, pivot_index - 1)
    comparisions_right = _sort_and_count(numbers, pivot_index + 1, right)

    return right - left + comparisons_left + comparisions_right


def partition(numbers: list[int], left: int, right: int) -> int:
    """Partition around pivot"""

    pivot_index = choose_pivot_median(numbers, left, right)

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


def choose_pivot_first(_: list[int], left: int, __: int) -> int:
    """Choose first element as pivot"""
    return left


def choose_pivot_last(_: list[int], __: int, right: int) -> int:
    """Choose last element as pivot"""
    return right


def choose_pivot_median(numbers: list[int], left: int, right: int) -> int:
    """Choose median element as pivot"""

    first = numbers[left]
    last = numbers[right]

    middle_index = left + (right - left) // 2
    middle = numbers[middle_index]

    median = find_median(first, middle, last)
    median_index = numbers.index(median)

    return median_index


def find_median(a: int, b: int, c: int) -> int:
    """Find median of three elements"""
    x = a - b
    y = b - c
    z = a - c

    if x * y > 0:
        return b

    if x * z > 0:
        return c

    return a
