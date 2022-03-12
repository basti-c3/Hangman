from datetime import datetime
import random

Hangman_Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
allowed_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z', 'ß', 'ä', 'ö', 'ü']


def write_words_in_file(word_set, file):
    word_file = open(file, 'w')
    for word in word_set:
        word_file.write(word + ';')
    word_file.close()


def get_words_from_word_file(file: str):
    file = open(file)
    word_set = set(file.readline().split(';')[0:-1])
    file.close()
    return list(word_set)


def put_in_next_letter(hangman_word, already_guessed_word, next_letter):
    for index in range(len(hangman_word)):
        if hangman_word[index] == next_letter:
            already_guessed_word = already_guessed_word[:index] + next_letter + already_guessed_word[index + 1:]
    return already_guessed_word
