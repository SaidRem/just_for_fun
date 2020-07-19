# Manager of a supermarket have a list of N items together
# with their prices that consumers bought on a particular day.
# Print each item_name and net_price in order of its first occurrence.

# Input format:
# The first line contains the number of items, N.
# The next N lines contains the item's name and price, separated
# by a space.

# Output format
# Print the item_name and net_price in order of its first
# occurrence.

from collections import OrderedDict

# ord_dict = OrderedDict()

# num = int(input())

# for _ in range(num):
#     item, price = input().split()
#     price = int(price)
#     if ord_dict.get(item):
#         ord_dict[item] += price
#     else:
#         ord_dict[item] = price

# for item in ord_dict:
#     print(item, ord_dict[item], sep=' ')


ord_dict = OrderedDict()

num = int(input())

for _ in range(num):
    temp = input().split()
    if len(temp) == 3:
        item1, item2, price = temp
        price = int(price)
        if ord_dict.get(item1+' '+item2):
            ord_dict[item1+' '+item2] += price
        else:
            ord_dict[item1+' '+item2] = price
    else:
        item, price = temp
        price = int(price)
        if ord_dict.get(item):
            ord_dict[item] += price
        else:
            ord_dict[item] = price

for item in ord_dict:
    print(item, ord_dict[item], sep=' ')
