import sys

file = open("day3Input.txt", "r")
directions = file.read().split("\n")

validTriangles = 0
counter = 0

for d in directions:
	directions[counter] = d.split()
	counter +=1

numRows = counter
counter = 0
triCounter = 0

triangles = []

triangle = [0,0,0]

for bigCounter in range(0,3):
	while counter < numRows:
		triangle[triCounter] = directions[counter][bigCounter]
		triCounter +=1
		counter +=1
		if triCounter == 3:
			triCounter = 0
			triangles.append(triangle)
			triangle = [0,0,0]

	counter = 0
validTriangles = 0
counter = 0

for sides in triangles:
	for x in range(0,3):
		sides[x] = int(sides[x])
	sides.sort()

	if sides[2] < sides[1] + sides[0]:
		validTriangles +=1

	print(counter, ": ", sides, ", ", sides[2] < sides[1] + sides[0])	
	counter +=1

print(validTriangles)
