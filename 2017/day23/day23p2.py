import sys

file = open("../inputs/day23input.txt", "r")
directions = file.read().split("\n")

registerList = {'a' : 1}
valueStack = []
mulUsed = 0
i = 0
for x in range(200):
#while i < len(directions):
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

	#print("i: ", i+1, " ins: {0}, reg: {1}, amt: {2}".format(ins, reg, amt))
	if ins == "set":
		registerList[reg] = amt
	elif ins == "sub":
		registerList[reg] -= amt
	elif ins == "mul":
		registerList[reg] *= amt
		mulUsed += 1
	elif ins == "jnz":
		#print("jump")
		if reg == "1" or registerList[reg] != 0:
			i += amt-1
			#print("jump used")
	if i == 16:
		print("x: ", x, ", ", registerList)
	i += 1

print(registerList['h'])