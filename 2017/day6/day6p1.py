import sys

file = open("../inputs/day6input.txt", "r")

bankArray = file.read().split()
bankArray = list(map(int, bankArray))

configurations = []
counter = 0
configurations.append(bankArray)
#print("configurations: ", configurations)

while True:
	newArray = bankArray[:]
	currentValue = max(newArray)
	currentIndex = newArray.index(currentValue) # tie won by smallest index

	newArray[currentIndex] = 0
	while currentValue > 0:
		currentIndex = (currentIndex + 1)%len(newArray)
		newArray[currentIndex] += 1
		currentValue -= 1
	counter += 1
	#print("configurations: ", configurations)
	for config in configurations:
		if newArray == config:
			print("Result: ", counter)
			exit()
	configurations.append(newArray)
	bankArray = newArray

