# This is the introduction of the program and tells the user that they will need to put their favorite 5 shows
print("Welcome to PumaPix!")
print("Enter your 5 favorite shows: ")
# This line will help make my while loop run
choice = 0
# This is my list that I will be using to add all the user's shows altogether
shows = []
# This while loop will run as long as my choice is < 5 which I have assigned it to 0
while choice < 5:
	print("Enter a show name: ")
# This will put the user's shows as the variable first
	first = raw_input()
# This will add the variable first to the shows list
	shows.append(first)
# This will increment choice so that way this loop will only run five times allowing the user to input 5 shows
	choice = choice + 1
# This print statement will tell the user what I will be doing next which is showing them their list
print("Okay, here's what you entered: ")
# This will print all the shows the user entered in one list
print shows
# I'm telling the user that I added some more shows
print("We've added a couple of important ones: ")
# I created another list with two more shows that I feel like the user didn't add but should
more = ['Luther', 'Containment']
# I combined their shows list with my show list all together under a new list called all
all = shows + more
# I set the variable number to 1 that way I can use this when I start my numbering process
number = int(1)
# I sorted my all list so that way it will be in alphabetical order
all.sort()
# This for command will create a loop that completes these sets of commands for each term in the all list
for show in all:
# This will print the number 1 with a period with the show
	print(str(number) + ". " + show)
# This line will make sure that the numbers are incrementing as it goes through the whole list
	number = number + 1
