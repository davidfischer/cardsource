import unittest

from cardsource import Card
from cardsource.games.blackjack import BJCard, BJHand


class TestBJHand(unittest.TestCase):
    def setUp(self):
        self.hand1 = BJHand()
        self.hand1.append('2c')
        self.hand1.append('4d')
        self.hand1.append('9h')

        self.hand2 = BJHand()
        self.hand2.append('2s')
        self.hand2.append('Js')
        self.hand2.append('Ts')

        self.hand3 = BJHand()
        self.hand3.append('As')
        self.hand3.append('Jd')
        self.hand3.append('Ts')

        self.hand4 = BJHand()
        self.hand4.append('2s')
        self.hand4.append('Ad')
        self.hand4.append('As')
        self.hand4.append('Ah')
        self.hand4.append('As')
        self.hand4.append('Ts')

        self.hand5 = BJHand()
        self.hand5.append('2s')
        self.hand5.append('5d')
        self.hand5.append('7s')
        self.hand5.append('6h')
        self.hand5.append('2s')
        self.hand5.append('As')

        self.hand6 = BJHand()
        self.hand6.append('2s')
        self.hand6.append('3d')
        self.hand6.append('4s')
        self.hand6.append('3h')
        self.hand6.append('2s')
        self.hand6.append('As')
        self.hand6.append('As')
        self.hand6.append('As')

        self.hand7 = BJHand()
        self.hand7.append('9s')
        self.hand7.append('As')

        self.hand8 = BJHand()
        self.hand8.append('As')
        self.hand8.append('As')

        self.hand9 = BJHand()
        self.hand9.append('Ts')
        self.hand9.append('Qs')

        self.hand10 = BJHand()
        self.hand10.append('4s')
        self.hand10.append('3s')

    def testCalculateValue(self):
        self.assertEqual(int(self.hand1), 15)
        self.assertEqual(int(self.hand2), 22)
        self.assertEqual(int(self.hand3), 21)
        self.assertEqual(int(self.hand4), 16)
        self.assertEqual(int(self.hand5), 23)
        self.assertEqual(int(self.hand6), 17)
        self.assertEqual(int(self.hand7), 20)
        self.assertEqual(int(self.hand8), 12)
        self.assertEqual(int(self.hand9), 20)

    def testSplittable(self):
        self.assertTrue(self.hand8.splittable())
        self.assertTrue(self.hand9.splittable())
        self.assertFalse(self.hand7.splittable())
        self.assertFalse(self.hand10.splittable())

    def testSplit(self):
        self.assertTrue(len(self.hand9), 2)
        split = self.hand9.split()
        self.assertTrue(len(self.hand9), 1)
        self.assertTrue(len(split), 1)
        self.assertEqual(int(split), int(self.hand9))

    def testSize(self):
        self.assertEqual(len(self.hand10), 2)
        self.assertEqual(len(self.hand9), 2)
        self.assertEqual(len(self.hand6), 8)
        self.hand6.clear()
        self.assertEqual(len(self.hand6), 0)

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


if __name__ == '__main__':
    unittest.main()
