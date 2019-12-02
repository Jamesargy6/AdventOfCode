from aoc_lib import file_utils

def calculate_fuel(mass: int) -> int:
	return (mass//3)-2

def calculate_fuel_for_fuel(current_fuel: int) -> int:
	fuel = max(calculate_fuel(current_fuel), 0)
	if fuel == 0:
		return fuel
	return fuel + calculate_fuel_for_fuel(fuel)

def calculate_total_fuel_for_module(mass: int) -> int:
	module_fuel = calculate_fuel(mass)
	return module_fuel + calculate_fuel_for_fuel(module_fuel)

if __name__ == '__main__':
    masses = file_utils.read_file_into_int_list('inputs/day1input.txt')

    total_module_fuel = sum(map(calculate_fuel, masses))
    print(f'Part 1: {total_module_fuel}')

    total_fuel = sum(map(calculate_total_fuel_for_module, masses))
    print(f'Part 2: {total_fuel}')