from ... import Hand, CardSourceError

from .cards import BJCard


class BJHand(Hand):
    def __init__(self):
        self._cards = []
        self.doubled = False

    # Representation methods
    def __int__(self):
        """
        Gets the value of a given hand
        """

        aces = 0
        val = 0

        for card in self._cards:
            if card.rank == 'A':
                aces += 1
            val += int(card)

        while val > 21 and aces > 0:
            val -= 10
            aces -= 1

        return val

    # Collection methods
    def append(self, card):
        """
        Adds a BJCard to a blackjack hand
        """

        if not isinstance(card, BJCard):
            card = BJCard(card)
        self._cards.append(card)

    def splittable(self):
        """
        Returns True if the hand can be split and False otherwise
        """

        return len(self._cards) == 2 and self._cards[0] == self._cards[1]

    def split(self):
        """
        Splits the hand and returns the new BJHand

        splittable() should be called before this method as this method does no checking
        """

        if self.splittable():
            hand = BJHand()
            hand.append(self._cards.pop())
            return hand

        raise CardSourceError('Unsplittable hand')

    def is_soft(self):
        """
        Determines whether this is a soft hand where an ace counts as 11
        """

        aces = 0
        val = 0

        for card in self._cards:
            if card.rank == 'A':
                aces += 1
            val += int(card)

        while val > 21 and aces > 0:
            val -= 10
            aces -= 1

        if aces > 0:
            return True
        else:
            return False

    def first_card(self):
        return self._cards[0]

    def second_card(self):
        return self._cards[1]
