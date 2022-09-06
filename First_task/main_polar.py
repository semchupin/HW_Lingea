# Time to solve, code and arrange: 15 minutes
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from re import search
from turtle import position
from typing import Tuple

# re_pattern contain some word wrappers that can be found it regular text
re_pattern = "['\",.\{\}\[\]\(\)-_?!;:\n]*"
# add regex to searching words
searching_words = r"{0}{1}{0}".format(re_pattern, ("|".join(sys.argv[-1:])))


def search_in_line(position_and_line: Tuple[int, str]) -> None:
    """
    Searching given words in string from stdin.
    Args:
        position_and_line (Tuple[int, str]): Line from stdin in which we need to find searching words
    """
    global searching_words
    position, line = position_and_line
    if search(searching_words, line.lower()):
        print(line)
    else:
        print(" ".join([str(position), line]), file=sys.stderr)


def main() -> None:
    # running analyzing of the stdin with Polars Library
    with ThreadPoolExecutor() as executor:
        executor.map(search_in_line, enumerate(sys.stdin))


if __name__ == "__main__":
    main()
