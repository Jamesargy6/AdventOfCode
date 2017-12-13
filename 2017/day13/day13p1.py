import sys
import array

file = open("../inputs/day13input.txt", "r")
directions = file.read().split("\n")

layers = {}
incrementing = {}
totalLayers = 0

#map each layer with an initialized array at that location, set with the scanner in the first position
for d in directions:
	dSplit = d.split(":")
	leftSide = int(dSplit[0])
	rightSide = int(dSplit[1].strip())

	layers[leftSide] = [0]*rightSide
	layers[leftSide][0] = 1
	totalLayers = leftSide

	incrementing[leftSide] = True

result = 0
#for every "tick", move the pointer. if the scanner exists at that location, multiply the layer's location by the length of the array at that layer
for x in range(0,totalLayers+1):
	if x in layers:
		if layers[x][0] == 1:
			result += x * len(layers[x])

	#move the scanner in each layer
	for y in layers:
		currentIndex = layers[y].index(1)
		if currentIndex == len(layers[y])-1:
			incrementing[y] = False
		elif currentIndex == 0:
			incrementing[y] = True
		layers[y][currentIndex] = 0
		if incrementing[y]:
			currentIndex += 1
		else:
			currentIndex -= 1
		layers[y][currentIndex] = 1

print(result)


