import sys

file = open("../inputs/day7input.txt", "r")

instructions = file.read().split("\n")

#initialize an array of programs, and a list of every parent-child relationship
childParentRelationships = []
programMap = []
programList = []
childList = []


for ins in instructions:
	parent = ins.split()[0]
	#if the program has children, note their relationship and add each child to its own list
	if ins.find("->") != -1:
		rawChildren = ins.split("->")[1]
		weight = ins[ins.find("(")+1:ins.find(")")]
		children = rawChildren.split(",")
		children = [x.strip(' ') for x in children]
		print("Parent {0} has the following children: {1}".format(parent, children))
		childParentRelationships.append({"parent" : parent, "children" : children})
		programMap[parent] = {"weight" : weight, "cumWeight" : 0}
		childList += children
	else:
		programMap.append({"program" : parent, "weight" : weight, "cumWeight" : weight})
	programList.append(parent)

#the difference between the parent and child sets is the solution
res = next(iter(set(programList).difference(set(childList))))
print(res)

#calculate the cumulative weights of each node
while programMap[res]["cumWeight"] == 0:
	for rel in childParentRelationships:
		