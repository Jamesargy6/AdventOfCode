from aoc_lib import file_utils
from aoc_lib import intcode


if __name__ == '__main__':
	instructions = file_utils.read_line_into_int_list('inputs/day5input.txt')
	part_1_input = [1]
	program = intcode.IntcodeProgram(instructions[:], part_1_input)
	program.run()
	print(f'Part 1: {program.output[-1]}')

	part_2_input = [5]
	program = intcode.IntcodeProgram(instructions[:], part_2_input)
	program.run()
	print(f'Part 2: {program.output[-1]}')


