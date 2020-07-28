# Integers in Python cab be as big as the bytes in a machine's
# memory. There is no limits in size as there is:
# 2^31 - 1 or 2^63 - 1

# Input
# integers a, b, c, d are given on four separate lines.

# Output
# Print the result of a^b + c^d
a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = a**b + c**d
print(result)