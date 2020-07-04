# Given a string 'S' and width 'w'
# Wrap the string into a paragraph of width 'w'

# The first line contains a string 'S'
# The second line contains the width 'w'
import textwrap


def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, width=max_width))


def test_1():
    assert 'ABCD\nEFGH\nIJKL' == wrap('ABCDEFGHIJKL', 4)


if __name__ == '__main__':
    test_1()
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
