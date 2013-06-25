from .errors import CardSourceError


__all__ = ['Card']


class Card(object):
    """
    Represents a single playing card

    A ``Card`` object supports a number of operations.

    When compared to another card, a card is greater than another card
    if the rank (A, 7, 2) is higher than the other card's rank. Suits are
    not considered. Jokers are higher than any card. For equivalence,
    both suit and rank must be equal for the objects to be equal.
    """

    RANKS = '23456789TJQKAX'
    SUITS = 'cdhs'

    def __init__(self, value):
        value = str(value)
        if len(value) > 2 or len(value) < 1:
            raise CardSourceError('Invalid card "{0}"'.format(value))

        # canonicalize data: rank - uppercase, suit - lowercase
        rank = str(value[0]).upper()
        if len(value) > 1 and rank != 'X':
            suit = str(value[1]).lower()
        else:
            suit = None

        # verify rank
        if rank in self.RANKS:
            self.rank = rank
        else:
            raise CardSourceError('Invalid rank "{0}"'.format(rank))

        # jokers do not have a suit. all others require a valid suit
        if (rank == 'X' and suit is None) or \
                (rank != 'X' and suit is not None and suit in self.SUITS):
            self.suit = suit
        else:
            raise CardSourceError('Invalid suit "{0}"'.format(suit))

    # Representation methods
    def __repr__(self):
        return '<{0}: {1}>'.format(self.__class__.__name__, self)

    def __str__(self):
        if self.suit is not None:
            return self.rank + self.suit
        else:
            return self.rank

    def __int__(self):
        return self.RANKS.find(self.rank)

    # Comparison methods
    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.rank == other.rank and self.suit == other.suit

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if type(self) != type(other):
            raise TypeError("Cards must be compared with other cards")
        return int(self) > int(other)

    def __lt__(self, other):
        if type(self) != type(other):
            raise TypeError("Cards must be compared with other cards")
        return int(self) < int(other)

    def __ge__(self, other):
        if type(self) != type(other):
            raise TypeError("Cards must be compared with other cards")
        return int(self) >= int(other)

    def __le__(self, other):
        if type(self) != type(other):
            raise TypeError("Cards must be compared with other cards")
        return int(self) <= int(other)
