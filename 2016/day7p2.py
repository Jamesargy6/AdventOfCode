import sys,operator, re




def hasABA(inputString, inBracket):
	result = []
	abas = []
	groups = re.finditer(r'(\w)(\w)\1', inputString)
	print([group.group(1) for group in groups])
	print(abas)
	if abas is not None:
			for a in abas:
				if a[0] != a[1]: 
					result.append(a)

	
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
			abasInBracket.append(aba)
			hasABAInBracket = True

	for uSet in unbracketedSets:
		uString = "".join(uSet)
		aba = hasABA(uString, True)
		if aba is not None:
			abasOutsideOfBracket.append(aba)
			hasABAOutsideOfBracket = True

	if(hasABAOutsideOfBracket and hasABAInBracket):
		print("INSIDE")
		print(*abasInBracket)
		print("OUTSIDE")
		print(*abasOutsideOfBracket)

		for outAba in abasOutsideOfBracket:
			for inAba in abasInBracket:
				if outAba[0] == inAba[1] and outAba[1] == inAba[0]:
					result +=1
					print("Result Total: " + str(result))

print("Result: " + str(result))

