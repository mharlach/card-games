class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.faceValue = str(number)
        self.cardValue = number
        self.setFaceValue()
        self.setCardValue()

    def toString(self):
        return str(self.faceValue) + "-" + self.suit

    def setFaceValue(self):
        if self.number == 11:
            self.faceValue = "Jack"
        elif self.number == 12:
            self.faceValue = "Queen"
        elif self.number == 13:
            self.faceValue = "King"
        elif self.number == 1:
            self.faceValue = "Ace"
    
    def setCardValue(self):
        if self.number == 1:
            self.cardValue = 14


