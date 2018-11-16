import sys

#helper utility for determining whether this component is good to be used
def hasMatchingPin(component, pinMatch):
	return component['ports'][0] == pinMatch or component['ports'][1] == pinMatch

#recursive method to build the bridge and manage the max count
def addToBridge(component, matchingPin):
	#import global vars
	global runningCount
	global maxCount
	global usedStackIds
	global maxLength

	runningCount += component['sum']
	usedStackIds.append(component['compId'])
	if len(usedStackIds) >= maxLength:
		maxLength = len(usedStackIds)
		if runningCount > maxCount:
			maxCount = runningCount 

	pinMatch = 0
	if component['ports'][0]== matchingPin:
		pinMatch = component['ports'][1]
	else:
		pinMatch = component['ports'][0]
	#search for components which match the current open end
	for comp in components:
		if comp['compId'] not in usedStackIds and hasMatchingPin(comp, pinMatch):
			addToBridge(comp, pinMatch)
	runningCount -= component['sum']
	usedStackIds.pop()

file = open("../inputs/day24input.txt", "r")
directions = file.read().split("\n")

components = []
startingComponents = []

i = 0
for d in directions:
	pins = d.split("/")
	comp = {
		'compId' : i,
		'ports': [int(pins[0]),int(pins[1])],
			
		'sum' : int(pins[1]) + int(pins[0])
	}
	components.append(comp)
	if hasMatchingPin(comp, 0):
		startingComponents.append(comp)
	i+=1

#print(startingComponents)
runningCount = 0
usedStackIds = []
maxCount = 0
maxLength = 0
for start in startingComponents:
	addToBridge(start, 0)

print(maxCount)


