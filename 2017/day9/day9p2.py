import sys

file = open("../inputs/day9input.txt", "r")

stream = file.read()

groupScore = 0
total = 0
inGarbage = False
skipNext = False
garbageChars = 0
currentGarbageStream = ""

for char in stream:

	if skipNext:
		skipNext = False
		continue


	if char == "!":
		skipNext = True
		continue

	if not inGarbage:
		if char == "{":
			groupScore += 1
			continue

		if char == "}":
			total += groupScore
			
			groupScore -= 1
			continue
	elif char != ">":
		currentGarbageStream += char
		garbageChars += 1

	if char == "<":
		inGarbage = True
		continue

	if char == ">":
		inGarbage = False
		print("Garbage Stream found: {}".format(currentGarbageStream))
		currentGarbageStream = ""

print(garbageChars)




