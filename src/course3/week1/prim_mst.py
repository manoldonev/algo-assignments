
"""Prim's Minimum Spanning Tree Algorithm"""

import sys
from random import randint
from typing import Mapping

from src.common.priority_queue import PriorityQueue, PrioritizedItem


def prim(graph: Mapping[int, list[tuple[int, int]]]):
    n = len(graph)
    source = randint(1, n)

    explored_vertices = set([source])
    mst = set()
    min_heap = initialize_heap(graph, source)

    while n > 1:
        weighted_edge, min_vertex_key = min_heap.pop_task()
        explored_vertices.add(min_vertex_key)
        mst.add(weighted_edge)

        for vertex2, cost in graph[min_vertex_key]:
            if vertex2 in explored_vertices:
                continue

            old_min_cost_edge = min_heap.remove_task(vertex2)
            old_min_cost = old_min_cost_edge[0]
            if (cost < old_min_cost):
                min_cost_edge = (cost, min_vertex_key, vertex2)
            else:
                min_cost_edge = old_min_cost_edge

            min_heap.add_task(vertex2, min_cost_edge)

        n -= 1

    return mst


def initialize_heap(graph: Mapping[int, list[tuple[int, int]]], source: int):
    costs: dict[int, tuple[int, int, int]] = {
        key: (sys.maxsize, -1, -1) for key in graph if key != source}
    for vertex2, cost in graph[source]:
        costs[vertex2] = (cost, source, vertex2)

    items = [PrioritizedItem(value, key)
             for key, value in costs.items()]

    return PriorityQueue(items)
