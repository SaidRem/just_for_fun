# Given two values a and b.
# Perform integer division and print a/b.

# Input fromat:
# The first line contains T, the number of test cases.
# The next T lines each contain the space separated values of a and b.

# Output format
# In the case of ZeroDivisionError or ValueError, print the error code.

n = int(input())
for _ in range(n):
    a, b = input().split()
    try:
        a, b = int(a), int(b)
        print(a/b)
    except ValueError as err:
        print('Error Code: ', err)
    except ZeroDivisionError as err:
        print('Error Code: ', err)

