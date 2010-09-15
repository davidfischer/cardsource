import optparse
import time
from cardsource.blackjack import BJCard, BJDeck, BJHand, BJShoe

class BJGame(object):
    """
    Controls the blackjack game
    """

    def __init__(self, num_decks=1, shuffle_percentage=0.25, hit_soft17=False, double_after_split=True, late_surrender=False):
        self.num_decks = num_decks
        self.shuffle_percentage = shuffle_percentage
        self.hit_soft17 = hit_soft17
        self.double_after_split = double_after_split
        self.late_surrender = late_surrender
        
        self.shoe = BJShoe(num_decks)
        self.player_hands = []
        self.dealer_hand = BJHand()
        
    def start_hand(self):
        self.player_hands = [BJHand()]
        self.dealer_hand = BJHand()
        self.player_hands[0].add_card(self.shoe.pop())
        self.dealer_hand.add_card(self.shoe.pop())
        self.player_hands[0].add_card(self.shoe.pop())
        self.dealer_hand.add_card(self.shoe.pop())
        
    def dealer_upcard(self):
        return self.dealer_hand.first_card()
    
    def dealer_has_blackjack(self):
        if len(self.dealer_hand) == 2 and self.dealer_hand.value() == 21:
            return True
        
        return False
    
    def player_has_blackjack(self):
        if len(self.player_hands[0]) == 2 and self.player_hands[0].value() == 21:
            return True
        
        return False

def main():
    """
    A simple interactive terminal based blackjack game
    """
    
    game = BJGame()
    
    while True:
        # deal cards
        print '**Dealing**'
        game.start_hand()
        
        print 'Dealer upcard: %s' %game.dealer_upcard()
        print 'Your hand: %s' %game.player_hands

        # if dealer has a ten or ace the dealer checks for a natural
        # if dealer has an ace, the dealer offers insurance
        if game.dealer_upcard().value() >= 10:
            if game.dealer_upcard().value() == 11:
                insurance = raw_input('Dealer: Would you like to take insurance? [y/n]')
                # TODO: implement insurance
            
            if game.dealer_has_blackjack():
                print 'Dealer: I have blackjack'
            else:
                print 'Dealer: I do not have blackjack'
        
        if game.dealer_has_blackjack():
            # player either pushes or loses
            if game.player_has_blackjack():
                print 'Dealer: Push'
            else:
                print '** Dealer collects **'
        else:
            pass
            # the player hits/stays/doubles/splits/etc
            # the dealer hits/stays
            # the dealer pays/collects/pushes
        
        # check if the shuffle percentage is exceeded
        # and reshuffle the removed cards if it is
        if game.shuffle_percentage > float(game.shoe.remaining()) / float(game.shoe.original_size):
            print '**Shuffling**'
            time.sleep(1)
            game.shoe.reset()
