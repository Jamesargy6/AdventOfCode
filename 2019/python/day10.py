from aoc_lib import file_utils
from typing import Tuple, List, Dict
from collections import namedtuple
import operator
from math import sqrt

Coord = namedtuple('Coord', 'x y')

SlopeDist = namedtuple('SlopeDist', 'coord slope distance lr')

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
			distance = sqrt((x_diff**2)+(y_diff**2))
			if x_diff != 0:
				rise_run = y_diff / x_diff
				x = str(rise_run)
				if x_diff > 0:
					lr = '1R'
				else: 
					lr = '3L'
				if lr not in asteroids[ast]:
					asteroids[ast][lr+x] = [SlopeDist(other_ast, rise_run, distance, lr)]
				else:
					asteroids[ast][lr+x].append(SlopeDist(other_ast, rise_run, distance, lr))
			else:
				if y_diff > 0:
					x = '+inf'
					if x not in asteroids[ast]:
						asteroids[ast][x] = [SlopeDist(other_ast, 1000, distance, '0U')]
					else:
						asteroids[ast][x].append(SlopeDist(other_ast, 1000, distance, '0U'))
				else:
					x = '-inf'
					if x not in asteroids[ast]:
						asteroids[ast][x] = [SlopeDist(other_ast, -1000, distance, '2D')]
					else:
						asteroids[ast][x].append(SlopeDist(other_ast, -1000, distance, '2D'))

	asteroid_lens = {key:len(value) for (key, value) in asteroids.items()}
	station = max(asteroid_lens.items(), key=operator.itemgetter(1))[0]
	print(station, asteroid_lens[station])

	relative_to_station = []
	for slope_dict in asteroids[station]:
		relative_to_station.append(asteroids[station][slope_dict])

	relative_to_station = sorted(relative_to_station, key=lambda x: (x[0].lr, -x[0].slope, x[0].slope >= 0))
	for x in relative_to_station:
		x = sorted(x, key=lambda i: i.distance)

	destroyed = 0
	index = 0
	for x in range(200):
		print(relative_to_station[index])
		if len(relative_to_station[index]) > 0:
			gone = relative_to_station[index].pop()
			print(f'destroyed {x+1}: {gone}')
		index = (index+1)%len(relative_to_station)






			




