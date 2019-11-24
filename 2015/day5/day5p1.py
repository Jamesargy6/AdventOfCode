import sys

file = open("../inputs/day5input.txt", "r")
directions = file.read().split("\n")

vowels = ["a","e","i","o","u"]
badStrings = ["ab", "cd", "pq", "xy"]

goodStrings = 0
for d in directions:
	#bad string check
	hasBadString = False
	for bs in badStrings:
		if bs in d:
			hasBadString = True
	if hasBadString:
		continue
	#double check
	hasDouble = False
	for x in range(0, len(d)-1):
		if d[x] == d[x+1]:
			hasDouble = True
	if not hasDouble:
		continue
	#vowel check
	numVowels = 0
	for v in vowels:
		numVowels += d.count(v)

	if numVowels < 3:
		continue

	goodStrings += 1
	
print(str(goodStrings))

