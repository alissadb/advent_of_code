"""
Day 8: Haunted Wasteland
https://adventofcode.com/2023/day/8
"""
import itertools
import math

from pydantic import BaseModel
from rich import print

from aoc.utils import read_data


class Node(BaseModel):
    name: str
    left: str
    right: str


def get_data(file_name: str) -> tuple[list[str], dict[list[Node]]]:
    data = read_data(file_name)

    instructions, network_data = data.split("\n\n")
    network = network_data.split("\n")

    network_dict = {}
    for nodes in network:
        start, left_right = nodes.split(" = ")
        left, right = left_right.strip("()").split(", ")

        network_dict[start] = Node(name=start, left=left, right=right)

    return instructions, network_dict


def find_number_of_steps(
    nodes: list[Node],
    instructions: list[str],
    network_dict: dict[list[Node]],
    ends_with_condition: str,
) -> list[int]:
    steps = []
    for node in nodes:
        steps_node = 0
        for instruction in itertools.cycle(instructions):
            steps_node += 1

            if instruction == "L":
                node = network_dict[node].left
            if instruction == "R":
                node = network_dict[node].right

            if node.endswith(ends_with_condition):
                steps.append(steps_node)
                break

    return steps


if __name__ == "__main__":
    instructions, network_dict = get_data("years/2023/inputs/input8.txt")

    # Part 1
    start_node = "AAA"
    step = find_number_of_steps(
        [start_node], instructions, network_dict, ends_with_condition="ZZZ"
    )

    # Part 2
    start_nodes = [node for node in network_dict.keys() if node.endswith("A")]
    steps = find_number_of_steps(
        start_nodes, instructions, network_dict, ends_with_condition="Z"
    )
    steps_lcm = math.lcm(*steps)

    print(
        f"""
        --- Day 8: Haunted Wasteland :ghost: ---
            Part one: {step[0]}
            Part two: {steps_lcm}
        """
    )
