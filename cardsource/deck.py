from cardsource.cards import Card

class Deck(object):
    def __init__(self):
        """
        Represents a 54 card deck with 2 Jokers
        """
        
        self.cards = [Card(rank, suit) for rank in Card.VALID_RANKS for suit in Card.VALID_SUITS if rank != 'X']
        self.cards.append(Card('X'))
        self.cards.append(Card('X'))
        
    def size(self):
        """
        Returns the number of cards in the deck
        """
        
        return len(self.cards)