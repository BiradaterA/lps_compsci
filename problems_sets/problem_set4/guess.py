# put this line at the start of your program
# to make the functions of this package available
import random
# creates a random number between 1 and 1000
myNum = random.randint(1, 1000)

# This tells my user to guess a number between 1 and 1000
print("I'm thinking of a number between 1 and 1000, can you guess the number?")

# Im setiing choice to 0 so I can use it for my while loop and make sure it will always run
choice = 0
# This while statement will always run since choice will always be less than myNum since it is 0 and myNum has to be at least 1
while choice < myNum:
# This assigns the user's guess to the variable guess and I made it an int
	guess = int(raw_input())
# This if statement will run if the users guess is greater than the number (myNum)
	if guess > myNum:
		print("Sorry, your too high! Try guessing a lower number!")
# If the if statement isn't true than this elif will run if the guess is the same number as myNum 
	elif guess == myNum:
                print("Yay, you guessed the lucky number! Good Job!")
# This will stop the loop since 1001 will have to be greater than any number myNum is since the range is from 1 to 1000
		choice = 1001
# This will run if the other two if statements didn't run and if the guess was smaller than myNum
	elif guess < myNum:
		print("Sorry, your too low! Try guessing a larger number!")

