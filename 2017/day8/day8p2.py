import sys

file = open("../inputs/day8input.txt", "r")

instructions = file.read().split("\n")


registers = {}
max = 0
for ins in instructions:
	insParts = ins.split()

	#split each line into its part	
	currentReg = insParts[0] 
	adding = insParts[1] == 'inc'
	amount = int(insParts[2])
	checkReg = insParts[4]
	compare = insParts[5]
	compareAmount = int(insParts[6])

	#make sure our registers are accounted for before using them
	if currentReg not in registers:
		registers[currentReg] = 0
	if checkReg not in registers:
		registers[checkReg] = 0

	#manually resolve the expression, and make the designated operation if True
	if True in {(compare == ">" and registers[checkReg] > compareAmount),
		(compare == ">=" and registers[checkReg] >= compareAmount), 
		(compare == "==" and registers[checkReg] == compareAmount),
		(compare == "!=" and registers[checkReg] != compareAmount),
		(compare == "<" and registers[checkReg] < compareAmount), 
		(compare == "<=" and registers[checkReg] <= compareAmount)} :
		if adding:
			registers[currentReg] += amount
		else:
			registers[currentReg] -= amount
		if registers[currentReg] > max:
			max = registers[currentReg]

print(max)