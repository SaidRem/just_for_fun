# Dataclasses are basically flexible interfaces. When you implement the
# interface, you get the added benefit of having an object with the
# coveted dot notation.
from dataclasses import dataclass


@dataclass
class DataClassCard:
    rank: str
    suit: str


queen_of_hearts = DataClassCard('Q', 'Hearts')
print(queen_of_hearts.rank)
print(queen_of_hearts.suit)


# You can also use dictionary decomposition when instantiating
# dataclass object.
data = {
    'rank': 'J',
    'suit': 'Spades'
    }
jack_of_spades = DataClassCard(**data)
print(jack_of_spades.rank)