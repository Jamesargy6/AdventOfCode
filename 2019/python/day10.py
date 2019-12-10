from aoc_lib import file_utils
from typing import Tuple, List, Dict
from collections import namedtuple


Coord = namedtuple('Coord', 'x y')

if __name__ == '__main__':
	input_lines = file_utils.read_file_into_str_list('inputs/day10input.txt')

	asteroids: Dict[Coord, List[Coord]] = {}
	length, width = 0,0
	for length, line in enumerate(input_lines):
		for width, coord in enumerate(list(line)):
			if coord == '#':
				asteroids[Coord(width+1,length+1)] = []


	for ast in asteroids.keys():
		for other_ast in asteroids.keys():
			x_diff = other_ast.x - ast.x
			y_diff = -other_ast.y - ast.y
			if x_diff != 0:
				rise_run = y_diff / x_diff
				x = str(rise_run)
				if x_diff > 0:
					x = 'R' + x
				else: 
					x = 'L' + x
				if x not in asteroids[ast]:
					print(ast, other_ast, x)
					asteroids[ast].append(x)

	inverse = [(value, key) for key, value in asteroids.items()]
	print(max(inverse)[1])
	print(asteroids[max(inverse)[1]])
	print(max(map(len, asteroids.values()))-1)
	print(len(asteroids[(5,8)]))
			




