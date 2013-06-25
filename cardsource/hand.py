from .cards import Card


__all__ = ['Hand']


class Hand(object):
    """
    Represents a playing card game hand containing instances of
    :class:`cardsource.cards.Card`

    A ``Hand`` is an iterable Python object that supports being added
    to other hands as well as other common iterable operations. Hands
    are not directly comparable but this is common in subclasses of
    ``Hand``.
    """

    def __init__(self):
        self._cards = []

    # Representation methods
    def __repr__(self):
        return '<{0}: {1}>'.format(self.__class__.__name__, self._cards)

    def __str__(self):
        return str(sorted(self._cards))

    # Iteration methods
    def __len__(self):
        return len(self._cards)

    def __iter__(self):
        return iter(self._cards)

    def __getitem__(self, key):
        if type(key) is slice:
            return [self._cards[n] for n in
                    range(*key.indices(len(self)))]
        else:
            return self._cards[key]

    def __getslice__(self, i, j):
        h = Hand()

        if j >= len(self):
            j = len(self)

        for k in range(i, j):
            if k >= len(self):
                break
            h.append(self[k])

        return h

    # Arithmetic methods
    def __add__(self, otherhand):
        newhand = Hand()
        newhand.extend(self)
        newhand.extend(otherhand)
        return newhand

    def __iadd__(self, otherhand):
        return self + otherhand

    # Collection methods
    def append(self, card):
        """
        Adds a Card to the hand

        This class can be overridden in subclasses to ensure that the correct
        type of cards are added to the hand. Hands should not contain both
        instances of ``Card`` and subclasses of ``Card``.

        :param card: the card to add
        :type card: :class:`cardsource.cards.Card`
        """

        if not isinstance(card, Card):
            card = Card(card)
        self._cards.append(card)

    def clear(self):
        """
        Removes all cards from the hand
        """

        self._cards = []

    def extend(self, otherhand):
        """
        Extends hand by appending cards from another hand

        :param card: the hand to append to this hand
        :type card: :class:`cardsource.hand.Hand`
        """

        for card in otherhand:
            self.append(card)

    def count(self, card):
        """
        Returns the number of instances of the specified card

        :param card: the card to search for
        :type card: :class:`cardsource.cards.Card`
        :rtype: int
        :returns: the number of instances of the specified card
        """

        num = 0
        for c in self._cards:
            if c == card:
                num += 1

        return num
