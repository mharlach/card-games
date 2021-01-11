class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.faceValue = str(number)
        self.cardValue = number
        self.set_face_value()
        self.set_card_value()

    def __str__(self):
        return str(self.faceValue) + "-" + self.suit

    # def toString(self):
    #     return str(self.faceValue) + "-" + self.suit

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
