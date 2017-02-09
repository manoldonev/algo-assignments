#!/usr/bin/python

"""Test Playground"""

import sys
import resource
from collections import defaultdict
from week1.scc import scc

# set rescursion limit and stack size limit
sys.setrecursionlimit(10 ** 6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))


def main():
    graph = defaultdict(list)
    for line in open("tests/week1_scc.txt"):
        tokens = line.split()
        graph[tokens[0]].append(tokens[1])

    sccs_by_leader = scc(graph)

    return sorted((len(x) for x in sccs_by_leader.itervalues()), reverse=True)[:5]


if __name__ == '__main__':
    print main()
