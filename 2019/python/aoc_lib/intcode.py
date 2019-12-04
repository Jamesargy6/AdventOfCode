from typing import List, Callable, Tuple
from dataclasses import dataclass


@dataclass
class Instruction:
	parameter_count: int
	operation: Callable


class IntcodeProgram:
	HALT_OPCODE = 99

	def __init__(self, memory: List[int]):
		self.OP_CODES = {
			1: Instruction(3, self._add),
			2: Instruction(3, self._mul),
		}
		self.instruction_pointer = 0
		self.memory = memory

	def _add(self, ia: int, ib: int, ipos: int):
		self.memory[ipos] = self.memory[ia] + self.memory[ib]
		self.instruction_pointer += 4

	def _mul(self, ia: int, ib: int, ipos: int):
		self.memory[ipos] = self.memory[ia] * self.memory[ib]
		self.instruction_pointer += 4

	def run(self) -> List[int]:
		while True:
			op_code = self.memory[self.instruction_pointer]
			if op_code == self.HALT_OPCODE:
				break
			instruction = self.OP_CODES[self.memory[self.instruction_pointer]]
			self.execute(instruction)

		return self.memory

	def execute(self, ins: Instruction):
		if ins.parameter_count > 0:
			parameters = self.get_parameters(ins.parameter_count)
		ins.operation(*parameters)

	def get_parameters(self, parameter_count: int) -> Tuple:
		parameters = self.memory[self.instruction_pointer+1:self.instruction_pointer+1+parameter_count]
		return (*parameters, )
