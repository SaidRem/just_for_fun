# Mike is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay x amount of
# money only if they get the shoe of their desire size.

# Compute how  much money Mike earned.

# Input format
# The first line contains X, the number of shoes.
# The second line contains the space separated list of all the shoe sizes
# in the shop.
# The third line contains the space separated values of the shoe size desired by the
# customer and x, the price of the shoe.

# Output: amount of money earned by Mike

import collections

number_shoes = int(input())
shoe_sizes = collections.Counter(map(int, input().split()))

num_customers = int(input())

total_cash = 0

for i in range(num_customers):
    size, price = map(int, input().split())
    if shoe_sizes.get(size): 
        total_cash += price
        shoe_sizes[size] -= 1

print(total_cash)