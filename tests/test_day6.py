import pytest

from days.day6 import find_first_marker


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
    ],
)
def test_find_first_marker(test_input, expected):

    assert find_first_marker(test_input, 4) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_find_first_marker2(test_input, expected):

    assert find_first_marker(test_input, 14) == expected


def test_find_first_marker_more_distinct_letter():
    with pytest.raises(ValueError):
        find_first_marker("abcd", 10)
