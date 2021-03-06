print("Welcome to Team Manager Deluxe!")
# This puts all the information about the players together
class Player(object):

        def __init__(self, name, age, goals, jerseyNumber, position):
                self.name = name
                self.age = age
                self.goals = goals
		self.jerseyNumber = jerseyNumber
		self.position = position

        def getstats(self):
                summary = "Name: " + self.name + "\n"
                summary = summary + "Age: " + self.age + "\n"
                summary = summary + "Goals: " + self.goals + "\n"
		summary = summary + "Jersey Number: " + self.jerseyNumber + "\n"
		summary = summary + "Position: " + self.position + "\n" 
                return summary

# takes the playerList and the user's desired filename
# writes each Player to file
def saveTeam(playerList, filename):
# open the file
	x = open(filename, "w")
	print(myPlayers)
	for player in myPlayers:
# write to the file
		x.write(player.name + " " + player.age + " " + player.goals + " " + player.jerseyNumber + " " + player.position + " \n")
# close the file
        x.close()

# takes a filename for a file of players
# returns a list of Players
def loadTeam(playerslist, filename):
    # open the file
	x = open(filename, 'r')
    # read each line and create Player from it (use a loop)
 	line = x.readline()
        # split each line into a list of the variables
	while line != "":
        # read each next line
 		peach = line.split(" ")
		playerslist.append(Player(peach[0], peach[1], peach[2], peach[3], peach[4]))
		line = x.readline()
    # close the file
 	x.close()

# This creates an empty list so the user can add players later on        
myPlayers = []
# This is used to create a while statement later on in my code
sport = "soccer"
print("Do you want to start with a new team or open an existing team?")
print("Enter the number of your choice and press Enter.")
print("(1) Start with a new team")
print("(2) Open a file for an existing team")
response = raw_input()

# This will run if the user chooses option 2 which will allow them to open a file
if response == '2':
	print("What's the file name for the existing team?")
	name1 = raw_input()
	loadTeam(myPlayers, name1)

# This while statement is used so that the user will be asked their options throughout the whole program
while sport == 'soccer':

# This will allow the user to add players if they choose option 1
	print("What do you want to do?")
	print("(1) Add Player")
	print("(2) Print Players")
	print("(3) Save your player list to a file")
	print("(0) Leave the program (save first to avoid losing your data!)")

# This asks the user for what choice they want to choose
	response2 = raw_input()

# this will run if the user chooses choice 1, which will ask the user for their player's information and then add all the info together
	if response2 == '1':
		print("OK, what is the player's name?")
		playerName = raw_input()
		print("What is the player's age?")
		playerAge = raw_input()
		print("How many goals did the player score?")
		playerGoals = raw_input()
		print("What is the player's jersey number?")
		playerJersey = raw_input()
		print("What position does the player play?")
		playerPosition = raw_input()
		my_player = (Player(playerName, playerAge, playerGoals, playerJersey, playerPosition))
		myPlayers.append(my_player)
		print("Your player is now added to the team!")

# This will run if the user chooses choice 2 which will display the list of all the players by calling the getstats method
	elif response2 == '2':
		print("Here's a list of the players: ")
		for player in myPlayers:
			print(player.getstats())
# This will run if the user chooses option 3, to save the file
	elif response2 == '3':
		print("What's the filename for your existing team? Enter the whole name, including its .tmd extension")
		name2 = raw_input()
		saveTeam(myPlayers, name2)
# This will run if the user chooses option 0			
	elif response2 == '0':
		sport = 'football'


