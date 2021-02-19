from blackjack_game_results import BlackjackGameResults
from blackjack_game_stage import BlackjackStage
from blackjack_game import BlackjackGame

game = BlackjackGame()
wins = 0
losses = 0
rounds = 0
goAgain = True
while(goAgain):
    state = game.deal()
    print(str(state))
    while(state.stage != BlackjackStage.END):
        print("***********")    
        state = game.play(state)
        print(str(state))
        if state.gameResult == BlackjackGameResults.Win:
            wins+=1
        elif state.gameResult == BlackjackGameResults.Lose:
            losses += 1
        rounds += 1

    print("\n")
    inVal = input("Press enter to run again")
    if inVal == "n":
        goAgain = False
    else:
        print("\n")

print("Wins: {w} -- Losses: {l}".format(w=str(wins), l=str(losses)))
print("Games: {g}".format(g=str(rounds)))