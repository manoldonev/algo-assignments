
import sys

from heapq import heappush, heappop, heapify


class PriorityQueue:
    """Priority queue implementation based on heapq
    See https://docs.python.org/2/library/heapq.html#priority-queue-implementation-notes"""

    REMOVED = sys.maxsize

    def __init__(self, heap=None):
        if heap is None:
            heap = []
        else:
            heapify(heap)

        self.heap = heap
        self.entry_finder = {i[-1]: i for i in heap}

    def add_task(self, task, priority=0):
        """Add new priority task."""
        if task in self.entry_finder:
            self.remove_task(task)

        entry = [priority, task]
        self.entry_finder[task] = entry
        heappush(self.heap, entry)

    def remove_task(self, task):
        """Mark an existing task as REMOVED.  Raise KeyError if not found."""
        entry = self.entry_finder.pop(task)
        entry[-1] = PriorityQueue.REMOVED

        return entry[0]

    def pop_task(self):
        """Remove and return the lowest priority task. Raise KeyError if empty."""
        while self.heap:
            priority, task = heappop(self.heap)
            if task is not PriorityQueue.REMOVED:
                del self.entry_finder[task]
                return priority, task

        raise KeyError('pop from an empty priority queue')
