print("For what number would you like multiples?")
number = float(raw_input())
factor = int(0)
multiple = factor * number
print(str(factor) + " times " + str(number) + " equals " + str(multiple) + ".")

while multiple < 1000:
	factor = factor + 1
	multiple = factor * number
        print(str(factor) + " times " + str(number) + " equals " + str(multiple) + ".")	
else:
	print("Those are all of the multiples up to 1000! Have a nice day!")
