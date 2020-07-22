# append, pop, popleft and appendleft methods on an empty
# deque d.

# Input format:
# The first line contains an integer N, the number of operations.
# The next N lines contains the space separated names of methods
# and their values.

# Output format:
# Print out the space separated elements of deque d.

from collections import deque

d = deque()


n = int(input())

for _ in range(n):
    command, *args = input().split()
    getattr(d, command)(*args)

for i in d:
    print(i, end=' ')

if __name__ == '__main__':
    pass