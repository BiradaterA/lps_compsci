# read all the words in words.txt into a list

wordsFile = open('words.txt', 'r')

wordsList = []

myWord = wordsFile.readline()
while myWord != '':
	# as long as there are more words,
	# put the word in the list & read another

	wordsList.append(myWord)
	myWord = wordsFile.readline()

print(wordsList[17406])
