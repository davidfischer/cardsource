from . import BJCard

class BJHandError(Exception):
    pass

class BJHand(object):
    def __init__(self):
        self.cards = []
        self.doubled = False
        
    def __repr__(self):
        return str(self.cards)
    
    def __str__(self):
        return self.__repr__()
    
    def __len__(self):
        return len(self.cards)
        
    def add_card(self, card):
        """
        Adds a BJCard to a blackjack hand
        
        Raises a BJHandError if the card is not a BJCard
        """
        
        if card is not None and isinstance(card, BJCard):
            self.cards.append(card)
        else:
            raise BJHandError('Card of type %s is not allowed in a blackjack hand' %str(type(card)))

    def splittable(self):
        """
        Returns True if the hand can be split and False otherwise
        """
        
        return len(self.cards) == 2 and self.cards[0].equal_rank(self.cards[1])
    
    def split(self):
        """
        Splits the hand and returns the new BJHand
        
        splittable() should be called before this method as this method does no checking
        """
        
        if self.splittable():
            hand = BJHand()
            hand.add_card(self.cards.pop())
            return hand

        raise BJHandError('Unsplittable hand')
    
    def size(self):
        """
        Returns the number of cards in the hand
        """
        
        return len(self.cards)
    
    def reset(self):
        """
        Removes all cards from the hand
        """
        
        self.cards = []

    def is_soft(self):
        """
        Determines whether this is a soft hand where an ace counts as 11
        """

        aces = 0
        val = 0
        
        for card in self.cards:
            if card.rank == 'A':
                aces += 1
            val += card.value()
            
        while val > 21 and aces > 0:
            val -= 10
            aces -= 1
            
        if aces > 0:
            return True
        else:
            return False
        
    def value(self):
        """
        Gets the value of a given hand
        """
        
        aces = 0
        val = 0
        
        for card in self.cards:
            if card.rank == 'A':
                aces += 1
            val += card.value()
            
        while val > 21 and aces > 0:
            val -= 10
            aces -= 1
            
        return val
    
    def first_card(self):
        return self.cards[0]
    
    def second_card(self):
        return self.cards[1]
