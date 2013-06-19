import unittest

from cardsource.cards import Card
from cardsource.games.blackjack import BJCard
from cardsource.games.blackjack.hand import BJHand, BJHandError

class TestBJHand(unittest.TestCase):
    def setUp(self):
        self.hand1 = BJHand()
        self.hand1.add_card(BJCard('2', 'c'))
        self.hand1.add_card(BJCard('4', 'd'))
        self.hand1.add_card(BJCard('9', 'h'))
        
        self.hand2 = BJHand()
        self.hand2.add_card(BJCard('2', 's'))
        self.hand2.add_card(BJCard('J', 's'))
        self.hand2.add_card(BJCard('T', 's'))
        
        self.hand3 = BJHand()
        self.hand3.add_card(BJCard('A', 's'))
        self.hand3.add_card(BJCard('J', 'd'))
        self.hand3.add_card(BJCard('T', 's'))
        
        self.hand4 = BJHand()
        self.hand4.add_card(BJCard('2', 's'))
        self.hand4.add_card(BJCard('A', 'd'))
        self.hand4.add_card(BJCard('A', 's'))
        self.hand4.add_card(BJCard('A', 'h'))
        self.hand4.add_card(BJCard('A', 's'))
        self.hand4.add_card(BJCard('T', 's'))
        
        self.hand5 = BJHand()
        self.hand5.add_card(BJCard('2', 's'))
        self.hand5.add_card(BJCard('5', 'd'))
        self.hand5.add_card(BJCard('7', 's'))
        self.hand5.add_card(BJCard('6', 'h'))
        self.hand5.add_card(BJCard('2', 's'))
        self.hand5.add_card(BJCard('A', 's'))
        
        self.hand6 = BJHand()
        self.hand6.add_card(BJCard('2', 's'))
        self.hand6.add_card(BJCard('3', 'd'))
        self.hand6.add_card(BJCard('4', 's'))
        self.hand6.add_card(BJCard('3', 'h'))
        self.hand6.add_card(BJCard('2', 's'))
        self.hand6.add_card(BJCard('A', 's'))
        self.hand6.add_card(BJCard('A', 's'))
        self.hand6.add_card(BJCard('A', 's'))
        
        self.hand7 = BJHand()
        self.hand7.add_card(BJCard('9', 's'))
        self.hand7.add_card(BJCard('A', 's'))
        
        self.hand8 = BJHand()
        self.hand8.add_card(BJCard('A', 's'))
        self.hand8.add_card(BJCard('A', 's'))
        
        self.hand9 = BJHand()
        self.hand9.add_card(BJCard('T', 's'))
        self.hand9.add_card(BJCard('Q', 's'))
        
        self.hand10 = BJHand()
        self.hand10.add_card(BJCard('4', 's'))
        self.hand10.add_card(BJCard('3', 's'))
    
    def testCalculateValue(self):
        self.assertEqual(self.hand1.value(), 15)
        self.assertEqual(self.hand2.value(), 22)
        self.assertEqual(self.hand3.value(), 21)
        self.assertEqual(self.hand4.value(), 16)
        self.assertEqual(self.hand5.value(), 23)
        self.assertEqual(self.hand6.value(), 17)
        self.assertEqual(self.hand7.value(), 20)
        self.assertEqual(self.hand8.value(), 12)
        self.assertEqual(self.hand9.value(), 20)
        
    def testSplittable(self):
        self.assertTrue(self.hand8.splittable())
        self.assertTrue(self.hand9.splittable())
        self.assertFalse(self.hand7.splittable())
        self.assertFalse(self.hand10.splittable())
        
    def testSplit(self):
        self.assertTrue(self.hand9.size(), 2)
        split = self.hand9.split()
        self.assertTrue(self.hand9.size(), 1)
        self.assertTrue(split.size(), 1)
        self.assertEqual(split.value(), self.hand9.value())
        
    def testSize(self):
        self.assertEqual(self.hand10.size(), 2)
        self.assertEqual(self.hand9.size(), 2)
        self.assertEqual(self.hand6.size(), 8)
        self.hand6.reset()
        self.assertEqual(self.hand6.size(), 0)

    def testIsSoft(self):
        self.assertFalse(self.hand1.is_soft())
        self.assertFalse(self.hand2.is_soft())
        self.assertFalse(self.hand3.is_soft())
        self.assertFalse(self.hand4.is_soft())
        self.assertFalse(self.hand5.is_soft())
        self.assertFalse(self.hand6.is_soft())
        self.assertTrue(self.hand7.is_soft())
        self.assertTrue(self.hand8.is_soft())
        self.assertFalse(self.hand9.is_soft())
        self.assertFalse(self.hand10.is_soft())

    def testInvalid(self):
        hand = BJHand()
        try:
            hand.add_card(Card('J', 'c'))
            self.fail('Should not be able to add a Card to a BJHand, must add BJCard')
        except BJHandError:
            pass
