import sys

file = open("../inputs/day9input.txt", "r")

stream = file.read()

groupScore = 0
total = 0
inGarbage = False
skipNext = False
garbageChars = 0

for char in stream:

	#control for handling cancelled characters
	if skipNext:
		skipNext = False
		continue
	if char == "!":
		skipNext = True
		continue

	#if we're not in garbage, execute the group logic
	if not inGarbage:
		if char == "{":
			groupScore += 1
		elif char == "}":
			total += groupScore
			groupScore -= 1
	#account for garbage chars
	elif char != ">":
		garbageChars += 1

	#handle entering and exiting garbage blocks
	if char == "<":
		inGarbage = True
	elif char == ">":
		inGarbage = False

print(garbageChars)