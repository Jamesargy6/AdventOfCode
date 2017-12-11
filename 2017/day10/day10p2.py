import sys, operator, functools

file = open("../inputs/day10input.txt", "r")

inputString = file.read()
#set up our list and input string
lengths = []
for c in inputString:
	lengths.append(ord(c))
llist = []
for x in range(0,256):
	llist.append(x)

lengths = lengths +[17, 31, 73, 47, 23]
llistLen = len(llist)
currentPos = 0
skipSize = 0

#iterate over the list 64 times
for r in range(0,64):
	for l in lengths:
		l = int(l)
		#tempList holds the initial sublist that needs to be reversed
		tempList = []
		for x in range(0,l):
			tempList.append(llist[(currentPos + x)%llistLen])
		#reverse it, and "put back" each item back at the appropriate index
		tempList = tempList[::-1]
		for x in range(0,l):
			llist[(currentPos + x)%llistLen] = tempList[x]

		#index logic
		currentPos += (l + skipSize)%llistLen
		skipSize += 1

#split the list into 16 arrays
subLists = []
for x in range(0,16):
	subLists.append(llist[(x*16):(x*16)+16])

#create the densh hash by xoring all of the values in each array
denseHash = []
for sl in subLists:
	denseHash.append(functools.reduce(operator.xor, sl))

#convert the hash to hex
hashResult = ""
for dh in denseHash:
	tempRes = hex(dh)[2:]
	if len(tempRes) == 1:
		tempRes = "0" + tempRes
	hashResult += tempRes

print(hashResult)
