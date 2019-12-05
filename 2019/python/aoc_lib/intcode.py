from typing import List, Callable, Tuple
from dataclasses import dataclass


@dataclass
class Instruction:
	op_code: int
	parameter_count: int
	operation: Callable


class IntcodeProgram:
	HALT_OPCODE = 99

	def __init__(self, memory: List[int], inputs: List[int] = []):
		self.OP_CODES = {
			1: Instruction(1, 3, self._add),
			2: Instruction(2, 3, self._mul),
			3: Instruction(3, 1, self._in),
			4: Instruction(4, 1, self._out),
			5: Instruction(5, 2, self._jit),
			6: Instruction(6, 2, self._jif),
			7: Instruction(7, 3, self._lt),
			8: Instruction(8, 3, self._eq),
			99: Instruction(99, 1, None)
		}
		self.PARAM_MODES = {
			0: lambda i: self.memory[i],
			1: lambda i: i
		}

		self.instruction_pointer = 0
		self.input_pointer = 0

		self.memory = memory
		self.inputs = inputs

	def _add(self, ia: int, ib: int, ipos: int, parameter_codes: List[int]):
		self.memory[ipos] = self.PARAM_MODES[parameter_codes[0]](ia) + self.PARAM_MODES[parameter_codes[1]](ib)
		self.instruction_pointer += 4

	def _mul(self, ia: int, ib: int, ipos: int, parameter_codes: List[int]):
		self.memory[ipos] = self.PARAM_MODES[parameter_codes[0]](ia) * self.PARAM_MODES[parameter_codes[1]](ib)
		self.instruction_pointer += 4

	def _in(self, i: int, _: List[int]):
		self.memory[i] = self.inputs[self.input_pointer]
		self.input_pointer += 1
		self.instruction_pointer += 2

	def _out(self, i: int, parameter_codes: List[int]):
		print(f'OUT: {self.PARAM_MODES[parameter_codes[0]](i)}')
		self.instruction_pointer += 2

	def _jit(self, ia: int, ib: int, parameter_codes: List[int]):
		if self.PARAM_MODES[parameter_codes[0]](ia) > 0:
			self.instruction_pointer = self.PARAM_MODES[parameter_codes[1]](ib)
			return
		self.instruction_pointer += 3

	def _jif(self, ia: int, ib: int, parameter_codes: List[int]):
		if self.PARAM_MODES[parameter_codes[0]](ia) == 0:
			self.instruction_pointer = self.PARAM_MODES[parameter_codes[1]](ib)
			return
		self.instruction_pointer += 3

	def _lt(self, ia: int, ib: int, ipos: int, parameter_codes: List[int]):
		value = 1 if self.PARAM_MODES[parameter_codes[0]](ia) < self.PARAM_MODES[parameter_codes[1]](ib) else 0
		self.memory[ipos] = value
		self.instruction_pointer += 4

	def _eq(self, ia: int, ib: int, ipos: int, parameter_codes: List[int]):
		value = 1 if self.PARAM_MODES[parameter_codes[0]](ia) == self.PARAM_MODES[parameter_codes[1]](ib) else 0
		self.memory[ipos] = value
		self.instruction_pointer += 4

	def run(self) -> List[int]:
		while True:
			instruction_code = self.memory[self.instruction_pointer]
			instruction, parameter_modes = self.parse_instruction_code(instruction_code)
			if instruction.op_code == self.HALT_OPCODE:
				break
			self.execute(instruction, parameter_modes)

		return self.memory

	def parse_instruction_code(self, ins_code: int) -> Tuple[int, List[int]]:
		op_code = ins_code % 100
		instruction = self.OP_CODES[op_code]

		parameter_code = ins_code // 100
		parameter_modes = [parameter_code // 10**p_count % 10 for p_count in range(instruction.parameter_count)]

		return instruction, parameter_modes

	def execute(self, ins: Instruction, parameter_modes: List[int]):
		parameters = self.get_parameters(ins.parameter_count)
		ins.operation(*parameters, parameter_modes)

	def get_parameters(self, parameter_count: int) -> Tuple:
		parameters = self.memory[self.instruction_pointer+1:self.instruction_pointer+1+parameter_count]
		return (*parameters, )
