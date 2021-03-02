from player import Player
from card import Card
from blackjack_turn_choices import TurnChoices
from blackjack_hand import PlayerHand


class BlackjackPlayer(Player):
    def __init__(self, name: str, handsCount: int) -> None:
        super().__init__(name)
        self.handsCount = handsCount
        self.hands = []
        for i in range(handsCount):
            self.hands.append(PlayerHand())

    def add_card(self, card: Card, handIndex: int) -> None:
        if handIndex < self.handsCount:
            self.hands[handIndex].add_card(card)

    def make_turn_choice(self, handIndex: int) -> TurnChoices:
        return TurnChoices.Hit

    def split_hand(self, handIndex: int) -> None:
        splitHandLeft = PlayerHand()
        splitHandLeft.add_card(self.hands[handIndex].cards[0])

        splitHandRight = PlayerHand()
        splitHandRight.add_card(self.hands[handIndex].cards[1])

        self.hands[handIndex] = splitHandLeft
        self.hands.insert(handIndex + 1, splitHandRight)

    def double_down(self, handIndex: int) -> None:
        pass

    
