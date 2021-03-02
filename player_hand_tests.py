from card import Card, CardSuits
from blackjack_hand import PlayerHand


def hand_total_returns_10():
    hand = PlayerHand()
    hand.add_card(Card(CardSuits.Clubs, 5))
    hand.add_card(Card(CardSuits.Diamonds, 5))
    assert len(hand.cards) == 2
    total = hand.hand_total()
    assert len(total) == 1
    assert total[0] == 10


def hand_total_returns_6_16():
    hand = PlayerHand()
    hand.add_card(Card(CardSuits.Clubs, 1))
    hand.add_card(Card(CardSuits.Clubs, 12))
    assert hand.hand_total()[1] == 21
    assert hand.is_blackjack() == True


if __name__ == "__main__":
    hand_total_returns_10()
    hand_total_returns_6_16()
    print("All tests completed")