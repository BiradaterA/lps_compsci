print("Welcome to Bree's Land Quest!")
print("Enter the name of your character: ")
name = raw_input()
print("Enter strength (1-10): ")
strength = raw_input()
print("Enter health (1-10): ")
health = raw_input()
print("Enter luck (1-10): ")
luck = raw_input()

if int(strength) + int(health) + int(luck) <= 15:
	print("Hi " + str(name) + "! Your strength is " + str(strength) + ". Your health is " + str(health) + ". Your luck is " + str(luck) + ".")
if int(strength) + int(health) + int(luck) > 15:
	print("You've added too many points, your points will default to 5 points each. Your strength is 5, health is 5, and luck is 5.")
	strength1 = 5
	health1 = 5
	luck1 = 5

print("Now " + name + ", you've come to a fork in the road. Do you want to go right or left? Enter right or left")
choice = raw_input()

if (choice == 'left') or (choice == 'Left'):
	print("As you turn left you come across a lake full of alligators with dragons spitting out fire from the sides.")
	if strength >= 7:
		print("Due to your high strength, you were able to fight and kill all the dragons and alligators! You won!")
	elif health >= 7:
		print("Due to your high health level, although you did get bitten by a few alligators and got hit with some dragons' fire while swimming across the lake, you were able to heal and recover quickly! You won!")
	elif luck >= 7:
		print("Due to your high luck, a fairy magically appeared and was able to transport you across the lake without any harm done! You won!")
	elif (strength or strength1) and (health or health1) and (luck or luck1) < 7:
		print("Sorry, your strength, your health, nor your luck could save you from this situation. You were eaten by alligators and caught on fire by the dragons. You lost!")

if (choice == 'right') or (choice == 'Right'):
	print("As you turn right you come to a forest with packs of wolves and bats flying all around.")
	if strength >= 7:
                print("Due to your high strength, you were able to fight and kill all the wolves and bats! You won!")
        elif health >= 7:
                print("Due to your high health level, although you did get bitten by a few wolves and got hit with a few bats while running through the forest, you were able to recover quickly. You won!")
        elif luck >= 7:
                print("Due to your high luck, the wolves and bats ignored you as if you were invisible, You were able to get through the forest without any mark left on you! You won!")
        elif (strength or strength1) and (health or health1) and (luck or luck1) < 7:
                print("Sorry, your strength, your health, nor your luck could save you from this situation. You were eaten by the pack of wolves and the bats decomposed your body.")
