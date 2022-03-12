from useful_things import *
from data.create_word_list import read_and_return_hangman_word_set


def add_words_to_file(new_words_file, word_file=''):
    if word_file != '':
        file = open(word_file)
        word_set = set(file.readline().split(';')[0:-1])
        file.close()
    else:
        word_set = set()
        word_file = 'data/words.txt'

    new_words_set = read_and_return_hangman_word_set(new_words_file)
    all_words_set = word_set.union(new_words_set)
    print('How many words we had before: ', len(word_set))
    print('How many words were in the file: ', len(new_words_set))
    print('How many words we have now: ', len(all_words_set))
    if len(all_words_set) != 0:
        write_words_in_file(all_words_set, word_file)
