import sys, math


file = open("../inputs/day21input.txt", "r")
directions = file.read().split("\n")
iterations = 0

inputs = []
outputs = []


def printProgram(program):
	for pLine in program:
		print(" ".join(pLine))

def splitProgram(masterProgram):
	programPieces ={}
	programCount = 0
	if len(masterProgram)%3 == 0:
		y = 0
		while y < len(masterProgram):
			x = 0
			while x < len(masterProgram):
				if programCount not in programPieces:
					programPieces[programCount] = []
				programPieces[programCount].append(masterProgram[y][x:x+3])
				programPieces[programCount].append(masterProgram[y+1][x:x+3])
				programPieces[programCount].append(masterProgram[y+2][x:x+3])
				x += 3
			y += 3
	elif len(masterProgram)%2 == 0:
		y = 0
		while y < len(masterProgram):
			x = 0
			while x < len(masterProgram):
				if programCount not in programPieces:
					programPieces[programCount] = []
				programPieces[programCount].append(masterProgram[y][x:x+2])
				programPieces[programCount].append(masterProgram[y+1][x:x+2])
				x += 2
			y += 2
	return programPieces

def flipConfig(program, modulo):
	flipped = []
	if modulo == 3:
		flipped = [program[2], program[1], program[0]]
	elif modulo == 2:
		flipped = [program[1], program[0]]

	return flipped

def rotateConfig(program, modulo):
	rotated = None
	if modulo == 3:
		rotated = [['X','X','X'],['X','X','X'],['X','X','X']]
	elif modulo == 2:
		rotated = [['X','X'],['X','X']]

	for x in range(0,modulo):
		for y in range(0,modulo):
			rotated[x][y]= program[modulo-y-1][x]
	return rotated


def getProgramConfigs(program):
	configs = []
	if len(masterProgram)%3 == 0:
		modulo = 3
	elif len(masterProgram)%2 == 0:
		modulo = 2
	currentConfig = program
	for x in range(0,4):
		configs.append(currentConfig)
		configs.append(flipConfig(currentConfig, modulo))
		currentConfig = rotateConfig(currentConfig, modulo)





	return configs


for d in directions:
	input, output = d.split(" => ")
	inputLines = input.split("/")
	inputProg = []
	for line in inputLines:
		inputProg.append(list(line))
	inputs.append(inputProg)

	outputLines = output.split("/")
	outputProg = []
	for line in outputLines:
		outputProg.append(list(line))
	outputs.append(outputProg)


masterProgram = [['.','#','.'],
				['.','.','#'],
				['#','#','#']]


#for every iteration
while iterations <= 5:
	print("Iter: ",iterations)
	printProgram(masterProgram)
	newPieces = []
	#get each program piece
	programPieces = splitProgram(masterProgram)

	#for each piece, calculate its potential configurations
	for pPiece in programPieces:
		pieceConfigs = getProgramConfigs(programPieces[pPiece])



		for config in pieceConfigs:
			if config in inputs:
				newPieces.append(outputs[inputs.index(config)])
	
	#TODO stitch the pieces back together
	stitchGridSize = int(math.sqrt(len(newPieces)))
	newMaster = []
	
	currentMasterRow = 0
	for x in range(len(newPieces)):
		if newMaster == []:
			newMaster = newPieces[x]
		elif x%stitchGridSize != 0:
			for l in newPieces[x]:
				





	iterations += 1