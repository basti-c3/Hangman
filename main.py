from useful_things import *
from Algorithm.main_algorithm import *


def main():
    start_time = datetime.now()
    words_stored_file = 'data/words.txt'
    max_wrong_guesses = 9
    hangman_word_length = 30
    initial_weight_update_step_length = 10
    max_weight_update_iterations = 20

    # Add Words To Word File
    # from data.create_word_list import read_and_return_hangman_word_set, write_words_in_file
    # from data.add_to_word_file import add_words_to_file
    # new_words_file = "data/deu_news_2020_300K-words.txt"
    # add_words_to_file(new_words_file, word_file=words_stored_file)

    # Play Hangman With One Word
    # from Algorithm.Game.play_hangman import play_hangman
    # hangman_word = random.sample(word_list, 1)[0]
    # other_word_list = get_words_of_given_length_from_word_file(file=words_stored_file, word_length=len(hangman_word)
    # print(play_hangman(hangman_word=hangman_word, same_length_word_list=other_word_list,
    #                     max_wrong_guesses=max_wrong_guesses, word_weights=get_initial_weights(word_list)))

    word_list = get_words_of_given_length_from_word_file(file=words_stored_file, word_length=hangman_word_length)
    print(f'There are {len(word_list)} words of the given length of {hangman_word_length}')

    optimized_word_weights = iterate_hangman_with_weight_updates(
        max_iterations=max_weight_update_iterations,
        initial_step_length=initial_weight_update_step_length,
        max_wrong_guesses=max_wrong_guesses,
        word_list=word_list,
    )
    for word in optimized_word_weights.keys():
        print(word, ': ', optimized_word_weights[word])

    end_time = datetime.now()
    print('The program took', end_time - start_time, 'time to run through')


if __name__ == '__main__':
    main()
    # yeet
