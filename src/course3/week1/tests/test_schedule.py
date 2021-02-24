"""Week1 Test Cases Schedule"""

from src.course3.week1.schedule import schedule_by_difference, schedule_by_ratio


def test_schedule_by_difference():
    # job (weight, length)
    jobs = [(1, 8), (2, 10), (3, 3), (4, 6)]
    schedule = schedule_by_difference(jobs)

    assert list(schedule) == [(3, 3), (4, 6), (1, 8), (2, 10)]


def test_schedule_by_difference_tiebreak_higher_weight():
    # job (weight, length)
    jobs = [(1, 8), (2, 10), (3, 3), (4, 4)]
    schedule = schedule_by_difference(jobs)

    assert list(schedule) == [(4, 4), (3, 3), (1, 8), (2, 10)]


def test_schedule_by_ratio():
    # job (weight, length)
    jobs = [(1, 8), (2, 10), (3, 3), (4, 6)]
    schedule = schedule_by_ratio(jobs)

    assert list(schedule) == [(3, 3), (4, 6), (2, 10), (1, 8)]
