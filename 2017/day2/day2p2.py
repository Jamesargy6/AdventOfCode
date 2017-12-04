import sys, math


file = open("day2input.txt", "r")
checksumLines = file.read().split("\n")


result = 0
for line in checksumLines:
	numbers = line.split()
	print("Line ", line)
	found = False
	for number in numbers:
		number = int(number)
		for number2 in numbers:
			number2 = int(number2)
			if number != number2:
				if number % number2 == 0:
					found = True
					result += number / number2
					print("Number: ", number, "Number 2: ", number2)
					print("Result: ", result)
				if number2 % number == 0:
					found = True
					result += number2 / number
					print("Number: ", number, "Number 2: ", number2)
					print("Result: ", result)
			if found: break
		if found: break


print("TOTAL: ", result)





