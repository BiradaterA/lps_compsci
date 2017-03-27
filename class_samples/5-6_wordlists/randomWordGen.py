# Produces a different random word every time

# Allows the program to use the random function
import random

# Opens the words.txt file and adds each line to the list
wordsFile = open('words.txt', 'r')
wordsList = []

myWord = wordsFile.readline()
while myWord != '':

        wordsList.append(myWord)
        myWord = wordsFile.readline()

# This creates a variable to a random word in the list
randomWord = random.choice(wordsList)

#This prints the random word
print("Here is a random word:")
print(randomWord)
