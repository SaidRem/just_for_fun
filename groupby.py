# Given a string. Suppose a character occures consecutively x times
# in the string. Output these consecutive occurences of the character
# (x, c), where x is the number of times occured the 'c' character in
# the string.

# Input format:
# A single line of output consisting of the string.

# Output format:
# A single line of output consisting of the modified string.

from itertools import groupby

the_line = input()

print(*[(len(list(iter_string)), int(c))
        for c, iter_string in groupby(the_line)])
