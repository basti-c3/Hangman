from useful_things import *
import re


def get_words_of_given_length(word_length: int, word_list: list[str]):
    return list(filter(lambda word: len(word) == word_length, word_list))


def get_possible_words_considering_dashes(hangman_word: str, word_list: list[str]):
    dash_indices = set(substr.start() for substr in re.finditer('-', hangman_word))

    return list(filter(
        lambda word: dash_indices == set(substr.start() for substr in re.finditer('-', word)),
        word_list)
    )


def get_possible_words(already_guessed_letters: list[str], already_guessed_word: str, word_list: list[str]):
    if len(word_list) == 0:
        raise Exception('There are no possible words left anymore. Should be impossible')

    if '_' not in already_guessed_word:
        return [already_guessed_word]

    possible_letters = set(Hangman_Alphabet).difference(already_guessed_letters)
    possible_letters_regex = '[' + ','.join(possible_letters) + ']'
    word_with_regex_at_blanks = already_guessed_word.replace('_', possible_letters_regex)

    return list(filter(lambda word: _contains_regex(word, word_with_regex_at_blanks), word_list))


def _contains_regex(word: str, regex: str):
    return bool(re.match(regex, word))
