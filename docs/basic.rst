Basic usage
===========


Examples
--------


WAR
###

The game of War_ is entirely determined by starting position. It is also
possible that the initial state results in a neverending game.

.. _War: http://en.wikipedia.org/wiki/War_(card_game)

Creating the game of War using cardsource is fairly straight-forward.
Take a look at the comments to see the cardsource library in action.



.. code-block:: python

    from cardsource import Deck

    deck = Deck()
    deck.shuffle()

    # Split the deck into two halves
    player1 = deck[:26]
    player2 = deck[26:]


    # Game loop which is potententially infinite
    while len(player1) > 0 and len(player2) > 0:
        card1 = player1.pop()
        card2 = player2.pop()
        stakes = [card1, card2]
        winner = None

        # Card gt/lt operations are based on rank alone
        # Suit is not considered
        if card1 > card2:
            winner = player1
        elif card1 < card2:
            winner = player2
        else:
            # handle WAR
            while winner is None:
                # Verify the players have enough cards for WAR
                # If either player does not have enough, they
                # automatically lose the WAR and the game.
                if len(player1) < 2:
                    winner = player2
                    while len(player1) > 0:
                        stakes.append(player1.pop())
                elif len(player2) < 2:
                    winner = player1
                    while len(player2) > 0:
                        stakes.append(player2.pop())
                else:
                    # append additional stakes for the war
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
