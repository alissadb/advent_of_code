"""
Day 2: Cube Conundrum
https://adventofcode.com/2023/day/2
"""
import re

import numpy as np

from aoc.utils import read_split_data, time_function

data = read_split_data("years/2023/inputs/input2.txt")
games = [re.split(": |; ", game) for game in data]

LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


@time_function
def part1():
    possible_games = 0
    for game_number, game in enumerate(games):
        possible_game = True
        for cubes in game[1:]:
            for cube in cubes.split(", "):
                number, colour = cube.split(" ")

                if int(number) > LIMITS[colour]:
                    # print(f"{number} {colour} more than {LIMITS[colour]}")
                    possible_game = False

        # print(f"Game number: {game_number} Possible: {possible_game}")
        if possible_game:
            possible_games += game_number + 1

    print(f"Possible games: {possible_games}")


@time_function
def part2():
    powers = 0
    for game_number, game in enumerate(games):
        colours = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for cubes in game[1:]:
            for cube in cubes.split(", "):
                number, colour = cube.split(" ")

                if int(number) > colours[colour]:
                    colours[colour] = int(number)

        power = np.prod(list(colours.values()))
        # print(
        #     f"Game number: {game_number+1} Power game: {power} Red: {colours['red']} Green: {colours['green']} Blue: {colours['blue']}"
        # )
        powers += power

    print(f"Total power: {powers}")


if __name__ == "__main__":
    print("\nPart 1:")
    part1()
    print("\nPart 2:")
    part2()
