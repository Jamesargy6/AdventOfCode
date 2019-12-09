from aoc_lib import file_utils
from aoc_lib.intcode import IntcodeProgram

if __name__ == '__main__':
	raw_memory = file_utils.read_line_into_int_list('inputs/day9input.txt')

	program = IntcodeProgram(raw_memory[:], [1])
	program.run()
	print(f'Part 1: {program.output[-1]}')
	program = IntcodeProgram(raw_memory[:], [2])
	program.run()
	print(f'Part 2: {program.output[-1]}')

