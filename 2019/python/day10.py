from aoc_lib import file_utils
from typing import Tuple, List, Dict
from collections import namedtuple
import operator
from math import sqrt

Coord = namedtuple('Coord', 'x y')

SlopeDist = namedtuple('SlopeDist', 'coord slope distance')

if __name__ == '__main__':
	input_lines = file_utils.read_file_into_str_list('inputs/day10input.txt')

	asteroids: Dict[Coord, List[Tuple]] = {}
	length, width = 0,0
	for length, line in enumerate(input_lines):
		for width, coord in enumerate(list(line)):
			if coord == '#':
				asteroids[Coord(width,-length)] = {}


	for ast in asteroids.keys():
		for other_ast in asteroids.keys():
			if ast == other_ast:
				continue
			x_diff = other_ast.x - ast.x
			y_diff = other_ast.y - ast.y
			distance = sqrt((x_diff**2)*(y_diff**2))
			if x_diff != 0:
				rise_run = y_diff / x_diff
				x = str(rise_run)
				if x_diff > 0:
					x = 'L' + x
				else: 
					x = 'R' + x
				if x not in asteroids[ast]:
					asteroids[ast][x] = [SlopeDist(other_ast, rise_run, distance)]
				else:
					asteroids[ast][x].append(SlopeDist(other_ast, rise_run, distance))
			else:
				if y_diff > 0:
					x = '+inf'
					if x not in asteroids[ast]:
						asteroids[ast][x] = [SlopeDist(other_ast, 1000, distance)]
					else:
						asteroids[ast][x].append(SlopeDist(other_ast, 1000, distance))
				else:
					x = '-inf'
					if x not in asteroids[ast]:
						asteroids[ast][x] = [SlopeDist(other_ast, -1000, distance)]
					else:
						asteroids[ast][x].append(SlopeDist(other_ast, -1000, distance))

	asteroid_lens = {key:len(value) for (key, value) in asteroids.items()}
	station = max(asteroid_lens.items(), key=operator.itemgetter(1))[0]
	print(station, asteroid_lens[station])

	station_can_see = {key:sorted(value, key = lambda value: value.distance) for (key, value) in asteroids[station].items()}

	station_can_see = sorted(station_can_see.values(), key=lambda value: list(station_can_see.items())[0][1][0].slope)
	print(station, station_can_see)
	
	#destroyed = 0:
	
	#while destroyed < 200:



			




