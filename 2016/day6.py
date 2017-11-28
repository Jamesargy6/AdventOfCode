import sys,operator


file = open("day6Input.txt", "r")
directions = file.read().split("\n")
output = ""

inputDicts = [{},{},{},{},{},{},{},{}]

for d in directions:
	stringIndex = 0
	for c in d:
		if c in inputDicts[stringIndex]:
			inputDicts[stringIndex][c] += 1
		else:
			inputDicts[stringIndex][c] = 0

		stringIndex += 1

stringIndex = 0
for iDict in inputDicts:
	inputDicts[stringIndex] = sorted(iDict.items(), key=operator.itemgetter(1), reverse=False) #Part 2 just switch the last parameter here
	output += inputDicts[stringIndex][0][0]
	stringIndex += 1

print(output)
