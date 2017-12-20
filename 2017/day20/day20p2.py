import sys, re

file = open("../inputs/day20input.txt", "r")
directions = file.read().split("\n")

particles = {}
particleCount = 0
for d in directions:
	pRaw, vRaw, aRaw = re.findall(r'<[^>]*>', d) 

	p = [int(x) for x in re.sub('[<>]', '', pRaw).split(",")]
	v = [int(x) for x in re.sub('[<>]', '', vRaw).split(",")]
	a = [int(x) for x in re.sub('[<>]', '', aRaw).split(",")]

	particles[particleCount] = {'p' : p, 'v' : v, 'a' : a}
	particleCount += 1


for iter in range(1000):
	for d in particles:
		p = particles[d]['p']
		v = particles[d]['v']
		a = particles[d]['a']
		
		#first set up the velocities
		for i in range(len(v)):
			v[i] += a[i]

		#then set up the locations
		for i in range(len(p)):
			p[i] += v[i]

		particles[d] = {'p' : p, 'v' : v, 'a' : a}

	markForDelete = []
	for pos in particles:
		deleting = False
		checkVal = particles[pos]
		for pos2 in particles:
			if pos != pos2 and particles[pos]['p'] == particles[pos2]['p']:
				markForDelete.append(pos2)
				deleting = True

		if deleting:
			markForDelete.append(pos)
	for mark in markForDelete:
		if mark in particles:
			del particles[mark]





print(len(particles))