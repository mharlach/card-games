from card import Card


class PlayerHand:
    def __init__(self, bet = 0) -> None:
        self.cards = []
        self.bet = 0

    def is_blackjack(self) -> bool:
        if len(self.cards) == 2:
            if self.hand_total()[1] == 21:
                return True
        return False

    def is_bust(self) -> bool:
        total = self.hand_total()
        if total[0] > 21:
            return True
        else:
            return False

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def hand_total(self) -> list[int]:
        low = 0
        high = 0
        for c in self.cards:
            if c.number == 1:
                low += 1
                high += 11
            elif c.number > 10:
                low += 10
                high += 10
            else:
                low += c.number
                high += c.number
        if low != high:
            if high > 21:
                return [low]
            else:
                return [low, high]
        else:
            return [low]
