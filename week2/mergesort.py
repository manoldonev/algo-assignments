
""" Mergesort Implementation """

def sort(array):
    """Divide & Conquer Step"""
    n = len(array)
    nby2 = n / 2

    if n <= 1:
        return array

    sorted_left = sort(array[:nby2])
    sorted_right = sort(array[nby2:])

    return merge(sorted_left, sorted_right)

def merge(left, right):
    """Combine Step"""
    n_left = len(left)
    n_right = len(right)
    i = 0
    j = 0
    merged = []

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
