from useful_things import *


def determine_most_probable_letter(word_list: list[str], already_guessed_letters: list[str]):
    local_alphabet = Hangman_Alphabet.copy()
    joined_string = ''.join(word_list)
    for already_guessed_letter in already_guessed_letters:
        if already_guessed_letter in local_alphabet:  # Not _ and not -
            local_alphabet.remove(already_guessed_letter)
            joined_string = joined_string.replace(already_guessed_letter, '')

    frequency_distribution = {letter: joined_string.count(letter) for letter in local_alphabet}
    most_probable_letters_sorted = sorted(frequency_distribution.keys(),
                                          key=lambda letter: frequency_distribution[letter],
                                          reverse=True)
    return most_probable_letters_sorted[0]
