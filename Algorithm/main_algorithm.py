def iterate_hangman_with_weight_updates():

    # Currently just giving every word the weight 1.0 - Attention: value has to be float!
    initial_word_weights = get_initial_weights(word_list=word_list)

    play_all_words_with_given_length(
        hangman_word_length=hangman_word_length,
        word_list=word_list,
        max_wrong_guesses=max_wrong_guesses,
        word_weights=current_word_weights,
    )
    return
