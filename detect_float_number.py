# The first line contains an integer number of test cases.
# The next line contains a string
# A valid float number must satisfy all of the following requirements:
# +3.50
# -1.0
# .5
# -.4

# Output True or False for each test case.

import re

for _ in range(int(input())):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))