# Given a string. Suppose a character occures consecutively x times
# in the string. Output these consecutive occurences of the character
# (x, c), where x is the number of times occured the 'c' character in
# the string.

# Input format:
# A single line of output consisting of the string.

# Output format:
# A single line of output consisting of the modified string.

from itertools import groupby

# itertools.groupby(iterable[, key])
# groupby returns an iterator that returns consecutive keys and groups from
# the iterable. The key is a function computing a key value for each element.
# if not specified or is None, key defaults to an identity function and returns
# the element unchanged.
# vehicles = [('Ford', 'Taurus'), ('Dodge', 'Durango'),
#             ('Chevrolet', 'Cobalt'), ('Ford', 'F150'),
#             ('Dodge', 'Charger'), ('Ford', 'GT')]

# sorted_vehicles = sorted(vehicles)

# for key, group in groupby(sorted_vehicles, lambda make: make[0]):
#     for make, model in group:
#         print('{model} is made by {make}'.format(model=model, make=make))

#     print ("**** END OF GROUP ***\n")

the_line = input()

print(*[(len(list(iter_string)), int(c))
        for c, iter_string in groupby(the_line)])
