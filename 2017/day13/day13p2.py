import sys
import array
import copy

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

delay = 0
cont = True

def iterateScanner():
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


def iterateSingleScanner(y):
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


masterLayers = copy.deepcopy(layers)
print(masterLayers)
while cont:
	if delay%1000 == 0:
		print(delay)	
	for y in layers:
		for x in range(0, delay%(2*len(layers[y])-2)):
			iterateSingleScanner(y)

	seen = False
	for x in range(0,totalLayers+1):
		if not seen:
			if x in layers:
				if layers[x][0] == 1:
						delay += 1
						seen = True
			iterateScanner()
	cont = seen
	layers = copy.deepcopy(masterLayers)

	

print(delay)


