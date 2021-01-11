from card import Card
from deck import Deck
from player import Player


class PokerGame:
    cardCount = 5

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []

    def deal(self, playerCount):
        if(playerCount > 11):
            raise Exception("Too many players")

        self.players = [Player("Player" + str(p)) for p in range(playerCount)]
        for p in self.players:
            for n in range(PokerGame.cardCount):
                p.add_card(self.deck.take_card())

    def print_status(self):
        n = 1
        for p in self.players:
            print("Player-" + str(n))
            n = n+1
            for c in p:
                print(c.toString())
            print("")

    def showdown(self):
        winner = None
        winningHand = PokerHand(0, 0, 0)
        for p in self.players:
            hand = evaluate_poker_hand(p.cards)
            if hand.handValue > winningHand.handValue:
                winner = p
                winningHand = hand
            elif hand.handValue == winningHand.handValue:
                if hand.handCardValue > winningHand.handCardValue:
                    winner = p
                    winningHand = hand
                elif hand.handCardValue == winningHand.handCardValue:
                    if hand.kicker > winningHand.kicker:
                        winner = p
                        winningHand = hand

        return (winner, winningHand)


class PokerHand:
    def __init__(self, handValue, handCardValue, kicker):
        self.handValue = handValue
        self.handCardValue = handCardValue
        self.kicker = kicker

    def __str__(self):
        text = "{a}.{b}.{c}".format(
            a=self.handValue, b=self.handCardValue, c=self.kicker)
        return text

    def to_long_string(self):
        if self.handValue == 1:
            return "High Card of {v}".format(v=self.handCardValue)
        elif self.handValue == 2:
            return "Pair of {v} w/ {k} kicker".format(v=self.handCardValue, k=self.kicker)
        elif self.handValue == 3:
            return "Two pair, {v} and {k}".format(v=self.handCardValue, k=self.kicker)
        elif self.handValue == 4:
            return "Three of a kind of {v} w/ {k} kicker".format(v=self.handCardValue, k=self.kicker)
        elif self.handValue == 5:
            return "Straight to a {v}".format(v=self.handCardValue)
        elif self.handValue == 6:
            return "Flush {v} high".format(v=self.handCardValue)
        elif self.handValue == 7:
            return "Full House, {v} over {k}".format(v=self.handCardValue, k=self.kicker)
        elif self.handValue == 8:
            return "Four of a Kind, {v} with {k} kicker".format(v=self.handCardValue, k=self.kicker)
        elif self.handValue == 9:
            return "Straight flush to a {v}".format(v=self.handCardValue)
        elif self.handValue == 10:
            return "Royal Flush!!"


def evaluate_poker_hand(hand):
    # jack - 1
    # pair - 2
    # two pair - 3
    # three of a kind - 4
    # straight - 5
    # flush - 6
    # full house - 7
    # four of a kind - 8
    # straight flush - 9
    # royal flush - 10
    # cards = cards.sort(key = lambda c: c.cardValue, reverse = True)
    cards = sorted(hand, key=lambda c: c.cardValue, reverse=True)

    def is_flush(cards):
        for c in cards:
            if c.suit != cards[0].suit:
                return False
        return True

    def is_ordered(cards):
        prev = cards[0]
        for n in range(1, len(cards)-1):
            if prev.cardValue-cards[n].cardValue != 1:
                return False
        return True

    isFlush = is_flush(cards)
    isStraight = is_ordered(cards)

    if isFlush and isStraight:
        if cards[0].cardValue == 14:
            # Royal Flush
            return PokerHand(10, 0, 0)
        else:
            # Straight Flush
            return PokerHand(9, cards[0].cardValue, 0)
    elif isFlush:
        return PokerHand(6, cards[0].cardValue, 0)
    elif isStraight:
        return PokerHand(5, cards[0].cardValue, 0)

    cardsByValue = {}
    multiples = False
    for c in cards:
        if cardsByValue.get(c.cardValue, None) == None:
            cardsByValue[c.cardValue] = 1
        else:
            cardsByValue[c.cardValue] = cardsByValue[c.cardValue] + 1
            multiples = True

    if multiples:
        pairs = []
        triples = None
        quads = None
        for k, v in cardsByValue.items():
            if v == 2:
                pairs.append(k)
            elif v == 3:
                triples = k
            elif v == 4:
                quads = k

        if quads != None:
            # Four of a Kind
            kicker = [c.cardValue for c in cards if c.cardValue != quads]
            return PokerHand(8, quads, kicker[0])

        if triples != None:
            if len(pairs) > 0:
                # Full House
                return PokerHand(7, triples, pairs[0])
            else:
                # Three of a Kind
                garbage = [c for c in cards if c.cardValue != triples]
                kicker = max(c.cardValue for c in garbage)
                return PokerHand(4, triples, kicker)

        if len(pairs) == 2:
            # two pair
            high = max(pairs)
            low = min(pairs)
            return PokerHand(3, high, low)

        if len(pairs) == 1:
            kicker = max(
                [c.cardValue for c in cards if c.cardValue != pairs[0]])
            return PokerHand(2, pairs[0], kicker)
    else:
        return PokerHand(1, cards[0].cardValue, 0)
