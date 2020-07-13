# Input format
# A single line of input contain the space separated
# month, day and year (MM DD YYYY).

# Output format
# Output the correct day in capital letters.

import calendar

month, day, year = map(int, input().split())

num_of_day = calendar.weekday(year, month, day)

print(calendar.day_name[num_of_day].upper())
