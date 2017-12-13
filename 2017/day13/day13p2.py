import sys
import array
import copy

file = open("../inputs/day13input.txt", "r")
directions = file.read().split("\n")

layers = {}

#map each location to the length of the array at that location
for d in directions:
	dSplit = d.split(":")
	leftSide = int(dSplit[0])
	rightSide = int(dSplit[1].strip())
	layers[leftSide] = rightSide

delay = 0
cont = True

#iterate until we find the correct delay
while cont:
	seen = False
	#for each layer, see if the scanner will be at index 0 after delay + y steps, where y is the location of the layer
	for y in layers:
		if not seen:
			if (delay + y)%(2*layers[y]-2) == 0:
				delay += 1
				seen = True
	cont = seen

print(delay)


