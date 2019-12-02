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
    masses = [int(line.rstrip('\n')) for line in open('../inputs/day1input.txt')]

    total_module_fuel = sum(calculate_fuel(mass) for mass in masses)
    print(f'Part 1: {total_module_fuel}')

    total_fuel = sum(calculate_total_fuel_for_module(mass) for mass in masses)
    print(f'Part 2: {total_fuel}')