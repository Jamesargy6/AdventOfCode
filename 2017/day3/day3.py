import sys

puzzleInput = 312051


RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

def move(currentLocation, currentDirection):
	return {
		0: 	{'x' : currentLocation['x'] + 1, 'y' : currentLocation['y']},
		1: 	{'x' : currentLocation['x'], 'y' : currentLocation['y'] + 1},
		2: 	{'x' : currentLocation['x'] - 1, 'y' : currentLocation['y']},
		3: 	{'x' : currentLocation['x'], 'y' : currentLocation['y'] - 1}
	}[currentDirection]


def getValueInMatrix(coord):
	try:
			val = spiralMatrix[frozenset(coord.items())]
			return val
	except KeyError:
		return 0

def getCurrentValue(currentLocation):
	#get all the numbers of all the adjacent boxes, an sum them up
	adjacentValues = []
	result = 0
	currentX = currentLocation['x']
	currentY = currentLocation['y']

	result +=  getValueInMatrix({'x' : currentX + 1, 'y' : currentY})
	result += getValueInMatrix({'x' : currentX + 1, 'y' : currentY + 1})
	result += getValueInMatrix({'x' : currentX, 'y' : currentY + 1})
	result += getValueInMatrix({'x' : currentX - 1, 'y' : currentY + 1})
	result += getValueInMatrix({'x' : currentX - 1, 'y' : currentY})
	result += getValueInMatrix({'x' : currentX - 1, 'y' : currentY - 1})
	result += getValueInMatrix({'x' : currentX, 'y' : currentY - 1})
	result += getValueInMatrix({'x' : currentX + 1, 'y' : currentY - 1})

	for val in adjacentValues:
		if val is not None:
			result += val

	return result


currentLocation = {'x' : 0, 'y' : 0}
currentDirection = RIGHT
currentManhattanDistance = 0
desiredManhattanDistance = 1

#keep track of the numbers in our spiralMatrix object in order to get the value for the next location
spiralMatrix = {frozenset({'x' : 0, 'y' : 0}.items()) : 1}

#build the spiral iteratively, starting from the inside out
while True:
	#first, move in the current direction
	print("Current Direction: ", currentDirection)
	currentLocation = move(currentLocation, currentDirection)
	print("Location: ", currentLocation)
	currentNumber = getCurrentValue(currentLocation)
	spiralMatrix[frozenset(currentLocation.items())] = currentNumber
	#then, calculate the distance
	currentManhattanDistance = abs(currentLocation['x']) + abs(currentLocation['y'])
	print("Number: ", currentNumber, ", Distance: ", currentManhattanDistance)
	#if it is greater than the puzzle input, print and exit
	if currentNumber > puzzleInput:
		print("Current Number: ", currentNumber)
		exit()
	#otherwise, is it the desired manhattan distance?
	if currentManhattanDistance == desiredManhattanDistance:
		#if so, re-orient yourself and recalculate the next desired distance. 
		currentDirection = (currentDirection+1)%4
		currentManhattanDistance = 0
		if currentDirection == RIGHT or currentDirection == UP:
			desiredManhattanDistance += 1

	print()


