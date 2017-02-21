
"""2-Sum Problem Package"""

import bisect


def two_sum(numbers, delta=10000):
    """2-Sum Problem in [-delta, delta]"""
    numbers.sort()
    two_sums = set()
    for x in numbers:
        # two-sum complement can only be in range [-delta -x, delta -x]
        lower = bisect.bisect_left(numbers, -delta - x)
        upper = bisect.bisect_right(numbers, delta - x)
        for y in numbers[lower:upper]:
            if x != y and x + y not in two_sums:
                two_sums.add(x + y)

    return len(two_sums)


def two_sum_generator(hash_table, target):
    """2-Sum Problem in [-delta, delta] (hash version)"""
    for x in hash_table:
        if target - x in hash_table and 2 * x != target:
            yield (x, target - x)
