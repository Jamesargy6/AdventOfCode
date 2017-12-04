import sys

file = open("input/day4input.txt", "r")
passphraseLines = file.read().split("\n")
validPhrases = 0
index = 0
for line in passphraseLines:
	isValidLine = True
	words = []
	for word in line.split():
		if ''.join(sorted(word)) in words:
			print("Line ", index, " invalid: ", ''.join(sorted(word)))
			isValidLine = False
			break
		else:
			words.append(''.join(sorted(word)))
	if isValidLine:
		print("Line ", index, " is valid: ", line)
		validPhrases += 1

print("number of valid phrases: ", validPhrases)


