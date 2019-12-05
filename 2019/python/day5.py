from aoc_lib import file_utils
from aoc_lib import intcode


if __name__ == '__main__':
	instructions = file_utils.read_line_into_int_list('inputs/day5input.txt')
	part_1_input = [1]
	print('Part 1')
	program = intcode.IntcodeProgram(instructions[:], part_1_input)
	program.run()

	part_2_input = [5]
	print('Part 2')
	program = intcode.IntcodeProgram(instructions[:], part_2_input)
	program.run()


