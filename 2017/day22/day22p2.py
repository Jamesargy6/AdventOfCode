import sys


file = open("../inputs/day22input.txt", "r")
directions = file.read().split("\n")

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

infGrid = []

for x in range(1001):
	infGrid.append(['.']*1001)
infCenter = int((len(infGrid)-1)/2)

#initialize the grid, padding it
startGrid = []
for d in directions:
	startGrid.append(list(d))
startCenter = int((len(startGrid)-1)/2)


begin = infCenter - startCenter
end = infCenter + startCenter

i = 0
for x in range(begin, end+1):
	infGrid[x][begin:end+1] = startGrid[i]
	i += 1

	

currentNode = {"x" : int((len(infGrid)-1)/2), "y" : int((len(infGrid)-1)/2), "facing" : UP}


infectionCount = 0
for x in range(10000000):
	#determine orientation
	if infGrid[currentNode['y']][currentNode['x']] == '#':
		currentNode['facing'] = (currentNode['facing']+1)%4
	elif infGrid[currentNode['y']][currentNode['x']] == 'F':
		currentNode['facing'] = (currentNode['facing']+2)%4
	elif infGrid[currentNode['y']][currentNode['x']] == '.':
		currentNode['facing'] = (currentNode['facing']-1)%4
	else:
		pass


	#flip bit
	if infGrid[currentNode['y']][currentNode['x']] == '#':
		infGrid[currentNode['y']][currentNode['x']] = "F"
	elif infGrid[currentNode['y']][currentNode['x']] == "F":
		infGrid[currentNode['y']][currentNode['x']] = "."
	elif infGrid[currentNode['y']][currentNode['x']] == ".":
		infGrid[currentNode['y']][currentNode['x']] = "W"
	else:
		infGrid[currentNode['y']][currentNode['x']] = "#"
		infectionCount += 1

	#move
	#print(currentNode['facing'])
	if currentNode['facing'] == UP:
		currentNode['y'] -= 1
	elif currentNode['facing'] == RIGHT:
		currentNode['x'] += 1
	elif currentNode['facing'] == DOWN:
		currentNode['y'] += 1
	elif currentNode['facing'] == LEFT:
		currentNode['x'] -= 1

print(infectionCount)
