import unittest

from cardsource.games.blackjack import BJDeck


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = BJDeck()

    def testSize(self):
        self.assertEqual(len(self.deck), 52)
