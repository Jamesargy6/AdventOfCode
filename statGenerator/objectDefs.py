from operator import attrgetter


class Contestant(object):
    def __init__(self, id, contestantData):
        self.id = id
        self.name = contestantData['name']
        self.stars = contestantData['stars']
        self.score = contestantData['local_score']

        self.dayData = []

        for day in contestantData['completion_day_level']:
        	dayDatum = contestantData['completion_day_level'][day]
        	self.dayData.append(Day(day, dayDatum))

        self.dayData.sort(key=attrgetter('id'))


class Day(object):
	def __init__(self, id, dayData):
		self.id = id
		self.part1Time = dayData.get('1', "DNF")
		if self.part1Time != "DNF":
			self.part1Time = self.part1Time['get_star_ts']
		self.part2Time = dayData.get('2', "DNF")
		if self.part2Time != "DNF":
			self.part2Time = self.part2Time['get_star_ts']

