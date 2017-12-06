import json
from operator import attrgetter
from objectDefs import *

#test approach
file = open("testData.json", "r")
rawData = file.read()

data = json.loads(rawData)
eventYear = int(data['event'])

def printContestantData(contestants):
	print("Current data for Advent of Code {}\n".format(eventYear))
	contestants.sort(key=attrgetter('score'), reverse=True)

	for contestant in contestants:
		print(" {0}: {1} points".format(contestant.name, contestant.score))
		for day in contestant.dayData:
			print("    Day {}:".format(day.id))
			print("      Part 1 completion time: {}".format(day.part1Time))
			print("      Part 2 completion time: {}".format(day.part2Time))


contestants = []

for member in data['members']:
	memberData = data['members'][member]
	contestants.append(Contestant(member, memberData))

printContestantData(contestants)