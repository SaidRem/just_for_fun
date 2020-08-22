import numpy as np

# Input format:
# The first line contains the space separated values of n and m.
# The next n lines contains the space separated elements of m columns.

# Output format:
# Print the transpose array and then print the flatten.


def tran_flat():
    n, m = map(int, input().split())
    my_arr = np.array([input().split() for _ in range(n)], int)
    print(np.transponse(my_arr))
    print(my_arr.flatten())


if __name__ == '__main__':
    tran_flat()

