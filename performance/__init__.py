from cardsource import Deck, Hand


def aces_count():
    aces = 0
    TOTAL = 100000
    for i in range(TOTAL):
        deck = Deck(numjokers=2)
        deck.shuffle()

        hand = Hand()
        hand.append(deck.pop())
        hand.append(deck.pop())

        if hand[0].rank == 'A' and hand[1].rank == 'A':
            aces += 1

    return aces
