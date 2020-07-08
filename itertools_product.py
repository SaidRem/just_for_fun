# This tool computes the cartesian product of input iterables.
# It is equivalent to nested for-loops.
# For example, product(A, B) returns the same as ((x, y) for x in A for y in B)

# Input format:
# The first line contains the space separated elements of list A.
# The second line contains the space separated elements of list B.

# Output format:
# Output the space separated tuples of the cartesian product.

from itertools import product

arr_1 = tuple(map(int, input().split()))
arr_2 = tuple(map(int, input().split()))

result = product(arr_1, arr_2)

for row in result:
    print(row, end=' ')
