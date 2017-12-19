import sys

file = open("../inputs/day19input.txt", "r")
directions = file.read().split("\n")

opposites = {'-' : '|', '|' : '-'}

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

char = '|'
y = 0
x = directions[y].index(char)
going = SOUTH

result = ""
steps = 0
while True:
	steps += 1
	if going == NORTH:
		y -= 1
	elif going == EAST:
		x += 1
	elif going == SOUTH:
		y += 1
	elif going == WEST:
		x -= 1
	newChar = directions[y][x]
	if newChar == " ":
		result = result.replace("|", "")
		result = result.replace("-", "")
		print(steps)
		exit()

	if newChar == char or (char in opposites and newChar == opposites[char]):
		char = newChar
		continue
	elif newChar == "+":
		print(going, x, y, char)
		if going%2 == 0:
			print("go east or west")
			if x-1 >= 0:
				west = directions[y][x-1]
				print("west: ", west)
				if west not in [char, " "]:
					going = WEST
			if x+1 < len(directions[y]):
				east = directions[y][x+1]
				print("east: ", east)
				if east not in [char, " "]:
					going = EAST
		else:
			print("go north or south")
			if y-1 >= 0:
				north = directions[y-1][x]
				print("north: ", north)
				if north not in [char, " "]:
					going = NORTH
			if y+1 < len(directions):
				south = directions[y+1][x]
				print("south: ", south)
				if south not in [char, " "]:
					going = SOUTH
	else:
		result += newChar
	
	
	char = newChar

result = result.replace("|", "")
result = result.replace("-", "")
