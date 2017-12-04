import sys, math


file = open("day2input.txt", "r")
checksumLines = file.read().split("\n")


result = 0
for line in checksumLines:
	numbers = line.split()
	print("Line ", line)
	currentMin = math.inf
	currentMax = -1
	for number in numbers:
		currentMin = int(number) if int(number) < currentMin  else currentMin
		currentMax = int(number) if int(number) > currentMax  else currentMax
	print("Max: ", currentMax)
	print("Min: ", currentMin)
	result += currentMax - currentMin
	print("Result: ", result)

print("TOTAL: ", result)





