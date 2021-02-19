from enum import Enum

class CardSuits(Enum):
    Hearts = 1
    Clubs = 2
    Diamonds = 3
    Spades = 4

    def __str__(self) -> str:
        return self.name

class Card:
    def __init__(self, suit: CardSuits, number: int):
        self.suit = suit
        self.number = number
        self.faceValue = str(number)
        self.cardValue = number
        self.set_face_value()
        self.set_card_value()

    def __str__(self) -> str:
        return str(self.faceValue) + "-" + str(self.suit)

    def set_face_value(self):
        if self.number == 11:
            self.faceValue = "Jack"
        elif self.number == 12:
            self.faceValue = "Queen"
        elif self.number == 13:
            self.faceValue = "King"
        elif self.number == 1:
            self.faceValue = "Ace"

    def set_card_value(self):
        if self.number == 1:
            self.cardValue = 14

