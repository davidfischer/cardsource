from optparse import OptionParser
from cardsource.utils import game_input
from cardsource.blackjack import BJCard, BJDeck, BJHand, BJShoe, BJStrategy

class BJGame(object):
    """
    Controls the blackjack game
    """
    
    MAX_SPLITS = 4

    def __init__(self, num_decks=1, shuffle_percentage=0.35, hit_soft17=False, double_after_split=True, late_surrender=False):
        self.num_decks = num_decks
        self.shuffle_percentage = shuffle_percentage
        self.hit_soft17 = hit_soft17
        self.double_after_split = double_after_split
        self.late_surrender = late_surrender
        
        self.shoe = BJShoe(num_decks)
        self.player_hands = []
        self.dealer_hand = BJHand()
        
        self.hands_played = 0
        self.shoes_played = 0
        self.starting_bankroll = 0.0
        self.bankroll_high = 0.0
        self.bankroll_low = 0.0
        self.current_bankroll = 0.0
        
    def _start_hand(self):
        self.player_hands = [BJHand()]
        self.dealer_hand = BJHand()
        self.player_hands[0].add_card(self.shoe.pop())
        self.dealer_hand.add_card(self.shoe.pop())
        self.player_hands[0].add_card(self.shoe.pop())
        self.dealer_hand.add_card(self.shoe.pop())
        self.hands_played += 1
    
    def _dealer_has_blackjack(self):
        if len(self.dealer_hand) == 2 and self.dealer_hand.value() == 21:
            return True
        
        return False
    
    def _player_has_blackjack(self):
        if len(self.player_hands[0]) == 2 and self.player_hands[0].value() == 21:
            return True
        
        return False
    
    def summary(self):
        """
        Returns a summary of the play
        """
        
        data = {}
        data['hands_played'] = self.hands_played
        data['shoes_played'] = self.shoes_played
        data['starting_bankroll'] = self.starting_bankroll
        data['bankroll_low'] = self.bankroll_low
        data['bankroll_high'] = self.bankroll_high
        data['ending_bankroll'] = self.current_bankroll
        
        return data
    
    def play(self, strategy, max_shoes=1, starting_bankroll=10000):
        """
        Begin playing the game with the given strategy 
        """
        
        # reset bankroll numbers
        self.starting_bankroll = float(starting_bankroll)
        self.bankroll_high = float(starting_bankroll)
        self.bankroll_low = float(starting_bankroll)
        self.current_bankroll = float(starting_bankroll)
        
        while True:
            # player chooses bet amount
            print 'Player has $%0.2f remaining' %self.current_bankroll
            if self.current_bankroll <= 0:
                break
            
            wager = strategy.bet_amount(self.current_bankroll)
            
            if wager > self.current_bankroll:
                wager = self.current_bankroll
                
            self.current_bankroll -= wager
            
            # deal cards
            print '** Dealing **'
            self._start_hand()
            
            player_active_hands = 1
            
            dealer_upcard = self.dealer_hand.first_card()
            dealer_downcard = self.dealer_hand.second_card()
            
            print 'Your hand: %s' %self.player_hands[0]
            print 'Dealer upcard: %s' %dealer_upcard
            
            # show the cards to the strategy object
            strategy.show_card(dealer_upcard)
            for hand in self.player_hands:
                for card in hand.cards:
                    strategy.show_card(card)
    
            # if dealer has a ten or ace the dealer checks for a natural
            # if dealer has an ace, the dealer offers insurance
            if dealer_upcard.value() >= 10:
                if dealer_upcard.value() == 11:
                    ## TODO: player cannot take insurance if they can't pay for it
                    insurance = strategy.take_insurance()
                    if insurance:
                        self.current_bankroll -= wager / 2
                
                if self._dealer_has_blackjack():
                    print 'Dealer: I have blackjack'
                    if insurance:
                        print 'Dealer: Your insurance bet paid 2:1'
                        self.current_bankroll += (wager / 2) * 3
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
                self.current_bankroll += wager * 2.5       # blackjack pays 3:2
            else:
                phand_index = 0
                while True:
                    # break if the player has no hands remaining
                    if phand_index >= len(self.player_hands):
                        break
                    
                    current_hand = self.player_hands[phand_index]
                    
                    if len(current_hand) == 1:
                        # the player split and needs another card
                        card = self.shoe.pop()
                        current_hand.add_card(card)
                        strategy.show_card(card)
                        
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
                        can_double = len(current_hand) == 2 and (self.double_after_split or len(self.player_hands) == 1) and (self.current_bankroll >= wager)
                        can_split = (len(self.player_hands) <= self.MAX_SPLITS and current_hand.splittable()) and (self.current_bankroll >= wager)
                        decision = strategy.make_decision(dealer_upcard, current_hand, can_double, can_split)
                        
                        ## TODO: implement surrender
                        if decision == strategy.HIT:
                            card = self.shoe.pop()
                            current_hand.add_card(card)
                            strategy.show_card(card)
                        elif decision == strategy.SPLIT:
                            new_hand = current_hand.split()
                            self.player_hands.append(new_hand)
                            player_active_hands += 1
                            self.current_bankroll -= wager
                            ## TODO: implement splitting aces properly
                        elif decision == strategy.DOUBLE:
                            card = self.shoe.pop()
                            current_hand.add_card(card)
                            current_hand.doubled = True
                            strategy.show_card(card)
                            phand_index += 1
                            self.current_bankroll -= wager
                        else:
                            # player stands
                            phand_index += 1
                    
                # dealer hits/stays if player has not already busted on all hands
                if player_active_hands > 0:
                    while (self.dealer_hand.value() < 17) or \
                          (self.hit_soft17 and self.dealer_hand.value() == 17 and self.dealer_hand.is_soft()):
                        card = self.shoe.pop()
                        self.dealer_hand.add_card(card)
                        strategy.show_card(card)
                
                # the dealer pays/collects/pushes
                print 'Dealer hand: %s with value %d' %(self.dealer_hand, self.dealer_hand.value())
                for hand in self.player_hands:
                    print 'Your hand: %s with value %d' %(hand, hand.value())
                    if (hand.value() > self.dealer_hand.value() and hand.value() <= 21) or (hand.value() <= 21 and self.dealer_hand.value() > 21):
                        # player wins
                        print '** You win **'
                        if hand.doubled == True:
                            self.current_bankroll += wager * 2
                        self.current_bankroll += wager * 2
                    elif hand.value() == self.dealer_hand.value() and hand.value() <= 21:
                        # push
                        print '** Push **'
                        if hand.doubled == True:
                            self.current_bankroll += wager
                        self.current_bankroll += wager
            
            # keep track of the high point and low point of the player's bankroll
            if self.current_bankroll < self.bankroll_low:
                self.bankroll_low = self.current_bankroll
            if self.current_bankroll > self.bankroll_high:
                self.bankroll_high = self.current_bankroll
                        
            # check if the shuffle percentage is exceeded
            # and reshuffle the removed cards if it is
            if self.shuffle_percentage > float(self.shoe.remaining()) / float(self.shoe.original_size):
                print '** Shuffling **'
                self.shoes_played += 1
                self.shoe.reset()
                
            if self.shoes_played >= max_shoes:
                print 'Played %d shoes. Exiting...' %self.shoes_played
                break
            
def main():
    parser = OptionParser()
    parser.add_option("-b", "--bankroll", type="int", dest="bankroll", default=10000, help='Starting bankroll [10,000]')
    parser.add_option("-s", "--shoes", type="int", dest="shoes", default=1000000, help='Number of shoes to play before exiting [1,000,000]')
    parser.add_option("-d", "--decks", type="int", dest="decks", default=1, help='Number of decks in a shoe [1]')
    parser.add_option("-t", "--hitsoft17", action="store_true", dest="hitsoft17", default=False, help='Whether the dealer hits soft 17 [False]')
    parser.add_option("-a", "--no-das", action="store_false", dest="no_das", default=True, help='Double after split is allowed by default [False]')
    parser.add_option("-l", "--late-surrender", action="store_true", dest="late_surrender", default=False, help='Whether late surrender is allowed [False]')
    parser.add_option("-p", "--shuffle", type="float", dest="shuffle_percentage", default=0.35, help='Shuffle when this percentage of the shoe left [0.35]')
    
    (options, args) = parser.parse_args()
    if options.shuffle_percentage < 0.2 or options.shuffle_percentage > 1.0:
        print 'Defaulting shuffle percentage to %0.2f' %(0.35)
        options.shuffle_percentage = 0.35
    
    game = BJGame(num_decks=options.decks, shuffle_percentage=options.shuffle_percentage, \
                  hit_soft17=options.hitsoft17, double_after_split=(not options.no_das), \
                  late_surrender=options.late_surrender)
    strategy = BJStrategy()
    
    try:
        game.play(strategy, starting_bankroll=options.bankroll, max_shoes=options.shoes)
    except KeyboardInterrupt:
        pass
    
    print
    print
    print 'Summary'
    summary = game.summary()
    for key in summary.keys():
        print '%s: %s' %(key, str(summary[key]))
    
if __name__ == '__main__':
    main()
