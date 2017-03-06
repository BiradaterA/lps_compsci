#This open the file and allows it to be read from, walking_file is an object that creates a file
walking_file = open('walking_instructions.txt', 'r')

#This prints out each line from the other file with , duh after each
lineToPrint = walking_file.readline()
while lineToPrint != "":
	print(lineToPrint + ", duh")
	lineToPrint = walking_file.readline()

#This closes the file
walking_file.close()
