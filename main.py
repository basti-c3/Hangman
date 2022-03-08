from data.create_word_list import read_and_return_hangman_word_set, write_words_in_file


def main():
    file = "data/deu_news_2021_10K-words.txt"
    word_set = read_and_return_hangman_word_set(file)
    write_words_in_file(word_set)


if __name__ == '__main__':
    main()
