#!/usr/bin/python

from collections import defaultdict
from week1.schedule import schedule_by_difference, schedule_by_ratio
from week1.prim_mst import prim


# def main():
#     jobs = []
#     with open("tests/week1_jobs.txt") as handle:
#         handle.readline()  # skip first line specifying number of jobs
#         for line in handle:
#             weight, length = line.split()
#             jobs.append((int(weight), int(length)))

#     completion_time = 0
#     weighted_completion_times_sum = 0
#     schedule = schedule_by_ratio(jobs)
#     for weight, length in schedule:
#         completion_time += length
#         weighted_completion_times_sum += weight * completion_time

#     return weighted_completion_times_sum

def main():
    graph = defaultdict(list)
    with open("tests/week1_prim.txt") as handle:
        handle.readline()  # skip first line specifying number of vertices and edges
        for line in handle:
            vertex1, vertex2, cost = line.split()
            # undirected graph so add the edge in both directions
            graph[int(vertex1)].append((int(vertex2), int(cost)))
            graph[int(vertex2)].append((int(vertex1), int(cost)))

        mst = prim(graph)

        total_mst_cost = 0
        for cost, _, _ in mst:
            total_mst_cost += cost

        return total_mst_cost


if __name__ == '__main__':
    print(main())
