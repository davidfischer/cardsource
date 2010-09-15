import unittest

from cardsource.blackjack.deck import BJDeck

class TestDeck(unittest.TestCase):
    def testCreate(self):
        deck = BJDeck()
        
    def testSize(self):
        deck = BJDeck()
        self.assertEqual(deck.size(), 52)