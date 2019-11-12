import sys

file = open("../inputs/day6input.txt", "r")
input = file.read().split("\n")
grid =[[0 for i in range(0,1000)] for j in range(0,1000)]
directions = []


def performDirection(scrub, turnOn, startCoords, endCoords):
	global grid
	startRow = startCoords[0]
	startCol = startCoords[1]
	endRow = endCoords[0]
	endCol = endCoords[1]
	print(startRow, startCol, endRow, endCol)
	for y in range(startRow, endRow+1):
		for x in range(startCol, endCol+1):
			if scrub == False:
					grid[y][x]+=2
			else:
				if turnOn:
					grid[y][x]+=1
				elif grid[y][x] > 0:
					grid[y][x]-=1


for i in input:
	tokens = i.split(" ")
	startCoords = []
	endCoords = []
	#turn on 774,539 through 778,786
	#toggle 341,780 through 861,813
	scrub = False
	turnOn = False
	print(tokens)
	if tokens[0] == "turn":
		scrub = True
		if tokens[1] == "on":
			turnOn = True
		startCoordsStrings = tokens[2].split(",")
		for string in startCoordsStrings:
			startCoords.append(int(string))
		endCoordsStrings = tokens[4].split(",")
		for string in endCoordsStrings:
			endCoords.append(int(string))
	else:
		startCoordsStrings = tokens[1].split(",")
		for string in startCoordsStrings:
			startCoords.append(int(string))
		endCoordsStrings = tokens[3].split(",")
		for string in endCoordsStrings:
			endCoords.append(int(string))

	performDirection(scrub, turnOn, startCoords, endCoords)


count = 0
for row in grid:
	for light in row:
		count += light

print(count)






