# -*- coding: utf-8 -*-
"""
This is my practise_001: number 25
"""


def break_words(stuff):
    """This function will break up words for us."""
    return stuff.split(" ")


def sort_words(words):
    """This function will sorts the words"""
    return sorted(words)


def print_first_word(words):
    """Print the first word after popping it off."""
    print words.pop(0)


def print_last_word(words):
    """Print the last word after popping it off."""
    print words.pop(-1)


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


if __name__ == "__main__":
    sentence = "All good things come to those who wait."
    words = break_words(sentence)
    print words
    sorted_words = sort_words(words)
    print sorted_words
    print_first_word(words)
    print_last_word(words)
    sorted_words = sort_sentence(sentence)
    print sorted_words
    print_first_and_last(sentence)
    print_first_and_last_sorted(sentence)






