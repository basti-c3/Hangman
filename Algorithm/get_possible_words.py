from useful_things import *
import re
import random


def get_possible_words(already_guessed_word: str, word_set: set):
    if len(word_set) == 0:
        raise Exception('There are no possible words left anymore. Should be impossible')
    random_word_from_set = random.sample(word_set, 1)
    if len(already_guessed_word) != len(random_word_from_set):
        raise Exception(f'The length of the word {random_word_from_set} does not equal the length'
                        f'of the searched word {already_guessed_word}')
    if '_' not in already_guessed_word:
        print('The word has nothing left to guess')
        return set(already_guessed_word)
    alphabet_regex = '[A-Z]'
    regex = already_guessed_word.replace('_', alphabet_regex)
    return set(filter(lambda word: _word_contains_regex(word, regex), word_set))


def _word_contains_regex(word: str, regex: str):
    print(word, regex, bool(re.match(regex, word)))
    return bool(re.match(regex, word))

