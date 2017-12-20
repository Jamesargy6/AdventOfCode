import sys

file = open("../inputs/day18input.txt", "r")
directions = file.read().split("\n")



p0 = {'p':0}
p1 = {'p':1}
p0ss = []
p1ss = []
i0 = 0
i1 = 0
term0 = False
term1 = False

result = 0

def executeInstruction(bool, p, ss, ssOther, i, wait, res):
	d = directions[i]
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
			if dParts[2] not in p:
				p[dParts[2]] = 0
			amt = p[dParts[2]]


	if reg not in p and reg is not "1":
		p[reg] = 0

	recoveredVal = 0

	if ins == "snd":
		ss.append(p[reg])
		if bool == 1:
			res += 1
	elif ins == "set":
		p[reg] = amt
	elif ins == "add":
		p[reg] += amt
	elif ins == "mul":
		p[reg] *= amt
	elif ins == "mod":
		p[reg] %= amt
	elif ins == "rcv":
		if len(ssOther) > 0:
			p[reg] = ssOther[0]
			ssOther = ssOther[1:]
			wait = False
		else:
			wait = True
	elif ins == "jgz":
		if reg == "1" or p[reg] > 0:
			i += amt-1

	if not wait:
		i += 1
	return p, ss, ssOther, i, wait, res



while result < 1000000:
	if term0 and term1:
		print(result)
		exit()
	p0, p0ss, p1ss, i0, term0, result = executeInstruction(0, p0, p0ss, p1ss, i0, term0, result)
	p1, p1ss, p0ss, i1, term1, result = executeInstruction(1, p1, p1ss, p0ss, i1, term1, result)




