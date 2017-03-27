# Produces a different random word every time

import random

wordsFile = open('words.txt', 'r')
wordsList = []

myWord = wordsFile.readline()
while myWord != '':

        wordsList.append(myWord)
        myWord = wordsFile.readline()

randomWord = random.choice(wordsList)

print("Here is a random word:")
print(randomWord)
