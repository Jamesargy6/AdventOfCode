import sys

keypad = [[1,2,3],[4,5,6],[7,8,9]]
currentLocation = [1,1]
result = ""

file = open("day2Input.txt", "r")
directions = file.read().split("\n")

for dLine in directions:
	for d in dLine:
		print("Current Location: ", currentLocation)
		print("Direction: ", d)
		if d == "U" and currentLocation[1] >0:
			currentLocation[1] -= 1
		elif d == "R" and currentLocation[0] <2:
			currentLocation[0] += 1
		elif d == "D" and currentLocation[1] <2:
			currentLocation[1] += 1
		elif d == "L" and currentLocation[0] >0:
			currentLocation[0] -= 1

	print("Keypad: ",keypad)
	print("Current Location: ",currentLocation)
	result += str(keypad[currentLocation[1]][currentLocation[0]])

print(result)



