# This script generates a list of the first N fibonacci numbers.
# Secondly, applied the map function and a lambda expression to
# cube each fibonacci number and print the list.
# Input format: one line of input: an integer n.


def fibonacci(n):
    fib = [0, 1]
    i = 0
    j = 1
    if n <= 2:
        return fib[:n]
    for i in range(n-2):
        fib.append(fib[i] + fib[i+1])
    return fib


if __name__ == '__main__':
    n = int(input())
    print(list(map(lambda x: x**3, fibonacci(n))))
