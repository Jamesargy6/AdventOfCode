import sys

file = open("../inputs/day5input.txt", "r")

stepList = file.read().split("\n")

counter = 0
currentIndex = 0
newValue = 0
print(stepList)
while currentIndex >= 0 and currentIndex < len(stepList):
	counter += 1
	#print("Counter: ", counter)

	#add the current value to the current index. if it is out of the bounds of hte list, return the counter.
	prevIndex = currentIndex
	currentIndex += int(stepList[currentIndex])
	if int(stepList[prevIndex]) >= 3:
		stepList[prevIndex] = int(stepList[prevIndex]) - 1
	else:
		stepList[prevIndex] = int(stepList[prevIndex]) + 1
	#print("new index: ", currentIndex)
	#print(stepList)


print("Counter: ", counter)
print("new index: ", currentIndex)

