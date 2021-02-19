from enum import Enum
from card import Card
from deck import Deck
from deck_shoe import DeckShoe
from blackjack_player import BlackjackPlayer
from blackjack_dealer import BlackjackDealer
from blackjack_game_state import BlackjackGameState
from blackjack_game_stage import BlackjackStage
from blackjack_game_results import BlackjackGameResults
from blackjack_turn_choices import TurnChoices


class BlackjackGame:
    def __init__(self) -> None:
        self.shoe = DeckShoe(2)


    def deal(self) -> BlackjackGameState:
        if(self.shoe.refreshRequired):
            self.shoe.refresh(75)

        player = BlackjackPlayer("Player 1")
        player.add_card(self.shoe.deal_card())
        player.add_card(self.shoe.deal_card())

        dealer = BlackjackDealer()
        dealer.add_card(self.shoe.deal_card())
        dealer.add_card(self.shoe.deal_card())

        state = BlackjackGameState(dealer, player)
        return state

    def play(self, state: BlackjackGameState) -> BlackjackGameState:
        if(state.stage == BlackjackStage.POST_DEAL):
            state = self._play_post_deal(state)
        elif(state.stage == BlackjackStage.PLAYER_TURN):
            state = self._play_player_turn(state)
        elif(state.stage == BlackjackStage.DEALER_TURN):
            state = self._play_dealer_turn(state)
        elif(state.stage == BlackjackStage.SHOWDOWN):
            state = self._play_get_result(state)

        return state

    def _play_post_deal(self, state) -> BlackjackGameState:
        if(state.player.has_blackjack() and state.dealer.has_blackjack()):
            state.stage = BlackjackStage.END
            state.gameResult = BlackjackGameResults.Push
        elif(state.player.has_blackjack()):
            state.stage = BlackjackStage.END
            state.gameResult = BlackjackGameResults.Win
        elif(state.dealer.has_blackjack()):
            state.stage = BlackjackStage.END
            state.gameResult = BlackjackGameResults.Lose
        else:
            state.stage = BlackjackStage.PLAYER_TURN

        return state

    def _play_player_turn(self, state: BlackjackGameState) -> BlackjackGameState:
        while(state.player.make_choice(state.dealer.up_card()) == TurnChoices.Hit):
            state.player.add_card(self.shoe.deal_card())

        if(state.player.has_bust()):
            state.stage = BlackjackStage.END
            state.gameResult = BlackjackGameResults.Lose
        else:
            state.stage = BlackjackStage.DEALER_TURN

        return state

    def _play_dealer_turn(self, state: BlackjackGameState) -> BlackjackGameState:
        while(state.dealer.make_choice() == TurnChoices.Hit):
            state.dealer.add_card(self.shoe.deal_card())

        if(state.dealer.has_bust()):
            state.stage = BlackjackStage.END
            state.gameResult = BlackjackGameResults.Win
        else:
            state.stage = BlackjackStage.SHOWDOWN

        return state


    def _play_get_result(self, state: BlackjackGameState) -> BlackjackGameState:
        def get_score(
            scores): return scores[1] if scores[1] <= 21 else scores[0]
        dealerScore = get_score(state.dealer.get_value())
        playerScore = get_score(state.player.get_value())

        if(playerScore > dealerScore):
            state.gameResult = BlackjackGameResults.Win
        elif(dealerScore > playerScore):
            state.gameResult = BlackjackGameResults.Lose
        else:
            state.gameResult = BlackjackGameResults.Push

        state.stage = BlackjackStage.END

        return state
