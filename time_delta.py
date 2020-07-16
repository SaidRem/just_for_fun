# When users post an update on social media, sych as a URL, image,
# status update etc, other user in their network are able to view
# this new post on their news feed. Users can also see exactly when
# the post was published, i.e., how many hours, minutes or seconds ago.

# Since sometimes posts are published and viewed in different time
# zones, this can be confusing.

# Input format:
# The first line contains number of testcases.
# Each testcase contains 2 lines, representing time t1 and t2.
# Format t1 and t2: weekday dd MM YYYY hh:mm:ss +xxxx.
# +xxxx represents the time zone.

# Sample input
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000

# Output format
# absolute difference (t1 - t2) in seconds.

import os
from datetime import datetime as dt


fmt = '%a %d %b %Y %H:%M:%S %z'


def time_delta(t1, t2):
    delta = str(int(abs((dt.strptime(t1, fmt) - 
                dt.strptime(t2, fmt)).total_seconds())))
    return delta


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for _ in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()




