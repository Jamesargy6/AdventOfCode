from typing import List, Callable, Tuple
from dataclasses import dataclass
from enum import Enum, auto


class HaltException(Exception):
	pass

class InputException(Exception):
	pass

class ParameterType(Enum): 
	READ = auto()
	WRITE = auto()
	JUMP = auto()

@dataclass
class Instruction:
	op_code: int
	parameter_types: List[ParameterType]
	operation: Callable

class ProgramState(Enum): 
	IDLE = auto()
	RUNNING = auto()
	INPUT_WAIT = auto()
	HALTED = auto()

class IntcodeProgram:
	HALT_OPCODE = 99
	instruction_pointer: int
	input_pointer: int
	memory: List[int]
	inputs: List[int]
	output: List[int]
	state: ProgramState
	write: Callable

	def __init__(self, memory: List[int], inputs: List[int] = []):
		self.OP_CODES = {
			1: Instruction(1, [ParameterType.READ, ParameterType.READ, ParameterType.WRITE], self._add),
			2: Instruction(2, [ParameterType.READ, ParameterType.READ, ParameterType.WRITE], self._mul),
			3: Instruction(3, [ParameterType.WRITE], self._in),
			4: Instruction(4, [ParameterType.READ], self._out),
			5: Instruction(5, [ParameterType.READ, ParameterType.JUMP], self._jit),
			6: Instruction(6, [ParameterType.READ, ParameterType.JUMP], self._jif),
			7: Instruction(7, [ParameterType.READ, ParameterType.READ, ParameterType.WRITE], self._lt),
			8: Instruction(8, [ParameterType.READ, ParameterType.READ, ParameterType.WRITE], self._eq),
			99: Instruction(99, [], self._halt)
		}
		self.PARAM_MODES = {
			0: lambda i: self.memory[i],
			1: lambda i: i
		}

		self.WRITE_MODES = {
			0: self._write_to_memory
		}

		self.instruction_pointer = 0
		self.input_pointer = 0

		self.memory = memory
		self.inputs = inputs
		self.output = []
		self.state = ProgramState.IDLE

	def run(self) -> List[int]:
		self.state = ProgramState.RUNNING
		while self.state == ProgramState.RUNNING:
			instruction_code = self.memory[self.instruction_pointer]
			instruction, parameters = self.prepare_instruction(instruction_code)
			try:
				result = instruction.operation(*parameters)
			except HaltException as e:
				self.state = ProgramState.HALTED
			except InputException as e:
				self.state = ProgramState.INPUT_WAIT

	def prepare_instruction(self, ins_code: int) -> Tuple[int, List[int]]:
		op_code = ins_code % 100
		instruction = self.OP_CODES[op_code]
		parameter_code = ins_code // 100
		parameter_modes = [parameter_code // 10**p_count % 10 for p_count in range(len(instruction.parameter_types))]
		parameters = self.prepare_parameters(instruction, parameter_modes)
		return instruction, parameters

	def prepare_parameters(self, ins: Instruction, parameter_modes: List[int]) -> Tuple:
		parameters = []
		for i, pm in enumerate(parameter_modes):
			param_index = self.instruction_pointer+1+i
			param_type = ins.parameter_types[i]
			if param_type == ParameterType.WRITE:
					self.write = self.WRITE_MODES[pm]
					parameters.append(self.memory[param_index])
			else:
				parameters.append(self.PARAM_MODES[pm](self.memory[param_index]))
		return (*parameters, )


	def _add(self, ia: int, ib: int, ipos: int):
		self.write(ia + ib, ipos)
		self.instruction_pointer += 4

	def _mul(self, ia: int, ib: int, ipos: int):
		self.write(ia * ib, ipos)
		self.instruction_pointer += 4

	def _in(self, i: int):
		if len(self.inputs) > self.input_pointer:
			self.write(self.inputs[self.input_pointer], i)
			self.input_pointer += 1
			self.instruction_pointer += 2
		else:
			raise InputException()

	def _out(self, out: int):
		self.output.append(out)
		self.instruction_pointer += 2

	def _jit(self, ia: int, j: int):
		if ia > 0:
			self.instruction_pointer = j
			return
		self.instruction_pointer += 3

	def _jif(self, ia: int, j: int):
		if ia == 0:
			self.instruction_pointer = j
			return
		self.instruction_pointer += 3

	def _lt(self, ia: int, ib: int, ipos: int):
		value = 1 if ia < ib else 0
		self.write(value, ipos)
		self.instruction_pointer += 4

	def _eq(self, ia: int, ib: int, ipos: int):
		value = 1 if ia == ib else 0
		self.write(value, ipos)
		self.instruction_pointer += 4

	def _halt(self):
		raise HaltException()

	def _write_to_memory(self, value: int, index: int):
		self.memory[index] = value