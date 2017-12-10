import sys

file = open("../inputs/day10input.txt", "r")

lengths = file.read().split(",")

llist = []
for x in range(0,256):
	llist.append(x)

llistLen = len(llist)

currentPos = 0
skipSize = 0

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
	print(llist)
	
print(llist[0]*llist[1])
