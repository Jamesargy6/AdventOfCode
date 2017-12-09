import sys

file = open("../inputs/day7input.txt", "r")

instructions = file.read().split("\n")

#initialize an array of programs, and a list of every parent-child relationship
childParentRelationships = {}
programMap = {}
programList = []
childList = []


for ins in instructions:
	parent = ins.split()[0]
	weight = int(ins[ins.find("(")+1:ins.find(")")])
	#if the program has children, note their relationship and add each child to its own list
	if ins.find("->") != -1:
		rawChildren = ins.split("->")[1]
		children = rawChildren.split(",")
		children = [x.strip(' ') for x in children]
		childParentRelationships[parent] = children
		programMap[parent] = {"weight" : weight, "cumWeight" : 0}
		childList += children
	else:
		programMap[parent] = {"weight" : weight, "cumWeight" : weight}
	programList.append(parent)

#the difference between the parent and child sets is the solution
root = next(iter(set(programList).difference(set(childList))))

#calculate the cumulative weights of each node
while programMap[root]["cumWeight"] == 0:
	for rel in childParentRelationships:
		runningTotalWeight = programMap[rel]["weight"]
		childrenComplete = True
		for child in childParentRelationships[rel]:
			if programMap[child]["cumWeight"] > 0:
				runningTotalWeight += programMap[child]["cumWeight"]
			else:
				childrenComplete = False

		if childrenComplete:
			programMap[rel]["cumWeight"] = runningTotalWeight


print(programMap)

#for each relationship, is the cumulative weight of each child the same? 
for rel in childParentRelationships:
	cumulativeWeights = []
	programs = []
	for child in childParentRelationships[rel]:
		cumulativeWeights.append(programMap[child]["cumWeight"])
		programs.append(programMap[child])
	#if not so, get the difference of the odd child's value plus/minus the difference in he cumulative values
	if len(set(cumulativeWeights)) > 1:
		print("Bad node Found!: ")
		for p in programs:
			print(p)


		