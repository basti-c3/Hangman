from useful_things import *
import re


def get_possible_words(already_guessed_word: str, word_set: set):
    if '_' not in already_guessed_word:
        print('The word has nothing left to guess')
    alphabet_regex = '[A-Z]'
    regex = already_guessed_word.replace('_', alphabet_regex)
    return set(filter(lambda word: _word_contains_regex(word, regex), word_set))


def _word_contains_regex(word: str, regex: str):
    print(word, regex, bool(re.match(regex, word)))
    return bool(re.match(regex, word))

