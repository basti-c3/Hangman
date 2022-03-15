def update_weights(word_weights: dict[str, float], wrong_guess_dict: dict[str, int], step_length: float):
    mean_value_of_wrong_guesses = sum(wrong_guess_dict.values()) / len(wrong_guess_dict.keys())
    print(f'Es ergibt sich ein mittlerer Wert an wrong guesses von {mean_value_of_wrong_guesses}.')

    # Create copy of word_weight.keys() to prevent errors that occur due to changing a dict while iterating over it
    words = list(word_weights.keys())
    for word in words:
        try:
            updated_weight = word_weights[word] + step_length * (wrong_guess_dict[word] - mean_value_of_wrong_guesses)
            word_weights[word] = updated_weight
        except KeyError:
            pass

    return word_weights
