# Given a string s consisting only of digits 0-9, commas and dots.

# Sample input
# 100,000,000.000

# Sample output:
# 100
# 000
# 000
# 000

import re

regex_pattern = r"[.,]+"

print("\n".join(re.split(regex_pattern, input())))
