import optparse
from cardsource.utils import game_input
from cardsource.blackjack import BJCard, BJDeck, BJHand, BJShoe, BJStrategy

class BJGame(object):
    """
    Controls the blackjack game
    """
    
    MAX_SPLITS = 4

    def __init__(self, num_decks=1, shuffle_percentage=0.25, hit_soft17=False, double_after_split=True, late_surrender=False):
        self.num_decks = num_decks
        self.shuffle_percentage = shuffle_percentage
        self.hit_soft17 = hit_soft17
        self.double_after_split = double_after_split
        self.late_surrender = late_surrender
        
        self.shoe = BJShoe(num_decks)
        self.player_hands = []
        self.dealer_hand = BJHand()
        
    def _start_hand(self):
        self.player_hands = [BJHand()]
        self.dealer_hand = BJHand()
        self.player_hands[0].add_card(self.shoe.pop())
        self.dealer_hand.add_card(self.shoe.pop())
        self.player_hands[0].add_card(self.shoe.pop())
        self.dealer_hand.add_card(self.shoe.pop())
        
    def _dealer_upcard(self):
        return self.dealer_hand.first_card()
    
    def _dealer_has_blackjack(self):
        if len(self.dealer_hand) == 2 and self.dealer_hand.value() == 21:
            return True
        
        return False
    
    def _player_has_blackjack(self):
        if len(self.player_hands[0]) == 2 and self.player_hands[0].value() == 21:
            return True
        
        return False
    
    def play(self, strategy, max_shoes=10):
        """
        Begin playing the game with the given strategy 
        """
        
        shoes = 0
        
        while True:
            # deal cards
            print '** Dealing **'
            self._start_hand()
            
            player_active_hands = 1
            
            print 'Your hand: %s' %self.player_hands[0]
            print 'Dealer upcard: %s' %self._dealer_upcard()
    
            # if dealer has a ten or ace the dealer checks for a natural
            # if dealer has an ace, the dealer offers insurance
            if self._dealer_upcard().value() >= 10:
                if self._dealer_upcard().value() == 11:
                    insurance = strategy.take_insurance()
                
                if self._dealer_has_blackjack():
                    print 'Dealer: I have blackjack'
                else:
                    print 'Dealer: I do not have blackjack'
            
            if self._dealer_has_blackjack():
                player_active_hands -= 1
                # player either pushes or loses
                if self._player_has_blackjack():
                    print 'Dealer: Push'
                else:
                    print '** Dealer collects **'
            elif self._player_has_blackjack():
                print '** Player has blackjack **'
                player_active_hands -= 1
            else:
                phand_index = 0
                while True:
                    # break if the player has no hands remaining
                    if phand_index >= len(self.player_hands):
                        break
                    
                    current_hand = self.player_hands[phand_index]
                    
                    if len(current_hand) == 1:
                        # the player split and needs another card
                        current_hand.add_card(self.shoe.pop())
                        
                    if len(self.player_hands) > 1 or len(current_hand) > 2:
                        print 'Your hand: %s' %current_hand
                    
                    if current_hand.value() > 21:
                        print '** Player busts **'
                        player_active_hands -= 1
                        phand_index += 1
                    elif current_hand.value() == 21:
                        print '** Player has made 21 **'
                        phand_index += 1
                    else:
                        # the player hits/stays/doubles/splits
                        can_double = len(current_hand) == 2 and (self.double_after_split or len(self.player_hands) == 1)
                        can_split = len(self.player_hands) <= self.MAX_SPLITS and current_hand.splittable()
                        decision = strategy.make_decision(can_double, can_split)
                        
                        if decision == strategy.HIT:
                            current_hand.add_card(self.shoe.pop())
                        elif decision == strategy.SPLIT:
                            new_hand = current_hand.split()
                            self.player_hands.append(new_hand)
                            player_active_hands += 1
                        elif decision == strategy.DOUBLE:
                            current_hand.add_card(self.shoe.pop())
                            phand_index += 1
                        else:
                            # player stands
                            phand_index += 1
                    
                # dealer hits/stays if player has not already busted on all hands
                if player_active_hands > 0:
                    while (self.dealer_hand.value() < 17) or \
                          (self.hit_soft17 and self.dealer_hand.value() == 17 and self.dealer_hand.is_soft()):
                        self.dealer_hand.add_card(self.shoe.pop())
                
                # the dealer pays/collects/pushes
                print 'Dealer hand: %s with value %d' %(self.dealer_hand, self.dealer_hand.value())
                for hand in self.player_hands:
                    print 'Your hand: %s with value %d' %(hand, hand.value())
            
            # check if the shuffle percentage is exceeded
            # and reshuffle the removed cards if it is
            if self.shuffle_percentage > float(self.shoe.remaining()) / float(self.shoe.original_size):
                print '** Shuffling **'
                shoes += 1
                self.shoe.reset()
                
            if shoes >= max_shoes:
                print 'Played %d shoes. Exiting...' %shoes
                break
            
def main():
    game = BJGame()
    strategy = BJStrategy()
    game.play(strategy)
