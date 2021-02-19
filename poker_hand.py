class PokerHand:
    def __init__(self, handValue, handCardValue, kicker):
        self.handValue = handValue
        self.handCardValue = handCardValue
        self.kicker = kicker

    def __str__(self):
        text = "{a}.{b}.{c}".format(
            a=self.handValue, b=self.handCardValue, c=self.kicker)
        return text

    def to_long_string(self):
        if self.handValue == 1:
            return "High Card of {v}".format(v=self.handCardValue)
        elif self.handValue == 2:
            return "Pair of {v} w/ {k} kicker".format(v=self.handCardValue, k=self.kicker)
        elif self.handValue == 3:
            return "Two pair, {v} and {k}".format(v=self.handCardValue, k=self.kicker)
        elif self.handValue == 4:
            return "Three of a kind of {v} w/ {k} kicker".format(v=self.handCardValue, k=self.kicker)
        elif self.handValue == 5:
            return "Straight to a {v}".format(v=self.handCardValue)
        elif self.handValue == 6:
            return "Flush {v} high".format(v=self.handCardValue)
        elif self.handValue == 7:
            return "Full House, {v} over {k}".format(v=self.handCardValue, k=self.kicker)
        elif self.handValue == 8:
            return "Four of a Kind, {v} with {k} kicker".format(v=self.handCardValue, k=self.kicker)
        elif self.handValue == 9:
            return "Straight flush to a {v}".format(v=self.handCardValue)
        elif self.handValue == 10:
            return "Royal Flush!!"