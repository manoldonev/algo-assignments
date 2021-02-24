#!/usr/bin/python

"""Test Playground"""

from src.course1.week1 import karatsuba

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
print('{0:d}'.format(karatsuba.multiply(x, y)))

# from src.course1.week2 import count_inversions

# with open("src/course1/week2/integer_array.txt") as file_handle:
#     lines = [int(line) for line in file_handle]

# _, inversions = count_inversions.sort_and_count(lines)
# print(inversions)

# from src.course1.week3 import count_comparisons

# with open("src/course1/week3/quicksort.txt") as file_handle:
#     lines = [int(line) for line in file_handle]

# _, comparisons = count_comparisons.sort_and_count(lines)
# print(comparisons)

# import math

# from src.course1.week4.mincut import min_cut

# graph = {}

# with open("src/course1/week4/kargerMinCut.txt") as file_handle:
#     for line in file_handle:
#         tokens = line.split()
#         graph[tokens[0]] = tokens[1:]

# n = len(graph)
# trials = math.ceil(n * n * math.log(n))

# result = n
# while trials > 0:
#     cut = min_cut(graph)
#     min_cut_candidate = len(cut[list(cut.keys())[0]])

#     if min_cut_candidate < result:
#         result = min_cut_candidate

#     trials -= 1
#     print(trials)

# print(result)
