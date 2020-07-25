# Read in two integers and print three lines.
# The first line is the integer division: a // b.
# The second line is the result of the modulo operator.
# The third line prints the tuple of numbers.

a = int(input())
b = int(input())
# divmod is one of the built-in functions, which takes two
# arguments and returns a tuple (x // y, x * y).
# Invariant: div * y + mod == x.
result = divmod(a, b)

print(result[0], result[1], result, sep='\n')
