import sys

file = open("../inputs/day7input.txt", "r")

instructions = file.read().split("\n")

#initialize an array of programs, and a list of every parent-child relationship
childParentRelationships = {}
programList = []
comlpetedPrograms = []
#array of weights mapped to programs
weights = {}
for ins in instructions:
	parent = ins.split()[0].strip()
	#if it is not a top level program
	if ins.find("->") != -1:

		rawChildren = ins.split("->")[1]
		children = rawChildren.split(", ")
		#print("Parent {0} has the following children: {1}".format(parent, children))
		childParentRelationships[parent] = children
	else:
		weights[parent] = ins[ins.find("(")+1:ins.find(")")]
		comlpetedPrograms.append(parent)
	programList.append(parent)

#iterate through relationships. add all unique children to a new set
#print(childParentRelationships)
children = []
for chs in childParentRelationships:
	#print(rel["children"])
	for c in  chs:
		#print("Child to be added: ", c)
		children.append(c.strip())
		#print(children)

root = set(programList).difference(set(children))

#print(root)

for p in programList:
	if not p in comlpetedPrograms:
		weights[p.strip()] = 0

print(len(weights))
for parent in programList:
	print("Parent: {}".format(parent))
	if parent not in comlpetedPrograms:
		childrenToAdd = childParentRelationships[parent]
		eligibleForCompletion = True
		potentialWeight = 0
		for child in childrenToAdd:
			print("Child: {0}, weight: {1}, complete: {2}".format(child ,weights[child.strip()],child in comlpetedPrograms))
			if(child in comlpetedPrograms):
				potentialWeight += int(weights[child.strip()])
			else:
				eligibleForCompletion = False
		if eligibleForCompletion:
			weights[parent] = potentialWeight
			comlpetedPrograms.append(parent)





#the difference between the parent and child sets is the solution