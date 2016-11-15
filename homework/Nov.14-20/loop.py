print("What is your favorite number?")
number = int(raw_input())

while number != 14:
	print("I don't like that number, try again")
	number = int(raw_input())
	if number == 14:
		print("Good choice, I love the number 14!")
