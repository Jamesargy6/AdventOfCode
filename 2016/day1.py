import sys

# 0 = North, 1 = East, 2 = South, 3 = West
face = 0
#positive is North/East
amountEastWest = 0
amountNorthSouth = 0

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

	if face == 0:
	    amountNorthSouth += amount
	elif face == 1:
	    amountEastWest += amount
	elif face == 2:
	    amountNorthSouth -= amount
	else:
	    amountEastWest -= amount

	print("Amount N/S: ", amountNorthSouth)
	print("Amount E/W: ", amountEastWest)

result = abs(amountEastWest) + abs(amountNorthSouth)

print(result)
