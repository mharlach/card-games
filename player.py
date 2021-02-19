from card import Card

class Player:
    def __init__(self, name: str)->None:
        self.name = name
        self.cards = []

    def add_card(self, c: Card) -> None:
        self.cards.append(c)

    def __str__(self) -> str:
        text = "{n} --".format(n=self.name)
        for c in self.cards:
            text += " {v}{s} ".format(v=c.cardValue, s=c.suit.name[0])

        return text
