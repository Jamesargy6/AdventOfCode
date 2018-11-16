import sys

file = open("../inputs/day23input.txt", "r")
directions = file.read().split("\n")

registerList = {}
valueStack = []
mulUsed = 0
i = 0
while i < len(directions):
	d = directions[i]
	#print(d)
	#parse the instruction
	dParts = d.split(" ")
	ins = dParts[0]
	reg = dParts[1]
	amt = None
	toReg = None

	if len(dParts) > 2:
		try:
			amt = int(dParts[2])
		except(ValueError):
			if dParts[2] not in registerList:
				registerList[dParts[2]] = 0
			amt = registerList[dParts[2]]

	if reg not in registerList and reg is not "1":
		registerList[reg] = 0

	recoveredVal = 0

	if ins == "set":
		registerList[reg] = amt
	elif ins == "sub":
		registerList[reg] -= amt
	elif ins == "mul":
		registerList[reg] *= amt
		mulUsed += 1
	elif ins == "jnz":
		print("jump")
		if reg == "1" or registerList[reg] != 0:
			i += amt-1
			print("jump used")

	print("i: ", i, " ins: {0}, reg: {1}, amt: {2}".format(ins, reg, amt))
	print(registerList)
	i += 1

print(mulUsed)