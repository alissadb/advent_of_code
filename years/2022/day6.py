"""Day 6: Tuning Trouble."""
from aoc.utils import read_data, time_function


# First solution
@time_function
def find_first_marker_(text: str, n_distinct: int) -> int:
    """Find the first marker of a distinct combination of n_distinct letters.

    Args:
        text (str): Text to search for the first marker
        n_distinct (int, optional): Number of distinct letters to search for

    Returns:
        int: First number where there are n distinct letters
    """
    queue = text[: n_distinct - 1]

    for i, character in enumerate(text[n_distinct - 1 :]):
        if character not in queue:
            if len(queue) < n_distinct:
                queue += character
            if len(set(queue)) == n_distinct:
                return i + n_distinct

        elif character in queue:
            queue += character

        if len(queue) == n_distinct:
            queue = queue[1:]
            

@time_function
def find_first_marker(text: str, n_distinct: int) -> int:
    """Find the first marker of a distinct combination of n_distinct letters.

    Args:
        text (str): Text to search for the first marker
        n_distinct (int, optional): Number of distinct letters to search for

    Returns:
        int: First number where there are n distinct letters
    """
    # Loop through all the subsets of n characters
    for i in range(len(text) - n_distinct):
        # Check when all the letters in the subset are distinct
        if len(set(text[i : (i + n_distinct)])) == n_distinct:
            return i + n_distinct

    # Throws an error when you want to search for more distinct letters than existing in the text
    if n_distinct > len(set(text)):
        raise ValueError(
            "The number of distinct letters should be less than the distinct letters in the text."
        )


def main():

    # Read data
    puzzle_input = read_data("years/2022/inputs/input6.txt")

    # Solutions
    first_4_distinct = find_first_marker(puzzle_input, 4)
    first_14_distinct = find_first_marker(puzzle_input, 14)

    print(f"Part 1: {first_4_distinct}")
    print(f"Part 2: {first_14_distinct}")


if __name__ == "__main__":
    main()
