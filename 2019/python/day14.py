from aoc_lib import file_utils
from typing import List, Dict
from dataclasses import dataclass
from collections import Counter, defaultdict
from math import gcd


ORE = 10**12
 
class ReactionError(Exception):
	pass


@dataclass
class Reactant:
	chemical: str
	amount: int

@dataclass
class Reaction:
	inputs: List[Reactant]
	result: Reactant

def get_reaction(raw_reaction: str) -> Reaction:
	raw_inputs, raw_result = raw_reaction.split(' => ')
	raw_inputs = raw_inputs.split(', ')

	raw_result = raw_result.split(' ')
	inputs = [Reactant(chemical, int(amount)) for amount, chemical in list(map(lambda x: x.split(' '), raw_inputs))]
	result = Reactant(raw_result[1], int(raw_result[0]))
	return Reaction(inputs, result)

class Reactor:
	reactor: List[Reaction]
	chemicals_made: Dict[str, int]
	chemicals_used: Dict[str, int]

	def __init__(self, reactions: List[Reaction]):
		self.reactions = reactions
		self.chemicals_made = defaultdict(int)
		self.chemicals_used = defaultdict(int)
		self.ore = ORE

	def react_for_chemical(self, chemical: str) -> Dict[str, int]:
		desired_reaction = self._get_reaction_by_chemical(chemical)
		desired_result = desired_reaction.result
		for reactant in desired_reaction.inputs:
			while self.chemicals_made[reactant.chemical] < reactant.amount:
				if reactant.chemical == 'ORE':
					self.chemicals_made[reactant.chemical] += reactant.amount
					self.ore -= reactant.amount
					if self.ore < 0:
						raise ReactionError
				else:
					self.react_for_chemical(reactant.chemical)
			self.chemicals_made[reactant.chemical] -= reactant.amount
			self.chemicals_used[reactant.chemical] += reactant.amount

		self.chemicals_made[desired_result.chemical] += desired_result.amount
		return self.chemicals_made

	def _get_reaction_by_chemical(self, chemical: str) -> Reaction:
		return list(filter(lambda x: x.result.chemical == chemical, self.reactions))[0]

if __name__ == '__main__':
	input_lines = file_utils.read_file_into_str_list('inputs/day14input.txt')

	reactions = [get_reaction(line) for line in input_lines]
	
	reactor = Reactor(reactions)

	reactor.react_for_chemical('FUEL')

	print(f'Part 1: {reactor.chemicals_used["ORE"]}')
