import unittest

from cardsource.cards import Card, InvalidRankError, InvalidSuitError

class TestCards(unittest.TestCase):
    def testCreateValid(self):
        c = Card(rank=2, suit='h')
        c = Card(rank=2, suit='H')
        c = Card(rank='A', suit='H')
        c = Card(rank='A', suit='h')
        c = Card(rank='a', suit='H')
        c = Card(rank='t', suit='s')
        c = Card(rank='t', suit='c')
        c = Card(rank='t', suit='d')
        c = Card(rank='j', suit='s')
        c = Card(rank='j', suit='S')

    def testInvalidSuit(self):
        try:
            c = Card(rank='j', suit='t')
            self.fail('"t" should fail since it is not a valid suit')
        except InvalidSuitError:
            pass
        
        try:
            c = Card(rank='j', suit='a')
            self.fail('"A" should fail since it is not a valid suit')
        except InvalidSuitError:
            pass
        
        try:
            c = Card(rank='Q')
            self.fail('"Q" requires a suit')
        except InvalidSuitError:
            pass
        
    def testInvalidRank(self):
        try:
            c = Card(rank='Z', suit='c')
            self.fail('"Z" should fail since it is not a valid rank')
        except InvalidRankError:
            pass
        
        try:
            c = Card(rank='w', suit='H')
            self.fail('"w" should fail since it is not a valid rank')
        except InvalidRankError:
            pass
        
        try:
            c = Card(rank=None, suit='H')
            self.fail('Rank should be required')
        except InvalidRankError:
            pass
        
    def testJoker(self):
        c = Card(rank='x')
        self.assertEqual(str(c), 'X')
        c = Card(rank='X', suit=None)
        self.assertEqual(str(c), 'X')
        c = Card(rank='X', suit='h')
        self.assertEqual(str(c), 'X')
        self.assertTrue(c.suit is None)
        
    def testToString(self):
        c = Card(rank=2, suit='h')
        self.assertEqual(str(c), '2h')
        c = Card(rank=2, suit='H')
        self.assertEqual(str(c), '2h')
        c = Card(rank='A', suit='H')
        self.assertEqual(str(c), 'Ah')
        c = Card(rank='A', suit='h')
        self.assertEqual(str(c), 'Ah')
        c = Card(rank='a', suit='H')
        self.assertEqual(str(c), 'Ah')
        c = Card(rank='t', suit='s')
        self.assertEqual(str(c), 'Ts')
        c = Card(rank='t', suit='c')
        self.assertEqual(str(c), 'Tc')
        c = Card(rank='t', suit='d')
        self.assertEqual(str(c), 'Td')
        c = Card(rank='j', suit='s')
        self.assertEqual(str(c), 'Js')
        c = Card(rank='j', suit='S')
        self.assertEqual(str(c), 'Js')
        
    def testSuited(self):
        c1 = Card(rank=2, suit='h')
        c2 = Card(rank=3, suit='H')
        self.assertTrue(c1.suited(c2))
        
        c3 = Card(rank='T', suit='H')
        self.assertTrue(c3.suited(c1))
        
        c4 = Card(rank='X')
        self.assertFalse(c4.suited(c3))
        
        c5 = Card(rank='J', suit='C')
        self.assertFalse(c5.suited(c4))
        self.assertFalse(c5.suited(c3))
        
    def testEqualRank(self):
        c1 = Card(rank=2, suit='h')
        c2 = Card(rank=3, suit='H')
        self.assertFalse(c1.equal_rank(c2))
        
        c3 = Card(rank='T', suit='c')
        c4 = Card(rank='T', suit='d')
        self.assertTrue(c4.equal_rank(c3))
        self.assertTrue(c3.equal_rank(c4))
        self.assertFalse(c1.equal_rank(c3))
        self.assertFalse(c1.equal_rank(c4))
        
        c5 = Card(rank='X')
        c6 = Card(rank='X')
        self.assertTrue(c5.equal_rank(c6))
        self.assertTrue(c6.equal_rank(c5))
        self.assertFalse(c1.equal_rank(c5))
        self.assertFalse(c4.equal_rank(c6))
    
if __name__ == '__main__':
    unittest.main()
