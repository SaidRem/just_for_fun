# Print all possible combinations, up to size k, of the string in
# lexicographic sorted order.

# Input format:
# a single line containing the string S and integer value k separated
# by a space.
# The string contains only UPPERCASE characters.

# Output format:
# Print the different combinations of string S on separate lines.

from itertools import combinations
# itertools.combinations returns the r length subsequences of elements from
# the input iterable.
# Cobinations are emitted in lexicographic sorted order. So, if the input
# iterabel is sorted, the combination tuples will be produced in sorted
# order.
s, c = input().split()

s, c = input().split()
for i in range(1, int(c)+1):
    for row in combinations(sorted(s), i):
        print(''.join(row))
