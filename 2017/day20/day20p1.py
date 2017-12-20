import sys, re

file = open("../inputs/day20input.txt", "r")
directions = file.read().split("\n")

ManhattanDistances = {}

particleCount = 0
for d in directions:
	pRaw, vRaw, aRaw = re.findall(r'<[^>]*>', d) 

	p = [int(x) for x in re.sub('[<>]', '', pRaw).split(",")]
	v = [int(x) for x in re.sub('[<>]', '', vRaw).split(",")]
	a = [int(x) for x in re.sub('[<>]', '', aRaw).split(",")]

	for iter in range(1000):
		#first set up the velocities
		for i in range(len(v)):
			v[i] += a[i]

		#then set up the locations
		for i in range(len(p)):
			p[i] += v[i]

	ManhattanDistances[particleCount] = abs(p[0]) + abs(p[1]) + abs(p[2])
	particleCount += 1


print(min(ManhattanDistances.items(), key=lambda x: x[1]) )