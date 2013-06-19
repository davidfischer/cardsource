from ...cards import Card
from ...errors import InvalidSuitError, InvalidRankError


class BJCard(Card):
    VALID_RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
    VALUE_MAPPING = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    def value(self):
        return self.VALUE_MAPPING[self.rank]

    def equal_rank(self, card):
        """
        Checks if 2 cards have the same rank (and are the same object type)
        """

        return type(self) == type(card) and self.VALUE_MAPPING[self.rank] == self.VALUE_MAPPING[card.rank]
