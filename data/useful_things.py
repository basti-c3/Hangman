from datetime import datetime

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'ß', 'ä', 'ö', 'ü']


def write_words_in_file(word_set, file):
    word_file = open(file, 'w')
    for word in word_set:
        word_file.write(word + ';')
