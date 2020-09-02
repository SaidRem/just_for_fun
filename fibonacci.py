# Fibonacci numbers is such sequence in which each number is the
# sum of the two preceding ones, starting from 0 and 1.
# This script generates a list of the first N fibonacci numbers.
# Secondly, applied the map function and a lambda expression to
# cube each fibonacci number and print the list.
# Input format: one line of input: an integer n.


def fibonacci(n):
    fib_start = [0, 1]
    for i in range(2, n):
        fib_start.append(fib_start[i-2] + fib_start[i-1])
    return fib_start[:n]


if __name__ == '__main__':
    n = int(input())
    print(list(map(lambda x: x**3, fibonacci(n))))
