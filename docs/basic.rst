Basic usage
===========


Examples
--------

.. code-block:: python

    """
    Implements the game of WAR using the cardsource library. The result of a game
    of WAR is entirely determined by original position. It is also
    possible for the game to continue forever.

    See: http://en.wikipedia.org/wiki/War_(card_game)
    """

    from cardsource import Deck

    deck = Deck()
    deck.shuffle()

    # Split the deck into two halves
    player1 = deck[:26]
    player2 = deck[26:]


    # Game loop
    while len(player1) > 0 and len(player2) > 0:
        card1 = player1.pop()
        card2 = player2.pop()
        stakes = [card1, card2]
        winner = None

        if card1 > card2:
            winner = player1
        elif card1 < card2:
            winner = player2
        else:
            # handle WAR
            while winner is None:
                # Verify the players have enough cards for WAR
                if len(player1) < 2:
                    winner = player2
                    while len(player1) > 0:
                        stakes.append(player1.pop())
                elif len(player2) < 2:
                    winner = player1
                    while len(player2) > 0:
                        stakes.append(player2.pop())
                else:
                    # append additional stakes
                    stakes.append(player1.pop())
                    stakes.append(player2.pop())
                    card1 = player1.pop()
                    card2 = player2.pop()
                    stakes.append(card1)
                    stakes.append(card2)
                    if card1 > card2:
                        winner = player1
                    elif card2 > card1:
                        winner = player2
        for card in stakes:
            winner.appendleft(card)

    if len(player1) > 0:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
