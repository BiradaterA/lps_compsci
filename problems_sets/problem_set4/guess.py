# put this line at the start of your program
# to make the functions of this package available
import random
# creates a random number between 1 and 1000
myNum = random.randint(1, 1000)

print("I'm thinking of a number between 1 and 1000, can you guess the number?")

choice = 0
while choice < myNum:
	guess = int(raw_input())
	if guess > myNum:
		print("Sorry, your too high! Try guessing a lower number!")
	elif guess == myNum:
                print("Yay, you guessed the lucky number! Good Job!")
		choice = 1001
	elif guess < myNum:
		print("Sorry, your too low! Try guessing a larger number!")

