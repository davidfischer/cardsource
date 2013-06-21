from ...deck import Deck
from . import BJCard


class BJDeck(Deck):
    def __init__(self):
        """
        Represents a 52 card standard blackjack deck
        """

        self._cards = [BJCard('{0}{1}'.format(rank, suit))
                       for rank in BJCard.RANKS for suit in BJCard.SUITS]
