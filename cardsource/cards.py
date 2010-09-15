class InvalidRankError(Exception):
    pass

class InvalidSuitError(Exception):
    pass

class Card(object):
    VALID_RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A', 'X')
    VALID_SUITS = ('c', 'd', 'h', 's')

    def __init__(self, rank, suit=None):
        """
        A playing card object

        **Parameters**

        * `rank`
         One of (2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A, X) where X is a joker
        * `suite`
         One of (c, d, h, s) indicating clubs, diamonds, etc. ``None`` for a joker

        """

        # canonicalize data
        rank = str(rank).upper()
        if suit is not None:
            suit = str(suit).lower()
        
        # verify rank
        if rank in self.VALID_RANKS:
            self.rank = rank
        else:
            raise InvalidRankError('Rank %s is not one of %s' %(rank, str(self.VALID_RANKS)))

        # verify suit
        # jokers do not have a suit. all others require a suit
        if self.rank != 'X':
            if suit is not None and suit in self.VALID_SUITS:
                self.suit = suit
            else:
                raise InvalidSuitError('Suit %s is not one of %s' %(suit, str(self.VALID_SUITS)))
        else:
            self.suit = None

    def __repr__(self):
        if self.suit is not None:
            return self.rank + self.suit
        else:
            return self.rank

    def __str__(self):
        return self.__repr__()
    
    def equal_rank(self, card):
        """
        Checks if 2 cards have the same rank (and are the same object type)
        """
        
        return type(self) == type(card) and self.rank == card.rank
    
    def suited(self, card):
        """
        Checks if 2 cards have the same suit (and are the same object type)
        """
        
        return type(self) == type(card) and self.suit == card.suit