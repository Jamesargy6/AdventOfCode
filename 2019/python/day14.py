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

	def clear_chemicals(self):
		self.chemicals_made = defaultdict(int)
		self.chemicals_used = defaultdict(int)
		self.ore = ORE



def get_cycle_length(reactor: Reactor) -> int:
	cycles = 0

	cycle_lengths ={}
	while True:
		try:
			cycles += 1
			reactor.react_for_chemical('FUEL')
			cycle_chemicals = dict(filter(lambda elem: elem[1] == 0, reactor.chemicals_made.items())).keys()
			for cycle_chem in cycle_chemicals:
				if cycle_chem not in cycle_lengths:
					cycle_lengths[cycle_chem] = cycles
			if len(cycle_lengths) >= len(reactor.chemicals_made)-1:
				break

		except ReactionError:
			print(f'Part 2: {reactor.chemicals_made["FUEL"]}')
			exit()
	cycle_values = list(cycle_lengths.values())
	cycles_to_empty = cycle_values[0]
	for i in cycle_values[1:]:
		cycles_to_empty = cycles_to_empty*i//gcd(cycles_to_empty, i)

	return cycles_to_empty


if __name__ == '__main__':
	input_lines = file_utils.read_file_into_str_list('inputs/day14input.txt')

	reactions = [get_reaction(line) for line in input_lines]
	
	reactor = Reactor(reactions)

	reactor.react_for_chemical('FUEL')

	print(f'Part 1: {reactor.chemicals_used["ORE"]}')

	reactor.clear_chemicals()
	cycle_length = get_cycle_length(reactor)

	reactor.clear_chemicals()

	reactor.react_for_chemical('FUEL')
	ore_reactions = []
	for reaction in reactions:
		for reactant in reaction.inputs:
			if 'ORE' == reactant.chemical:
				ore_reactions.append(reaction)

	ore_amounts_used = {chemical:amount_used for (chemical,amount_used) in 
		dict(filter(lambda elem: elem[0] in [reaction.result.chemical for reaction in ore_reactions], reactor.chemicals_used.items())).items()
	}
	
	ore_amounts_used_in_cycle = dict(map(lambda elem: (elem[0], elem[1]*cycle_length), ore_amounts_used.items()))
	
	
	print(ore_amounts_used_in_cycle, cycle_length)

	ore_used_in_cycle = 0
	for chemical, amount in ore_amounts_used_in_cycle.items():
		ore_reaction = reactor._get_reaction_by_chemical(chemical)
		ore_used_in_cycle += (amount//ore_reaction.result.amount)*ore_reaction.inputs[0].amount


	reactor.clear_chemicals()
	
	reactor.chemicals_made["FUEL"] = (reactor.ore//ore_used_in_cycle)*cycle_length
	reactor.ore =  reactor.ore - (ore_used_in_cycle*reactor.chemicals_made["FUEL"])

	while True:
		try:
			reactor.react_for_chemical('FUEL')
		except ReactionError:
			print(f'Part 2: {reactor.chemicals_made["FUEL"]}')
			exit()


