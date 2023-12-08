"""Day 2: Rock Paper Scissors.

Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
If both players choose the same shape, the round instead ends in a draw.
"""

MOVES = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

MOVES_SCORE = {"rock": 1, "paper": 2, "scissors": 3}


class Player:
    """Class for the user and the elf and operations."""

    def __init__(self, letter):
        self.move = MOVES[letter]

    def get_score(self) -> int:
        """Return the score of the move."""
        return MOVES_SCORE[self.move]

    def get_winning_score(self) -> int:
        """Get the winning score of the move."""
        if self.move == "scissors":
            return 1
        return MOVES_SCORE[self.move] + 1

    def get_losing_score(self) -> int:
        """Get the losing score of the move."""
        if self.move == "rock":
            return 3
        return MOVES_SCORE[self.move] - 1


def calculate_score_part_1(user_choice: list, elf_choice: list) -> int:
    """Calcualte the score based on the shape the elf selects and the outcome of the round.

    Args:
        user_choice (list): Choices of the user (A, B, C)
        elf_choice (list): Choices of the elf (X, Y, Z)

    Returns:
        int: Total score based on the strategy guide
    """
    user = Player(user_choice)
    elf = Player(elf_choice)

    score = elf.get_score()
    if user.move == elf.move:  # Draws
        score += 3
    elif (
        (user.move == "rock" and elf.move == "paper")
        | (user.move == "paper" and elf.move == "scissors")
        | (user.move == "scissors" and elf.move == "rock")
    ):  # Wins
        score += 6

    return score


def calculate_score_part_2(user_choice: list, elf_choice: list) -> int:
    """Calcualte the score based on the shape the user selects and the outcome of the round.

    Args:
        user_choice (list): Choices of the user (A, B, C)
        elf_choice (list): Choices of the elf (X, Y, Z)

    Returns:
        int: Total score based on the strategy guide
    """
    user = Player(user_choice)
    elf = Player(elf_choice)

    score = 0

    if elf.move == "rock":  # Need to lose
        score += 0 + user.get_losing_score()

    elif elf.move == "paper":  # End in a draw
        score += 3 + user.get_score()

    elif elf.move == "scissors":  # Need to win
        score += 6 + user.get_winning_score()

    return score


def read_data(file_name: str) -> list[list]:
    """Read the data from a given file name.

    Args:
        file_name (str): File name of the file to read

    Returns:
        list[list]: List of lists with the data
    """
    with open(file_name, mode="r", encoding="utf-8") as file_obj:
        puzzle_input = file_obj.read().splitlines()

    return puzzle_input


def main():
    """Calculate the total score for part 1 and part 2."""
    # Read data
    puzzle_input = read_data("years/2022/inputs/input2.txt")

    # Extract opponent and
    player_1, player_2 = map(list, zip(*[row.split(" ") for row in puzzle_input]))

    # Scores for the different parts
    total_score_part_1 = sum(map(calculate_score_part_1, player_1, player_2))
    total_score_part_2 = sum(map(calculate_score_part_2, player_1, player_2))

    print(f"Part 1: {total_score_part_1}")
    print(f"Part 2: {total_score_part_2}")


if __name__ == "__main__":
    main()
