
""" Count Inversions (Extended Mergesort Algorithm) """

def sort_and_count(array):
    """Divide & Conquer Step"""
    n = len(array)
    nby2 = n / 2

    if n <= 1:
        return [array, 0]

    [sorted_left, left_inversions] = sort_and_count(array[:nby2])
    [sorted_right, right_inversions] = sort_and_count(array[nby2:])

    [merged, split_inversions] = merge_and_count(sorted_left, sorted_right)

    return [merged, left_inversions + right_inversions + split_inversions]

def merge_and_count(left, right):
    """Combine Step"""
    n_left = len(left)
    n_right = len(right)
    i = 0
    j = 0
    merged = []
    split_inversions = 0

    while i < n_left and j < n_right:
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            split_inversions += n_left - i

    if i == n_left:
        merged.extend(right[j:])
    elif j == n_right:
        merged.extend(left[i:])

    return [merged, split_inversions]
