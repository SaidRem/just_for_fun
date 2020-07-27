# Two sets: A and B.

# Input format:
# The first line will contain the number of test cases T.
# The first line of each test case contains the number of elements in set A.
# The second line of each test case contains the space separated elements of set A.
# The third line of each test case contains the number of elements in set B.
# The fourth line of each test case contains the space separated elements of set B.

# Sample input
# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2

# Sample output
# True
# False
# False

# Output True of False for each test case on separate lines.

test_cases = int(input())

results = []
for _ in range(test_cases):
    n_a = int(input())
    a = set(input().split())
    n_b = int(input())
    b = set(input().split())
    results.append(a.issubset(b))

for result in results:
    print(result)