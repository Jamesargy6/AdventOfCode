import sys

file = open("../inputs/day9input.txt", "r")

stream = file.read()

groupScore = 0
total = 0
inGarbage = False
skipNext = False


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
			print("Group level {} added".format(groupScore))
			groupScore -= 1
			continue

	if char == "<":
		inGarbage = True
		continue

	if char == ">":
		inGarbage = False

print(total)




