import sys

file = open("day3Input.txt", "r")
directions = file.read().split("\n")

validTriangles = 0
counter = 0

for d in directions:
	sides = d.split()
	for x in range(0,3):
		sides[x] = int(sides[x])
	sides.sort()

	if sides[2] < sides[1] + sides[0]:
		validTriangles +=1

	print(counter, ": ", sides, ", ", sides[2] < sides[1] + sides[0])	
	counter +=1

print(validTriangles)