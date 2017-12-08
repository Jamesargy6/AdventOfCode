import sys

file = open("../inputs/day8input.txt", "r")

instructions = file.read().split("\n")


registers = {}
maxReg = 0
for ins in instructions:
	insParts = ins.split()
	
	currentReg = insParts[0] 
	adding = insParts[1] == 'inc'
	amount = int(insParts[2])
	checkReg = insParts[4]
	compare = insParts[5]
	compareAmount = int(insParts[6])

	if currentReg not in registers:
		registers[currentReg] = 0
	if checkReg not in registers:
		registers[checkReg] = 0

	if (compare == ">" and registers[checkReg] > compareAmount) or (compare == ">=" and registers[checkReg] >= compareAmount) or (compare == "==" and registers[checkReg] == compareAmount) or (compare == "!=" and registers[checkReg] != compareAmount) or (compare == "<" and registers[checkReg] < compareAmount) or (compare == "<=" and registers[checkReg] <= compareAmount):
		if adding:
			registers[currentReg] += amount
		else:
			registers[currentReg] -= amount
		if registers[currentReg] > maxReg:
			maxReg = registers[currentReg]

print(maxReg)