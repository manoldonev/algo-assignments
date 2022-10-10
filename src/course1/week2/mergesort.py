""" Mergesort Implementation """


def sort(numbers: list[int]) -> list[int]:
    """Divide & Conquer Step"""

    n = len(numbers)
    if n <= 1:
        return numbers

    nby2 = n // 2
    sorted_left = sort(numbers[:nby2])
    sorted_right = sort(numbers[nby2:])

    return merge(sorted_left, sorted_right)


def merge(left: list[int], right: list[int]) -> list[int]:
    """Combine Step"""

    n_left = len(left)
    n_right = len(right)
    i = 0
    j = 0
    merged: list[int] = []

    while i < n_left and j < n_right:
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    if i == n_left:
        merged.extend(right[j:])
    elif j == n_right:
        merged.extend(left[i:])

    return merged
