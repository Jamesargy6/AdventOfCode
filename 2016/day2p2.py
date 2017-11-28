import sys

keypad = [[None,None,1,None,None],[None,2,3,4,None],[5,6,7,8,9],[None,"A","B","C",None],[None,None,"D",None,None]]
currentLocation = [0,2]
result = ""

mins = [2,1,0,1,2]
maxs = [2,3,4,3,2]



file = open("day2Input.txt", "r")
directions = file.read().split("\n")

for dLine in directions:
	for d in dLine:
		print("Current Location: ", currentLocation)
		print("Direction: ", d)
		if d == "U" and currentLocation[1] > mins[currentLocation[0]] :
			currentLocation[1] -= 1
		elif d == "R" and currentLocation[0] < maxs[currentLocation[1]] :
			currentLocation[0] += 1
		elif d == "D" and currentLocation[1] < maxs[currentLocation[0]] :
			currentLocation[1] += 1
		elif d == "L" and currentLocation[0] > mins[currentLocation[1]] :
			currentLocation[0] -= 1

	print("Keypad: ",keypad)
	print("Current Location: ",currentLocation)
	result += str(keypad[currentLocation[1]][currentLocation[0]])
	print("Interim Result: ", result)

print(result)



