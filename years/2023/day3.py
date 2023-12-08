import math
import re

import numpy as np

from aoc.utils import read_split_data, time_function


def get_adjacent_indices_value(matrix, row, column):
    adjacent_indices = []
    adjacent_values = []

    for direction_row, direction_column in [
        (-1, 0),
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]:
        row_new, column_new = row + direction_row, column + direction_column
        if 0 <= row_new < matrix.shape[0] and 0 <= column_new < matrix.shape[1]:
            adjacent_indices.append((row_new, column_new))
            value = matrix[row_new, column_new]
            if value != "." and not value.isdigit():
                adjacent_values.append(value)

    return adjacent_indices, adjacent_values


@time_function
def calculate_part_1(engine_schematic):
    part_numbers = 0
    numbers = {}
    for row_i, row in enumerate(engine_schematic):
        for number in re.finditer(r"\d+", row):
            number_str = number.group()
            start = number.start()
            end = number.end()

            adjacent_indices = set()
            for col in [start, (end - 1)]:
                _, adjacent_values = get_adjacent_indices_value(matrix, row_i, col)
                adjacent_indices.update(adjacent_values)

                # Get all the numbers for part 2
                numbers.update({(row_i, col): int(number_str)})

            if len(adjacent_indices) > 0:
                part_numbers += int(number_str)

    print(f"Part 1: {part_numbers}")
    return numbers


@time_function
def calculate_part_2(engine_schematic, numbers):
    total_sum = 0
    for row_i, row in enumerate(engine_schematic):
        for symbol in re.finditer(r"\*", row):
            start = symbol.start()

            adjacent_indices, _ = get_adjacent_indices_value(matrix, row_i, start)

            values = [
                numbers[adjacent_index]
                for adjacent_index in adjacent_indices
                if adjacent_index in numbers
            ]

            if len(set(values)) == 2:
                total_sum += math.prod(set(values))

    print(f"Part 2: {total_sum}")


if __name__ == "__main__":
    engine_schematic = read_split_data("years/2023/inputs/input3.txt")
    matrix = np.array([list(line) for line in engine_schematic])

    numbers = calculate_part_1(engine_schematic)
    calculate_part_2(engine_schematic, numbers)
