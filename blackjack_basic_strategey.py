from blackjack_strategy import IBlackjackStrategy
from blackjack_player import BlackjackPlayer
from blackjack_turn_choices import TurnChoices
from card import Card


class BasicStrategy(IBlackjackStrategy):
    def __init__(self) -> None:
        super().__init__()

    def get_choice(self, player: BlackjackPlayer, dealerUpCard: Card) -> TurnChoices:
        def findAces(card): card.number == 1
        aces = list(filter(findAces, player.cards))
        if len(player.cards) == 2:
            if len(aces) > 0:
                return self._get_soft_choice(player, dealerUpCard)
            else:
                return self._get_hard_choice(player, dealerUpCard)
        elif len(aces) > 1:
            return self._get_soft_choice(player, dealerUpCard)
        else:
            return self._get_hard_choice(player, dealerUpCard)

    def _get_hard_choice(self, player: BlackjackPlayer, dealerUpCard: Card) -> TurnChoices:
        total = 0
        for c in player.cards:
            total += self._get_card_value(c)

        if total < 8:
            return TurnChoices.Hit
        elif total >= 17:
            return TurnChoices.Stay
        else:
            rowIndex = total-8
            columnIndex = self._get_dealer_upcard_index(dealerUpCard)
            choiceValue = self._build_hard_total_chart()[rowIndex][columnIndex]
            return self._convert_to_choice(choiceValue)

    def _get_soft_choice(self, player: BlackjackPlayer, dealerUpCard: Card) -> TurnChoices:
        otherCards = list(filter(lambda c: c.number != 1, player.cards))
        total = 0
        for c in otherCards:
            total += self._get_card_value(c)

        if total < 2:
            return TurnChoices.Hit
        elif total >= 9:
            return TurnChoices.Stay
        else:
            rowIndex = total-2
            columnIndex = self._get_dealer_upcard_index(dealerUpCard)
            chartVal = self._build_soft_total_chart()[rowIndex][columnIndex]
            return self._convert_to_choice(chartVal)

    def _get_dealer_upcard_index(self, c: Card) -> int:
        if c.number >= 2 and c.number <= 10:
            return c.number-2
        elif c.number > 10:
            return 8
        else:
            return 9

    def _build_hard_total_chart(self):
        tbl = [["h", "h", "h", "h", "h", "h", "h", "h", "h", "h"],  # 8
               ["h", "d", "d", "d", "d", "h", "h", "h", "h", "h"],  # 9
               ["d", "d", "d", "d", "d", "d", "d", "d", "h", "h"],  # 10
               ["d", "d", "d", "d", "d", "d", "d", "d", "d", "d"],  # 11
               ["h", "h", "s", "s", "s", "h", "h", "h", "h", "h"],  # 12
               ["s", "s", "s", "s", "s", "h", "h", "h", "h", "h"],  # 13
               ["s", "s", "s", "s", "s", "h", "h", "h", "h", "h"],  # 14
               ["s", "s", "s", "s", "s", "h", "h", "h", "h", "h"],  # 15
               ["s", "s", "s", "s", "s", "h", "h", "h", "h", "h"],  # 16
               ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s"]]  # 17

        return tbl

    def _build_soft_total_chart(self) -> list[list[str]]:
        tbl = [["h", "h", "h", "d", "d", "h", "h", "h", "h", "h"],  # 13 -> A,2
               ["h", "h", "h", "d", "d", "h", "h", "h", "h", "h"],  # 14 -> A,3
               ["h", "h", "d", "d", "d", "h", "h", "h", "h", "h"],  # 15 -> A,4
               ["h", "h", "d", "d", "d", "h", "h", "h", "h", "h"],  # 16 -> A,5
               ["h", "d", "d", "d", "d", "h", "h", "h", "h", "h"],  # 17 -> A,6
               ["d", "d", "d", "d", "d", "s", "s", "h", "h", "h"],  # 18 -> A,7
               ["s", "s", "s", "s", "d", "s", "s", "s", "s", "s"],  # 19 -> A,8
               ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s"]]  # 20 -> A,9

        return tbl

    def _build_pair_spitting_chart(self) -> list[list[str]]:
        tbl = [["y", "y", "y", "y", "y", "y", "n", "n", "n", "n"],  # 2,2
               ["y", "y", "y", "y", "y", "y", "n", "n", "n", "n"],  # 3,3
               ["n", "n", "n", "y", "y", "n", "n", "n", "n", "n"],  # 4,4
               ["n", "n", "n", "n", "n", "n", "n", "n", "n", "n"],  # 5,5
               ["y", "y", "y", "y", "y", "n", "n", "n", "n", "n"],  # 6,6
               ["y", "y", "y", "y", "y", "y", "n", "n", "n", "n"],  # 7,7
               ["y", "y", "y", "y", "y", "y", "y", "y", "y", "y"],  # 8,8
               ["y", "y", "y", "y", "y", "n", "y", "y", "n", "n"],  # 9,9
               ["n", "n", "n", "n", "n", "n", "n", "n", "n", "n"],  # 10,10
               ["y", "y", "y", "y", "y", "y", "y", "y", "y", "y"]]  # A,A

        return tbl

    def _convert_to_choice(self, input: str) -> TurnChoices:
        if(input == "h"):
            return TurnChoices.Hit
        elif(input == "s"):
            return TurnChoices.Stay
        elif(input == "d"):
            return TurnChoices.Hit
        elif(input == "y"):
            return TurnChoices.Stay
        else:
            return TurnChoices.Stay
