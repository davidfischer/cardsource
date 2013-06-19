from .utils import game_input
from . import BJCard, BJDeck, BJHand, BJShoe

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
    
    DEFAULT_BET_AMOUNT = 10
    
    def __init__(self):
        self.last_bet = self.DEFAULT_BET_AMOUNT
    
    def show_card(self, card):
        """
        Notifies the strategy that a certain card is visible. This method can be used
        to count cards or keep an insurance count. By default, this method does nothing
        """
        
        pass
    
    def bet_amount(self, remaining_bankroll):
        """
        The amount the player will bet on this hand. Rounds to 2 decimal places.
        """
        
        bet = 0.0
        
        while bet <= 0:
            bet = game_input('How much would you like to wager on this hand? [%0.2f]' %self.last_bet)
            if len(bet) == 0:
                bet = self.last_bet
            
            try:
                bet = float(bet)
            except ValueError:
                bet = 0
            
        bet = round(bet, 2)
        self.last_bet = bet
        return bet
    
    def take_insurance(self):
        """
        Return ``True`` if the player takes insurance and ``False`` otherwise
        """
        
        insurance = game_input('Dealer: Would you like to take insurance?', ['y', 'n'])
        if insurance == 'y':
            return True
        return False
    
    def make_decision(self, dealer_upcard, player_hand, can_double=False, can_split=False):
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
        
        
        
