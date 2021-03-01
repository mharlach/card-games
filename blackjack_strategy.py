from player import Player
from card import Card
from blackjack_turn_choices import TurnChoices

class IBlackjackStrategy:
    def get_choice(self, player: Player, dealerUpCard: Card) -> TurnChoices:
        pass

    def _get_card_value(self, c: Card) -> int:
        if c.number >= 2 and c.number <= 10:
            return c.number
        elif c.number == 1:
            return 1
        else:
            return 10