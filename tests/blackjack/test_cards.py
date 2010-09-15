import unittest

from cardsource.cards import InvalidRankError, InvalidSuitError
from cardsource.blackjack.cards import BJCard

class TestBJCard(unittest.TestCase):
    def testNoJoker(self):
        try:
            c = BJCard(rank='x')
            self.fail('Jokers are not valid in blackjack')
        except InvalidRankError:
            pass
        
    def testBasicBJSanity(self):
        c = BJCard(rank=2, suit='h')
        self.assertEqual(str(c), '2h')
        c = BJCard(rank=2, suit='H')
        self.assertEqual(str(c), '2h')
        
    def testBasicBJInvalid(self):
        try:
            c = BJCard(rank='j', suit='t')
            self.fail('"t" should fail since it is not a valid suit')
        except InvalidSuitError:
            pass
        
if __name__ == '__main__':
    unittest.main()
