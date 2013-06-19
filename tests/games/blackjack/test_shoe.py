import unittest

from cardsource.games.blackjack import BJShoe

class TestShoe(unittest.TestCase):
    def setUp(self):
        self.shoe1 = BJShoe(1)
        self.shoe2 = BJShoe(2)
        self.shoe4 = BJShoe(4)
        self.shoe6 = BJShoe(6)
        self.shoe8 = BJShoe(8)
        self.shoe9 = BJShoe(9)
        
    def testRemaining(self):
        self.assertEqual(self.shoe1.remaining(), 52)
        self.assertEqual(self.shoe2.remaining(), 52*2)
        self.assertEqual(self.shoe4.remaining(), 52*4)
        self.assertEqual(self.shoe6.remaining(), 52*6)
        self.assertEqual(self.shoe8.remaining(), 52*8)
        self.assertEqual(self.shoe9.remaining(), 52*9)
        
    def testOriginalSize(self):
        self.assertEqual(self.shoe1.remaining(), 52)
        self.assertEqual(self.shoe1.original_size, 52)
        self.shoe1.pop()
        self.shoe1.pop()
        self.shoe1.pop()
        self.assertEqual(self.shoe1.remaining(), 49)
        self.assertEqual(self.shoe1.original_size, 52)

    def testRemove(self):
        self.assertEqual(self.shoe1.remaining(), 52)
        c1 = self.shoe1.remove('A')
        self.assertEqual(c1.rank, 'A')
        c1 = self.shoe1.remove('A')
        self.assertEqual(c1.rank, 'A')
        c1 = self.shoe1.remove('A')
        self.assertEqual(c1.rank, 'A')
        c1 = self.shoe1.remove('A')
        self.assertEqual(c1.rank, 'A')
        c1 = self.shoe1.remove('A')
        self.assertTrue(c1 is None)
 
