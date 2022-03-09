from data.useful_things import *
from data.create_word_list import read_and_return_hangman_word_set, write_words_in_file
from data.add_to_word_file import add_words_to_file


def main():
    new_words_file = "data/deu_news_2020_300K-words.txt"
    words_stored_file = 'data/words.txt'
    add_words_to_file(new_words_file, word_file=words_stored_file)


if __name__ == '__main__':
    main()
