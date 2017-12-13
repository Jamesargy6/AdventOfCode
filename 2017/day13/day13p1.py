import sys
import array

file = open("../inputs/day13input.txt", "r")
directions = file.read().split("\n")

layers = {}
incrementing = {}
totalLayers = 0
for d in directions:
	dSplit = d.split(":")

	leftSide = int(dSplit[0])
	rightSide = int(dSplit[1].strip())

	print("Left side: {0}, Right Side: {1}".format(leftSide, rightSide))

	layers[leftSide] = [0]*rightSide
	layers[leftSide][0] = 1
	totalLayers = leftSide

	incrementing[leftSide] = True
print(layers)

result = 0
for x in range(0,totalLayers+1):
	if x in layers:
		if layers[x][0] == 1:
			print("multiplying {0} and {1}".format(x, len(layers[x])))
			result += x * len(layers[x])


	for y in layers:
		currentIndex = layers[y].index(1)
		if currentIndex == len(layers[y])-1:
			incrementing[y] = False
		elif currentIndex == 0:
			incrementing[y] = True
		print(layers[y])
		layers[y][currentIndex] = 0
		if incrementing[y]:
			currentIndex += 1
		else:
			currentIndex -= 1
		print("New index for layer {0}: {1}".format(y, currentIndex))
		layers[y][currentIndex] = 1
		print(layers[y])

print(result)


