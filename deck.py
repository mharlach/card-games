from random import randint
from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Clubs", "Diamonds", "Spades", "Hearts"]
        for s in suits:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def shuffle(self):
        for n in range(0, 51):
            a = randint(0, 51)
            b = randint(0, 51)
            cardA = self.cards[a]
            cardB = self.cards[b]
            self.cards[a] = cardB
            self.cards[b] = cardA

    def take_card(self):
        return self.cards.pop(0)
