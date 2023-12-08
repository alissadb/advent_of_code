"""Helpers for AOC."""
import functools
from time import perf_counter

import numpy as np


def vectorize(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        vectorized_func = np.vectorize(func)
        return vectorized_func(*args, **kwargs)

    return wrapper


def time_function(func):
    def wrap_func(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        run_time = (perf_counter() - start) * 1000
        print(f"Result: {result} \nRunning time: {run_time:.2f}ms \n")
        return result

    return wrap_func


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


def read_split_data(file_name: str) -> list[list]:
    """Read the data from a given file name.

    Args:
        file_name (str): File name of the file to read

    Returns:
        list[list]: List of lists with the data
    """
    with open(file_name, mode="r", encoding="utf-8") as file_obj:
        puzzle_input = file_obj.read().split("\n")

    return puzzle_input
