
'''

The script takes your birthday and the current date and
calculates your age in days.
Account for leap days. Calc without using built-in functions.
'''

Month_in_leapy = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
Month_in_non_leapy = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def leap_year(y):
    if y % 4 != 0:
        return Month_in_non_leapy
    elif y % 100 == 0:
        if y % 400 == 0:
            return Month_in_leapy
        return Month_in_non_leapy
    return Month_in_leapy


def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    dsum = 0
    y = y1
    if y1 == y2:
        dinm = leap_year(y1)
        return sum(dinm[m1:m2]) + d2 - d1
    while y < y2:
        dinm = leap_year(y)
        dsum += sum(dinm)
        y += 1
        if y == y2:
            dinmy2 = leap_year(y2)
            dinmy1 = leap_year(y1)
            return dsum - sum(dinmy1[:m1]) - d1 + sum(dinmy2[:m2]) + d2 


# Test routine

def test():
    test_cases = [((2020, 1, 1, 2020, 2, 28), 58),
                  ((2020, 1, 1, 2020, 3, 1), 60),
                  ((2019, 6, 30, 2020, 6, 30), 366),
                  ((2018, 1, 1, 2019, 8, 8), 584),
                  ((1991, 4, 24, 2020, 6, 2), 10632)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


if __name__ == '__main__':
    data_1 = list(map(int, input('enter first date'
                                 '(year, month, day): ').split(',')))
    if data_1 == [0, 0, 0]:
        test()
        print(daysBetweenDates(2018, 1, 1, 2019, 8, 8))
    else:
        y1, m1, d1 = data_1
        data_2 = list(map(int, input('enter second date'
                                     '(year, month, day): ').split(',')))
        y2, m2, d2 = data_2
        print(daysBetweenDates(y1, m1, d1, y2, m2, d2))
