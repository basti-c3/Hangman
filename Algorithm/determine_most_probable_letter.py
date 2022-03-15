from useful_things import *


def determine_most_probable_letter(word_list: list[str], already_guessed_letters: list[str],
                                   word_weights: dict[str, float]):
    letter_weight = {}
    for possible_letter in Hangman_Alphabet:
        if possible_letter in already_guessed_letters:
            continue
        letter_weight[possible_letter] = 0
        for word in word_list:
            if possible_letter in word:
                try:
                    letter_weight[possible_letter] += math.exp(word_weights[word])
                except KeyError:
                    print(f"The word {word} has no given weight, maybe something in the code is incorrect?"
                          f"Code ignores word for now")

    letters_sorted_by_weights = sorted(letter_weight.keys(),
                                       key=lambda letter: letter_weight[letter],
                                       reverse=True)
    return letters_sorted_by_weights[0]
