from aoc_lib import file_utils
from dataclasses import dataclass
from typing import List


OP_CODES = {
	1: add,
	2: mul,
	99: q
}

def add(a: int, b: int) -> int:
	return a+b

def mul(a: int, b: int) -> int:
	return a*b

def q(a: int, b:int):
	pass

def perform_op(instructions: List[int], index: int):
	op = op_codes[instructions[index]]
	a, b = instructions[instructions[index+1]], instructions[instructions[index+2]]
	if instructions[index] != 99:
		result = op(a,b)
		instructions[instructions[index+3]] = result
		return -1
	return instructions[0]



def run_program(instructions: List[int]) -> int:
	index = 0
	while True:
		result = perform_op(instructions, index)
		index += 4
		if result > 0:
			return result



def get_instructions(original_instructions: List[int], noun: int, verb: int) -> List[int]:
	new_ins = original_instructions[:]
	new_ins[1] = noun
	new_ins[2] = verb
	return new_ins


if __name__ == '__main__':
     original_instructions = read_line_into_int_list('inputs/day2input.txt')

     noun, verb = 12, 2

     part_1_ins = get_instructions(original_instructions, noun, verb)
     print(f'Part 1: {run_program(part_1_ins)}')

     desired_result = 19690720

     for noun in range(100):
     	for verb in range(100):
     		part_2_ins = get_instructions(original_instructions, noun, verb)
     		result = run_program(part_2_ins)
     		if result == desired_result:
     			print(f'Part 2: {(noun*100)+verb}')
     


     