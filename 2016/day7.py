import sys,operator, re




def hasABBA(inputString, inBracket):
	regex = re.compile(r'(\w)(\w)\2\1')
	group = None
	if regex.search(inputString)is not None:
		group = regex.search(inputString).group()
	if group is not None and group[0] is not group[1]: 
		print("    Set with ABBA: " + inputString)
		print("    " + regex.search(inputString).group())
		if inBracket:
			print("    Found IN bracket")
		else:
			print("    Found OUTSIDE bracket")
		return True
	else:
		return False


file = open("day7Input.txt", "r")
directions = file.read().split("\n")

result = 0

for d in directions:
	hasABBAInBracket = False
	hasABBAOutsideOfBracket = False
	bracketedSets = []
	unbracketedSets = [[]]
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
		if hasABBA(bString, True):
			hasABBAInBracket = True


	for uSet in unbracketedSets:
		uString = "".join(uSet)
		if hasABBA(uString, False):
			hasABBAOutsideOfBracket = True

	if(hasABBAOutsideOfBracket and not hasABBAInBracket):
		result +=1
		print("Result Total: " + str(result))

print("Result: " + str(result))

