# The first and last names of people begin with a capital letter
# in their passports. For example, alan grin should be capitalised
# correctly as Alan Grin.

import math
import os
import random
import re
import sys


def solve(s):
    for name in s.split():
        s = s.replace(name, name.capitalize())
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
