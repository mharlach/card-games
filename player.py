from card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, c):
        self.cards.append(c)

    def print_hand(self):
        for c in self.cards:
            print(c.toString())

    def __str__(self):
        text = "{n} --".format(n=self.name)
        for c in self.cards:
            text = text + " {v}{s} ".format(v=c.cardValue, s=c.suit[0])

        return text
