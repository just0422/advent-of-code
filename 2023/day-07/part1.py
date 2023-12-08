import sys
import math
from collections import Counter

letter_value = { "A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
type_ranks = {
    "Five of a Kind": 7,
    "Four of a Kind": 6,
    "Full House": 5,
    "Three of a Kind": 4,
    "Two Pair": 3,
    "One Pair": 2,
    "High Card": 1
}

class Hand:
    def __init__(self, cards, bid):
        self.rank = int(bid)

        self.original = cards
        self.cards = self._convert_cards(cards)
        self.type = self._get_type(self.cards)
        self.value = self._get_value()

    def _get_type(self, cards):
        card_counts = Counter(cards)

        counts = sorted(card_counts.values())

        if counts == [ 5 ]:
            return type_ranks["Five of a Kind"]

        if counts == [ 1, 4 ]:
            return type_ranks["Four of a Kind"]

        if counts == [ 2, 3 ]:
            return type_ranks["Full House"]

        if counts == [ 1, 1, 3 ]:
            return type_ranks["Three of a Kind"]

        if counts == [ 1, 2, 2 ]:
            return type_ranks["Two Pair"]

        if counts == [ 1, 1, 1, 2 ]:
            return type_ranks["One Pair"]

        return type_ranks["High Card"]

    def _get_value(self):
        value = 0

        reversed_cards = list(reversed(self.cards))
        for x in range(len(self.cards)):
            value += reversed_cards[x] * math.pow(10, x * 2)

        value += self.type * math.pow(10, len(self.cards) * 2)
        return int(value)

    def _convert_cards(self, cards):
        num_cards = []
        for card in list(cards):
            if card.isnumeric():
                num_cards.append(int(card))
            else:
                num_cards.append(letter_value[card])
        return num_cards

    def __str__(self):
        return f"{self.original} - {self.cards} - {self.type} - {self.value}"

    def __repr__(self):
        return str(self)

hands = []
with open(sys.argv[1]) as hand_file:
    while line := hand_file.readline().rstrip():
        cards, bid = line.split(" ")
        hands.append(Hand(cards, bid))

bids = [hand.rank for hand in sorted(hands, key=lambda hand: hand.value)]

bid_sum = 0
for x in range(len(bids)):
    bid_sum += (x + 1) * bids[x]

print(bid_sum)
