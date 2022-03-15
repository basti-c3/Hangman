from Weights.initial_weights import get_initial_weights
from Weights.weight_update import update_weights
from Game.play_hangman import play_all_words_with_given_length
from useful_things import *


def iterate_hangman_with_weight_updates(max_iterations: int, max_wrong_guesses: int, hangman_word_length: int,
                                        word_list: list[str]):
    # Currently just giving every word the weight 1.0 - Attention: value has to be float!
    current_word_weights = get_initial_weights(word_list=word_list)
    step_length = 10
    _next_step_length = lambda previous_step: previous_step / 1.5
    iteration = 0
    while iteration < max_iterations:
        wrong_guess_dict = play_all_words_with_given_length(
            hangman_word_length=hangman_word_length,
            word_list=word_list,
            max_wrong_guesses=max_wrong_guesses,
            word_weights=current_word_weights,
        )
        current_word_weights = update_weights(
            word_weights=current_word_weights,
            wrong_guess_dict=wrong_guess_dict,
            step_length=step_length,
        )
        step_length = _next_step_length(step_length)
        if step_length < 1.e-6:
            print(f'Nach Iteration {iteration} lohnt sich kein Schritt mehr wegen zu kleiner Schrittlänge. Abbruch')
            break
        iteration += 1

    return current_word_weights
