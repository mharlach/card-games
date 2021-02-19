from card import Card, CardSuits
import random

class Deck:
    def __init__(self) -> None:
        self.cards = []
        suits = [CardSuits.Hearts, CardSuits.Diamonds, CardSuits.Spades, CardSuits.Clubs]
        for s in suits:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def take_card(self) -> Card:
        return self.cards.pop(0)

    def __str__(self) -> str:
        separator = "\n"
        output = separator.join(map(lambda x: str(x), self.cards))
        return output

