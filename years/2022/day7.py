"""Day 7: No Space Left On Device."""

from aoc.utils import read_split_data


class Directory:
    def __init__(self, parent: str, name: str):
        self.parent = parent
        self.name = name
        self.size = 0
        self.total_size = 0
        self.files = []
        self.sub_directories = []

    def add_file(self, file: str, size: int) -> None:
        """Add a file and the size of the file.

        Args:
            file (str): File name
            size (int): Size of the file
        """
        self.files.append(file)
        self.size += int(size)

    def add_sub_directory(self, sub_directory_name: str) -> None:
        """Add subdirectory.

        Args:
            sub_directory_name (str): Add name of the subdirectory
        """
        self.sub_directories.append(sub_directory_name)

    def _get_all_sub_directories(self, directories: dict) -> list:
        """Get all the sub directories.

        Args:
            directories (dict): Dictionary with all the directories

        Returns:
            list: All the sub directories
        """
        sub_dirs = []
        for sub_dir in self.sub_directories:
            sub_dirs += directories[sub_dir].sub_directories
        return sub_dirs

    def get_total_size(self, directories: dict) -> int:
        """Retrieve the total size of the directory.

        Args:
            directories (dict): Dictionary with all the directories

        Returns:
            int: Size of this directory and the sub directories
        """
        self.sub_directories = self._get_all_sub_directories(directories)

        self.total_size = self.size

        for directory in directories:
            if (
                self.name in directories[directory].name
                and not self.name == directories[directory].name
            ):
                self.total_size += directories[directory].size

        return self.total_size


def get_directories(puzzle_input: str) -> dict[Directory]:
    """Retrieve directories from the input.

    Args:
        puzzle_input (str): Input of the commands of the terminal

    Returns:
        dict: Dictionary with all the directories
    """
    name = ""
    directories = {}

    # Initialize root directory
    name = "/"
    directories[name] = Directory(name, "/")

    for line in puzzle_input[1:]:
        # Add directory if it doesn't exist' and use that as the current directory
        if "$ cd" in line:
            # Go to parent directory
            if line == "$ cd ..":
                name = directories[name].parent

            # Go to child directory
            elif line != "$ cd ..":
                _, _, sub_directory_name = line.split(" ")

                new_directory_name = (
                    f"{name}/{sub_directory_name}"
                    if name != "/"
                    else f"{name}{sub_directory_name}"
                )
                if directories.get(new_directory_name) is None:
                    directory = Directory(name, new_directory_name)
                    directories[new_directory_name] = directory

                name = new_directory_name

        # Add subdirectory
        elif "dir" in line:
            sub_directory_name = line.split(" ")[1]
            new_directory_name = (
                f"{name}/{sub_directory_name}"
                if name != "/"
                else f"{name}{sub_directory_name}"
            )

            # Add new subdir
            directories[name].add_sub_directory(new_directory_name)

        # Add files to the directory
        elif "$ ls" not in line:  # then <value> <file_name>
            size, file = line.split(" ")
            directories[name].add_file(file, size)

    return directories


def total_sum_directories_smaller_than(directories: dict, max_size=100000) -> int:
    """Total sum of the directories smaller than n.

    Args:
        directories (dict): All the directories and their properties
        max_size (int, optional): Max size of a directory. Defaults to 100000.

    Returns:
        int: Sum of the directories smaller than n
    """
    total = 0

    for name in directories:
        directory = directories[name]
        total_size = directory.get_total_size(directories)

        if total_size < max_size:
            total += total_size

    return total


def smallest_size_directory_to_delete(
    directories: dict[Directory], size_filesystem: int, free_space_needed: int
) -> int:
    """Get the smalles directory size to delete.

    Args:
        directories (dict[Directory]): All the directories and their properties
        size_filesystem (int): Size of the filesystem
        free_space_needed (int): Free space needed for the update

    Returns:
        int: Smallest directory size
    """
    total_outermost_directory = directories["/"].get_total_size(directories)
    clean_up_space = free_space_needed - (size_filesystem - total_outermost_directory)

    sizes = []
    for directory_name in directories:
        directory = directories[directory_name]
        total_size = directory.get_total_size(directories)

        if total_size > clean_up_space:
            sizes.append(total_size)

    return min(sizes)


def main():
    """Solve part 1 and part 2."""
    puzzle_input = read_split_data("years/2022/inputs/input7.txt")
    directories = get_directories(puzzle_input)

    part_1 = total_sum_directories_smaller_than(directories)
    print(
        f"What is the sum of the total sizes of those directories? \nPart 1: {part_1} \n"
    )

    part_2 = smallest_size_directory_to_delete(
        directories, size_filesystem=70000000, free_space_needed=30000000
    )
    print(f"What is the total size of that directory? \nPart 2: {part_2}")


if __name__ == "__main__":
    main()
