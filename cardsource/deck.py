import random

from .cards import Card


class Deck(object):
    def __init__(self, numjokers=0):
        """
        Represents a playing card deck optionally with jokers
        """
        self._cards = [Card('{0}{1}'.format(rank, suit)) \
                for rank in Card.RANKS for suit in Card.SUITS if rank != 'X']

        for i in xrange(numjokers):
            self._cards.append(Card('X'))

    # Representation methods
    def __str__(self):
        return str(self._cards)

    def __repr__(self):
        # Subclasses can use this repr with their class name
        return '<{0}: {1}>'.format(self.__class__.__name__, self)

    # Iteration methods
    def __len__(self):
        """
        Returns the number of cards in the deck
        """
        return len(self._cards)

    # Collection methods
    def pop(self):
        return self._cards.pop()

    # Deck specific methods
    def shuffle(self):
        random.shuffle(self.cards)
