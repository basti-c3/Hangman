from useful_things import *
from data.create_word_list import read_and_return_hangman_word_set, write_words_in_file
from data.add_to_word_file import add_words_to_file
from Algorithm.get_possible_words import get_same_length_words, get_possible_words


def main():
    words_stored_file = 'data/words.txt'
    # new_words_file = "data/deu_news_2020_300K-words.txt"
    # add_words_to_file(new_words_file, word_file=words_stored_file)

    word_list: list = get_words_from_word_file(file=words_stored_file)
    if len(word_list) == 0:
        raise Exception('No words were found')
    hangman_word = 'BEINE'  # random.sample(word_set, 1)[0]
    word_length = len(hangman_word)

    print(f'We selected the word {hangman_word} with word length {word_length}')
    same_length_words = get_same_length_words(word_length=word_length, word_list=word_list)
    print(f'We had {len(word_list)} words before, now only {len(same_length_words)} '
          f'words of same length as the selected one')
    already_guessed_word = '_E_NE'
    possible_words = get_possible_words(already_guessed_word=already_guessed_word, word_list=same_length_words)
    print(possible_words)


if __name__ == '__main__':
    main()
