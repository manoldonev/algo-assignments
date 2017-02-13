#!/usr/bin/python

"""Test Playground"""

import sys
import resource
from collections import defaultdict
from week1.scc import scc
from week2.dijkstra_naive import dijkstra
from week2.dijkstra_heapq import dijkstra as dijkstra_heapq

# # set rescursion limit and stack size limit
# sys.setrecursionlimit(10 ** 6)
# resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))


# def main():
#     graph = defaultdict(list)

#     with open("tests/week1_scc.txt") as handle:
#         for line in handle:
#             tokens = line.split()
#             graph[tokens[0]].append(tokens[1])

#     sccs_by_leader = scc(graph)

# return sorted((len(x) for x in sccs_by_leader.itervalues()),
# reverse=True)[:5]

def main():
    graph = defaultdict(list)
    with open("tests/week2_dijkstraData.txt") as handle:
        for line in handle:
            tokens = line.split()
            for i in range(1, len(tokens)):
                graph[int(tokens[0])].append([int(number)
                                              for number in tokens[i].split(",")])

    shortest_paths = dijkstra_heapq(graph, 1)

    test_cases = [str(shortest_paths[x])
                  for x in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]]
    return ",".join(test_cases)


if __name__ == '__main__':
    print main()
