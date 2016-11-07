# number 2
# Ask the user their age
print("How old are you?")
# Creates the variable age to be the users age which also made it an int
age = int(input())

# This asks how tall is the user in inches
print("How many inches tall are you?")
#This assigns the variable height to be the users height in inches as an int
height = int(input())

#This displays the hooray statement in the user is older than 10 and taller than 50 inches but if one of those is false, than the sorry statement gets displayed.
if age > 10 and height > 50:
	print("Hooray! You're old enough and tall enough to ride.")
else:
	print("Sorry, you can't ride.")
