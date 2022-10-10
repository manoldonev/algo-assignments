"""PriorityQueue Test Cases"""

from collections import deque
import pytest

from src.common.priority_queue import PrioritizedItem, PriorityQueue


def test_case_init():
    pq = PriorityQueue[str, int]()
    assert pq is not None
    assert isinstance(pq, PriorityQueue)


def test_case_remove_nonexistent_task_raises_error():
    pq = PriorityQueue[str, int]()
    with pytest.raises(KeyError):
        pq.remove_task("no-such-task")


def test_case_1():
    pq = PriorityQueue[str, int]()
    pq.add_task("A", 5)
    pq.add_task("B", 1)
    pq.add_task("C", 4)
    pq.add_task("D", 3)
    pq.add_task("E", 2)

    expected = deque([(1, "B"), (2, "E"), (3, "D"), (4, "C"), (5, "A")])

    while not pq.is_empty:
        assert pq.pop_task() == expected.popleft()

    assert not expected


def test_case_2():
    pq = PriorityQueue[str, int]()
    pq.add_task("A", 5)

    assert pq.pop_task() == (5, "A")
    assert pq.is_empty

    pq.add_task("B", 1)
    pq.add_task("C", 4)

    assert pq.pop_task() == (1, "B")
    assert not pq.is_empty

    pq.add_task("D", 3)
    pq.add_task("E", 2)

    assert pq.remove_task("E") == 2
    assert pq.pop_task() == (3, "D")


def test_case_3():
    pq = PriorityQueue[str, int]()
    pq.add_task("A", 5)
    pq.add_task("B", 1)
    assert not pq.is_empty

    pq.remove_task("A")
    pq.remove_task("B")
    assert pq.is_empty


def test_case_4():
    pq = PriorityQueue[str, int]()
    pq.add_task("A", 5)
    pq.add_task("B", 1)
    pq.remove_task("A")
    pq.remove_task("B")

    with pytest.raises(KeyError):
        pq.pop_task()


def test_case_5():
    data = [("A", 2), ("B", 1), ("C", 3)]
    items = [PrioritizedItem(value, key) for key, value in data]
    pq = PriorityQueue(items)
    assert not pq.is_empty
    assert pq.pop_task() == (1, "B")
    assert pq.remove_task("A") == 2
    assert pq.pop_task() == (3, "C")
    assert pq.is_empty


def test_case_6():
    pq = PriorityQueue[str, int]()
    pq.add_task("A", -5)
    pq.add_task("B", 1)
    pq.add_task("C", -4)
    pq.add_task("D", 3)
    pq.add_task("E", -2)

    expected = deque([(-5, "A"), (-4, "C"), (-2, "E"), (1, "B"), (3, "D")])

    while not pq.is_empty:
        assert pq.pop_task() == expected.popleft()

    assert not expected
