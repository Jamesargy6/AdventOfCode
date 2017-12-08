import sys

file = open("../inputs/day7input.txt", "r")

instructions = file.read().split("\n")

#initialize an array of programs, and a list of every parent-child relationship
childParentRelationships = []
programList = []
childList = []

for ins in instructions:
	parent = ins.split()[0]
	#if the program has children, note their relationship and add each child to its own list
	if ins.find("->") != -1:
		rawChildren = ins.split("->")[1]
		children = rawChildren.split(",")
		children = [x.strip(' ') for x in children]
		print("Parent {0} has the following children: {1}".format(parent, children))
		childParentRelationships.append({"parent" : parent, "children" : children})
		childList += children
	programList.append(parent)

#the difference between the parent and child sets is the solution
res = set(programList).difference(set(childList))
print(res)