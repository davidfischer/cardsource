from collections import deque
import random

from .cards import Card


__all__ = ['Deck']


class Deck(object):
    """
    Represents a playing card deck optionally with jokers. Each member is
    an instance of :class:`cardsource.cards.Card`.

    A ``Deck`` is an iterable object that supports a number of standard
    Python operations like indexing, iteration and slicing.
    """

    def __init__(self, numjokers=0):
        self._cards = deque([Card('{0}{1}'.format(rank, suit))
                             for rank in Card.RANKS for suit in Card.SUITS
                             if rank != 'X'])

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
        if type(key) is slice:
            return deque([self._cards[n] for n in
                         range(*key.indices(len(self)))])
        else:
            return self._cards[key]

    def __getslice__(self, i, j):
        d = Deck()
        d.clear()

        if j >= len(self):
            j = len(self)

        for k in range(i, j):
            if k >= len(self):
                break
            d._cards.append(self[k])

        return d

    # Collection methods
    def pop(self):
        """
        Removes and returns the top card in the deck

        :raises: IndexError if the deck is empty
        :returns: the top card in the deck
        :rtype: :class:`cardsource.cards.Card`
        """
        return self._cards.pop()

    def append(self, card):
        """
        Put a card on the top of the deck

        :param card: the card to add
        :type card: :class:`cardsource.cards.Card`
        """
        if not isinstance(card, Card):
            card = Card(card)
        self._cards.append(card)

    def appendleft(self, card):
        """
        Put a card on the bottom of the deck

        :param card: the card to add
        :type card: :class:`cardsource.cards.Card`
        """
        if not isinstance(card, Card):
            card = Card(card)
        self._cards.appendleft(card)

    def clear(self):
        """
        Remove all cards in the deck
        """
        self._cards = deque()

    # Deck specific methods
    def shuffle(self):
        """
        Shuffle the deck

        Uses ``random.shuffle``
        """
        random.shuffle(self._cards)
