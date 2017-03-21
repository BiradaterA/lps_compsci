# Introduces the program
print("Welcome to Contacts!")
# Creates an empty dictionary and a while loop so the program continuosly runs
contacts = {}
x = 0
while x < 1:

	print("What would you like to do?")
	print("(1) Add a phone number.")
	print("(2) Print the full list of contacts.")
	print("(3) Enter a name to retrieve that contact's phone number.")
	print("(4) Delete a contact.")
	print("(5) Update a contact's number.")
	print("(0) Exit the Contacts app.")
	response = raw_input()

# Will run if the user chooses 1 which will store the user's contacts in the empty dictionary
	if response == '1':
		print("What's the name of your contact?")
		name = raw_input()
		print("What's the phone number of your contact?")
		number = raw_input()
		contacts[name] = number

# Will run if user chooses option 2 which will print the dictionary
	elif response == '2':
		print contacts

# Will run if the user chooses 3 which will choose the number from the dictionary of whomever name they enter
	elif response == '3':
		print("Whose number would you like?")
		person = raw_input()
		print("Okay, here's their number:")
		print(contacts[person])

# Will run if the user chooses 4 which will delete a contact
	elif response == '4':
		print("Which contact do you want to delete?")
		delete = raw_input()
		del(contacts[delete])
		print("Okay, they are now deleted!")

# Will run if user chooses 5 which will allow them to change a contact's number
	elif response == '5':
		print("Which contact's number would you like to update?")
		update = raw_input()
		print("Okay, what is their new number?")
		newNumber = raw_input()
		print("Their number has successfully updated!")
		contacts[update] = newNumber

# This will close the program
	elif response == '0':
		x = 7
