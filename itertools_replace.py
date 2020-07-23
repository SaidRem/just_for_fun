# Given a string.
# Print all possible size replacement combinations of the string in
# lexicographic sorted order.

# Input format:
# A sinfle line containing the string and integer value separated by a space.

# Output format:
# Print the combinations with their replacements of the string on separate lines.

from itertools import combinations_with_replacement
# This tool return r lingth subsequences of elements of elements from
# the input iterable allowing individual elements to be repeated more
# than once.
string, n = input().split()

combinations = combinations_with_replacement(sorted(string), int(n))

for row in combinations:
    print(''.join(row))
