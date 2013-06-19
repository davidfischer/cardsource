from .cards import Card


class Deck(object):
    def __init__(self, withjokers=True):
        """
        Represents a playing card deck optionally with jokers
        """
        self.cards = [Card(rank, suit) for rank in Card.VALID_RANKS for suit in Card.VALID_SUITS if rank != 'X']
        if withjokers:
            self.cards.append(Card('X'))
            self.cards.append(Card('X'))

    def size(self):
        """
        Returns the number of cards in the deck
        """
        return len(self.cards)
