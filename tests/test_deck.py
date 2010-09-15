import unittest

from cardsource.deck import Deck

class TestDeck(unittest.TestCase):
    def testCreate(self):
        deck = Deck()
        
    def testSize(self):
        deck = Deck()
        self.assertEqual(deck.size(), 54)