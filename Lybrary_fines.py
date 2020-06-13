'''
The program takes expected and actual return dates for
a library book, then calculates the fine (if any)
'''


from datetime import date


def fines(date_1, date_2):
    d_1 = date(date_1[2], date_1[1], date_1[0])
    d_2 = date(date_2[2], date_2[1], date_2[0])
    if d_1 <= d_2:
        return 0
    elif d_1.year > d_2.year:
        return 10000
    elif d_1.month > d_2.month:
        return 500*(d_1.month - d_2.month)
    else:
        delta = d_1 - d_2
        return 15*delta.days


date_1 = list(map(int, input().split()))
date_2 = list(map(int, input().split()))
print(fines(date_1, date_2))