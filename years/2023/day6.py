"""
Day 6: Wait For It
https://adventofcode.com/2023/day/6
"""
import math

from aoc.utils import time_function


def read_data(file_name: str) -> tuple[list[int], list[int], int, int]:
    with open(file_name, "r") as file:
        lines = file.readlines()
        times = [int(number) for number in lines[0].split()[1:]]
        distances = [int(number) for number in lines[1].split()[1:]]
        time = int("".join(lines[0].split()[1:]))
        distance = int("".join(lines[1].split()[1:]))

    return times, distances, time, distance


def calculate_distance(time: int, hold_button_time: int) -> int:
    distance = hold_button_time * (time - hold_button_time)
    return distance


@time_function
def part_1(times: list[int], distances: list[int]) -> int:
    races = []
    for time, distance in zip(times, distances):
        race = 0
        for option in range(time + 1):
            calculated_distance = calculate_distance(time, option)
            if calculated_distance > distance:
                race += 1
        races.append(race)

    return math.prod(races)


@time_function
def part_2(time: list[int], distance: list[int]) -> int:
    race = 0
    for option in range(time + 1):
        calculated_distance = calculate_distance(time, option)
        if calculated_distance > distance:
            race += 1
    return race


if __name__ == "__main__":
    times, distances, time, distance = read_data("years/2023/inputs/input6.txt")

    print("Part 1:")
    part_1(times, distances)

    print("Part 2:")
    part_2(time, distance)
