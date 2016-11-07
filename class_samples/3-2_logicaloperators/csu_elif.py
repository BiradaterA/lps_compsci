print("Do you want to apply for Richmond State?")
print("How many miles do you live from Richmond?")
miles = int(raw_input())

print("What is your GPA?")
GPA = float(raw_input())

print("What is your ACT score?")
ACT = int(raw_input())

if miles <= 30 and GPA >= 2.0 and ACT >= 0:
	print("Congratulations! You have been admitted to Richmond State!")
#elif miles > 30 and GPA < 2.5:
#	print("Sorry, you have not been admitted to Richmond State.")
elif miles < 30 and GPA < 2.0 and ACT >= 0:
	print("Sorry, you have not been admitted to Richmond State.")
elif miles > 30 and GPA >= 2.5 and ACT >= 18:
	print("Congratulations! You have been admitted to Richmond State!")
elif miles > 30 and GPA < 2.5 or ACT < 18:
	print("Sorry, you have not been admitted to Richmond State.") 

