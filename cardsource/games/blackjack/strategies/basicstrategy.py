from .. import BJStrategy

class OneDeckFlatBetStrategy(BJStrategy):
    """
    Implements a basic flat bet (10/hand) strategy that is optimal for:
    
    - 1 deck
    - DAS allowed
    - no late surrender
    - hit soft 17
    
    Basic strategy from http://www.blackjackinfo.com/
    """
    
    def take_insurance(self):
        return False
    
    def bet_amount(self, remaining_bankroll):
        return self.DEFAULT_BET_AMOUNT
    
    def make_decision(self, dealer_upcard, player_hand, can_double=False, can_split=False):
        is_soft = player_hand.is_soft()
        hand_value = player_hand.value()
        upcard_value = dealer_upcard.value()
        splittable = player_hand.splittable() and can_split
        
        if hand_value <= 8 and not splittable:
            return self.HIT
        elif hand_value == 9:
            if can_double and upcard_value in (5, 6):
                return self.DOUBLE
            else:
                return self.HIT
        elif hand_value == 10 and not splittable:
            if can_double and upcard_value < 10:
                return self.DOUBLE
            else:
                return self.HIT
        elif hand_value == 11:
            if can_double:
                return self.DOUBLE
            else:
                return self.HIT
        elif hand_value == 12 and not is_soft and not splittable:
            if upcard_value not in (4, 5, 6):
                return self.HIT
            else:
                return self.STAND
        elif hand_value in (13, 14, 15, 16) and not is_soft and not splittable:
            if upcard_value < 7:
                return self.STAND
            else:
                return self.HIT
        elif hand_value >= 17 and not is_soft and not splittable:
            return self.STAND
        elif hand_value in (13, 14, 15, 16) and is_soft and not splittable:
            if upcard_value in (4, 5, 6) and can_double:
                return self.DOUBLE
            else:
                return self.HIT
        elif hand_value == 17 and is_soft:
            if upcard_value < 7 and can_double:
                return self.DOUBLE
            else:
                return self.HIT
        elif hand_value == 18 and is_soft and not splittable:
            if upcard_value in (3, 4, 5, 6) and can_double:
                return self.DOUBLE
            elif upcard_value < 9:
                return self.HIT
            else:
                return self.STAND
        elif hand_value == 19 and is_soft:
            if upcard_value == 6 and can_double:
                return self.DOUBLE
            else:
                return self.STAND
        elif hand_value >= 20 and is_soft and not splittable:
            return self.STAND
        elif splittable:
            if hand_value == 4:
                if upcard_value < 8:
                    return self.SPLIT
                else:
                    return self.HIT
            elif hand_value == 6:
                if upcard_value < 9:
                    return self.SPLIT
                else:
                    return self.HIT
            elif hand_value == 8:
                if upcard_value in (4, 5, 6):
                    return self.SPLIT
                else:
                    return self.HIT
            elif hand_value == 10:
                if upcard_value < 10:
                    return self.DOUBLE
                else:
                    return self.HIT
            elif hand_value == 12:
                # could be AA or 66
                if player_hand.first_card().value() == 11:
                    # AA
                    return self.SPLIT
                else:
                    # 66
                    if upcard_value < 8:
                        return self.SPLIT
                    else:
                        return self.HIT
            elif hand_value == 14:
                if upcard_value < 9:
                    return self.SPLIT
                elif upcard_value == 10:
                    return self.STAND
                else:
                    return self.HIT
            elif hand_value == 16:
                return self.SPLIT
            elif hand_value == 18:
                if upcard_value in (7, 10):
                    return self.STAND
                else:
                    return self.SPLIT
            elif hand_value == 20:
                return self.STAND
            
        raise RuntimeError('Rule not implemented for hand %s with upcard %s' %(player_hand, dealer_upcard))
        
