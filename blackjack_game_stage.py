from enum import Enum

class BlackjackStage(Enum):
    POST_DEAL = 1
    PLAYER_TURN = 2
    DEALER_TURN = 3
    SHOWDOWN = 4
    END = 5