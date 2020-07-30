# Input format:
# A single line containing integer N.

# Output format:
# Print a numerical triangle of height N - 1 like the one below:
# 1
# 22
# 333
# 4444
# 55555

for i in range(1, int(input())):
    print((10**(i) // 9) * i)         # Pure math

# Another version:

# for i in range(1, int(input())):
#     print([0, 1, 22, 333, 4444, 55555, 666666,
#            7777777, 88888888, 999999999][i])
