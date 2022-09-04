""" 
Time to solve, code and arrange: 30 minutes
"""
import sys
from re import search
from typing import List, Optional, Tuple


def search_in_strings(
    searching_words: List[str], sentences: List[Optional[str]] = [], filename: str = ""
) -> Tuple[List[str], List[str]]:
    """
    Searching given words in given strings or file.
    Args:
        searching_words (List[str]): List of words to search
        sentences (List[Optional[str]], optional): List of sentences in which we need to find the seeking words
        filename (str, optional): Instead of defining sentences we can defining text file in with we have sentences to search in.

    Returns:
        Tuple[List[str], List[str]]: Two lists with sentences, in firs we have sentences that contained sentences with seeking words and in second without it.
    """
    if filename:
        with open(filename) as file:
            sentences = file.read().split("\n")
    correct_sentences = []
    wrong_sentences = []
    re_pattern = "['\",.\{\}\[\]\(\)-_?!;:\n]*"
    re_searching_words = "{0}{1}{0}".format(re_pattern, ("|".join(searching_words)))
    i = 0
    for sentence in sentences:
        i += 1
        if search(re_searching_words, sentence.lower()):
            correct_sentences.append(sentence)
        else:
            wrong_sentences.append(" ".join([str(i), sentence]))
    return correct_sentences, wrong_sentences


def main() -> None:
    print("Input words to search with whitespace to separate your words:")
    searching_words = input(">>> ").lower().split(" ")
    sentences = []
    file_name = ""
    print("Input your sentences with Enter to separate your sentences:")
    print(
        'When you are finished adding new sentences "!END"\n'
        'If you want to read it from file instead type "!FILE" and then type file name '
        "(file need to be in same directory as you when you running main.py or you need to provide full path to the file)"
    )
    while True:
        sentence = input(">>> ")
        if sentence == "!END":
            break
        if sentence == "!FILE":
            file_name = input("File name: ")
            break
        sentences.append(sentence)

    print(searching_words)
    print(sentences)
    if file_name:
        correct_sentences, wrong_sentences = search_in_strings(
            searching_words, filename=file_name
        )
    else:
        correct_sentences, wrong_sentences = search_in_strings(
            searching_words, sentences
        )
    print("Sentence(s) that contain seeking words:")
    print("\n".join(correct_sentences))
    print("\nSentence(s) that don't contain seeking words:")
    print("\n".join(wrong_sentences), file=sys.stderr)


if __name__ == "__main__":
    main()
