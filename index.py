#!/usr/bin/python

from collections import defaultdict
from week1.schedule import schedule_by_difference, schedule_by_ratio
from week1.prim_mst import prim
from week2.clustering import clusterize
from week2.hamming import calculate_hamming_clusters

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

# def main():
#     graph = defaultdict(list)
#     with open("tests/week1_prim.txt") as handle:
#         handle.readline()  # skip first line specifying number of vertices and edges
#         for line in handle:
#             vertex1, vertex2, cost = line.split()
#             # undirected graph so add the edge in both directions
#             graph[int(vertex1)].append((int(vertex2), int(cost)))
#             graph[int(vertex2)].append((int(vertex1), int(cost)))

#         mst = prim(graph)

#         total_mst_cost = 0
#         for cost, _, _ in mst:
#             total_mst_cost += cost

#         return total_mst_cost

# def main():
#     graph = defaultdict(list)
#     edge_list = []
#     with open("tests/week2_clustering.txt") as handle:
#         handle.readline()  # skip first line specifying number of vertices and edges
#         for line in handle:
#             vertex1, vertex2, cost = line.split()
#             # undirected graph so add the edge in both directions
#             # make them zero-based
#             graph[int(vertex1) - 1].append((int(vertex2) - 1, int(cost)))
#             graph[int(vertex2) - 1].append((int(vertex1) - 1, int(cost)))

#             edge_list.append((int(cost), int(vertex1) - 1, int(vertex2) - 1))

#         _, max_spacing = clusterize(graph, edge_list, 4)

#         return max_spacing


def main():
    numbers = []
    with open("tests/week2_clustering_big.txt") as handle:
        handle.readline()
        for line in handle:
            numbers.append(int(line.replace(" ", ""), base=2))

    return calculate_hamming_clusters(numbers)


if __name__ == '__main__':
    print(main())
