import sys, math

file = open("input/day2input.txt", "r")
checksumLines = file.read().split("\n")

result = 0
for line in checksumLines:
	numbers = line.split()
	print("Line ", line)
	#check every number with every other in the list
	for number in numbers:
		number = int(number)
		for number2 in numbers:
			number2 = int(number2)
			if number != number2:

				#if the numbers have a zero-remainder division, add their result
				if number % number2 == 0:
					result += number / number2
					print("Number: ", number, "Number 2: ", number2)

print("TOTAL: ", result)