import sys

# 0 = North, 1 = East, 2 = South, 3 = West
face = 0
visited = [[0,0]]
currentLocation = [0,0]

file = open("day1Input.txt", "r")

directions = file.read().split(",")

for d in directions:
	d = d.strip()
	print("Direction: ", d, ", Face: ", face)
	turn = d[0]
	if turn == "L":
		face -= 1
		if face == -1:
			face = 3
	else:
		face +=1
		if face == 4:
			face = 0

	amount = int(d[1:])

	currentAdds = []

	while amount > 0:
		if face == 0:
		    currentLocation = [currentLocation[0]+1, currentLocation[1]]
		    currentAdds.append(currentLocation)
		elif face == 1:
		    currentLocation = [currentLocation[0], currentLocation[1]+1]
		    currentAdds.append(currentLocation)
		elif face == 2:
		    currentLocation = [currentLocation[0]-1, currentLocation[1]]
		    currentAdds.append(currentLocation)
		else:
		    currentLocation = [currentLocation[0], currentLocation[1]-1]
		    currentAdds.append(currentLocation)
		amount -=1




	for add in currentAdds:
		for v in visited:
			if add == v:
				print("RESULT: ", abs(add[0] + abs(add[1])))
				sys.exit()
		visited.append(add)


	print("Current Location", currentLocation)


print("Visited", visited)

