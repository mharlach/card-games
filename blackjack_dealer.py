from blackjack_strategy import IBlackjackStrategy
from blackjack_player import BlackjackPlayer
from blackjack_turn_choices import TurnChoices
from card import Card

class BlackjackDealer(BlackjackPlayer):
    def __init__(self, strategy: IBlackjackStrategy) -> None:
        super().__init__("Dealer", strategy)

    def up_card(self) -> Card:
        return self.cards[0]