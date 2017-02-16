# This puts all the information about the players together
class Player(object):
	
	def __init__(self, name, age, goals):
		self.name = name
		self.age = age
		self.goals = goals 
	
	def getstats(self):
		summary = "Name: " + self.name + "\n"
    		summary = summary + "Age: " + self.age + "\n"
    		summary = summary + "Goals: " + self.goals + "\n"
		return summary

#This creates an empty list so the user can add players later on	
myPlayers = []	
#this is used to create a while statement later on in my code
sport = "soccer"

# This while statement is used so that the user will be asked their options throughout the whole program
while sport == 'soccer':
	print("What do you want to do?")
	print("(1) Add Player")
	print("(2) Print Players")

#This asks the user for what choice they want to choose
	response = input()

# this will run if the user chooses choice 1, which will ask the user for their player's information and then add all the info together
	if response == 1:
		print("OK, what is the player's name?")
		playerName = raw_input()
		print("What is the player's age?")
		playerAge = raw_input()
		print("How many goals did the player score?")
		playerGoals = raw_input()
		my_player = (Player(playerName, playerAge, playerGoals))
		myPlayers.append(my_player)
		print("Your player is now added to the team!")
# This will run if the user chooses choice 2 which will display the list of all the players by calling the getstats method
	elif response == 2:
		print("Here's a list of the players: ")
		for player in myPlayers:
			print(player.getstats())
