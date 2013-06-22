import unittest

from cardsource import Hand, Card, CardSourceError


class TestHand(unittest.TestCase):
    def setUp(self):
        self.hand1 = Hand()
        self.hand2 = Hand()

        self.hand1.append('2h')
        self.hand1.append('Ah')
        self.hand1.append('6s')
        self.hand1.append('6s')

        self.hand2.append('4s')
        self.hand2.append('4c')
        self.hand2.append('X')

    def testSize(self):
        self.assertEqual(len(Hand()), 0)
        self.assertEqual(len(self.hand1), 4)
        self.assertEqual(len(self.hand2), 3)

    def testClear(self):
        self.hand1.clear()
        self.assertEqual(len(self.hand1), 0)

    def testCount(self):
        self.assertEqual(self.hand1.count(Card('6s')), 2)
        self.assertEqual(self.hand1.count(Card('6c')), 0)
        self.assertEqual(self.hand1.count(Card('AH')), 1)

    def testExtend(self):
        self.hand1.extend(self.hand2)
        self.assertEqual(len(self.hand2), 3)
        self.assertEqual(len(self.hand1), 7)

    def testAdd(self):
        newhand = self.hand1 + self.hand2
        self.assertEqual(len(self.hand1), 4)
        self.assertEqual(len(self.hand2), 3)
        self.assertEqual(len(newhand), 7)
