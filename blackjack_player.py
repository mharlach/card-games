from player import Player
from card import Card
from blackjack_turn_choices import TurnChoices
from blackjack_strategy import IBlackjackStrategy


class BlackjackPlayer(Player):
    def __init__(self, name: str, strategy: IBlackjackStrategy) -> None:
        super().__init__(name)
        self.value = [0, 0]
        self.strategy = strategy

    def get_value(self) -> list[int]:
        return self.value

    def add_card(self, c: Card) -> None:
        if(c.number >= 11 and c.number <= 13):
            self.value[0] += 10
            self.value[1] += 10
        elif(c.number == 1):
            self.value[0] += 1
            self.value[1] += 11
        else:
            self.value[0] += c.number
            self.value[1] += c.number

        return super().add_card(c)

    def has_blackjack(self) -> bool:
        if(self.value[1] == 21 and len(self.cards) == 2):
            return True
        else:
            return False

    def has_bust(self) -> bool:
        if(self.value[1] > 21):
            return True
        else:
            return False

    def make_choice(self, dealerCard: Card) -> TurnChoices:
        return self.strategy.get_choice(self, dealerCard)

    def __str__(self) -> str:
        text = super().__str__()
        if(self.value[0] != self.value[1]):
            text += " ==> {l}/{h}".format(
                l=str(self.value[0]), h=str(self.value[1]))
        else:
            text += " ==> {v}".format(v=str(self.value[0]))
        return text
        # text += "==> {}".format(v=str(self.value))
