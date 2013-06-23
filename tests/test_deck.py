import unittest

from cardsource import Deck


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.deck_with_jokers = Deck(numjokers=2)

    def testSize(self):
        self.assertEqual(len(self.deck), 52)
        self.assertEqual(len(self.deck_with_jokers), 54)

    def testSlice(self):
        self.assertEqual(len(self.deck[:10]), 10)
        self.assertEqual(len(self.deck), 52)

        self.assertEqual(len(self.deck[10:20]), 10)
        self.assertEqual(len(self.deck[10:]), 42)
        self.assertEqual(len(self.deck[:]), 52)
        self.assertEqual(len(self.deck[100:]), 0)
        self.assertEqual(len(self.deck[:1000]), 52)


if __name__ == '__main__':
    unittest.main()
