# The symmetric_difference() operator returns a set with all
# the elements that are in the set and the iterable but not both.

# ^ - operator is used in place of the symmetric_difference() tool,
# but it only operates on the set of elements in set.
# The set is immutable to the symmetric_difference() operation.

# Input format
# The first line: number of students who have subscribed to the English.
# The second line: space separated list of students who have subscribed
# to the English.
# The third line contains the number of students who have subscribed to
# French newspaper.
# The fourth line contains the space separated list of student who have
# subscribed to the French newspaper.

# Output format
# Total number of students who have subscriptions to the English or the French
# newspaper but not both.

n1 = input()
arr1 = set(map(int, input().split()))
n2 = input()
arr2 = set(map(int, input().split()))
print(f'The total number of students who have subscriptions only to '
      f'the English or French is {len(arr1 ^ arr2)}')