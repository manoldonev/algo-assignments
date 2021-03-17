#!/usr/bin/python

import sys
from collections import defaultdict

from src.course3.week1.schedule import schedule_by_difference, schedule_by_ratio
from src.course3.week1.prim_mst import prim
from src.course3.week2.clustering import clusterize
from src.course3.week2.hamming import calculate_hamming_clusters
from src.course3.week3.huffman import make_huffman_tree, get_encoding, get_max_length, get_min_length
from src.course3.week3.mwis import calculate_maximum_weight_independent_set, reconstruct_weight_independent_set
from src.course3.week4.knapsack import knapsack, knapsack_recursive


# def main():
#     jobs = []
#     with open('src/course3/week1_jobs.txt') as handle:
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
#     with open('src/course3/week1_prim.txt') as handle:
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
#     with open('src/course3/week2_clustering.txt') as handle:
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


# def main():
#     numbers = []
#     with open('src/course3/week2_clustering_big.txt') as handle:
#         handle.readline()
#         for line in handle:
#             numbers.append(int(line.replace(' ', ''), base=2))

#     return calculate_hamming_clusters(numbers)

# def main():
#     symbols = {}
#     n = 0
#     with open('src/course3/week3_huffman.txt') as handle:
#         handle.readline()
#         for line in handle:
#             symbols[f'symbol{n}'] = int(line)
#             n += 1

#     huffman_tree = make_huffman_tree(symbols)
#     encoding = get_encoding(huffman_tree)
#     return encoding, get_max_length(encoding), get_min_length(encoding)

# def main():
#     with open('src/course3/week3_mwis.txt') as handle:
#         handle.readline()
#         graph_list = [int(line) for line in handle]

#     max_weights = calculate_maximum_weight_independent_set(graph_list)
#     max_weight_independent_set = reconstruct_weight_independent_set(
#         graph_list, max_weights)

#     # 1-based indices
#     result = ''
#     for index in [1, 2, 3, 4, 17, 117, 517, 997]:
#         result += f'{int(index - 1 in max_weight_independent_set)}'

#     return result

def main():
    sys.setrecursionlimit(10000)

    items = []
    with open('src/course3/week4_knapsack_big.txt') as handle:
        knapsack_size, _ = handle.readline().split()
        knapsack_size = int(knapsack_size)
        for line in handle:
            value, weight = line.split()
            items.append((int(value), int(weight)))

    return knapsack_recursive(items, knapsack_size)


if __name__ == '__main__':
    print(main())
