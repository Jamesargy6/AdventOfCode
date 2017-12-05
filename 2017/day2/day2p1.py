import sys, math

file = open("../inputs/day2input.txt", "r")
checksumLines = file.read().split("\n")

result = 0
for line in checksumLines:
	numbers = line.split()
	print("Line ", line)
	#ensure that the mins and maxes will always initialize with the first number
	currentMin = math.inf
	currentMax = -1
	for number in numbers:
		#update current min/max
		currentMin = int(number) if int(number) < currentMin  else currentMin
		currentMax = int(number) if int(number) > currentMax  else currentMax
	print("Max: ", currentMax)
	print("Min: ", currentMin)
	#update the check sum with max - min
	result += currentMax - currentMin
	print("Result: ", result)

print("TOTAL: ", result)