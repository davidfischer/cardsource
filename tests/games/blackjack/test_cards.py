import unittest

from cardsource import CardSourceError
from cardsource.games.blackjack.cards import BJCard


class TestBJCard(unittest.TestCase):
    def testNoJoker(self):
        self.assertRaises(CardSourceError, BJCard, 'X')
        self.assertRaises(CardSourceError, BJCard, 'Xx')

    def testBasicBJSanity(self):
        self.assertEqual(str(BJCard('2H')), '2h')


if __name__ == '__main__':
    unittest.main()
