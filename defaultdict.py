# The defaultdict tool is a container in the collections class of
# Python. It's similar to the usual dictionary container, but the
# only difference is that a defaultdict will have a default value
# if that key has not been set yet.

# Input format:
# The first line contains integers, n and m separated by a space.
# The next n lines contains the words belonging to group A.
# The next m lines contains the words belonging to group B.

# Output format:
# Output m lines.
# The i line should contain the indexed positions of the
# occurences of the i word separated by spaces.

from collections import defaultdict


d = defaultdict(list)

n, m = map(int, input().split())

res = []

for i in range(1, n+1):
    d[input()].append(i)

for i in range(m):
    res.append(input())

for i in res:
    if i in d:
        print(*d[i])
    else:
        print(-1)