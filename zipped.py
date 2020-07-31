# The National University conducts an examination of N students
# in X subjects.
# Compute the average scores of each student.

# Input
# The first line contains N and X separated by a space.
# The next X lines contains the space separated marks obtained
# by students in a particular subject.

# Output
# Print averages of all students on separate lines.

x, n = map(int, input().split())

scores = []

for _ in range(n):
    scores.append(list(map(float, input().split())))

group_by_stud = zip(*scores)

for i in group_by_stud:
    print(sum(i)/len(i))
