from aoc_lib import file_utils
from aoc_lib import intcode
from typing import List


def get_instructions(original_ins: List[int], noun: int, verb: int) -> List[int]:
	new_ins = original_ins[:]
	new_ins[1] = noun
	new_ins[2] = verb
	return new_ins


if __name__ == '__main__':
	original_instructions = file_utils.read_line_into_int_list('inputs/day2input.txt')

	part_1_ins = get_instructions(original_instructions, 12, 2)
	part_1_program = intcode.IntcodeProgram(part_1_ins)
	part_1_program.run()
	print(f'Part 1: {part_1_program.run()[0]}')

	desired_result = 19690720
	for noun in range(100):
		for verb in range(100):
			part_2_ins = get_instructions(original_instructions, noun, verb)
			part_2_program = intcode.IntcodeProgram(part_2_ins)
			result = part_2_program.run()[0]
			if result == desired_result:
				print(f'Part 2: {(noun*100)+verb}')
