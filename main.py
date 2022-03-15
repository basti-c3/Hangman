from useful_things import *
from data.create_word_list import read_and_return_hangman_word_set, write_words_in_file
from data.add_to_word_file import add_words_to_file
from Algorithm.main_algorithm import *

def main():
    start_time = datetime.now()
    words_stored_file = 'data/words.txt'
    max_wrong_guesses = 9
    hangman_word_length = 2
    # new_words_file = "data/deu_news_2020_300K-words.txt"
    # add_words_to_file(new_words_file, word_file=words_stored_file)

    word_list = get_words_from_word_file(file=words_stored_file)
    hangman_word = random.sample(word_list, 1)[0]

    iterate_hangman_with_weight_updates()

    end_time = datetime.now()
    print('The program took', end_time - start_time, 'time to run through')


if __name__ == '__main__':
    main()
# yeet
