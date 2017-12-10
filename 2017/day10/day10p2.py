import sys, operator, functools

file = open("../inputs/day10input.txt", "r")

inputString = file.read()




lengths = []
for c in inputString:
	lengths.append(ord(c))

llist = []
for x in range(0,256):
	llist.append(x)

llistLen = len(llist)
lengths = lengths +[17, 31, 73, 47, 23]


llistLen = len(llist)
print(llistLen)
currentPos = 0
skipSize = 0

for r in range(0,64):
	for l in lengths:
		l = int(l)
		tempList = []
		for x in range(0,l):
			tempList.append(llist[(currentPos + x)%llistLen])
		tempList = tempList[::-1]
		for x in range(0,l):
			llist[(currentPos + x)%llistLen] = tempList[x]

		currentPos += (l + skipSize)%llistLen
		skipSize += 1

	
denseHash = []
currentIter = 0
subLists = []
for x in range(0,16):
	subLists.append(llist[(x*16):(x*16)+16])

for sl in subLists:
	denseHash.append(functools.reduce(operator.xor, sl))

print(denseHash)

hashResult = ""
for dh in denseHash:
	tempRes = hex(dh)[2:]
	if len(tempRes) == 1:
		tempRes = "0" + tempRes
	hashResult += tempRes

print(hashResult)
