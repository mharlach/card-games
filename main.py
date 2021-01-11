from card import Card
from deck import Deck
from game import PokerGame
from game import evaluate_poker_hand

for i in range(10):
    pokerGame = PokerGame()
    pokerGame.deal(3)
    (winner, winningHand) = pokerGame.showdown()

    print("==== Game {num} ====".format(num = i))
    for p in pokerGame.players:
        print(p)
    print()
    print("{winner} -- {hand}".format(winner=winner.name, hand=winningHand.to_long_string()))