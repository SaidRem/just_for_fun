# The first line contains an integer n. n is the total number of integers
# in the list.
# The second line contains the space separated list of n integers.

# Output format
# Print True if all the conditions of the problem statement are satisfied.
# Otherwise, print False.

n = int(input())

numbers = list(map(int, input().split()))

checked_num = [i >= 0 for i in numbers]


def checking():
    if all(checked_num):
        for i in numbers:
            if str(i) == str(i)[::-1]:
                return True
    return False


print(checking())
