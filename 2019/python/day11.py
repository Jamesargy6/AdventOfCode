from aoc_lib import file_utils
from aoc_lib.intcode import IntcodeProgram, ProgramState
from enum import Enum
from collections import namedtuple, defaultdict, OrderedDict
from typing import Dict, NewType
import time


Position = namedtuple('Position', 'x y')

Color = NewType('Color', str)

COLOR_DICT = {
	0: '.',
	1: '#'
}

class Direction(Enum): 
	NORTH = 0
	EAST = 1
	SOUTH = 2
	WEST = 3


class Robot:
	program: IntcodeProgram
	direction: Direction
	position: Position

	def __init__(self, program: IntcodeProgram, position: Position, direction: Direction):
		self.program = program
		self.direction = direction
		self.position = position
		self.MOVEMENT_DICT = {
			Direction.NORTH: (0, 1),
			Direction.EAST: (1, 0),
			Direction.SOUTH: (0, -1),
			Direction.WEST: (-1, 0)
		}

	def _move(self, turn_direction: int):
		turn = turn_direction if turn_direction == 1 else -1
		self.direction = Direction((self.direction.value + turn)%4)
		self.position = tuple(map(sum,zip(self.position,self.MOVEMENT_DICT[self.direction])))


	def run_program(self, starting_tile: int) -> Dict[Direction, int]:
		grid = defaultdict(int, {self.position: starting_tile})
		output_index = 0
		while self.program.state != ProgramState.HALTED:
			self.program.inputs.append(grid[self.position])
			self.program.run()
			while output_index < len(self.program.output):
				paint_color, turn_direction = tuple(self.program.output[output_index:output_index+2])
				grid[self.position] = paint_color
				self._move(turn_direction)
				output_index += 2
		return grid



def print_grid(grid: Dict[Direction, int]):
	positions = sorted(grid.keys())

	min_x, max_x = min(x for x, y in positions), max(x for x, y in positions)
	min_y, max_y = min(y for x, y in positions), max(y for x, y in positions)

	for y in reversed(range(min_y, max_y+1)):
		row = ''
		for x in range(min_x, max_x+1):
			if (x, y) not in grid:
				row += '.'
			else:
				row += COLOR_DICT[grid[(x,y)]]
		print(row)


if __name__ == '__main__':
	raw_memory = file_utils.read_line_into_int_list('inputs/day11input.txt')

	p1_program = IntcodeProgram(raw_memory.copy())
	p2_program = IntcodeProgram(raw_memory.copy())

	p1_robot = Robot(p1_program, (0,0), Direction.NORTH)
	part_1_grid = p1_robot.run_program(0)
	print(f'Part 1: {len(part_1_grid.keys())}')

	print('Part 2:')
	p2_robot = Robot(p2_program, (0,0), Direction.NORTH)
	part_2_grid = p2_robot.run_program(1)
	print_grid(part_2_grid)
	

