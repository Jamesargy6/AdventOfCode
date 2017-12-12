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

groups = []

for p in pMap:
	pArray = []
	pArray.append(p)
	pArray = pArray + pMap[p]
	print(pArray)
	groups.append(pArray)

for x in range(0,10):
	for g in groups:
		for p in g:
			for g2 in groups:
				if p in g2 and g != g2:
					groups.remove(g)
					groups.remove(g2)
					g = list(set(g + g2))

					groups.append(g)


print(len(groups))