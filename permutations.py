# Returns successive length permutations of elements in an iterable.
# Given a string to print all possible permutations of size k of the
# string in lexicographic sorted order.

# Input format:
# A single line containing the space separated string S and the integer value k.

# Output format:
# Print the permutations of the string S on separate lines.

from itertools import permutations

'''
input_data = input().split()

process_data = list(permutations(input_data[0], int(input_data[1])))

for i, j in sorted(process_data):
    print(f'{i}{j}')
'''

# Optimized version

s, n = input().split()
print(*[''.join(i) for i in permutations(sorted(s), int(n))], sep='\n')