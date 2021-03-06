import unittest

from cardsource import Card, CardSourceError


class TestCards(unittest.TestCase):
    def testInvalidSuit(self):
        self.assertRaises(CardSourceError, Card, 'Jt')
        self.assertRaises(CardSourceError, Card, 'Ja')
        self.assertRaises(CardSourceError, Card, 'Q')

    def testInvalidRank(self):
        self.assertRaises(CardSourceError, Card, 'Zc')
        self.assertRaises(CardSourceError, Card, 'wH')
        self.assertRaises(CardSourceError, Card, 'H')
        self.assertRaises(CardSourceError, Card, 2)
        self.assertRaises(CardSourceError, Card, ['2', 'h'])

    def testToString(self):
        tests = [
            ('2h', '2h'),
            ('2H', '2h'),
            ('aH', 'Ah'),
            ('AH', 'Ah'),
            ('ts', 'Ts'),
            ('xx', 'X'),
            ('X', 'X'),
            ('x', 'X'),
        ]

        for t in tests:
            self.assertEqual(str(Card(t[0])), t[1])

    def testComparisons(self):
        self.assertTrue(Card('2h') == Card('2h'))
        self.assertFalse(Card('2h') == Card('3h'))
        self.assertTrue(Card('2H') == Card('2h'))

        self.assertTrue(Card('3h') > Card('2h'))
        self.assertTrue(Card('Ah') > Card('Ts'))
        self.assertFalse(Card('Ah') < Card('Ts'))
        self.assertTrue(Card('Ah') >= Card('As'))
        self.assertTrue(Card('Ah') >= Card('Ks'))
        self.assertTrue(Card('Ah') != Card('As'))
        self.assertTrue(Card('4c') <= Card('Ts'))

    def testInvalidComparisons(self):
        self.assertFalse(Card('4c') == '4c')
        self.assertFalse('4c' == Card('4c'))

        try:
            Card('Ah') >= 'Ah'
            self.fail('Comparing cards with non-cards should fail')
        except TypeError:
            pass
        try:
            self.assertRaises(TypeError, Card('Ah') > [])
            self.fail('Comparing cards with non-cards should fail')
        except TypeError:
            pass


if __name__ == '__main__':
    unittest.main()
