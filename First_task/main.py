""" 
Time to solve, code and arrange: 30 minutes + 10 minutes to fix
"""
import sys
import time
from re import search
from typing import List


def search_in_stdin(searching_words: List[str]) -> None:
    """
    Searching given words in stdin.
    Args:
        searching_words (List[str]): List of words to search
    """
    for position, line in enumerate(sys.stdin):
        if search(searching_words, line.lower()):
            print(line)
        else:
            print(" ".join([str(position), line]), file=sys.stderr)


def main() -> None:
    # re_pattern contain some word wrappers that can be found it regular text
    re_pattern = "['\",.\{\}\[\]\(\)-_?!;:\n]*"
    # add regex to searching words
    searching_words = "{0}{1}{0}".format(re_pattern, ("|".join(sys.argv[-1:])))
    search_in_stdin(searching_words)


if __name__ == "__main__":
    main()
