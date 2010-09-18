from cardsource.utils import game_input
from cardsource.blackjack import BJCard, BJDeck, BJHand, BJShoe

class BJStrategy(object):
    """
    A strategy defines how a player plays a Blackjack Game (BJGame)
    
    All other strategies inherit from this one. This strategy
    simply prompts the user for what to do.
    """
    
    HIT = 'h'
    STAND = 's'
    DOUBLE = 'd'
    SPLIT = 't'
    
    def take_insurance(self):
        """
        Return ``True`` if the player takes insurance and ``False`` otherwise
        """
        
        insurance = game_input('Dealer: Would you like to take insurance?', ['y', 'n'])
        if insurance == 'y':
            return True
        return False
    
    def make_decision(self, can_double=False, can_split=False):
        """
        Returns one of ``HIT``, ``STAND``, ``DOUBLE`` or ``SPLIT``
        """
        
        if can_double == True and can_split == True:
            decision = game_input('Hit/Stand/Double/spliT?', [self.HIT, self.STAND, self.DOUBLE, self.SPLIT])
        elif can_double == True:
            decision = game_input('Hit/Stand/Double?', [self.HIT, self.STAND, self.DOUBLE])
        elif can_split == True:
            decision = game_input('Hit/Stand/spliT?', [self.HIT, self.STAND, self.SPLIT])
        else:
            decision = game_input('Hit/Stand?', [self.HIT, self.STAND])
            
        return decision
        
        
        