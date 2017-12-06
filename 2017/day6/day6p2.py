import sys

file = open("../inputs/day6input.txt", "r")

bankArray = file.read().split()
bankArray = list(map(int, bankArray))

configurations = []
counter = 0
configurations.append(bankArray)

while True:
	#copy the array into a new object
	newArray = bankArray[:]
	#determine the current max value and its index
	currentValue = max(newArray)
	currentIndex = newArray.index(currentValue) # tie won by smallest index

	#"redistribute" the maximum through the array
	newArray[currentIndex] = 0
	while currentValue > 0:
		currentIndex = (currentIndex + 1)%len(newArray)
		newArray[currentIndex] += 1
		currentValue -= 1

	counter += 1
	#if we've seen this configuration before, return the size of the loop
	for config in configurations:
		if newArray == config:
			print("Result: ",counter - configurations.index(newArray))
			exit()
	#otherwise add it to the list
	configurations.append(newArray)
	bankArray = newArray

