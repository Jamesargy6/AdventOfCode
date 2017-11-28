import sys


file = open("day8Input.txt", "r")
directions = file.read().split("\n")

pixelMap = []
UNITS_WIDE = 50
UNITS_TALL = 6

def drawRect(xDimen, yDimen):
	for y in range(0, yDimen):
		for x in range(0, xDimen):
			pixelMap[y][x] = "#"

def shiftRight(rowNum, shiftAmount):
	for x in range(0, shiftAmount):
		lastChar = pixelMap[rowNum][0]
		currentChar = pixelMap[rowNum][1] 
		for y in range(1, UNITS_WIDE+1):
			currentChar = pixelMap[rowNum][(y)%UNITS_WIDE] 
			pixelMap[rowNum][(y)%UNITS_WIDE] = lastChar
			lastChar = currentChar

def shiftDown(colNum, shiftAmount):
	for x in range(0, shiftAmount):
		lastChar = pixelMap[0][colNum]
		currentChar = pixelMap[1][colNum] 
		for y in range(1, UNITS_TALL+1):
			currentChar = pixelMap[(y)%UNITS_TALL][colNum]
			pixelMap[(y)%UNITS_TALL][colNum] = lastChar
			lastChar = currentChar

def parseDirection(direction):
	directionParts = direction.split(" ")

	if directionParts[0] == "rect":
		rectDimensions = directionParts[1].split("x")
		xDimen = int(rectDimensions[0])
		yDimen = int(rectDimensions[1])
		print("Draw a rectangle ", xDimen, " units wide and ", yDimen, " units tall.")
		drawRect(xDimen, yDimen)
	elif directionParts[0] == "rotate":
		isShiftRight = False
		if directionParts[1] == "row":
			isShiftRight = True
		colOrRowNum = int(directionParts[2].split("=")[1])
		shiftAmount = int(directionParts[4])
		print("Shift all of the pixels in ", directionParts[1], colOrRowNum, shiftAmount, " units.")
		if isShiftRight:
			shiftRight(colOrRowNum, shiftAmount)
		else:
			shiftDown(colOrRowNum, shiftAmount)

def printPixelMap():
	for pRow in pixelMap:
		print(pRow)


#initialize the pixel map
for x in range(0,UNITS_TALL):
	pixelMap.append(["." for x in range(0,UNITS_WIDE)])

printPixelMap()


for d in directions:
	parseDirection(d)
	printPixelMap()

result = 0
for pRow in pixelMap:
	for char in pRow:
		if char == "#":
			result += 1

print("Result: ", result)

