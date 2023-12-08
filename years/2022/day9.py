"""Day 9: Rope Bridge."""
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import numpy as np
import typer
from aoc.utils import read_split_data


def plot_head_tail_positions(
    x_head_path: list, y_head_path: list, x_tail_path: list, y_tail_path: list
) -> None:
    """Plot all the head and tail positions.

    Args:
        x_head_path (list): X coordinates of the head
        y_head_path (list): Y coordinates of the head
        x_tail_path (list): X coordinates of the tail
        y_tail_path (list): Y coordinates of the tail
    """
    plt.plot(x_head_path, y_head_path, color="green", label="Head")
    plt.plot(x_tail_path, y_tail_path, color="red", label="Tail")
    plt.xticks(np.arange(0, 6))
    plt.yticks(np.arange(0, 5))
    plt.legend()
    plt.grid()
    plt.show()


def move_in_direction(direction: str, x_head: int, y_head: int) -> tuple:
    """Move the X and the Y based on the direction.

    Args:
        direction (str): Direction (R, L, U, D)
        x_head (int): X coordinates of the head
        y_head (int): Y coordinates of the head

    Returns:
        tuple: New X and Y coordinate
    """
    if direction == "R":
        x_head += 1
    if direction == "L":
        x_head -= 1
    if direction == "U":
        y_head += 1
    if direction == "D":
        y_head -= 1

    return (x_head, y_head)


def moves(data: pd.DataFrame) -> list:
    """Move the tail and head based on the positions and steps.

    Args:
        data (pd.DataFrame): Containing the direction and steps

    Returns:
        lists: The coordinates of the X, Y of the head and tail
    """
    x_head_path, y_head_path = [0], [0]
    x_tail_path, y_tail_path = [0], [0]

    for row in data:
        direction, steps_str = row.split(" ")
        steps = int(steps_str)

        for _ in range(0, steps):
            x_head, y_head = x_head_path[-1], y_head_path[-1]
            x_tail, y_tail = x_tail_path[-1], y_tail_path[-1]

            x_head, y_head = move_in_direction(direction, x_head, y_head)
            x_head_path.append(x_head)
            y_head_path.append(y_head)

            distance = np.sqrt(
                np.power(x_head - x_tail, 2) + np.power(y_head - y_tail, 2)
            )
            if distance >= 2:  # move tail
                [x_tail, y_tail] = [
                    x_tail + np.sign(x_head - x_tail),
                    y_tail + np.sign(y_head - y_tail),
                ]

            x_tail_path.append(x_tail)
            y_tail_path.append(y_tail)

    return x_head_path, y_head_path, x_tail_path, y_tail_path


def main(visualize: bool = typer.Argument(False)):
    """Solve part 1."""
    data = read_split_data("years/2022/inputs/input9.txt")
    x_head_path, y_head_path, x_tail_path, y_tail_path = moves(data)
    positions_tail = len(Counter(zip(x_tail_path, y_tail_path)))

    if visualize:
        plot_head_tail_positions(x_head_path, y_head_path, x_tail_path, y_tail_path)

    print(f"Part 1: {positions_tail} \n")


if __name__ == "__main__":
    typer.run(main)
