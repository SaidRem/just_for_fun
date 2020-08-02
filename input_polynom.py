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

# The eval() built-in function helps evaluating an expression.
# The expression can be a Python statement, or a code object.

# expression = input()
# eval(expression)

# Sample input: print(2 + 3)
# Sample output: 5
