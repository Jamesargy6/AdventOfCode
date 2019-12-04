from aoc_lib import file_utils
from typing import List


def to_power(tup) -> int:
	index, v = tup
	return v*(10**(5-index))

def get_positions(input: int) -> List[int]:
	positions: List[int] = []
	divisor = 100000
	while divisor > 0:
		test = 0
		if len(positions) > 0:
			test = sum(map(to_power, list(enumerate(positions))))
		value = (input - test)//divisor
		positions.append(value)
		divisor //= 10
	return positions

def is_increasing(positions: List[int]) -> bool:

	for i in range(0, len(positions)-1):
		if positions[i] > positions[i+1]:
			return False

	return True

def get_run_counts(positions: List[int]) -> bool:
	run_counts: List[int] = []
	current_val_count = 1
	current_val = positions[0]
	for x in positions[1:]:
		if x == current_val:
			current_val_count+=1
		else: 
			run_counts.append(current_val_count)
			current_val_count = 1
		current_val = x
	run_counts.append(current_val_count)
	return run_counts

if __name__ == '__main__':
	min_value = 265275
	max_value = 781584

	p1_passwords = 0
	p2_passwords = 0
	for x in range(min_value, max_value+1):
		positions = get_positions(x)
		if is_increasing(positions):
			run_counts = get_run_counts(positions)
			runs = list(filter(lambda x: x>1, run_counts))
			if len(runs) > 0:
				p1_passwords += 1
			runs_2 = list(filter(lambda x: x==2, run_counts))
			if len(runs_2) > 0:
				p2_passwords += 1

	print(f'Part 1: {p1_passwords}')
	print(f'Part 2: {p2_passwords}')