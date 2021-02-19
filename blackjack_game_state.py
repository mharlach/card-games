from blackjack_dealer import BlackjackDealer
from blackjack_player import BlackjackPlayer
from blackjack_game_stage import BlackjackStage
from blackjack_game_results import BlackjackGameResults


class BlackjackGameState:
    def __init__(self, dealer: BlackjackDealer, player: BlackjackPlayer) -> None:
        self.dealer = dealer
        self.player = player
        self.stage = BlackjackStage.POST_DEAL
        self.gameResult = BlackjackGameResults.IN_PROGRESS

    def __str__(self) -> str:
        output = "{a} : {b}".format(a=str(self.stage.name),b=str(self.gameResult.name))
        output += "\n"
        output += str(self.player)
        output += "\n"
        output += str(self.dealer)
        return output
