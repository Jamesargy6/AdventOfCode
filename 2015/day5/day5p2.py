import sys

file = open("../inputs/day5input.txt", "r")
directions = file.read().split("\n")


goodStrings = 0
for d in directions:
	#sandwish check
	hasSandwich = False
	for x in range(0, len(d)-2):
		if d[x] == d[x+2]:
			hasSandwich = True
	if not hasSandwich:
		continue

	#two pairs check
	#create array of all adjacent pairings
	pairings = []
	foundPairings = False
	for x in range(0, len(d)-1):
		pairings.append(d[x:x+2])
	for y in range(0, len(pairings)):
		pair = pairings[y]
		for z in range(0,len(pairings)):
			if abs(y-z) > 1 and pairings[z] == pair:
				print(d, pair)
				goodStrings += 1
				foundPairings = True
				break
		if foundPairings:
			break

	
print(str(goodStrings))

