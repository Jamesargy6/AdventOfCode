from aoc_lib import file_utils
from aoc_lib.intcode import IntcodeProgram, ProgramState
import itertools

if __name__ == '__main__':
	instructions = file_utils.read_line_into_int_list('inputs/day7input.txt')

	max_output = 0
	for perm in itertools.permutations(range(5)):
		amps = [IntcodeProgram(instructions[:], [perm[i]]) for i in range(len(perm))]
		amps[0].inputs.append(0)

		for amp_index in range(len(amps)):
			amps[amp_index].run()
			amps[(amp_index+1)%len(amps)].inputs.append(amps[amp_index].output[-1])
			

		if amps[-1].output[-1] > max_output:
			max_output = amps[-1].output[-1]
	print(f'Part 1: {max_output}')


	max_output = 0
	for perm in itertools.permutations(range(5,10)):
		amps = [IntcodeProgram(instructions[:], [perm[i]]) for i in range(len(perm))]
		amps[0].inputs.append(0)

		amp_index = 0
		current_amp = amps[amp_index]
		while not amps[-1].state == ProgramState.HALTED:
			current_amp = amps[amp_index]
			current_amp.run()
			next_amp_index = (amp_index + 1) % len(amps)
			next_amp = amps[next_amp_index]
			next_amp.inputs.append(current_amp.output[-1])
			amp_index = next_amp_index
		if amps[-1].output[-1] > max_output:
			max_output = amps[-1].output[-1]
	print(f'Part 2: {max_output}')