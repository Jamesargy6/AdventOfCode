import sys

file = open("../inputs/day18input.txt", "r")
directions = file.read().split("\n")

registerList = {}
soundStack = []
i = 0
while True:
	print("i: ",i)
	d = directions[i]
	print(d)
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

	print("ins: {0}, reg: {1}, amt: {2}".format(ins, reg, amt))

	if reg not in registerList:
		registerList[reg] = 0

	recoveredVal = 0

	if ins == "snd":
		soundStack.append(registerList[reg])
	elif ins == "set":
		registerList[reg] = amt
	elif ins == "add":
		registerList[reg] += amt
	elif ins == "mul":
		registerList[reg] *= amt
	elif ins == "mod":
		registerList[reg] %= amt
	elif ins == "rcv" and registerList[reg] != 0:
		print(soundStack)
		exit()
	elif ins == "jgz" and registerList[reg] > 0:
		i += amt-1

	i += 1

	print(registerList)




