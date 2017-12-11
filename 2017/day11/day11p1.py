import sys
from operator import add

file = open("../inputs/day11input.txt", "r")

directions = file.read().split(",")

#we will use this to calculate our current coordinate afeter each iteration
directList = {'ne' : [1,0,-1],
				'se' : [1,-1,0],
				's' : [0,-1,1],
				'sw' : [-1,0,1],
				'nw' : [-1,1,0],
				'n' : [0,1,-1]
		}

currentCoord = [0,0,0]


#calculate the coordinate for each direction and print the result
for d in directions:
	currentCoord = [a + b for a, b in zip(currentCoord, directList[d])]
	print(currentCoord)