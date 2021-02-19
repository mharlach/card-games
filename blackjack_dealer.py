from blackjack_player import BlackjackPlayer
from blackjack_turn_choices import TurnChoices
from card import Card

class BlackjackDealer(BlackjackPlayer):
    def __init__(self) -> None:
        super().__init__("Dealer")

    def make_choice(self) -> TurnChoices:
        if(self.value[1] < 16):
            return TurnChoices.Hit
        return TurnChoices.Stay

    def up_card(self) -> Card:
        return self.cards[0]