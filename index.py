#!/usr/bin/python

"""Test Playground"""

# from week1 import karatsuba

# x = 3141592653589793238462643383279502884197169399375105820974944592
# y = 2718281828459045235360287471352662497757247093699959574966967627
# print '{0:d}'.format(karatsuba.multiply(x, y))

# from week2 import countInversions

# lines = [int(line) for line in open("tests/week2_integer_array.txt")]
# [sorted, inversions] = countInversions.sort_and_count(lines)
# print inversions

from week3 import countComparisons

lines = [int(line) for line in open("tests/week3_quicksort.txt")]
sorted, comparisons = countComparisons.sort_and_count(lines)
print comparisons
