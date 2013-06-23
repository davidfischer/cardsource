import random
import sys

from .cards import Card


__all__ = ['Deck']


class Deck(object):
    """
    Represents a playing card deck optionally with jokers
    """

    def __init__(self, numjokers=0):
        self._cards = [Card('{0}{1}'.format(rank, suit))
                       for rank in Card.RANKS for suit in Card.SUITS
                       if rank != 'X']

        for i in range(numjokers):
            self._cards.append(Card('X'))

    # Representation methods
    def __str__(self):
        return "{0} cards left".format(len(self._cards))

    def __repr__(self):
        # Subclasses can use this repr with their class name
        return '<{0}: {1}>'.format(self.__class__.__name__, self)

    # Iteration methods
    def __len__(self):
        """
        Returns the number of cards in the deck
        """
        return len(self._cards)

    def __iter__(self):
        """
        Returns an iterator of cards remaining in the deck
        """
        return iter(self._cards)

    def __getitem__(self, key):
        return self._cards[key]

    def __getslice__(self, i, j):
        d = Deck()
        d.clear()

        if j >= sys.maxint:
            j = len(self)

        for k in range(i, j):
            if k >= len(self):
                break
            d._cards.append(self[k])

        return d

    # Collection methods
    def pop(self):
        return self._cards.pop()

    def clear(self):
        self._cards = []

    # Deck specific methods
    def shuffle(self):
        random.shuffle(self._cards)
