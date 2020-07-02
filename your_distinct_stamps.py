"""You have a huge collection of country stamps.
Count the total number of distinct country stamps in your collection.
"""
# The first line contains an integer N, the total number of country stamps.
# The next N lines contains the name of the country where the stamp is from.


def count_stamps(n):
    stamp_collection = set()
    for _ in range(n):
        stamp_collection.add(n)
    return len(stamp_collection)


if __name__ == '__main__':
    n = int(input())
    print(count_stamps(n))
