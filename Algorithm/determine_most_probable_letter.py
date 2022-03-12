from useful_things import *


def determine_most_probable_letter(already_guessed_word: str, word_list: list[str]):
    local_alphabet = alphabet.copy()
    joined_string = ''.join(word_list)
    for already_guessed_letter in already_guessed_word:
        if already_guessed_letter in local_alphabet:  # Not _ and not -
            local_alphabet.remove(already_guessed_letter)
            joined_string = joined_string.replace(already_guessed_letter, '')

    frequency_distribution = {letter: joined_string.count(letter) for letter in local_alphabet}
    most_probable_letters_sorted = sorted(frequency_distribution.keys(),
                                          key=lambda letter: frequency_distribution[letter],
                                          reverse=True)
    print(frequency_distribution)
    most_probable_letter = most_probable_letters_sorted[0]
    print(
        f'Der nächste wahrscheinlichste Buchstabe ist {most_probable_letter} with a total of '
        f'{frequency_distribution[most_probable_letter]} appearances.')
    return most_probable_letter
