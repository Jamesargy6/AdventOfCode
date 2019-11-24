from dataclasses import dataclass
from typing import List, Dict
import sys

@dataclass
class Rule:
    input: str
    output: str

PLANT = '#'
EMPTY = '.'


def parse_rule(rule_string: str) -> Rule:
    tokens = rule_string.split(' ')
    return Rule(tokens[0], tokens[2])


def pad_pot_map(pot_map: Dict[int, str]):
    leftmost_plant_index = min([pot_index for (pot_index, pot) in pot_map.items() if pot == PLANT])
    rightmost_plant_index = max([pot_index for (pot_index, pot) in pot_map.items() if pot == PLANT])

    for empty_pot_index in range(leftmost_plant_index-5, leftmost_plant_index):
        pot_map[empty_pot_index] = EMPTY
    for empty_pot_index in range(rightmost_plant_index+1, rightmost_plant_index+6):
        pot_map[empty_pot_index] = EMPTY


def perform_rules_on_pot(pot_map: Dict[int, str], pot_index, rules: List[Rule]) -> str:
    pots_to_match = ''.join([pot_map[i] for i in range(pot_index-2, pot_index+3)])
    for rule in rules:
        if pots_to_match == rule.input:
            return rule.output
    return EMPTY


def perform_generation(pot_map: Dict[int, str], rules: List[Rule]) -> Dict[int, str]:
    pad_pot_map(pot_map)
    leftmost_pot_index = min([pot_index for pot_index in pot_map.keys()])
    rightmost_pot_index = max([pot_index for pot_index in pot_map.keys()])
    new_pot_map: Dict[int, str] = {}
    for gen_index in range(leftmost_pot_index+2, rightmost_pot_index-1):
        new_pot_map[gen_index] = perform_rules_on_pot(pot_map, gen_index, rules)

    return new_pot_map


def get_plant_sum(pot_map: Dict[int, str]) -> int:
    return sum([pot_index for (pot_index, pot) in pot_map.items() if pot == PLANT])


if __name__ == '__main__':
    num_generations = int(sys.argv[1])
    inputs = open('./input.txt').read().split('\n')

    initial_state_string = inputs[0].split(' ')[2]
    pot_map = {pot_index: initial_state_string[pot_index] for pot_index in range(len(initial_state_string))}

    rules: List[Rule] = [parse_rule(input) for input in inputs[2:]]
    current_plants_sum, next_plants_sum = 0, 0
    current_plant_diff, stabilized_plant_diff = 0, 0
    for i in range(num_generations):
        pot_map = perform_generation(pot_map, rules)
        next_plants_sum = get_plant_sum(pot_map)
        current_plant_diff = next_plants_sum - current_plants_sum
        if i % 10 == 1:
            if stabilized_plant_diff == current_plant_diff:
                extrapolated_sum = current_plants_sum + (stabilized_plant_diff * (num_generations-i))
                print(extrapolated_sum)
                exit()
            stabilized_plant_diff = current_plant_diff
        current_plants_sum = next_plants_sum

    print(current_plants_sum)


