
"""Week4 Test Cases"""

from collections import deque

from src.course2.week4.twoSumProblem import two_sum_generator


def test_twoSum():
    expected = deque([(1, 9),
                      (2, 8),
                      (3, 7),
                      (4, 6),
                      (6, 4),
                      (7, 3),
                      (8, 2),
                      (9, 1)])

    # sets are implemented as hash tables
    hash_table = set([1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -
                      2, -3, -4, -5, -6, -7, -8, -9, 0])

    for result in two_sum_generator(hash_table, 10):
        assert result == expected.popleft()
