from useful_things import *
import re
from get_possible_words import get_words_of_given_length, get_possible_words, \
    get_possible_words_considering_dashes
from determine_most_probable_letter import determine_most_probable_letter


# Returns wrong guess count
def play_hangman(hangman_word: str, same_length_word_list: list[str], max_wrong_guesses: int,
                  word_weights: dict[str, float]):
    wrong_guess_count = 0
    already_guessed_letters = []

    # Get all the words that have the same length as the selected one
    same_length_words = get_possible_words_considering_dashes(hangman_word=hangman_word,
                                                              word_list=same_length_word_list)
    possible_words = same_length_words

    # Create the hangman guess '_____-____' with possible dashes staying dashes
    already_guessed_word = re.sub('[A-Z]', '_', hangman_word)

    while '_' in already_guessed_word and wrong_guess_count < max_wrong_guesses and len(possible_words) > 1:
        next_letter = determine_most_probable_letter(
            word_list=possible_words,
            already_guessed_letters=already_guessed_letters,
            word_weights=word_weights,
        )
        already_guessed_letters.append(next_letter)

        if next_letter in hangman_word:
            # Put in the guessed letter at all places
            already_guessed_word = put_in_next_letter(hangman_word, already_guessed_word, next_letter)

            # Get all possible words of that length and the already guessed letters at the same places
            possible_words = get_possible_words(
                already_guessed_letters=already_guessed_letters,
                already_guessed_word=already_guessed_word,
                word_list=possible_words,
            )
        else:
            wrong_guess_count += 1
            possible_words = list(filter(lambda word: next_letter not in word, possible_words))

    return wrong_guess_count


def play_all_words_with_given_length(word_list: list[str], max_wrong_guesses: int,
                                     word_weights: dict[str, float]):
    if len(word_list) == 0:
        raise Exception('No words were found')

    wrong_guess_count_dict = {}
    for word in word_list:
        wrong_guess_count = play_hangman(
            hangman_word=word,
            same_length_word_list=word_list,
            max_wrong_guesses=max_wrong_guesses,
            word_weights=word_weights,
        )
        wrong_guess_count_dict[word] = wrong_guess_count

    return wrong_guess_count_dict
