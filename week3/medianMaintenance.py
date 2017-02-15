
"""Median Maintenance Package"""

from heapq import heappop, heappush


def median(numbers):
    """Median Maintenance"""
    heap_low = [-numbers[0]]
    yield abs(heap_low[0])

    if numbers[1] < numbers[0]:
        heap_low, heap_high = [-numbers[1]], [numbers[0]]
    else:
        heap_high = [numbers[1]]

    yield abs(heap_low[0])

    diff = 0
    for n in numbers[2:]:
        if n > heap_high[0]:
            heappush(heap_high, n)
            diff += 1
        else:
            heappush(heap_low, -n)
            diff -= 1

        if diff < -1:
            swap_element = abs(heappop(heap_low))
            heappush(heap_high, swap_element)
            diff = 0
        elif diff > 1:
            swap_element = heappop(heap_high)
            heappush(heap_low, -swap_element)
            diff = 0

        if diff > 0:
            yield heap_high[0]
        else:
            yield abs(heap_low[0])
