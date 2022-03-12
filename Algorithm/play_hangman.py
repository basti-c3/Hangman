from useful_things import *
import re
from Algorithm.get_possible_words import get_words_of_given_length, get_possible_words, \
    get_possible_words_considering_dashes
from Algorithm.determine_most_probable_letter import determine_most_probable_letter


# Returns wrong guess count
def play_hangman(hangman_word: str, same_length_word_list: list[str], max_wrong_guesses: int):
    word_length = len(hangman_word)
    wrong_guess_count = 0
    right_guess_count = 0
    wrong_guesses = []
    right_guesses = []
    already_guessed_letters = []
    if len(same_length_word_list) == 0:
        raise Exception('No words were found')

    print(f'We selected the word {hangman_word} with word length {word_length}')

    # Get all the words that have the same length as the selected one
    same_length_words = get_possible_words_considering_dashes(hangman_word=hangman_word,
                                                              word_list=same_length_word_list)
    print(f'We have {len(same_length_words)} words of same length as the selected one')
    print(same_length_words)
    possible_words = same_length_words

    if hangman_word not in possible_words:
        raise Exception('The selected word could not be found in the words of same length.')

    # Create the hangman guess '_____-____' with possible dashes staying dashes
    already_guessed_word = re.sub('[A-Z]', '_', hangman_word)

    while '_' in already_guessed_word and wrong_guess_count < max_wrong_guesses and len(possible_words) > 1:
        next_letter = determine_most_probable_letter(word_list=possible_words,
                                                     already_guessed_letters=already_guessed_letters)
        already_guessed_letters.append(next_letter)

        if next_letter in hangman_word:
            right_guesses.append(next_letter)
            right_guess_count += 1
            # Put in the guessed letter at all places
            for index in range(len(hangman_word)):
                if hangman_word[index] == next_letter:
                    already_guessed_word = already_guessed_word[:index] + next_letter + already_guessed_word[index + 1:]

            # Get all possible words of that length and the already guessed letters at the same places
            possible_words = get_possible_words(
                already_guessed_letters=already_guessed_letters,
                already_guessed_word=already_guessed_word,
                word_list=possible_words,
            )
            print(f'The current guess is: {already_guessed_word}')
            print(f'There are {len(possible_words)} possible words left.')
        else:
            wrong_guesses.append(next_letter)
            wrong_guess_count += 1
            possible_words = list(filter(lambda word: next_letter not in word, possible_words))
            print('The letter was wrong')
            print(f'There are {len(possible_words)} possible words left.')

    if wrong_guesses == max_wrong_guesses:
        print(f'The word could not be guessed! There were {wrong_guesses} wrong guesses: {wrong_guesses} and it '
              f'could only be guessed so far: {already_guessed_word}')
    else:
        print(f'The word {possible_words[0]} could be guessed in {right_guess_count} guesses. '
              f'{wrong_guess_count} were wrong: {wrong_guesses}')
    return wrong_guess_count


def play_all_words_with_given_length(hangman_word_length: int, word_list: list[str], max_wrong_guesses: int):
    same_length_word_list = get_words_of_given_length(word_length=hangman_word_length, word_list=word_list)
    print(f'There are {len(same_length_word_list)} words of the given length of {hangman_word_length}')
    weight_dict = {}
    i=0
    for word in same_length_word_list:
        wrong_guess_count = play_hangman(word, same_length_word_list, max_wrong_guesses)
        weight_dict[word] = wrong_guess_count
        print('Iteration ', i)
        i+=1
    mean_value_of_wrong_guesses = sum(weight_dict.values())/len(same_length_word_list)
    print(f'Es ergibt sich ein mittlerer Wert an wrong guesses von {mean_value_of_wrong_guesses}.')
    return weight_dict

