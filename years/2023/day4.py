"""
Day 4: Scratchcards
https://adventofcode.com/2023/day/4
"""
import re

from aoc.utils import read_split_data, time_function


def process_line(line: str):
    first_part, numbers = line.split("|")
    card, winning_numbers = first_part.split(":")

    card_number = int(re.split(r"\s+", card)[1])
    card_numbers = [num for num in numbers.split()]
    card_winning_numbers = [num for num in winning_numbers.split()]

    return card_number, card_winning_numbers, card_numbers


@time_function
def calculate_part_1(data: list[str]):
    total_points = 0

    for line in data:
        _, card_winning_numbers, card_numbers = process_line(line)

        overlapping_numbers = len(set(card_numbers) & set(card_winning_numbers))

        total_points += 2 ** max(0, overlapping_numbers - 1)  # 2^0 + 2^1 + .. + 2^n

    print(f"Part 1: {total_points}")


@time_function
def calculate_part_2(data: list[str]):
    cards = [1] * len(data)
    for card_number, line in enumerate(data):
        first_part, numbers = line.split("|")
        _, winning_numbers = first_part.split(":")

        card_numbers = [num for num in numbers.split()]
        card_winning_numbers = [num for num in winning_numbers.split()]

        overlapping_numbers = len(set(card_numbers) & set(card_winning_numbers))

        # Winning cards are the next few cards
        for number in range(card_number, card_number + overlapping_numbers):
            cards[number + 1] += cards[card_number]

    print(f"Part 2: {sum(cards)}")


# Didn't read well, you win copies of the scratchcards above your scratch card,
# which are equal to the number of matches. So you don't need a recursive function
def count_scratch_cards(cards: dict, card_number: int, cards_counts: dict) -> dict:
    winning_cards = cards.get(card_number, [])
    for winning_card in winning_cards:
        cards_counts[winning_card] += 1
        count_scratch_cards(cards, winning_card, cards_counts=cards_counts)

    return cards_counts


if __name__ == "__main__":
    data = read_split_data("years/2023/inputs/input4.txt")

    calculate_part_1(data)
    calculate_part_2(data)
