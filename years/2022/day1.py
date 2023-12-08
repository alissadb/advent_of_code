"""Day 1: Calorie Counting."""


def read_data(file_name: str) -> list[list]:
    """Read the data from a given file name.

    Args:
        file_name (str): File name of the file to read

    Returns:
        list[list]: List of lists with the data
    """
    with open(file_name, mode="r", encoding="utf-8") as file_obj:
        puzzle_input = file_obj.read()

    return puzzle_input


def main():
    """Calculate the total calories of the Elf and Elves."""
    elves = read_data("years/2022/inputs/input.txt")

    calories_per_elf = [
        sum([int(calorie) for calorie in elf.split("\n")])
        for elf in elves.split("\n\n")
    ]
    calories_per_elf.sort(reverse=True)

    print(f"Part 1: Most calories per elf: {calories_per_elf[0]}")
    print(
        f"Part 2: Total calories top 3 Elves: {calories_per_elf[0]+calories_per_elf[1]+calories_per_elf[2]}"
    )


if __name__ == "__main__":
    main()
