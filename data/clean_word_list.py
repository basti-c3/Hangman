"""The word list might contain errors. Here we eliminate them"""
file = "deu_news_2021_10K-words.txt"


def readAndReturnWordList(file):
    wordList = []
    for line in open(file):
        lineAsList = line.split(' ')
        if len(lineAsList) != 3:
            pass
        else:
            word = lineAsList[1]
            wordList.append(word)
    return wordList
