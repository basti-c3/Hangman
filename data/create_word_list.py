from useful_things import *


def read_and_return_hangman_word_set(file):
    all_words = set()
    for line in open(file):
        first_index_of_word = 0
        line_length = len(line)
        while line[first_index_of_word].lower() not in allowed_characters:
            first_index_of_word += 1
            if first_index_of_word == line_length:
                break
        last_index_of_word = len(line) - 1
        while line[last_index_of_word].lower() not in allowed_characters:
            last_index_of_word -= 1
            if last_index_of_word == 0:
                break
        words = line[first_index_of_word: last_index_of_word + 1].split(' ')
        for word in words:
            if _word_is_clean(word):
                hangman_word = _transform_to_hangman_format(word)
                all_words.add(hangman_word)
    return all_words


def _word_is_clean(word):
    if word == '':
        return False
    for letter in word:
        if letter.lower() not in allowed_characters and letter != "-":
            return False
    return True


def _transform_to_hangman_format(word):
    return word.upper().replace('Ä', 'AE').replace('Ü', 'UE').replace('Ö', 'OE')
