from ... import Card


class BJCard(Card):
    RANKS = Card.RANKS.replace('X', '')   # no jokers in blackjack
    VALUES = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11
    }

    def __int__(self):
        return self.VALUES[self.rank]

    def __eq__(self, other):
        """
        Checks if 2 cards have the same rank
        """

        if not isinstance(other, BJCard):
            other = BJCard(other)

        return self.VALUES[self.rank] == self.VALUES[other.rank]
