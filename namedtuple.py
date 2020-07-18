# Namedtuples are lightweight object types.
# They turn tuples into convenient containers for simple tasks.
# With namedtuples there are no need to use integer indices for
# accessing members of a tuple.

from collections import namedtuple
# point = namedtuple('Point', 'x, y')
# pt1 = point(1, 2)
# pt2 = point(3, 4)
# dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)
# print(dot_product)

# Car = namedtuple('Car', 'Price Mileage Colour Class')
# xyz = Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
# print(xyz)
# print(xyz.Class)

# The first line contains an integer N, the total number of students.
# The second line contains the names of the columns in any order.
# The next N lines contains the marks, IDs, name and class, under
# their respective column names.

# Output format:
# Average marks of the list corrected to 2 decimal places.

Students = namedtuple('Students', 'MARKS, CLASS, NAME, ID')

studs = Students([], [], [], [])

num = int(input())
columns = input().split()
for i, name in enumerate(columns):
    if name == 'MARKS':
        mark_i = i
        break

for _ in range(num):
    student_n = input().split()
    studs.MARKS.append(int(student_n[mark_i]))

print('{:.2f}'.format(sum(studs.MARKS)/num))
