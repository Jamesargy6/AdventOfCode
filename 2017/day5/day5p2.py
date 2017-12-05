import sys

file = open("../inputs/day5input.txt", "r")

stepList = file.read().split("\n")
stepList = list(map(int, stepList))

counter = 0
currentIndex = 0
while currentIndex >= 0 and currentIndex < len(stepList):
	counter += 1
	prevIndex = currentIndex
	#add the current value to the current index. 
	currentIndex += stepList[currentIndex]
	#set up the current value for future iterations
	if stepList[prevIndex] >= 3:
		stepList[prevIndex] = stepList[prevIndex] - 1
	else:
		stepList[prevIndex] = stepList[prevIndex] + 1

print("Counter: ", counter)

