from .cards import Card


class Hand(object):
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

    # Collection methods
    def append(self, card):
        """
        Adds a Card to the hand
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

    def extend(self, iterable):
        """
        Extends hand by appending cards from the iterable
        """

        for card in iterable:
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
