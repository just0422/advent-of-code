import sys
import math
from collections import Counter

letter_value = { "A": 13, "K": 12, "Q": 11, "J": 1, "T": 10}
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

        self.label = ""

        self.original = cards
        self.cards = self._convert_cards(cards)
        self.type = self._get_type(self.cards)
        self.value = self._get_value()

    def _get_type(self, cards):
        card_counts = Counter(cards)

        counts = sorted(card_counts.values())
        jacks = card_counts.get(1, 0)
        self.jacks = card_counts.get(1, 0)

        if counts == [ 5 ]:
            self.label = "Five of a Kind"
            return type_ranks["Five of a Kind"]

        if counts == [ 1, 4 ]:
            if jacks == 1 or jacks == 4:
                self.label = "Five of a Kind"
                return type_ranks["Five of a Kind"]
            self.label = "Four of a Kind"
            return type_ranks["Four of a Kind"]

        if counts == [ 2, 3 ]:
            if jacks == 2 or jacks == 3:
                self.label = "Five of a Kind"
                return type_ranks["Five of a Kind"]
            self.label = "Full House"
            return type_ranks["Full House"]

        if counts == [ 1, 1, 3 ]:
            if jacks == 3 or jacks == 1:
                self.label = "Four of a Kind"
                return type_ranks["Four of a Kind"]
            self.label = "Three of a Kind"
            return type_ranks["Three of a Kind"]

        if counts == [ 1, 2, 2 ]:
            if jacks == 2:
                self.label = "Four of a Kind"
                return type_ranks["Four of a Kind"]
            if jacks == 1:
                self.label = "Full House"
                return type_ranks["Full House"]
            self.label = "Two Pair"
            return type_ranks["Two Pair"]

        if counts == [ 1, 1, 1, 2 ]:
            if jacks == 2 or jacks == 1:
                self.label = "Three of a Kind"
                return type_ranks["Three of a Kind"]
            self.label = "One Pair"
            return type_ranks["One Pair"]

        if jacks == 1:
            self.label = "One Pair"
            return type_ranks["One Pair"]
        self.label = "High Card"
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
        return f"{self.original} - {self.label} - {self.cards} - {self.type} - {self.value}"

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
