import sys

file = open("../inputs/day4input.txt", "r")
passphraseLines = file.read().split("\n")
validPhrases = 0
index = 0
for line in passphraseLines:
	isValidLine = True
	words = []
	for word in line.split():
		#if the word is exists in this list, declare the line invalid. otherwise, add the word to the list and continue
		if word in words:
			print("Line ", index, " invalid: ", word)
			isValidLine = False
			break
		else:
			words.append(word)
	if isValidLine:
		print("Line ", index, " is valid: ", line)
		validPhrases += 1
	index += 1

print("number of valid phrases: ", validPhrases)


