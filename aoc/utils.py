"""Helpers for reading the data."""
import time


def time_function(func):
    def wrap_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"The function took {end-start} seconds")
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
