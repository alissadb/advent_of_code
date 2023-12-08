"""
Day 7: Camel Cards
https://adventofcode.com/2023/day/7
"""
from collections import Counter

from pydantic import BaseModel

from aoc.utils import read_split_data, time_function

CARD_TYPE = {
    "Five of a kind": 6,
    "Four of a kind": 5,
    "Full house": 4,
    "Three of a kind": 3,
    "Two pair": 2,
    "One pair": 1,
    "High card": 0,
}

CARD_ORDER_PART_1 = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}


CARD_ORDER_PART_2 = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


class Card(BaseModel):
    hand: str
    bid: int
    hand_counts: dict = {}
    ranking: int = 0
    value: list[int] = []
    use_joker: bool = False
    card_order: dict = {}

    def determine_value(self):
        self.value = [self.card_order[card] for card in self.hand]

    def determine_ranking(self):
        self.hand_counts = Counter(self.hand)
        if self.use_joker:
            if "J" in self.hand_counts:
                use_joker_count = self.hand_counts["J"]
                self.hand_counts.pop("J")

                # Only use_jokers
                if use_joker_count == 5:
                    self.ranking = CARD_TYPE["Five of a kind"]
                    return self.ranking

                # Check other most common_values
                counter_hand_counts = Counter(self.hand_counts)
                most_count = counter_hand_counts.most_common(1)[0][1]
                most_value = counter_hand_counts.most_common(1)[0][0]
                for hand_key in self.hand_counts.keys():
                    if self.hand_counts[hand_key] == most_count:
                        if self.card_order[hand_key] > self.card_order[most_value]:
                            most_value = hand_key
                self.hand_counts[most_value] += use_joker_count

        if len(self.hand_counts) == 1:
            self.ranking = CARD_TYPE["Five of a kind"]
        elif len(self.hand_counts) == 2:
            if 4 in self.hand_counts.values():
                self.ranking = CARD_TYPE["Four of a kind"]
            if 3 in self.hand_counts.values():
                self.ranking = CARD_TYPE["Full house"]
        elif len(self.hand_counts) == 3:
            if 3 in self.hand_counts.values():
                self.ranking = CARD_TYPE["Three of a kind"]
            if 2 in self.hand_counts.values():
                self.ranking = CARD_TYPE["Two pair"]
        elif len(self.hand_counts) == 4 and 2 in self.hand_counts.values():
            self.ranking = CARD_TYPE["One pair"]
        elif len(self.hand_counts) == 5:
            self.ranking = CARD_TYPE["High card"]

        return self.ranking


class Cards:
    def __init__(self, camels: list, card_order: dict, use_joker: bool):
        self.camels = camels
        self.card_order = card_order
        self.use_joker = use_joker
        self.cards = []
        self.total_winnings = 0

    def get_cards(self) -> list[Card]:
        cards: list[Card] = []
        for camel in camels:
            hand, bid = camel.split()

            card = Card(
                hand=hand,
                bid=int(bid),
                use_joker=self.use_joker,
                card_order=self.card_order,
            )
            card.determine_ranking()
            card.determine_value()
            cards.append(card)

        self.cards = cards

    def sort_cards(self) -> list[Card]:
        self.cards = sorted(
            self.cards, key=lambda card: (card.ranking, card.value), reverse=False
        )

    def calculate_total_winnings(self) -> int:
        if self.cards == []:
            self.get_cards()
            self.sort_cards()

        self.total_winnings = sum(
            [(rank + 1) * card.bid for rank, card in enumerate(self.cards)]
        )


@time_function
def calculate_part(camels: list, card_order: dict, use_joker: bool):
    cards = Cards(camels, card_order, use_joker=use_joker)
    cards.calculate_total_winnings()

    return cards.total_winnings


if __name__ == "__main__":
    camels = read_split_data("years/2023/inputs/input7.txt")

    print("Part 1:")
    calculate_part(camels, CARD_ORDER_PART_1, use_joker=False)

    print("Part 2:")
    part_2 = calculate_part(camels, CARD_ORDER_PART_2, use_joker=True)
