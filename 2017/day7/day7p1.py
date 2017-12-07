import sys

file = open("../inputs/day7input.txt", "r")

instructions = file.read().split("\n")

#initialize an array of programs, and a list of every parent-child relationship
childParentRelationships = []
programList = []
for ins in instructions:
	parent = ins.split()[0]
	#if it is not a top level program
	if ins.find("->") != -1:

		rawChildren = ins.split("->")[1]
		children = rawChildren.split(", ")
		print("Parent {0} has the following children: {1}".format(parent, children))
		childParentRelationships.append({"parent" : parent, "children" : children})
	programList.append(parent)

#iterate through relationships. add all unique children to a new set
children = []
for rel in childParentRelationships:
	print(rel["children"])
	for c in  rel["children"]:
		print("Child to be added: ", c)
		children.append(c.strip())
		print(children)

res = set(programList).difference(set(children))

print(res)



#the difference between the parent and child sets is the solution