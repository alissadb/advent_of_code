"""
Day 1: Trebuchet?!
https://adventofcode.com/2023/day/1
"""
import re

import numpy as np
import typer

DIGIT_MAPPING: dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
REGEX_NUMBERS: str = "\d+"
REGEX_NUMBERS_WORDS: str = "(?=(one|two|three|four|five|six|seven|eight|nine|\d+))"


def get_calibration_value(digits: str) -> int:
    """
    Get calibration value for a line. Will either transform the number to digit or take the digit itself.

    Args:
        digits (str): The digits to transform.

    Returns:
        int: Calibration value.
    """
    all_digits = "".join([DIGIT_MAPPING.get(digit, digit) for digit in digits])
    return int(all_digits[0] + all_digits[-1])


def calculate_total_calibration_value(input_file_name: str, regex_pattern: str):
    """
    Calculate total calibration value for a document using a specified regex method to find the numbers.

    Args:
        input_file_name: The document file name.
        regex_pattern (str): The regex pattern to use for extracting digits from each line.

    Returns:
        int: Total calibration value.
    """
    document = np.loadtxt(input_file_name, dtype=str)

    total_calibration_value = 0
    for line in document:
        digits = re.findall(regex_pattern, line)
        total_calibration_value += get_calibration_value(digits)

    return total_calibration_value


def main(
    input_file_name: str = typer.Argument(
        "years/2023/inputs/input1.txt", help="Input file"
    ),
):
    part_one = calculate_total_calibration_value(input_file_name, REGEX_NUMBERS)
    part_two = calculate_total_calibration_value(input_file_name, REGEX_NUMBERS_WORDS)

    print(f"Total calibration value for part 1: {part_one}")
    print(f"Total calibration value for part 2: {part_two}")


if __name__ == "__main__":
    typer.run(main)
