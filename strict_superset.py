# Given a set A and n other sets.
# Is A a strict superset of each of the n sets.

# Input:
# The first line contains the space separated elements of set A.
# The second line contains integer n, the number of other sets.
# The next n lines contains the  space separated elements of the other sets.

# Output
# Print True if set A is a strict superset of all other N sets.
# Otherwise, print False.

a = set(input().split())
print(all(a > set(input().split()) for _ in range(int(input()))))