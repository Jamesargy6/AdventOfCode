import sys

file = open("../inputs/day12input.txt", "r")
directions = file.read().split("\n")

pMap = {}
for d in directions:
	dParts = d.split("<->")

	currentVal = int(dParts[0].strip())
	if currentVal not in pMap:
		pMap[currentVal] = []

	rightSideVals = dParts[1].split(",")
	for v in rightSideVals:
		v = int(v.strip())
		if v not in pMap:
			pMap[v] = []
		if currentVal not in pMap[v]:	
			pMap[v].append(currentVal)
		if v not in pMap[currentVal]:
			pMap[currentVal].append(v)


currentLength = 0
while currentLength != len(pMap[0]):
	currentLength = len(pMap[0])
	for p in pMap:
		if p != 0:
			if p in pMap[0]:
				pMap[0] = list(set(pMap[0] + pMap[p]))
print(len(pMap[0]))

