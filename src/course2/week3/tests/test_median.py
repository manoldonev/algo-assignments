"""Week3 Test Cases (Median Maintenanace)"""

from src.course2.week3.median_maintenance import median


def test_median():
    assert list(median([7, 1, 3, 5, 2, 9, 4, 6, 8])) == [7, 1, 3, 3, 3, 3, 4, 4, 5]
