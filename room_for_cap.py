# The hotel has an infinite amount of rooms.
# One fine day, a finity number of tourists come to stay at
# the hotel.
# The tourists consist of:
# - Captain
# Group of families consisting of K members per group where k != 1

# The Captain was given a separate room, and the rest were given one room
# per group.

# The manager has an unordered list of randomly arranged room entries.
# The list consists of the room numbers for all of the tourists. The room numbers
# will appear K times per group except for the Captain's room.

# The manager needs help to find the Captain's room number.

k, rooms, single, multy = (input(),
                           input().split(),
                           set(),
                           set()
                           )

for room in rooms:
    single.add(room) if room not in single else multy.add(room)

print(single.difference(multy).pop())
