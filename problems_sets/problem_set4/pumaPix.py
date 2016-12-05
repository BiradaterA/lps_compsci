print("Welcome to PumaPix!")
print("Enter your 5 favorite shows: ")
print("Enter a show name: ")
first = raw_input()
print("Enter a show name: ")
second = raw_input()
print("Enter a show name: ")
third = raw_input()
print("Enter a show name: ")
fourth = raw_input()
print("Enter a show name: ")
fifth = raw_input()
print("Okay, here's what you entered: ")
shows = [first, second, third, fourth, fifth]
print shows

print("We've added a couple of important ones: ")
more = ['Luther', 'Containment']
all = shows + more
number = int(1)
all.sort()
for show in all:
	print(str(number) + ". " + show)
	number = number + 1
