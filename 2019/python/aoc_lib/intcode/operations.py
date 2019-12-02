from typing import List, Callable



OP_CODES = {
	1: Add,
	2: Mul,
	99: Quit
}

class Instruction:
	opcode: int
	operation: Callable
	parameter_count: int

class Add(Instruction):
	def __init__(self):
		self.opcode = 1
		self.operation: lambda a, b: a+b
		self.parameter_count = 3

class Mul(Instruction):
	def __init__(self):
		self.opcode = 1
		self.operation: lambda a, b: a*b
		self.parameter_count = 3

class Quit(Instruction):
	def __init__(self):
		self.opcode = 1
		self.operation: pass
		self.parameter_count = 0

class IntcodeProgram:
	def __init__(self, memory: List[int]):
		self.instruction_pointer = 0
		self.memory = memory

	def run():
		while True:
			instruction = OP_CODES[self.memory[self.instruction_pointer]]()
			if instruction.parameter_count > 0:
				parameters = *self.memory[self.instruction_pointer+1:self.instruction_pointer+2+instruction.parameter_count]
			instruction.operation(parameters)


