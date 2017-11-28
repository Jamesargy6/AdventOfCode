import sys,operator, regex as re




def hasABA(inputString, inBracket):
	result = []
	groups = re.finditer(r'(\w)(\w)\1', inputString, overlapped=True)	
	if groups is not None:
			for g in groups:
				if g[0][0] != g[0][1]:
					result.append(g)
	print(result)
	return result


file = open("day7Input.txt", "r")
directions = file.read().split("\n")

result = 0

for d in directions:
	hasABAInBracket = False
	hasABAOutsideOfBracket = False
	bracketedSets = []
	unbracketedSets = [[]]
	abasInBracket = []
	abasOutsideOfBracket = []
	appendingMode = False
	index = 0
	for c in d:
		if c not in ("[","]"):
			if appendingMode:
				bracketedSets[index].append(c)
			else:
				unbracketedSets[index].append(c)
		if c == "[":
			appendingMode = True
			bracketedSets.append([])
		elif c == "]":
			index += 1
			appendingMode = False
			unbracketedSets.append([])

	print("Direction: " + d)

	for bSet in bracketedSets:
		bString = "".join(bSet)
		aba = hasABA(bString, True)
		if aba is not None:
			abasInBracket.extend(aba)
			hasABAInBracket = True

	for uSet in unbracketedSets:
		uString = "".join(uSet)
		aba = hasABA(uString, True)
		if aba is not None:
			abasOutsideOfBracket.extend(aba)
			hasABAOutsideOfBracket = True

	print("ABAS Outside of bracket: ", [aba for aba in abasOutsideOfBracket])
	print("ABAS Inside of bracket: ", [aba for aba in abasInBracket])

	foundMatchingPair = False
	if(hasABAOutsideOfBracket and hasABAInBracket):
		for outAba in abasOutsideOfBracket:
			for inAba in abasInBracket:
				if  not foundMatchingPair:
					print("OUT ABA: ", outAba[0][0], outAba[0][1])
					print("IN ABA: ", inAba[0][0], inAba[0][1])
					if outAba[0][0] == inAba[0][1] and outAba[0][1] == inAba[0][0]:
						result +=1
						print("Result Total: " + str(result))
						foundMatchingPair = True

print("Result: " + str(result))

