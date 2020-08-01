# Given a polynomial P of a single indeterminate (or variable), x.

# Input format
# The first line contains the space separated values of x and k.
# The second line contains the polynomial P.

# Output format
# Print True if P(x) = k. Otherwise, print False

# Sample input
# 1 4
# x**3 + x**2 + x + 1

# Sample output
# True

x, k = map(float, input().split())

result = eval(input())
print(result == k)
