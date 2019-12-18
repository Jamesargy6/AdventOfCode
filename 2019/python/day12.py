from aoc_lib import file_utils
import re
from collections import namedtuple
from typing import List
import copy


PLANET_REGEX = re.compile('<x=(-?[\d]+), y=(-?[\d]+), z=(-?[\d]+)>')


Vector3D = namedtuple('Vector3D', 'x y z')

class Planet:
	position: Vector3D
	velocity: Vector3D

	def __init__(self, pos: Vector3D):
		self.position = pos
		self.velocity = Vector3D(0,0,0)

	def apply_gravity(self):
		self.position = Vector3D(*tuple(sum(x) for x in zip(self.position, self.velocity)))

	def calculate_energy(self) -> int:
		pot = sum(map(abs, self.position))
		kin = sum(map(abs, self.velocity))
		return pot*kin

	def __eq__(self, other) -> bool:
		return self.position == other.position and self.velocity == other.velocity

def get_planet(raw_str: str) -> Planet:
	result = PLANET_REGEX.match(raw_str)
	x,y,z = map(int, result.group(1,2,3))

	return Planet(Vector3D(x,y,z))

def compare(x: int, y: int) -> int:
	comp = x-y
	return 1 if comp<0 else 0 if comp==0 else -1


def move_planets(planets: List[Planet]):
	for p1 in planets:
		for p2 in filter(lambda p: p != p1, planets):
			x_diff = compare(p1.position.x, p2.position.x)
			y_diff = compare(p1.position.y, p2.position.y)
			z_diff = compare(p1.position.z, p2.position.z)
			p1.velocity = Vector3D(*tuple(sum(x) for x in zip(p1.velocity, (x_diff, y_diff, z_diff))))
	list(map(lambda p: p.apply_gravity(), planets))

def are_planets_equal(planets: List[Planet], others: List[Planet]) -> bool:
	for i in range(len(planets)):
		if planets[i] != others[i]:
			return False
	return True

if __name__ == '__main__':
	inputs = file_utils.read_file_into_str_list('inputs/day12input.txt')

	original_planets = [get_planet(i) for i in inputs]

	part_1_planets = copy.deepcopy(original_planets)
	for s in range(1000):
		move_planets(part_1_planets)
	system_energy = sum(list(map(lambda p: p.calculate_energy(), part_1_planets)))
	print(f'Part 1: {system_energy}')
	
	part_2_planets = copy.deepcopy(original_planets)
	move_planets(part_2_planets)
	steps = 1
	while not are_planets_equal(part_2_planets, original_planets):
		move_planets(part_2_planets)
		steps += 1

	print(f'Part 2: {steps}')
