from heapq import heappush, heappop, heapify
from dataclasses import dataclass, field
from typing import Generic, Optional, TypeVar

T = TypeVar("T")
S = TypeVar("S")


@dataclass(order=True)
class PrioritizedItem(Generic[T, S]):
    priority: S
    task: T = field(compare=False)
    is_active: bool = field(default=True, compare=False)


class PriorityQueue(Generic[T, S]):
    """Priority queue implementation based on heapq
    See https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes"""

    def __init__(self, items: Optional[list[PrioritizedItem[T, S]]] = None):
        if items is None:
            items = []
        else:
            heapify(items)

        # list of entries arranged in a heap
        self._heap = items

        # mapping of tasks to entries
        self._entry_finder: dict[T, PrioritizedItem[T, S]] = {
            entry.task: entry for entry in items
        }

    @property
    def is_empty(self):
        return not self._entry_finder

    def add_task(self, task: T, priority: S):
        """Add new priority task."""
        if task in self._entry_finder:
            self.remove_task(task)

        entry = PrioritizedItem(priority, task)
        self._entry_finder[task] = entry
        heappush(self._heap, entry)

    def remove_task(self, task: T) -> S:
        """Mark an existing task as not active and return its priority.  Raise KeyError if not found."""
        entry = self._entry_finder.pop(task)
        entry.is_active = False

        return entry.priority

    def pop_task(self) -> tuple[S, T]:
        """Remove and return the lowest priority task. Raise KeyError if empty."""
        while self._heap:
            item = heappop(self._heap)
            if item.is_active:
                del self._entry_finder[item.task]
                return item.priority, item.task

        raise KeyError("pop from an empty priority queue")
