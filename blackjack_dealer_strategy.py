from player import Player
from card import Card
from blackjack_turn_choices import TurnChoices
from blackjack_strategy import IBlackjackStrategy

class BlackjackDealerStrategy(IBlackjackStrategy):
    def get_choice(self, player: Player, dealerUpCard: Card) -> TurnChoices:
        total = 0
        for c in player.cards:
            if c.number > 10:
                total += 10
            else:
                total += c.number

        return TurnChoices.Hit if total <= 16 else TurnChoices.Stay