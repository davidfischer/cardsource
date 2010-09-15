from cardsource.deck import Deck
from cardsource.blackjack import BJCard

class BJDeck(Deck):
    def __init__(self):
        """
        Represents a 52 card standard blackjack deck
        """
        
        self.cards = [BJCard(rank, suit) for rank in BJCard.VALID_RANKS for suit in BJCard.VALID_SUITS]