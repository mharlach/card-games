from card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def addCard(self, c):
        self.cards.append(c)

    def printHand(self):
        for c in self.cards:
            print(c.toString())

    def toShortString(self):
        text = "{n} --".format(n=self.name)
        for c in self.cards:
            text = text + " {v}{s} ".format(v=c.cardValue, s=c.suit[0])

        return text
