from deck import Deck
import random
from card import Card

class DeckShoe:
    def __init__(self, deckCount: int) -> None:
        self.cards = []
        self.deckCount = deckCount
        self.refreshRequired = True

    def refresh(self, percentCut: float) -> None:
        self.cards = []
        for i in range(self.deckCount):
            self.cards.extend(Deck().cards)
        random.shuffle(self.cards)
        self.cutCardIndex = len(self.cards) * (percentCut/100)
        self.refreshRequired = False
        self.playIndex = 0

    def deal_card(self) -> Card:
        self.playIndex += 1
        if(self.playIndex >= self.cutCardIndex):
            self.refreshRequired = True

        return self.cards.pop()