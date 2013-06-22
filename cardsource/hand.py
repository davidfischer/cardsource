from .cards import Card


__all__ = ['Hand']


class Hand(object):
    """
    A playing card game hand.
    """

    def __init__(self):
        self._cards = []

    # Representation methods
    def __repr__(self):
        return '<{0}: {1}>'.format(self.__class__.__name__, self.self)

    def __str__(self):
        return str(sorted(self._cards))

    # Iteration methods
    def __len__(self):
        return len(self._cards)

    def __iter__(self):
        return iter(self._cards)

    # Arithmetic methods
    def __add__(self, otherhand):
        newhand = Hand()
        newhand.extend(self)
        newhand.extend(otherhand)
        return newhand

    # Collection methods
    def append(self, card):
        """
        Adds a Card to the hand

        This class can be overridden in subclasses to ensure that the correct
        type of cards are added to the hand. Hands should not contain both
        instances of ``Card`` and subclasses of ``Card``.
        """

        if not isinstance(card, Card):
            card = Card(card)
        self._cards.append(card)

    def clear(self):
        """
        Removes all cards from the hand and returns the list of cards
        """

        result = self._cards
        self._cards = []
        return result

    def extend(self, otherhand):
        """
        Extends hand by appending cards from another hand
        """

        for card in otherhand:
            self.append(card)

    def count(self, card):
        """
        Returns the number of instances of the exact specified card
        """

        num = 0
        for c in self._cards:
            if c == card:
                num += 1

        return num
