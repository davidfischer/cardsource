import random

from . import BJCard, BJDeck


class BJShoe(object):
    def __init__(self, num_decks=1):
        """
        Create and shuffle a dealing shoe made of the correct number of BJDecks
        """

        self._cards = []
        self.num_decks = num_decks
        self.reset()
        self.original_size = len(self._cards)

    def remaining(self):
        """
        Return the number of remaining cards in the shoe
        """

        return len(self._cards)

    def pop(self):
        """
        Returns the top card of the shoe or None if the show is empty
        """

        if self.remaining() > 0:
            return self._cards.pop()
        return None

    def shuffle(self):
        """
        Shuffles the remaining deck
        """

        random.shuffle(self._cards)

    def reset(self):
        """
        Recreates the shoe with the correct amount of decks
        """

        self.cards = []

        for i in range(self.num_decks):
            deck = BJDeck()
            self._cards.extend(deck._cards)

        self.shuffle()

    def remove(self, rank):
        """
        Removes the bottom card with rank from the deck (all tens are equal) and then shuffles
        """

        for i in range(len(self._cards)):
            if BJCard.VALUES[self._cards[i].rank] == BJCard.VALUES[rank]:
                card = self._cards.pop(i)
                self.shuffle()
                return card

        return None
